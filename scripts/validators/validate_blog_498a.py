"""Validador del blog estatico de 498advance.com (Perspectivas).

Comprueba un `.html` ya generado en el repo `498AS/498a-new-web-design`:
maquetacion sin estilos inline, clases que existen de verdad en blog.css,
anclas de seccion, indice coherente, schema que parsea, canonical vs og:url,
alt de imagenes, cifras canonicas y enlaces internos que no son 404.

Tambien comprueba lo que _i18n/blog_build.py necesita para hacer su parte:
los marcadores 498A:*, los meta que alimentan listados y feeds, y que toda
clave data-i18n exista en _i18n/blog_i18n.json. El reparto es: blog_build.py
pone la fontaneria de idioma, este validador mira el contenido.

Uso directo (sale 1 si hay avisos):
  python3 validate_blog_498a.py ".../498Adesign/blog/slug.html"

Tambien se usa desde run_all.py, que es advisory y siempre sale 0.

Reglas: references/blog-498advance-static.md
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

SITE = "https://498advance.com"
LANGS = ("es", "ca", "en", "it")
MARCADORES = ("hreflang", "nav", "switcher")
CATEGORIAS = ("Estudio", "Método", "Producto", "Investigación")

# Clases que el JS anade o que viven en tokens.css / la home
EXTRA_CLASSES = {"is-current", "is-active", "nav-open", "lang-cjk",
                 "notranslate"}  # selector de idioma, lo pone blog_build.py

# Cifras y naming que ya no son validos -> lo correcto. Canon 2026-09-27.
STALE = [
    (r"\b10\s?M\+?\s+menciones", "menciones analizadas: 12M+"),
    (r"\b10\s?millones\s+de\s+menciones", "menciones analizadas: 12M+"),
    (r"\b3\.000\s*[-–a]\s*30\.000", "volumen por estudio: 6.000-30.000 prompts"),
    (r"Business\s+Impact\s+Score", "BIS es Brand Impact Score"),
    (r"\b40\s+proyectos\b", "+150 estudios entregados · 50+ marcas e instituciones"),
    (r"\b16\+?\s+marcas\b", "50+ marcas e instituciones"),
    (r"\b(cinco|seis)\s+superficies\b", "son siete superficies de IA"),
    (r"498AS\s+Innovation\s+Lab", "el nombre vigente es 498 Advance (498A)"),
    (r"\bBanking\b", "el vertical se llama Finance"),
    (r"\bAutomotive\b", "el vertical se llama Mobility"),
    (r"zoopa\.cat", "zoopa.cat no resuelve: usar zoopa.es"),
    (r"https?://498as\.com", "el dominio canonico es 498advance.com"),
]

PRODUCT_PAGES_OK = {"/productos/", "/productos/index.html", "/productos/georadar.html"}


def find_repo(path: Path) -> Path | None:
    for parent in [path.parent, *path.parents]:
        if (parent / "blog" / "blog.css").exists():
            return parent
    fallback = Path("/Users/carlos/Documents/claudecode-proj/design system 498A/498Adesign")
    return fallback if (fallback / "blog" / "blog.css").exists() else None


def load_i18n(repo: Path) -> dict:
    path = repo.parent / "_i18n" / "blog_i18n.json"
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def css_classes(repo: Path) -> set[str]:
    found: set[str] = set(EXTRA_CLASSES)
    for name in ("blog/blog.css", "tokens.css"):
        css = repo / name
        if not css.exists():
            continue
        text = re.sub(r"/\*.*?\*/", " ", css.read_text(encoding="utf-8"), flags=re.S)
        for chunk in text.split("}"):
            selector = chunk.split("{")[0]
            found.update(re.findall(r"\.([A-Za-z][\w-]*)", selector))
    return found


def strip_tags(text: str) -> str:
    return re.sub(r"<[^>]+>", " ", text)


def body_region(html: str) -> str:
    a = html.find('<div class="post__body"')
    if a < 0:
        return ""
    b = html.find('<nav class="post-toc"', a)
    return html[a:b if b > 0 else len(html)]


def local_path(repo: Path, page: Path, href: str) -> Path | None:
    url = href.split("#")[0].split("?")[0]
    if not url:
        return None
    if url.startswith(("http://", "https://")):
        parts = urlsplit(url)
        if parts.netloc not in ("498advance.com", "www.498advance.com"):
            return None
        url = parts.path
    if url.startswith(("mailto:", "tel:", "javascript:", "data:")):
        return None
    base = repo if url.startswith("/") else page.parent
    target = (base / url.lstrip("/")).resolve() if url.startswith("/") else (base / url).resolve()
    if url.endswith("/") or target.is_dir():
        target = target / "index.html"
    return target


def check_file(path: Path) -> list[str]:
    path = Path(path)
    if path.suffix.lower() != ".html":
        return []
    html = path.read_text(encoding="utf-8", errors="replace")
    body = body_region(html)
    if not body:
        return []  # no es un post del blog 498A
    issues: list[str] = []
    repo = find_repo(path)

    # 1 · marcadores sin rellenar
    for mark in sorted(set(re.findall(r"\{\{[A-Z_0-9]+\}\}", html))):
        issues.append(f"marcador sin rellenar: {mark}")

    # 2 · estilos inline
    for m in re.finditer(r'style\s*=\s*"', html):
        line = html[:m.start()].count("\n") + 1
        issues.append(f"linea {line}: style= inline. El blog 498A solo usa clases de blog.css")

    # 3 · clases que no existen
    if repo:
        known = css_classes(repo)
        used: set[str] = set()
        for attr in re.findall(r'class="([^"]*)"', html):
            used.update(c for c in attr.split() if c)
        for klass in sorted(used - known):
            issues.append(f"clase inexistente en blog.css: .{klass}")
    else:
        issues.append("no encuentro el repo (blog/blog.css): no puedo validar clases ni enlaces")

    # 4 · un solo h1
    h1s = re.findall(r"<h1\b", html)
    if len(h1s) != 1:
        issues.append(f"la pagina tiene {len(h1s)} <h1>, debe tener exactamente 1")

    # 5 · h2: id + .num + .ancla, y presencia en el indice
    toc_block = html[html.find('<nav class="post-toc"'):] if '<nav class="post-toc"' in html else ""
    toc_ids = set(re.findall(r'<a href="#([A-Za-z0-9_-]+)"', toc_block))
    body_ids: list[str] = []
    for tag, inner in re.findall(r"(<h2\b[^>]*>)(.*?)</h2>", body, flags=re.S):
        sid = re.search(r'id="([^"]+)"', tag)
        if not sid:
            issues.append(f"h2 sin id: {strip_tags(inner).strip()[:60]}")
            continue
        sid = sid.group(1)
        body_ids.append(sid)
        if '<span class="num">' not in inner:
            issues.append(f'h2 #{sid}: falta <span class="num">')
        if f'class="ancla" href="#{sid}"' not in inner.replace("\n", " "):
            issues.append(f"h2 #{sid}: falta el enlace de ancla a #{sid}")
        if sid not in toc_ids:
            issues.append(f"h2 #{sid}: no esta en el indice lateral (.post-toc)")
    all_ids = set(re.findall(r'id="([^"]+)"', html))
    for tid in sorted(toc_ids - all_ids):
        issues.append(f"el indice apunta a #{tid}, que no existe en la pagina")
    if not body_ids:
        issues.append("el cuerpo no tiene ninguna seccion h2 con id")

    # 6 · JSON-LD
    tipos: set[str] = set()
    for raw in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, flags=re.S):
        try:
            data = json.loads(raw)
        except json.JSONDecodeError as exc:
            issues.append(f"JSON-LD no parsea: {exc}")
            continue
        for node in (data if isinstance(data, list) else [data]):
            if isinstance(node, dict) and node.get("@type"):
                tipos.add(node["@type"])
    es_estudio = 'class="metodologia"' in html or "#dataset" in html
    for needed in ("Article", "FAQPage", "BreadcrumbList"):
        if needed not in tipos:
            issues.append(f"falta el bloque {needed} en el JSON-LD")
    if es_estudio and "Dataset" not in tipos:
        issues.append("es un estudio y no declara Dataset en el JSON-LD")
    if not es_estudio and "Dataset" in tipos:
        issues.append("declara Dataset pero no trae .metodologia: un estudio la necesita")

    # FAQPage con al menos dos preguntas
    faq_q = re.findall(r'"@type":\s*"Question"', html)
    if len(faq_q) < 2:
        issues.append(f"el FAQPage trae {len(faq_q)} preguntas, minimo 2")

    # 7 · canonical vs og:url vs mainEntityOfPage
    def meta(prop: str) -> str:
        m = re.search(rf'<meta property="{prop}" content="([^"]*)"', html)
        return m.group(1) if m else ""

    can_m = re.search(r'<link rel="canonical" href="([^"]*)"', html)
    canonical = can_m.group(1) if can_m else ""
    og_url = meta("og:url")
    meop_m = re.search(r'"mainEntityOfPage":\s*\{[^}]*"@id":\s*"([^"]+)"', html)
    meop = meop_m.group(1) if meop_m else ""
    expected = ""
    if repo:
        try:
            expected = SITE + "/" + path.resolve().relative_to(repo.resolve()).as_posix()
        except ValueError:
            expected = ""
    if not og_url:
        issues.append("falta og:url")
    elif expected and og_url != expected:
        issues.append(f"og:url ({og_url}) no coincide con la ruta del fichero ({expected})")
    if meop and og_url and meop != og_url:
        issues.append(f"mainEntityOfPage ({meop}) no coincide con og:url ({og_url})")
    if not canonical:
        issues.append("falta rel=canonical")
    elif canonical != og_url:
        if not canonical.startswith(("http://", "https://")):
            issues.append(f"canonical no absoluto: {canonical}")
        elif '"sameAs"' not in html:
            issues.append("pieza derivada (canonical externo) sin sameAs al original en el Article")

    # 8 · description
    desc = re.search(r'<meta name="description" content="([^"]*)"', html)
    if not desc:
        issues.append("falta meta description")
    elif len(desc.group(1)) > 155:
        issues.append(f"meta description de {len(desc.group(1))} caracteres, maximo 155")

    # 9 · alt de imagenes
    for tag in re.findall(r"<img\b[^>]*>", body):
        alt = re.search(r'alt="([^"]*)"', tag)
        if not alt or not alt.group(1).strip():
            issues.append(f"img sin alt descriptivo: {tag[:90]}")

    # 10 · conclusiones con numeros
    tk = re.search(r'<section class="post-takeaways".*?</section>', html, flags=re.S)
    if not tk:
        issues.append("falta el bloque .post-takeaways (conclusiones arriba)")
    else:
        lis = re.findall(r"<li>(.*?)</li>", tk.group(0), flags=re.S)
        if len(lis) < 3:
            issues.append(f".post-takeaways trae {len(lis)} conclusiones, minimo 3")
        sin_cifra = [strip_tags(x).strip()[:50] for x in lis if not re.search(r"\d", x)]
        for txt in sin_cifra:
            issues.append(f"conclusion sin cifra: \"{txt}...\". Sin numero no se cita")

    # 11 · anti-patrones de maquetacion
    if "<blockquote" in body:
        issues.append("<blockquote> en el cuerpo: el destacado es <aside class=\"callout\">")
    if re.search(r"[—–]", strip_tags(body)):
        issues.append("em-dash o en-dash en el cuerpo (orthography-rules.md §3)")
    if es_estudio and 'class="datos-abiertos"' not in html:
        issues.append("estudio sin bloque .datos-abiertos con el csv y el json")

    # 12 · cifras y naming obsoletos
    texto = strip_tags(html)
    for pattern, fix in STALE:
        if re.search(pattern, texto, flags=re.I):
            issues.append(f"dato o naming obsoleto ({pattern}): {fix}")
    # el modulo se escribe exactamente GEOdoctor: cualquier otra grafia es error
    for m in re.finditer(r"\bgeo[\s_]?doctor\b", texto, flags=re.I):
        if m.group(0) != "GEOdoctor":
            issues.append(f"naming: '{m.group(0)}' se escribe GEOdoctor")

    # 13 · lo que necesita _i18n/blog_build.py
    for marca in MARCADORES:
        if f"<!-- 498A:{marca} -->" not in html:
            issues.append(f"falta el marcador <!-- 498A:{marca} -->: blog_build.py no podra "
                          "poner la fontaneria de idioma")
    for prop, patron in (
        ("og:title", r'<meta property="og:title" content="[^"]+"'),
        ("article:published_time", r'<meta property="article:published_time" content="\d{4}-\d{2}-\d{2}'),
        ("article:section", r'<meta property="article:section" content="[^"]+"'),
        ("og:image", r'<meta property="og:image" content="[^"]+"'),
    ):
        if not re.search(patron, html):
            issues.append(f"falta {prop}: blog_build.py lo usa para el listado y el feed")
    seccion = re.search(r'<meta property="article:section" content="([^"]*)"', html)
    if seccion and seccion.group(1) not in CATEGORIAS:
        issues.append(f"categoria '{seccion.group(1)}' fuera de {' · '.join(CATEGORIAS)}")
    if repo:
        i18n = load_i18n(repo)
        if i18n:
            claves = set(re.findall(r'data-i18n(?:-label)?="([a-z0-9_]+)"', html))
            for clave in sorted(claves - set(i18n)):
                issues.append(f'data-i18n="{clave}" no existe en _i18n/blog_i18n.json')
    rss = re.search(r'<link rel="alternate" type="application/rss\+xml"[^>]*href="([^"]*)"', html)
    if rss and og_url:
        pref = og_url[len(SITE):].split("/blog/")[0]
        if rss.group(1) != f"{SITE}{pref}/feed.xml":
            issues.append(f"el feed enlazado ({rss.group(1)}) no es el del idioma "
                          f"({SITE}{pref}/feed.xml)")

    # 14 · enlaces internos
    if repo:
        # solo enlaces de navegacion y recursos: canonical y alternate son
        # URLs de pagina, no ficheros que tengan que estar en el repo
        hrefs = set(re.findall(r'<a\b[^>]*\shref="([^"]+)"', html))
        for tag in re.findall(r"<link\b[^>]*>", html):
            rel = re.search(r'rel="([^"]*)"', tag)
            if rel and rel.group(1).split()[0] in ("canonical", "alternate"):
                continue
            h = re.search(r'href="([^"]+)"', tag)
            if h:
                hrefs.add(h.group(1))
        vistos: set[str] = set()
        for href in sorted(hrefs):
            if href.startswith("#"):
                continue
            target = local_path(repo, path, href)
            if target is None:
                continue
            limpio = href.split("#")[0] or "/"
            if limpio in vistos:          # /, /#capacidades, /#contacto... son el mismo fichero
                continue
            vistos.add(limpio)
            if rel_is_bad_product(href):
                issues.append(f"pagina de producto inventada: {href}. Solo GEORadar tiene propia")
            elif not target.exists():
                issues.append(f"enlace interno roto: {limpio}")
        for src in sorted(set(re.findall(r'<img[^>]+src="([^"]+)"', html))):
            target = local_path(repo, path, src)
            if target is not None and not target.exists():
                issues.append(f"imagen que no existe en el repo: {src}")

    return issues


def rel_is_bad_product(href: str) -> bool:
    path = href.split("#")[0].split("?")[0]
    if not path.startswith("/productos/"):
        return False
    return path not in PRODUCT_PAGES_OK


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 2
    rc = 0
    for raw in argv[1:]:
        p = Path(raw)
        if not p.exists():
            print(f"[x] {raw}: no existe")
            rc = 1
            continue
        issues = check_file(p)
        if not issues:
            print(f"[ok] {p.name}: sin avisos")
            continue
        print(f"[{len(issues)} aviso(s)] {p.name}")
        for it in issues:
            print(f"  · {it}")
        rc = 1
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv))
