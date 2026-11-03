# Catalogo maestro de canales — WriterBatch Zoopa

## Blog (core)

**Los canales de blog dependen del destino** (PASO 1, pregunta 1 del SKILL). Los dos juegos
no son intercambiables y no se generan los dos a la vez salvo peticion explicita.

### Destino zoopa.es · WordPress + Polylang

| Canal | Archivo | Idioma | Por defecto |
|-------|---------|--------|-------------|
| Blog WordPress | `blog.md` | ES | SI |
| Blog WordPress | `blog_en.md` | EN | SI |
| Blog WordPress | `blog_ca.md` | CA | SI |
| Blog Lectura Facil | `blog_facil_es.md` | ES Facil | NO |

### Destino 498advance.com · blog estatico (Perspectivas)

| Canal | Archivo | Idioma | Por defecto |
|-------|---------|--------|-------------|
| Blog 498A | `blog498a_es.md` | ES | SI si el destino es 498advance.com |
| Blog 498A | `blog498a_ca.md` | CA | SI si el destino es 498advance.com |
| Blog 498A | `blog498a_en.md` | EN | SI si el destino es 498advance.com |
| Blog 498A | `blog498a_it.md` | IT | SI si el destino es 498advance.com |

> **OBLIGATORIO** leer `references/blog-498advance-static.md` antes de redactar cualquiera de
> los cuatro. No es WordPress: es HTML estatico con clases de `blog.css`, plantilla fija con
> `{{MARCADORES}}`, schema escrito a mano y constructor propio en el repo de la web. **NO** usar
> `blog-html-components.md` ni `wp_publish.py`. El **slug es el mismo en los cuatro idiomas**,
> igual que los `id` de seccion. El blog **no lleva frances**: `/fr/` enlaza al blog en ingles.
> Front matter, bloques de markdown soportados y pasos de publicacion, en la referencia.

## Redes sociales (core)

| Canal | Archivo | Idioma | Por defecto |
|-------|---------|--------|-------------|
| LinkedIn | `linkedin.md` | ES | SI |
| LinkedIn | `linkedin_ca.md` | CA | SI |
| X / Twitter | `x_twitter_ready.txt` | ES/EN/CA | SI |
| Threads | `threads_ready.txt` | ES | SI |
| Facebook (cuenta personal) | `facebook_personal.md` | ES | NO |
| Facebook (page Zoopa/498A) | `facebook_page.md` | ES | NO |

## Mensajeria (core)

| Canal | Archivo | Idioma | Por defecto |
|-------|---------|--------|-------------|
| WhatsApp Grupos | `whatsapp.md` | ES | SI |
| WhatsApp Grupos | `whatsapp_ca.md` | CA | SI |
| WhatsApp Canal | `whatsapp_channel_es.md` | ES | SI |
| WhatsApp Canal | `whatsapp_channel_ca.md` | CA | SI |
| Telegram | `telegram_ready.txt` | ES | NO |

## Newsletter y articulos

| Canal | Archivo | Idioma | Por defecto |
|-------|---------|--------|-------------|
| Substack | `substack_ready.txt` | ES | SI |
| Medium | `medium_article_ready.md` | EN | SI |

## Plataformas tech

| Canal | Archivo | Idioma | Por defecto |
|-------|---------|--------|-------------|
| Dev.to | `devto_ready.md` | EN | NO |
| Hashnode | `hashnode_ready.md` | EN | NO |
| Hacker News | `hackernews_ready.txt` | EN | NO |
| HackerNoon | `hackernoon_ready.md` | EN | NO |
| DZone | `dzone_ready.md` | EN | NO |
| Lobste.rs | `lobsters_ready.txt` | EN | NO |

## Reddit

| Canal | Archivo | Idioma | Por defecto |
|-------|---------|--------|-------------|
| Reddit (subreddit principal) | `reddit_ready.txt` | EN | NO |
| Reddit (subreddit secundario) | `reddit_2_ready.txt` | EN | NO |

## Plataformas descentralizadas / Web3

| Canal | Archivo | Idioma | Por defecto |
|-------|---------|--------|-------------|
| Mirror.xyz | `mirror_ready.md` | EN | NO |
| Farcaster (Warpcast) | `farcaster_ready.txt` | EN | NO |
| Mastodon | `mastodon_ready.txt` | EN | NO |
| Bluesky | `bluesky_ready.txt` | EN/ES | NO |

## Reviews y directorios

| Canal | Archivo | Idioma | Por defecto |
|-------|---------|--------|-------------|
| Trustpilot | `trustpilot_ready.txt` | ES | NO |
| Product Hunt | `producthunt_ready.txt` | EN | NO |
| G2 | `g2_ready.txt` | EN | NO |
| Capterra | `capterra_ready.txt` | EN | NO |

## Q&A y comunidades

| Canal | Archivo | Idioma | Por defecto |
|-------|---------|--------|-------------|
| Quora | `quora_ready.txt` | EN (70%) / ES (30%) | NO |
| Discord (servidores IA) | `discord_ready.txt` | EN | NO |

> **Quora:** ver `references/quora-best-practices.md` para requisitos de cuenta, formato de respuesta (600-1.200 palabras, 1 imagen min), reglas de idioma, anti-patrones, plantilla del `.txt` y prompt de extracción de preguntas desde source.md. Canal de alto valor GEO (citado por LLMs, long-tail 5-10 años).

## Video (si aplica)

| Canal | Archivo | Idioma | Por defecto |
|-------|---------|--------|-------------|
| YouTube Community | `youtube_community_ready.txt` | ES | NO |
| YouTube Shorts script | `youtube_shorts_script.txt` | ES | NO |
| Reels / TikTok script | `reels_script.txt` | ES | NO |

---

## Resumen

**Total disponible: 41 canales**
**Core por defecto: 12 canales** (los marcados SI)
**Idiomas: 5** (ES, EN, CA, IT, ES Facil) · el italiano solo en el blog de 498advance.com

Los canales marcados "SI" en "Por defecto" se generan siempre salvo que el usuario diga lo contrario. Los demas se generan solo si el usuario los selecciona explicitamente.
