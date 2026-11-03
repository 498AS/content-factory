---
tipo: articulo
slug: los-tres-lectores-de-ia-de-tu-web
lang: es
titulo: "Tu web tiene tres lectores de IA y ninguno ve la misma página"
titulo_h1: "Tu web tiene tres lectores de IA. Y *ninguno* ve la misma página."
descripcion: "Crawlers, Google y agentes leen tu web por canales distintos. Uno la mira como píxeles y, pasada cierta densidad, empieza a adivinar."
entradilla: "Auditamos cómo los modelos describen una marca por el canal de texto. El tercer lector, el agente que mira la página como imagen, todavía no lo audita nadie."
categoria: Método
fecha: 2026-09-27
autor: Carlos Ortet
rol_autor: "Cofundador y CEO de 498 Advance"
bio_autor: "Dirige 498A, el laboratorio de IA aplicada del grupo Zoopa, y GEORadar. Profesor invitado en la UAB, donde dirige trabajos de máster en IA con el IIIA-CSIC."
canonical: https://carlosortet.com/blog/como-leen-los-llms-el-texto-como-imagen
conclusiones:
  - "Ningún crawler de IA ejecuta JavaScript a mediados de 2026. GPTBot descarga ficheros JS el 11,5 % de las veces y ClaudeBot el 23,8 %, y ninguno los ejecuta."
  - "Por debajo de una compresión de 10x, un lector de visión decodifica una página al 97 % de precisión. A 20x cae al 60 %, según DeepSeek-OCR (octubre de 2025)."
  - "En recuperación documental, hacer embedding de la imagen de la página bate al pipeline clásico de extraer y trocear: 0,81 contra 0,66 de NDCG@5, e indexa en 0,39 segundos en lugar de 7,22."
fuentes:
  - "Text or Pixels? It Takes Half. arXiv 2510.18279, octubre de 2025. https://arxiv.org/abs/2510.18279"
  - "DeepSeek-OCR: compresión óptica de contextos. arXiv 2510.18234, octubre de 2025. https://arxiv.org/abs/2510.18234"
  - "ColPali: Efficient Document Retrieval with Vision Language Models. ICLR 2025, arXiv 2407.01449. https://arxiv.org/abs/2407.01449"
  - "Vercel. The rise of the AI crawler: análisis de tráfico de producción. https://vercel.com/blog/the-rise-of-the-ai-crawler"
faq:
  - pregunta: "¿Los crawlers de IA ejecutan JavaScript?"
    respuesta: "No. Ni los de entrenamiento como GPTBot y ClaudeBot, ni los de índice de búsqueda, ni los fetchers en vivo disparados por el usuario. Recogen el HTML servido y siguen. La excepción es Google: Gemini y AI Overviews heredan la infraestructura de Googlebot, que sí renderiza."
  - pregunta: "¿Por qué mi marca aparece en AI Overviews pero no en las respuestas de ChatGPT?"
    respuesta: "Suele ser dependencia de JavaScript. Google renderiza tu página y ve el contenido; ChatGPT, Claude y Perplexity leen el HTML crudo y no lo ven. Una visibilidad decente en AI Overviews no demuestra nada sobre las otras superficies: hay que auditarlas por separado."
  - pregunta: "¿Qué es el tercer lector de una web?"
    respuesta: "El navegador agéntico: Atlas de OpenAI o Comet de Perplexity. Lee la página renderizada mezclando el árbol de accesibilidad, el DOM y capturas enviadas a un modelo de visión. Es el único de los tres que ve tu layout, y el que se degrada si la página es densa."
---

Cuando una marca nos pregunta por qué no aparece en las respuestas de ChatGPT, la primera hipótesis suele ser el modelo. Casi nunca lo es. El problema está antes: en qué parte de la página llega a leerse, y por qué canal.

Porque una web no tiene un lector de IA. Tiene tres, y no se ponen de acuerdo.

## Tres lectores, tres versiones de la misma página

Cada empresa de IA lanza tres familias de bots contra un dominio, y cada familia hace un trabajo distinto.

| Lector | Quién es | Qué ve | Ejecuta JS |
|---|---|---|---|
| **Crawler** | GPTBot, ClaudeBot, OAI-SearchBot, ChatGPT-User, Perplexity-User | El HTML servido, tal cual | No |
| **Google** | Googlebot, y detrás Gemini y AI Overviews | La página renderizada | Sí |
| **Agente** | Atlas de OpenAI, Comet de Perplexity | Árbol de accesibilidad, DOM y capturas a un modelo de visión | Sí |
: Los tres lectores de IA de una web, y por qué canal entra cada uno

El dato que ordena la primera fila es del análisis de tráfico de producción de Vercel: GPTBot descarga ficheros JavaScript alrededor del 11,5 % de las veces y ClaudeBot el 23,8 %, y ninguno de los dos los ejecuta. Sin segunda pasada y sin cola de renderizado. Si la sustancia de una página solo existe en el DOM después del renderizado en cliente, para dos de los tres lectores no existe.

La consecuencia práctica es incómoda: la misma página puede ser perfectamente visible para las superficies de IA de Google e invisible para ChatGPT, Claude y Perplexity a la vez.

:::callout
Una buena visibilidad en AI Overviews no demuestra nada sobre ChatGPT. Google renderiza tu JavaScript y los demás no.
:::

## El tercer lector se degrada, y avisa mal

El agente es el único que ve el layout, y eso lo hace el más interesante y el más frágil de los tres.

Dos papers de octubre de 2025 fijaron la economía de leer texto como imagen. Renderizar texto largo como imagen comprime alrededor de 2:1 manteniendo la precisión a menos de tres puntos del texto plano. Y DeepSeek-OCR cartografió el límite: mientras la ratio entre tokens de texto y tokens de visión se mantiene por debajo de 10x, la precisión de decodificación aguanta en el 97 %; forzada a 20x, cae al 60 %.

Esa curva es la que aplica cuando un navegador agéntico mira una página de marca. Una página limpia y bien jerarquizada se lee cerca del 97 %. Una página densa, recargada y de bajo contraste resbala hacia el extremo del 60 %, y ahí el modelo no se calla: rellena los huecos con suposiciones seguras de sí mismas. Un precio mal leído desde una captura falla igual que un hash mal recordado, en silencio y con confianza.

![Rejilla editorial con la misma información servida en tres densidades distintas](/assets/visuals/blog-figure.jpg)
: La estructura visual es información, no decoración · Fuente: 498A, septiembre de 2026

Hay un cuarto patrón en el lado de la recuperación que apunta a lo mismo. ColPali demostró que, para búsqueda documental, saltarse el OCR y hacer embedding directo de la imagen de la página bate al pipeline clásico de extraer y trocear: 0,81 contra 0,66 de NDCG@5, indexando en 0,39 segundos por página en lugar de 7,22. El layout, las tablas y las figuras que la extracción de texto destruye llevan significado recuperable.

:::detalle Detalle técnico · por qué los píxeles salen más baratos
Todos los modelos multimodales ponen precio a una imagen según sus dimensiones, no según lo que haya pintado encima. El texto, en cambio, se cobra carácter a carácter. En contenido denso, un carácter sale aproximadamente a un token de texto; ese mismo contenido en una imagen bien compactada sale a unos 3,1 caracteres por token de imagen. Ese hueco es todo el mecanismo, y se mueve sin avisar: cuando subió la resolución nativa máxima de imagen de un proveedor, la misma captura pasó de unos 1.558 tokens a 4.739.
:::

## Qué hacemos con esto en 498A

Nuestras auditorías interrogan a los modelos sobre una marca por el canal de texto, y la capa técnica comprueba qué pueden recoger los crawlers. Eso cubre dos de los tres lectores. El tercero, el agente que mira la página, todavía no lo audita nadie.

Así se reparte hoy el trabajo en el stack:

- **El canal de texto lo mide [GEORadar](/productos/georadar.html)**, con entre 6.000 y 30.000 prompts personalizados por estudio contra las siete superficies que seguimos: ChatGPT, Claude, Gemini, Perplexity, Copilot, AI Overviews y AI Mode de Google.
- **El acceso de los crawlers lo audita GEOdoctor**, el módulo de Agent Experience del [stack](/productos/): bloqueos de CDN, robots.txt, llms.txt, comportamiento de GPTBot, ClaudeBot y PerplexityBot, indexabilidad.
- **El canal de visión es el prototipo**: dar páginas de marca a modelos de visión tal como las ve un navegador agéntico, captura más árbol de accesibilidad, y puntuar qué sobrevive al viaje. Para S.A.M., nuestra máquina de alineamiento semántico, eso extiende la validación a un segundo canal: una afirmación tiene que sobrevivir como texto para el crawler y como píxeles para el agente.

Y un test que cuesta un comando, antes de culpar al modelo: haz `curl` a tu página y busca en la respuesta los datos que te importan. Si no están ahí, dos de tus tres lectores no pueden verlos. Esa comprobación es la mitad del trabajo de [Agent Experience](/#capacidades) que hacemos en cada auditoría.

El alineamiento semántico era una propiedad del copy. Está pasando a ser también una propiedad del layout.
