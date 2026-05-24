#!/usr/bin/env python3
"""
generate_blog_main_image.py

Generador de imagenes principales (main + secondary) para blog posts
de Carlos Ortet, siguiendo el estilo canonico documentado en:
  /Users/cop/.claude/skills/content-factory/references/blog-main-image-style.md

Uso:
  python3 generate_blog_main_image.py \\
    --topic "Authority Boost servicio digital" \\
    --output /tmp/test_main.png \\
    [--prompt-extra "specific elements like a megaphone and graphs"] \\
    [--model gemini-3.1-flash-image-preview]

Requisitos:
  - Variable de entorno GOOGLE_GENERATIVE_AI_API_KEY definida
  - Pillow instalado (pip install pillow)
  - Acceso a internet (api Gemini)

Salida: PNG 1600x900 con el watermark de Gemini recortado.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import urllib.request
import urllib.error
from io import BytesIO
from pathlib import Path
from typing import Optional, Tuple

try:
    from PIL import Image
except ImportError:
    print("ERROR: Pillow no esta instalado. Ejecuta: pip3 install pillow")
    sys.exit(1)


# ----------------------------------------------------------------------------
# Configuracion del estilo canonico
# ----------------------------------------------------------------------------

CANONICAL_PROMPT_TEMPLATE = """Editorial flat vector illustration in the style of Quanta Magazine and Wired Ideas opinion section. A friendly fluffy yeti character with multiple small round white eyes (3 to 4 eyes arranged in a triangle on his face), a big happy smile showing square white teeth, long blonde shaggy fur covering most of his body, beige pinkish hands with 3 fingers, centered in the frame, frontal pose. The yeti is interacting with {props} that represent the topic of {topic}. Solid grape purple background, exact hex #6E3A7E, no gradient, no texture. The illustration is flat 2D vector style, no 3D, no isometric, no photorealism. Color palette is purple #6E3A7E for background, blonde beige #F4D9A3 for the yeti fur, red #E63946 for accent stickers or details, off white #FAFAFA for teeth and paper, with occasional secondary colors (blue, green, orange) only on small props. Friendly and playful but editorial and intelligent tone, like a magazine article hero image. No text overlays except small labels on stickers or cards if relevant. Aspect ratio 16:9, wide horizontal composition. High quality digital illustration, crisp vector lines, clean shapes."""

# Mapa de topic keywords a props sugeridos. Se usa heuristica simple para
# matchear y elegir props consistentes con el tema.
TOPIC_PROPS_MAP = {
    "fama": "wearing a HELLO MY NAME IS red sticker on his chest, with a silhouette of a crowd of people in the foreground holding up smartphones and cameras to take pictures of him",
    "viral": "wearing a HELLO MY NAME IS red sticker on his chest, with a silhouette of a crowd of people in the foreground holding up smartphones and cameras to take pictures of him",
    "atencion": "wearing a HELLO MY NAME IS red sticker on his chest, with a silhouette of a crowd of people in the foreground holding up smartphones and cameras to take pictures of him",
    "authority": "wearing a HELLO MY NAME IS red sticker on his chest, with a silhouette of a crowd of people in the foreground holding up smartphones and cameras to take pictures of him",
    "ml": "holding a fan of trading cards in his hands, each card showing a different ML concept written on it (World models, RL, Neuro-symbolic, Energy-based models, Program synthesis), the cards have colorful icons",
    "machine learning": "holding a fan of trading cards in his hands, each card showing a different ML concept written on it (World models, RL, Neuro-symbolic, Energy-based models, Program synthesis), the cards have colorful icons",
    "ia": "holding a fan of trading cards in his hands, each card showing a different AI concept written on it (LLMs, agents, RAG, embeddings, fine tuning), the cards have colorful icons",
    "musica": "playing a drum kit beside him, with a microphone stand and guitar leaning nearby",
    "creatividad": "playing a drum kit beside him, with a microphone stand and guitar leaning nearby",
    "datos": "surrounded by floating bar charts, pie charts and graph papers with simple data visualization",
    "analitica": "surrounded by floating bar charts, pie charts and graph papers with simple data visualization",
    "numeros": "surrounded by floating bar charts, pie charts and graph papers with simple data visualization",
    "ciudad": "with simplified flat buildings, traffic lights and a metro icon floating around him",
    "mobilidad": "with simplified flat buildings, traffic lights and a metro icon floating around him",
    "urbanismo": "with simplified flat buildings, traffic lights and a metro icon floating around him",
    "salud": "holding a stethoscope and surrounded by simple medical icons (heart, pill, plus sign)",
    "bienestar": "holding a stethoscope and surrounded by simple medical icons (heart, pill, plus sign)",
    "finanzas": "holding stacks of coins and floating dollar and euro symbols, with a simple line chart going up behind him",
    "dinero": "holding stacks of coins and floating dollar and euro symbols, with a simple line chart going up behind him",
    "tecnologia": "surrounded by floating smartphones, laptops and circuit board icons, holding a glowing chip in his hand",
    "gadgets": "surrounded by floating smartphones, laptops and circuit board icons, holding a glowing chip in his hand",
    "digital": "surrounded by floating smartphones, laptops and circuit board icons, holding a glowing chip in his hand",
    "servicio": "surrounded by floating smartphones, laptops and circuit board icons, holding a glowing chip in his hand",
}

FALLBACK_PROPS = "holding a magnifying glass and a notebook with question marks floating around him"

GENERATION_RES = (1920, 1080)  # bruto antes del crop
FINAL_RES = (1600, 900)         # final entregable
WATERMARK_MARGIN_PX = 80         # margen aproximado para limpiar la estrella Gemini


# ----------------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------------

def pick_props(topic: str, extra: Optional[str]) -> str:
    """Selecciona props segun el topic. Si hay --prompt-extra explicito, lo usa."""
    if extra and extra.strip():
        return extra.strip()
    topic_lower = topic.lower()
    for keyword, props in TOPIC_PROPS_MAP.items():
        if keyword in topic_lower:
            return props
    return FALLBACK_PROPS


def build_prompt(topic: str, extra: Optional[str]) -> str:
    """Construye el prompt final inyectando topic y props."""
    props = pick_props(topic, extra)
    return CANONICAL_PROMPT_TEMPLATE.format(topic=topic, props=props)


def call_gemini_image_api(prompt: str, model: str, api_key: str) -> bytes:
    """Llama a Nano Banana (Gemini) y devuelve los bytes PNG decodificados."""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"responseModalities": ["TEXT", "IMAGE"]},
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "x-goog-api-key": api_key,
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTPError {e.code} al llamar Gemini: {body}") from e
    except urllib.error.URLError as e:
        raise RuntimeError(f"URLError llamando Gemini: {e}") from e

    candidates = data.get("candidates", [])
    if not candidates:
        raise RuntimeError(f"Respuesta sin candidates. Body: {json.dumps(data)[:500]}")
    parts = candidates[0].get("content", {}).get("parts", [])
    for part in parts:
        inline = part.get("inlineData") or part.get("inline_data")
        if inline and inline.get("data"):
            return base64.b64decode(inline["data"])
    raise RuntimeError(f"No se encontro inlineData en la respuesta. Body: {json.dumps(data)[:500]}")


def crop_to_16_9_clean_watermark(img: Image.Image, target_size: Tuple[int, int]) -> Image.Image:
    """
    Recorta la imagen a ratio 16:9 final eliminando el watermark Gemini de la
    esquina inferior derecha. Estrategia: corta WATERMARK_MARGIN_PX de la
    parte inferior y derecha, luego ajusta proporcionalmente y reescala al
    tamaño final.
    """
    w, h = img.size

    # Paso 1: quitar pixeles del area del watermark (esquina inferior derecha).
    margin = WATERMARK_MARGIN_PX
    # Conservamos toda la parte izquierda y superior, recortamos abajo y derecha.
    cropped = img.crop((0, 0, max(1, w - margin), max(1, h - margin)))

    # Paso 2: ajustar a ratio 16:9 exacto centrando.
    cw, ch = cropped.size
    target_ratio = target_size[0] / target_size[1]
    current_ratio = cw / ch
    if current_ratio > target_ratio:
        # demasiado ancho, recortar laterales
        new_w = int(ch * target_ratio)
        left = (cw - new_w) // 2
        cropped = cropped.crop((left, 0, left + new_w, ch))
    elif current_ratio < target_ratio:
        # demasiado alto, recortar arriba y abajo (preferir conservar abajo
        # porque el watermark ya esta quitado; quitamos mas de arriba para no
        # decapitar al personaje, asi que cortamos por igual)
        new_h = int(cw / target_ratio)
        top = (ch - new_h) // 2
        cropped = cropped.crop((0, top, cw, top + new_h))

    # Paso 3: reescalar al tamaño final.
    return cropped.resize(target_size, Image.LANCZOS)


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Genera imagen principal de blog post con estilo canonico Carlos Ortet (yeti grape purple).",
    )
    parser.add_argument("--topic", required=True, help="Tema del post (ej: 'Authority Boost servicio digital').")
    parser.add_argument("--output", required=True, help="Ruta destino del PNG final.")
    parser.add_argument("--prompt-extra", default=None, help="Props explicitos para sobrescribir heuristica.")
    parser.add_argument("--model", default="gemini-3.1-flash-image-preview", help="Modelo Gemini a usar.")
    parser.add_argument("--keep-raw", action="store_true", help="Guarda tambien el PNG bruto sin crop, con sufijo .raw.png.")
    args = parser.parse_args()

    api_key = os.environ.get("GOOGLE_GENERATIVE_AI_API_KEY")
    if not api_key:
        print("ERROR: variable de entorno GOOGLE_GENERATIVE_AI_API_KEY no definida.")
        return 1

    output_path = Path(args.output).expanduser().resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    prompt = build_prompt(args.topic, args.prompt_extra)
    print(f"[1/3] Prompt construido ({len(prompt)} chars).")

    print(f"[2/3] Llamando a {args.model} ...")
    raw_bytes = call_gemini_image_api(prompt, args.model, api_key)
    raw_img = Image.open(BytesIO(raw_bytes)).convert("RGB")
    print(f"      Imagen bruta recibida: {raw_img.size}")

    if args.keep_raw:
        raw_path = output_path.with_suffix(".raw.png")
        raw_img.save(raw_path, "PNG")
        print(f"      Bruto guardado en: {raw_path}")

    print(f"[3/3] Crop y reescalado a {FINAL_RES[0]}x{FINAL_RES[1]} (limpiando watermark) ...")
    final_img = crop_to_16_9_clean_watermark(raw_img, FINAL_RES)
    final_img.save(output_path, "PNG", optimize=True)

    size_kb = output_path.stat().st_size // 1024
    print()
    print("OK.")
    print(f"  path : {output_path}")
    print(f"  size : {final_img.size[0]}x{final_img.size[1]} px, {size_kb} KB")
    print(f"  topic: {args.topic}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
