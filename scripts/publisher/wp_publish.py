"""WordPress publisher for content-factory.

Reads a generated blog .md file from project-XXX/output/, converts the
markdown body into Gutenberg-block HTML, and publishes (or drafts) to
zoopa.es via the WP REST API.

Usage:
  python3 _system/publisher/wp_publish.py \
      --file project_XXX/output/blog.md \
      --lang es \
      --categories 2245,2235 \
      --status draft

Env vars required:
  WP_USER, WP_APP_PASSWORD, WP_SITE (defaults to https://zoopa.es)
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

try:
    import requests
except ImportError:
    print("Falta requests. Instala con: python3 -m pip install requests", file=sys.stderr)
    sys.exit(1)


def env(name: str, default: str | None = None) -> str:
    v = os.environ.get(name, default)
    if not v:
        print(f"ERROR: variable de entorno {name} no definida", file=sys.stderr)
        sys.exit(1)
    return v


def parse_metadata(text: str) -> tuple[dict, str]:
    """Extract leading <!-- SEO metadata ... --> block."""
    m = re.match(r"\s*<!--\s*\n?(.+?)\n?-->\s*\n", text, flags=re.DOTALL)
    meta: dict[str, str] = {}
    rest = text
    if m:
        block = m.group(1)
        rest = text[m.end():]
        for line in block.splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip().lower()] = v.strip()
    return meta, rest


def md_to_gutenberg(md: str) -> tuple[str, str]:
    """Convert markdown body to Gutenberg-block HTML.

    Returns (title, content_html). The H1 is extracted as title.
    Figure blocks whose src contains 'placeholder' are skipped — they're
    documentation-only references that should not appear in published content.
    """
    md = re.sub(
        r"<figure[^>]*>\s*<img[^>]*placeholder[^>]*/?>\s*(?:<figcaption[^>]*>.*?</figcaption>\s*)?</figure>\s*",
        "",
        md,
        flags=re.DOTALL | re.IGNORECASE,
    )
    lines = md.split("\n")
    title = ""
    body_lines: list[str] = []

    in_html_block = False
    html_buffer: list[str] = []
    paragraph_buffer: list[str] = []

    out_blocks: list[str] = []

    def flush_paragraph():
        if not paragraph_buffer:
            return
        text = " ".join(paragraph_buffer).strip()
        paragraph_buffer.clear()
        if not text:
            return
        text = inline_md(text)
        out_blocks.append(f"<!-- wp:paragraph -->\n<p>{text}</p>\n<!-- /wp:paragraph -->")

    def flush_html():
        if not html_buffer:
            return
        chunk = "\n".join(html_buffer).strip()
        html_buffer.clear()
        if not chunk:
            return
        out_blocks.append(f"<!-- wp:html -->\n{chunk}\n<!-- /wp:html -->")

    for raw in lines:
        line = raw.rstrip()

        if not title and line.startswith("# "):
            title = line[2:].strip()
            continue

        if line.startswith("<figure") or line.startswith("<div ") or line.startswith("<hr "):
            flush_paragraph()
            in_html_block = True
            html_buffer.append(raw)
            continue

        if in_html_block:
            html_buffer.append(raw)
            if line == "</figure>" or line == "</div>" or line.startswith("<hr ") and line.endswith("/>"):
                if line == "</figure>" or line == "</div>":
                    in_html_block = False
                    flush_html()
            elif line.startswith("<hr "):
                in_html_block = False
                flush_html()
            continue

        h_match = re.match(r"^(#{2,6})\s+(.+)$", line)
        if h_match:
            flush_paragraph()
            level = len(h_match.group(1))
            heading_text = inline_md(h_match.group(2).strip())
            attrs = "" if level == 2 else f' {{"level":{level}}}'
            out_blocks.append(
                f"<!-- wp:heading{attrs} -->\n<h{level}>{heading_text}</h{level}>\n<!-- /wp:heading -->"
            )
            continue

        if line.lstrip().startswith("<h2") or line.lstrip().startswith("<h3"):
            flush_paragraph()
            in_html_block = True
            html_buffer.append(raw)
            if "</h2>" in line or "</h3>" in line:
                in_html_block = False
                flush_html()
            continue

        if line.startswith("*") and line.endswith("*") and not line.startswith("**"):
            flush_paragraph()
            text = inline_md(line)
            out_blocks.append(f"<!-- wp:paragraph -->\n<p>{text}</p>\n<!-- /wp:paragraph -->")
            continue

        if line == "":
            flush_paragraph()
            continue

        paragraph_buffer.append(line)

    flush_paragraph()
    flush_html()
    return title, "\n\n".join(out_blocks)


def inline_md(text: str) -> str:
    """Convert markdown inline emphasis to HTML."""
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    return text


def upload_image(site: str, auth: tuple[str, str], path: Path, alt: str) -> int | None:
    """Upload an image to WP media library. Returns media ID or None."""
    if not path.exists():
        return None
    url = f"{site}/wp-json/wp/v2/media"
    with path.open("rb") as f:
        files = {"file": (path.name, f, "image/jpeg" if path.suffix.lower() in {".jpg", ".jpeg"} else "image/png")}
        data = {"alt_text": alt}
        r = requests.post(url, auth=auth, files=files, data=data, timeout=120)
    if r.status_code >= 300:
        print(f"ERROR upload_image: {r.status_code} {r.text[:300]}", file=sys.stderr)
        return None
    return r.json().get("id")


def create_post(
    site: str,
    auth: tuple[str, str],
    *,
    title: str,
    content: str,
    excerpt: str,
    slug: str,
    status: str,
    categories: list[int],
    author: int,
    lang: str,
    featured_media: int | None = None,
    tags: list[int] | None = None,
) -> dict:
    payload = {
        "title": title,
        "content": content,
        "excerpt": excerpt,
        "slug": slug,
        "status": status,
        "categories": categories,
        "author": author,
        "lang": lang,
    }
    if featured_media:
        payload["featured_media"] = featured_media
    if tags:
        payload["tags"] = tags
    r = requests.post(f"{site}/wp-json/wp/v2/posts", auth=auth, json=payload, timeout=60)
    if r.status_code >= 300:
        print(f"ERROR create_post: {r.status_code} {r.text[:600]}", file=sys.stderr)
        sys.exit(2)
    return r.json()


def update_post(site: str, auth: tuple[str, str], post_id: int, **fields) -> dict:
    r = requests.post(f"{site}/wp-json/wp/v2/posts/{post_id}", auth=auth, json=fields, timeout=60)
    if r.status_code >= 300:
        print(f"ERROR update_post: {r.status_code} {r.text[:600]}", file=sys.stderr)
        sys.exit(2)
    return r.json()


def update_rank_math(site: str, auth: tuple[str, str], post_id: int, *, title: str, description: str, focus_keyword: str) -> bool:
    payload = {
        "objectID": post_id,
        "objectType": "post",
        "meta": {
            "rank_math_title": title,
            "rank_math_description": description,
            "rank_math_focus_keyword": focus_keyword,
        },
    }
    r = requests.post(f"{site}/wp-json/rankmath/v1/updateMeta", auth=auth, json=payload, timeout=30)
    if r.status_code >= 300:
        print(f"WARN rank_math: {r.status_code} {r.text[:200]}", file=sys.stderr)
        return False
    return True


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--file", required=True)
    p.add_argument("--lang", required=True, choices=["es", "en", "ca"])
    p.add_argument("--categories", required=True, help="comma-separated IDs")
    p.add_argument("--author", type=int, default=7)
    p.add_argument("--status", default="draft", choices=["draft", "publish", "private"])
    p.add_argument("--featured-image")
    p.add_argument("--print-content", action="store_true", help="Imprime el HTML generado y sale")
    args = p.parse_args(argv[1:])

    site = env("WP_SITE", "https://zoopa.es").rstrip("/")
    user = env("WP_USER")
    pwd = env("WP_APP_PASSWORD").replace(" ", "")
    auth = (user, pwd)

    fp = Path(args.file)
    raw = fp.read_text(encoding="utf-8")
    meta, body = parse_metadata(raw)

    title, content = md_to_gutenberg(body)
    if not title:
        title = meta.get("title", fp.stem)

    if args.print_content:
        print(f"TITLE: {title}\n")
        print(content[:2000])
        return 0

    seo_title = meta.get("title", title)
    description = meta.get("meta_description", "")
    slug = meta.get("slug", "")
    focus_keyword = meta.get("focus_keyword", "")
    excerpt = description or title

    if not slug:
        print("ERROR: slug missing in SEO metadata block", file=sys.stderr)
        return 2

    categories = [int(c) for c in args.categories.split(",") if c.strip()]

    featured_media = None
    if args.featured_image:
        featured_media = upload_image(site, auth, Path(args.featured_image), alt=description or title)

    print(f"[publish] creating post lang={args.lang} status={args.status} slug={slug}")
    post = create_post(
        site, auth,
        title=title,
        content=content,
        excerpt=excerpt,
        slug=slug,
        status=args.status,
        categories=categories,
        author=args.author,
        lang=args.lang,
        featured_media=featured_media,
    )
    post_id = post.get("id")
    post_url = post.get("link")
    print(f"[ok] post_id={post_id} url={post_url}")

    if focus_keyword or seo_title or description:
        ok = update_rank_math(site, auth, post_id, title=seo_title, description=description, focus_keyword=focus_keyword)
        print(f"[rankmath] {'ok' if ok else 'failed'}")

    out = {
        "post_id": post_id,
        "url": post_url,
        "lang": args.lang,
        "status": args.status,
        "categories": categories,
        "slug": slug,
    }
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
