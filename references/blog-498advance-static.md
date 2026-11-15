# Blog estatico de 498advance.com · referencia obligatoria

> Lectura OBLIGATORIA antes de escribir cualquier output `blog498a_*`, igual que
> `substack-style.md` lo es para Substack. Ultima verificacion: 2026-09-27, contra
> el commit `9473a17` del repo de la web (blog multiidioma).

Cubre **solo** el blog de 498advance.com (Perspectivas). El blog de zoopa.es es
WordPress y se rige por `blog-html-components.md` + `wp_publish.py`. Los dos flujos
son incompatibles: no mezclarlos.

---

## 1 · Los dos blogs no se parecen en nada

| | Blog WordPress (zoopa.es) | Blog 498advance.com (Perspectivas) |
|---|---|---|
| Destino | CMS, REST API | Fichero `.html` estatico en un repo |
| Estilos | `style=""` inline en cada elemento | Clases de `blog.css`, **cero estilos inline** |
| Estructura | Libre, el tema la envuelve | Plantilla fija con `{{MARCADORES}}` |
| Metadatos | Campos de Rank Math | `<head>` + JSON-LD escritos a mano |
| Idiomas | Polylang | Un fichero por idioma, `hreflang` generado |
| Publicar | Un POST a la API | Escribir el `.html` + `blog_build.py` + FTPS |
| Objetivo | SEO | SEO **y** GEO: que un modelo cite una seccion suelta |
| Output del skill | `blog.md`, `blog_en.md`, `blog_ca.md` | `blog498a_es.md` · `_ca` · `_en` · `_it` |

**Prohibido si el destino es 498advance.com:** `blog-html-components.md` (es HTML con
estilos inline para WordPress), `wp_publish.py`, bloque de metadatos Rank Math,
categorias numericas de Polylang, formato Gutenberg.

Estado a 2026-09-27: `498as.com` hace 301 hacia `498advance.com` (el canonico ya es
el nuevo) y **no queda WordPress en ninguno de los dos**: `/wp-json/` da 404.

---

## 2 · Donde vive y quien hace que

Repo: **`498AS/498a-new-web-design`**
Local: `/Users/carlos/Documents/claudecode-proj/design system 498A/`
Raiz publicable: `498Adesign/` (se sube su **contenido**, no la carpeta)

```
498Adesign/
  blog/
    index.html                 listado ES · GENERADO, no editar
    blog.css                   sistema editorial (56 clases)
    _plantilla-estudio.html    estudio con datos · la pieza diferencial
    _plantilla-articulo.html   articulo normal, sin dataset ni metodologia
    datos/                     csv y json de cada estudio
    <slug>.html                los posts en castellano
  ca/blog/ · en/blog/ · it/blog/
    index.html                 listado del idioma · GENERADO, no editar
    <slug>.html                la traduccion del post · MISMO slug
  assets/og/<slug>.jpg         imagen social 1200x630
  assets/blog/<slug>-figN.jpg  figuras del cuerpo
  feed.xml · ca/feed.xml · en/feed.xml · it/feed.xml    GENERADOS
  sitemap.xml                  el bloque del blog, GENERADO
_i18n/
  blog_build.py                el constructor del blog
  blog_i18n.json               cadenas fijas en los cuatro idiomas
```

### El reparto de trabajo, que es lo que hay que tener claro

| Quien | Que hace |
|---|---|
| **El skill** (`blog498a_<lang>.md`) | El contenido: titulo, entradilla, conclusiones, cuerpo, tablas, figuras, metodologia, fuentes, FAQ |
| **`build_498a_post.py`** (skill) | Convierte ese `.md` en el `.html` de la plantilla: head, hero, secciones con ancla, componentes, schema, indice lateral |
| **`_i18n/blog_build.py`** (repo web) | La fontaneria: `lang`, `hreflang` reciproco, `og:locale`, `inLanguage`, navegacion, selector de idioma, etiquetas `data-i18n`, los cuatro listados, el bloque del blog en `sitemap.xml` y los cuatro feeds |
| **`deploy.sh`** (repo web) | La subida por FTPS y el aviso de purgar Cloudflare |

**Nunca a mano:** los bloques `<!-- 498A:hreflang -->`, `<!-- 498A:nav -->`,
`<!-- 498A:switcher -->` y `<!-- 498A:lista -->`, los listados, el sitemap y los
feeds. `blog_build.py` los reescribe en cada pasada: editarlos es trabajo perdido.

### Lectura obligatoria antes de escribir

| Fichero | Para que |
|---|---|
| `498Adesign/blog/README.md` | Linea editorial, idiomas, canonico y los pasos de publicacion |
| `498Adesign/blog/_plantilla-articulo.html` | Plantilla del articulo |
| `498Adesign/blog/_plantilla-estudio.html` | Plantilla del estudio |
| `498Adesign/blog/blog.css` | Las clases disponibles. No se inventan clases nuevas |
| `_i18n/blog_i18n.json` | Las cadenas fijas. Etiqueta nueva = entrada nueva en los cuatro idiomas |
| `_i18n/blog_build.py` | Que reescribe el constructor y que espera de cada post |
| `498Adesign/llms.txt` | Contexto de entidad que ya leen los modelos. Todo post debe ser coherente |
| `498Adesign/productos/georadar.html` | Referencia de tono comercial del producto estrella |
| `~/.claude/CLAUDE.md` | Canon de cifras y de naming |

---

## 3 · Que plantilla toca

| | `_plantilla-articulo.html` | `_plantilla-estudio.html` |
|---|---|---|
| Cuando | Articulo de metodo, nota de producto, ensayo, pieza derivada | Estudio con datos propios de GEORadar |
| Schema | `Article` + `FAQPage` + `BreadcrumbList` | + `Dataset` |
| Bloque `.datos` (cifras) | No | Si, tres cifras |
| `.tabla-datos` | No | Si |
| `.metodologia` | No | **Obligatoria** |
| `.datos-abiertos` + csv/json | No | **Obligatorio** |

Un articulo de metodo que cita datos de un estudio ya publicado enlaza a ese
estudio; no duplica su metodologia.

---

## 4 · Reglas de maquetacion

1. **Cero estilos inline.** Solo clases de `blog.css`. Si algo no se puede montar con
   las clases existentes, se dice; no se inventa un `style=""` ni una clase nueva.
2. **Partir siempre de la plantilla.** Nunca escribir el HTML desde cero.
3. **Cada `<h2>` lleva tres cosas**: `id`, su `<span class="num">NN</span>` y su
   enlace de ancla `<a class="ancla" href="#id" data-i18n-label="post_ancla_aria"
   aria-label="...">#</a>`. Es lo que permite que una persona, o un modelo, cite una
   seccion suelta.
4. **Los `id` de seccion no cambian nunca** una vez publicados, y son **los mismos en
   los cuatro idiomas**. Cambiarlos rompe las citas externas y las anclas indexadas.
5. Esas mismas secciones se dan de alta en el indice lateral (`.post-toc`).
6. **Un solo `<h1>`**, el del `.post-hero__title`.
7. `<time datetime="YYYY-MM-DD">` en toda fecha visible.
8. Toda `<img>` con `alt` descriptivo de verdad.
9. El cuerpo no lleva `<blockquote>`: el destacado es `<aside class="callout">`.
10. **Etiquetas fijas con `data-i18n`.** Toda cadena de interfaz que se repita en los
    cuatro idiomas se marca `data-i18n="clave"` (texto) o `data-i18n-label="clave"`
    (aria-label) con la clave de `blog_i18n.json`, y `blog_build.py` la escribe en
    cada idioma. Una etiqueta propia del autor (un `:::callout` con su rotulo) va sin
    `data-i18n` y se escribe ya en el idioma del fichero.

### Inventario de clases de `blog.css`

No hay mas. Cualquier otra clase es un invento.

**Cabecera y meta**
`.blog` (en `<body>`) · `.blog-wrap` · `.post-hero` · `.post-hero__cat` ·
`.post-hero__title` (+ `em` para la palabra en verde) · `.post-hero__lead` · `.post-meta`

**Estructura**
`.post-grid` · `.post__body` · `.post-takeaways` · `.post-toc` · `.post-toc__title` ·
`.post-toc a.is-current` (lo pone el JS) · `.sr-only`

**Componentes del cuerpo**
`.callout` + `.callout__label` · `.detalle` + `.detalle__cuerpo` ·
`.datos` + `.dato` + `.dato__cifra` (+ `em` para verde) + `.dato__etiqueta` ·
`.tabla-wrap` + `.tabla-datos` (+ `th`, `td.num`, `.destaca`) ·
`.figura` (con `img` + `figcaption`) · `.metodologia` + `.metodologia__cab` +
`.metodologia__cuerpo` (con `dl`/`dt`/`dd`) · `.datos-abiertos` +
`.datos-abiertos__label` · `.fuentes` + `.fuentes__titulo` ·
`.post-autor` + `.post-autor__nombre` + `.post-autor__rol` + `.post-autor__bio`

**Listado** (lo genera `blog_build.py`, no se escribe a mano)
`.blog-head` + `.blog-head__title` + `.blog-head__lead` · `.blog-filtros` ·
`.blog-lista` · `.blog-item` + `.blog-item__fecha` + `.blog-item__cat` +
`.blog-item__title` + `.blog-item__sum` + `.blog-item__fig` · `.blog-vacio`

**Cabecera compartida con la home** (la genera `blog_build.py`)
`.nav` · `.nav__brand-box` · `.nav__links` · `.nav__link-box` (+ `.num`) ·
`.nav__spacer` · `.nav__cta-box` · `.nav__toggle` + `.nav__toggle-bar` ·
`.lang-grid` + `.lang-grid__cell` (+ `.is-active`) · `.btn-light` · `.btn-ghost-light`

**Ojo:** `.post-siguiente` aparece en el comentario de cabecera de `blog.css` pero
**no tiene reglas CSS**. No usarla hasta que exista.

---

## 5 · Estructura obligatoria, en este orden

El orden es el de Ahrefs, no el de un blog al uso: la conclusion va antes del cuerpo.

1. `.post-hero` · categoria, H1, entradilla, meta (fecha, minutos, autor, y en un
   estudio la muestra: "8.600 prompts · 7 superficies").
2. `.post-takeaways` · **conclusiones antes del cuerpo**, con numeros concretos. Es
   lo primero que extrae un modelo. Generalidades aqui = post que no se cita. Tres
   bullets, cada uno con cifra, unidad y referencia temporal.
3. Parrafo de entrada.
4. En un estudio, el bloque `.datos` con tres cifras.
5. Cuerpo en secciones `h2` numeradas (`01`, `02`, `03`...).
6. `<aside class="callout">` con la frase clave, una sola vez.
7. En un estudio, `.tabla-datos` con el set competitivo.
8. `<figure class="figura">` con `alt` descriptivo y `figcaption` con fuente y fecha.
9. `<details class="detalle">` para el detalle tecnico, que no rompe la lectura.
10. En un estudio: `.metodologia` completa y `.datos-abiertos` con el csv y el json.
11. En una pieza derivada, la linea `post_original` enlazando al original.
12. `.fuentes` · lista de fuentes.
13. `.post-autor`.
14. `.post-toc` en la columna lateral, con las secciones mas Metodologia y Fuentes.

---

## 6 · Metadatos y schema

Todo a mano en el `<head>`: no hay CMS que los genere.

- `<title>` (`Titulo · 498A`), `meta description` (<=155 car.), `meta author`,
  `meta robots`, `link rel="canonical"` (ver §7).
- El bloque `<!-- 498A:hreflang -->` vacio: lo rellena `blog_build.py`.
- `link rel="alternate" type="application/rss+xml"` al feed del idioma.
- Open Graph completo (`og:type=article`, title, description, url, site_name,
  locale, image 1200x630) + `article:published_time` + `article:section`.
- Twitter Card `summary_large_image`.
- JSON-LD como **array**: `Article` (con `headline`, `description`, `image`,
  `datePublished`, `dateModified`, `inLanguage`, `articleSection`, `wordCount`,
  `author` como `Person` a carlosortet.com, `publisher` por `@id`,
  `mainEntityOfPage`, `isPartOf` al `Blog` y `citation` con las fuentes),
  `FAQPage` (minimo 2 preguntas), `BreadcrumbList`, y en un estudio `Dataset`
  con `license` CC BY 4.0, `measurementTechnique`, `variableMeasured` y
  `distribution` con el csv y el json.

**`blog_build.py` necesita de cada post**, o no lo puede listar ni meter en el feed:
`og:title` · `meta description` · `article:published_time` · `article:section` ·
`og:image` · `canonical`. El listado usa `og:title` como titular y la
`meta description` como resumen.

---

## 7 · Politica de canonico · preguntar SIEMPRE antes de escribir

### Caso A · pieza derivada de carlosortet.com

El ensayo es de Carlos y su canonico se queda en su web:

```html
<link rel="canonical" href="https://carlosortet.com/blog/SLUG-ORIGINAL">
```

`blog_build.py` respeta cualquier canonico externo y avisa por consola.

Y **no puede ser un copia-pega**. Obligatorio:

- entradilla nueva, escrita para 498A;
- un bloque **"Que hacemos con esto en 498A"** que conecte el tema con el stack
  (GEORadar, S.A.M., GEOdoctor, LEO, lo que toque);
- los enlaces a servicios de §9;
- `.post-autor` con el rol en 498A, no el de la web personal;
- la linea `post_original` enlazando al original (la pone el generador si el front
  matter trae `canonical`).

> Nota tecnica: `rel=canonical` es una senal de Google. GPTBot, ClaudeBot,
> PerplexityBot y CCBot la ignoran en la practica: indexan lo que descargan. Por eso
> la version sindicada si se lee y si se puede citar con la marca 498A al lado,
> mientras Google no reparte autoridad entre dos copias. Eso solo funciona si el
> texto **no** es identico.

### Caso B · pieza nativa de 498A

Estudios con datos propios, notas de producto, articulos de metodo. El canonico es
`https://498advance.com{/lang}/blog/SLUG.html`, que es lo que traen las plantillas.

---

## 8 · Idiomas · cuatro, y el slug es el mismo

El blog se publica en **castellano, catalan, ingles e italiano**. La web tiene ademas
version francesa, pero **el blog no lleva frances**: `/fr/` enlaza al blog en ingles.
Decision de Carlos, 27/09/2026. No generar `blog498a_fr`.

| Idioma | Ruta del post | Listado | Feed |
|---|---|---|---|
| ES | `/blog/<slug>.html` | `/blog/` | `/feed.xml` |
| CA | `/ca/blog/<slug>.html` | `/ca/blog/` | `/ca/feed.xml` |
| EN | `/en/blog/<slug>.html` | `/en/blog/` | `/en/feed.xml` |
| IT | `/it/blog/<slug>.html` | `/it/blog/` | `/it/feed.xml` |

**El slug es el mismo en los cuatro idiomas** y solo cambia el prefijo de ruta. Es a
proposito: con el slug compartido el `hreflang` es mecanico y no hay pares rotos. Se
pierde algo de coincidencia de palabra clave en la URL; a cambio no hay tabla de
equivalencias que se desincronice. **No traducir el slug.**

Los `id` de seccion tambien son los mismos en los cuatro idiomas: solo cambia el
titular visible.

Un post **no tiene que existir en los cuatro idiomas**. Si falta en alguno, ese
idioma no se declara en el `hreflang` ni aparece en el selector, y `blog_build.py`
avisa de que falta. Lo gestiona el constructor a partir de los ficheros que hay en
disco: no hay nada que declarar en el front matter.

Prioridad cuando no se hacen los cuatro: **ES primero** (es el `x-default`), despues
EN, y CA e IT segun el tema. La version EN del blog no sustituye a Medium: Medium
sigue llevando su propio output con canonical al post de 498A.

---

## 9 · Enlazado interno a servicios

Todo post enlaza a lo que 498A vende, sin forzarlo. Mapa de destinos reales:

| Tema del post | Enlazar a |
|---|---|
| Visibilidad en IA, GEO, como te citan los modelos | `/productos/georadar.html` |
| Alineamiento de contenido con prompts reales (S.A.M.) | `/productos/` |
| Crawlers, robots.txt, llms.txt, bloqueos de CDN, indexabilidad (GEOdoctor) | `/productos/` |
| Generacion de contenido multicanal (LEO) | `/productos/` |
| Datasets de prompts por sector (Prompt Atlas) | `/productos/` |
| Reputacion (Stardesk) | `/productos/` |
| EU AI Act, cumplimiento (COMPLY) | `/productos/` |
| Autoria y procedencia de contenido humano (HUMANMADE) | `/productos/` |
| Modelos locales, soberania del dato, Smart Routing Engine | `/#capacidades` |
| Sistemas multiagente | `/#capacidades` |
| Datasets a medida, anotacion experta | `/#capacidades` |
| Investigacion, UAB, IIIA-CSIC, Gerard | `/#investigacion` |

**Solo GEORadar tiene pagina propia.** Los demas productos se enlazan al hub
`/productos/`. Inventarse `/productos/sam.html` es un 404.

En las versiones de idioma el enlace de home lleva prefijo (`/en/#capacidades`), pero
`/productos/` y `/productos/georadar.html` solo existen en castellano: se enlazan sin
prefijo y punto.

---

## 10 · Cifras canonicas · no inventar ninguna

Confirmadas 2026-09-27 y aplicadas en la web en los cinco idiomas.

| Dato | Valor |
|---|---|
| Superficies medidas | **Siete**: ChatGPT · Claude · Gemini · Perplexity · Copilot · Google AI Overviews · Google AI Mode |
| Volumen por estudio | **6.000-30.000** prompts personalizados |
| Profundidad | Conversaciones simuladas, en producción, de hasta **diez interacciones** |
| Estudios entregados | **+150** |
| Marcas | **50+ marcas e instituciones** |
| Prompts simulados | **1M+** acumulados · 540K+/mes |
| Menciones analizadas | **12M+** |
| KPI compuesto | **BIS · Brand Impact Score** (nunca "Business Impact") |
| KPIs universales | BIS · SOV · SBOV · SS · PS |
| Verticales | **Nueve**, con KPIs propietarios cerrados |
| Plazo | **Entrega en 4 semanas** · rango de inversion en 48 h |
| Panel | **Business View**, orientado a venta y conversion |
| Plan | **90 dias** |
| Modulo tecnico | **GEOdoctor** (nunca "GEO_DOCTOR" ni "DOC") |
| Stack GEORadar | Seis modulos: GEOAtlas · motor multi-LLM · GEOdesk · S.A.M. · GEOdoctor · LEO |

Las nueve verticales y sus KPIs propietarios estan en `~/.claude/CLAUDE.md`. El cheat
sheet canonico de KPIs manda sobre cualquier otra fuente.

---

## 10 bis · Método y posicionamiento nuevos (noviembre de 2026)

Cuatro capacidades que ya se pueden nombrar en el contenido. Salen del método de GEORadar
y ninguna lleva cifras propias, así que no se inventa ninguna.

| Tema | Qué se puede decir | Qué no se dice |
|---|---|---|
| **Conversaciones simuladas** | Están en producción. Un agente que lleva el perfil sintético del usuario genera cada pregunta a partir de la respuesta anterior de la IA, y un agente vigilante decide cuándo termina la conversación, con un tope de diez iteraciones. Complementan el estudio por cobertura y muestran cómo cambia la recomendación de una marca cuando el usuario concreta, compara o plantea objeciones | Que somos los únicos que lo hacen. Tampoco se citan KPIs de conversación con nombre propio: no hay canon publicado |
| **Límite ético** | 498 Advance no acepta encargos para tapar información cierta, evitar que la IA diga algo verdadero ni difundir información falsa. El reposicionamiento se hace a favor de la transparencia y del derecho a estar informado | Qué encargos se han rechazado ni quién los pidió |
| **Partidos medidos como marcas** | El mismo marco de marcas e instituciones se aplica a partidos y candidatos: cuota de voz de marca (SBOV), posición (PS), sentimiento (SS) y atributos asociados, exactitud de las afirmaciones, aceptación o corrección de las premisas de la pregunta, y variación por perfil y por fuente | Resultados, perfiles, calendario o modelos de un estudio electoral concreto antes de que se publique |
| **Decision triggers** | Grupos de KPIs nuevos: los temas, argumentos o fuentes que hacen que la IA pase de informar a recomendar. *Purchase triggers* en consumo, *affiliation triggers* en entornos institucionales y *vote triggers* en política. Se buscan en el turno de la conversación simulada en que cambia el tono | Acrónimo, fórmula, umbrales o valores numéricos: todavía no existen |

---

## 11 · Categorias

Cuatro, y no hay mas. Van en `article:section`, en `articleSection` del schema y en
`.post-hero__cat`.

**Se escriben SIEMPRE en castellano**, tambien en el fichero catalan, ingles o
italiano. Son la clave canonica: el generador marca el hero con
`data-i18n="cat_<categoria>"` y `blog_build.py` la traduce ahi y en el listado con
`blog_i18n.json`. Una categoria fuera de las cuatro hace fallar el build.

| Categoria | Clave i18n | Filtro | Cuando |
|---|---|---|---|
| Estudio | `cat_estudio` | `?c=estudio` | Datos propios, metodologia completa, csv y json |
| Método | `cat_metodo` | `?c=metodo` | Como se mide un KPI, por que un vertical necesita los suyos |
| Producto | `cat_producto` | `?c=producto` | Nota de lanzamiento. Al lanzar, no un mes despues |
| Investigación | `cat_investigacion` | `?c=investigacion` | Papers, UAB, IIIA-CSIC, Gerard |

Calendario de referencia (de `blog/README.md`): un estudio al trimestre, un articulo
de metodo al mes, notas de producto cuando toque.

---

## 12 · Que hace esto GEO y no solo SEO

- La cifra arriba, con unidad y fecha en la misma frase.
- Metodologia visible: sin metodo un dato no se cita; con metodo se convierte en fuente.
- El dato crudo descargable, para que un agente pueda comprobarte sin parsear HTML.
- Licencia explicita (CC BY 4.0) que le dice a un modelo que puede citarte y como.
- Anclas por seccion, para citar un fragmento y no la pagina entera.
- `citation` en el `Article`, enlazando a las fuentes.
- Sin muros: ni banner encima, ni scroll infinito, ni texto detras de JavaScript.
- Fechas en `<time datetime>`, para que la frescura sea legible sin interpretar.

---

## 13 · Formato del output del skill · `blog498a_<lang>.md`

El skill **no** escribe HTML a mano: escribe un `.md` con front matter y un cuerpo en
markdown restringido, y `build_498a_post.py` lo convierte en el HTML de la plantilla.
Un fichero por idioma, **con el mismo `slug` en los cuatro**.

```markdown
---
tipo: estudio            # estudio | articulo
slug: como-nos-citan-los-modelos-2026    # el mismo en los cuatro idiomas
lang: es                 # es | ca | en | it
titulo: "Titulo para el <title> y para og:title, sin el sufijo 498A"
titulo_h1: "Titular del <h1>, con *una palabra* en verde"
descripcion: "Meta description, maximo 155 caracteres. Es el resumen del listado."
entradilla: "Dos frases que digan el hallazgo, no el tema."
categoria: Estudio       # SIEMPRE en castellano: Estudio | Método | Producto | Investigación
fecha: 2026-10-14
autor: Carlos Ortet
rol_autor: "Cofundador y CEO de 498 Advance"
bio_autor: "Una o dos frases."
muestra: "8.600 prompts · 7 superficies"       # solo estudio
canonical: https://carlosortet.com/blog/slug   # solo Caso A (pieza derivada)
og_image: /assets/og/slug.jpg                  # opcional, se deduce del slug
conclusiones:
  - "Primera conclusion con cifra, unidad y fecha."
  - "Segunda."
  - "Tercera."
cifras:                                        # solo estudio · exactamente 3
  - ["19,13 %", "SOV medio de la marca lider"]
  - ["+0,77", "sentimiento agregado"]
  - ["7", "superficies medidas"]
fuentes:
  - "Nombre de la fuente. Publicacion, fecha. https://..."
faq:
  - pregunta: "Pregunta real que responde el post"
    respuesta: "Respuesta en una o dos frases, autocontenida."
  - pregunta: "..."
    respuesta: "..."
metodo:                                        # solo estudio · todos los campos
  prompts: "8.600"
  motores: "ChatGPT, Claude, Gemini, Perplexity, Copilot, AI Overviews, AI Mode"
  periodo: "Del 1 al 21 de septiembre de 2026"
  mercados: "Espana, Italia, Reino Unido"
  marcas: "24"
  kpis: "BIS, SOV, SBOV, SS, PS y los seis propietarios de Travel"
  limitaciones: "Que no cubre el estudio y por que."
dataset:                                       # solo estudio
  descripcion: "Que hay en el csv y en el json."
  kpis: ["SOV", "Sentiment Score"]
---

Parrafo de entrada.

## Titular de la primera seccion

Texto. Admite **negrita**, *cursiva*, `codigo`, [enlaces](/productos/georadar.html),
listas con `-` y listas numeradas.

:::callout Lo que importa
La frase clave del post, 15-25 palabras, autocontenida.
:::

## Titular de la segunda seccion

| Marca | SOV | Sentimiento | Posicion |
|---|---:|---:|---:|
| **Marca lider** | 19,13 % | +0,77 | 1 |
: Pie de la tabla

![Alt descriptivo de verdad, que se entienda sin ver la imagen](/assets/blog/slug-fig1.jpg)
: Pie de la figura · Fuente: GEORadar, octubre de 2026

:::detalle Detalle tecnico · como se calcula
El detalle que no debe romper la lectura.
:::

## Titular de la tercera seccion

Texto.
```

Conversion que hace el generador:

| Markdown | HTML 498A |
|---|---|
| `## Titular` | `h2` con `id="seccion-N"`, `<span class="num">0N</span>`, `.ancla` con `data-i18n-label`, y entrada en el `.post-toc` |
| `## Titular {#mi-id}` | Igual, con el `id` indicado. Obligatorio para que los cuatro idiomas compartan `id` si el orden cambia |
| `### Sub` | `h3` |
| `:::callout` sin rotulo | `<aside class="callout">` con la etiqueta del sistema (`data-i18n="post_callout"`) |
| `:::callout Rotulo propio` | Igual, con el rotulo del autor y sin `data-i18n` |
| `:::detalle [Resumen]` | `<details class="detalle">` + `.detalle__cuerpo` |
| Tabla + linea `: pie` | `.tabla-wrap` > `table.tabla-datos` con `<caption>`. Columnas alineadas a la derecha en el markdown salen con `td.num`; primera celda en `**negrita**` sale con `.destaca` |
| `![alt](src)` + linea `: pie` | `<figure class="figura">` con `figcaption` |
| `cifras:` del front matter | Bloque `.datos` con tres `.dato` |
| `metodo:` | `.metodologia` con su `dl` y sus `dt` marcados con `data-i18n` |
| `dataset:` | `.datos-abiertos` + el `Dataset` del JSON-LD |
| `categoria:` | `article:section` + `articleSection` + `.post-hero__cat` con su `data-i18n` |
| `canonical:` externo | La linea `post_original` al final del cuerpo |

Un `>` de cita, una clase inventada o un `style=` en el markdown hacen fallar el build.

---

### Ejemplo trabajado

`examples/blog498a_es-pieza-derivada.md` es un `blog498a_es.md` completo y validado: una
pieza **derivada** de carlosortet.com (canonico externo, entradilla nueva, bloque "que
hacemos con esto en 498A"), con tabla, callout, figura, `:::detalle`, tres conclusiones con
cifra, cuatro fuentes y tres preguntas de FAQ. Sirve de plantilla de front matter y de
muestra del dialecto de markdown. Genera un HTML que pasa el validador sin avisos.

---

## 14 · Generar, construir y validar

```bash
# 1 · el HTML de cada idioma (ensayo, sin tocar el repo)
python3 ~/.claude/skills/content-factory/scripts/publisher/build_498a_post.py \
  project_XXX/output/blog498a_es.md --dry-run

# 2 · de verdad, los cuatro idiomas, y despues el constructor del blog
python3 ~/.claude/skills/content-factory/scripts/publisher/build_498a_post.py \
  project_XXX/output/blog498a_{es,ca,en,it}.md --build

# 3 · validar el HTML generado
python3 ~/.claude/skills/content-factory/scripts/validators/validate_blog_498a.py \
  "/Users/carlos/Documents/claudecode-proj/design system 498A/498Adesign/blog/slug.html"

# 4 · comprobar que la web queda coherente (no escribe)
cd "/Users/carlos/Documents/claudecode-proj/design system 498A" && \
  python3 _i18n/blog_build.py --check
```

Flags del generador: `--dry-run` (escribe en /tmp) · `--build` (ejecuta
`_i18n/blog_build.py` al terminar) · `--repo RUTA` · `--out DIR` · `--no-validate`.

**El generador pasa el validador por su cuenta** sobre cada HTML que escribe y sale con
codigo 1 si hay avisos, asi que no se puede generar un post sin comprobarlo. El paso 3 de
arriba sirve para volver a validar despues de `blog_build.py`, que reescribe la fontaneria.

El validador comprueba: marcadores `{{...}}` sin rellenar, `style=` en el cuerpo,
clases que no existen en `blog.css`, `h2` sin `id`/`.num`/`.ancla` o ausente del
`.post-toc`, un solo `h1`, JSON-LD que parsea con `Article` + `FAQPage` +
`BreadcrumbList` (+ `Dataset` si es estudio), coherencia entre `canonical`, `og:url`
y `mainEntityOfPage`, `alt` vacios, conclusiones sin cifra, em-dash, cifras que
contradicen §10, categoria fuera de las cuatro, claves `data-i18n` que no existen en
`blog_i18n.json`, los marcadores `498A:*` que necesita el constructor, el feed del
idioma y enlaces internos o imagenes que no existen en el repo.

---

## 15 · Publicar

1. `build_498a_post.py` para cada idioma (escribe `blog/<slug>.html` y
   `<lang>/blog/<slug>.html`).
2. **Imagen social** 1200x630 en `assets/og/<slug>.jpg`. `_i18n/og_build.py` es la
   referencia: Chrome headless sobre una plantilla HTML con las fuentes de marca.
3. **En un estudio: el csv y el json** en `blog/datos/<slug>.csv` y `.json`, con la
   cabecera de metodo que describe `blog/datos/README.md` y licencia CC BY 4.0.
4. `python3 _i18n/blog_build.py` · listados, sitemap, feeds y hreflang de una vez.
5. `validate_blog_498a.py` sobre cada `.html` (el generador ya lo pasa al escribirlos;
   aqui se repite porque `blog_build.py` ha reescrito la fontaneria) y `blog_build.py --check`.
6. `./deploy.sh` y purgar Cloudflare.

Listados, sitemap y feeds ya no son pasos manuales: los hace el paso 4. Lo que sigue
siendo manual es la imagen social y, en un estudio, los datos abiertos.

---

## 16 · Deploy

Web estatica. No hay build ni backend: se sube por FTPS.

```bash
cd "/Users/carlos/Documents/claudecode-proj/design system 498A"
./deploy.sh --dry-run     # ensena que subiria
./deploy.sh               # sube (lftp pide la contrasena por teclado)
```

- Origen: Dinahosting, con Cloudflare por delante. El host concreto esta en
  `deploy.sh`, dentro del repo de la web; no se escribe aqui porque esta referencia
  viaja a un repo publico y nombrar el origen permite saltarse Cloudflare.
- Se sube **el contenido** de `498Adesign/`, no la carpeta.
- El script ya excluye `*.md`, `_plantilla-*.html`, `playground.html`,
  `showcase.html`, `design-system.html`.
- La primera publicacion tiene que subir tambien `blog/index.html`,
  `blog/blog.css`, los tres listados de idioma, los cuatro feeds y el
  `sitemap.xml` con el bloque del blog ya generado.
- Despues de subir, **purgar Cloudflare** (Caching > Purge Everything).
- Comprobar: `curl -sI https://498advance.com/blog/<slug>.html` (200), lo mismo en
  `/en/blog/`, y que el post aparece en el listado de cada idioma.

**No subir:** `blog/_plantilla-*.html`, `blog/README.md`, ningun `.md`, `_i18n/`.

---

## 17 · Checklist antes de dar por cerrado un post

- [ ] Plantilla correcta (estudio vs articulo) y ningun `{{MARCADOR}}` sin rellenar
- [ ] Cero `style=` en el cuerpo y ninguna clase fuera de `blog.css`
- [ ] Un solo `h1`; cada `h2` con `id`, `.num` y `.ancla`, y presente en el `.post-toc`
- [ ] Los `id` de seccion coinciden en los cuatro idiomas
- [ ] Mismo `slug` en los cuatro idiomas
- [ ] `.post-takeaways` con tres conclusiones que llevan cifra, unidad y fecha
- [ ] `.callout` una sola vez, con la frase clave autocontenida
- [ ] En estudio: `.datos`, `.tabla-datos`, `.metodologia` completa, `.datos-abiertos`,
      y el csv y el json publicados en `blog/datos/`
- [ ] Toda `<img>` con `alt` descriptivo; `figcaption` con fuente y fecha
- [ ] `<head>`: title, description <=155, canonical segun §7, OG + Twitter completos,
      `article:published_time` y `article:section` presentes, feed del idioma
- [ ] Los tres marcadores `498A:*` intactos y vacios
- [ ] JSON-LD parsea: `Article` + `FAQPage` + `BreadcrumbList` (+ `Dataset` en estudio)
- [ ] Minimo dos preguntas en el `FAQPage`, reales y respondidas en el post
- [ ] Categoria entre las cuatro de §11
- [ ] Enlace a servicio segun §9, y ninguna URL inventada (`curl -I` a las externas)
- [ ] Cifras coherentes con §10
- [ ] Si es pieza derivada: canonical a carlosortet.com, entradilla nueva, bloque
      "Que hacemos con esto en 498A", linea `post_original`, y el texto **no** es
      identico al original
- [ ] Sin em-dash (`—`), sin referencias temporales relativas, sin frases formulaicas
      de IA (`orthography-rules.md` §3)
- [ ] `blog_build.py` ejecutado · `validate_blog_498a.py` y `--check` sin avisos
- [ ] Imagen social 1200x630 generada

---

## 18 · Anti-patrones

| No | Por que |
|---|---|
| HTML con `style=""` inline | Es el patron de WordPress. Rompe el design system |
| Clases inventadas (`.post-siguiente`, `.grid-2`) | No existen en `blog.css`: se renderiza sin estilo |
| `<blockquote>` para el destacado | El destacado es `.callout` |
| Editar a mano los bloques `498A:*`, los listados, el sitemap o los feeds | `blog_build.py` los reescribe: es trabajo perdido |
| Traducir el slug | El slug es el mismo en los cuatro idiomas, por diseno |
| Cambiar un `id` de seccion ya publicado | Rompe las citas externas |
| `id` distintos por idioma | Rompe la equivalencia entre versiones |
| Generar `blog498a_fr` | El blog no lleva frances: `/fr/` va al blog en ingles |
| Conclusiones cualitativas en `.post-takeaways` | Sin cifra no hay cita. Es el bloque que lee el modelo |
| Estudio sin metodologia | Un dato sin metodo no se convierte en fuente |
| Copia-pega de carlosortet.com | Para un modelo son dos copias: acaba citando una |
| Categoria fuera de las cuatro | El listado la deja sin traducir |
| Etiqueta fija nueva sin entrada en `blog_i18n.json` | `blog_build.py` la marca como problema |
| Inventar `/productos/sam.html` | Solo GEORadar tiene pagina propia |
| Cifras aproximadas o de memoria | La tabla de §10 es la unica fuente |
