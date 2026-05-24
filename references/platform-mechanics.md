# Platform Mechanics · Playwright automation playbook

> Referencia consolidada de cómo automatizar la publicación en cada plataforma vía Playwright CLI. Captura URLs canónicas, mecánica de login, selectores composer, trampas conocidas y verificación post-publicación. Extraído de `lessons-learned.md` durante mayo 2026 para acceso rápido al arrancar nuevo proyecto.
>
> Última actualización: 2026-05-24

---

## Setup global

### Instalar Playwright CLI

```bash
# Pre-requisito (una vez)
npm install -g @playwright/cli
playwright-cli install chromium
```

### Convención de sesiones persistentes

Usar `--persistent` con un nombre semántico por plataforma. Las sesiones viven en `~/Library/Caches/ms-playwright/daemon/{hash}/ud-{nombre}-chrome/`. Reusables durante semanas.

```bash
playwright-cli --browser=chrome --persistent --headed -s={nombre} open {URL}
```

Nombres usados (no inventar otros):
- `wp` — WordPress (NO usar, va por REST API)
- `linkedin`, `medium`, `substack`, `x`, `hn`, `bluesky`, `threads`, `facebook`, `quora`, `mastodon`

### UTF-8 fiable

**SIEMPRE** usar `playwright-cli type "$TEXTO"` para escribir texto con acentos. NO usar pbcopy + Cmd+V — corrompe UTF-8 en composers (LinkedIn, Substack, X, etc.).

Excepción Substack RTF: si necesitas preservar formato markdown a Substack ProseMirror, usar `textutil -convert rtf` + `pbcopy -Prefer rtf` (pierde H2, recuperar manual).

---

## WordPress (zoopa.es) · via REST API

**NO Playwright. Via API.** Más rápido y robusto.

### URLs canónicas zoopa.es

| Endpoint | Path |
|---|---|
| Login admin | `https://zoopa.es/wp-admin/` |
| REST API | `https://zoopa.es/wp-json/wp/v2/` |
| Posts | `https://zoopa.es/wp-json/wp/v2/posts` |
| Media | `https://zoopa.es/wp-json/wp/v2/media` |
| Categories | `https://zoopa.es/wp-json/wp/v2/categories` |

### Headers obligatorios

```python
HEADERS = {
    "Authorization": f"Basic {base64(WP_USER:WP_APP_PASSWORD)}",
    "Content-Type": "application/json",
    "Accept": "application/json",  # CRÍTICO: sin esto, CloudFlare devuelve 406
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",  # CRÍTICO: sin esto, CF block
}
```

### Trampas

- **CloudFlare 403 (code 1010)** con `urllib` sin User-Agent → añadir UA Mozilla
- **406 Not Acceptable** en POST → falta Accept header `application/json`
- **Media upload PNG→JPG auto-convert**: WP optimizer (Imagify) convierte automáticamente. Tu request acepta `image/png` pero la response devuelve `image/jpeg`. No molesta para uso normal.
- **Media upload requires multipart/form-data** con boundary explícito, no raw bytes
- **Polylang Pro**: usar field `lang` (ej. `"lang": "es"`) y `translations` en single POST call para vincular ES/EN/CA simultáneo
- **Rank Math SEO meta**: enviar como `meta` field en standard POST endpoint con keys `rank_math_focus_keyword`, `rank_math_description`, etc.

### Verificación post-publicación

```bash
curl -sL "{URL}" -H "User-Agent: Mozilla/5.0" | grep -c "marker-key"
```

---

## LinkedIn · personal de Carlos Ortet

### URL login

`https://www.linkedin.com/login`

### Mecánica composer

1. Click avatar Carlos → home feed
2. Click "Start a post" en composer top
3. Modal abre con "Share to anyone" → cambiar a "Connections" si quieres
4. Click textbox → type texto vía `playwright-cli type`
5. Subir media (vídeo nativo para AI Chips Economy)
6. Click "Post"
7. URL del post en `linkedin.com/feed/update/urn:li:activity:{N}/`

### Vídeo nativo

LinkedIn premia vídeo nativo (subido directo) sobre vídeo en link. Optimizar:
- Square 1:1 o 16:9
- ≤10 minutos
- MP4 H.264

### Trampas

- **UTF-8 con pbcopy**: corrompe acentos en composer LinkedIn. SIEMPRE `playwright-cli type`.
- **Modal "Add to story" interfere** si tienes feature activa
- **Captions auto-generated** pueden tardar 30-60s tras upload

### Voz Carlos Ortet personal

→ Ver `references/linkedin-voice-carlos-ortet.md` (manual completo del estilo validado por el autor).

---

## Medium · cross-post EN

### URL

`https://medium.com/new-story`

### Mecánica preferida: import-from-URL

NO copiar texto. Usar:
1. `https://medium.com/p/import` → URL del blog publicado (ej. zoopa.es/en/...)
2. Medium scrapea y crea draft preservando formato + canonical
3. Editar manualmente: tags, subtítulo, hero image
4. Click "Publish" → asignar publication si aplica

### Trampas

- **`execCommand('selectAll')` destruye el draft entero** (incluye título + subtítulo + body en la selección). Si paste-and-edit, NUNCA usar selectAll.
- **Tags ≤5**, lowercase, sin espacios (kebab-case mejor)
- **Canonical URL** debe apuntar al original zoopa.es para evitar duplicate content penalty

---

## Substack · ES

### URL

`https://carlosortet.substack.com/publish/post`

### Mecánica

1. Composer ProseMirror (no es contenteditable estándar)
2. Subject line ≤55 chars sin marca
3. Preheader que expande sin repetir subject
4. Body: paste con `textutil -convert rtf | pbcopy -Prefer rtf` para preservar UTF-8
5. H2 perdidos en RTF → convertir manual a `## titulo`
6. Hero image en Settings (cover)
7. Click "Continue" → "Send to everyone now"

### Trampas

- **ProseMirror rompe HTML**: NO pegar HTML del blog. Convertir a prosa
- **pbcopy directo** corrompe UTF-8 → usar `textutil -convert rtf` puente
- **Cover image** se sube en Settings panel, NO en el editor body
- **Subject ≤55 chars**: Substack trunca en email preview a partir de ahí
- **"Continue" pre-send**: muestra preview email, oportunidad de revisar

### Estilo Substack

→ Ver `references/substack-style.md` (patrones validados con AI Chips Economy mayo 2026).

---

## X / Twitter · hilo

### URLs

| Para qué | URL |
|---|---|
| Home | `https://x.com/home` |
| Composer | `https://x.com/compose/post` |
| Profile | `https://x.com/{user}` |
| Replies tab | `https://x.com/{user}/with_replies` |

### Mecánica hilo

1. Click composer (`/compose/post`)
2. Textbox `[ref=eXXX]` activo por defecto → type Tuit 1
3. Para añadir Tuit 2: encontrar button "Add post" (ref cambia cada iter, e.g. `e1535 → e1700 → e2381`)
4. Click → nuevo textbox activo → type Tuit 2
5. Loop por todos los tuits
6. Final: click "Post all" (ref e4524 ej.) → URL redirige `/compose/post` → `/home` = success

### Verificar refs dinámicas

```bash
# Cada iter:
SNAP=$(playwright-cli -s=x snapshot 2>&1 | grep -oE 'page-[^]]+\.yml' | head -1)
ADD_REF=$(grep -oE 'button "Add post" \[ref=e[0-9]+\]' ".playwright-cli/$SNAP" | grep -oE 'e[0-9]+' | head -1)
```

### Trampas

- **NO Twitter API necesaria**: Playwright funciona perfecto para hilos
- **UTF-8 con type**: preservado (acentos, emojis 🧵)
- **280 chars**: validar pre-flight con `validate_char_limits.py`
- **"Schedule post" button siempre disabled** en composer normal
- **Hashtags no penalizados** pero limitar a 2-3 al final del último tuit

### Verificación

```bash
playwright-cli -s=x goto https://x.com/{user}/with_replies
playwright-cli -s=x eval '() => [...document.querySelectorAll("a")].map(a=>a.href).filter(h=>h.includes("/status/")).slice(0, 5)'
# Tuit starter = ID más bajo entre las nuevas
```

### Voz X anti-LLM

→ Ver `references/x-twitter-voice-style.md` (manual 3.250 palabras anti-LLM patterns).

---

## Bluesky · @carlosortet.bsky.social

### URLs

| Para qué | URL |
|---|---|
| Home | `https://bsky.app/` |
| Profile | `https://bsky.app/profile/{handle}` |
| Settings email | `https://bsky.app/settings/account` |

### Mecánica hilo

1. Click "Nueva publicación" (FAB botón flotante)
2. Modal abre con textbox "Rich-Text Editor" (ref e3843 ej.)
3. Type Post 1
4. Click "Add another post to thread" (button al lado del char counter)
5. Type Post 2 → repeat
6. Click "Publicar las publicaciones" / "Publicar Todo" final

### TRAMPA CRÍTICA · email verification

**Bluesky requiere verificación de email ANTES del primer post** (incluso después de login). Modal "Verifica tu correo electrónico" aparece al click compose. Flow:

1. Click "Enviar correo" en modal
2. Abrir email
3. Copiar código formato `XXXXX-XXXXX`
4. En modal, click "¿Tienes un código? Haz clic aquí"
5. Pegar código → "Verify code"
6. Hasta entonces el composer está bloqueado

### Otras trampas

- **Char limit 300 estricto**: rechaza publicar si excedes
- **Handle custom DID** disponible con DNS TXT (rel=me)
- **Hashtags ok, max 2-3** en último post del hilo
- **Rich link cards** se renderizan automático para URLs

### Verificación

```bash
playwright-cli -s=bluesky goto "https://bsky.app/profile/{handle}"
playwright-cli -s=bluesky eval '() => [...document.querySelectorAll("a")].map(a=>a.href).filter(h=>/\/{handle}\/post\//.test(h)).slice(0,5)'
```

---

## Threads · Meta

### URL canónica

- Dominio actual: `threads.com` (NO .net, redirige)
- Handle de Carlos: `@carlosortet.i` (con sufijo `.i`, NO `@carlos.ortet`)
- Login via Instagram (2FA puede pedir código app autenticación)

### Mecánica hilo

1. Click "Nuevo hilo" en sidebar
2. Modal "Crea una publicació" con composer
3. Click textbox → type Post 1
4. Click "Añadir al hilo" (button debajo composer)
5. Type Post 2 → repeat
6. Click "Publicar" final

### Trampas

- **Char limit ~500**: warning si excedes pero permite
- **Hashtag suggestions** popup intenta convertir tu #hashtag en "topic tag" — ignorar o cerrar
- **Composer cierra al click outside**: cuidado

### Verificación

```bash
playwright-cli -s=threads goto "https://www.threads.com/@{handle}"
# Buscar post URLs
```

---

## Facebook · Page (Zoopa)

### URL canónica Page Zoopa

`https://www.facebook.com/Zoopa.TV` (NO `/zoopa`, que es un user no relacionado: Tom Malarky)

### Mecánica

1. Login en `facebook.com` (carles.ortet personal cuenta admin de Page Zoopa)
2. Rechazar cookies opcionales (privacy-first): click "Rechazar cookies opcionales"
3. Navegar a `/Zoopa.TV` → modal "Review changes to your Page" → click "Get started" → "Use Page"
4. Entra en Page mode
5. Ir a `/?profile_view=1` → home feed en modo Page → composer "What's on your mind, Zoopa?" visible
6. Click composer → modal "Crea una publicació"
7. Click textbox → type via Playwright (UTF-8 fiable)
8. Click "Següent" (Next) → modal "Post settings" (Public, Publish now)
9. Click "Publica" → live

### URL post

Format: `facebook.com/Zoopa.TV/posts/pfbid{XX}`

Extraer via:
```javascript
[...document.querySelectorAll("a")].map(a => a.href).filter(h => /pfbid/.test(h))
```

### Trampas

- **Slug `/zoopa` ya tomado** por user Tom Malarky → SIEMPRE `Zoopa.TV`
- **Modal "Use Page"** primera vez en cada sesión
- **Playwright SÍ funciona en Pages** (a diferencia de personal que se desaconseja para casos no esenciales)
- **Aplicar reglas globales ANTES de typear**: orthography-rules § 3 (sin em-dash, sin formulaicas)

---

## Facebook · personal Carlos

### URL handle real

`facebook.com/carles.ortet` (NO carlosortet)

### Mecánica para post NATIVO

(Native long-form publica 5-10× más reach que link card. URL va en primer comentario.)

1. Switch de Page Zoopa a personal: click avatar top-right "El teu perfil" → dropdown → "Switch to Carlos Ortet"
2. Navegar a profile/home
3. Click composer "En què penses?" → modal "Crea una publicació"
4. **Cambiar audiencia**: click "Edit privacy. Sharing with Públic" → seleccionar "Amics" → "Fet" (regla skill)
5. Type long-form (~250-300 palabras, sin URL en cuerpo)
6. Click "Següent" → Post settings (Amics, Publish now)
7. Click "Publica"
8. INMEDIATAMENTE: abrir tu propio post → "Comment as Carlos Ortet" → pegar URL del Substack/blog → Enter

### Trampas

- **FB detecta automation agresivo** en personal. Pages funciona mejor que personal.
- **URL en cuerpo penaliza reach 60-80%**. SIEMPRE en primer comentario.
- **Audiencia "Amics"** vs "Públic" — Público dilute el algoritmo
- **NO hashtags** en FB (no premia como LinkedIn)

---

## Hacker News

### URLs

| Para qué | URL |
|---|---|
| Home | `https://news.ycombinator.com/` |
| Submit | `https://news.ycombinator.com/submit` |
| Login | `https://news.ycombinator.com/login?goto=news` |
| Newest | `https://news.ycombinator.com/newest` |
| User profile | `https://news.ycombinator.com/user?id={handle}` |

### Mecánica submission

1. Login (carlosortet, karma 1+)
2. Navegar a `/submit`
3. Title field e24 (activo) → type title (≤80 chars)
4. URL field e28 → type URL
5. Text field → dejar VACÍO (HN favorece submissions con solo URL)
6. Click "submit" button e39

### Mecánica primer comentario (OP)

INMEDIATAMENTE tras submit:
1. URL redirige `/newest` → encontrar tu post
2. Click en el post para abrir item page
3. Comment textbox e66 → click → type OP comment
4. Click "add comment" e70 → publicado

### TRAMPA CRÍTICA · low-karma auto-flag

**Cuentas con karma <50 tienen comentarios auto-flagged** especialmente si:
- Listas con bullets `*` o `-` seguidos de nombres de empresas
- Múltiples cifras (€111M, $254M, etc.)
- Múltiples URLs en mismo comentario
- Prefijo "OP here" combinado con lo anterior
- Longitud >2000 chars en primera contribución

**Verificar post-publish**:
```bash
curl -s "https://news.ycombinator.com/item?id={ID}" -H "User-Agent: Mozilla/5.0" | grep -oE "commtext|flagged|dead"
```

Si NO ves `commtext` para tu comentario en HTML anónimo, está flagged.

### Soluciones flag

1. **Email dang** (hn@ycombinator.com): "Auto-flagged OP comment, please review". Responde 6-24h.
2. **Delete + repost** más conversacional (sin bullets, sin "OP here"). Riesgo re-flag.
3. **Asumir y mover**: title+URL siguen vivos.

### Estrategia karma

→ Ver `case-studies/karma-boost-carlos-ortet-20260524.md` § Hacker News (plan 10-15 min/día durante 2 semanas → karma 50+).

### 🚨 REGLA NUEVA (24 may 2026): contenido HN debe ser 100% manual

Tras email de dang el 24 may 2026 confirmando que nuestro OP comment fue clasificado como `genai` por software interno HN (independiente del filtro de spam, ver `lessons-learned.md`), política nueva:

- **HN no acepta LLM-assisted content**, ni siquiera aplicando reglas anti-LLM superficiales
- El clasificador detecta **cadencia estructural** (no solo léxico): párrafos de longitud uniforme, densidad informacional consistente, transiciones formales, ausencia de irregularidades humanas
- **Política para HN**: el autor escribe 100% del comentario/submission desde cero. El skill content-factory puede ayudar con investigación (datos, fuentes, links) pero NO con drafting de texto
- Aplica a comments, submissions y replies. Cualquier texto enviado a HN
- Otros canales (Bluesky, Mastodon, Threads, LinkedIn, Substack) son más permisivos con LLM-assist si aplicas reglas anti-LLM

---

## Mastodon

### Instancia recomendada

`mastodon.social` (general) o `fosstodon.org` (tech) o `mas.to`

### Mecánica

1. Login en instancia elegida
2. Click "Toot!" / "Publicar"
3. Composer 500 chars máximo
4. Subir media opcional (cada toot soporta 4 imágenes)
5. Public / Unlisted / Followers / Direct
6. Click "Publicar"

### Trampas

- **NO tracking links**: la comunidad anti-corporate los castiga (UTM, redirects). URLs limpias.
- **Char limit 500 estricto**
- **Hilos** se hacen con replies a tu propio toot (no botón nativo)
- **Avoid hashtag stuffing**: máximo 3-4 hashtags relevantes

---

## Quora

### URL canónica

- Profile: `https://www.quora.com/profile/{handle}`
- Question: `https://www.quora.com/{question-slug}`

### Mecánica answer

1. Login (Carlos-Ortet)
2. Navegar a question URL
3. Click "Answer" button
4. Editor abre
5. Type/paste answer (preferir reformular vs copy-paste del blog)
6. Añadir 1 imagen mínimo (Quora ranking premia imágenes)
7. Click "Submit"

### Trampas

- **Cadencia 24-48h** entre answers del mismo topic (evitar señal de spam)
- **Reformular cada respuesta** vs copy-paste del blog (Quora penaliza duplicate)
- **1 imagen mínimo** mejora ranking
- **Max 1-2 enlaces salientes** (1 al blog, 0 a paid)
- **Disclosure obligatoria** si trabajas en sector mencionado

### Best practices

→ Ver `references/quora-best-practices.md` (manual completo).

---

## carlosortet.com · auto-add publication

### Mecánica

Cuando publicamos pieza editorial firmada por Carlos Ortet (blog, Medium, Substack):

1. Editar `/Users/cop/Documents/03_PERSONAL/carlosortet/src/data/resume.tsx`
2. Añadir entry a `publications[0]` (es array, el más nuevo arriba)
3. Pattern:
   ```tsx
   {
     title: "...",
     dates: "Month Year",
     location: "Medium · zoopa.es (EN, ES, CA)",
     description: "...",
     image: "",
     links: [
       { title: "Read in English (Zoopa)", icon: <Icons.globe />, href: "..." },
       { title: "Read in Spanish (Zoopa)", ... },
       { title: "Read in Catalan (Zoopa)", ... },
       { title: "Read on Medium", ... },
       { title: "Read on Substack (Spanish)", ... },
     ],
   },
   ```
4. `cd ~/Documents/03_PERSONAL/carlosortet && npm run build` (verifica)
5. `git add src/data/resume.tsx && git commit -m "publications: add ... (Nth link)"`
6. `git push origin main` → CloudFlare Pages deploy automático en ~30s

### Trampa

- **Convención**: nuevas pubs SIEMPRE arriba (más recientes primero)
- **URL Substack format**: `https://open.substack.com/pub/carlosortet/p/{slug}` (sin tracking)

---

## Comandos útiles globales

### Listar sesiones Playwright activas

```bash
ls /Users/cop/Library/Caches/ms-playwright/daemon/*/ud-*-chrome/ 2>/dev/null
```

### Reset sesión específica (forzar re-login)

```bash
rm -rf /Users/cop/Library/Caches/ms-playwright/daemon/*/ud-{nombre}-chrome/
```

### Screenshot rápido

```bash
playwright-cli -s={nombre} screenshot --filename /tmp/check.png
```

### Eval JS arbitrario

```bash
playwright-cli -s={nombre} eval '() => document.title'
```

### Snapshot semántico (para encontrar refs)

```bash
playwright-cli -s={nombre} snapshot
# Output: .playwright-cli/page-{timestamp}.yml
```
