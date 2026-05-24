# metadata.json — Schema por proyecto

Cada proyecto tiene un `metadata.json` en su raiz. Captura que se generó, donde se publicó y, opcionalmente, metricas.

Es la unica fuente persistente de "que pasó con este contenido", y permite analisis transversal (ej: "que tipo de source.md genera mas trafico").

---

## Schema

```json
{
  "project_id": "project_02052026_tema",
  "created_at": "2026-05-02T10:00:00Z",
  "source_words": 1480,
  "system_prompt_version": "2.0",

  "channels_generated": ["blog_es", "blog_en", "blog_ca", "linkedin_es", "..."],

  "published": {
    "blog_es": {
      "url": "https://zoopa.es/blog/...",
      "wp_post_id": 12345,
      "published_at": "2026-05-02T11:30:00Z",
      "categories": [2231],
      "featured_media": 9876
    },
    "blog_en": { "...": "..." },
    "blog_ca": { "...": "..." },
    "linkedin_es": {
      "url": "https://linkedin.com/posts/...",
      "published_at": "2026-05-02T12:00:00Z",
      "account": "Carlos Ortet"
    },
    "substack_es": {
      "url": "https://carlosortet.substack.com/p/...",
      "published_at": "2026-05-02T12:30:00Z"
    }
  },

  "metrics": {
    "blog_es": {
      "views_30d": null,
      "search_clicks_30d": null,
      "last_pulled": null
    },
    "linkedin_es": {
      "impressions_7d": null,
      "reactions_7d": null,
      "comments_7d": null,
      "last_pulled": null
    }
  },

  "tags": ["GEO", "ChatGPT"],
  "notes": ""
}
```

---

## Campos

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| `project_id` | string | Nombre de la carpeta (`project_DDMMAAAA_tema`) |
| `created_at` | ISO-8601 UTC | Cuando se creó el proyecto |
| `source_words` | int \| null | Palabras de `source.md` (rellenar tras crear source) |
| `system_prompt_version` | string | Version del system prompt usada |
| `channels_generated` | string[] | Keys de canal (ver convencion abajo) |
| `published[<canal>]` | object | Datos de publicacion por canal |
| `metrics[<canal>]` | object | Metricas por canal (rellenadas async) |
| `tags` | string[] | Topicos para agrupacion analitica |
| `notes` | string | Notas libres |

### Convencion de keys de canal

`<canal_base>_<idioma>`. Ejemplos:

- `blog_es`, `blog_en`, `blog_ca`, `blog_facil_es`
- `linkedin_es`, `linkedin_ca`
- `whatsapp_grupo_es`, `whatsapp_grupo_ca`, `whatsapp_canal_es`, `whatsapp_canal_ca`
- `substack_es`, `medium_en`, `devto_en`, `hashnode_en`, `hackernoon_en`
- `x_twitter`, `threads_es`, `bluesky`, `mastodon`
- `reddit_es` o subreddit name, `hackernews`
- `youtube_community_es`, `youtube_shorts_es`, `reels_es`

---

## Campos por tipo de canal

### Canales con WordPress (blog_*)

| Campo | Obligatorio |
|-------|-------------|
| `url` | si |
| `wp_post_id` | si |
| `published_at` | si |
| `categories` | si (IDs) |
| `featured_media` | si (ID del attachment) |

### Canales web simples (linkedin, substack, medium, etc.)

| Campo | Obligatorio |
|-------|-------------|
| `url` | si |
| `published_at` | si |
| `account` | opcional (cuando hay multiples cuentas) |

### Canales sin URL fija (whatsapp, telegram-groups)

| Campo | Obligatorio |
|-------|-------------|
| `published_at` | si |
| `groups` | array opcional |

---

## Cuando se actualiza

| Momento | Que rellena |
|---------|-------------|
| `new-project.sh` | `project_id`, `created_at`, `source_words` (si --paste), versiones |
| Skill al generar (PASO 4) | `channels_generated` |
| Skill al publicar (PASO 5) | `published[<canal>]` para cada canal publicado |
| Job semanal externo (futuro) | `metrics[<canal>]` |

---

## Helper CLI

`_system/metadata.py` ofrece:

```bash
# Inicializar (si no existe)
python3 _system/metadata.py init project_XXX

# Marcar canales generados
python3 _system/metadata.py set-generated project_XXX --channels blog_es,blog_en,linkedin_es

# Anadir publicacion
python3 _system/metadata.py add-publication project_XXX \
  --channel blog_es \
  --url https://zoopa.es/... \
  --wp-post-id 12345 \
  --categories 2231 \
  --featured-media 9876

# Anadir publicacion social simple
python3 _system/metadata.py add-publication project_XXX \
  --channel linkedin_es \
  --url https://linkedin.com/posts/... \
  --account "Carlos Ortet"

# Resumen
python3 _system/metadata.py summary project_XXX

# Listar publicaciones de la ultima semana (todos los proyectos)
python3 _system/metadata.py recent --days 7
```

---

## Analisis cross-proyecto

Con `metadata.json` consistente en cada proyecto, queries futuras como:

- "Que posts GEO han generado mas visitas en 30 dias"
- "Que canales tienen mejor engagement por tipo de tema"
- "Cuantos proyectos publicaron en X y Y la misma semana"

se resuelven leyendo todos los `metadata.json` del repo.

---

*Schema v1 — 2026-05*
