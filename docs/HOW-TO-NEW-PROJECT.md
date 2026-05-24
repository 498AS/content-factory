# Cómo arrancar un proyecto nuevo de Content Factory

> Cheat-sheet rápido. Imprimir o tener a mano.

---

## TL;DR (90 segundos)

```bash
cd /Users/cop/Documents/claudecode-proj/contentfactory
claude --dangerously-skip-permissions
./_system/new-project.sh tema-corto       # crea la estructura
# pegar el source.md
```

Y en el chat de Claude:

```
/content-factory project_DDMMAAAA_tema-corto
```

---

## Flujo paso a paso

### 1. Abrir terminal en el directorio correcto

**CRÍTICO:** Claude debe arrancarse desde `contentfactory/`. Si no, los paths relativos (`_system/...`, `project_XXX/...`) no resuelven.

```bash
cd /Users/cop/Documents/claudecode-proj/contentfactory
claude --dangerously-skip-permissions
```

### 2. Crear estructura del proyecto

```bash
# Modo interactivo: te pide el tema
./_system/new-project.sh

# Con tema en argumento
./_system/new-project.sh small-llms

# Con tema + source.md desde portapapeles
./_system/new-project.sh small-llms --paste
```

Esto crea:
- `project_DDMMAAAA_tema/source.md` (vacío o con tu portapapeles)
- `project_DDMMAAAA_tema/output/` (donde se generan los outputs)
- `project_DDMMAAAA_tema/metadata.json` (schema vacío listo para registrar publicaciones)

### 3. Pegar el contenido fuente en `source.md`

El `source.md` debe contener **tres bloques**:

1. **Tesis** (1 párrafo, 80 palabras) — la afirmación que vas a defender
2. **Hechos curados** (5-12 bullets con cifra + fuente + fecha)
3. **Ángulo de marca** (2-5 bullets con tu posición, anécdotas reales, recomendaciones)

> **El error a evitar:** tratar `source.md` como un research dump genérico. La skill puede sintetizar lo que le des, pero no inventa el ángulo. Si quieres calidad de salida, dale calidad de entrada.

### 4. Lanzar la skill

En el chat de Claude (cualquiera de estos sirve):

```
/content-factory project_DDMMAAAA_tema
lanza el proyecto project_DDMMAAAA_tema
launch project_DDMMAAAA_tema
writerbatch project_DDMMAAAA_tema
```

### 5. Responder a PASO 0 (canales)

La skill te lista 35 canales y te confirma los 12 core por defecto:
- Blog WordPress (ES, EN, CA)
- LinkedIn (ES, CA)
- X/Twitter (ES/EN/CA)
- Threads
- WhatsApp Grupos (ES, CA), WhatsApp Canal (ES, CA)
- Substack, Medium

Añade o quita lo que quieras. Recomendaciones:
- Si el tema es **AI / GEO / tech** → añade Dev.to, Hashnode, HackerNoon, Hacker News, Reddit
- Si es **producción audiovisual / branded content** → añade YouTube Shorts, Reels, Behance project, LBB op-ed
- Si es **personal / opinión** → Substack core + Carlos personal LinkedIn Article
- Si NO es para audiencia developer → quita Dev.to, Hashnode, HN

### 6. Responder a PASO 1 (pre-publicación)

| Pregunta | Respuesta típica |
|----------|------------------|
| Web | zoopa.es (audiovisual/marketing) o 498as.com (AI/GEO) |
| Autor | Carlos Ortet |
| LinkedIn | ZOOPA / 498AS / Carlos personal |
| Tema nuevo o existente | si existe, enlazar a posts previos |
| Imagen principal | path local o URL |
| Imagen secundaria | opcional |

### 7. Generación automática (PASOS 2-3-3.5-3.6-4)

La skill genera todos los outputs en `project_XXX/output/`:
- Blog (ES/EN/CA) con SEO+GEO completo (metadatos, key takeaways, mid+final CTAs, glosario, FAQ ≥5, alt text)
- Social (LinkedIn ES/CA, X/Twitter, Threads, WhatsApp Canal ES/CA, Substack, Medium)
- Cualquier canal extra que hayas seleccionado

**Validators automáticos** corren tras cada `Write`/`Edit`:
- `validate_titles.py` — sentence case
- `validate_numbers.py` — false friends (billion/billón)
- `validate_catalan.py` — ç, l·l, etc. en archivos `*_ca.md`
- `validate_blog_completeness.py` — bloque SEO, takeaways, CTAs, glosario, FAQ ≥5, alt text, 1 H1, palabras mínimas

### 8. Publicación en zoopa.es (PASO 5, opcional)

Cuando me digas "publica en el blog", uso el publisher API REST:

```bash
# Con env vars WP_USER y WP_APP_PASSWORD configuradas:
python3 _system/publisher/wp_publish.py \
  --file project_XXX/output/blog.md \
  --lang es --categories 2245,2235 \
  --status draft           # o publish
```

Luego registra automáticamente en `metadata.json`.

### 9. Registrar publicaciones (cuando publiques en otros canales)

```bash
python3 _system/metadata.py add-publication project_XXX \
  --channel linkedin_article_personal_es \
  --url https://linkedin.com/pulse/...
```

Ver `_system/metadata-schema.md` para el schema completo.

---

## Carpeta del proyecto resultante

```
project_DDMMAAAA_tema/
├── source.md                              # tu input
├── metadata.json                          # registro de publicaciones y métricas
└── output/
    ├── blog.md                            # canónico ES (publicar primero)
    ├── blog_en.md                         # native EN
    ├── blog_ca.md                         # natural CA
    ├── linkedin.md                        # post 300 palabras (ZOOPA)
    ├── linkedin_ca.md                     # post 300 palabras CA
    ├── linkedin_article_carlos_es.md      # opcional: long-form Pulse Carlos personal
    ├── x_twitter_ready.txt                # hilo ES + EN
    ├── threads_ready.txt                  # hilo ES
    ├── whatsapp_channel_es.md             # canal directo
    ├── whatsapp_channel_ca.md             # canal directo CA
    ├── substack_ready.txt                 # newsletter
    ├── medium_article_ready.md            # adaptación EN con canonical
    ├── youtube_shorts_script.txt          # 45-60s
    ├── reels_script.txt                   # 30-45s
    ├── pitches_trade.md                   # opcional: pitches a prensa trade
    ├── ugc_strategy.md                    # opcional: plan UGC
    └── hackernoon_ready.md                # opcional EN tech-cultural
```

---

## Archivos del sistema (no tocar a menos que sepas)

```
_system/
├── system_prompt_writerbatch_zoopa.md    # voz, estilo, specs por canal
├── launch.md                             # mirror local de la skill global
├── new-project.sh                        # script de creación
├── metadata.py                           # CLI helper para metadata.json
├── metadata-schema.md                    # documentación del schema
├── workflow.md                           # SOP narrativa
├── readme.md                             # arquitectura del sistema
├── HOW-TO-NEW-PROJECT.md                 # este archivo
├── publisher/
│   ├── wp_publish.py                     # publicación API REST WordPress
│   └── publish_config.md                 # config Playwright sesiones
└── validators/
    ├── run_all.py                        # entry point hook
    ├── validate_titles.py
    ├── validate_numbers.py
    ├── validate_catalan.py
    └── validate_blog_completeness.py
```

---

## Skill global (canónica)

`~/.claude/skills/content-factory/SKILL.md`

Las referencias adicionales (catálogo de 35 canales, ortografía, lecciones aprendidas, componentes HTML para blogs) viven en `~/.claude/skills/content-factory/references/`.

---

## Si algo falla

| Síntoma | Causa probable | Solución |
|---------|----------------|----------|
| `_system: No such file or directory` | No estás en `contentfactory/` | `cd /Users/cop/Documents/claudecode-proj/contentfactory` |
| `validators no responden` | Hook no cargado al iniciar Claude | Reiniciar Claude Code en este directorio |
| `WP_APP_PASSWORD not set` al publicar | Env var no exportada | Exportar `WP_USER` y `WP_APP_PASSWORD` antes de publicar |
| `slug ya en uso` al publicar | Hay un post con ese slug | Cambiar slug en el bloque de metadatos del .md |
| `categoria 404 en idioma X` | Faltan categorías nuevas en EN/CA | Crear vía API con `lang` + `translations` |

---

## Triggers que reconoce la skill

Cualquiera de estos en el chat:

- `/content-factory <project_id>`
- `lanza el proyecto <project_id>`
- `launch <project_id>`
- `writerbatch <project_id>`
- `vamos a hacer un proyecto sobre <tema>` (la skill crea la carpeta primero)

---

*Última actualización: 2026-05-03 — versión sincronizada con SKILL.md global.*
