# Lecciones aprendidas por plataforma

## Reviews y directorios

- **G2/Capterra**: Solo para software comercial listado en su base de datos. Verificar que el producto existe ANTES de preparar contenido. Para open-source, considerar solo Trustpilot.
- **Product Hunt**: Requiere launch oficial del creador. No preparar contenido PH hasta confirmar que el producto existe o esta planificado.
- **Trustpilot**: Solo reseñas, NO artículos. Si no hay listing previo del business (verificado con dueño), no se puede publicar nada. Verificación 2026-05-24: cero listings para zoopa.es / zoopa.com / georadar.app / 498as.com en Trustpilot global o ES. **No fit para distribución de contenido editorial**. Solo tiene sentido cuando: (a) ya existe un business profile, (b) lo va a publicar un cliente real con experiencia genuina del servicio. Auto-reviews violan ToS.

## Plataformas tech

- **Dev.to**: Editor Markdown puede dar error JSON al publicar. Reintentar o publicar manualmente. Front matter con `published: false` para revisar antes de publicar.
- **Hashnode**: Primera vez requiere crear blog (nombre + subdomain) y completar AI Tour (4 pasos) antes de publicar articulos. Blog existente: carlosortet.hashnode.dev.
- **HackerNoon**: Tiene editores que revisan submissions. Estilo editorial tipo Wired.
- **DZone**: Audiencia enterprise. Incluir siempre "Key Takeaways" al inicio.
- **Lobste.rs**: Solo link-aggregation (titulo + URL, sin self-text). Requiere invitacion para publicar.

## Comunidades

- **Reddit r/selfhosted**: Regla 8 exige flair "AI-Assisted App (Fridays!)" para posts de IA. Evitar self-promotion directa. Responder TODOS los comentarios en 2h.
- **Hacker News**: No hacer self-promotion directa. Contribuir al hilo existente si lo hay. Tono factual, sin hype.

### Hacker News · template de submission (añadido mayo 2026)

- **Title**: máximo 80 chars, factual contrarian. Mejor "X is actually Y" con datos verificables que titulares promocionales. Si el título del artículo cabe, úsalo; si no, reescribir manteniendo precisión.
- **URL única**: dejar el campo Text vacío. HN favorece submissions con URL clara, sin self-text.
- **Primer comentario OP (publicar inmediatamente tras submit)**: declarar "OP here" + añadir información que NO está en el artículo. Esa información extra es lo que desactiva el flag de self-promo. Datos verificables 2024-2026 (raises, productos, fechas) funcionan mejor que opiniones.
- **Anti-patrones que matan el post en HN**:
  - Title con "delve into", "deep dive", "harness", "leverage", "unlock"
  - Cuerpo del comentario con CTAs ("read the full article", "subscribe", "learn more")
  - Adjetivos vacíos ("groundbreaking", "revolutionary", "cutting-edge")
  - Em-dashes excesivos (regla global, ver `orthography-rules.md` § 3.1)
- **Timing**: martes-jueves 09:00-11:00 ET = 15:00-17:00 CET (pico HN US East + EU evening). NO viernes-domingo.
- **Verificación primeras 4h**: cada 30 min responder TODOS los comentarios. Reconocer error fáctico inmediatamente (HN respeta humildad técnica). Si alguien dice "this is content marketing", responder con transparencia ("yes I work at X, the additional data is my own research").
- **Caso de uso ideal**: artículo con datos contraintuitivos verificables (chips, semis, ML internals, sistemas distribuidos, criptografía). Mal fit: posts opinion-piece, framework launches, lifestyle.
- **Ejemplo real**: ver `proyecto-AI-chips-economy-23052026/output/hackernews_ready.txt` — comentario OP con 7 startups EU verificadas (Axelera, SiPearl, OpenChip, Black Semi, Codasip, GreenWaves, Quintauris) más DARE program context. Añade lo que el artículo no cubre, no lo promociona.

#### ⚠️ Trampa CRÍTICA: low-karma accounts → comentarios auto-flagged

- **Síntoma**: el comentario es visible a TI (logueado como autor) pero aparece como `[flagged]` para cualquier usuario anónimo. Curl de la URL pública confirma: el commtext NO aparece en el HTML que ven los demás.
- **Causa**: HN tiene un filtro anti-spam agresivo para cuentas con karma <50. Triggers conocidos:
  1. Listas con bullets (`*` o `-`) seguidos de nombres de empresas
  2. Múltiples cifras (€111M, $254M, etc.)
  3. Múltiples URLs en el mismo comentario
  4. Prefijo "OP here" combinado con lo anterior
  5. Longitud >2000 chars en primera contribución de la cuenta
- **Verificación obligatoria post-publicación HN (regla a partir mayo 2026)**:
  ```bash
  curl -s "https://news.ycombinator.com/item?id=XXX" -H "User-Agent: Mozilla/5.0" | grep -oE "commtext|flagged|dead"
  ```
  Si NO ves `commtext` para tu comentario en el HTML anónimo, está flagged.
- **Soluciones probadas en orden de eficacia**:
  1. **Email a hn@ycombinator.com** (mods dang/sctb). Asunto: "Auto-flagged OP comment, please review". Cuerpo: explicar contexto + disclosure laboral + link. Responde en 6-24h, suele vouchear si es genuino.
  2. **Delete + repost más conversacional**: sin bullets, sin "OP here", menos cifras, párrafos prosaicos. Riesgo de re-flagging.
  3. **Asumir y mover**: title+URL siguen vivos, el OP comment se pierde.
- **Prevención futura**: para cuentas con karma <50, primer comentario debe ser corto (<500 chars), conversacional, sin bullets ni cifras. Construir karma respondiendo en hilos ajenos durante 2-4 semanas antes de submission propia.
- **Caso real 2026-05-24**: post `48256396` ("invisible fabric of AI") flagged. OP comment con 7 EU chip startups oculto a anónimos. Cuenta carlosortet, karma 1.
- **Discord**: Respetar reglas del servidor. Consultar #rules. Enmarcar como contribucion, no promocion.

## Redes sociales

- **Threads**: Login con cuenta Meta/Instagram (2FA en app). Playwright funciona perfecto para publicar (mejor que X, mejor que LinkedIn). Composer: click "Nuevo hilo" → escribir Post 1 → click "Añadir al hilo" → escribir Post 2 → repeat → click "Publicar" final. Char limit ~500. Dominio actual: threads.com (NO .net). Handle de Carlos: @carlosortet.i (con .i sufijo, NO @carlos.ortet). Verificado 2026-05-24: hilo 4 posts publicado en https://www.threads.com/@carlosortet.i/post/DYuLTeZF-Mi. UTF-8 perfecto con `playwright-cli type`.
- **Mastodon**: Comunidad tech early-adopter, buen engagement organico. No usar tracking links.
- **Bluesky**: 30M+ usuarios (2026). Comunidad tech, periodistas, academicos. Anti-corporate — voz personal funciona mucho mejor que marca. 300 chars por post, threads nativos (3-5 posts optimo). Links muestran rich cards. Max 2 hashtags y solo en ultimo post. Lo que funciona: datos originales, hallazgos contraintuitivos, narrativa "esto es lo que encontramos cuando...". Lo que no: listicles, tips genericos, lenguaje promocional. Cuenta: carlosortet.bsky.social.
  - **⚠️ Trampa email verification**: Bluesky requiere verificación de email ANTES del primer post, incluso después de login. Modal "Verifica tu correo electrónico" aparece al click compose. Flow: click "Enviar correo" → email recibe código formato `XXXXX-XXXXX` → click "¿Tienes un código? Haz clic aquí" → input code → "Verify code". Hasta entonces el composer está bloqueado.
  - **Mecánica de hilo**: click "Nueva publicación" (FAB botón flotante) → click textbox "Rich-Text Editor" → typear Post 1 → click "Add another post to thread" (button al lado de char counter) → typear Post 2 → repeat → click "Publicar las publicaciones" / "Publicar Todo" final.
  - Verificado 2026-05-24: hilo 5 posts asimétricos publicado en https://bsky.app/profile/carlosortet.bsky.social/post/3mmlzmhwog22j. UTF-8 perfecto.

### Facebook · personal y page (añadido mayo 2026)

- **Cuenta personal (`facebook_personal.md`)**: red mixta amigos/familia/profesional. El algoritmo favorece fotos y video nativo sobre links externos. Para links a contenido propio (Substack, blog, Medium), el reach organico es 10-15% de la red.
- **Tono recomendado cuenta personal**: conversacional ("os comparto este analisis que me ha llevado tiempo"), NO institucional. 4-5 frases maximo. Sin hashtags (FB no los premia como LinkedIn).
- **Link card automatica**: FB renderiza un preview rich del Substack/blog con cover image (og:image), titulo y preheader. ASEGURAR que el destino tiene og:image bien configurada antes de postear. Verificar con [Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/) si la card no se ve bien.
- **Privacidad recomendada para contenido pro**: `Amigos` o `Amigos de amigos` (no `Publico`) para evitar diluir el algoritmo con audiencia no-engaged.
- **Cuando NO publicar en FB personal**: si tu red FB es 90% familia/lifestyle y el contenido es tecnico-corporate, el reach sera bajisimo y puede generar percepcion negativa ("ahora Carlos usa FB como LinkedIn"). Mejor saltar FB y quedarse en LinkedIn.
- **Detector de automatizacion FB**: muy agresivo. Playwright NO funciona fiable para postear en FB. Siempre manual.
- **Page Zoopa / 498A (`facebook_page.md`)**: tono institucional, reach organico aun mas bajo (~5% de seguidores sin paid). Solo merece la pena si va con paid promotion o si la audiencia de la page es muy especifica.
  - **URL canónica Page**: `facebook.com/Zoopa.TV` (NO `/zoopa` que es un user no relacionado, Tom Malarky). Verificado 2026-05-24.
  - **Automatización Playwright SÍ funciona en Pages** (a diferencia del FB personal que se desaconseja). Verificado 2026-05-24: post publicado vía Playwright. Flow:
    1. Login normal en `facebook.com`.
    2. Si modal cookies aparece: click "Rechazar cookies opcionales" (privacy-first).
    3. Navegar a `https://www.facebook.com/Zoopa.TV` → si Carlos es admin, modal "Review changes to your Page" → click "Get started" → "Use Page" → entra en Page mode.
    4. Ir a `https://www.facebook.com/?profile_view=1` → home feed en modo Page → composer "What's on your mind, Zoopa?" visible.
    5. Click composer → modal "Crea una publicació" → click textbox → typear texto vía `playwright-cli type` (UTF-8 fiable).
    6. Click "Següent" (Next) → modal "Post settings" (Public, Publish now, share to groups optional).
    7. Click "Publica" → posts live.
  - **URL post**: formato `facebook.com/Zoopa.TV/posts/pfbid...`. Recuperable via DOM eval `[...document.querySelectorAll("a")].map(a => a.href).filter(h => /pfbid/.test(h))`.
  - Recordatorio: aplicar reglas globales `orthography-rules.md § 3` ANTES de typear (no em-dash, no "Lectura recomendada para founders, CTOs..." formulaico).
- **Mejor formato FB para contenido editorial largo**: post de texto corto + link → genera card. NO copiar el contenido completo (FB castiga texto largo nativo si tambien hay link externo).
- **Horarios optimos audiencia profesional EU**: martes-jueves 9-11h CET.
- **Output format `facebook_personal.md`**: 4-5 frases conversacionales + URL del long-form al final + nota sobre privacidad recomendada (publico/amigos). Ver caso real en `proyecto-AI-chips-economy-23052026/output/facebook_personal.md`.

### X / Twitter · hilo (añadido mayo 2026)

- **Login persistente**: abrir sesion Playwright headed (`playwright-cli --browser=chrome --persistent --headed -s=x open https://x.com/home`), usuario hace login manual una vez, sesion persiste en `ud-x-chrome/`. Reutilizable durante semanas.
- **UTF-8 fiable**: `playwright-cli -s=x type "$TUIT"` preserva UTF-8 perfecto (oirás, técnicamente, Japón, Taiwán, fábrica). NO usar `pbcopy + Cmd+V` — corrompe UTF-8 en composer X igual que en LinkedIn/Substack.
- **Mecanica hilo (Add post button)**: tras escribir tuit N, encuentra ref del boton `"Add post"` (cambia cada iteracion, ej. e1535 → e1700 → e2381…). Click → composer crea nuevo textbox vacio que recibe automaticamente el `type` siguiente. Loop por todos los tuits 2..N.
- **Refs dinamicas**: NO hardcodear refs. Cada iteracion: `playwright-cli -s=x snapshot` → grep `'button "Add post"'` → extract ref → click. Mismo patron para `"Post all"` final.
- **Limite 280 chars**: validar TODOS los tuits ANTES de empezar. Script Python conta `len(tuit)` y marca `⚠️ EXCEEDS by N`. Trims comunes: `Semiconductores → Semis`, `hispanohablante → hispano`, `consolidación a Vietnam/Malasia → a Vietnam/Malasia`, eliminar adverbios redundantes.
- **Señal de exito del Post all**: URL pasa de `/compose/post` → `/home` (~2-3 seg). Si sigue en `/compose/post`, click no se registro — reintentar con ref fresh.
- **Verificar hilo publicado**: `playwright-cli -s=x goto https://x.com/$USERNAME/with_replies` + `eval '[...document.querySelectorAll("a")].map(a=>a.href).filter(h=>h.includes("/status/"))'` → ID mas bajo = tuit starter del hilo. Visitar esa URL para confirmar render.
- **Sin parse-hack**: si el `.txt` de origen separa hilos con `===`, el regex puede capturar el separador como "tuit 1". Skipear `tuits[0]` si es solo separadores.
- **URL final hardcoded**: el ultimo tuit lleva la URL canonica del long-form. Asegurar que es la URL definitiva (zoopa.es vs 498as.com vs Substack) ANTES de empezar — corregirla a mitad de hilo es engorroso.
- **Tiempo total**: 19 tuits ≈ 2-3 minutos automatizado (incluyendo snapshots + clicks + types). Plus 30 seg de Post all. Muy rapido vs manual.
- **Trampa "Schedule post" disabled**: el boton existe pero esta `[disabled]` en composer normal. Ignorar — solo se activa con flow distinto.
- **NO Twitter API necesaria**: el flujo Playwright es 100% suficiente y evita el hassle de keys/scopes. Free, sin rate limits API, soporta hilos nativos (no replies encadenados).

Ver caso real publicado: `https://x.com/carlos_ortet/status/2058492127642865883` (19 tuits, AI chips, 24 may 2026 12:15 CEST).

## Mensajeria

- **Substack**: Flujo "Continue" > "Send to everyone now" > puede pedir botones subscribe (skip).
- **WhatsApp**: Riesgo de ban en grupos si se percibe como spam. Tener numero secundario como backup.

## Web3

- **Mirror.xyz**: Requiere wallet conectada para publicar. Incluir recordatorio en el header del archivo.
- **Farcaster**: Requiere cuenta Warpcast con invitacion o pago.

## General

- **Wikipedia**: No intentar crear articulos para productos nuevos. Requiere cobertura en medios tradicionales (TechCrunch, Wired, etc.). GitHub stars no son criterio de notabilidad.
- **Cloudflare Challenges**: Algunas plataformas (Hashnode, G2) tienen Cloudflare protection que bloquea automatizacion. Esperar 3-5 segundos o verificar manualmente.

## WordPress / Publicacion en zoopa.es

### Categorias y Polylang (CRITICO — actualizado abril 2026)

- **zoopa.es usa Polylang Pro** con 3 idiomas: ES, CA, EN. Cada idioma tiene categorias con IDs propios.
- **Las paginas de blog usan widgets de Elementor** que filtran por categorias especificas del idioma.
- **CATEGORIAS NUEVAS (abril 2026)**: El blog se reestructuro completamente. Las categorias antiguas (Blog, Digital Marketing, Content Marketing) fueron eliminadas o reemplazadas. Usar SOLO las nuevas.

### Categorias ES (abril 2026)

| Categoria | ID | Slug |
|-----------|-----|------|
| GEO, IA y Visibilidad en Buscadores de IA | 2231 | geo-ia-visibilidad |
| Social Media | 2233 | social-media-es |
| Creatividad y Contenido | 2235 | creatividad-contenido |
| Innovacion y Tecnologia | 2237 | innovacion-tecnologia |
| Estrategia y Marketing Digital | 2239 | estrategia-marketing-digital |
| Branding, UX y Diseno | 2241 | branding-ux-diseno |
| Influencer Marketing | 2243 | influencer-marketing-es |
| Produccion Audiovisual | 2245 | produccion-audiovisual |

### Reglas de asignacion de categorias

- **Asignar 1-2 categorias por post** segun el tema principal. Un post puede estar en 2 categorias si toca ambos temas.
- **Todo post sobre GEO, ChatGPT, LLMs, visibilidad en IA** → categoria GEO (2231). Es el cluster estrategico.
- **NO usar categorias legacy** (Blog ID 26, Sin categoria ID 1, Digital Marketing, Content Marketing antiguas). Estan vacias o eliminadas.
- **Verificar IDs de categorias EN y CA** antes de asignar traducciones: `GET /wp-json/wp/v2/categories?lang=en` / `?lang=ca`
- **Verificar siempre** que el post aparece en la pagina del blog tras publicar.

### Contenido vaciado por Polylang (BUG)

- Al vincular traducciones via la API REST, se observo que el contenido de uno de los posts se vaciaba a 0 caracteres.
- **Causa probable**: asignar `lang` y `translations` en llamadas separadas o en combinacion con updates de contenido puede causar que Polylang vacíe el `content.raw`.
- **Solucion**: asignar idioma, traducciones y contenido en una SOLA llamada API. Verificar `content.raw.length > 0` inmediatamente despues de cada update.
- **Si el contenido se vacia**: reinyectar via `POST /wp-json/wp/v2/posts/ID` con `{content: "..."}`.

### Imagen destacada

- **El dialogo de WordPress para imagen destacada** (via Playwright) es poco fiable: el boton "Establecer la imagen destacada" puede quedar en estado `disabled` o `active` sin completar la accion.
- **Solucion**: usar la API REST directamente: `POST /wp-json/wp/v2/posts/ID` con `{featured_media: ATTACHMENT_ID}`.
- **Subir imagenes**: usar la pagina `/wp-admin/media-new.php` con `browser_file_upload` de Playwright (soporta multiples archivos). Luego obtener URLs via `GET /wp-json/wp/v2/media?per_page=N&orderby=date&order=desc`.

### Editor de codigo vs Editor visual

- **Siempre usar el editor de codigo** (Opciones > Editor de codigo) cuando se inyecta contenido via Playwright. El editor visual de Gutenberg no acepta bien contenido largo inyectado via JS.
- **Para contenido muy largo**: usar `page.evaluate()` para inyectar en el textarea, no `browser_type()` (timeout).
- **Al navegar fuera del editor con cambios no guardados**: WordPress muestra un dialogo `beforeunload`. Hay que manejarlo con `browser_handle_dialog({accept: true})`.

### Rank Math SEO via API

- Endpoint: `POST /wp-json/rankmath/v1/updateMeta`
- Body: `{objectID: POST_ID, objectType: "post", meta: {rank_math_title, rank_math_description, rank_math_focus_keyword}}`
- Funciona correctamente desde el navegador autenticado usando `wpApiSettings.nonce`.

### Cache de Elementor

- Las paginas de blog construidas con Elementor pueden mostrar contenido cacheado. Purgar la cache de Elementor (Herramientas > Vaciar archivos y datos) puede ser necesario, pero no siempre es la causa real.
- **La causa mas comun de que un post no aparezca es que le falta una categoria**, no la cache.

## Ortografia y traducciones

### False friends numericos (CRITICO)

- **"Billion" (EN) = "mil millones" (ES) = "mil milions" (CA).** NO es "billon" (ES) ni "bilio" (CA), que significan trillion (10^12).
- Verificar SIEMPRE las cifras grandes al traducir del ingles. Common Crawl tiene 300 billion documents = 300.000 millones (ES) = 300 mil milions (CA).

### Catalan: errores especificos

- **Punt volat (l·l)**: verificar "intel·ligencia", "col·laborar", "sol·licitar". Error frecuente: omitir el punt volat.
- **Ce trencada (c)**: verificar "informació", "organització". Error frecuente: usar "c" sin cedilla.
- **"Bilions" NO significa billions**: es un false friend del ingles. Usar "mil milions" para billions.

## SEO/GEO — Lecciones de la auditoria zoopa.es (marzo-abril 2026)

### CTAs en posts (CRITICO)

- **Todo post del blog debe tener CTAs** que enlacen a paginas de servicio y contacto. Sin CTAs, el blog genera trafico pero no conversiones.
- **Mid CTA** (~50% del contenido): enlace a la pagina de servicio relevante. Ejemplo: post sobre influencers → /servicios/marketing-de-influencers/
- **Final CTA**: enlace a /contactanos/. Copy directo: "Hablemos"
- **CTA de cluster**: si el post pertenece a un cluster tematico (ej: GEO), incluir enlace a la pillar page. Los posts GEO lo reciben automaticamente via Snippet #56.
- **Formato**: usar bloques HTML con fondo gris (mid) o negro (final), no links sueltos.

### Interlinking (CRITICO)

- **Cada post debe enlazar a 1-2 paginas de servicio** de zoopa.es de forma contextual inline. No solo en CTAs.
- **Cada post debe enlazar a 2-3 posts del mismo cluster/categoria**. Consultar posts existentes: `GET /wp-json/wp/v2/posts?categories=CAT_ID&per_page=5`
- **La pillar page debe enlazar a los posts del cluster** (ya hecho para GEOradar con 18 links).
- **Blog → servicios es la ruta de conversion principal.** Sin estos links, Google no entiende la relacion entre el contenido informativo y las paginas comerciales.

### Schema y structured data

- **Service schema** en paginas de servicio clave: JSON-LD con @type Service, provider, offers, review, knowsAbout. Aumenta comprension por LLMs.
- **OG:image obligatoria** en toda pagina publicable. Sin og:image, los shares en LinkedIn/WhatsApp salen sin imagen. Formato: 1200x630 JPG.
- **contentUrl en ImageObject**: verificar que el schema tiene tanto `url` como `contentUrl` apuntando a la imagen correcta (no a un 404).
- **@id correcto**: Organization usa `#organization`, nunca `#person`.

### Heading hierarchy

- **1 H1 por pagina**, siempre. Los templates de Elementor/JetEngine generan H1/H2 adicionales en carousels y listings. Verificar despues de publicar.
- **H2 para secciones principales**, H3 para subsecciones. Nunca saltar niveles.
- **Paginas de servicios con JetEngine** pueden tener 100+ H2 de listings. Verificar y arreglar via snippets si es necesario.

### Meta descriptions

- **Maximo 155 caracteres** (margen de seguridad sobre los 160 de Google).
- **No repetir nombre de marca** si ya esta en el title tag.
- **Incluir keywords principales** y una CTA implicita.
- **Cada idioma debe tener su propia meta description** en el idioma correcto. No copiar la ES en EN/CA.

### Categorias y clusters

- **Usar las 8 categorias nuevas** (ver tabla arriba). Nunca las legacy.
- **Posts GEO son el cluster estrategico**: cualquier post sobre ChatGPT, LLMs, visibilidad en IA → categoria 2231.
- **Un post puede tener 2 categorias** si toca ambos temas. No mas de 2.
- **Produccion Audiovisual** existe como categoria estrategica (diferencial Zoopa: productora in-house). Asignar a posts sobre VR, XR, video, jingles, produccion.

### Multiidioma

- **Todo post debe existir en ES + EN + CA** con traducciones vinculadas en Polylang.
- **Vincular traducciones en una sola llamada API** (evita bug de contenido vaciado).
- **Las categorias tienen IDs diferentes por idioma**. Verificar antes de asignar.

## Horarios optimos de publicacion

| Plataforma | Hora optima (ES) | Notas |
|------------|------------------|-------|
| LinkedIn | 8-10h o 17-19h | Horario laboral europeo |
| Reddit | 00-02h (medianoche ES) | Horario USA morning |
| Substack | 10-12h | Manana laboral |
| Threads | 00-02h | Horario USA |
| Blog | Cualquier hora | Publicar primero como canonical |

---

## Lecciones de TV-oscura-dialogos (mayo 2026)

### Polylang content-blank bug — vincular en una sola llamada API

**Sintoma:** al vincular traducciones via WP REST API en llamadas separadas, el contenido de uno de los posts se vacia a 0 caracteres silenciosamente.

**Causa raiz:** asignar `lang` y `translations` y `content` en updates separados puede disparar este bug del plugin Polylang en su REST handler.

**Solucion:** vincular en una sola llamada al `POST /wp-json/wp/v2/posts/<id>` incluyendo `{lang, translations, content}` en el mismo body. Verificar `content.raw.length > 0` inmediatamente despues.

**Codigo working (testado):**

```python
trans = {'es': 21072, 'en': 21074, 'ca': 21075}
for lang, post_id in trans.items():
    payload = {'lang': lang, 'translations': trans}  # NO incluir content si ya esta seteado correctamente
    r = requests.post(f'{site}/wp-json/wp/v2/posts/{post_id}', auth=auth, json=payload, timeout=30)
    # Verificar que content sigue lleno tras el update
    assert len(r.json().get('content',{}).get('raw','')) > 0
```

### Categorias nuevas EN/CA no existen automaticamente — crearlas via API

**Contexto:** zoopa.es tiene 8 categorias nuevas (abril 2026) en ES (IDs 2231-2245). En EN y CA solo existen las legacy (Marketing, Digital Marketing, Social Media, etc.).

**Implicacion:** si quieres publicar un post en EN o CA en una categoria nueva tematica, **hay que crear la traduccion de la categoria primero** via API.

**Codigo (validado en proyecto LEO — categorias 2248 EN, 2250 CA vinculadas a 2245 ES):**

```python
def create_cat(name, slug, lang, parent_translations=None):
    payload = {'name': name, 'slug': slug, 'lang': lang}
    if parent_translations:
        payload['translations'] = parent_translations
    r = requests.post(f'{site}/wp-json/wp/v2/categories', auth=auth, json=payload, timeout=30)
    return r.json()['id']

# Crear EN vinculada a 2245 ES
en_id = create_cat('Audiovisual Production', 'audiovisual-production-en', 'en', {'es': 2245})

# Crear CA vinculada a ambas
ca_id = create_cat('Producció Audiovisual', 'produccio-audiovisual-ca', 'ca',
                   {'es': 2245, 'en': en_id})

# Re-vincular las 3 desde cada lado
trans = {'es': 2245, 'en': en_id, 'ca': ca_id}
for tid in [2245, en_id, ca_id]:
    requests.post(f'{site}/wp-json/wp/v2/categories/{tid}', auth=auth,
                  json={'translations': trans}, timeout=30)
```

**Si el cliente no tiene equivalente en EN/CA y no quieres crearlo:** usar la categoria legacy mas cercana (Marketing 803 EN, Digital Marketing 1509 CA) y dejar nota en `metadata.json` para reasignar despues.

### CTAs URLs frágiles — verificar HTTP 200 antes de meterlas

**Sintoma:** generamos posts con CTAs hacia `/ca/contacta/` y `/en/services/production-and-branded-content/`. Ambas devolvieron 404 porque el slug real era distinto: `/ca/contactans/` y `/en/services/`.

**Causa:** los slugs no son siempre lo que parecen. Polylang puede tener slugs distintos al hardcoded, y las paginas de servicio especificas pueden no existir todavia.

**Solucion:** **antes** de meter una CTA en el contenido, hacer un curl HEAD HTTP a la URL y verificar 200. Si 404, fallback al index del servicio (`/ca/serveis/`) o al contacto general.

**Bash one-liner para verificar todas las URLs candidatas en bulk:**

```bash
for path in es/servicios/produccion-y-branded-content/ ca/serveis/ en/services/ es/contactanos/ ca/contactans/ en/contact-us/; do
  code=$(curl -s -o /dev/null -w "%{http_code}" -L "https://zoopa.es/$path")
  echo "  HTTP $code  https://zoopa.es/$path"
done
```

### Placeholder image figure stripping — el publisher debe limpiar

**Sintoma:** los blogs generados llevan `<figure><img src="featured-image-placeholder.jpg" /></figure>` cuando el usuario no aporta imagen real. Si publicas tal cual, el post sale con icono de imagen rota.

**Solucion:** el `wp_publish.py` debe regex-strippar cualquier `<figure>` cuyo `<img src>` contenga "placeholder" antes de convertir a Gutenberg blocks.

**Codigo (ya en `_system/publisher/wp_publish.py`, en `md_to_gutenberg`):**

```python
md = re.sub(
    r"<figure[^>]*>\s*<img[^>]*placeholder[^>]*/?>\s*(?:<figcaption[^>]*>.*?</figcaption>\s*)?</figure>\s*",
    "",
    md,
    flags=re.DOTALL | re.IGNORECASE,
)
```

Cuando el usuario aporte imagen real, asignar via `featured_media: ID` en el body del POST a WP. El theme la pone arriba del post automaticamente.

### Issue creator (crawler) en GitHub debe usar el slug real del repo

**Sintoma:** transferencia de repo de `carlosortet/leo` a `498AS/leo` redirigio el push pero algunas referencias (Issue templates, README links) seguian apuntando a la ruta vieja.

**Solucion:** despues de un transfer, ejecutar `git remote set-url origin https://github.com/<new-org>/<repo>.git` localmente. Y revisar todos los `.md` por links viejos.

### Generacion de label "type:prd" / "priority:high" / "v1" antes de crear issues

**Sintoma:** `gh issue create --label "type:prd"` falla con `'type:prd' not found` si el label no existe en el repo.

**Solucion:** crear los labels una vez por repo (idempotente, falla silenciosamente si ya existen):

```bash
gh label create "type:prd"      --color "0E8A16" --description "Product Requirements Document"  || true
gh label create "type:feature"  --color "A2EEEF" --description "New feature"                    || true
gh label create "type:dx"       --color "FBCA04" --description "Developer experience"           || true
gh label create "type:docs"     --color "0075CA" --description "Documentation"                  || true
gh label create "type:ux-review" --color "FFCC00" --description "UX audit / structural review"  || true
gh label create "priority:high" --color "B60205" --description "High priority"                  || true
gh label create "v1"            --color "1D76DB" --description "v1 MVP scope"                   || true
gh label create "area:auth"     --color "5319E7" --description "Auth & authorization"           || true
gh label create "area:web"      --color "0052CC" --description "apps/web frontend"              || true
gh label create "area:tooling"  --color "BFD4F2" --description "Build, scripts, dev tooling"    || true
gh label create "status:deferred" --color "CCCCCC" --description "Do not start until prerequisite is met" || true
```

Convertir esto en script `scripts/init-labels.sh` por repo.

---

## Publicacion API a zoopa.es — Lecciones reales (mayo 2026, proyecto AI Chips)

### CloudFlare 403 / error code 1010 — User-Agent OBLIGATORIO

- **Sintoma**: `urllib.request` o `requests` de Python sin `User-Agent` reciben HTTP 403 con CloudFlare error 1010 al hacer POST autenticado.
- **Causa**: CloudFlare WAF de zoopa.es bloquea User-Agent vacio o "Python-urllib/X.X" por defecto.
- **Solucion**: añadir SIEMPRE el header `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15` a toda llamada API. Tambien `Accept: application/json`.
- **Tambien aplica a curl**: si llamas con `curl -u ...` desde un script, añadir `-H "User-Agent: Mozilla/5.0"`.

### Polylang Pro — Crear categorias traducidas via API

- **Polylang Pro acepta `lang` directamente en `POST /wp-json/wp/v2/categories`**. No necesitas usar el endpoint `/pll/v1/`.
- **Vincular como traduccion**: una vez creada la nueva categoria, `POST /wp-json/wp/v2/categories/{new_id}` con body `{"translations": {"es": ES_ID, "<lang>": NEW_ID}}` la vincula al cluster de traducciones.
- **Confirmacion**: la respuesta incluye `translations: {es: X, en: Y, ca: Z}` con todos los vinculos.
- **Caso real**: cluster GEO IA (2231) + Innovacion Tecnologia (2237) solo existian en ES. Para publicar EN/CA hubo que crear las 4 traducciones (EN: 2253+2257, CA: 2255+2259) antes de poder asignarlas a los posts.
- **Script tipo**: `_create_translated_categories.py` en el proyecto. Reutilizable.

### Polylang vinculacion traducciones posts (single-call vs separado)

- **Confirmado mayo 2026**: vincular `translations` en una SOLA llamada POST sobre cada post funciona sin vaciar contenido. Body: `{"translations": {"es": 21131, "en": 21132, "ca": 21133}}`.
- **Hacer la llamada en LOS TRES posts**, no solo en uno. Polylang necesita que cada post conozca a sus traducciones hermanas.
- **El BUG de vaciado de contenido** (documentado en seccion anterior) NO se reprodujo cuando solo se actualiza `translations` despues de que el post ya tiene contenido. Es seguro hacerlo asi: 1) crear post con content, 2) llamada separada para `translations`.

### Rank Math meta — Setear via /wp-json/wp/v2/posts/{id} meta field

- **Endpoint mas simple**: `POST /wp-json/wp/v2/posts/{id}` con body `{"meta": {"rank_math_title": "...", "rank_math_description": "...", "rank_math_focus_keyword": "..."}}`.
- **No se devuelven los valores** en el GET porque los meta protected no aparecen en `context=view`. Para verificar, consultar el HTML publico del post o usar `?context=edit` con auth.
- **Si Rank Math no esta configurado**, WordPress puede usar el `excerpt` del post como meta description fallback. Conviene setear el `excerpt` igualmente como red de seguridad.
- **Funciona sin pasar por** `POST /wp-json/rankmath/v1/updateMeta`, mas simple.

### Subida de imagenes y caracteres especiales

- **`-F "alt_text=..."` con curl puede fallar con caracteres no-ASCII** (acentos, eñes) si el sistema no esta en UTF-8 completo.
- **Solucion practica**: subir con alt_text en ASCII puro (sin acentos), luego actualizar el alt_text via PATCH/POST `/wp-json/wp/v2/media/{id}` con body JSON UTF-8 completo. La API JSON maneja UTF-8 sin problemas.
- **Mejor**: usar Python con `urllib` o `requests` y body JSON desde el principio en vez de form-data con curl.

### Convertir Markdown a HTML para WordPress

- **Usar `markdown.markdown(text, extensions=["extra", "tables", "sane_lists"], output_format="html5")`**.
- **Strippear** el bloque `<!-- SEO METADATA -->` y la primera linea `# H1` antes de convertir (WordPress setea el title del post separadamente).
- **Reemplazar** las rutas locales de imagenes (`AI-hero.jpg`) por las URLs de WordPress despues de subirlas.
- **HTML inline** (figure, div con styles, blockquote): se preserva porque `markdown` extension `extra` ignora bloques HTML ya formados.

### Rate limiting CloudFlare zoopa.es

- **Sintoma**: tras ~15-20 requests autenticados en pocos minutos, la web responde con timeout (`No route to host`) desde la misma IP. Ping a los IPs de CloudFlare tambien falla. Otros sitios CloudFlare (cloudflare.com, 498as.com) siguen respondiendo OK — el block es especifico de zoopa.es.
- **Causa**: WAF de zoopa.es activa rate limit por IP cuando detecta burst de POSTs autenticados.
- **Solucion**: esperar 15-30 minutos. El block expira solo. Para flujos largos, intercalar `sleep 2-3` entre llamadas POST.
- **Alternativa**: cambiar de red (4G/movil) o pedir al admin que whiteliste la IP temporalmente en CloudFlare dashboard.

### Estructura de URLs zoopa.es con Polylang

- **Permalink format por idioma**:
  - ES: `zoopa.es/es/{category-slug}/{post-slug}/`
  - EN: `zoopa.es/en/{category-slug}/{post-slug}/`
  - CA: `zoopa.es/ca/{category-slug}/{post-slug}/`
- **La categoria aparece en la URL** (no hay `/blog/` directo). El category-slug es el primer "directorio" tras el codigo de idioma.
- **Si el post tiene 2 categorias**, WordPress usa la primera (orden numerico de IDs) para la URL.

### Paginas de contacto por idioma (verificadas mayo 2026)

- ES: `https://zoopa.es/es/contactanos/` (ID 326)
- EN: `https://zoopa.es/en/contact-us/`
- CA: `https://zoopa.es/ca/contactans/`

### Featured media en POST

- **`featured_media: ID`** en el body del POST funciona bien. La imagen aparece correctamente como og:image y en el listing del blog.
- **No necesitas** asignar la imagen via dialogo de WordPress — la API REST es suficiente.

### Excerpt y meta description fallback

- Si seteas `excerpt: "<p>...</p>"` en el POST, WordPress lo usa como meta description si no hay Rank Math meta configurado.
- Util como **red de seguridad** para SEO basico mientras se setea Rank Math correctamente.

### Validacion post-publicacion — checks esenciales

Verificar SIEMPRE despues de publicar consultando el HTML publico:

```python
import urllib.request, re
url = "https://zoopa.es/es/{cat}/{slug}/"
html = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})).read().decode()

assert len(re.findall(r"<h1[^>]*>", html)) == 1  # exactamente 1 H1
assert "og:image" in html
assert re.search(r'<meta name="description"[^>]*content="[^"]+"', html)  # meta description presente
assert re.findall(r'hreflang="[^"]+"', html)  # hreflang tags para Polylang
# verificar bloques editoriales obligatorios
assert "Lo que necesitas saber" in html  # key takeaways
assert "Glosario" in html or "Glossary" in html or "Glossari" in html
assert "Preguntas frecuentes" in html or "Frequently asked" in html or "Preguntes freqüents" in html
```

### Scripts reutilizables del proyecto AI Chips (mayo 2026)

Tres scripts Python en `proyecto-AI-chips-economy-23052026/`:

1. **`_publish.py`**: Lee `.md`, convierte a HTML, sube post nuevo con autor/categorias/featured_media. Toma argumentos: file, lang, slug, hero_id, hero_url, rc1_url, rc2_url, categories_csv.
2. **`_create_translated_categories.py`**: Crea categorias EN/CA como traducciones de las ES. Hardcoded mapping (es_id → name + slug).
3. **`_update_posts.py`**: Re-renderiza y actualiza posts ya publicados. Util para iterar cambios editoriales sin recrear.
4. **`_link_and_seo.py`**: Vincula translations Polylang + setea Rank Math meta en una pasada.

Los 4 scripts asumen que las credenciales estan en env vars `WP_USER`, `WP_APP_PASSWORD`, `WP_SITE`. Recomendado: guardarlas en `_system/.wp-credentials` (gitignored) y hacer `source` al inicio de cada sesion.

### Caso de estudio — Proyecto "AI Chips" (3 posts ES+EN+CA, mayo 2026)

- Posts: ID 21131 (ES), 21132 (EN), 21133 (CA).
- Featured media: ID 21128 (Tara Jacoby) compartida entre los 3.
- Categorias creadas: 2253 (EN Innovation), 2255 (CA Innovacio), 2257 (EN GEO AI), 2259 (CA GEO IA).
- Validacion HTML publico: H1 unico, og:image, meta description, 13 hreflang tags cross-linked, 6 img tags renderizados.
- Tiempo total publicacion: ~12 minutos los 3 idiomas (incluye creacion de categorias traducidas).
- Coste posterior por rate limit: ~20 min de espera tras un burst de updates.
