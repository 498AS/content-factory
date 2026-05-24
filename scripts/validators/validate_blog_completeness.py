"""Blog completeness validator.

For files matching blog*.md in an output/ directory, verify the structural
checklist: SEO metadata block, key takeaways, mid-CTA, final-CTA, glosario,
FAQ (>=5), exactly 1 H1, alt text on images.

Advisory only. Exits 0.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

H1_RE = re.compile(r"(^#\s+\S)|(<h1[\s>])", re.MULTILINE | re.IGNORECASE)
FAQ_HEADING_RE = re.compile(
    r"(^#{2,3}\s*(faq|preguntas\s+frecuentes|preguntes\s+freq[uü]ents|frequently\s+asked))"
    r"|(<h[23][^>]*>\s*(faq|preguntas\s+frecuentes|preguntes\s+freq[uü]ents|frequently\s+asked))",
    re.MULTILINE | re.IGNORECASE,
)
GLOSSARY_HEADING_RE = re.compile(
    r"(^#{2,3}\s*(glosario|glossari|glossary))"
    r"|(<h[23][^>]*>\s*(glosario|glossari|glossary))",
    re.MULTILINE | re.IGNORECASE,
)
TAKEAWAYS_RE = re.compile(r"(lo que necesitas saber|key takeaways|key\s*points|punts\s+clau|el que has de saber)", re.IGNORECASE)
META_BLOCK_RE = re.compile(r"<!--\s*(seo|metadata|meta|wordpress).*?-->", re.IGNORECASE | re.DOTALL)
SLUG_LINE_RE = re.compile(r"\b(slug|focus[-\s_]?keyword|meta[-\s_]?description|canonical)\b\s*[:=]", re.IGNORECASE)
MID_CTA_RE = re.compile(r"(esto es lo nuestro|aix[oò] [eé]s el nostre|this is our|/servicios/|/serveis/|/services/)", re.IGNORECASE)
FINAL_CTA_RE = re.compile(r"(hablemos|parlem|let'?s talk|/contactanos|/contactans|/contact-us|/contact/)", re.IGNORECASE)
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\([^)]+\)|<img\s+[^>]*>", re.IGNORECASE)
IMG_TAG_RE = re.compile(r"<img\s+[^>]*>", re.IGNORECASE)
ALT_ATTR_RE = re.compile(r'\balt\s*=\s*"([^"]*)"', re.IGNORECASE)


def is_blog_file(path: Path) -> bool:
    name = path.name.lower()
    if not name.endswith(".md"):
        return False
    if not name.startswith("blog"):
        return False
    if "output" not in {p.name.lower() for p in path.parents}:
        return False
    return True


def count_faqs(text: str) -> int:
    m = FAQ_HEADING_RE.search(text)
    if not m:
        return 0
    after = text[m.end():]
    next_section = re.search(r"(^##\s+|<h2[\s>])", after, flags=re.MULTILINE | re.IGNORECASE)
    if next_section:
        after = after[: next_section.start()]
    md_questions = re.findall(r"^\s*(?:#{3,4}|\*\*|-)\s*[¿?]?[A-Z0-9]", after, flags=re.MULTILINE)
    html_questions = re.findall(r"<h[34][^>]*>\s*[¿?]?[A-Z0-9]", after, flags=re.IGNORECASE)
    return len(md_questions) + len(html_questions)


def check_alt_text(text: str) -> list[str]:
    problems: list[str] = []
    for m in re.finditer(r"!\[([^\]]*)\]\(([^)]+)\)", text):
        alt = m.group(1).strip()
        if not alt:
            problems.append(f"imagen Markdown sin alt text: ![]({m.group(2)})")
        elif len(alt) < 10:
            problems.append(f"alt text demasiado corto ('{alt}'). Debe ser descriptivo y con keywords.")
    for m in IMG_TAG_RE.finditer(text):
        tag = m.group(0)
        alt_match = ALT_ATTR_RE.search(tag)
        if not alt_match:
            problems.append(f"<img> sin atributo alt: {tag[:80]}...")
        elif len(alt_match.group(1).strip()) < 10:
            problems.append(f"alt='{alt_match.group(1)}' demasiado corto.")
    return problems


def check_file(path: Path) -> list[str]:
    issues: list[str] = []
    if not is_blog_file(path):
        return issues
    if not path.exists():
        return issues
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return issues

    h1_count = len(H1_RE.findall(text))
    if h1_count != 1:
        issues.append(f"{path}: {h1_count} H1 encontrados (esperado: 1).")

    if not META_BLOCK_RE.search(text) and not SLUG_LINE_RE.search(text):
        issues.append(f"{path}: falta bloque de metadatos SEO al inicio (title, meta description, slug, focus keyword, canonical).")

    if not TAKEAWAYS_RE.search(text):
        issues.append(f"{path}: falta seccion 'Lo que necesitas saber' / 'Key takeaways' tras la intro.")

    if not MID_CTA_RE.search(text):
        issues.append(f"{path}: falta mid-CTA (~50%) hacia pagina de servicio. Buscar: 'Esto es lo nuestro' o link a /servicios/.")

    if not FINAL_CTA_RE.search(text):
        issues.append(f"{path}: falta final-CTA hacia /contactanos/. Buscar: 'Hablemos' / 'Parlem' / 'Let\\'s talk'.")

    if not GLOSSARY_HEADING_RE.search(text):
        issues.append(f"{path}: falta seccion 'Glosario' / 'Glossari' / 'Glossary' con entidades.")

    if not FAQ_HEADING_RE.search(text):
        issues.append(f"{path}: falta seccion 'FAQ' / 'Preguntas frecuentes'.")
    else:
        faq_count = count_faqs(text)
        if faq_count < 5:
            issues.append(f"{path}: FAQ con {faq_count} preguntas (esperado: >=5).")

    word_count = len(re.findall(r"\b\w+\b", text))
    name = path.name.lower()
    is_facil = "facil" in name
    min_words = 800 if is_facil else 2000
    if word_count < min_words:
        issues.append(f"{path}: {word_count} palabras (esperado: >={min_words}).")

    issues.extend(f"{path}: {p}" for p in check_alt_text(text))

    return issues


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        return 0
    path = Path(argv[1])
    issues = check_file(path)
    for it in issues:
        print(f"[blog] {it}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
