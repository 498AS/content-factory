# Quora — best practices para content-factory

> Output canal Quora. Pull search-driven, long-tail SEO/GEO, alta vida útil (5-10 años por respuesta).

## Por qué Quora en el stack

- Está en el corpus de entrenamiento de los LLMs (ChatGPT, Gemini, Claude) y aparece citada en respuestas a queries informativas.
- Sigue rankeando en Google (autoridad de dominio alta).
- Long-tail extremo: una respuesta puede traer tráfico durante 5-10 años sin tocarla.
- Pull (búsqueda) vs push (Substack/LinkedIn): cubre el hueco "que te encuentren cuando buscan".

## Requisitos de cuenta

- **Antigüedad mínima recomendada:** 30 días antes de postear contenido con links.
- **Bio completa:** nombre real, cargo, empresas, link al sitio (Quora penaliza perfiles vacíos).
- **Foto profesional** (la misma de LinkedIn idealmente — coherencia cross-canal).
- **Credentials específicas por topic:** Quora permite añadir "credenciales" por tema. Aprovéchalo: `"CEO at Zoopa"` para topic Marketing, `"GEO researcher · georadar.app"` para topic AI, etc.
- **Topics seguidos:** mínimo 5 relevantes para que el algoritmo te empiece a recomendar preguntas.

## Formato de respuesta óptimo

- **Longitud:** 600-1.200 palabras. Respuestas <300 palabras casi nunca rankean.
- **Estructura:**
  1. Frase 1 — respuesta directa a la pregunta (snippet-friendly para LLMs).
  2. Párrafo 2 — contexto / por qué importa.
  3. Cuerpo — datos, ejemplos, números, casos.
  4. Cierre — síntesis o caveat.
- **Una imagen mínimo** (diagrama, captura, gráfico). Quora prioriza visualmente respuestas con imagen y aumenta CTR ~30%.
- **Enlaces:** máximo 1-2 enlaces salientes y solo si aportan. Más de 2 = spam signal.
- **Listas y bullets:** sí, pero intercalados con prosa. Quora penaliza respuestas todo-bullets.

## Reglas de idioma

| Tipo de query | Idioma | Razón |
|---|---|---|
| Técnico / GEO / AI / marketing B2B | **EN** | Audiencia técnica internacional, LLMs prefieren EN |
| Negocio local / agencia / empresa España | **ES** | Quora ES tiene menos competencia, fácil ranking |
| Consumer / lifestyle / generalista | **ES** | Audiencia local engaged |
| Catalán | **No** | Quora CA tiene tráfico residual, no compensa |

**Mix recomendado para perfiles profesionales tipo Carlos Ortet:** 70% EN, 30% ES. Cero CA.

## Cómo elegir preguntas a responder

1. **Search volume + respuestas mediocres** = oportunidad.
   - Herramientas: Quora "Search by topic" + Ahrefs/SEMrush para volumen.
   - Buscar `[query] site:quora.com` en Google → ver qué Quoras rankean ya.
2. **Preguntas con <5 respuestas y >1.000 vistas** = sweet spot.
3. **Evitar:**
   - Preguntas "evergreen saturadas" (ya hay 50 respuestas con miles de upvotes).
   - Preguntas hiperespecíficas con 0 búsqueda mensual.
   - Preguntas politizadas (downvotes garantizados).
4. **Preguntas que no existen** se pueden crear, pero solo aportan si tú mismo aportas tráfico (LinkedIn, Substack) — no esperan tráfico orgánico inicial.

## Disclosure y conflicto de interés

- **Si mencionas tu producto/empresa:** disclosure explícito al final ("Disclosure: I'm CEO of Zoopa, an agency working on this").
- **Si linkas a tu propio contenido:** máximo 1 link y solo si es la mejor referencia objetiva disponible. Quora baja respuestas autopromocionales.

## Anti-patrones (penalizan o bannean)

- Misma respuesta copiada en varias preguntas similares.
- Respuesta cortísima ("Sí, totalmente") en preguntas serias.
- Auto-promo descarada sin disclosure.
- Comentarios genéricos en respuestas de otros para inflar perfil.
- Más de 2 enlaces salientes por respuesta.

## Output content-factory

**Archivo:** `quora_ready.txt` (un fichero por respuesta cuando aplique, o multi-respuesta separadas por `---`).

**Estructura del .txt:**

```
PREGUNTA: [texto exacto de la pregunta de Quora]
URL_PREGUNTA: [url si existe ya, "crear nueva" si no]
IDIOMA: [EN/ES]
TOPIC_QUORA: [topic principal donde encaja]
LONGITUD_OBJETIVO: [800-1200 palabras]
CREDENTIAL_USAR: [credencial específica del topic]

---RESPUESTA---

[texto de la respuesta — formato plain text, sin markdown agresivo, párrafos separados por línea en blanco]

---DISCLOSURE---

[disclosure si procede]

---NOTAS_PUBLICACION---

[recordatorios para el publicador: imagen a añadir, link a poner, topic a clasificar]
```

## Reciclaje desde otros canales (cero coste marginal)

Cada source.md de content-factory puede generar:
- 1 post Substack (ya hace).
- 1 post LinkedIn (ya hace).
- **2-3 respuestas Quora** derivadas, identificando preguntas existentes que el contenido responde directamente.

El prompt para extraer preguntas Quora desde un source.md:

> "Dado este source, identifica 3 preguntas reales que probablemente existan en Quora EN y 2 en ES, donde una respuesta basada en este contenido pueda rankear. Para cada una, propón título exacto de la respuesta (no la pregunta), longitud, credencial a usar y 1 imagen recomendada."

## Métricas de éxito

- **Operativas (mensual):** vistas/respuesta, upvotes, comentarios, shares externos.
- **De canal (trimestral):** vistas totales del perfil, tasa vistas/respuesta media.
- **De impacto GEO (mensual, vía GEOradar):** citation lift de Quora en respuestas LLM para queries target.

KPI principal a 12 meses: **5-10 respuestas con >5.000 vistas/año cada una**, presencia constante en respuestas LLM para queries del nicho.
