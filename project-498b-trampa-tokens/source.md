# La trampa de los tokens

### Por qué depender de un solo proveedor de IA es un riesgo financiero, y por qué la estrategia multimodelo es ventaja competitiva antes de ser cuestión de supervivencia

> Documento fuente · 498A / Zoopa · 4 de junio de 2026
> Master source para generación de contenido multicanal.
> Metodología: investigación profunda con verificación adversarial (29 fuentes, 130 afirmaciones, 24 confirmadas) más segunda tanda dirigida (IA soberana cuantificada, citas de expertos, glosario). Las afirmaciones se marcan por nivel de confianza. Lo etiquetado como *contextual* o *tesis* procede de fuente única, blog u opinión y no se sometió a verificación adversarial.

---

## TL;DR

La trampa de los tokens es real, pero es asimétrica.

El precio por unidad de capacidad se desploma. Cae entre 5x y 10x al año para rendimiento equivalente, con picos de hasta 900x en hitos concretos. Altman lo cifra en 150x entre GPT-4 (2023) y GPT-4o (2024).

Y aun así, tu factura sube. Los modelos de razonamiento y los agentes queman de 5 a 30 veces más tokens por tarea, y hasta 1000x más en código agéntico. El coste absoluto de operar en frontera sube de 3x a 18x al año.

Gartner lo resume sin rodeos: hacia 2030 la inferencia costará más de un 90% menos a los proveedores, pero ese ahorro no llega al cliente, porque el consumo crece más rápido de lo que cae el precio.

El lock-in dejó de ser teoría. OpenAI retiró GPT-4o, GPT-4.1 y o4-mini de ChatGPT por decisión unilateral, alegando que solo el 0,1% de usuarios los usaba a diario. El proveedor controla el ciclo de vida del modelo del que dependes.

La economía de los labs no cierra. Sequoia cifró en 600.000 M$ el agujero entre la inversión en IA y los ingresos que la justifican. Si el precio de hoy está subsidiado, tu margen de mañana depende de decisiones ajenas.

La respuesta estructural, avalada por Gartner y ya operativa en producción, es la arquitectura multimodelo: enrutar cada tarea al modelo adecuado, con fallbacks entre proveedores y opción soberana. RouteLLM demuestra hasta 85% de ahorro reteniendo el 95% del rendimiento.

---

## El ángulo: sostenibilidad de modelos como activo estratégico

La conversación de mercado se quedó en el titular fácil: "la IA es cada vez más barata". Ese titular es cierto por token y engañoso por negocio.

Quien construya hoy un producto, un servicio o un flujo de trabajo sobre un único modelo de un único proveedor está firmando tres cheques en blanco a la vez:

1. **Cheque de precio.** Aceptas el pricing que el lab fije mañana.
2. **Cheque de continuidad.** Aceptas que el modelo siga existiendo.
3. **Cheque de consumo.** Aceptas que cada mejora de capacidad multiplique los tokens que pagas.

La tesis de este documento: la **sostenibilidad de la estrategia de modelos** es ya una ventaja competitiva medible. Quien la diseñe ahora, mientras es opcional, evitará tener que improvisarla cuando sea cuestión de vida o muerte para el margen.

---

## 1. Evolución de costes: la paradoja central

### El precio por capacidad cae a ritmo histórico

El precio para alcanzar un nivel de rendimiento dado cae entre **5x y 10x al año** según el paper de referencia *The Price of Progress* (MIT/Epoch, nov 2025). Los datos primarios de Epoch AI lo afinan: la caída va de 9x a 900x al año según el hito, con **mediana de 50x/año**. Filtrando solo datos posteriores a enero de 2024, la mediana sube a **200x/año**.
*(Confianza: alta. Fuentes: arXiv 2511.23455, Epoch AI. Verificado 3-0.)*

Tres voces de máxima autoridad coinciden en el "10x al año":

- **a16z (Guido Appenzeller), "LLMflation":** *"For an LLM of equivalent performance, the cost is decreasing by 10x every year."* Su ejemplo: alcanzar MMLU 42 costaba 60$/M tokens con GPT-3 (nov 2021) y 0,06$ con Llama 3.2 3B. *"The cost of LLM inference has dropped by a factor of 1,000 in 3 years"*, más rápido que el coste del cómputo en la era PC.
- **Sam Altman (OpenAI), "Three Observations" (feb 2025):** *"The cost to use a given level of AI falls about 10x every 12 months."* Y el dato concreto: *"the price per token dropped about 150x"* de GPT-4 (principios 2023) a GPT-4o (mediados 2024). *"Moore's law changed the world at 2x every 18 months; this is unbelievably stronger."*
- **Ethan Mollick (Wharton), "Mass Intelligence" (ago 2025):** *"When GPT-4 came out it was around $50 to work with a million tokens. Now it costs around 14 cents per million tokens."*

*(Contextual / citas de blog propio de cada autor. Convergencia notable en el 10x/año.)*

### Y aun así el coste por tarea sube

Aquí está la trampa. El paper *The Price of Progress* lo dice literal: **el coste absoluto de operar modelos frontier sube entre 3x y 18x al año**, porque cada mejora marginal de rendimiento exige sustancialmente más inferencia.
*(Confianza: alta. Verificado 3-0.)*

El mecanismo se llama consumo de tokens:

| Carga de trabajo | Consumo vs. baseline | Fuente |
|---|---|---|
| Chatbot estándar | 1x (baseline) | Gartner |
| Modelo agéntico | **5x a 30x más tokens/tarea** | Gartner (25-mar-2026) |
| Código agéntico | **~1000x más tokens** que chat de código | Microsoft Research (arXiv 2604.22750) |
| Una llamada a o3 | hasta ~50.000 tokens de razonamiento facturados como output antes de una respuesta de un párrafo | CloudZero |

*(Confianza: alta. Verificado 3-0 en los tres primeros.)*

Detalle crítico para presupuestar: en código agéntico el coste lo dominan los tokens de **input**, no de output. Y el consumo es estocástico. La misma tarea ejecutada dos veces puede diferir **hasta 30x** en tokens totales. Más tokens no significa más precisión.
*(Confianza: alta. Fuente: Microsoft Research/Stanford. Verificado 2-1 y 3-0.)*

### La brecha de precio entre modelos es de un orden de magnitud

Datos de mayo de 2026 (perecederos, ver caveats):

| Modelo | Input $/M tokens | Output $/M tokens |
|---|---|---|
| GPT-5.4 (flagship) | 2,50 | 15,00 |
| DeepSeek-chat | 0,27 | 1,10 |
| GPT-4.1 Nano | 0,10 | 0,40 |

Entre el flagship y el modelo nano hay **~25x de diferencia en input y ~37x en output**. Usar el modelo equivocado para una tarea trivial es tirar dinero por orden de magnitud.
*(Confianza: media. Fuentes: CloudZero, pricepertoken.com, OpenRouter. Las cifras concretas cambian mes a mes: DeepSeek ya pasó a V4 en junio.)*

---

## 2. El coste especulativo: dependes de una economía que pierde dinero

### El agujero de los 600.000 millones

David Cahn (Sequoia Capital), en *AI's $600B Question* (jun 2024), planteó el cálculo más citado del sector. Su método: *"take Nvidia's run-rate revenue forecast and multiply it by 2x to reflect the total cost of AI data centers... Then you multiply by 2x again, to reflect a 50% gross margin for the end-user of the GPU."*

Su conclusión incómoda: *"AI's $200B question is now AI's $600B question."* Es decir, hay un gap enorme entre lo invertido en infraestructura de IA y los ingresos que deberían justificarlo. Cahn no es un agorero: *"Speculative frenzies are part of technology... Those who remain level-headed through this moment have the chance to build extremely important companies."*
*(Contextual. Fuente: Sequoia Capital. Citas verbatim del ensayo.)*

### Los labs no son rentables en inferencia (probablemente)

La evidencia verificada confirma caída de precios y deprecaciones. No confirma las economías internas de los labs. Las señales contextuales apuntan en una dirección incómoda:

- **OpenAI** estaría perdiendo dinero en suscripciones. Un usuario de Claude Code o ChatGPT a 200$/mes puede consumir tokens por valor de **5.000$**.
- **Anthropic** "no es rentable a día de hoy" según el reporte; a los inversores se les pide "aguantar unos años más".
- El gasto empresarial en coding con IA llegó a **3.000 M$ anuales** (dato a16z).

*(Contextual. Fuentes: The Register, ikangai, uncoveralpha. No verificado adversarialmente.)*

Benedict Evans predice que **los modelos se commoditizarán y el poder de fijación de precios de los labs líderes se disipará**. Esa es la tesis optimista. La pesimista: consolidación y subida de precios.

La pregunta de negocio es la misma en ambos escenarios: **si el precio actual está subsidiado por capital de riesgo, ¿qué pasa con tu margen cuando los labs tengan que ser rentables?**

### El lock-in ya tiene víctimas

El 29 de enero de 2026 OpenAI anunció la retirada de GPT-4o, GPT-4.1, GPT-4.1 mini y o4-mini de ChatGPT, efectiva el 13 de febrero. Justificación oficial: solo el **0,1% de usuarios** seguía eligiendo GPT-4o a diario tras la migración a GPT-5.2.

El movimiento #keep4o reunió **21.000 firmas**. No cambió nada.
*(Confianza: alta. Fuente: OpenAI, confirmado por CNBC y Engadget. Verificado 3-0.)*

La lección no es sobre GPT-4o. Es sobre quién decide. El proveedor poda los modelos de bajo uso aunque una minoría dependa de ellos para producción. Si tu prompt engineering, tus evals y tu producto están calibrados sobre un modelo concreto, su retirada es tu problema, no el suyo.

(Matiz honesto: esta retirada aplicó al interfaz ChatGPT. La API "no cambia por ahora". Pero ilustra el patrón de migración forzada.)

Andrej Karpathy le puso nombre al riesgo sistémico. Cuando los LLMs punteros caen, dice, es *"kind of like an intelligence brownout in the world"*: *"the planet just gets dumber the more reliance we have on these models, which already is really dramatic."* Su marco: los LLMs *"feel like they have properties of utilities right now"*, con los labs gastando CAPEX para entrenar y OPEX para servir inteligencia por API. Depender de una sola utility es el riesgo.
*(Contextual. Fuente: charla "Software Is Changing (Again)", YC, jun 2025.)*

---

## 3. IA soberana: la independencia como cobertura de riesgo

Europa decidió que la dependencia de proveedores estadounidenses es un riesgo de Estado, no solo de empresa.

### Mistral AI: el caso testigo europeo

- **Serie C: 1.700 M€ levantados, valoración post-money 11.700 M€ (~13.800 M$), 9 sept 2025.** Lead investor ASML (1.300 M€); también NVIDIA, DST Global, a16z, Bpifrance. Más que dobló la valoración previa de 5.800 M€. *(Confianza alta: comunicado de Mistral + CNBC + Bloomberg.)*
- **ARR superó los 400 M$ en febrero 2026**, frente a ~20 M$ un año antes (×20). Objetivo: >1.000 M$ ARR a cierre de 2026. *(Confianza media-alta, secundaria.)*
- **Infraestructura propia**: data center cerca de París (~13.800 chips NVIDIA, 830 M$ de deuda, operativo Q2 2026), abandonando la dependencia de Azure/Google/CoreWeave. Segundo data center en Suecia (1.200 M€, 23 MW). *(Confianza media-alta.)*
- **Modelos open-weight bajo Apache 2.0**: Mistral 7B, Mixtral 8x7B y 8x22B (uso comercial libre, sin royalties). *(Confianza alta.)*
- **Pricing**: Mistral Large 3 reportado hasta ~80-90% más barato que Claude Sonnet 4.6 y GPT-5.4, a cambio de un contexto menor (128K). *(Confianza media, single-source; fuentes discrepan en cifras exactas.)*

Arthur Mensch, ante la Asamblea Nacional francesa (12 mayo 2026), articuló la tesis soberana con dureza:

> *"Once supply is monopolized by American players, suddenly we no longer have supply and we no longer transform electrons into tokens."*

> *"The Americans are deploying a trillion dollars next year. The one who controls the chips, who controls the electrons, who has massive access to energy, that's the one who wins."*

> *"In a world where you import all your digital services from the United States, you have no leverage over the United States."*

> *"It will be decided in the next two years."*

*(Confianza alta: múltiples medios; traducción del francés.)*

### Europa institucional

- **EuroStack**: alternativa europea de soberanía digital; inversión estimada de hasta **300.000 M€ para 2035** (informe Bertelsmann Stiftung), con un Fondo Tecnológico Europeo propuesto de 10.000 M€. *(Confianza media-alta.)*
- **EU Cloud and AI Development Act (CADA)** bajo la cartera de Henna Virkkunen (EVP Tech Sovereignty), anunciado el 3 jun 2026, para reducir la dependencia de proveedores US/chinos. *(Confianza alta: Comisión Europea.)*
- **EU AI Act plenamente aplicable el 2 de agosto de 2026**, con obligaciones de gobernanza de datos para sistemas de alto riesgo. *(Confianza alta.)*
- El driver de fondo: los hyperscalers US controlan **>70% del mercado cloud de la UE** y están sujetos al CLOUD Act y FISA, lo que crea el problema "residencia del dato ≠ soberanía del dato". *(Confianza media-alta.)*

### DeepSeek: la disrupción de coste

- **Coste reportado: ~5,576 M$** (2,788 M de horas-GPU H800 a 2$/h, sobre 2.048 GPUs H800), según el *DeepSeek-V3 Technical Report* (arXiv 2412.19437). *(Confianza alta.)*
- **Caveat clave del propio paper**: esa cifra cubre *"only the official training of DeepSeek-V3, excluding the costs associated with prior research and ablation experiments."* Es el coste GPU de la corrida final, no el TCO. SemiAnalysis estima el CapEx total real en **1.300-1.600 M$** (~50.000 GPUs clase Hopper). *(Estimación, no auditada.)*
- **Impacto de mercado**: el 27 de enero de 2025, NVIDIA perdió **~600.000 M$ de capitalización en un día (-16,9%)**, la mayor caída diaria de cualquier empresa en la historia de EE.UU., tras el lanzamiento de R1. *(Confianza alta: CNBC, NBC, Fortune.)*
- **Modelos open-weight bajo licencia MIT** (self-hosting permitido). R1 reportado ~96% más barato que o1 de OpenAI. *(Confianza alta en la licencia; media en pricing.)*
- **Por qué disrumpió**: rendimiento comparable a o1 a fracción del coste, arquitectura MoE eficiente, pesos abiertos. Rompió la asunción de que el estado del arte exigía CapEx masivo y modelos cerrados.

### Self-hosting: cuándo compensa

Economía orientativa (blogs técnicos 2026, *confianza baja-media*, rangos no canónicos):

- **Breakeven contra API premium (~5$/M)**: ~256 M tokens/mes, asumiendo 60-70% de utilización de GPU.
- **Breakeven contra API open-weight barata**: del orden de miles de millones de tokens/mes (estimaciones de 5.700 M a 11.000 M tokens/mes con una H100).
- **La variable crítica es la utilización de GPU**: a 10% de carga, el coste efectivo por token se dispara 10x y pierde frente a la API.
- **Regla de TCO**: multiplicar el coste bruto de GPU por **1,3x-2,0x** para el coste real.
- **El override de compliance**: para cargas HIPAA/RGPD/SOC2, el breakeven a menudo es irrelevante. Sin acuerdo de tratamiento de datos, las APIs de consumo no pueden procesar legalmente datos protegidos, lo que hace del self-hosting la única vía conforme. **La decisión deja de ser de coste y pasa a ser de jurisdicción.**

> **Nota de fiabilidad.** El eje soberano combina datos duros (Mistral Serie C, coste GPU de DeepSeek, caída de NVIDIA, fechas del EU AI Act) con estimaciones blandas (umbrales de self-hosting, pricing exacto de Mistral). Usar las primeras sin reservas; marcar las segundas como orientativas.

---

## 4. La respuesta: estrategia multimodelo (el ángulo Zoopa)

### Gartner avala la arquitectura, no solo la idea

> *"El valor se acumulará en las plataformas capaces de orquestar cargas a través de un portfolio diverso de modelos. Las tareas rutinarias de alta frecuencia deben enrutarse a modelos pequeños y de dominio específico. La inferencia cara de los modelos frontier debe estar fuertemente restringida y reservada en exclusiva para razonamiento complejo de alto margen."*
> — Gartner, 25 de marzo de 2026

*(Confianza: alta. Verificado 3-0.)*

Esto valida exactamente el enfoque de Zoopa: **agentes que distribuyen tareas entre modelos**, eligiendo el adecuado por coste y capacidad, con fallbacks entre proveedores.

### El ahorro está cuantificado

**RouteLLM** (LMSYS / UC Berkeley) enruta entre un modelo fuerte y uno débil según la complejidad del prompt:

| Benchmark | Ahorro de coste | Rendimiento retenido |
|---|---|---|
| MT Bench | **>85%** | 95% de GPT-4 |
| MMLU | **45%** | 95% de GPT-4 |
| GSM8K | **35%** | 95% de GPT-4 |

*(Confianza: alta. Fuente: LMSYS. Verificado 3-0. Caveat: 85% es el benchmark más favorable; el ahorro real varía fuerte por tarea.)*

### Las herramientas de producción ya existen

No hay que construir el routing desde cero:

- **OpenRouter Auto Router**: selecciona el modelo de un pool curado según complejidad y tipo de tarea, con un parámetro explícito de tradeoff coste-calidad en escala 0-10 (0 = máxima calidad sin importar coste, 10 = máximo ahorro).
- **LiteLLM** (open-source, self-hostable): gateway a 100+ APIs de LLM con **fallback automático en cadena ordenada** entre proveedores cuando una llamada falla. Resiliencia multiproveedor sin lock-in.
- **RouteLLM**: código abierto, routing entrenado.

*(Confianza: alta. Fuentes: docs de OpenRouter y LiteLLM. Verificado 3-0.)*

### La arquitectura de modelos sostenible, en 4 capas

1. **Clasificación de tarea.** Cada petición se etiqueta por complejidad antes de tocar un modelo.
2. **Enrutamiento por coste-capacidad.** Tareas triviales a modelos nano/pequeños; razonamiento complejo a frontera, restringido.
3. **Fallback multiproveedor.** Cadena ordenada entre labs distintos. Si uno cae, sube de precio o deprecia un modelo, el sistema no se entera.
4. **Opción soberana / open-weight.** Para dato sensible o para desacoplarse del pago por token, modelos self-hosted en la cadena.

Esto es resiliencia (no dependes de un proveedor) más eficiencia (no pagas frontera por tareas triviales) en una sola decisión de diseño.

---

## 5. Voces de expertos (citas textuales)

**Sobre el abaratamiento (la tesis del 10x):**
- **Guido Appenzeller (a16z):** *"For an LLM of equivalent performance, the cost is decreasing by 10x every year... The cost of LLM inference has dropped by a factor of 1,000 in 3 years."*
- **Sam Altman (OpenAI):** *"The cost to use a given level of AI falls about 10x every 12 months, and lower prices lead to much more use."*
- **Ethan Mollick (Wharton):** *"When GPT-4 came out it was around $50 to work with a million tokens. Now it costs around 14 cents per million tokens."* Y: *"Google has reported that energy efficiency per prompt has improved by 33x in the last year alone."*

**El contrapunto (el abaratamiento no es infinito):**
- **Ethan Mollick (X, ~mar 2026):** *"I think it is entirely possible that there will be no new frontier open weights models at some point in the near future. Counting on the Chinese AI labs to keep making their models free forever doesn't make sense as model costs rise."*
- **Benedict Evans:** los modelos se commoditizarán y el poder de pricing de los labs líderes se disipará (paráfrasis).

**Sobre la sostenibilidad económica y la burbuja:**
- **David Cahn (Sequoia):** *"AI's $200B question is now AI's $600B question."* / *"Where is all the revenue?"* / *"Speculative frenzies are part of technology, and so they are not something to be afraid of."*

**Sobre el riesgo sistémico de dependencia:**
- **Andrej Karpathy:** *"LLMs certainly feel like they have properties of utilities right now."* / *"the planet just gets dumber the more reliance we have on these models."*

**Sobre la soberanía:**
- **Arthur Mensch (Mistral):** *"In a world where you import all your digital services from the United States, you have no leverage over the United States."*

> **Nota.** No existe cita textual de Karpathy con cifras de coste de inferencia. El dato "la inferencia se reduce a la mitad cada 8 semanas" que circula NO es suyo. Las citas de X (Mollick, a16z) están confirmadas en texto pero no en fecha exacta (X bloquea el fetch).

---

## 6. Extrapolación cuantificada 2027-2030

| Variable | Trayectoria | Fuente |
|---|---|---|
| Coste de inferencia para el proveedor (LLM de 1B parámetros) | **>90% más barato en 2030** vs. 2025 | Gartner |
| Eficiencia de coste de los LLMs en 2030 | hasta **100x** vs. modelos equivalentes de 2022 | Gartner |
| Precio por capacidad equivalente | **5x a 10x más barato cada año** (mediana 50x, acelerando a 200x post-2024) | Epoch AI, MIT, a16z, Altman |
| Coste total de inferencia para la empresa | **AL ALZA**, el consumo crece más rápido que la caída de precio | Gartner |
| Consumo de tokens por tarea agéntica | **5x a 30x** sobre chatbot; tendencia creciente con más autonomía | Gartner |
| Poder de fijación de precios de los labs | **A la baja** por commoditización | Benedict Evans (contextual) |
| Gap inversión-ingresos | **600.000 M$** a resolver | Sequoia (2024) |

**La predicción operativa.** El precio por token seguirá cayendo y será una distracción. La variable que decidirá márgenes hacia 2030 es el **consumo**, no el precio unitario. Las organizaciones que no controlen qué modelo ejecuta qué tarea verán su factura de IA crecer aunque cada token sea más barato.

Gartner es explícito: *"el cliente no va a ver todo ese dinero"*. El ahorro de eficiencia se lo queda la dinámica de consumo.

**Conclusión.** Hacia 2027-2030 la estrategia de modelos deja de ser una optimización técnica y pasa a ser una palanca de margen de primer orden. Quien la diseñe ahora, mientras la IA está subsidiada y el routing es opcional, llegará a ese punto con una ventaja estructural. Quien la deje para cuando duela, la diseñará bajo presión, con el margen ya comprometido y un proveedor decidiendo su ciclo de vida.

La sostenibilidad de la estrategia de modelos es ventaja competitiva ahora. Después es supervivencia.

---

## 7. Una tesis crítica: por qué cambió la narrativa de la IA

> Esta sección recoge una **tesis de opinión** procedente de una transcripción de vídeo (creador pro-soberanía de IA). No es evidencia verificada. Se incluye porque su análisis del *incentivo económico detrás del consumo de tokens* es lúcido y conecta de forma directa con el resto del documento. Tratar como marco interpretativo, no como hecho.

### El giro de narrativa

La narrativa de la IA cambió de *"la IA reemplazará a los humanos"* a *"todo humano necesita usar IA para ser más productivo"*. La tesis: no es un giro ético, es un giro de modelo de negocio.

El argumento es elegante. **Para quemar tokens hacen falta humanos.** La IA todavía no trabaja sola de forma autónoma a escala. La promesa de reemplazar al humano no se puede cumplir hoy, pero los labs necesitan justificar inversiones colosales. ¿Cómo se justifican? Aumentando el consumo de tokens. ¿Y cómo se aumenta el consumo? Poniendo a los 8.000 millones de humanos a usar IA. De ahí el mensaje "no despidas a tu gente, dale IA".

Beneficio colateral: ese giro **desactiva el backlash social**. Si la IA no reemplaza al trabajador sino que lo "empodera", desaparece la pregunta incómoda del plan B para los desplazados.

### El monopolio del cómputo

La segunda pieza de la tesis: las grandes corporaciones eligieron, entre todas las vías posibles de desarrollar IA, **la más cara**, la que depende de cantidades masivas de cómputo. No por necesidad técnica pura, sino como estrategia de monopolio: si entrenar un modelo frontera cuesta miles de millones, nadie fuera de un puñado de gigantes puede competir. China responde con la estrategia inversa: hacerlo extremadamente barato (la jugada DeepSeek).

### El falso KPI del consumo

El punto más valioso y operativo de la tesis, y el que más refuerza este documento:

**Medir la productividad por número de tokens consumidos es un error interesado.** Solo tiene sentido para quien vende tokens. La métrica correcta no es cuántos tokens quemas, sino **la relación entre la calidad del output y su coste**. El objetivo es el mínimo de tokens para la máxima calidad de salida, no el máximo de tokens para aparentar productividad.

Esto es exactamente lo que justifica la arquitectura multimodelo: enrutar al modelo más barato que resuelve la tarea con calidad suficiente, no al más caro por defecto.

### Ganar tiempo hacia la AGI

La misión de fondo de los labs, según la tesis, no cambió: sigue siendo construir AGI capaz de reemplazar trabajo humano, con un horizonte estimado de **2028-2030**. El giro de narrativa solo **compra tiempo** para llegar a ese punto sin que la burbuja estalle antes.

### La salida: soberanía

La conclusión del autor es la misma que la de este documento desde otro ángulo: **soberanía de IA**. Poseer el sistema, priorizar IA local cuando es posible y operar un escenario mixto local + cloud, usando los modelos de los grandes proveedores solo cuando es necesario. Salir del juego de incentivos ajeno.

---

## Glosario: conceptos básicos

> Definiciones técnicamente correctas y accesibles para perfil de negocio. Ordenadas de lo fundamental a lo derivado.

### Token
Unidad mínima de texto que un modelo procesa y factura. No es una palabra ni una letra, sino un fragmento (una palabra corta, parte de una palabra, un signo) generado por un tokenizador tipo BPE. Como el modelo predice y cobra token a token, **el token es la moneda real de la economía de los LLMs**. En inglés, **1 token ≈ 0,75 palabras** (100 tokens ≈ 75 palabras). El español es menos eficiente: la misma idea consume más tokens porque los tokenizadores se entrenaron sobre todo con inglés, así que operar en español cuesta más por idea expresada.

### Input tokens vs Output tokens
Todo intercambio se cobra en dos partidas. El **input** es lo que envías (prompt, documentos, historial). El **output** es lo que el modelo genera. **El output es más caro, normalmente entre 3x y 8x**, porque generar cada token de salida exige una pasada completa del modelo. Implicación: las respuestas verbosas disparan la factura más rápido que los prompts largos.

### Context window (ventana de contexto)
Máximo de tokens que un modelo puede "tener en mente" a la vez (input + output). Es su memoria de trabajo: lo que queda fuera, no lo ve. Va de miles a más de un millón de tokens en modelos punteros. **Cada token dentro de la ventana se factura en cada llamada**: llenar ventanas enormes en cada petición es una forma clásica de caer en la trampa.

### Inferencia vs Entrenamiento
El **entrenamiento** es el proceso único y carísimo de crear el modelo (millones de dólares, semanas de GPUs). La **inferencia** es cada uso del modelo ya entrenado. El entrenamiento es coste de capital del proveedor; **la inferencia es el coste recurrente que paga el cliente**. Toda la trampa de los tokens vive en la inferencia.

### LLM (Large Language Model)
Modelo de lenguaje de gran tamaño entrenado para predecir el siguiente token según el contexto. Con miles de millones de parámetros, generaliza a casi cualquier tarea de lenguaje sin entrenamiento específico. Es la categoría base. Ejemplos: GPT, Claude, Gemini, Llama.

### RLM (Reasoning Language Model)
**El acrónimo es ambiguo; el sentido relevante para coste de tokens es Reasoning Language Model.** Es un LLM post-entrenado (normalmente con refuerzo) para resolver problemas complejos generando **cadenas de razonamiento explícitas (chain-of-thought) antes de la respuesta final**. A diferencia de un LLM estándar, que responde directo ("System 1", intuitivo), el RLM "piensa en voz alta" en pasos ("System 2", deliberativo): descompone, se autocorrige, valida. Ejemplos: o1/o3 de OpenAI, los modos "thinking" de Claude y Gemini, DeepSeek-R1.

**Por qué consume muchísimos más tokens.** Antes de responder genera una cadena de **reasoning tokens** (monólogo interno), que suele ocupar miles de tokens, que el usuario normalmente no ve pero **sí paga**, y que se facturan como output (la partida cara, del orden de 6x el input). De ahí la trampa: una sola pregunta a un modelo de razonamiento puede consumir 10x o más tokens que la misma a un LLM estándar.

*Otros sentidos de "RLM" (no confundir): Recursive Language Model (paradigma de inferencia de contexto largo, 2025-2026); Recurrent/Routing (lecturas sueltas, poco estandarizadas).*

### Chain-of-thought (CoT) y reasoning tokens
**CoT** es la técnica por la que un modelo expone pasos intermedios de razonamiento en vez de saltar a la respuesta. En su origen era prompting ("piensa paso a paso"); en los modelos de razonamiento es comportamiento entrenado de fábrica. Los **reasoning tokens** son los tokens de esa cadena: miles por consulta, facturados como salida, a menudo ocultos al usuario. Son la causa directa de que el razonamiento sea caro.

### SLM (Small Language Model) y modelos de dominio
Un **SLM** es un modelo reducido (de cientos de millones a pocos miles de millones de parámetros), rápido, barato y ejecutable en hardware modesto. Sacrifica conocimiento general por coste y latencia bajos. Los **modelos de dominio** son SLM afinados para una tarea o sector (legal, médico, soporte); en su nicho igualan o superan a un LLM grande a fracción del coste. Son la palanca principal contra la trampa: modelo pequeño para el 80% de tareas simples, grande para lo complejo.

### Model routing (enrutamiento de modelos)
Sistema que, ante cada petición, decide automáticamente **qué modelo es el más adecuado**: las simples a un modelo pequeño y barato, las complejas a uno grande. Optimiza coste/calidad sin que el usuario elija. Es una de las defensas más efectivas contra la trampa. (No confundir con "Routing Language Model".)

### Fallback
Mecanismo de respaldo: si el modelo o proveedor principal falla (caída, límite de uso, error, baja calidad), el sistema reintenta automáticamente con un **alternativo**. Aporta robustez. Cara de coste: mal diseñado, puede reintentar en modelos más caros o duplicar llamadas.

### Open-weight vs Open-source vs propietario
- **Propietario / cerrado:** solo vía API; no se publican pesos ni código (GPT, Claude, Gemini). Pagas por token, no lo alojas tú.
- **Open-weight:** se publican los **pesos** (puedes descargarlo y ejecutarlo), pero no necesariamente datos ni licencia plenamente libre (Llama). Permite self-hosting.
- **Open-source estricto:** pesos, código y datos bajo licencia libre. El nivel más abierto. Muchos modelos "open source" son en realidad solo open-weight.

Solo open-weight u open-source permiten escapar del coste por token alojando el modelo por tu cuenta.

### Agente / sistema agéntico
Sistema en el que el LLM no solo responde, sino que **planifica y ejecuta tareas de varios pasos de forma autónoma**, usando herramientas en un bucle hasta cumplir un objetivo. Impacto de coste central: hace muchas llamadas encadenadas, y cada paso reinyecta el contexto acumulado como input. El consumo crece de forma no lineal e invisible. Es el mayor amplificador de gasto de tokens.

### Prompt caching
El proveedor **almacena la parte estable y repetida de un prompt** (instrucciones de sistema, documentos, ejemplos) para no reprocesarla cada vez. En la siguiente llamada que la reutilice, esos tokens se cobran reducidos. Anthropic: acierto de caché al **10% del precio de input** (90% de descuento). OpenAI: **50% de descuento** automático. Una de las optimizaciones de mayor retorno con prompts largos repetidos.

### Fine-tuning vs RAG
- **Fine-tuning:** reentrenar parcialmente el modelo con tus datos; coste de entrenamiento por adelantado, luego prompts cortos y baratos.
- **RAG (Retrieval-Augmented Generation):** dejar el modelo intacto y, en cada consulta, recuperar documentos relevantes e inyectarlos en el prompt; flexible y actualizable al instante, pero **engorda el input** y sube el gasto recurrente.

Regla: fine-tuning para comportamiento/estilo estable; RAG para conocimiento que cambia.

### AGI (Artificial General Intelligence)
Sistema hipotético capaz de igualar o superar a un humano en prácticamente cualquier tarea cognitiva. **No hay consenso** sobre qué es ni cómo medirla: no existe definición operativa única, ni acuerdo sobre cómo medir "inteligencia general", y el término tiene fuerte carga comercial. Hoy funciona más como aspiración que como categoría técnica medible.

### Self-hosting / on-premise
Ejecutar un modelo (open-weight u open-source) en infraestructura propia en vez de llamar a una API. Desaparece el pago por token; el coste pasa a ser infraestructura, GPUs, energía y operación. Sale a cuenta a gran volumen y aporta control, privacidad y previsibilidad, a cambio de complejidad técnica.

### Soberanía de IA y soberanía del dato
**Soberanía de IA:** capacidad de una organización o país de controlar su propia infraestructura de IA (modelos, cómputo, datos) sin depender críticamente de terceros extranjeros. **Soberanía del dato:** garantizar que los datos se procesan y almacenan bajo la jurisdicción y reglas propias. Es el principal argumento no económico para el self-hosting y los modelos open-weight.

---

## Caveats y limitaciones de evidencia

1. Las cifras de Gartner (90%, 100x, 5-30x) son pronósticos de analista, no hechos medidos.
2. El paper arXiv 2511.23455 es preprint sin revisión por pares; el rango 3x-18x usa tres benchmarks como proxy.
3. Epoch AI advierte que los ritmos más rápidos (900x/año) empiezan tras ene-2024 y "pueden no persistir".
4. El ahorro de RouteLLM (85%) es el benchmark más favorable de los propios autores; MMLU/GSM8K dan 45%/35%.
5. Los precios concretos son extremadamente perecederos. Las cifras de mayo de 2026 ya cambiaban en junio.
6. **Citas de blog/X** (Altman, Mollick, Appenzeller, Cahn, Karpathy, Mensch) están confirmadas en texto pero algunas no en fecha exacta. No fueron sometidas a verificación adversarial de 3 votos.
7. **Estimaciones blandas marcadas**: TCO y breakeven de self-hosting (blogs 2026), coste total real de DeepSeek (1,3-1,6 B$ es estimación SemiAnalysis), pricing exacto de Mistral Large 3 (fuentes discrepan).
8. La **Sección 7** es una tesis de opinión de una transcripción de vídeo, no evidencia.
9. Una claim fue **refutada (0-3)** y descartada: cifras erróneas sobre GPT-5.4 Pro a 180$, Claude 3 Opus a 75$, DeepSeek V3 a 1,1$ y Gemini 1.5 Flash a 0,3$.

## Fuentes

**Primarias / alta confianza:**
- arXiv 2511.23455, *The Price of Progress* (MIT/Epoch): https://arxiv.org/pdf/2511.23455
- Epoch AI, LLM inference price trends: https://epoch.ai/data-insights/llm-inference-price-trends
- Gartner (25-mar-2026), inference cost forecast 2030: https://www.gartner.com/en/newsroom/press-releases/2026-03-25-gartner-predicts-that-by-2030-performing-inference-on-an-llm-with-1-trillion-parameters-will-cost-genai-providers-over-90-percent-less-than-in-2025
- Microsoft Research (arXiv 2604.22750), token consumption in agentic coding: https://www.microsoft.com/en-us/research/publication/how-do-ai-agents-spend-your-money-analyzing-and-predicting-token-consumption-in-agentic-coding-tasks/
- OpenAI, retiring GPT-4o: https://openai.com/index/retiring-gpt-4o-and-older-models/
- DeepSeek-V3 Technical Report (arXiv 2412.19437): https://arxiv.org/abs/2412.19437
- Mistral Serie C: https://mistral.ai/news/mistral-ai-raises-1-7-b-to-accelerate-technological-progress-with-ai/
- LMSYS RouteLLM: https://www.lmsys.org/blog/2024-07-01-routellm/
- OpenRouter Auto Router: https://openrouter.ai/docs/guides/routing/routers/auto-router
- LiteLLM reliability/fallbacks: https://docs.litellm.ai/docs/proxy/reliability

**Citas de expertos:**
- a16z LLMflation (Appenzeller): https://a16z.com/llmflation-llm-inference-cost/
- Sam Altman, Three Observations: https://blog.samaltman.com/three-observations
- Ethan Mollick, Mass Intelligence: https://www.oneusefulthing.org/p/mass-intelligence
- Sequoia (David Cahn), AI's $600B Question: https://www.sequoiacap.com/article/ais-600b-question/
- Andrej Karpathy, Software Is Changing Again (transcripción): https://singjupost.com/andrej-karpathy-software-is-changing-again/

**Secundarias / contextuales:**
- CloudZero, LLM API pricing: https://www.cloudzero.com/blog/llm-api-pricing-comparison/
- The Register, AI margins: https://www.theregister.com/ai-ml/2026/05/18/the-big-ai-companies-are-going-to-see-their-margins-disappear/
- esg.ai, Mistral sovereign AI: https://esg.ai/mistral-ai-how-europes-sovereign-ai-pioneer-outmaneuvers-american-giants/
- SemiAnalysis, DeepSeek debates: https://newsletter.semianalysis.com/p/deepseek-debates
- CNBC, NVIDIA -$600B: https://www.cnbc.com/2025/01/27/nvidia-sheds-almost-600-billion-in-market-cap-biggest-drop-ever.html
- Bertelsmann Stiftung, EuroStack: https://www.bertelsmann-stiftung.de/en/our-projects/reframetech-algorithmen-fuers-gemeinwohl/project-news/eurostack-a-european-alternative-for-digital-sovereignty
- Comisión Europea, tech sovereignty (3-jun-2026): https://commission.europa.eu/news-and-media/news/strengthening-europes-tech-sovereignty-2026-06-03_en

**Glosario (referencias técnicas):**
- OpenAI, what are tokens: https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them
- Reasoning Language Models: A Blueprint (arXiv 2501.11223): https://arxiv.org/html/2501.11223v1
- Recursive Language Models (Alex L. Zhang): https://alexzhang13.github.io/blog/2025/rlm/
- Anthropic pricing / prompt caching: https://platform.claude.com/docs/en/about-claude/pricing

---

*498A / Zoopa · Documento fuente para generación de contenido · Confidencial.*
