# Estructuras avanzadas para posts de LinkedIn

Cinco estructuras en las que **la forma del post forma parte del argumento**. Se eligen antes de
redactar, no se arreglan después.

**Cuándo se lee:** siempre que se vaya a escribir un post de LinkedIn, en PASO 3, antes de la
primera línea. Aplica a **cualquier presencia** (cuenta personal, Page de marca, portavoz del
equipo): es artesanía de plataforma, no la voz de una persona.

**Cómo compone con la voz.** Este fichero decide **cómo se arma el argumento**; la ficha de voz
decide **cómo suena quien lo firma**. Son capas distintas y no compiten: una estructura E3 con la
voz de Carlos y una E3 con la voz de una Page de marca son el mismo esqueleto con otro registro.
Para la cuenta personal de Carlos, la voz está en
[linkedin-voice-carlos-ortet.md](linkedin-voice-carlos-ortet.md), cuya «Estructura validada» de 11
bloques es un patrón **de voz**, no de argumento.

**Nota de notación:** las flechas de este documento marcan la secuencia de bloques. **Nunca van en
el post.** La regla de cero flechas en el output sigue en pie
([orthography-rules.md](orthography-rules.md) §3).

El esquema genérico Hook, re-hook y lista lo produce cualquier IA y no diferencia. **Úsalo solo
como último recurso.**

## Reglas comunes

- El hook cabe antes del «ver más»: unos **140 caracteres** en móvil, y como máximo **8-10
  palabras** en la primera línea.
- Mejor abrir con **un dato propio**: los hooks con dato rinden más y casi nadie los usa. Solo
  datos reales del usuario o de su trabajo (GEORadar, auditorías, campañas). **Nunca inventes
  cifras**: si no hay dato, pídelo o elige otra estructura.
- **Una idea por post**, de **900 a 1.500 caracteres**, con línea en blanco cada 1-3 frases. Ese es
  el objetivo, no el techo: el límite duro de la plataforma son 3.000 y lo comprueba
  `scripts/validators/validate_char_limits.py`.
- Nada de emojis decorativos, frases motivacionales ni preguntas genéricas al final («¿Qué
  opinas?»). Si cierras con pregunta, que sea **concreta y de respuesta corta**. Esto estrecha,
  sin contradecirla, la regla de cierre que ya está en
  [linkedin-voice-carlos-ortet.md](linkedin-voice-carlos-ortet.md) §«Pregunta abierta al final»,
  que pide pregunta concreta y descarta el CTA explícito.
- **Indica siempre qué estructura has usado y por qué.** Va en la nota de entrega del canal, no en
  el post.

## E1 · La lista que se rompe

Hook que promete una lista → 4 puntos con tono normal → el último punto contradice o relativiza la
premisa («…y 5: nada de lo anterior sirve si…») → 1-2 líneas de cierre.

El giro hace de re-hook **al final**, no al principio. Para desmontar consejos habituales del
sector.

## E2 · La nota al pie

Hook con un asterisco en la palabra clave («Ser visible\* en ChatGPT ya no depende de Google») →
desarrollo → última línea: «\*Por "visible" me refiero a…».

La nota añade una segunda lectura: un matiz, el tamaño de la muestra o una definición incómoda.
Para cuando un término del hook es ambiguo **a propósito**.

## E3 · Anomalía → Mecanismo → Implicación

1. **Anomalía**: un dato raro o contraintuitivo de primera mano (1-2 líneas).
2. **Mecanismo**: por qué ocurre, explicado sin jerga (3-5 líneas).
3. **Implicación**: qué cambia para quien lee, en prosa y sin viñetas (3-4 líneas).
4. Opcional: nota al pie con la metodología o la muestra.

**Es la estructura por defecto para contenido de GEO y de datos propios.**

## E4 · Puzzle hook

Plantea una adivinanza («Tres marcas, mismo presupuesto. Solo una aparece en Perplexity. ¿Cuál?»)
→ da las pistas → revela la respuesta → cuenta la lección.

**La respuesta no puede estar antes del «ver más».** Para casos y comparativas.

## E5 · Matriz 2×2 en texto

Hook que presenta dos ejes → 4 casillas, cada una con nombre propio y una sola línea → cierre:
«¿En qué casilla estás?».

Muestra un **modelo propio** del usuario, no una lista de consejos. Para posicionar una
metodología.

## Cómo elegir

| Situación | Estructura |
|---|---|
| Hay un dato propio sorprendente | **E3**, o **E2** si el dato necesita matiz |
| Toca desmontar un consejo habitual | **E1** |
| Hay un caso o una comparativa | **E4** |
| Toca presentar un marco o una metodología | **E5** |
| Ninguna de las anteriores | Hook, re-hook y lista, como último recurso |

## Checklist antes de entregar el canal

- [ ] Estructura elegida **antes** de redactar, y declarada en la nota de entrega con su motivo
- [ ] El hook cabe en ~140 caracteres y la primera línea no pasa de 8-10 palabras
- [ ] Si el hook lleva dato, el dato es **real y verificable**, no estimado ni redondeado a ojo
- [ ] Una sola idea; entre 900 y 1.500 caracteres
- [ ] Línea en blanco cada 1-3 frases
- [ ] Cero flechas, cero emojis decorativos, cero pregunta genérica de cierre
- [ ] En **E4**, la respuesta queda por debajo del corte del «ver más»
- [ ] En **E2**, la nota al pie aporta una segunda lectura y no repite el hook
- [ ] En **E1**, el punto que rompe la lista relativiza de verdad la premisa, no la adorna

## Procedencia

Estructuras aportadas por Carlos Ortet, 15-11-2026. Ampliar esta tabla cuando una estructura nueva
demuestre rendimiento, y anotar con qué presencia y con qué post se validó.
