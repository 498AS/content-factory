# Humanize Text — Anti-AI Detection Guide

> Cómo escribir texto que pase los clasificadores GenAI activos en plataformas como
> Hacker News, Quora, Reddit, Turnitin, GPTZero, Originality.ai, Pangram.
>
> Versión: 1.0 · 24 mayo 2026 · Validada con respuesta oficial de dang (HN admin)

---

## El paradigma de 2026 (resumen ejecutivo)

> *"You should not worry about mistakes in grammar, spelling, etc. because these
>  are rapidly becoming signs of authenticity!"* — Daniel Gackle (dang), HN admin,
>  24 mayo 2026

Tres verdades operativas que invierten 25 años de copywriting profesional:

1. **Los detectores AI funcionan** — y los humanizers automáticos (que prometen "bypass") **no funcionan** contra los mejores detectores. GPTZero detecta correctamente los outputs de los principales humanizers comerciales (AI2Human, BypassAI, Undetectable.ai). La única humanización real es la escritura humana real.

2. **Grammarly también delata** — incluso herramientas legítimas como Grammarly dejan "AI imprints" detectables por clasificadores entrenados sobre estilometría. No es solo ChatGPT/Claude.

3. **Los errores ahora son una feature, no un bug** — typos genuinos, conjugaciones imperfectas, sintaxis no-native pasan de "vergonzoso" a "authenticity marker". Las plataformas como HN tienen política explícita pro-ESL (English as Second Language).

---

## Cómo funcionan los detectores (qué miden realmente)

Los clasificadores GenAI actuales (2026) miden tres dimensiones principales:

### 1. Perplexity (predictibilidad léxica)

Mide cuán "esperable" es cada palabra dada la anterior. Los LLMs tienden a generar texto con perplexity baja (palabras predecibles), porque su entrenamiento optimiza la probabilidad de la siguiente palabra. Los humanos rompen las expectativas más a menudo.

**Markers de perplexity alta (humano)**: palabras inesperadas, jerga local, referencias culturales específicas, neologismos personales, lapsus, expresiones idiomáticas regionales.

**Markers de perplexity baja (LLM)**: vocabulario estándar, sinónimos "literarios" ("delve", "leverage", "navigate", "unlock"), construcciones formulaicas.

### 2. Burstiness (asimetría rítmica)

Mide la variación de longitud y complejidad entre frases consecutivas. Los humanos escribimos con ráfagas: frases muy cortas seguidas de párrafos largos, sentencias incompletas mezcladas con prosa estructurada. Los LLMs tienden a uniformidad: párrafos de longitud similar, sentencias de complejidad parecida.

**Markers de burstiness alta (humano)**: frases de 3 palabras junto a párrafos de 80. Cortes abruptos. Fragmentos. Listas mezcladas con prosa irregular.

**Markers de burstiness baja (LLM)**: párrafos uniformes (4-6 frases cada uno), sentencias de longitud similar, listas all-bullets cuando hay listas.

### 3. Stylometric features (firma estilística)

Análisis de patrones lingüísticos profundos:
- Frecuencia de bigramas de part-of-speech
- Distribución de signos de puntuación
- Uso de em-dashes
- Conectores transicionales
- Densidad informacional por párrafo
- Estructura "set-up → bullets → wrap-up" (típica de outputs LLM)

---

## Anti-patterns: what to avoid at all costs (English reference tables)

> Quick-lookup tables in English. Source of truth synchronized with the public one-pager at
> [carlosortet.com/humanize-ai-text](https://carlosortet.com/humanize-ai-text).
> Use these when working on EN content (HN, Quora, Reddit, Medium, LinkedIn EN, X EN, etc.).

### Lexical (words that betray)

| CATEGORY | EXAMPLES | WHY IT BETRAYS |
|---|---|---|
| Pretentious verbs | delve, leverage, navigate, unlock, harness, foster, embark, illuminate, underscore | Overused by ChatGPT/Claude. Almost never in spontaneous human writing. |
| Empty adjectives | groundbreaking, revolutionary, cutting-edge, seamless, robust, comprehensive, multifaceted | Modifiers without concrete information. |
| Formulaic adverbs | crucially, importantly, notably, significantly, ultimately | Connectors LLMs use to signal transitions. |
| Abstract nouns | transparency, intelligence (noun), efficiency, optimization, alignment | LLMs abstract when humans would use examples. |

### Structural (forms that betray)

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

### Auto-scan grep patterns (bash)

Para PASO 3.7 del flujo, ejecutar contra cada output antes de marcarlo como listo:

```bash
# Lexical flags
grep -iEn "\b(delve|leverage|navigate|unlock|harness|foster|embark|illuminate|underscore)\b" output/<file>
grep -iEn "\b(groundbreaking|revolutionary|cutting-edge|seamless|robust|comprehensive|multifaceted)\b" output/<file>
grep -iEn "\b(crucially|importantly|notably|significantly|ultimately)\b" output/<file>
grep -iEn "\b(transparency|efficiency|optimization|alignment)\b" output/<file>

# Structural flags
grep -nE "—" output/<file>                            # em-dashes (count > 1 = rewrite)
grep -nE "→" output/<file>                            # arrows in lists
grep -nE "^(In short|Ultimately|The conclusion):" output/<file>
grep -iEn "\b(furthermore|moreover|additionally|subsequently)\b" output/<file>
grep -iEn "(read the full|subscribe|learn more)" output/<file>
```

Si cualquiera devuelve matches relevantes, aplicar reescritura humana antes de publicar.

---

## Anti-patrones LLM (qué EVITAR a toda costa) · versión castellana extendida

### Léxicos (palabras que delatan)

| Categoría | Ejemplos | Por qué delata |
|---|---|---|
| Verbos pretenciosos | delve, leverage, navigate, unlock, harness, foster, embark, illuminate, underscore | Sobreusados por ChatGPT/Claude. Casi nunca aparecen en escritura humana espontánea. |
| Adjetivos vacíos | groundbreaking, revolutionary, cutting-edge, seamless, robust, comprehensive, multifaceted | Modificadores sin información concreta. |
| Adverbios formulaicos | crucially, importantly, notably, significantly, ultimately | Conectores que LLMs usan para señalar transiciones. |
| Sustantivos abstractos | transparency, intelligence (como noun), efficiency, optimization, alignment | LLMs tienden a abstraer cuando humanos usarían ejemplos. |

### Estructurales (formas que delatan)

| Patrón | Por qué delata |
|---|---|
| **Rule of three** ("X, Y, and Z" con tres elementos paralelos) | Patrón retórico clásico sobreusado. Real life solo tiene 3 cosas paralelas a veces. |
| **Em-dashes para incisos** (—) | LLMs los usan en exceso. Humanos usan más comas, paréntesis, o frases nuevas. |
| **"No es X, es Y"** (negación-afirmación) | Estructura punchline LLM, casi nunca natural. |
| **"La conclusión:" / "In short:" / "Ultimately:"** | Cierres formulaicos. Humanos no señalizan conclusiones así. |
| **Flechas → en listas** | Casi exclusivo de LLMs. Humanos usan bullets simples o guiones. |
| **Listas all-bullets** | Cuando un humano escribe sobre algo complejo, mezcla prosa y bullets. LLMs van todo-bullets. |
| **Párrafos uniformes** (4-6 frases cada uno) | Burstiness baja. Humanos varían: párrafos de 1 frase junto a párrafos de 12. |
| **Conectores formales** ("Furthermore", "Moreover", "Additionally", "Subsequently") | Formales casi exclusivamente en escritura académica humana. En redes sociales / comments delatan. |
| **CTA al final** ("read the full article", "subscribe", "learn more") | Marketing-speak detectable. |

### Temporales (timing que delata)

- **Tiempos verbales perfectos consistentes** — LLMs raramente cambian de tiempo abruptamente
- **Sin cambios de registro** — humanos pasan de formal a coloquial dentro del mismo párrafo
- **Sin auto-correcciones** — humanos a veces escriben "X — wait, actually Y"
- **Sin sentencias incompletas** — humanos las dejan a propósito para énfasis

---

## Patrones humanos (qué INCLUIR a propósito)

### Léxicos

- **Contracciones** ("don't" en vez de "do not", "it's" en vez de "it is")
- **Conectores orales** ("So,", "Look,", "Here's the thing —", "Now,", "I mean,")
- **Modalizadores tentativos** ("kind of", "sort of", "I think", "probably", "in my view")
- **Vocabulario regional** o cultural específico
- **Referencias personales** ("when I visited X", "a client told me last month")
- **Cifras inexactas pero honestas** ("around 50 million", "roughly 30%", "I don't have the exact figure but...")

### Estructurales

- **Ritmo asimétrico** — alterna párrafos de 1 frase con párrafos de 12
- **Sentencias incompletas** para énfasis ("Like really. Really really.")
- **Auto-correcciones visibles** ("X — wait, more accurately Y")
- **Preguntas retóricas** ("Why does this matter? Because...")
- **Conectores hablados** en vez de formales
- **Paréntesis** y guiones en vez de em-dashes
- **Mezcla de prosa y listas** sin patrón fijo

### Temporales y emocionales

- **Cambios de tiempo verbal** ("Last year we built X. Today we're seeing...")
- **Cambios de registro** dentro del mismo párrafo (formal → coloquial)
- **Expresiones de duda o opinión personal** ("I'm not 100% sure about this but...")
- **Anécdotas específicas** (con fecha, lugar, persona si es posible)
- **Reconocimiento de error** ("I was wrong about this before, here's what I now think")

### Errores aceptables (no corregir)

⚠️ Inversión clave: en 2026, **estos errores son markers positivos**:

- **Typos genuinos ocasionales** ("infomration", "replaying" en vez de "replying")
- **Lowercase incorrecta** ("english" en vez de "English" si eres ESL)
- **Sintaxis no-native** ("I came out with a POV" si traduces directamente de tu lengua)
- **Idiom shifts** ("rule of dumb" en vez de "rule of thumb" — los detectores no penalizan esto)
- **Concordancia imperfecta** (singular/plural) en ESL writers

**No corregir todos los errores**. Acepta 1-2 typos por párrafo. Esto es contraintuitivo pero validado por dang.

---

## Workflow: research-assist vs writing-assist

La distinción crítica para usar LLMs sin que delaten:

### ✅ Research-assist (LLM permitido)

El LLM aporta investigación, datos, fuentes verificables. El humano escribe el texto.

```
INPUT del usuario: "Necesito escribir un comentario en HN sobre el coste de los chips"

OUTPUT del LLM (research-assist):
- 10-15 bullets con cifras verificadas + URL fuente
- Cronología de eventos con fechas
- Lista de actores clave
- Referencias citables
- Anti-patterns documentados para la plataforma

OUTPUT que el humano escribe (writing-assist NO usado):
- Comentario completo en su voz, su inglés, sus errores
- Usando los datos del bullet point como referencias
- Tono conversacional, primera persona
- Sin ningún polish posterior con Grammarly
```

### 🚫 Writing-assist (LLM prohibido para HN/Quora/Turnitin/etc.)

El LLM redacta el texto, el humano lo edita o publica. **No funciona**: incluso edición fuerte deja patrones detectables.

### 🟡 Edición humana fuerte de draft LLM (mid-risk)

El LLM redacta, el humano reescribe ≥50% del texto manualmente. Funciona para plataformas con detección débil (LinkedIn, Substack, Medium) pero falla en HN/Quora/Turnitin.

---

## Tabla cross-platform de severidad de detección

| Plataforma | Detección | Política recomendada |
|---|---|---|
| **Hacker News** | 🔴 Clasificador activo confirmado por admin (24 may 2026) | Research-assist only. 100% manual writing. Sin Grammarly. |
| **Turnitin** | 🔴 Detector v4 con stylometry avanzada | 100% manual writing. Académico estricto. |
| **GPTZero** | 🔴 Detector profesional, ajusta contra humanizers conocidos | 100% manual writing si crítico. |
| **Originality.ai** | 🔴 Detector profesional, optimizado para SEO content | Research-assist + edit fuerte ≥70% manual |
| **Quora** | 🟡 Detección emergente, no oficialmente confirmada | Edit manual fuerte ≥30% prose reescrita. Sin Grammarly. |
| **Reddit r/programming, r/MachineLearning** | 🟡 Audiencia detecta + moderadores agresivos | 100% manual o research-assist |
| **Reddit r/europe, r/news** | 🟢 Sin detección sistemática | Edit ligero OK |
| **LinkedIn** | 🟢 Algoritmo no penaliza, pero audiencia técnica detecta | Skill drafts OK con voz personal aplicada |
| **Substack** | 🟢 Sin detección plataforma | Skill drafts OK + pasada final humana |
| **Medium** | 🟢 Sin detección plataforma | Import desde blog OK |
| **X / Bluesky / Threads** | 🟢 Sin detección plataforma | Skill drafts OK con voz personal aplicada |
| **WhatsApp / Telegram** | 🟢 N/A | Skill drafts OK |
| **Discord** | 🟢 N/A | Skill drafts OK |

---

## Checklist práctico: ¿este texto sonará a IA?

Antes de publicar, verifica:

### Léxico
- [ ] ¿Hay verbos pretenciosos? (delve, leverage, navigate, unlock, harness, foster)
- [ ] ¿Hay adjetivos vacíos? (groundbreaking, revolutionary, cutting-edge, robust)
- [ ] ¿Hay adverbios formulaicos? (crucially, importantly, notably, significantly)
- [ ] ¿Hay sustantivos abstractos sin ejemplos? (transparency, optimization, alignment)
- [ ] ¿Hay contracciones? (don't, it's, we're) — debería haber varias
- [ ] ¿Hay conectores orales? (So, Look, Here's the thing) — debería haber al menos 1-2

### Estructura
- [ ] ¿Hay alguna estructura "rule of three" (X, Y, and Z)?
- [ ] ¿Hay em-dashes para incisos? — limita a 1 máximo
- [ ] ¿Hay alguna estructura "no es X, es Y"?
- [ ] ¿Hay un cierre tipo "In short:" / "La conclusión:" / "Ultimately:"?
- [ ] ¿Hay flechas → en listas?
- [ ] ¿Los párrafos tienen longitud uniforme (4-6 frases cada uno)?
- [ ] ¿Las listas son all-bullets, sin prosa mezclada?
- [ ] ¿Hay conectores formales? (Furthermore, Moreover, Additionally)
- [ ] ¿Hay CTA al final? (read the full, subscribe, learn more)

### Burstiness y autenticidad
- [ ] ¿Hay al menos 1 sentencia incompleta o muy corta?
- [ ] ¿Hay variación clara de longitud entre párrafos?
- [ ] ¿Hay alguna anécdota específica con fecha o nombre?
- [ ] ¿Hay alguna referencia personal ("when I", "in my experience")?
- [ ] ¿Hay alguna cifra inexacta o tentativa ("around", "roughly", "about")?
- [ ] ¿Hay al menos un cambio de registro o tiempo verbal?
- [ ] ¿Hay 1-2 typos o errores menores aceptables?
- [ ] ¿Si eres ESL, hay alguna sintaxis no-native que has dejado?

### Si tu texto NO pasa al menos 6 de 8 en la sección "Burstiness y autenticidad", reescribe.

---

## Casos reales validados

### Caso 1 · HN flag por GenAI (24 may 2026)

- **Plataforma**: Hacker News
- **Contenido**: comentario OP con 7 EU chip startups, bullets, cifras
- **Generación**: drafted por Claude, editado con anti-LLM rules superficiales
- **Resultado**: flagged invisible al autor logueado, oculto a anónimos
- **Email a admin** (dang): admisión transparente del uso LLM + propuesta reescritura manual
- **Respuesta de dang**: confirmó clasificador GenAI activo, autorizó reescritura, validó "errors = authenticity"
- **Lección**: cualquier asistencia LLM (incluyendo Grammarly) en HN es detectada

### Caso 2 · LinkedIn personal con voz Carlos Ortet (validado)

- **Plataforma**: LinkedIn cuenta personal
- **Contenido**: post 450 palabras con hook coloquial, conectores hablados, auto-ironía
- **Generación**: skill drafted con `linkedin-voice-carlos-ortet.md` aplicado
- **Resultado**: post publicado sin flag, engagement orgánico normal
- **Lección**: LinkedIn no tiene detector activo. Skill drafts con voz personal pasan.

### Caso 3 · Substack ES con stylebook propio (validado)

- **Plataforma**: Substack newsletter
- **Contenido**: 2.700 palabras editorial
- **Generación**: skill drafted con `substack-style.md` aplicado
- **Resultado**: publicado, sin issues de detección
- **Lección**: Substack sin detección plataforma. Skill drafts OK.

---

## Política para Authority Boost (AB90) — pivotes

Como consecuencia de esta política, el servicio AB90 debe distinguir:

**Canales estándar AB90 (skill drafts OK)**:
- LinkedIn personal/company
- Substack newsletter
- Medium (con import desde blog canonical)
- X / Bluesky / Threads
- Blog WordPress
- WhatsApp Canal
- Reels script / YouTube Short script

**Canales add-on "manual authorship" (cliente escribe)**:
- Hacker News (research-assist only)
- Quora (skill borrador + cliente reescribe ≥30%)
- Reddit r/programming, r/MachineLearning (research-assist only)
- Turnitin-checked academic content

Pitchear al cliente: "Te entregamos contenido publicable directo en 12 canales. Para HN y Quora te damos dossiers de datos verificables y tú escribes — política de plataforma."

---

## Recursos externos consultados

- [GPTZero · Detecting AI-Humanized Text](https://gptzero.me/news/detecting-ai-humanized-text-how-gptzero-stays-ahead/) — confirma que humanizers populares son detectables
- [Pangram Labs · Why Perplexity and Burstiness Fail](https://www.pangram.com/blog/why-perplexity-and-burstiness-fail-to-detect-ai) — limitaciones del análisis stylometric simple
- [Langvault · How Perplexity and Burstiness Expose AI Writing](https://langvault.com/how-perplexity-and-burstiness-expose-ai-writing/) — fundamentos técnicos
- [QuillBot · Burstiness & Perplexity Definitions](https://quillbot.com/blog/ai-writing-tools/burstiness-and-perplexity/) — definiciones canónicas
- HN newsguidelines · [Generated content](https://news.ycombinator.com/newsguidelines.html#generated) — política oficial HN
- HN precedente case [item id=47340079](https://news.ycombinator.com/item?id=47340079)

---

## Cambios futuros previsibles

Esta guía es válida en **mayo 2026** y debe revisarse trimestralmente porque:

- Los detectores evolucionan rápido (cada 2-3 meses cambios mayores)
- Los LLMs nuevos (Claude 4.8, GPT-5, Gemini 3) pueden ser más difíciles de detectar
- Las políticas de plataforma se ajustan (HN endureció clasificador en abril 2026)
- El concepto "errors = authenticity" puede invertirse si los LLMs aprenden a generar errores convincentes

**Próxima revisión sugerida**: agosto 2026


---

## El reencuadre definicional (ampliación, 24-sep-2026)

La checklist ya preguntaba por "no es X, es Y". No basta: hay que vetar **toda la familia**,
porque al quitar el "sino" o al partir la frase en dos el patrón sobrevive y sigue sonando a
máquina. Origen: Carlos Ortet, 24-sep-2026, sobre el informe de agentes. Su ejemplo: *"la
unidad de trabajo en GEO no es la táctica, es el diagnóstico que la selecciona"*.

| Variante | Ejemplo a evitar |
|---|---|
| Con "sino" | "no es un problema técnico, sino contractual" |
| Con coma (la más frecuente) | "el riesgo no es técnico, es contractual" |
| Partida en dos frases | "No compite en capacidad. Compite en que no hay que alojarlo." |
| Invertida | "es restricción de oferta, no de demanda" |
| Con "que" | "no es que piense rápido. Es que no tiene umbral" |
| Con sustantivo abstracto | "la unidad de trabajo no es A, es B" · "lo que cambia no es A, es B" · "la pregunta no es A, es B" |

**Por qué delata.** La persona experta afirma y concreta. El modelo necesita un contraste para
parecer perspicaz, así que inventa un adversario (la definición equivocada) solo para
derribarlo. Casi siempre el lector no sostenía esa creencia, de modo que la negación no
informa: decora.

**Cómo se corrige.** Quita la negación y afirma directamente. Si el contraste aporta algo real,
sepáralo en dos frases con contenido propio, no en dos mitades de la misma antítesis.

| Reencuadre | Corrección |
|---|---|
| "El riesgo no es técnico, es contractual." | "El riesgo está en el contrato." |
| "Lo que cambia no es la tecnología, es quién opera el servicio." | "La tecnología es la misma. Cambia quién opera el servicio." |
| "No compite en capacidad. Compite en que no hay que alojarlo." | "Su ventaja es que no hay que alojarlo ni mantenerlo." |
| "Es conversación de API, no de interfaz." | "Eso se resuelve en la API." |

**Regla operativa:** como mucho una por documento largo, y solo si el adversario que niega es
una creencia que el lector sostiene de verdad. Dos o más en el mismo texto es firma de LLM.
Cero en textos cortos (email, WhatsApp, post).

**Checklist actualizada:** sustituir el ítem "¿Hay alguna estructura 'no es X, es Y'?" por
"¿Hay más de un reencuadre definicional, en cualquiera de sus seis variantes?".
