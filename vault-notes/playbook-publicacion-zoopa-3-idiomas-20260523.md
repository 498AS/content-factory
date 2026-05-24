---
date: 2026-05-23
type: playbook
tags: [zoopa, wordpress, publicacion, polylang, seo, geo, contentfactory]
project: contentfactory
related: [content-factory-skill, GEORadar]
---

# Playbook · Publicación 3-idiomas a zoopa.es vía API REST

> Caso de estudio: **Proyecto AI Chips Economy** (mayo 2026, 3 posts ES+EN+CA publicados en ~12 minutos)
>
> URLs publicadas:
> - ES — https://zoopa.es/es/geo-ia-visibilidad/tejido-invisible-ia-chips-geopolitica/
> - EN — https://zoopa.es/en/innovation-technology/invisible-fabric-ai-chips-geopolitics/
> - CA — https://zoopa.es/ca/innovacio-tecnologia/teixit-invisible-ia-xips-geopolitica/

---

## Por qué este playbook

Publicar un artículo largo (3.500-8.000 palabras con componentes HTML inline, key takeaways, stat blocks, pull-quotes, glosarios y FAQ) en zoopa.es en los tres idiomas que soporta Polylang Pro es una operación con bastantes piezas móviles. Si se hace bien, lleva 10-15 minutos. Si se hace mal, lleva horas (categorías rotas, traducciones desvinculadas, imágenes 404, meta description vacía, posts huérfanos en categoría "Sin categoría").

Este playbook documenta el flujo exacto que funcionó para el primer artículo de IA del laboratorio 498A publicado en zoopa.es, y deja los 4 scripts Python reutilizables que se usaron.

---

## Pre-requisitos

### Credenciales

Variables de entorno (o archivo `_system/.wp-credentials` gitignored con `chmod 600`):

```bash
export WP_USER="admzoopa"
export WP_APP_PASSWORD="UvOB ct5T JAhC JIrD 0yg0 1hKI"
export WP_SITE="https://zoopa.es"
```

Cargar al inicio de cada sesión: `source _system/.wp-credentials`.

### Source preparado

Archivos `output/blog.md`, `output/blog_en.md`, `output/blog_ca.md` con:

1. **Bloque SEO al inicio** (comentario HTML que NO se publica):
   ```
   <!--
   Title: ...
   Meta description: ... (≤155 chars)
   Slug: ...
   Focus keyword: ...
   Canonical: https://zoopa.es/{es|en|ca}/blog/...
   -->
   ```
2. **H1 del artículo** debajo del bloque.
3. **Componentes HTML inline** (figure, divs con estilos, blockquote pull-quote, etc.).
4. **Imágenes con paths locales** (`AI-diplomacy-Tara-Jacoby.jpg`) — se reemplazarán por URLs WP tras subir.

### Decisiones tomadas antes de arrancar

- **Web destino**: zoopa.es
- **Autor**: Carlos Ortet (`author_id=7`)
- **Categorías por idioma** (ver tabla abajo)
- **Status**: `publish` directo o `draft` para revisión
- **Slugs por idioma** (idempotentes, sin acentos)

---

## Mapa de categorías zoopa.es (mayo 2026)

### ES (cluster nuevo abril 2026)

| ID | Slug | Nombre |
|---|---|---|
| 2231 | geo-ia-visibilidad | GEO, IA y Visibilidad en Buscadores de IA |
| 2233 | social-media-es | Social Media |
| 2235 | creatividad-contenido | Creatividad y Contenido |
| 2237 | innovacion-tecnologia | Innovación y Tecnología |
| 2239 | estrategia-marketing-digital | Estrategia y Marketing Digital |
| 2241 | branding-ux-diseno | Branding, UX y Diseño |
| 2243 | influencer-marketing-es | Influencer Marketing |
| 2245 | produccion-audiovisual | Producción Audiovisual |

### EN (creadas mayo 2026 para este proyecto)

| ID | Slug | Nombre | Traducción de |
|---|---|---|---|
| 2253 | innovation-technology | Innovation and Technology | 2237 |
| 2257 | geo-ai-visibility | GEO, AI and Visibility in AI Search Engines | 2231 |

### CA (creadas mayo 2026 para este proyecto)

| ID | Slug | Nombre | Traducción de |
|---|---|---|---|
| 2255 | innovacio-tecnologia | Innovació i Tecnologia | 2237 |
| 2259 | geo-ia-visibilitat | GEO, IA i Visibilitat en Cercadors d'IA | 2231 |

**Regla de oro**: si publicas un post EN/CA en una categoría que solo existe en ES, créala antes con script (ver abajo). Si no, el post acaba en "Sin categoría" y no aparece en los listings de Elementor del blog.

---

## Flujo completo en 6 pasos (~12 minutos)

### PASO 1 · Actualizar URLs canonical y CTAs en los `.md` locales

Cambiar todas las menciones de 498as.com → zoopa.es:

- **Canonical**: `https://zoopa.es/{es|en|ca}/blog/{slug}/`
- **Mid-CTA box**: link al cluster relevante, e.g. `/es/servicios/georadar/`
- **Final-CTA**: `/es/contactanos/`, `/en/contact-us/`, `/ca/contactans/`

### PASO 2 · Subir las 3 imágenes a la media library

Usar `curl` con `-F file=@...` (formdata):

```bash
curl -s -X POST "$WP_SITE/wp-json/wp/v2/media" \
  -u "$WP_USER:$WP_APP_PASSWORD" \
  -F "file=@AI-diplomacy-Tara-Jacoby.jpg" \
  -F "alt_text=descripción SEO sin acentos para evitar bug encoding" \
  -F "caption=Ilustracion: Tara Jacoby" \
  -F "title=El tejido invisible de la IA" > /tmp/hero.json

python3 -c "import json; d=json.load(open('/tmp/hero.json')); print(f'ID={d[\"id\"]} URL={d[\"source_url\"]}')"
```

⚠️ **Caracteres no-ASCII en `alt_text` pueden fallar con form-data**. Subir con texto sin acentos y actualizar después vía PATCH JSON.

### PASO 3 · Crear categorías EN/CA traducidas (si no existen)

Script `_create_translated_categories.py`:

```python
# Polylang Pro: lang directo en POST + translations field para vincular
res = call("POST", "/wp-json/wp/v2/categories", {"name": "...", "slug": "...", "lang": "en"})
new_id = res["id"]
call("POST", f"/wp-json/wp/v2/categories/{new_id}",
     {"translations": {"es": ES_ID, "en": new_id}})
```

### PASO 4 · Crear los 3 posts

Script `_publish.py` por idioma:

```bash
python3 _publish.py output/blog.md es {SLUG_ES} {HERO_ID} {HERO_URL} {RC1_URL} {RC2_URL} "2231,2237"
python3 _publish.py output/blog_en.md en {SLUG_EN} {HERO_ID} {HERO_URL} {RC1_URL} {RC2_URL} "2257,2253"
python3 _publish.py output/blog_ca.md ca {SLUG_CA} {HERO_ID} {HERO_URL} {RC1_URL} {RC2_URL} "2259,2255"
```

El script:
1. Lee el `.md` y parsea el bloque SEO metadata.
2. Strippea el H1 (se setea separado como title).
3. Reemplaza paths locales de imágenes por URLs WP.
4. Convierte Markdown a HTML con `markdown` extensions `extra, tables, sane_lists`.
5. POST al endpoint con autor, featured_media, categorías, lang, excerpt.
6. **OBLIGATORIO**: header `User-Agent: Mozilla/5.0` para evitar CloudFlare 403 / error 1010.

### PASO 5 · Vincular traducciones Polylang + Rank Math SEO

Script `_link_and_seo.py`:

```python
TRANSLATIONS = {"es": POST_ES, "en": POST_EN, "ca": POST_CA}
for lang, post_id in TRANSLATIONS.items():
    call("POST", f"/wp-json/wp/v2/posts/{post_id}", {"translations": TRANSLATIONS})

# Rank Math meta (set en cada post)
call("POST", f"/wp-json/wp/v2/posts/{post_id}", {
    "meta": {
        "rank_math_title": SEO["title"],
        "rank_math_description": SEO["description"],
        "rank_math_focus_keyword": SEO["focus_keyword"],
    }
})
```

### PASO 6 · Verificación post-publicación

```python
URLS = {"ES": "...", "EN": "...", "CA": "..."}
for lang, url in URLS.items():
    html = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})).read().decode()
    h1_count = len(re.findall(r"<h1[^>]*>", html))
    hreflangs = re.findall(r'hreflang="([^"]+)"\s+href="([^"]+)"', html)
    og_image = re.search(r'<meta property="og:image"\s+content="([^"]+)"', html)
    meta_desc = re.search(r'<meta name="description"\s+content="([^"]+)"', html)
    assert h1_count == 1
    assert og_image
    assert meta_desc
    assert len(hreflangs) >= 3  # las 3 traducciones cross-linked
```

---

## Gotchas y solutions (lecciones reales mayo 2026)

| Síntoma | Causa | Solución |
|---|---|---|
| HTTP 403 + `error code: 1010` | CloudFlare WAF bloquea User-Agent vacío | `User-Agent: Mozilla/5.0 (...)` en todo request |
| Post EN/CA acaba en "Sin categoría" | Categoría asignada solo existe en ES | Crear categoría traducida primero (paso 3) |
| Translations vacía contenido del post | Asignar lang+translations+content en llamadas separadas | Hacer `translations` SOLO después de que post ya tiene content |
| Meta description vacía | Rank Math meta no se aplicó | Setear `excerpt` también como fallback |
| Imagen no aparece como featured | Dialogo de WordPress no fiable | Asignar `featured_media: ID` directo en POST |
| Timeout `No route to host` | Rate limit CloudFlare por burst de POSTs | Esperar 15-30 min o cambiar a 4G |
| Post no aparece en blog page | Categoría legacy ("Blog" ID 26) que el widget Elementor no muestra | Reasignar a categoría nueva (cluster 2231-2245) |
| Alt text con acentos roto | curl form-data encoding | ASCII en alt_text inicial, actualizar luego con PATCH JSON |

---

## Scripts del proyecto (reutilizables)

Los 4 scripts viven en `proyecto-AI-chips-economy-23052026/` y se pueden copiar a futuros proyectos:

1. **`_publish.py`** — Crear 1 post desde un .md
2. **`_create_translated_categories.py`** — Crear cats EN/CA como traducciones de ES
3. **`_link_and_seo.py`** — Vincular Polylang + Rank Math meta
4. **`_update_posts.py`** — Re-renderizar y actualizar posts existentes (para iteraciones editoriales)

Todos usan urllib/json (sin dependencias externas más allá de `markdown`).

---

## Estructura URL final por idioma

`zoopa.es/{lang}/{category-slug}/{post-slug}/`

Donde category-slug es la PRIMERA categoría asignada (por orden numérico de IDs).

Si quieres una URL específica, asegúrate de que la categoría destino tenga el menor ID en la lista que asignas al post.

---

## Próxima iteración del playbook

- **Schema JSON-LD Article**: Rank Math Free no lo genera. Para maximizar GEO (citabilidad LLMs), activar schema Article en Rank Math admin o pasar a Rank Math Pro.
- **Cache Cloudflare purge**: tras update de un post, purgar URL específica con skill `cf-purge-zoopa` para forzar refresh.
- **Translations en una sola llamada al crear**: probar si pasar `translations` ya en el POST inicial funciona (en lugar de en llamada separada). Reduciría a 1 call por idioma.

---

*Caso de estudio: AI Chips Economy · 23 de mayo de 2026 · Carlos Ortet*
