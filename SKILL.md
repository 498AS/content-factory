---
name: content-factory
description: |
  Genera contenido multicanal (hasta 41 canales, 4 idiomas) a partir de un source.md
  usando el sistema WriterBatch Zoopa. Orquesta seleccion de canales, preguntas pre-publicacion,
  generacion de outputs y revision ortografica/estilo.
  Cubre los dos blogs de la casa, que son tecnicamente distintos: el WordPress de zoopa.es
  (Polylang + Rank Math) y el blog estatico de 498advance.com (Perspectivas: HTML con clases
  de blog.css, plantilla con marcadores, schema a mano, cuatro idiomas con slug compartido).
  Triggers: "content-factory", "launch", "lanzar proyecto", "generar contenido", "writerbatch",
  "publicar contenido", "content batch", "/content-factory".
  NO usar para optimizar/auditar un PERFIL o Company Page de LinkedIn (headline, About,
  experiencia, tagline, SSI, afinidad con perfiles objetivo): para eso usar `linkedin-profile-optimizer`.
  Este skill genera CONTENIDO (posts, articulos, hilos), no trabaja sobre el activo perfil/Page.
---

# Skill: Content Factory — WriterBatch Zoopa

## Proposito

Generar todos los outputs de contenido multicanal para un proyecto a partir de un unico `source.md`. El flujo completo incluye seleccion de canales, preguntas pre-publicacion, generacion con system prompt especializado y revision obligatoria de ortografia y estilo.

## Archivos Clave

### Referencias editoriales (markdown)

| Elemento | Ruta |
|----------|------|
| **Catalogo de canales** | `~/.claude/skills/content-factory/references/channel-catalog.md` |
| **Reglas ortografia** | `~/.claude/skills/content-factory/references/orthography-rules.md` |
| **Lecciones aprendidas** | `~/.claude/skills/content-factory/references/lessons-learned.md` |
| **Componentes HTML para blogs WordPress · solo zoopa.es** | `~/.claude/skills/content-factory/references/blog-html-components.md` |
| **Blog estático de 498advance.com (Perspectivas)** ⭐ | `~/.claude/skills/content-factory/references/blog-498advance-static.md` |
| **Estructura del source.md (3-block brief)** ⭐ | `~/.claude/skills/content-factory/references/content-brief-structure.md` |
| **Patrones editoriales (killer line, paradoja, "cuándo X suma")** ⭐ | `~/.claude/skills/content-factory/references/editorial-patterns.md` |
| **Voz LinkedIn · Carlos Ortet (cuenta personal)** ⭐ | `~/.claude/skills/content-factory/references/linkedin-voice-carlos-ortet.md` |
| **Estilo Substack (email + permalink, no blog)** ⭐ | `~/.claude/skills/content-factory/references/substack-style.md` |
| **Voz X/Twitter (humano, no LLM)** ⭐ | `~/.claude/skills/content-factory/references/x-twitter-voice-style.md` |
| **Humanize Text · Anti-AI Detection Guide** ⭐ | `~/.claude/skills/content-factory/references/humanize-text-anti-ai.md` |

⭐ = nuevos en mayo 2026. `linkedin-voice-carlos-ortet.md` es OBLIGATORIO leer y aplicar antes de redactar `linkedin.md` o `linkedin_ca.md` cuando el autor sea Carlos Ortet (cuenta personal). Captura las correcciones reales que aplicó al post "La siguiente bestIA" (2026-05-10): hook coloquial-irónico, conectores hablados, glosa parentética para audiencia mixta, auto-ironía, balance "soy pro-X pero...", pregunta abierta final, política estricta de anonimización (clientes con NDA → eliminar caso, no anonimizar a nivel sectorial), y otros patrones documentados.

`substack-style.md` es OBLIGATORIO leer y aplicar antes de redactar `substack_ready.txt`. Captura los patrones reales validados con el proyecto AI Chips Economy (mayo 2026): subject line ≤55 chars sin marca, preheader que expande sin repetir, headers H2 editoriales/aforísticos (no descriptivos), conversión de componentes HTML del blog a prosa equivalente, tono conversacional con conectores hablados, cierre obligatorio con CTA suscripción + lista de versiones long-form (blog ES/EN/CA + Medium). Substack NO es un blog Wordpress condensado — es un email + permalink con reglas propias.

`x-twitter-voice-style.md` es OBLIGATORIO leer y aplicar antes de redactar `x_twitter_ready.txt` y `threads_ready.txt` (mismas reglas de tono y cadencia). Captura los anti-patrones de IA detectables al instante (em-dashes, "no es X, es Y", "la conclusión:", "lectura completa con datos verificados...", flechas → en listas, rule-of-three) y los patrones que SÍ funcionan: opener con dato raro/contradicción, hilos cortos (3-12 unidades de consideración), ritmo asimétrico (tuits de 30 y de 280 chars mezclados), castellano oral (contracciones, "o sea", "lo que pasa es que"), cierre human-first (pregunta abierta o link sin frase ceremoniosa). Aprendido tras publicar un hilo de 19 tuits que sonaba demasiado a IA (2026-05-24).

`blog-498advance-static.md` es OBLIGATORIO leer y aplicar antes de redactar cualquier `blog498a_*.md`. El blog de 498advance.com (Perspectivas, abierto en septiembre de 2026) **no es WordPress**: es HTML estático con clases de `blog.css`, plantilla fija con `{{MARCADORES}}`, schema escrito a mano y un constructor propio en el repo de la web. Si se le aplica el estilo del blog de zoopa.es sale HTML con estilos inline que rompe el design system y se salta el schema. Cubre las dos plantillas (estudio y artículo), el inventario de clases, la política de canónico (pieza nativa vs pieza derivada de carlosortet.com), los cuatro idiomas con slug compartido y el reparto de trabajo con `_i18n/blog_build.py`.

### Scripts ejecutables (en el skill global)

| Script | Para qué | Cuándo invocarlo |
|--------|----------|-------------------|
| **`scripts/new-project.sh tema [--paste]`** | Crea `project_DDMMAAAA_tema/` con source.md + output/ + metadata.json | Antes de cualquier proyecto nuevo |
| **`scripts/metadata.py`** | CRUD sobre `metadata.json` por proyecto (publications, metrics, tags) | PASO 4 (set-generated) y PASO 5 (add-publication) |
| **`scripts/validators/run_all.py`** | Ejecuta los validators (titles, numbers, catalan, blog completeness y, en `.html`, blog 498A) | Hook `PostToolUse` después de cada `Write`/`Edit` en `output/*` |
| **`scripts/publisher/wp_publish.py`** | Publica blog en WordPress via REST API con Polylang single-call + Rank Math | PASO 5.A, **solo** si el destino es zoopa.es |
| **`scripts/publisher/build_498a_post.py`** | Convierte `blog498a_<lang>.md` en el HTML de la plantilla del blog estático de 498advance.com | PASO 5.B, si el destino es 498advance.com |
| **`scripts/validators/validate_blog_498a.py`** | Valida un post del blog de 498advance.com: maquetación, clases, anclas, schema, canónico, cifras y enlaces | PASO 5.B, tras generar cada `.html` |

### Workspace project files

| Elemento | Ruta |
|----------|------|
| System prompt | `_system/system_prompt_writerbatch_zoopa.md` (relativo al workspace contentfactory) |
| Source content | `project-XXX/source.md` (dentro del workspace) |
| Output dir | `project-XXX/output/` |
| Metadata por proyecto | `project-XXX/metadata.json` (schema en `scripts/metadata-schema.md`) |

### Cómo se invocan los scripts del skill global

Los scripts viven en el skill global pero operan sobre el **workspace local** del usuario (típicamente `/Users/carlos/Documents/claudecode-proj/contentfactory/`). El usuario los invoca desde el workspace con paths absolutos:

```bash
# Crear proyecto:
~/.claude/skills/content-factory/scripts/new-project.sh tv-oscura --paste

# Validar un output:
python3 ~/.claude/skills/content-factory/scripts/validators/run_all.py project_XXX/output/blog.md

# Publicar en WordPress (solo zoopa.es):
python3 ~/.claude/skills/content-factory/scripts/publisher/wp_publish.py \
  --file project_XXX/output/blog.md --lang es --categories 2245,2235 --status draft

# Generar los posts del blog estatico de 498advance.com (es, ca, en, it):
python3 ~/.claude/skills/content-factory/scripts/publisher/build_498a_post.py \
  project_XXX/output/blog498a_{es,ca,en,it}.md --build

# Validar un post del blog de 498advance.com:
python3 ~/.claude/skills/content-factory/scripts/validators/validate_blog_498a.py \
  "/Users/carlos/Documents/claudecode-proj/design system 498A/498Adesign/blog/slug.html"
```

**O symlinkar al `_system/` local** para preservar el workflow histórico:

```bash
ln -sf ~/.claude/skills/content-factory/scripts _system
```

### Setup walkthrough

Ver `~/.claude/skills/content-factory/docs/HOW-TO-NEW-PROJECT.md` para el flujo completo paso a paso (incluye troubleshooting).

---

## Flujo de Ejecucion

### PASO 0: Selector de canales (OBLIGATORIO)

**Antes de generar CUALQUIER contenido, preguntar al usuario:**

> "Que canales quieres incluir en esta campana?"

1. Presentar la lista completa de canales (ver `references/channel-catalog.md`)
2. Marcar los 12 canales core como activados por defecto
3. Dejar que el usuario seleccione/deseleccione
4. Confirmar seleccion antes de continuar

**Total disponible: 41 canales | Core por defecto: 12 canales**

**Los canales de blog dependen del destino** (PASO 1, pregunta 1): si es zoopa.es se generan `blog.md` / `blog_en.md` / `blog_ca.md`; si es 498advance.com se generan `blog498a_es.md` / `_ca` / `_en` / `_it` y **no** los de WordPress. No generar los dos juegos salvo que el usuario pida publicar en las dos webs.

Nunca asumir canales sin preguntar. Nunca generar contenido sin completar este paso.

---

### PASO 1: Preguntas pre-publicacion (OBLIGATORIO)

Despues de seleccionar canales, preguntar SIEMPRE:

1. **Web de publicacion** — PREGUNTAR SIEMPRE, sin asumir. Los dos destinos son técnicamente
   distintos y el output no es intercambiable:

   | Destino | Qué es | Outputs | Publicación |
   |---|---|---|---|
   | **zoopa.es** | WordPress + Polylang + Rank Math | `blog.md`, `blog_en.md`, `blog_ca.md` (HTML con estilos inline) | REST API · `wp_publish.py` · PASO 5.A |
   | **498advance.com** | HTML estático, repo `498AS/498a-new-web-design` | `blog498a_es.md`, `_ca`, `_en`, `_it` (markdown restringido → plantilla) | `build_498a_post.py` + `_i18n/blog_build.py` + FTPS · PASO 5.B |

   `498as.com` ya no es un destino: hace 301 hacia `498advance.com` y no queda WordPress ahí.
   Si el destino es 498advance.com, leer `references/blog-498advance-static.md` antes de redactar.

   **Si el destino es 498advance.com, preguntar además el canónico** (cambia el `<head>` y el cuerpo):
   *"¿Es una pieza nativa de 498A (estudio, método, producto → canónico en 498advance.com) o una pieza
   derivada de carlosortet.com (canónico en la web personal)?"*. En el caso derivado el texto **no**
   puede ser un copia-pega: entradilla nueva, bloque "qué hacemos con esto en 498A" y enlaces a servicio.
   Ver § 7 de la referencia.

2. **Autor del blog** — Carlos Ortet u otro autor. En zoopa.es tiene que existir como usuario de
   WordPress; en 498advance.com el autor va en el front matter (`autor`, `rol_autor`, `bio_autor`)
3. **Canal de LinkedIn** — ZOOPA, 498AS o Carlos Ortet personal
4. **Tema nuevo o existente** — Si ya hay posts anteriores, revisar para no duplicar y enlazar
5. **Imagen principal** — URL o ruta de la featured image (blog, Substack, Medium, LinkedIn, og:image)
6. **Imagen secundaria** — URL o ruta opcional para cuerpo del blog o plataformas con varias imagenes
7. **⭐ Anecdotas reales con cliente nombrado** — *"¿Tienes 1-2 anecdotas reales de proyectos con clientes nombrados (con o sin NDA) que ilustren el angulo? Sin esto el post sale como divulgacion; con esto sale como posicionamiento."* Si el usuario no tiene a mano, dejar placeholder visible en el `source.md` (formato `[EJEMPLO 1 — historia real ...]`) y avisar antes de PASO 4.

8. **⭐ Si el autor es Carlos Ortet, añadir entrada a carlosortet.com (con pregunta previa)** — Cuando se publique una pieza editorial (blog en zoopa.es / 498advance.com, post en Medium, artículo en Harvard Deusto, Substack relevante, paper, etc.) firmada por **Carlos Ortet**, PREGUNTAR siempre al usuario despues de publicar: *"¿Añadimos esta publicación a `carlosortet.com`?"*. Si el usuario dice sí, ejecutar el sub-flujo de PASO 6.

### Reglas derivadas

- **Blog siempre primero.** Su URL se integra despues en LinkedIn (CTA), Substack (enlace), WhatsApp (referencia), Medium/Dev.to/Hashnode (canonical URL) y cualquier plataforma que lo necesite.
- **Titulos en sentence case.** Solo la primera letra de la frase en mayuscula. Nombres propios y acronimos mantienen su capitalizacion. Aplica a todos los outputs en todos los idiomas.
- **Verificar URLs de CTAs antes de meterlas.** Hacer `curl -I` (HTTP HEAD) a cada URL candidata de mid-CTA y final-CTA. Si 404, fallback al index del servicio o al contacto general. Ver `references/lessons-learned.md` "CTAs URLs frágiles".
- **⭐ Sin em-dash (`—`), sin referencias temporales relativas, sin frases formulaicas de IA.** Reglas globales en `references/orthography-rules.md` § 3. Aplica a TODOS los canales (blog, LinkedIn, X, Substack, Medium, WhatsApp, Quora, Bluesky, Threads, etc.) y todos los idiomas. NO usar `—` ni `–`; NO usar "esta semana / este mes / este año / hoy / recientemente"; NO usar "También es, técnicamente, falsa" / "Lectura completa con datos verificados" / "La conclusión:" ni similares. Auditarlo en PASO 3.6 (revisión ortográfica final).

### ⭐ Validar la estructura del `source.md` antes de PASO 4

Verificar que el `source.md` cumple el formato 3-block descrito en `references/content-brief-structure.md`:

1. **Bloque 1 — Tesis** (1 párrafo, 60-100 palabras, posición clara)
2. **Bloque 2 — Hechos curados** (5-15 bullets, cada uno con dato + fuente + fecha)
3. **Bloque 3 — Ángulo de marca** (3-5 bullets con anécdotas reales firmadas)

Si falta alguno, devolver al usuario para que lo complete. Sin las 3 partes, el output sale neutral.

---

### PASO 2: Verificacion pre-launch

Antes de ejecutar, verificar que existen:

1. `_system/system_prompt_writerbatch_zoopa.md` — visible en el workspace actual
2. `project-XXX/source.md` — con el contenido completo (todos los items)
3. `project-XXX/output/` — directorio de salida creado
4. `project-XXX/metadata.json` — si no existe, crearlo con `python3 _system/metadata.py init project-XXX`

Si el proyecto no existe, sugerir al usuario crearlo con `./_system/new-project.sh tema-corto` (no crear carpetas a mano, el script genera la estructura completa con metadata.json inicial).

Si `source.md` esta vacio, no continuar — pedir al usuario que pegue el contenido.

Tras verificar, contar palabras del source y guardarlas: `python3 _system/metadata.py set-source-words project-XXX --auto`.

---

### PASO 3: Generacion de contenido

1. Leer el system prompt de `_system/system_prompt_writerbatch_zoopa.md` y adoptarlo como guia de voz, estilo y especificaciones por canal.
2. Leer todo el contenido de `project-XXX/source.md` como unico input autorizado.
3. Aplicar las reglas del system prompt:
   - Todos los items de source.md son igualmente importantes
   - Si hay multiples items, TODOS se integran en TODOS los outputs
   - No ignorar ni descartar ninguna parte salvo instruccion explicita
4. Generar outputs en este orden:
   - Blog ES → Blog EN → Blog CA → Blog Lectura Facil (si aplica)
     *(si el destino es 498advance.com: `blog498a_es` → `_ca` → `_en` → `_it`, con el MISMO slug)*
   - LinkedIn ES → LinkedIn CA
   - X/Twitter → Threads
   - WhatsApp Grupos ES → CA → Canal ES → CA
   - Substack → Medium
   - Resto de canales seleccionados en orden alfabetico
5. Idiomas: primero espanol, luego catalan e ingles segun canales seleccionados.
6. Escribir cada output en `project-XXX/output/` con el nombre de archivo del catalogo de canales.
7. No incluir razonamiento intermedio. Solo el contenido final en cada archivo.

### ⭐ Estilo específico por canal (OBLIGATORIO leer antes de redactar)

| Canal | Archivo de referencia | Cuándo se aplica |
|---|---|---|
| `linkedin.md` / `linkedin_ca.md` | `references/linkedin-voice-carlos-ortet.md` | Cuenta personal de Carlos Ortet (LinkedIn personal) |
| `substack_ready.txt` | `references/substack-style.md` | Siempre — Substack es email + permalink, no blog Wordpress condensado |
| `x_twitter_ready.txt` / `threads_ready.txt` | `references/x-twitter-voice-style.md` | Siempre — X penaliza voz LLM, requiere cadencia humana asimétrica |
| `blog.md` / `blog_en.md` / `blog_ca.md` | `references/blog-html-components.md` + `references/editorial-patterns.md` | Siempre — blog largo Wordpress con componentes HTML inline |
| `blog498a_es.md` / `_ca` / `_en` / `_it` | `references/blog-498advance-static.md` + `references/editorial-patterns.md` | Siempre — blog estático de 498advance.com. **NO usar `blog-html-components.md` ni `wp_publish.py`** |

**Regla crítica**: si vas a generar `substack_ready.txt`, un output de LinkedIn personal de Carlos, o `x_twitter_ready.txt` / `threads_ready.txt`, lee primero el file de estilo correspondiente. Aplicar el estilo del blog largo a otros canales produce: (a) Substack → subject line aburrido + cuerpo con HTML que el editor Prosemirror rompe; (b) X → hilos formulaicos detectables como IA al instante (em-dashes, "no es X, es Y", "lectura completa con datos verificados", rule-of-three obsesivo).

### ⭐ Patrones editoriales obligatorios para blogs

Aplicar **al menos 2 de 4** de los patrones documentados en `references/editorial-patterns.md`. Recomendado: los 4 si el contenido lo permite.

| Patrón | Cuándo aplicar | Output |
|--------|----------------|--------|
| **1. Killer line + pull-quote** | Siempre (1 por blog) | Frase 15-25 palabras autocontenida, aislada en `<blockquote>` (componente "Pull-quote" de blog-html-components.md). Reusada textual en LinkedIn, X, Substack. En 498advance.com el equivalente es `<aside class="callout">`, no `<blockquote>`. |
| **2. Paradoja explícita** | Cuando el ángulo identifica una decisión sectorial cuestionable | Subsección con estructura: A vs B opuestos → síntesis tipo *"todo tiene que parecer lo que no es"* |
| **3. "Cuándo X suma y cuándo X resta"** | Siempre que la tesis ataque una práctica del sector | Subsección H3 que matiza, distinguiendo cuando la práctica es decisión deliberada útil vs cuando es reflejo/moda contraproducente |
| **4. Caso real con cliente nombrado** | Siempre (1-2 casos) | Sección "Lo que vemos desde la trinchera" con anécdotas firmadas (clientes con o sin NDA). Estructura: tensión → decisión → lección |

### ⭐ Componentes HTML obligatorios en blogs de WordPress (zoopa.es)

> Esta sección es **solo** para zoopa.es. En 498advance.com los componentes son las clases de
> `blog.css` y la estructura obligatoria está en § 5 de `references/blog-498advance-static.md`:
> `.post-takeaways` arriba, `.callout`, `.datos`, `.tabla-datos`, `.figura`, `.detalle`,
> `.metodologia`, `.datos-abiertos`, `.fuentes`, `.post-autor`. Cero estilos inline.

Incluir **siempre** estos componentes (definiciones en `references/blog-html-components.md`):

1. **Featured image figure inline** al inicio del cuerpo (después del H1, antes de la intro)
2. **Stat block 2-column** con 2-3 cifras de impacto del bloque 2 del source.md (gradient teal-marino)
3. **Key takeaways** ("Lo que necesitas saber") con 5-7 bullets
4. **Mid-CTA** con gradient charcoal hacia página de servicio (~50% del cuerpo)
5. **Pull-quote** aislado con la killer line (antes del CTA final)
6. **Final-CTA** negro sólido hacia /contactanos/ (más fuerte que el mid)
7. **Glosario** de entidades (al final, antes del FAQ)
8. **FAQ** ≥5 preguntas (al final)

---

### PASO 3.5: Optimizacion SEO y GEO (OBLIGATORIO)

**Despues de generar todos los outputs**, aplicar las siguientes optimizaciones a TODOS los blogs (ES, EN, CA, ES Facil):

#### SEO

1. **Bloque de metadatos** al inicio del archivo (como comentario HTML):
   - Title tag (max 60 chars, con marca)
   - Meta description (max 155 chars, con dato clave y CTA implicita)
   - Slug optimizado (keywords separadas por guiones)
   - Focus keyword y secondary keywords
   - Canonical URL
   - Category y tags
2. **Alt text descriptivo** en todas las imagenes: no generico, sino que describa el contenido visual y contenga keywords relevantes
3. **Seccion "Lo que necesitas saber"** (key takeaways) despues de la intro: 5-7 bullets con los datos mas citables del articulo. Optimizado para featured snippets de Google y para extraccion por LLMs
4. **Internal linking**: enlazar a posts relacionados del mismo cluster/categoria Y a la pagina de servicio correspondiente (ver regla de CTAs abajo)
5. **CTAs contextuales (OBLIGATORIO)**: cada blog post debe incluir:
   - **Mid CTA** (tras el ~50% del contenido): enlace a la pagina de servicio relacionada. Estilo: fondo gris, texto "Esto es lo nuestro →"
   - **Final CTA**: enlace a /contactanos/. Estilo: fondo negro, texto "Hablemos"
   - **CTA de cluster** (si aplica): enlace a la pillar page del cluster tematico. Ejemplo: posts GEO → /es/servicios/georadar/
6. **Heading hierarchy**: exactamente 1 H1 (titulo del post). Subtitulos en H2. Sub-subtitulos en H3. Nunca saltar niveles.
7. **Meta description**: maximo 155 caracteres. No repetir el nombre de marca si ya esta en el title tag.
8. **Alt text**: descriptivo y con keywords, no generico. Cada imagen debe tener alt text unico.

#### GEO (Generative Engine Optimization)

1. **Glosario de entidades** al final del articulo: definiciones claras y autonomas de cada termino tecnico, persona, herramienta u organizacion mencionada. Cada entrada debe ser citable de forma independiente por un LLM
2. **FAQ ampliado**: minimo 5 preguntas, formuladas como long-tail keywords que un usuario buscaria. Respuestas directas en la primera frase, luego expansion
3. **Datos autonomos**: cifras y estadisticas deben incluir fuente y fecha para maximizar citabilidad
4. **Entity-rich content**: mencionar explicitamente nombres de empresas, herramientas, papers academicos y personas con contexto suficiente para que un LLM los identifique como entidades
5. **Links salientes E-E-A-T**: incluir 2-4 links a fuentes autoritativas (papers academicos, documentacion oficial Google, instituciones como CSIC, UAB, universidades). Aumenta credibilidad para LLMs y Google
6. **Formato citable**: parrafos cortos con afirmaciones autonomas que un LLM pueda extraer y citar directamente. Evitar contexto que requiera leer el parrafo anterior para entender

Estas optimizaciones aplican tambien a Medium, Dev.to, Hashnode y HackerNoon (sin bloque de metadatos WordPress, pero si con alt text, glosario y FAQ ampliado).

#### Publicacion del metadata en WordPress

Al publicar el blog en WordPress (solo zoopa.es), los metadatos del comentario HTML deben introducirse en los campos correspondientes del editor:

| Campo del comentario HTML | Donde introducirlo en WordPress |
|---------------------------|--------------------------------|
| Title | Titulo del post (y campo SEO title en Yoast/RankMath) |
| Meta description | Campo "Meta description" en Yoast/RankMath |
| Slug | Campo "URL slug" / Permalink del post |
| Focus keyword | Campo "Focus keyphrase" en Yoast/RankMath |
| Canonical | Campo "Canonical URL" en Yoast (solo si es distinta de la URL del post) |
| Category | Selector de categorias de WordPress |
| Tags | Selector de etiquetas de WordPress |

**Regla:** El bloque de metadatos NO se publica como parte del contenido visible. Es una referencia para configurar los campos SEO del CMS. Al pegar el contenido en WordPress, eliminar el comentario HTML o asegurarse de que no se renderiza.

#### Maquetacion HTML avanzada para blogs

Los blogs (`blog.md`, `blog_en.md`, `blog_ca.md`) deben incluir maquetacion HTML profesional inline para que WordPress renderice tablas, key takeaways, glosarios y FAQs con diseno avanzado. Ver `references/blog-html-components.md` para los componentes disponibles.

**Reglas de maquetacion:**

1. **Tablas**: nunca usar tablas Markdown planas. Usar tablas HTML con clases CSS inline que incluyan bordes, colores alternos, cabecera destacada y responsive design
2. **Key takeaways**: usar un bloque HTML con fondo de color, borde lateral, icono y tipografia destacada
3. **FAQ**: usar acordeones HTML/CSS o bloques con separadores visuales claros
4. **Glosario**: usar bloques de definicion con tipografia jerarquizada (termino en bold/color, definicion en texto regular)
5. **Datos destacados**: cifras importantes deben ir en bloques de estadistica con numero grande y fuente debajo
6. **Imagenes**: deben ir dentro de `<figure>` con `<figcaption>` descriptivo
7. **Citas**: usar `<blockquote>` con estilo editorial (borde lateral, italica, fuente citada)

**Todo el CSS debe ser inline** (atributo `style=""`) para garantizar compatibilidad con WordPress, newsletters y RSS. No depender de hojas de estilo externas ni de clases CSS del tema.

Consultar `references/blog-html-components.md` para copiar los componentes HTML exactos.

---

### PASO 3.6: Revision ortografica y de estilo (OBLIGATORIO)

**Despues de optimizar SEO/GEO y ANTES de dar los outputs por finalizados**, ejecutar la revision completa descrita en `references/orthography-rules.md`.

Resumen:

1. **Acentos y caracteres especiales** — Revisar cada output segun su idioma (ES: acentos/n/¿¡, CA: graves/agudos/c/l·l, EN: nombres propios)
2. **Capitalizacion sentence case** — Verificar que todos los titulos, subtitulos y encabezados cumplen la regla
3. Recorrer cada archivo, corregir y guardar

**El proyecto NO se considera finalizado hasta completar los pasos 3.5, 3.6 y 3.7.**

---

### PASO 3.7: Anti-AI-detection check (OBLIGATORIO antes de cada publicacion)

**Antes de marcar cualquier output como listo para publicar**, aplicar este checklist de 12 puntos. Aplica a TODOS los canales, pero es CRITICO para Hacker News, Quora, Reddit r/programming, r/MachineLearning, Turnitin-checked content.

> **Before publishing, check if any of these appear in your text:**
>
> - [ ] "Delve into" / "Leverage" / "Navigate" / "Unlock" / "Harness"
> - [ ] "Groundbreaking" / "Revolutionary" / "Cutting-edge" / "Seamless"
> - [ ] "Furthermore" / "Moreover" / "Additionally" / "Crucially"
> - [ ] "In short" / "Ultimately" / "The conclusion:"
> - [ ] More than 1 em-dash
> - [ ] "Not X, but Y" structure
> - [ ] Arrows → in lists
> - [ ] Uniform paragraphs of 4-6 sentences each
> - [ ] CTA at the end ("read the full", "subscribe")
> - [ ] Zero typos, zero minor errors
> - [ ] Zero spoken connectors ("So,", "Look,", "Here's the thing")
> - [ ] Zero specific anecdotes (no dates, no names)
>
> **Threshold:**
> **If you check 3 or more boxes, your text will sound like LLM and a detector will flag it. Rewrite.**

#### Tablas de referencia rápida (anti-patterns)

**Lexical (words that betray):**

| CATEGORY | EXAMPLES | WHY IT BETRAYS |
|---|---|---|
| Pretentious verbs | delve, leverage, navigate, unlock, harness, foster, embark, illuminate, underscore | Overused by ChatGPT/Claude. Almost never in spontaneous human writing. |
| Empty adjectives | groundbreaking, revolutionary, cutting-edge, seamless, robust, comprehensive, multifaceted | Modifiers without concrete information. |
| Formulaic adverbs | crucially, importantly, notably, significantly, ultimately | Connectors LLMs use to signal transitions. |
| Abstract nouns | transparency, intelligence (noun), efficiency, optimization, alignment | LLMs abstract when humans would use examples. |

**Structural (forms that betray):**

| PATTERN | WHY IT BETRAYS |
|---|---|
| "Rule of three" (X, Y, and Z) | Overused classical rhetorical pattern. |
| Em-dashes for parenthetical inserts (—) | LLMs overuse. Humans use commas, parens, or new sentences. |
| "Not X, but Y" | LLM punchline structure, almost never natural. |
| "In short:" / "Ultimately:" | Formulaic closings. Humans don't signal conclusions this way. |
| Arrows → in lists | Almost exclusive to LLMs. |
| All-bullets lists | Humans mix prose and bullets. LLMs go all-bullets. |
| Uniform paragraphs (4-6 sentences each) | Low burstiness. Humans vary radically. |
| Formal connectors (Furthermore, Moreover) | Academic-only. In social media or comments: betrays. |
| CTA at end ("read more", "subscribe") | Marketing-speak, easily detectable. |

#### Procedimiento operativo del check

1. **Auto-scan** del output con grep para detectar palabras-bandera (verbos, adjetivos, conectores formales):
   ```bash
   # Lexical flags
   grep -iEn "\b(delve|leverage|navigate|unlock|harness|foster|embark|illuminate|underscore)\b" output/<file>
   grep -iEn "\b(groundbreaking|revolutionary|cutting-edge|seamless|robust|comprehensive|multifaceted)\b" output/<file>
   grep -iEn "\b(crucially|importantly|notably|significantly|ultimately)\b" output/<file>
   grep -iEn "\b(transparency|efficiency|optimization|alignment)\b" output/<file>

   # Structural flags
   grep -nE "—" output/<file>                          # em-dashes (count > 1 = rewrite)
   grep -nE "→" output/<file>                          # arrows in lists
   grep -nE "^(In short|Ultimately|The conclusion):" output/<file>
   grep -iEn "\b(furthermore|moreover|additionally|subsequently)\b" output/<file>
   grep -iEn "(read the full|subscribe|learn more)" output/<file>
   ```

2. **Conteo de em-dashes**: si `grep -c "—" output/<file>` devuelve >1, reescribir.

3. **Detectar arrows en listas**:
   ```bash
   grep -E "^\s*[—-].*→|^→" output/<file>
   ```

4. **Verificar burstiness** (asimetria parrafos): si todos los parrafos tienen 4-6 frases similares, reescribir al menos 2 con longitud distinta (1 frase muy corta + 1 muy larga).

5. **Verificar marcadores humanos**:
   - Al menos 1 conector oral ("So,", "Look,", "Here's the thing")
   - Al menos 1 anecdota especifica con fecha o nombre
   - Al menos 1 contraccion (don't, it's, we're)
   - Idealmente 1-2 typos o errores menores aceptables (especialmente en ESL writers)

#### Severidad por canal

Aplicar el threshold ajustado segun la plataforma destino:

| Canal | Threshold maximo de boxes marcados | Politica |
|---|---|---|
| Hacker News, Turnitin, GPTZero/Originality.ai | **0 boxes** | Research-assist only. Carlos escribe 100% manual. |
| Quora, Reddit r/programming, r/MachineLearning | **≤1 box** | Edit manual fuerte ≥30% prose reescrita. Sin Grammarly. |
| Reddit r/europe, r/news | **≤2 boxes** | Edit ligero OK. |
| LinkedIn, Substack, Medium, X, Bluesky, Threads, WhatsApp, Blog WP | **≤3 boxes** | Skill drafts OK con voces personales aplicadas. |

#### Referencias completas

Para guia tecnica completa (perplexity, burstiness, stylometric features, casos reales validados), ver `references/humanize-text-anti-ai.md`. Es **OBLIGATORIO leerla y aplicarla** la primera vez que se ejecuta el skill, y consultarla en cada PASO 3.7.

**El proyecto NO se considera finalizado hasta completar los pasos 3.5, 3.6 y 3.7.**

---

### PASO 4: Validacion de outputs

Verificar que `project-XXX/output/` contiene EXACTAMENTE los archivos de los canales seleccionados en PASO 0. Ni mas ni menos.

Consultar `references/channel-catalog.md` para la tabla completa de archivos esperados por canal.

### Validators automaticos

Cada vez que se hace `Write`/`Edit` sobre un fichero en `project-XXX/output/`, el hook `PostToolUse` de Claude Code (configurado en `.claude/settings.json` del workspace) ejecuta `_system/validators/run_all.py`. Esto produce avisos en stdout sobre:

- Sentence case en headings
- False friends `billion`/`billon` (ES) o `bilions` (CA)
- Caracteres catalanes faltantes (ç, l·l) en archivos `*_ca.md`
- Completitud de blogs de WordPress: bloque SEO, key takeaways, mid-CTA, final-CTA, glosario, FAQ ≥ 5, alt text, exactamente 1 H1, palabras minimas (se salta los `blog498a_*`, que tienen otra estructura)
- Posts del blog de 498advance.com (`.html` en `blog/` o `<lang>/blog/`): maquetacion sin estilos inline, clases que existen en `blog.css`, anclas de seccion, indice coherente, JSON-LD, canonico, cifras canonicas y enlaces internos

**Procedimiento:** revisar los avisos despues de cada escritura y corregir antes de continuar al siguiente fichero. Los avisos NO bloquean, pero deben resolverse antes de PASO 5.

Ejecucion manual: `python3 _system/validators/run_all.py project-XXX/output/blog.md`.

### Registrar canales generados

Tras escribir todos los outputs, marcar en metadata:

```bash
python3 _system/metadata.py set-generated project-XXX --channels blog_es,blog_en,blog_ca,linkedin_es,...
```

Convencion de keys: `<canal_base>_<idioma>` (ej: `blog_es`, `linkedin_ca`, `whatsapp_canal_es`). El blog estatico de 498advance.com usa `blog498a_es`, `blog498a_ca`, `blog498a_en`, `blog498a_it`, distintas de `blog_es` (que sigue siendo el de WordPress). Ver `_system/metadata-schema.md`.

---

### PASO 5.A: Publicacion en WordPress · solo zoopa.es (si aplica)

Cuando el destino sea el blog de zoopa.es (WordPress + Polylang + Rank Math), seguir este protocolo.

**Si el destino es 498advance.com, saltar a PASO 5.B: ahi no hay WordPress.** `498as.com` hace 301 hacia `498advance.com` y su `/wp-json/` da 404 (verificado 2026-09-27).

#### 5.1 Publicar via API REST — CLI con curl/python (OBLIGATORIO)

**NUNCA usar Playwright/MCP para operaciones de WordPress.** Usar siempre la CLI (curl o python) con la API REST de WordPress. Es mas rapido, fiable y no sufre problemas de modales, timeouts ni snapshots enormes.

**Autenticacion:** Usar Application Password de WordPress o cookies de sesion reutilizadas.

```bash
# Subir imagen
curl -X POST "https://zoopa.es/wp-json/wp/v2/media" \
  -u "usuario:app_password" \
  -F "file=@/ruta/imagen.png" \
  -F "alt_text=descripcion"

# Crear post
curl -X POST "https://zoopa.es/wp-json/wp/v2/posts" \
  -u "usuario:app_password" \
  -H "Content-Type: application/json" \
  -d '{"title":"...","content":"...","status":"publish","categories":[ID],"author":ID,"lang":"es","featured_media":ID}'

# Actualizar post
curl -X POST "https://zoopa.es/wp-json/wp/v2/posts/ID" \
  -u "usuario:app_password" \
  -H "Content-Type: application/json" \
  -d '{"content":"..."}'
```

Playwright SOLO se usa para plataformas sin API (LinkedIn, Substack, Threads).

```
POST /wp-json/wp/v2/posts/
Headers: Content-Type: application/json, X-WP-Nonce: wpApiSettings.nonce
Body: {title, content, status: "publish", categories: [...], featured_media: ID, lang: "es|ca|en"}
```

**NUNCA usar el editor visual de Gutenberg para pegar contenido largo.** Usar siempre la API REST o el editor de codigo.

#### 5.2 Contenido en formato Gutenberg blocks

El contenido debe estar en formato de bloques Gutenberg (no Markdown ni HTML plano):

- Parrafos: `<!-- wp:paragraph --><p>...</p><!-- /wp:paragraph -->`
- Headings: `<!-- wp:heading --><h2>...</h2><!-- /wp:heading -->` o con level: `<!-- wp:heading {"level":3} --><h3>...</h3><!-- /wp:heading -->`
- Listas: `<!-- wp:list --><ul>...</ul><!-- /wp:list -->` o `<!-- wp:list {"ordered":true} --><ol>...</ol><!-- /wp:list -->`
- Tablas: `<!-- wp:table --><figure class="wp-block-table"><table>...</table></figure><!-- /wp:table -->`
- Imagenes: `<!-- wp:image --><figure class="wp-block-image"><img src="URL" alt="..."/></figure><!-- /wp:image -->`
- Separadores: `<!-- wp:separator --><hr class="wp-block-separator has-alpha-channel-opacity"/><!-- /wp:separator -->`

#### 5.3 Imagenes

1. **Subir TODAS las imagenes ANTES de crear los posts.** Usar la pagina `/wp-admin/media-new.php` con file upload via Playwright.
2. **Obtener las URLs** de las imagenes subidas via API: `GET /wp-json/wp/v2/media?per_page=N&orderby=date&order=desc`
3. **Reemplazar rutas locales** por URLs de WordPress en el contenido ANTES de publicar.
4. **Imagen destacada**: asignar via `featured_media: ID` en el body del POST, no via el dialogo de WordPress (es poco fiable con Playwright).
5. **Alt text**: configurar al subir la imagen via la API: `POST /wp-json/wp/v2/media/ID` con `{alt_text: "..."}`.

#### 5.4 Categorias por idioma (Polylang) — ACTUALIZADO ABRIL 2026

**CRITICO**: zoopa.es usa Polylang. Las categorias fueron reestructuradas en abril 2026.

**Categorias ES (usar estas):**

| Categoria | ID ES | Slug |
|-----------|-------|------|
| GEO, IA y Visibilidad en Buscadores de IA | 2231 | geo-ia-visibilidad |
| Social Media | 2233 | social-media-es |
| Creatividad y Contenido | 2235 | creatividad-contenido |
| Innovacion y Tecnologia | 2237 | innovacion-tecnologia |
| Estrategia y Marketing Digital | 2239 | estrategia-marketing-digital |
| Branding, UX y Diseno | 2241 | branding-ux-diseno |
| Influencer Marketing | 2243 | influencer-marketing-es |
| Produccion Audiovisual | 2245 | produccion-audiovisual |

**Reglas:**
- **Asignar 1-2 categorias tematicas** por post. NO usar "Blog" ni "Sin categoria" (legacy).
- **Todo post sobre GEO/ChatGPT/LLMs** → obligatorio categoria 2231 (cluster estrategico con CTA automatico a /servicios/georadar/).
- **Verificar IDs EN/CA** antes de asignar traducciones: `GET /wp-json/wp/v2/categories?lang=en`
- **Verificar que el post aparece** en la pagina del blog tras publicar.

#### 5.5 Autor

- Cambiar autor via API: `POST /wp-json/wp/v2/posts/ID` con `{author: AUTHOR_ID}`
- Carlos Ortet: verificar ID con `GET /wp-json/wp/v2/users?search=Carlos`
- Alternativa: usar el dialogo de autor en el editor de WordPress.

#### 5.6 Rank Math SEO

Configurar via la API de Rank Math:

```
POST /wp-json/rankmath/v1/updateMeta
Body: {
  objectID: POST_ID,
  objectType: "post",
  meta: {
    rank_math_title: "...",
    rank_math_description: "...",
    rank_math_focus_keyword: "..."
  }
}
```

Usar los datos del bloque de metadatos HTML del archivo .md generado en PASO 3.5.

#### 5.7 Traducciones (Polylang)

Para vincular posts como traducciones entre idiomas:

```
POST /wp-json/wp/v2/posts/POST_ID
Body: {lang: "ca", translations: {es: ES_POST_ID, ca: CA_POST_ID}}
```

**IMPORTANTE**: Asignar idioma y traducciones en una SOLA operacion. Hacerlo por separado puede vaciar el contenido del post (bug observado en Polylang via API REST).

#### 5.8 Verificacion post-publicacion

Despues de publicar, verificar SIEMPRE:

1. **Contenido**: `GET /wp-json/wp/v2/posts/ID?context=edit` → `content.raw.length > 0`
2. **Imagen destacada**: `featured_media > 0`
3. **Alt text**: verificar que la imagen destacada tiene alt text descriptivo con keywords
4. **Categorias correctas**: 1-2 categorias tematicas de las 8 nuevas (no legacy)
5. **Visibilidad en la pagina del blog**: navegar a la pagina del blog del idioma y confirmar que el post aparece
6. **Traducciones vinculadas**: verificar que `translations` contiene los IDs correctos
7. **OG:image**: verificar que el post tiene imagen para compartir en redes. Si no tiene featured image, asignar una.
8. **Heading hierarchy**: verificar que el post tiene exactamente 1 H1 (titulo) y que no hay saltos de nivel
9. **Meta description**: verificar que tiene ≤155 caracteres y no esta vacia
10. **CTAs presentes**: verificar que el contenido incluye mid-CTA (→ servicio) y final-CTA (→ contacto)

Si alguna verificacion falla, corregir inmediatamente via la API REST antes de continuar.

#### 5.9 Interlinking y clusters (OBLIGATORIO)

Despues de publicar, ejecutar estas acciones de interlinking:

1. **Enlazar a pagina de servicio**: todo post debe enlazar a la pagina de servicio mas relevante de zoopa.es. Servicios disponibles:
   - /es/servicios/georadar/ (GEO)
   - /es/servicios/servicios-geo-visibilidad-en-ia-chatgpt/ (GEO/IA)
   - /es/servicios/marketing-de-influencers/
   - /es/servicios/www-zoopa-com-social-media/
   - /es/servicios/produccion-y-branded-content/
   - /es/servicios/agencia-creativa/
   - /es/servicios/branding-diseno-grafico-identidad-visual/
   - /es/servicios/estrategia/
   - /es/servicios/agencia-paidmedia-performance-marketing/
   - /es/servicios/zoopa-agency-gestion-linkedin/
   - /es/servicios/wikipedia-reputacion-online/
   - /es/servicios/servicios-agencia-reddit/
   - /es/servicios/agencia-pinterest-para-empresas/
   - /es/servicios/diseno-produccion-eventos/

2. **Posts GEO → pillar automatico**: los posts en categoria GEO (2231) reciben automaticamente un CTA a /es/servicios/georadar/ via Snippet #56. No es necesario anadir el link manualmente, pero si es bueno incluir un link contextual inline adicional.

3. **Enlazar a posts relacionados**: buscar 2-3 posts del mismo cluster/categoria y enlazarlos inline en el contenido. Consultar: `GET /wp-json/wp/v2/posts?categories=CAT_ID&per_page=5&exclude=POST_ID`

4. **Publicar en 3 idiomas**: todo post de zoopa.es debe existir en ES, EN y CA con traducciones vinculadas en Polylang. El contenido EN y CA puede ser mas corto pero debe cubrir los puntos clave.

#### 5.10 Registrar publicaciones en metadata.json (OBLIGATORIO)

Despues de cada publicacion exitosa, anadir el registro al `metadata.json` del proyecto. Esto permite analisis transversal posterior (que canales, que rendimiento, que clusters).

```bash
# Blog WordPress
python3 _system/metadata.py add-publication project-XXX \
  --channel blog_es \
  --url https://zoopa.es/blog/slug-del-post \
  --wp-post-id 12345 \
  --categories 2231 \
  --featured-media 9876

# Canal social (LinkedIn, Substack, Medium, Threads, etc.)
python3 _system/metadata.py add-publication project-XXX \
  --channel linkedin_es \
  --url https://linkedin.com/posts/... \
  --account "Carlos Ortet"
```

Hacer una llamada por canal publicado. Si un canal no se llega a publicar (p.ej. Hashnode falla), no registrarlo — solo `published[<canal>]` refleja publicaciones reales.

Ver `_system/metadata-schema.md` para el schema completo y la convencion de keys de canal.

---

### PASO 5.B: Publicacion en el blog estatico de 498advance.com (si aplica)

Cuando el destino sea **498advance.com** (Perspectivas). No hay CMS ni API: son ficheros
`.html` en el repo `498AS/498a-new-web-design`, local en
`/Users/carlos/Documents/claudecode-proj/design system 498A/`.

**Antes de escribir una sola linea, leer `references/blog-498advance-static.md`.**

#### 5.B.1 Reparto de trabajo (no cruzarlo)

| Quien | Que hace |
|---|---|
| El skill | El contenido: `blog498a_<lang>.md` con front matter + markdown restringido |
| `build_498a_post.py` | Lo convierte en el HTML de la plantilla: head, hero, secciones con ancla, componentes, schema, indice lateral |
| `_i18n/blog_build.py` (repo web) | La fontaneria: `lang`, `hreflang` reciproco, `og:locale`, `inLanguage`, navegacion, selector de idioma, etiquetas `data-i18n`, los cuatro listados, el bloque del blog en `sitemap.xml` y los cuatro feeds |
| `deploy.sh` (repo web) | La subida por FTPS y el aviso de purgar Cloudflare |

**Nunca a mano**: los bloques `<!-- 498A:hreflang -->`, `<!-- 498A:nav -->`,
`<!-- 498A:switcher -->` y `<!-- 498A:lista -->`, los listados, el `sitemap.xml` ni los
feeds. `blog_build.py` los reescribe en cada pasada.

#### 5.B.2 Idiomas

Cuatro: **es, ca, en, it**. El blog **no lleva frances** (`/fr/` enlaza al blog en ingles).
El **slug es el mismo en los cuatro idiomas** y los `id` de seccion tambien: solo cambia el
prefijo de ruta (`/blog/`, `/ca/blog/`, `/en/blog/`, `/it/blog/`). No traducir el slug.

Un post no tiene que existir en los cuatro: `blog_build.py` declara solo los que hay y avisa
de los que faltan. Prioridad si no se hacen los cuatro: ES (es el `x-default`), luego EN.

#### 5.B.3 Secuencia

```bash
cd "/Users/carlos/Documents/claudecode-proj/design system 498A"

# 1 · ensayo, sin tocar el repo
python3 ~/.claude/skills/content-factory/scripts/publisher/build_498a_post.py \
  <proyecto>/output/blog498a_es.md --dry-run

# 2 · los cuatro idiomas y el constructor del blog
python3 ~/.claude/skills/content-factory/scripts/publisher/build_498a_post.py \
  <proyecto>/output/blog498a_{es,ca,en,it}.md --build

# 3 · revalidar despues del constructor (el generador ya valida al escribir,
#     pero blog_build.py reescribe la fontaneria de idioma)
python3 ~/.claude/skills/content-factory/scripts/validators/validate_blog_498a.py \
  498Adesign/blog/<slug>.html 498Adesign/en/blog/<slug>.html

# 4 · comprobar que la web queda coherente
python3 _i18n/blog_build.py --check

# 5 · subir y purgar
./deploy.sh --dry-run && ./deploy.sh
```

Lo que sigue siendo manual despues del paso 2:

1. **Imagen social** 1200x630 en `498Adesign/assets/og/<slug>.jpg`. `_i18n/og_build.py` es la
   referencia (Chrome headless sobre una plantilla con las fuentes de marca).
2. **En un estudio: el csv y el json** en `498Adesign/blog/datos/<slug>.csv` y `.json`, con la
   cabecera de metodo de `blog/datos/README.md` y licencia CC BY 4.0.

#### 5.B.4 Enlazado interno

Todo post enlaza a lo que vende 498A, sin forzarlo. **Solo GEORadar tiene pagina propia**
(`/productos/georadar.html`); S.A.M., GEOdoctor, LEO, Prompt Atlas, Stardesk, COMPLY y
HUMANMADE se enlazan al hub `/productos/`. Capacidades a `/#capacidades`, investigacion y
Gerard a `/#investigacion`. Inventarse `/productos/sam.html` es un 404. Tabla completa en
§ 9 de la referencia.

#### 5.B.5 Verificacion post-publicacion

1. `curl -sI https://498advance.com/blog/<slug>.html` devuelve 200, y lo mismo en
   `/ca/blog/`, `/en/blog/` y `/it/blog/` para los idiomas publicados
2. El post aparece en el listado de cada idioma
3. El `hreflang` de cada version declara solo los idiomas que existen
4. El selector de idioma de la cabecera no lleva a ningun 404
5. La imagen social se ve al pegar la URL en LinkedIn o Slack
6. En un estudio: el csv y el json se descargan y el `Dataset` del schema los declara
7. `validate_blog_498a.py` y `blog_build.py --check` sin avisos

#### 5.B.6 Registro en metadata.json

Igual que en 5.A, una llamada por idioma publicado:

```bash
python3 _system/metadata.py add-publication project-XXX \
  --channel blog498a_es \
  --url https://498advance.com/blog/<slug>.html
```

Si el autor es Carlos Ortet, seguir con PASO 6.

---

### PASO 6: Añadir entrada a carlosortet.com (CONDICIONAL — solo si autor = Carlos Ortet)

**OBLIGATORIO** preguntar al usuario despues de la publicacion exitosa de cualquier pieza editorial firmada por Carlos Ortet (blog en zoopa.es / 498advance.com, post en Medium, articulo en Harvard Deusto Business Review, Substack relevante, paper academico, etc.).

**Pregunta exacta:**

> *"He publicado [TITULO] en [PLATAFORMAS]. ¿Añadimos esta publicacion a la lista de carlosortet.com? Va a `src/data/resume.tsx` array `publications`, incluyendo botones a las versiones disponibles (EN/ES/CA + Medium si aplica)."*

**Opciones a ofrecer:**
- Si — commit + push directo a `main` (recomendado, deploy automatico Vercel/Netlify)
- Solo commit local, no push
- Crear branch + PR (si requiere revision previa)
- No, no procede

#### 6.1 Estructura de la entrada (TypeScript)

Insertar como **primer item** del array `publications` (mas reciente primero) en `/Users/carlos/Documents/03_PERSONAL/carlosortet/src/data/resume.tsx`. Formato:

```typescript
{
  title: "<titulo de la pieza, version EN si existe>",
  dates: "<Mes Año en EN>",  // Ej: "May 2026"
  location: "<plataforma principal · plataformas secundarias>",  // Ej: "Medium · zoopa.es (EN, ES, CA)"
  description:
    "<150-300 palabras EN, datos verificables clave, sin pitch comercial>",
  image: "",
  links: [
    {
      title: "Read in English (Zoopa)",
      icon: <Icons.globe className="h-4 w-4" />,
      href: "https://zoopa.es/en/<category-slug>/<post-slug>/",
    },
    {
      title: "Read in Spanish (Zoopa)",
      icon: <Icons.globe className="h-4 w-4" />,
      href: "https://zoopa.es/es/<category-slug>/<post-slug>/",
    },
    {
      title: "Read in Catalan (Zoopa)",
      icon: <Icons.globe className="h-4 w-4" />,
      href: "https://zoopa.es/ca/<category-slug>/<post-slug>/",
    },
    {
      title: "Read on Medium",
      icon: <Icons.globe className="h-4 w-4" />,
      href: "https://medium.com/@carlosortet/<slug>",
    },
  ],
},
```

**Reglas:**
- Incluir solo los `links` que existen realmente (verificar URLs activas antes con `curl -I`).
- Idioma `description`: SIEMPRE en EN (la home del site esta en EN).
- `dates` en formato "May 2026" (en EN).
- Mantener el patron de commits existente: `publications · Add '<titulo corto>' (<plataforma principal> · <fecha>)`.

#### 6.2 Flujo operativo

```bash
# 1. Editar el archivo
# (con Edit tool, insertar como primer item del array publications)

# 2. Verificar el diff
cd /Users/carlos/Documents/03_PERSONAL/carlosortet
git diff src/data/resume.tsx

# 3. Commit con mensaje en patron existente
git add src/data/resume.tsx
git commit -m "publications · Add '<TITULO>' (<PLATAFORMA> · <FECHA>)"

# 4. Push a main (si autorizado)
git push origin main

# 5. Esperar ~60-90s deploy Vercel/Netlify

# 6. Verificar en vivo
curl -s -H "User-Agent: Mozilla/5.0" https://carlosortet.com | grep -oE "<titulo distintivo>" | head -1
```

#### 6.3 Caso de estudio (mayo 2026)

Ejemplo real en commit `8a28b60`: tras publicar "The invisible fabric of AI" (Medium + zoopa.es EN/ES/CA), se añadio entrada con los 4 links. Deploy completado en ~2 min, verificado via grep al HTML de produccion.

---

## Recomendaciones por tipo de producto

| Tipo | Plataformas recomendadas |
|------|--------------------------|
| Thought leadership / Analisis | Blog, LinkedIn, Medium, Substack, HN, Threads |
| Open Source | Reddit, Dev.to, Hashnode, HN, Lobsters, Mastodon |
| SaaS / Commercial | G2, Capterra, Product Hunt, Trustpilot |
| Consumer App | Product Hunt, App Store, Trustpilot, Threads |
| Enterprise | G2, Capterra, Gartner Peer Insights, DZone |
| Web3 / Crypto | Mirror.xyz, Farcaster, Reddit crypto subs |

---

## Referencias

- Ver `references/channel-catalog.md` para la lista maestra de 41 canales con archivos, idiomas y defaults
- Ver `references/blog-498advance-static.md` para el blog estatico de 498advance.com (OBLIGATORIO antes de cualquier `blog498a_*`)
- Ver `references/orthography-rules.md` para las reglas de revision ortografica y de estilo
- Ver `references/lessons-learned.md` para lecciones aprendidas por plataforma
