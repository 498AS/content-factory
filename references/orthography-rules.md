# Reglas de revision ortografica y de estilo

## Cuando ejecutar

Despues de generar TODOS los outputs y ANTES de darlos por finalizados. Aplicar sobre CADA archivo generado en `project-XXX/output/`.

---

## 1. Revision de acentos y caracteres especiales

Revisar que cada output contiene los acentos y caracteres especiales correctos segun su idioma:

| Idioma | Verificar |
|--------|-----------|
| **Espanol (ES)** | Acentos (a, e, i, o, u), ene (n), signos de apertura (¿ ¡), dieresis (u en "linguistica", etc.) |
| **Catalan (CA)** | Acentos graves y agudos (a, e, i, o, u / a, e, o), ce trencada (c), punt volat en l·l (ela geminada) |
| **Ingles (EN)** | Sin acentos nativos, pero respetar acentos en nombres propios y palabras prestadas (e.g., "cafe", "naive", "resume") |
| **Espanol Facil (ES Facil)** | Mismas reglas que ES, sin excepciones |

### Errores frecuentes a detectar

#### Espanol
- "n" en lugar de "n" → "companias" debe ser "compañias"
- Ausencia de acentos en esdrujulas: "tecnologia" → "tecnologia" debe ser "tecnología"
- Ausencia de acentos en agudas: "informacion" → "informacion" debe ser "información"
- Falta de signos de apertura: "Que opinas?" → "¿Que opinas?" debe ser "¿Que opinas?"

#### Catalan
- Falta de ce trencada: "informacio" → "informacio" debe ser "informació" con c trencada
- Falta de punt volat: "intelligencia" → "intel·ligencia"
- Confundir acento grave y agudo: "tecnologia" (grave en catalan: "tecnologia" con accent obert)

#### Ingles
- Omitir acentos en prestamos: "cafe" → "cafe" (aceptable en ingles informal, mantener consistencia)
- Nombres propios: siempre respetar la ortografia original

---

## 2. Revision de capitalizacion (sentence case)

Verificar que TODOS los titulos, subtitulos, headlines y encabezados cumplen:

### Regla principal
- Solo la primera letra de la frase en mayuscula
- Nombres propios mantienen su mayuscula (marcas, personas, ciudades)
- Acronimos mantienen sus mayusculas (IA, SEO, SaaS, GEO, LLM)
- El resto de palabras en minuscula

### Donde aplica
- Titulos de blog (H1)
- Subtitulos y secciones (H2, H3)
- Headlines de LinkedIn
- Asuntos de Substack / newsletter
- Titulos de Medium, Dev.to, Hashnode, HackerNoon
- Titulos de Reddit, Hacker News
- Cualquier encabezado en todos los outputs y todos los idiomas

### Ejemplos

| Incorrecto | Correcto |
|------------|----------|
| Como Los Agentes De IA Estan Transformando El Marketing | Como los agentes de IA estan transformando el marketing |
| La Guia Definitiva Para Optimizar Tu Estrategia SEO | La guia definitiva para optimizar tu estrategia SEO |
| Why AI Agents Are Changing The Future Of Work | Why AI agents are changing the future of work |
| Els Agents D'IA Que Estan Canviant El Marketing Digital | Els agents d'IA que estan canviant el marketing digital |

### Excepcion para ingles

En ingles, sentence case tambien aplica. NO usar title case aunque sea convencion habitual en medios anglosajones. El estilo WriterBatch Zoopa usa sentence case en TODOS los idiomas.

---

## 3. Reglas globales de estilo (aplican a TODOS los canales y todos los idiomas)

> Aprendido de feedback real del autor en proyecto AI Chips Economy (mayo 2026). Estas reglas son **obligatorias en todo output**, no solo X/Twitter — aunque son especialmente delatoras ahí.

### 3.1 Prohibido el em-dash (—) y en-dash (–) en cualquier output

- **Razón**: el em-dash es la huella mas inconfundible de texto generado por LLM. Casi nadie lo usa en castellano natural escrito. En inglés tampoco abusa así.
- **NO uses** `—` ni `–` en ningún punto del cuerpo del texto: ni como pausa enfática, ni como apertura/cierre de inciso, ni para listas, ni en subtitulos.
- **Alternativas según función**:
  - Pausa enfática → coma, punto y aparte, o dos puntos
  - Inciso aclaratorio → paréntesis o comas
  - Listas con pseudo-bullet → punto seguido + frase nueva
- **Excepción única**: nombres propios o títulos donde el em-dash es ortográfico (e.g., "Costa Rica — Country Report 2025" si es exactamente el título oficial).

**Ejemplos**:

| Mal (con em-dash) | Bien |
|--|--|
| "Lo más sorprendente —y casi nadie lo cuenta— es que..." | "Lo más sorprendente: casi nadie lo cuenta. Es que..." |
| "Tres edificios — AP3, AP5, AP6 — saturados" | "Tres edificios. AP3, AP5, AP6. Todos saturados." |
| "Carl Zeiss SMT facturó €1.200M en 2016 — y €4.100M en 2024" | "Carl Zeiss SMT facturó €1.200M en 2016. En 2024: €4.100M." |
| "Una decisión industrial —y nadie habló de ella" | "Una decisión industrial. Y nadie habló de ella." |

### 3.2 Prohibido referencias temporales relativas que envejecen

- **NO** usar: "esta semana", "este mes", "ayer", "mañana", "hoy", "recientemente", "últimamente", "actualmente", "en los últimos días/meses".
- **Razón**: el contenido aparece en Substack, blog, RRSS con vida útil de meses o años. Leerlo en julio cuando dice "esta semana" lo invalida.
- **Alternativas**:
  - Específico → fecha exacta: "en septiembre de 2025", "el 7 de mayo de 2026"
  - Atemporal → quitar el marcador: "ASML invirtió €1.300M en Mistral" (sin "recientemente")
  - Referencia al evento → "tras la cumbre Xi-Trump", "después del PERTE Chip"

**Ejemplos**:

| Mal | Bien |
|--|--|
| "Esa frase la oirás en cada panel y keynote esta semana" | "Esa frase aparece en cada panel y keynote del último año" o simplemente "Esa frase está en todas partes" |
| "Recientemente ASML invirtió en Mistral" | "En septiembre de 2025 ASML invirtió en Mistral" |
| "Hoy se discute mucho sobre IA y geopolítica" | "Se discute mucho sobre IA y geopolítica" (sin "hoy") |
| "Últimamente China ha impuesto restricciones" | "Entre 2023 y 2025 China impuso restricciones" |

### 3.3 Prohibidas frases de "voz IA" formulaicas

- **Razón**: estas frases las genera el LLM por reflexión RLHF. Quemar texto al instante.

| Patrón formulaico | Por qué quema | Alternativa |
|--|--|--|
| "Esa frase la oirás en cada panel, keynote y artículo de opinión" | Rule-of-three obvio + tono profesoral | "Esa frase está en todas partes" o cortarla |
| "También es, técnicamente, falsa" | Antítesis pomposa | "Y es falsa" o "No encaja con cómo se hacen los chips" |
| "Lectura completa con datos verificados y fuentes:" | CTA formulaico | "Lo conté entero aquí:" o nada antes del link |
| "La conclusión:" | Cierre académico | terminar con la frase, sin etiqueta |
| "El verdadero X es Y" | Setup IA pomposo | dato directo: "Y es donde está el cuello" |
| "Te lo explico en N tuits 🧵" | Hilo-template clásico | empezar directo con el dato |
| "Aquí va una historia" / "Aquí va un hilo" | Meta-comentario inútil | empezar directo |

### 3.4 Prohibido el sandwich de listas con flechas →

- En castellano natural casi nadie usa "→" como bullet en redes.
- Sustituir por: punto y aparte + frase. O viñetas markdown "—" (guion simple, NO em-dash) o "•" si el medio las soporta nativo.

## 4. Procedimiento

1. Recorrer cada archivo generado en `project-XXX/output/`
2. Corregir acentos, enes y caracteres especiales segun idioma del archivo
3. Corregir capitalizacion incorrecta en titulos y encabezados
4. **Eliminar todos los `—` y `–`** del cuerpo (regla 3.1) y reescribir la frase
5. **Eliminar referencias temporales relativas** (regla 3.2) y reescribir con fecha o atemporal
6. **Reescribir frases formulaicas** detectadas (regla 3.3)
7. Guardar los archivos corregidos

**El proyecto NO se considera finalizado hasta completar este paso.**
