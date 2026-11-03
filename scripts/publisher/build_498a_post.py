"""Generador de posts del blog estatico de 498advance.com (Perspectivas).

Convierte un `blog498a_<lang>.md` (front matter YAML + markdown restringido) en el
HTML de la plantilla del repo `498AS/498a-new-web-design`, en cualquiera de los
cuatro idiomas del blog (es, ca, en, it). El frances no lleva blog.

Reparto de trabajo, y es importante no cruzarlo:

  ESTE script          escribe el cuerpo de un post: <head>, hero, conclusiones,
                       secciones con ancla, componentes, metodologia, fuentes,
                       schema y el indice lateral. Un fichero por idioma.
  _i18n/blog_build.py  del repo de la web hace la fontaneria: lang, hreflang
                       reciproco, og:locale, inLanguage, navegacion, selector de
                       idioma, etiquetas data-i18n, los cuatro listados, el
                       sitemap y los cuatro feeds RSS.

Nunca toques a mano los bloques <!-- 498A:hreflang -->, <!-- 498A:nav --> ni
<!-- 498A:switcher -->, ni los listados, ni el sitemap, ni los feeds.

Nada que ver con wp_publish.py: alli hay un CMS, aqui un fichero estatico con
clases de blog.css y schema escrito a mano.

Uso:
  python3 build_498a_post.py output/blog498a_es.md --dry-run
  python3 build_498a_post.py output/blog498a_{es,ca,en,it}.md --build
  python3 build_498a_post.py output/blog498a_es.md --repo /ruta/498Adesign

Flags:
  --dry-run    escribe en un directorio temporal, no toca el repo
  --build      despues de escribir, ejecuta _i18n/blog_build.py del repo
  --repo RUTA  raiz publicable (por defecto 498Adesign del repo local)
  --out DIR    destino alternativo para el .html

Formato de entrada y reglas: references/blog-498advance-static.md
"""

from __future__ import annotations

import argparse
import html as htmllib
import json
import re
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path

REPO_DEFAULT = Path(
    "/Users/carlos/Documents/claudecode-proj/design system 498A/498Adesign"
)
SITE = "https://498advance.com"
ORG_ID = f"{SITE}/#organization"
LANGS = ("es", "ca", "en", "it")
CATEGORIAS = ("Estudio", "Método", "Producto", "Investigación")
WPM = 220

# Cadenas que NO llevan data-i18n en la plantilla: las escribe este script en el
# idioma del fichero. Todo lo demas sale de _i18n/blog_i18n.json.
SUELTAS = {
    "es": {"prompts_v": "prompts personalizados", "marcas_v": "marcas del set competitivo",
           "abiertos_p": "Los datos de este estudio están publicados en formato legible por "
                         "máquina, bajo licencia CC BY 4.0. Cítanos como 498A.",
           "fuente": "Fuente"},
    "ca": {"prompts_v": "prompts personalitzats", "marcas_v": "marques del set competitiu",
           "abiertos_p": "Les dades d'aquest estudi estan publicades en format llegible per "
                         "màquina, amb llicència CC BY 4.0. Cita'ns com a 498A.",
           "fuente": "Font"},
    "en": {"prompts_v": "custom prompts", "marcas_v": "brands in the competitive set",
           "abiertos_p": "The data behind this study is published in machine-readable format "
                         "under a CC BY 4.0 licence. Cite us as 498A.",
           "fuente": "Source"},
    "it": {"prompts_v": "prompt personalizzati", "marcas_v": "marchi del set competitivo",
           "abiertos_p": "I dati di questo studio sono pubblicati in formato leggibile dalle "
                         "macchine, con licenza CC BY 4.0. Citaci come 498A.",
           "fuente": "Fonte"},
}

# Reserva minima si no se encuentra blog_i18n.json en el repo.
I18N_FALLBACK = {
    "locale": {"es": "es_ES", "ca": "ca_ES", "en": "en_GB", "it": "it_IT"},
    "schema_lang": {"es": "es-ES", "ca": "ca-ES", "en": "en-GB", "it": "it-IT"},
    "post_takeaways": {"es": "Lo que encontramos", "ca": "El que hem trobat",
                       "en": "What we found", "it": "Quello che abbiamo trovato"},
    "post_callout": {"es": "Lo que importa", "ca": "El que importa",
                     "en": "What matters", "it": "Quello che conta"},
    "post_detalle": {"es": "Detalle técnico · cómo se calcula",
                     "ca": "Detall tècnic · com es calcula",
                     "en": "Technical detail · how it is calculated",
                     "it": "Dettaglio tecnico · come si calcola"},
    "post_fuentes": {"es": "Fuentes", "ca": "Fonts", "en": "Sources", "it": "Fonti"},
    "post_ancla_aria": {"es": "Enlace a esta sección", "ca": "Enllaç a aquesta secció",
                        "en": "Link to this section", "it": "Link a questa sezione"},
    # Credito al medio donde se publico una version anterior. El {enlace} lo
    # rellena el generador con el <a> al original.
    "post_version_anterior": {
        "es": "Una versión anterior de este texto se publicó en {enlace}.",
        "ca": "Una versió anterior d'aquest text es va publicar a {enlace}.",
        "en": "An earlier version of this text was published on {enlace}.",
        "it": "Una versione precedente di questo testo è stata pubblicata su {enlace}."},
    "post_original": {"es": "Publicado originalmente en carlosortet.com",
                      "ca": "Publicat originalment a carlosortet.com",
                      "en": "Originally published on carlosortet.com",
                      "it": "Pubblicato originariamente su carlosortet.com"},
    "est_metodologia": {"es": "Metodología", "ca": "Metodologia",
                        "en": "Methodology", "it": "Metodologia"},
    "est_datos": {"es": "Datos abiertos", "ca": "Dades obertes",
                  "en": "Open data", "it": "Dati aperti"},
    "est_prompts": {"es": "Prompts", "ca": "Prompts", "en": "Prompts", "it": "Prompt"},
    "est_motores": {"es": "Motores y superficies", "ca": "Motors i superfícies",
                    "en": "Engines and surfaces", "it": "Motori e superfici"},
    "est_periodo": {"es": "Periodo", "ca": "Període", "en": "Period", "it": "Periodo"},
    "est_mercados": {"es": "Mercados", "ca": "Mercats", "en": "Markets", "it": "Mercati"},
    "est_marcas": {"es": "Marcas", "ca": "Marques", "en": "Brands", "it": "Marchi"},
    "est_kpis": {"es": "KPIs", "ca": "KPIs", "en": "KPIs", "it": "KPI"},
    "est_limitaciones": {"es": "Limitaciones", "ca": "Limitacions",
                         "en": "Limitations", "it": "Limiti"},
}


class BuildError(Exception):
    pass


def cargar_validador():
    """El validador vive en scripts/validators/. Se carga por ruta para que el
    generador nunca escriba un post sin comprobarlo."""
    ruta = Path(__file__).resolve().parent.parent / "validators" / "validate_blog_498a.py"
    if not ruta.exists():
        return None
    import importlib.util
    spec = importlib.util.spec_from_file_location("validate_blog_498a", ruta)
    if spec is None or spec.loader is None:
        return None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_i18n(repo: Path) -> dict:
    path = repo.parent / "_i18n" / "blog_i18n.json"
    if path.exists():
        data = json.loads(path.read_text(encoding="utf-8"))
        for key, val in I18N_FALLBACK.items():
            data.setdefault(key, val)
        return data
    return dict(I18N_FALLBACK)


# --------------------------------------------------------------------------
# Front matter (subconjunto de YAML, sin dependencias)
# --------------------------------------------------------------------------

def split_front_matter(text: str) -> tuple[list[str], str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise BuildError("falta el front matter: la primera linea debe ser ---")
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return lines[1:i], "\n".join(lines[i + 1:])
    raise BuildError("el front matter no se cierra con ---")


def _inline_list(raw: str) -> list[str]:
    inner = raw[1:-1].strip()
    if not inner:
        return []
    out: list[str] = []
    cur = ""
    quote = None
    for ch in inner:
        if quote:
            if ch == quote:
                quote = None
            else:
                cur += ch
        elif ch in "\"'":
            quote = ch
        elif ch == ",":
            out.append(cur.strip())
            cur = ""
        else:
            cur += ch
    out.append(cur.strip())
    return [x for x in out if x != ""]


def _scalar(raw: str):
    raw = raw.strip()
    if raw.startswith("[") and raw.endswith("]"):
        return _inline_list(raw)
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in "\"'":
        return raw[1:-1]
    return raw


def _parse_node(items: list[tuple[int, str]], pos: int, indent: int):
    if items[pos][1].startswith("- "):
        seq: list = []
        while pos < len(items) and items[pos][0] == indent and items[pos][1].startswith("- "):
            rest = items[pos][1][2:].strip()
            pos += 1
            if ":" in rest and rest[0] not in "\"'[":
                key, _, val = rest.partition(":")
                node: dict = {}
                if val.strip():
                    node[key.strip()] = _scalar(val)
                elif pos < len(items) and items[pos][0] > indent:
                    sub, pos = _parse_node(items, pos, items[pos][0])
                    node[key.strip()] = sub
                else:
                    node[key.strip()] = ""
                while pos < len(items) and items[pos][0] > indent \
                        and not items[pos][1].startswith("- "):
                    k2, _, v2 = items[pos][1].partition(":")
                    own = items[pos][0]
                    pos += 1
                    if v2.strip():
                        node[k2.strip()] = _scalar(v2)
                    elif pos < len(items) and items[pos][0] > own:
                        sub, pos = _parse_node(items, pos, items[pos][0])
                        node[k2.strip()] = sub
                    else:
                        node[k2.strip()] = ""
                seq.append(node)
            else:
                seq.append(_scalar(rest))
        return seq, pos

    mapping: dict = {}
    while pos < len(items) and items[pos][0] == indent and not items[pos][1].startswith("- "):
        key, _, val = items[pos][1].partition(":")
        own = items[pos][0]
        pos += 1
        if val.strip():
            mapping[key.strip()] = _scalar(val)
        elif pos < len(items) and (items[pos][0] > own
                                   or (items[pos][0] == own and items[pos][1].startswith("- "))):
            sub, pos = _parse_node(items, pos, items[pos][0])
            mapping[key.strip()] = sub
        else:
            mapping[key.strip()] = ""
    return mapping, pos


def parse_front_matter(lines: list[str]) -> dict:
    items = [(len(l) - len(l.lstrip(" ")), l.strip())
             for l in lines if l.strip() and not l.lstrip().startswith("#")]
    if not items:
        return {}
    data, _ = _parse_node(items, 0, items[0][0])
    if not isinstance(data, dict):
        raise BuildError("el front matter debe ser un mapa de claves")
    return data


# --------------------------------------------------------------------------
# Markdown restringido -> HTML del design system
# --------------------------------------------------------------------------

def esc(text: str) -> str:
    return htmllib.escape(text, quote=False)


def esc_attr(text: str) -> str:
    """Escape para valores que viven dentro de atributos. El apostrofo no necesita
    entidad entre comillas dobles, y ademas blog_build.py lee estos atributos como
    texto para el listado y el feed."""
    return htmllib.escape(text).replace("&#x27;", "'")


def inline(text: str) -> str:
    out = esc(text)
    out = re.sub(r"`([^`]+)`", r"<code>\1</code>", out)
    out = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2">\1</a>', out)
    out = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", out)
    return out


def build_table(rows: list[str], caption: str) -> str:
    cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
    if len(cells) < 3:
        raise BuildError("una tabla necesita cabecera, separador y al menos una fila")
    header, sep, body = cells[0], cells[1], cells[2:]
    right = [bool(re.match(r"^:?-+:$", s.strip())) for s in sep]
    out = ['<div class="tabla-wrap">', '  <table class="tabla-datos">']
    if caption:
        out.append(f"    <caption>{inline(caption)}</caption>")
    out.append("    <thead><tr>" + "".join(f"<th>{inline(h)}</th>" for h in header)
               + "</tr></thead>")
    out.append("    <tbody>")
    for row in body:
        tds = []
        for i, cell in enumerate(row):
            klass = []
            text = cell
            strong = re.fullmatch(r"\*\*(.+)\*\*", cell.strip())
            if strong and i == 0:
                klass.append("destaca")
                text = strong.group(1)
            if i < len(right) and right[i]:
                klass.append("num")
            attr = f' class="{" ".join(klass)}"' if klass else ""
            tds.append(f"<td{attr}>{inline(text)}</td>")
        out.append("      <tr>" + "".join(tds) + "</tr>")
    out.extend(["    </tbody>", "  </table>", "</div>"])
    return "\n".join(out)


def md_to_html(body: str, lang: str, tr) -> tuple[str, str, list[tuple[str, str]]]:
    """Devuelve (lo_anterior_al_primer_h2, cuerpo, secciones)."""
    lines = body.replace("\r\n", "\n").split("\n")
    head_parts: list[str] = []
    parts: list[str] = []
    sections: list[tuple[str, str]] = []
    used_ids: set[str] = set()
    i = 0
    seen_h2 = False

    def out() -> list[str]:
        return parts if seen_h2 else head_parts

    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        if line.startswith(">"):
            raise BuildError(f"linea {i + 1}: no se usan citas '>'. El destacado es :::callout")
        if "style=" in line:
            raise BuildError(f"linea {i + 1}: prohibido 'style=' en el cuerpo")

        if line.startswith("## "):
            seen_h2 = True
            title = line[3:].strip()
            explicit = re.search(r"\{#([A-Za-z0-9_-]+)\}\s*$", title)
            if explicit:
                sec_id = explicit.group(1)
                title = title[:explicit.start()].strip()
            else:
                sec_id = f"seccion-{len(sections) + 1}"
            if sec_id in used_ids:
                raise BuildError(f"id de seccion repetido: {sec_id}")
            used_ids.add(sec_id)
            num = f"{len(sections) + 1:02d}"
            sections.append((sec_id, title))
            parts.append(
                f'<h2 id="{sec_id}"><span class="num">{num}</span>{inline(title)}'
                f'<a class="ancla" href="#{sec_id}" data-i18n-label="post_ancla_aria"'
                f' aria-label="{tr("post_ancla_aria", lang)}">#</a></h2>'
            )
            i += 1
            continue

        if line.startswith("### "):
            out().append(f"<h3>{inline(line[4:].strip())}</h3>")
            i += 1
            continue

        if line.startswith(":::"):
            kind, _, label = line[3:].strip().partition(" ")
            kind = kind.lower()
            if kind not in ("callout", "detalle"):
                raise BuildError(f"linea {i + 1}: bloque ':::{kind}' no soportado")
            label = label.strip()
            i += 1
            buf: list[str] = []
            while i < len(lines) and lines[i].strip() != ":::":
                buf.append(lines[i])
                i += 1
            if i >= len(lines):
                raise BuildError(f"bloque :::{kind} sin cerrar")
            i += 1
            inner = [f"<p>{inline(p.strip())}</p>"
                     for p in re.split(r"\n\s*\n", "\n".join(buf).strip()) if p.strip()]
            key = "post_callout" if kind == "callout" else "post_detalle"
            # sin etiqueta propia se usa la del sistema, marcada con data-i18n
            # para que blog_build.py la traduzca; con etiqueta propia, no.
            mark = "" if label else f' data-i18n="{key}"'
            texto = label or tr(key, lang)
            if kind == "callout":
                out().append('<aside class="callout">\n'
                             f'  <span class="callout__label"{mark}>{inline(texto)}</span>\n  '
                             + "\n  ".join(inner) + "\n</aside>")
            else:
                out().append('<details class="detalle">\n'
                             f"  <summary{mark}>{inline(texto)}</summary>\n"
                             '  <div class="detalle__cuerpo">\n    '
                             + "\n    ".join(inner) + "\n  </div>\n</details>")
            continue

        if line.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(lines[i])
                i += 1
            caption = ""
            if i < len(lines) and lines[i].strip().startswith(": "):
                caption = lines[i].strip()[2:].strip()
                i += 1
            out().append(build_table(rows, caption))
            continue

        fig = re.fullmatch(r"!\[(.*?)\]\(([^)\s]+)\)", line)
        if fig:
            alt, src = fig.group(1).strip(), fig.group(2).strip()
            if not alt:
                raise BuildError(f"linea {i + 1}: la imagen necesita alt descriptivo")
            i += 1
            caption = ""
            if i < len(lines) and lines[i].strip().startswith(": "):
                caption = lines[i].strip()[2:].strip()
                i += 1
            cap = f"\n  <figcaption>{inline(caption)}</figcaption>" if caption else ""
            out().append(f'<figure class="figura">\n  <img src="{esc(src)}" '
                         f'alt="{htmllib.escape(alt)}">{cap}\n</figure>')
            continue

        if re.match(r"^[-*] ", line):
            items = []
            while i < len(lines) and re.match(r"^[-*] ", lines[i].strip()):
                items.append(lines[i].strip()[2:].strip())
                i += 1
            out().append("<ul>\n" + "\n".join(f"  <li>{inline(x)}</li>" for x in items) + "\n</ul>")
            continue

        if re.match(r"^\d+\. ", line):
            items = []
            while i < len(lines) and re.match(r"^\d+\. ", lines[i].strip()):
                items.append(re.sub(r"^\d+\.\s*", "", lines[i].strip()))
                i += 1
            out().append("<ol>\n" + "\n".join(f"  <li>{inline(x)}</li>" for x in items) + "\n</ol>")
            continue

        buf = []
        while i < len(lines):
            nxt = lines[i].strip()
            if not nxt or nxt.startswith(("## ", "### ", ":::", "|", "- ", "* ", ": ")) \
                    or re.match(r"^\d+\. ", nxt) \
                    or re.fullmatch(r"!\[(.*?)\]\(([^)\s]+)\)", nxt):
                break
            buf.append(nxt)
            i += 1
        if buf:
            out().append(f"<p>{inline(' '.join(buf))}</p>")

    if not sections:
        raise BuildError("el cuerpo no tiene ninguna seccion '## '")
    return "\n\n".join(head_parts), "\n\n".join(parts), sections


# --------------------------------------------------------------------------
# Bloques del design system que salen del front matter
# --------------------------------------------------------------------------

def block_datos(cifras: list) -> str:
    out = ['<div class="datos">']
    for idx, pair in enumerate(cifras):
        if not isinstance(pair, list) or len(pair) != 2:
            raise BuildError("cada entrada de 'cifras' es una lista [cifra, etiqueta]")
        cifra, etiqueta = pair
        val = f"<em>{esc(cifra)}</em>" if idx == 0 else esc(cifra)
        out.append(f'  <div class="dato"><span class="dato__cifra">{val}</span>\n'
                   f'    <span class="dato__etiqueta">{esc(etiqueta)}</span></div>')
    out.append("</div>")
    return "\n".join(out)


def block_metodologia(metodo: dict, lang: str, tr) -> str:
    campos = [("prompts", "est_prompts"), ("motores", "est_motores"), ("periodo", "est_periodo"),
              ("mercados", "est_mercados"), ("marcas", "est_marcas"), ("kpis", "est_kpis"),
              ("limitaciones", "est_limitaciones")]
    missing = [k for k, _ in campos if not str(metodo.get(k, "")).strip()]
    if missing:
        raise BuildError("un estudio necesita metodo completo. Faltan: " + ", ".join(missing))
    s = SUELTAS[lang]
    valores = {
        "prompts": f'{esc(str(metodo["prompts"]))} {esc(s["prompts_v"])}',
        "motores": esc(str(metodo["motores"])),
        "periodo": esc(str(metodo["periodo"])),
        "mercados": esc(str(metodo["mercados"])),
        "marcas": f'{esc(str(metodo["marcas"]))} {esc(s["marcas_v"])}',
        "kpis": esc(str(metodo["kpis"])),
        "limitaciones": esc(str(metodo["limitaciones"])),
    }
    dl = [f'      <dt data-i18n="{key}">{tr(key, lang)}</dt><dd>{valores[campo]}</dd>'
          for campo, key in campos]
    return ('<section class="metodologia" aria-labelledby="metodologia">\n'
            f'  <div class="metodologia__cab" id="metodologia" data-i18n="est_metodologia">'
            f'{tr("est_metodologia", lang)}</div>\n'
            '  <div class="metodologia__cuerpo">\n    <dl>\n'
            + "\n".join(dl) + "\n    </dl>\n  </div>\n</section>")


def ficheros_dataset(slug: str, repo) -> list:
    """Los ficheros que de verdad hay en blog/datos/ para este slug.

    El dataset vive una sola vez, en /blog/datos/, y lo comparten los cuatro
    idiomas: los datos no se traducen. Por eso las URL son absolutas y sin
    prefijo de idioma. Si no hay ficheros, devuelve lista vacia y quien llama
    se salta el bloque en lugar de inventar nombres.
    """
    import os
    d = os.path.join(str(repo), "blog", "datos")
    if not os.path.isdir(d):
        return []
    fs = [f for f in sorted(os.listdir(d))
          if f.startswith(slug) and f.rsplit(".", 1)[-1] in ("csv", "json")]
    # el json del estudio completo primero, luego los csv por orden
    fs.sort(key=lambda f: (not f.endswith(".json"), f))
    return fs


def block_abiertos(slug: str, lang: str, tr, repo=None) -> str:
    fs = ficheros_dataset(slug, repo if repo is not None else REPO_DEFAULT)
    enlaces = " ·\n".join(f'  <a href="/blog/datos/{f}">{f}</a>' for f in fs)
    return ('<div class="datos-abiertos">\n'
            f'  <span class="datos-abiertos__label" data-i18n="est_datos">'
            f'{tr("est_datos", lang)}</span>\n'
            f'  <p>{esc(SUELTAS[lang]["abiertos_p"])}</p>\n'
            + enlaces + "\n"
            "</div>")


# --------------------------------------------------------------------------
# Utilidades
# --------------------------------------------------------------------------

def replace_between(text: str, start: str, end: str, inner: str, what: str) -> str:
    a = text.find(start)
    if a < 0:
        raise BuildError(f"la plantilla no contiene el ancla de {what}: {start!r}")
    b = text.find(end, a + len(start))
    if b < 0:
        raise BuildError(f"la plantilla no cierra {what}: {end!r}")
    return text[:a + len(start)] + inner + text[b:]


MESES = {
    "es": ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto",
           "septiembre", "octubre", "noviembre", "diciembre"],
    "ca": ["gener", "febrer", "març", "abril", "maig", "juny", "juliol", "agost",
           "setembre", "octubre", "novembre", "desembre"],
    "en": ["January", "February", "March", "April", "May", "June", "July", "August",
           "September", "October", "November", "December"],
    "it": ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio",
           "agosto", "settembre", "ottobre", "novembre", "dicembre"],
}


def fecha_larga(iso: str, lang: str) -> str:
    dt = datetime.strptime(iso, "%Y-%m-%d")
    mes = MESES[lang][dt.month - 1]
    if lang == "es":
        return f"{dt.day} de {mes} de {dt.year}"
    if lang == "ca":
        prep = "d'" if mes[0] in "aeiou" else "de "
        return f"{dt.day} {prep}{mes} de {dt.year}"
    return f"{dt.day} {mes} {dt.year}"


ACENTOS = str.maketrans("áéíóúàèìòùñç", "aeiouaeiounc")


def cat_key(categoria: str) -> str:
    """La misma clave que usa _i18n/blog_build.py para traducir la categoria."""
    return "cat_" + categoria.lower().translate(ACENTOS)


def prefix(lang: str) -> str:
    return "" if lang == "es" else f"/{lang}"


def blog_url(lang: str, slug: str) -> str:
    return f"{SITE}{prefix(lang)}/blog/{slug}.html"


def feed_url(lang: str) -> str:
    return f"{SITE}{prefix(lang)}/feed.xml"


def plain_text(html_body: str) -> str:
    return re.sub(r"<[^>]+>", " ", html_body)


# --------------------------------------------------------------------------
# Schema
# --------------------------------------------------------------------------

def build_jsonld(fm: dict, lang: str, slug: str, canonical: str, og_image: str,
                 words: int, tr, repo=None) -> str:
    repo = repo if repo is not None else REPO_DEFAULT
    faq = fm.get("faq") or []
    if len(faq) < 2:
        raise BuildError("el FAQPage necesita al menos dos preguntas ('faq:' en el front matter)")
    fuentes = fm.get("fuentes") or []
    url = blog_url(lang, slug)
    article = {
        "@context": "https://schema.org",
        "@type": "Article",
        "@id": f"{url}#article",
        "headline": fm["titulo"],
        "description": fm["descripcion"],
        "image": og_image,
        "datePublished": str(fm["fecha"]),
        "dateModified": str(fm.get("actualizado") or fm["fecha"]),
        "inLanguage": tr("schema_lang", lang),
        "articleSection": fm["categoria"],
        "wordCount": str(words),
        "author": {"@type": "Person", "name": fm["autor"], "url": "https://carlosortet.com"},
        "publisher": {"@id": ORG_ID},
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
        "isPartOf": {"@id": f"{SITE}{prefix(lang)}/blog/#blog"},
    }
    if canonical != url:
        article["sameAs"] = canonical
    if fm.get("origen"):
        article["isBasedOn"] = fm["origen"]
    if fuentes:
        article["citation"] = list(fuentes)
    blocks = [article]

    if fm["tipo"] == "estudio":
        ds = fm.get("dataset") or {}
        if not str(ds.get("descripcion", "")).strip():
            raise BuildError("un estudio necesita 'dataset.descripcion'")
        blocks.append({
            "@context": "https://schema.org",
            "@type": "Dataset",
            "@id": f"{url}#dataset",
            "name": f'{fm["titulo"]} · {tr("est_datos", lang)}',
            "description": ds["descripcion"],
            "license": "https://creativecommons.org/licenses/by/4.0/",
            "creator": {"@id": ORG_ID},
            "datePublished": str(fm["fecha"]),
            "measurementTechnique": (fm.get("metodo") or {}).get("motores", ""),
            "variableMeasured": list(ds.get("kpis") or []),
            # El dataset es unico y compartido por los cuatro idiomas: sin
            # prefijo de idioma en la URL, y solo los ficheros que existen.
            "distribution": [
                {"@type": "DataDownload",
                 "encodingFormat": "application/json" if f.endswith(".json") else "text/csv",
                 "contentUrl": f"{SITE}/blog/datos/{f}"}
                for f in ficheros_dataset(slug, repo)
            ],
        })

    blocks.append({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q["pregunta"],
                        "acceptedAnswer": {"@type": "Answer", "text": q["respuesta"]}}
                       for q in faq],
    })
    blocks.append({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": tr("post_migas_inicio", lang),
             "item": f"{SITE}{prefix(lang)}/"},
            {"@type": "ListItem", "position": 2, "name": tr("blog_nombre", lang).split(" · ")[0],
             "item": f"{SITE}{prefix(lang)}/blog/"},
            {"@type": "ListItem", "position": 3, "name": fm["titulo"], "item": url},
        ],
    })
    return json.dumps(blocks, ensure_ascii=False, indent=2)


REQUIRED = ["tipo", "slug", "lang", "titulo", "titulo_h1", "descripcion", "entradilla",
            "categoria", "fecha", "autor", "rol_autor", "bio_autor"]


def build(src: Path, repo: Path, i18n: dict) -> tuple[str, dict, str]:
    def tr(key: str, lang: str) -> str:
        try:
            return i18n[key][lang]
        except KeyError:
            raise BuildError(f"falta la cadena '{key}' en {lang} (blog_i18n.json)")

    fm_lines, body_md = split_front_matter(src.read_text(encoding="utf-8"))
    fm = parse_front_matter(fm_lines)

    missing = [k for k in REQUIRED if not str(fm.get(k, "")).strip()]
    if missing:
        raise BuildError("faltan claves en el front matter: " + ", ".join(missing))
    if fm["tipo"] not in ("estudio", "articulo"):
        raise BuildError("tipo debe ser 'estudio' o 'articulo'")
    lang = fm["lang"]
    if lang not in LANGS:
        raise BuildError(f"lang debe ser uno de {', '.join(LANGS)}. El blog no lleva frances")
    if not re.fullmatch(r"[a-z0-9-]+", str(fm["slug"])):
        raise BuildError("el slug solo admite minusculas, numeros y guiones")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(fm["fecha"])):
        raise BuildError("fecha en formato YYYY-MM-DD")
    if fm["categoria"] not in CATEGORIAS:
        raise BuildError(f"categoria '{fm['categoria']}' no valida. Se escribe SIEMPRE en "
                         f"castellano, una de: {' · '.join(CATEGORIAS)}. blog_build.py la "
                         f"traduce en el hero y en el listado")
    if len(fm["descripcion"]) > 155:
        raise BuildError(f"la descripcion tiene {len(fm['descripcion'])} caracteres, maximo 155")
    conclusiones = fm.get("conclusiones") or []
    if len(conclusiones) < 3:
        raise BuildError("'conclusiones' necesita tres bullets con cifra, unidad y fecha")
    if not (fm.get("fuentes") or []):
        raise BuildError("'fuentes' no puede estar vacia")

    slug, tipo = str(fm["slug"]), fm["tipo"]
    tpl_path = repo / "blog" / f"_plantilla-{tipo}.html"
    if not tpl_path.exists():
        raise BuildError(f"no encuentro la plantilla: {tpl_path}")
    page = tpl_path.read_text(encoding="utf-8")
    for marca in ("hreflang", "nav", "switcher"):
        if f"<!-- 498A:{marca} -->" not in page:
            raise BuildError(f"la plantilla no trae el marcador <!-- 498A:{marca} -->")

    entradilla_html, cuerpo_html, sections = md_to_html(body_md, lang, tr)
    words = len(plain_text(entradilla_html + " " + cuerpo_html).split())
    minutos = max(1, round(words / WPM))

    piezas = [entradilla_html] if entradilla_html else []
    if tipo == "estudio":
        cifras = fm.get("cifras") or []
        if len(cifras) != 3:
            raise BuildError("un estudio necesita exactamente tres 'cifras'")
        piezas.append(block_datos(cifras))
    piezas.append(cuerpo_html)
    if tipo == "estudio":
        piezas.append(block_metodologia(fm.get("metodo") or {}, lang, tr))
        piezas.append(block_abiertos(slug, lang, tr, repo))

    url = blog_url(lang, slug)
    canonical = str(fm.get("canonical") or url)
    if canonical != url:
        # sin clase propia: .post__body > p ya esta estilado y blog.css no
        # tiene ninguna clase para esto
        piezas.append(f'<p><a href="{canonical}" '
                      f'data-i18n="post_original">{tr("post_original", lang)}</a></p>')
    cuerpo = "\n\n".join(p for p in piezas if p.strip())
    cuerpo = ("\n" + "\n".join("        " + l if l.strip() else "" for l in cuerpo.split("\n"))
              + "\n\n        ")

    page = replace_between(page, '<div class="post__body" itemprop="articleBody">',
                           "<!-- ===== FUENTES", cuerpo, "el cuerpo")
    page = replace_between(
        page, '<section class="post-takeaways" aria-labelledby="conclusiones">', "</section>",
        f'\n        <h2 id="conclusiones" data-i18n="post_takeaways">'
        f'{tr("post_takeaways", lang)}</h2>\n        <ul>\n'
        + "\n".join(f"          <li>{inline(str(c))}</li>" for c in conclusiones)
        + "\n        </ul>\n      ", "las conclusiones")
    page = replace_between(
        page, '<section class="fuentes" aria-labelledby="fuentes">', "</section>",
        f'\n          <div class="fuentes__titulo" id="fuentes" data-i18n="post_fuentes">'
        f'{tr("post_fuentes", lang)}</div>\n          <ol>\n'
        + "\n".join(f"            <li>{inline(str(f))}</li>" for f in fm["fuentes"])
        + "\n          </ol>\n        ", "las fuentes")

    # Credito al original, antes de las fuentes. Se localiza aqui y no con
    # data-i18n porque la frase lleva un enlace dentro y data-i18n reescribe
    # el contenido entero del elemento.
    origen = (fm.get("origen") or "").strip()
    if origen:
        host = re.sub(r"^https?://(www\.)?", "", origen).split("/")[0]
        enlace = f'<a href="{esc_attr(origen)}" rel="noopener">{esc(host)}</a>'
        linea = tr("post_version_anterior", lang).replace("{enlace}", enlace)
        marca = '<section class="fuentes"'
        i = page.find(marca)
        if i < 0:
            raise BuildError("no se encontro la seccion de fuentes para colgar el credito")
        page = page[:i] + f'<p class="post-origen">{linea}</p>\n\n        ' + page[i:]

    toc = [f'        <li><a href="#{sid}">{inline(title)}</a></li>' for sid, title in sections]
    if tipo == "estudio":
        toc.append(f'        <li><a href="#metodologia">{tr("est_metodologia", lang)}</a></li>')
    toc.append(f'        <li><a href="#fuentes">{tr("post_fuentes", lang)}</a></li>')
    toc_start = page.find('<nav class="post-toc"')
    ol_start = page.find("<ol>", toc_start)
    ol_end = page.find("</ol>", ol_start)
    if toc_start < 0 or ol_start < 0 or ol_end < 0:
        raise BuildError("la plantilla no trae el indice lateral")
    page = page[:ol_start + 4] + "\n" + "\n".join(toc) + "\n      " + page[ol_end:]

    og_image = str(fm.get("og_image") or f"/assets/og/{slug}.jpg")
    if og_image.startswith("/"):
        og_image = SITE + og_image
    # El <title> y el titulo editorial son cosas distintas. Google corta la
    # etiqueta sobre los 60 caracteres, y los titulares de este blog son largos
    # a proposito: se cortaban justo donde estaba la idea. 'titulo_seo' es el
    # que va al <title>; og:title y el headline del schema siguen llevando el
    # titulo entero, que ahi no se trunca y lee mejor.
    # Un canonical externo solo vale si el original esta en ESTE idioma. Apuntar
    # el italiano al original castellano hace que Google descarte el grupo
    # hreflang entero y deje fuera del indice las traducciones. Para atribuir sin
    # ceder el canonical esta 'origen'. Aqui solo se avisa, porque desde un
    # fichero suelto no se puede saber en que idioma esta esa URL; quien lo
    # comprueba de verdad es blog_build.py, que ve los cuatro idiomas a la vez y
    # falla si dos comparten canonical.
    can = str(fm.get("canonical") or "")
    if can and "498advance.com" not in can and lang != "es":
        print(f"    · canonical externo en un post '{lang}': {can}")
        print(f"      Tiene que ser el original EN {lang.upper()}. Si no existe, quita")
        print(f"      'canonical' y deja 'origen' para la atribucion.")

    titulo_seo = str(fm.get("titulo_seo") or fm["titulo"]).strip()
    largo = len(titulo_seo) + len(" · 498A")
    if largo > 62:
        raise BuildError(
            f"el <title> queda en {largo} caracteres y Google corta sobre 60. "
            f"Anade 'titulo_seo' al front matter con {62 - len(' · 498A')} como maximo. "
            f"Ahora: {titulo_seo!r}")
    marks = {
        "{{TITULO}}": fm["titulo"], "{{TITULO_SEO}}": titulo_seo,
        "{{DESCRIPCION}}": fm["descripcion"],
        "{{ENTRADILLA}}": fm["entradilla"], "{{CATEGORIA}}": fm["categoria"],
        "{{AUTOR}}": fm["autor"], "{{ROL_AUTOR}}": fm["rol_autor"],
        "{{BIO_AUTOR}}": fm["bio_autor"], "{{FECHA_ISO}}": str(fm["fecha"]),
        "{{FECHA_LEGIBLE}}": fecha_larga(str(fm["fecha"]), lang),
        "{{MINUTOS}}": str(minutos), "{{PALABRAS}}": str(words),
        "{{MUESTRA}}": str(fm.get("muestra") or ""),
    }
    page = page.replace("{{TITULO_H1}}", re.sub(r"\*([^*]+)\*", r"<em>\1</em>",
                                                esc(str(fm["titulo_h1"]))))
    for key, val in marks.items():
        page = page.replace(key, esc_attr(str(val)))
    page = page.replace("{{SLUG}}", slug)
    if not str(fm.get("muestra") or "").strip():
        page = re.sub(r"\n\s*<span></span>", "", page)

    # la categoria del hero se traduce con la misma clave que usa el listado
    page = page.replace('<span class="post-hero__cat">',
                        f'<span class="post-hero__cat" data-i18n="{cat_key(fm["categoria"])}">', 1)

    # fontaneria minima: blog_build.py la reescribe, pero el fichero debe ser
    # valido por si solo desde el primer momento.
    page = page.replace('<html lang="es">', f'<html lang="{lang}">', 1)
    page = re.sub(r'<meta property="og:locale" content="[^"]*">',
                  f'<meta property="og:locale" content="{tr("locale", lang)}">', page, count=1)
    if lang != "es":
        page = page.replace(f"{SITE}/blog/", f"{SITE}{prefix(lang)}/blog/")
    page = re.sub(r'<link rel="canonical" href="[^"]*">',
                  f'<link rel="canonical" href="{canonical}">', page, count=1)
    page = re.sub(r'(<link rel="alternate" type="application/rss\+xml"[^>]*href=")[^"]*(")',
                  lambda m: m.group(1) + feed_url(lang) + m.group(2), page, count=1)

    ld = build_jsonld(fm, lang, slug, canonical, og_image, words, tr, repo)
    ld_start = page.find('<script type="application/ld+json">')
    ld_end = page.find("</script>", ld_start)
    if ld_start < 0:
        raise BuildError("la plantilla no trae JSON-LD")
    page = page[:ld_start] + '<script type="application/ld+json">\n' + ld + "\n" + page[ld_end:]

    meta = {"lang": lang, "slug": slug, "tipo": tipo, "url": url, "canonical": canonical,
            "og_image": og_image, "minutos": minutos, "palabras": words,
            "secciones": sections, "categoria": fm["categoria"]}
    rel = f"blog/{slug}.html" if lang == "es" else f"{lang}/blog/{slug}.html"
    return page, meta, rel


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Genera un post del blog de 498advance.com")
    ap.add_argument("files", nargs="+", help="uno o varios blog498a_<lang>.md")
    ap.add_argument("--repo", default=str(REPO_DEFAULT), help="raiz publicable (498Adesign)")
    ap.add_argument("--out", help="directorio de salida alternativo")
    ap.add_argument("--dry-run", action="store_true", help="escribe en /tmp, no toca el repo")
    ap.add_argument("--build", action="store_true",
                    help="ejecuta _i18n/blog_build.py al terminar")
    ap.add_argument("--no-validate", action="store_true",
                    help="no pasar el validador sobre el HTML generado (no recomendado)")
    args = ap.parse_args(argv[1:])

    repo = Path(args.repo).expanduser()
    if not (repo / "blog").is_dir():
        print(f"No encuentro {repo}/blog. Usa --repo", file=sys.stderr)
        return 2
    if args.dry_run and args.build:
        print("--dry-run y --build son incompatibles", file=sys.stderr)
        return 2

    i18n = load_i18n(repo)
    validador = None if args.no_validate else cargar_validador()
    if validador is None and not args.no_validate:
        print("aviso: no encuentro validate_blog_498a.py, sigo sin validar", file=sys.stderr)
    dest_root = Path(args.out) if args.out else (
        Path(tempfile.mkdtemp(prefix="blog498a-")) if args.dry_run else repo)

    rc = 0
    hechos: list[dict] = []
    for raw in args.files:
        src = Path(raw)
        if not src.exists():
            print(f"[x] {raw}: no existe", file=sys.stderr)
            rc = 1
            continue
        try:
            page, meta, rel = build(src, repo, i18n)
        except BuildError as exc:
            print(f"[x] {src.name}: {exc}", file=sys.stderr)
            rc = 1
            continue
        out = dest_root / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page, encoding="utf-8")
        hechos.append(meta)
        print(f"[ok] {src.name} -> {out}")
        print(f"     {meta['palabras']} palabras · {meta['minutos']} min · "
              f"{len(meta['secciones'])} secciones · {meta['tipo']} · {meta['categoria']}")
        print(f"     canonical: {meta['canonical']}")
        if meta["canonical"] != meta["url"]:
            print("     pieza derivada: canonical fuera de 498advance.com. El texto NO puede "
                  "ser identico al original")
        print(f"     pendiente: imagen social 1200x630 en assets/og/{meta['slug']}.jpg"
              + ("  ·  csv y json en blog/datos/" if meta["tipo"] == "estudio" else ""))
        if validador is not None:
            avisos = validador.check_file(out)
            if avisos:
                print(f"     validador: {len(avisos)} aviso(s)")
                for a in avisos:
                    print(f"       · {a}")
                rc = 1
            else:
                print("     validador: sin avisos")

    if hechos and not args.dry_run:
        script = repo.parent / "_i18n" / "blog_build.py"
        if args.build and script.exists():
            print(f"\n== {script.name} ==")
            res = subprocess.run([sys.executable, str(script)], cwd=str(repo.parent))
            rc = rc or res.returncode
        else:
            print(f"\nAhora, para listados, sitemap, feeds y hreflang:\n"
                  f"  cd \"{repo.parent}\" && python3 _i18n/blog_build.py")
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv))
