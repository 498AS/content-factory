# -*- coding: utf-8 -*-
"""Imagen social 1200x630 de un post del blog de 498advance.com.

Mismo procedimiento que _i18n/og_build.py del repo de la web (Chrome headless sobre
una plantilla HTML con las fuentes de marca, y magick para el JPG), con la
composicion de un post en lugar de la de la home: categoria como eyebrow, titular
en Hepta Slab cursiva y fecha al pie.

Uso:
  python3 og_498a_post.py project_XXX/output/blog498a_es.md
  python3 og_498a_post.py project_XXX/output/blog498a_es.md --repo /ruta/498Adesign

Escribe 498Adesign/assets/og/<slug>.jpg. El slug es el mismo en los cuatro idiomas,
asi que basta generarla una vez, desde el fichero del idioma que se quiera.
"""

import argparse
import base64
import pathlib
import re
import subprocess
import sys

REPO_DEFAULT = pathlib.Path(
    "/Users/carlos/Documents/claudecode-proj/design system 498A/498Adesign"
)
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
# Fondo por defecto. Cada post puede llevar el suyo con "fondo:" en el front
# matter, para que el listado no parezca trece veces la misma imagen.
FONDO = "assets/visuals/sc-simulation-cube.jpg"
LOGO = "assets/logos/498A_ADVANCED_white.svg"

MESES = {"01": "enero", "02": "febrero", "03": "marzo", "04": "abril", "05": "mayo",
         "06": "junio", "07": "julio", "08": "agosto", "09": "septiembre",
         "10": "octubre", "11": "noviembre", "12": "diciembre"}

TPL = """<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Hepta+Slab:ital,wght@1,300&family=Roboto+Mono:wght@500&display=swap" rel="stylesheet">
<style>
 *{margin:0;padding:0;box-sizing:border-box}
 body{width:1200px;height:630px;background:#000;overflow:hidden;position:relative;color:#fff}
 .bg{position:absolute;inset:0;background:url('{{IMG}}') center/cover no-repeat;filter:saturate(1.05) contrast(1.05)}
 .scrim{position:absolute;inset:0;background:linear-gradient(100deg, rgba(0,0,0,.95) 0%, rgba(0,0,0,.88) 42%, rgba(0,0,0,.4) 68%, rgba(0,0,0,.18) 100%)}
 .edge{position:absolute;inset:0;box-shadow:inset 0 0 160px 40px rgba(0,0,0,.65)}
 .wrap{position:relative;height:100%;padding:66px 80px;display:flex;flex-direction:column;justify-content:space-between}
 .top{display:flex;align-items:center;gap:20px}
 .logo{height:46px}
 .rule{flex:0 0 42px;height:1px;background:#2DD60F}
 .eyebrow{font-family:'Roboto Mono',monospace;font-size:16px;letter-spacing:3.2px;text-transform:uppercase;color:#2DD60F}
 .title{font-family:'Hepta Slab',Georgia,serif;font-style:italic;font-weight:300;
        font-size:{{SIZE}}px;line-height:1.14;max-width:1000px;color:#fff;letter-spacing:-.5px}
 .title em{color:#2DD60F;font-style:italic}
 .foot{display:flex;justify-content:space-between;align-items:flex-end;
       font-family:'Roboto Mono',monospace;font-size:16px;letter-spacing:2.4px;text-transform:uppercase}
 .foot .dom{color:#2DD60F}
 .foot .meta{color:#9a9a9a}
</style></head><body>
<div class="bg"></div><div class="scrim"></div><div class="edge"></div>
<div class="wrap">
  <div class="top"><img class="logo" src="{{LOGO}}" alt=""><span class="rule"></span><span class="eyebrow">{{EYEBROW}}</span></div>
  <div class="title">{{TITLE}}</div>
  <div class="foot"><span class="dom">498advance.com/blog</span><span class="meta">{{META}}</span></div>
</div></body></html>"""


def b64(path: pathlib.Path) -> str:
    mime = {"jpg": "image/jpeg", "jpeg": "image/jpeg", "png": "image/png",
            "webp": "image/webp", "svg": "image/svg+xml"}[path.suffix.lstrip(".").lower()]
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()


def front_matter(md: pathlib.Path) -> dict:
    out = {}
    lines = md.read_text(encoding="utf-8").splitlines()
    for line in lines[1:]:
        if line.strip() == "---":
            break
        m = re.match(r'^([a-z_0-9]+):\s*"?(.*?)"?\s*$', line)
        if m:
            out[m.group(1)] = m.group(2)
    return out


def main(argv):
    ap = argparse.ArgumentParser(description="Imagen social de un post del blog 498A")
    ap.add_argument("file", help="blog498a_<lang>.md")
    ap.add_argument("--repo", default=str(REPO_DEFAULT))
    ap.add_argument("--quality", type=int, default=88)
    args = ap.parse_args(argv[1:])

    repo = pathlib.Path(args.repo).expanduser()
    fm = front_matter(pathlib.Path(args.file))
    for clave in ("slug", "titulo_h1", "categoria", "fecha"):
        if not fm.get(clave):
            print(f"falta '{clave}' en el front matter", file=sys.stderr)
            return 2

    titulo = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", fm["titulo_h1"])
    plano = re.sub(r"<[^>]+>", "", titulo)
    size = 54 if len(plano) <= 78 else (46 if len(plano) <= 104 else 40)
    anio, mes, dia = fm["fecha"].split("-")
    meta = f"{int(dia)} de {MESES[mes]} de {anio}"

    html = TPL
    fondo = (fm.get("fondo") or FONDO).strip()
    if not (repo / fondo).exists():
        raise SystemExit(f"el fondo no existe en el repo: {fondo}")
    for k, v in {"{{IMG}}": b64(repo / fondo), "{{LOGO}}": b64(repo / LOGO),
                 "{{EYEBROW}}": fm["categoria"], "{{TITLE}}": titulo,
                 "{{META}}": meta, "{{SIZE}}": str(size)}.items():
        html = html.replace(k, v)

    tmp_html = pathlib.Path(f"/tmp/og_post_{fm['slug']}.html")
    tmp_html.write_text(html, encoding="utf-8")
    png = f"/tmp/og_post_{fm['slug']}.png"
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
                    f"--screenshot={png}", "--window-size=1200,630",
                    "--default-background-color=000000", f"file://{tmp_html}"],
                   capture_output=True)
    if not pathlib.Path(png).exists():
        print("Chrome no genero la captura", file=sys.stderr)
        return 1
    destino = repo / "assets" / "og" / f"{fm['slug']}.jpg"
    destino.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["magick", png, "-quality", str(args.quality), str(destino)],
                   capture_output=True)
    if not destino.exists():
        print("magick no genero el jpg (brew install imagemagick)", file=sys.stderr)
        return 1
    print(f"[ok] {destino}  {destino.stat().st_size // 1024} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
