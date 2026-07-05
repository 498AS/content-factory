# content-factory

> Multi-channel content production skill for Claude Code. Generates editorial-ready outputs for **35+ platforms** (blog WordPress, LinkedIn, Substack, Medium, X, Bluesky, Threads, Quora, Hacker News, Reddit, Mastodon, Facebook personal & page, WhatsApp, etc.) from a single source brief. Includes anti-LLM voice validators, platform mechanics playbook, image generation helper, and case studies.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![498AS](https://img.shields.io/badge/by-498AS-blue.svg)](https://498as.com)
[![Zoopa](https://img.shields.io/badge/with-Zoopa-orange.svg)](https://zoopa.es)

## Qué es

`content-factory` (codename **LEO** — The Ultimate Content Factory) es el skill de Claude Code que utilizamos en Zoopa / 498A para producir contenido editorial multicanal de calidad. Toma un brief de 3 bloques (`source.md`) y genera outputs listos para publicar en cada plataforma con las particularidades de cada una (char limits, formato, tono, anti-patrones).

Es parte del stack [GEORadar](https://georadar.app) (DOC · S.A.M. · LEO) que ofrecemos a clientes empresariales para construir presencia editorial coherente en LLMs y buscadores.

## No confundir con `linkedin-profile-optimizer`

Este skill produce **contenido** (posts, artículos, hilos) para 35+ plataformas, LinkedIn incluida. Su hermano [`linkedin-profile-optimizer`](https://github.com/498AS/linkedin-profile-optimizer) trabaja sobre **el activo**: audita y reescribe perfiles individuales y Pages de empresa (headline, About, experiencia, tagline), planifica SSI/ads/advocacy y estudia afinidad con perfiles objetivo.

| Necesitas… | Usa |
|------------|-----|
| Redactar un post/artículo/hilo para LinkedIn (u otro canal) | **`content-factory`** (este repo) |
| Optimizar o auditar un perfil o una Company Page de LinkedIn | [`linkedin-profile-optimizer`](https://github.com/498AS/linkedin-profile-optimizer) |
| Plan de personal branding, social selling, afinidad con un perfil objetivo | [`linkedin-profile-optimizer`](https://github.com/498AS/linkedin-profile-optimizer) |

## Cómo se usa

### Instalación

Copiar el skill a `~/.claude/skills/content-factory/`:

```bash
git clone https://github.com/498AS/content-factory.git ~/.claude/skills/content-factory
```

### Crear un proyecto nuevo

```bash
~/.claude/skills/content-factory/scripts/new-project.sh tema-del-post --paste
```

Crea `project_{ddmmaaaa}_{tema}/` con scaffolding `source.md` + `output/` + `metadata.json`.

### Invocar en Claude Code

Dentro de Claude Code en el directorio del workspace:

```
/content-factory
```

O simplemente: "lanza el content-factory con la pieza pillar primero".

## Estructura del repo

```
.
├── SKILL.md                         # Instrucciones principales del skill
├── README.md                        # Este archivo
├── references/                      # Style guides + playbooks por plataforma
│   ├── channel-catalog.md           # Catálogo maestro 37 canales
│   ├── content-brief-structure.md   # Formato source.md (3-block brief)
│   ├── editorial-patterns.md        # Killer line, paradoja, pull-quote
│   ├── blog-html-components.md      # Componentes HTML inline para WordPress
│   ├── blog-main-image-style.md     # Estilo visual main image (yeti editorial)
│   ├── linkedin-voice-carlos-ortet.md  # Voz LinkedIn personal validada
│   ├── substack-style.md            # Estilo email + permalink (no blog)
│   ├── x-twitter-voice-style.md     # Voz X anti-LLM (3.250 palabras)
│   ├── quora-best-practices.md      # Cuenta + format + cadencia
│   ├── orthography-rules.md         # Reglas globales (no em-dash, etc.)
│   ├── platform-mechanics.md        # ⭐ Playwright playbook per plataforma
│   └── lessons-learned.md           # Trampas operativas conocidas
├── scripts/
│   ├── new-project.sh               # Scaffolding nuevo proyecto
│   ├── metadata.py                  # CRUD metadata.json
│   ├── generate_blog_main_image.py  # Nano Banana auto-gen main image
│   ├── validators/
│   │   ├── run_all.py               # Wrapper que ejecuta todos los validators
│   │   ├── validate_anti_llm_patterns.py  # ⭐ Em-dash, temporales, frases IA
│   │   ├── validate_char_limits.py        # ⭐ Per-channel char limits
│   │   ├── validate_titles.py             # Sentence case + length
│   │   ├── validate_numbers.py            # Coherencia cifras
│   │   ├── validate_catalan.py            # Punt volat, ce trencada
│   │   └── validate_blog_completeness.py  # Estructura blog WP
│   └── publisher/
│       └── wp_publish.py            # WordPress REST API (Polylang + Rank Math)
├── case-studies/
│   ├── karma-boost-carlos-ortet-20260524.md         # Plan personal multi-plataforma
│   └── lecciones-publicacion-multicanal-AI-chips-20260524.md  # Cierre proyecto AI Chips
├── vault-notes/
│   ├── Content_Factory_Workspace.md       # Setup workspace inicial
│   ├── MOC Content Factory.md             # Mapa de Contenido vault
│   ├── playbook-publicacion-zoopa-3-idiomas-20260523.md
│   ├── guia-linkedin-voz-carlos-ortet-20260510.md
│   └── servicio-authority-boost-90-20260524.md     # Servicio comercial AB90
└── docs/                            # Documentación adicional (a expandir)
```

## Canales soportados (37)

### Blog & Newsletter (core)
- WordPress (ES/EN/CA) con Polylang Pro + Rank Math SEO
- Substack (ES) con preheader + cover image
- Medium (EN) via import-from-URL

### Redes sociales (core)
- LinkedIn personal + page (ES/CA)
- X / Twitter (hilos asimétricos)
- Threads (Meta cross-graph)
- Facebook personal nativo + Facebook Page institucional

### Mensajería
- WhatsApp Grupos (ES/CA)
- WhatsApp Canal (ES/CA)
- Telegram

### Plataformas tech
- Dev.to · Hashnode · HackerNoon · DZone · Lobste.rs

### Reddit
- 2 subreddits con flairs específicos

### Plataformas descentralizadas
- Mirror.xyz · Farcaster · Mastodon · Bluesky

### Q&A y comunidades
- Quora (long-tail SEO + LLM citation source)
- Hacker News
- Discord servers IA

### Reviews y directorios
- Trustpilot · Product Hunt · G2 · Capterra

### Video (si aplica)
- YouTube Community · YouTube Shorts script · Reels / TikTok script

Ver [`references/channel-catalog.md`](references/channel-catalog.md) para detalle completo.

## Idiomas soportados

ES (Castellano) · EN (English) · CA (Català) · ES Fácil (Lectura Fácil)

## Componentes clave

### 1. Validators (CI-ready)

**`validate_anti_llm_patterns.py`** — detecta y reporta:
- Em-dash (—) y en-dash (–) que delatan generación LLM
- Referencias temporales relativas ("esta semana", "este año", "today", etc.)
- Frases formulaicas ("Lectura completa con datos verificados", "delve into", "deep dive", etc.)
- Flechas → como bullets de lista
- Patrón HN auto-flag (bullet + empresa + país + cifra)

```bash
python3 scripts/validators/validate_anti_llm_patterns.py output/*.md output/*.txt
```

**`validate_char_limits.py`** — valida limits por canal:
- X 280 chars por tuit · Bluesky 300 · Threads 500 · Mastodon 500
- LinkedIn 3000 total · WhatsApp Canal 4096
- Reporta violations con offset y trim necesario

```bash
python3 scripts/validators/validate_char_limits.py output/x_twitter_ready.txt
```

### 2. Platform Mechanics Playbook

`references/platform-mechanics.md` documenta cómo automatizar publicación en cada plataforma vía Playwright CLI:
- URLs canónicas (handles correctos, slugs reales)
- Mecánica composer step-by-step
- Trampas conocidas (Bluesky email verification, FB Page slug, HN auto-flag)
- Selectores y refs dinámicos
- Verificación post-publicación

### 3. Voice Style Guides

- `linkedin-voice-carlos-ortet.md` — voz personal validada
- `substack-style.md` — email + permalink (NO blog WordPress condensado)
- `x-twitter-voice-style.md` — anti-LLM (3.250 palabras)
- `quora-best-practices.md` — long-tail SEO + cadencia 48h
- `orthography-rules.md` § 3 — reglas globales anti-LLM
- `blog-main-image-style.md` — estilo visual main image yeti editorial

### 4. Image generation helper

`scripts/generate_blog_main_image.py` — wrapper Nano Banana (Gemini) que:
- Usa el prompt template canónico del estilo Carlos Ortet
- Genera a 1920x1080
- Crop a 1600x900 quitando watermark Gemini
- Output PNG listo para blog WP / Substack cover

```bash
GOOGLE_GENERATIVE_AI_API_KEY=... python3 scripts/generate_blog_main_image.py \
  --topic "Authority Boost servicio digital" \
  --output ./main.png
```

## Caso de uso real

**Proyecto AI Chips Economy (24 may 2026)** publicó en:
- Blog WP (ES/EN/CA) con infografía
- Medium (EN)
- Substack (ES)
- LinkedIn personal (con vídeo nativo + URL en comentario)
- X (hilo 19 tuits)
- WhatsApp Canal
- Quora (1 de 4 answers, resto cadencia 48h auto-programada)
- Hacker News (submission + OP comment — OP flagged por low karma, ver case study)
- Bluesky (hilo 5 posts asimétrico)
- Threads (hilo 4 posts)
- FB Page Zoopa (versión institucional)
- FB personal Carlos (nativo long-form, URL en 1er comentario)
- carlosortet.com (publication entry con 5 links)

**12 canales activos** publicados desde una única `source.md` en ~6 horas.

→ Ver [`case-studies/lecciones-publicacion-multicanal-AI-chips-20260524.md`](case-studies/lecciones-publicacion-multicanal-AI-chips-20260524.md)

## Filosofía del skill

1. **Una fuente, muchos canales** — un solo brief estructurado produce contenido adaptado a cada plataforma
2. **Voz humana por defecto** — detectar y bloquear patrones de "voz IA" (em-dashes, antítesis formulaicas, listicles con cifras)
3. **Validar antes de publicar** — char limits, ortografía, completeness checks como parte del flow
4. **Automatizar la mecánica, no la voz** — Playwright para publish, no para escribir
5. **Iterar con cada proyecto** — `lessons-learned.md` crece con cada trampa encontrada

## Relación con el ecosistema Zoopa / 498A

- **DOC** (Diagnostic Optimization Checker) — optimiza la AX (Agent Experience) del sitio web destino antes de publicar
- **S.A.M.** (Semantic Alignment Machine) — valida que el contenido encaja con prompts target del nicho
- **LEO = este skill** — produce el contenido multicanal
- **GEORadar** — mide la presencia post-publicación en LLMs

Combinados ofrecen el servicio [**Authority Boost 90**](vault-notes/servicio-authority-boost-90-20260524.md) (plan integral 90 días para autoridad digital).

## Contribuir

Este skill se itera con cada proyecto real publicado. Si encuentras una trampa nueva en una plataforma:

1. Añade nota a `references/lessons-learned.md` + sección correspondiente en `references/platform-mechanics.md`
2. Si afecta validación, ampliar pattern en `scripts/validators/`
3. PR a este repo

## Licencia

MIT (excepto las case-studies que pueden contener data de cliente — verifica antes de redistribuir).

## Maintainers

- **Carlos Ortet** ([carlosortet.com](https://carlosortet.com)) · CEO Zoopa · Director 498A
- **Mer Canet** · Operaciones contenido
- **Community lead GEORadar** · Medición LLM visibility

## Links

- [Zoopa](https://zoopa.es) · Innovation & Creative Technology
- [498AS](https://498as.com) · AI R&D Division
- [GEORadar](https://georadar.app) · LLM brand visibility
- [carlosortet.com](https://carlosortet.com) · Speaker bio + publications

---

*Skill iniciado en 2025. Repo público creado 2026-05-24 tras consolidación de aprendizajes de 15+ proyectos editoriales multicanal.*
