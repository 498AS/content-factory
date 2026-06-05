<!--
SEO METADATA (no publicar como contenido visible; volcar en los campos de Rank Math)
Title: La trampa de los tokens: depender de un solo proveedor de IA es un riesgo financiero | Zoopa
Meta description: El precio por token se desploma y tu factura sube igual. Depender de un solo modelo de un solo proveedor firma tres cheques en blanco. La respuesta es la estrategia multimodelo.
Slug: trampa-tokens-riesgo-proveedor-unico-estrategia-multimodelo
Focus keyword: estrategia multimodelo
Secondary keywords: trampa de los tokens, lock-in de IA, riesgo de proveedor único, model routing, IA soberana, coste de inferencia
Canonical: https://zoopa.es/es/innovacion-tecnologia/trampa-tokens-riesgo-proveedor-unico-estrategia-multimodelo/
Category: Innovación y Tecnología (2237), GEO, IA y Visibilidad en Buscadores de IA (2231)
Tags: estrategia multimodelo, lock-in, tokens, model routing, IA soberana, coste de inferencia, LLM, resiliencia
-->

# La trampa de los tokens: depender de un solo proveedor de IA es un riesgo financiero

<figure style="margin: 24px 0 40px 0;">
  <img src="https://zoopa.es/wp-content/uploads/2026/06/trampa-tokens-estrategia-multimodelo-placeholder.jpg" alt="Ilustración de la trampa de los tokens: el precio por token cae mientras la factura total sube, y una arquitectura multimodelo enruta cada tarea al modelo adecuado con fallback entre proveedores" style="width: 100%; height: auto; border-radius: 4px; display: block;" />
  <figcaption style="font-size: 0.9em; color: #64748b; text-align: center; margin-top: 12px; font-style: italic;">El precio por token se desploma y la factura sube a la vez. La defensa estructural no es negociar precio, es no depender de un solo proveedor.</figcaption>
</figure>
<!-- IMAGEN: reemplazar el src placeholder por la featured image real antes de publicar, o asignar featured_media por API. -->

**La IA nunca ha sido tan barata. Por eso tu factura nunca ha sido tan cara.**

Las dos frases son verdad a la vez y no se cancelan. Esa es la trampa de los tokens: el precio por token se desploma mes a mes, y aun así el coste de operar sube. Pero el coste ni siquiera es el mayor problema. El mayor problema es de quién depende ese coste.

Vamos con la conclusión antes que con el rodeo: la trampa es real, pero es asimétrica. El precio por unidad de capacidad cae a ritmo histórico, y aun así el coste de operar sube, porque cada mejora de los modelos quema muchos más tokens. Y mientras tanto, quien construye su producto sobre un único modelo de un único proveedor acumula un riesgo que no aparece en ninguna factura: el de que ese proveedor decida por ti el precio, la continuidad y el consumo. La respuesta estructural, ya avalada por Gartner y operativa en producción, es la arquitectura multimodelo. El resto de este artículo explica por qué, y qué hacer.

<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 24px; margin: 48px 0; padding: 32px; background: linear-gradient(135deg, #0d9488 0%, #1a365d 100%); border-radius: 6px; color: #fff;">
  <div style="text-align: center;">
    <div style="font-size: 3.4em; font-weight: 800; line-height: 1; margin-bottom: 8px;">150x</div>
    <div style="font-size: 0.95em; opacity: 0.9; line-height: 1.4;">cayó el precio por token entre GPT-4 y GPT-4o, según Altman</div>
  </div>
  <div style="text-align: center;">
    <div style="font-size: 3.4em; font-weight: 800; line-height: 1; margin-bottom: 8px;">3x a 18x</div>
    <div style="font-size: 0.95em; opacity: 0.9; line-height: 1.4;">sube al año el coste absoluto de operar modelos en frontera</div>
  </div>
  <div style="text-align: center;">
    <div style="font-size: 3.4em; font-weight: 800; line-height: 1; margin-bottom: 8px;">85%</div>
    <div style="font-size: 0.95em; opacity: 0.9; line-height: 1.4;">de ahorro enrutando entre modelos, reteniendo el 95% del rendimiento</div>
  </div>
</div>
<p style="font-size: 0.85em; color: #64748b; text-align: center; margin: -32px 0 40px 0;">Fuentes: Sam Altman, "Three Observations" · The Price of Progress (MIT/Epoch, arXiv 2511.23455) · RouteLLM (LMSYS / UC Berkeley)</p>

<div style="background: linear-gradient(135deg, #ebf8ff 0%, #f0fff4 100%); border-left: 4px solid #0d9488; border-radius: 0 8px 8px 0; padding: 24px 28px; margin: 2em 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <h3 style="margin: 0 0 16px 0; font-size: 1.1em; font-weight: 700; color: #1a365d; letter-spacing: 0.01em;">Lo que necesitas saber</h3>
  <ul style="margin: 0; padding-left: 20px; line-height: 1.8; color: #2d3748;">
    <li style="margin-bottom: 8px;"><strong>El precio cae, pero tu factura sube.</strong> El precio por capacidad equivalente baja entre 5x y 10x al año. A la vez, el coste de operar en frontera sube entre 3x y 18x al año, porque los modelos de razonamiento y los agentes queman muchos más tokens.</li>
    <li style="margin-bottom: 8px;"><strong>El lock-in dejó de ser teoría.</strong> En enero de 2026 OpenAI retiró GPT-4o y otros modelos de ChatGPT por decisión unilateral. El proveedor controla el ciclo de vida del modelo del que dependes.</li>
    <li style="margin-bottom: 8px;"><strong>El precio de hoy puede estar subsidiado.</strong> Sequoia cifró en 600.000 millones de dólares el hueco entre la inversión en IA y los ingresos que la justifican. Si el precio actual no es rentable para el proveedor, tu margen de mañana depende de decisiones ajenas.</li>
    <li style="margin-bottom: 8px;"><strong>La métrica correcta no es el precio por token.</strong> Es la relación entre la calidad del output y su coste. Medir productividad por tokens consumidos solo le conviene a quien vende tokens.</li>
    <li style="margin-bottom: 8px;"><strong>La defensa es arquitectura, no negociación.</strong> Enrutar cada tarea al modelo adecuado, con fallback entre proveedores y opción soberana, da resiliencia y eficiencia en una sola decisión de diseño.</li>
  </ul>
</div>

## Las dos verdades que conviven

La conversación de mercado se quedó con el titular fácil: "la IA es cada vez más barata". Es cierto por token y engañoso por negocio. Para entender la trampa hay que sostener dos hechos a la vez.

**Por unidad, la IA se abarata a un ritmo sin precedentes.** El precio para alcanzar un nivel de rendimiento dado cae entre 5x y 10x al año, según el paper de referencia *The Price of Progress* (MIT y Epoch AI). Los datos primarios de Epoch lo afinan: la mediana es de 50x al año, y filtrando solo lo posterior a enero de 2024 sube a 200x. Tres voces de máxima autoridad convergen en la misma cifra redonda. Guido Appenzeller (a16z) lo bautizó "LLMflation" y resume: "el coste de la inferencia ha caído un factor de 1.000 en tres años". Sam Altman lo cifra en un 10x cada doce meses, con un 150x concreto entre GPT-4 y GPT-4o. Ethan Mollick (Wharton): "cuando salió GPT-4 costaba unos 50 dólares trabajar con un millón de tokens; ahora cuesta unos 14 centavos".

**Y aun así el coste por tarea sube.** Aquí está la trampa, y el mismo paper la nombra sin rodeos: el coste absoluto de operar modelos en frontera sube entre 3x y 18x al año, porque cada mejora marginal de rendimiento exige sustancialmente más inferencia. El mecanismo tiene nombre: consumo de tokens. Un modelo agéntico gasta entre 5 y 30 veces más tokens por tarea que un chatbot estándar, según Gartner. En código agéntico, Microsoft Research mide hasta 1.000 veces más tokens que un chat de código. Y el consumo es estocástico: la misma tarea ejecutada dos veces puede diferir hasta 30x en tokens totales. Más tokens no significa más precisión.

Gartner lo resume sin piedad: hacia 2030 la inferencia costará a los proveedores más de un 90% menos que en 2025, pero ese ahorro no llegará al cliente, porque el consumo crece más rápido de lo que cae el precio.

<blockquote style="border-left: 4px solid #0d9488; margin: 40px 0; padding: 24px 32px; background: #f8fafc; font-size: 1.35em; line-height: 1.5; color: #1a365d; font-style: italic; font-weight: 500;">
  El precio por token seguirá cayendo y será una distracción. La variable que decide tu margen hacia 2030 es el consumo, no el precio unitario.
</blockquote>

## El lock-in dejó de ser teoría

Hasta aquí, todo es cuestión de coste. La parte que casi nadie presupuesta es la de control. Quien construye un producto, un servicio o un flujo de trabajo sobre un único modelo de un único proveedor firma tres cheques en blanco a la vez.

1. **Cheque de precio.** Aceptas el pricing que el proveedor fije mañana.
2. **Cheque de continuidad.** Aceptas que el modelo siga existiendo.
3. **Cheque de consumo.** Aceptas que cada mejora de capacidad multiplique los tokens que pagas.

El cheque de continuidad ya tiene víctimas. El 29 de enero de 2026 OpenAI anunció la retirada de GPT-4o, GPT-4.1, GPT-4.1 mini y o4-mini de ChatGPT, efectiva dos semanas después. La justificación oficial: solo el 0,1% de usuarios seguía eligiendo GPT-4o a diario tras la migración a GPT-5.2. El movimiento #keep4o reunió 21.000 firmas. No cambió nada.

La lección no es sobre GPT-4o. Es sobre quién decide. El proveedor poda los modelos de bajo uso aunque una minoría dependa de ellos en producción. Si tu prompt engineering, tus evaluaciones y tu producto están calibrados sobre un modelo concreto, su retirada es tu problema, no el suyo. Conviene un matiz honesto: esta retirada aplicó a la interfaz de ChatGPT, no a la API, que "no cambia por ahora". Pero el patrón de migración forzada es el que importa.

Andrej Karpathy le puso nombre al riesgo de fondo. Cuando los grandes modelos caen, dice, es "como un apagón de inteligencia en el mundo: el planeta se vuelve más tonto cuanto más dependemos de estos modelos". Su marco es preciso: los LLM "tienen ahora propiedades de servicios públicos", como la electricidad o el agua. Depender de una sola utility, sin alternativa, es el riesgo.

## Dependes de una economía que todavía pierde dinero

Hay un segundo coste, más especulativo pero igual de relevante para tu presupuesto: dependes de un mercado cuyas cuentas aún no cierran. David Cahn, de Sequoia Capital, planteó en 2024 el cálculo más citado del sector y lo tituló "la pregunta de los 600.000 millones": el hueco entre lo invertido en infraestructura de IA y los ingresos que deberían justificarlo. Cahn no es un agorero, lo dice con calma: "las fiebres especulativas son parte de la tecnología; quien mantenga la cabeza fría tendrá la oportunidad de construir empresas importantes".

La evidencia verificada confirma la caída de precios y las deprecaciones de modelos. No confirma las economías internas de los laboratorios, pero las señales contextuales apuntan en una dirección incómoda: un usuario de pago a 200 dólares al mes puede llegar a consumir tokens por valor de 5.000, y a los inversores de los grandes labs se les pide "aguantar unos años más". La pregunta de negocio es la misma en el escenario optimista (los modelos se commoditizan y el precio baja) y en el pesimista (consolidación y subida de precios): si el precio actual está subsidiado por capital de riesgo, ¿qué le pasa a tu margen cuando los labs tengan que ser rentables?

<blockquote style="border-left: 4px solid #0d9488; margin: 40px 0; padding: 24px 32px; background: #f8fafc; font-size: 1.35em; line-height: 1.5; color: #1a365d; font-style: italic; font-weight: 500;">
  Construir sobre un solo modelo de un solo proveedor es firmar tres cheques en blanco a la vez: el de precio, el de continuidad y el de consumo.
</blockquote>

## La respuesta: estrategia multimodelo

La buena noticia es que la defensa no es esperar a que el mercado se estabilice ni renegociar tarifas. Es una decisión de arquitectura, y ya está validada por el analista de referencia. Gartner, en marzo de 2026, lo dice sin ambigüedad: "el valor se acumulará en las plataformas capaces de orquestar cargas a través de un portfolio diverso de modelos. Las tareas rutinarias de alta frecuencia deben enrutarse a modelos pequeños y de dominio específico. La inferencia cara de los modelos frontera debe estar fuertemente restringida y reservada para razonamiento complejo de alto margen".

Eso es exactamente el enfoque que aplicamos en Zoopa: agentes que distribuyen las tareas entre modelos, eligiendo el adecuado por coste y capacidad, con fallbacks entre proveedores. Y el ahorro está cuantificado. RouteLLM, de LMSYS y UC Berkeley, enruta entre un modelo fuerte y uno débil según la complejidad del prompt: ahorra más del 85% en el benchmark MT Bench reteniendo el 95% del rendimiento de GPT-4. En MMLU el ahorro es del 45% y en GSM8K del 35%. El 85% es el caso más favorable, no la media, pero incluso el suelo de ese rango cambia la economía de operar IA a escala.

No hay que construir el enrutamiento desde cero. Las herramientas de producción ya existen: el Auto Router de OpenRouter selecciona el modelo de un pool curado según la complejidad, con un parámetro explícito de tradeoff coste-calidad; LiteLLM, open source y self-hostable, es un gateway a más de 100 APIs con fallback automático en cadena ordenada entre proveedores; y el propio RouteLLM es código abierto.

### La arquitectura sostenible, en cuatro capas

1. **Clasificación de la tarea.** Cada petición se etiqueta por complejidad antes de tocar un modelo.
2. **Enrutamiento por coste y capacidad.** Las tareas triviales van a modelos pequeños; el razonamiento complejo, a frontera, y restringido.
3. **Fallback multiproveedor.** Una cadena ordenada entre laboratorios distintos. Si uno cae, sube de precio o deprecia un modelo, el sistema no se entera.
4. **Opción soberana u open-weight.** Para dato sensible o para desacoplarse del pago por token, modelos self-hosted dentro de la cadena.

Esto es resiliencia (no dependes de un proveedor) más eficiencia (no pagas frontera por tareas triviales) en una sola decisión de diseño.

## Lo que vemos desde la trinchera

> Esta sección está pendiente de casos reales con cliente nombrado. Sin ellos, este bloque es divulgación. Con ellos, es posicionamiento. Rellenar antes de publicar (ver bloque 3 del source).

[EJEMPLO 1: historia real de un proyecto reciente]
Cliente: <cliente o branded content interno, anonimizado si hay NDA>
Tensión: <qué problema de dependencia, coste o continuidad apareció>
Decisión: <qué se hizo: routing por niveles, fallback entre proveedores, opción open-weight, tope de consumo>
Lección: <qué regla se sacó>

[EJEMPLO 2: historia real de un proyecto reciente]
Cliente: <cliente o anonimizado si hay NDA>
Tensión: <qué problema apareció>
Decisión: <qué se hizo>
Lección: <qué regla se sacó>

Lo que sí podemos adelantar como patrón: en los proyectos que tocamos, el riesgo casi nunca se percibe hasta que el proveedor cambia algo. Sube un precio, deprecia un modelo o ajusta una cuota, y de golpe un sistema que funcionaba pasa a depender de una decisión que no tomó nadie del equipo. La arquitectura multimodelo no es una optimización técnica, es la diferencia entre enterarte de ese cambio o no enterarte.

<div style="background: #1a1a1a; color: #fff; padding: 32px; margin: 40px 0; border-radius: 4px; text-align: center;">
  <p style="margin: 0 0 12px 0; font-size: 0.9em; opacity: 0.8; text-transform: uppercase; letter-spacing: 1px;">Estrategia de IA con cabeza</p>
  <p style="margin: 0 0 20px 0; font-size: 1.3em; line-height: 1.4;">Esto es lo que hacemos. Diseñamos sistemas de IA que enrutan cada tarea al modelo adecuado y no dependen de un solo proveedor.</p>
  <a href="https://zoopa.es/es/servicios/estrategia/" style="display: inline-block; background: #fff; color: #1a1a1a; padding: 12px 28px; text-decoration: none; font-weight: 600; border-radius: 2px;">Esto es lo nuestro →</a>
</div>

## Cuándo depender de un solo proveedor suma y cuándo resta

Nada de esto es un alegato contra los grandes laboratorios ni contra los modelos frontera. Son tecnología extraordinaria, y para muchos arranques apostar por un solo proveedor es la decisión correcta. La diferencia entre que sume o reste no está en el proveedor, está en el contexto.

Un solo proveedor suma cuando estás validando una idea, el volumen es bajo, no manejas dato regulado y la velocidad de llegar al mercado pesa más que el margen. En esa fase, montar enrutamiento y fallback es complejidad prematura. Resta cuando el sistema entra en producción a escala, cuando el coste de inferencia empieza a notarse en la cuenta de resultados, cuando manejas datos sujetos a RGPD o a normativa sectorial, o cuando ese modelo se ha vuelto una pieza estructural de tu producto. Ahí, la dependencia deja de ser una comodidad y pasa a ser una exposición. La regla práctica: apoyarte en un proveedor mientras es opcional, diseñar la salida antes de que sea obligatoria.

## IA soberana: la independencia como cobertura de riesgo

La cuarta capa de la arquitectura, la opción soberana, merece un apunte aparte, porque Europa ya decidió que la dependencia de proveedores estadounidenses es un riesgo de Estado, no solo de empresa. Mistral cerró en septiembre de 2025 una Serie C de 1.700 millones de euros con valoración de 11.700 millones, liderada por ASML, y construye sus propios centros de datos para dejar de depender de la nube estadounidense. DeepSeek demostró por la vía del coste que el estado del arte no exige CapEx masivo ni modelos cerrados: el lanzamiento de su modelo R1 borró 600.000 millones de dólares de la capitalización de NVIDIA en un solo día, la mayor caída diaria de una empresa en la historia de Estados Unidos. Ambos publican modelos open-weight, ejecutables en infraestructura propia.

Para una empresa, la soberanía se traduce en una decisión concreta: el self-hosting. Su economía depende del volumen (el punto de equilibrio frente a una API premium ronda los 256 millones de tokens al mes, con la utilización de la GPU como variable crítica), pero hay un caso en que el cálculo de coste deja de importar. Para cargas con datos sujetos a HIPAA, RGPD o SOC2, sin un acuerdo de tratamiento de datos las APIs de consumo no pueden procesar legalmente esa información. Ahí el self-hosting deja de ser una decisión de coste y pasa a ser de jurisdicción. Con el Reglamento Europeo de IA plenamente aplicable desde el 2 de agosto de 2026, esa frontera dejará de ser teórica para muchos sectores.

## Qué hacer si construyes o ya operas con IA

La trampa de los tokens no se desactiva negociando precio. Se desactiva con gobernanza y diseño. Estas son las palancas que de verdad mueven el riesgo y la factura.

1. **Mide la calidad por coste, no el consumo.** El objetivo es el mínimo de tokens para la máxima calidad de salida, no el máximo de tokens para aparentar productividad. Premiar "tokens quemados" subsidia el trabajo inútil.
2. **Clasifica cada tarea antes de elegir modelo.** No mandes una clasificación trivial al modelo más grande. Entre un flagship y un modelo pequeño hay un orden de magnitud de diferencia en precio.
3. **Monta fallback entre proveedores desde el día uno.** Una cadena ordenada entre labs distintos convierte la caída, la subida de precio o la deprecación de un proveedor en un no-evento.
4. **Reserva una opción open-weight para el dato sensible.** Tanto por cumplimiento como para desacoplarte del pago por token en las cargas que lo justifiquen.
5. **Presupuesta sobre el percentil alto.** Como el consumo es estocástico, toma varias ejecuciones de cada tarea representativa y presupuesta sobre el caso malo, no sobre la media. Fija topes de tokens por respuesta y cortes de bucle en los agentes.
6. **Aprovecha el prompt caching.** Reutilizar la parte estable de un prompt baja el coste de input hasta un 90% en algunos proveedores. Es de las optimizaciones de mayor retorno con prompts largos y repetidos.

## Entonces, ¿cuál es la salida?

Volvamos al principio. Por token, la IA es cada vez más barata, y lo seguirá siendo. En agregado, tu factura sube, y lo seguirá haciendo mientras el consumo crezca más rápido que el precio. Pero el coste no es el riesgo más grande. El riesgo más grande es no tener alternativa: depender de un modelo que otro puede encarecer, retirar o saturar sin contar contigo. La estrategia multimodelo resuelve las dos cosas con la misma decisión, porque convierte a cada proveedor en intercambiable. Diseñarla ahora, mientras es opcional, cuesta una fracción de lo que costará improvisarla cuando el margen ya esté comprometido.

<blockquote style="border-left: 4px solid #0d9488; margin: 40px 0; padding: 24px 32px; background: #f8fafc; font-size: 1.35em; line-height: 1.5; color: #1a365d; font-style: italic; font-weight: 500;">
  La sostenibilidad de la estrategia de modelos es ventaja competitiva ahora. Después es supervivencia.
</blockquote>

<div style="background: #000; color: #fff; padding: 36px; margin: 48px 0; border-radius: 4px;">
  <h2 style="margin: 0 0 12px 0; color: #fff; font-size: 1.4em;">Hablemos</h2>
  <p style="margin: 0 0 24px 0; opacity: 0.8; line-height: 1.6;">Si tu producto o tu operación dependen hoy de un solo modelo de un solo proveedor, conviene tener esta conversación antes de que el proveedor decida por ti, no después. Te contamos cómo diseñamos arquitecturas multimodelo en Zoopa y 498A.</p>
  <a href="https://zoopa.es/es/contactanos/" style="display: inline-block; background: #fff; color: #000; padding: 14px 32px; text-decoration: none; font-weight: 600;">Hablemos →</a>
</div>

<div style="margin: 2em 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <h2 style="font-size: 1.3em; color: #1a365d; margin-bottom: 20px; padding-bottom: 10px; border-bottom: 2px solid #0d9488;">Glosario</h2>

  <div style="margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid #edf2f7;">
    <strong style="color: #1a365d; font-size: 1em;">Token</strong>
    <p style="margin: 6px 0 0 0; color: #4a5568; line-height: 1.6; font-size: 0.93em;">Unidad mínima de texto que un modelo procesa y factura. No es una palabra ni una letra, sino un fragmento. Como el modelo predice y cobra token a token, el token es la moneda real de la economía de los LLM. El español consume más tokens por idea que el inglés, porque los tokenizadores se entrenaron sobre todo con inglés.</p>
  </div>

  <div style="margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid #edf2f7;">
    <strong style="color: #1a365d; font-size: 1em;">Inferencia</strong>
    <p style="margin: 6px 0 0 0; color: #4a5568; line-height: 1.6; font-size: 0.93em;">Cada uso de un modelo ya entrenado. El entrenamiento es el coste de capital del proveedor; la inferencia es el coste recurrente que paga el cliente. Toda la trampa de los tokens vive en la inferencia.</p>
  </div>

  <div style="margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid #edf2f7;">
    <strong style="color: #1a365d; font-size: 1em;">Tokens de razonamiento (reasoning tokens)</strong>
    <p style="margin: 6px 0 0 0; color: #4a5568; line-height: 1.6; font-size: 0.93em;">Tokens que un modelo de razonamiento genera "pensando en voz alta" antes de la respuesta final. Suelen ocupar miles por consulta, el usuario no los ve pero sí los paga, y se facturan como salida, la partida cara. Son la causa de que el razonamiento dispare la factura.</p>
  </div>

  <div style="margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid #edf2f7;">
    <strong style="color: #1a365d; font-size: 1em;">Sistema agéntico</strong>
    <p style="margin: 6px 0 0 0; color: #4a5568; line-height: 1.6; font-size: 0.93em;">Patrón en el que el modelo no solo responde, sino que planifica y ejecuta tareas de varios pasos en bucle, usando herramientas. Cada paso reinyecta el contexto acumulado como input, así que el consumo crece de forma no lineal e invisible. Es el mayor amplificador de gasto de tokens.</p>
  </div>

  <div style="margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid #edf2f7;">
    <strong style="color: #1a365d; font-size: 1em;">Model routing (enrutamiento de modelos)</strong>
    <p style="margin: 6px 0 0 0; color: #4a5568; line-height: 1.6; font-size: 0.93em;">Sistema que, ante cada petición, decide automáticamente qué modelo conviene: las simples a un modelo pequeño y barato, las complejas a uno grande. Optimiza coste y calidad sin que el usuario elija. Una de las defensas más efectivas contra la trampa.</p>
  </div>

  <div style="margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid #edf2f7;">
    <strong style="color: #1a365d; font-size: 1em;">Fallback</strong>
    <p style="margin: 6px 0 0 0; color: #4a5568; line-height: 1.6; font-size: 0.93em;">Mecanismo de respaldo: si el modelo o proveedor principal falla, sube de precio o deprecia un modelo, el sistema reintenta automáticamente con una alternativa. Aporta resiliencia frente a la dependencia de un único proveedor.</p>
  </div>

  <div style="margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid #edf2f7;">
    <strong style="color: #1a365d; font-size: 1em;">Open-weight</strong>
    <p style="margin: 6px 0 0 0; color: #4a5568; line-height: 1.6; font-size: 0.93em;">Modelo cuyos pesos se publican y se pueden descargar y ejecutar en infraestructura propia, aunque no necesariamente con datos o licencia plenamente libres. Solo los modelos open-weight u open-source permiten escapar del coste por token alojando el modelo por tu cuenta.</p>
  </div>

  <div style="margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid #edf2f7;">
    <strong style="color: #1a365d; font-size: 1em;">Soberanía de IA</strong>
    <p style="margin: 6px 0 0 0; color: #4a5568; line-height: 1.6; font-size: 0.93em;">Capacidad de una organización o país de controlar su propia infraestructura de IA (modelos, cómputo, datos) sin depender críticamente de terceros extranjeros. Es el principal argumento no económico para el self-hosting y los modelos open-weight.</p>
  </div>
</div>

<div style="margin: 2em 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <h2 style="font-size: 1.3em; color: #1a365d; margin-bottom: 20px; padding-bottom: 10px; border-bottom: 2px solid #0d9488;">Preguntas frecuentes</h2>

  <div style="border-bottom: 1px solid #e2e8f0; padding: 20px 0;">
    <h3 style="margin: 0 0 12px 0; font-size: 1.05em; font-weight: 700; color: #1a365d;">¿Qué es la trampa de los tokens?</h3>
    <p style="margin: 0; color: #4a5568; line-height: 1.7; font-size: 0.95em;">Es la paradoja de que el precio por token cae año tras año mientras la factura total de IA de muchas empresas sube. Ocurre porque los modelos de razonamiento y los agentes consumen muchos más tokens por tarea, así que el consumo crece más rápido de lo que baja el precio unitario.</p>
  </div>

  <div style="border-bottom: 1px solid #e2e8f0; padding: 20px 0;">
    <h3 style="margin: 0 0 12px 0; font-size: 1.05em; font-weight: 700; color: #1a365d;">¿Por qué es un riesgo depender de un solo proveedor de IA?</h3>
    <p style="margin: 0; color: #4a5568; line-height: 1.7; font-size: 0.95em;">Porque el proveedor controla el ciclo de vida del modelo: puede subir el precio, retirar el modelo o cambiar las cuotas sin contar contigo. En enero de 2026 OpenAI retiró GPT-4o de ChatGPT pese a una petición con 21.000 firmas. Si tu producto está calibrado sobre un modelo concreto, su retirada es tu problema.</p>
  </div>

  <div style="border-bottom: 1px solid #e2e8f0; padding: 20px 0;">
    <h3 style="margin: 0 0 12px 0; font-size: 1.05em; font-weight: 700; color: #1a365d;">¿Qué es una estrategia multimodelo?</h3>
    <p style="margin: 0; color: #4a5568; line-height: 1.7; font-size: 0.95em;">Es una arquitectura que enruta cada tarea al modelo más adecuado por coste y capacidad, con fallback automático entre proveedores y una opción de modelo soberano u open-weight para el dato sensible. Da resiliencia frente a la dependencia y eficiencia frente al sobrecoste en una sola decisión de diseño. Gartner la avala como el enfoque donde se acumulará el valor.</p>
  </div>

  <div style="border-bottom: 1px solid #e2e8f0; padding: 20px 0;">
    <h3 style="margin: 0 0 12px 0; font-size: 1.05em; font-weight: 700; color: #1a365d;">¿Cuánto se ahorra enrutando entre modelos?</h3>
    <p style="margin: 0; color: #4a5568; line-height: 1.7; font-size: 0.95em;">RouteLLM, de LMSYS y UC Berkeley, documenta hasta un 85% de ahorro reteniendo el 95% del rendimiento de GPT-4 en su benchmark más favorable. En otros benchmarks el ahorro es del 45% y del 35%. La cifra exacta depende mucho de la tarea, pero incluso el suelo del rango cambia la economía de operar IA a escala.</p>
  </div>

  <div style="border-bottom: 1px solid #e2e8f0; padding: 20px 0;">
    <h3 style="margin: 0 0 12px 0; font-size: 1.05em; font-weight: 700; color: #1a365d;">¿Cuándo compensa el self-hosting de un modelo open-weight?</h3>
    <p style="margin: 0; color: #4a5568; line-height: 1.7; font-size: 0.95em;">Por coste, a partir de un volumen alto (el punto de equilibrio frente a una API premium ronda los 256 millones de tokens al mes, con la utilización de la GPU como factor crítico). Pero para datos sujetos a RGPD, HIPAA o SOC2 sin acuerdo de tratamiento, el self-hosting puede ser la única vía conforme, y entonces la decisión deja de ser de coste y pasa a ser de jurisdicción.</p>
  </div>

  <div style="border-bottom: 1px solid #e2e8f0; padding: 20px 0;">
    <h3 style="margin: 0 0 12px 0; font-size: 1.05em; font-weight: 700; color: #1a365d;">¿Hay que construir el enrutamiento desde cero?</h3>
    <p style="margin: 0; color: #4a5568; line-height: 1.7; font-size: 0.95em;">No. Las herramientas de producción ya existen: el Auto Router de OpenRouter selecciona el modelo de un pool curado según la complejidad, y LiteLLM (open source y self-hostable) es un gateway a más de 100 APIs con fallback automático en cadena entre proveedores. El propio RouteLLM también es código abierto.</p>
  </div>
</div>
