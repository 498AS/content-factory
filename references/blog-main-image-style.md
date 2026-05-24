# Estilo canonico de imagenes principales (blog Carlos Ortet)

> Referencia oficial para generar imagenes "main" y "secondary" de blog posts en el sistema content-factory. Establecido visualmente en el proyecto `project_09052026_siguiente-bestia` (mayo 2026). Este estilo es el gold standard.

## Indice

1. Descripcion del estilo canonico
2. Paleta de colores exacta
3. Personaje + props
4. Prompt template para Nano Banana
5. Dimensiones requeridas
6. Post procesamiento (crop del watermark)
7. Anti patron (que NO es el estilo)
8. Caso de uso correcto

---

## 1. Descripcion del estilo canonico

El estilo establecido para imagenes principales de los blog posts de Carlos Ortet es una ilustracion **flat editorial** (estilo vector plano, sin gradientes complejos) con un tono **juguetón pero profesional**, que mezcla:

- Estetica de revista digital tipo Quanta Magazine, Wired Ideas, MIT Tech Review opinion section.
- Personaje recurrente (mascota): un yeti / bestia peluda amistoso con multiples ojos, cara expresiva, melena rubia clara.
- Composicion centrada con el personaje como heroe del encuadre.
- Props relacionados con el tema del articulo (camaras + smartphones para "fama", cartas con conceptos para "ML", instrumentos musicales, etc.).
- Sin texto en la imagen (salvo etiquetas pequeñas tipo "HELLO MY NAME IS" en stickers o titulos de cartas).
- Sin fotografias reales, solo vector flat 2D.
- Sin perspectivas 3D ni isometricas: todo en plano frontal o ligero 3/4.

El proposito de este estilo es transmitir autoria fuerte y reconocible, evitar el cliche del stock photo corporate o la ilustracion isometrica generica de SaaS.

---

## 2. Paleta de colores exacta

| Rol | Color | Hex aproximado |
|-----|-------|----------------|
| Fondo principal | Purpura grape solido | `#6E3A7E` (purpura medio uva) |
| Sombra del fondo | Purpura mas oscuro para vinetas | `#4A2657` |
| Personaje principal | Beige melena rubia | `#F4D9A3` |
| Sombreado personaje | Beige rosado | `#E8B98F` |
| Acento rojo (stickers HELLO) | Rojo brillante | `#E63946` |
| Acento blanco | Off white para dientes, papel | `#FAFAFA` |
| Siluetas oscuras (publico) | Negro purpura | `#2A1530` |
| Cartas / props secundarios | Multi color (azul `#4A90E2`, verde `#7CB342`, naranja `#FF9933`) |

**Regla**: el fondo siempre es un purpura grape solido (`#6E3A7E` o muy similar). Es el color firma del estilo. NO usar otros backgrounds (no azul, no negro, no blanco). Es lo que hace reconocibles las imagenes a primera vista.

---

## 3. Personaje + props

### Mascota principal: "La bestia" (yeti amistoso)

Caracteristicas fijas:
- Cuerpo peludo, melena larga rubia clara cubriendo gran parte del torso.
- Multiples ojos pequeños redondos blancos con pupila negra (entre 2 y 4 ojos visibles, dispone en triangulo o linea).
- Boca grande sonriente con dientes blancos cuadrados visibles.
- Brazos peludos largos, manos beige rosado de 3 dedos.
- Postura frontal centrada en el encuadre.
- Expresion: alegre, abierta, juguetona. Nunca seria ni amenazante.

### Props variables (segun topic del articulo)

El personaje sostiene o interactua con objetos relacionados al tema:
- Tema "fama / virality" : sticker "HELLO MY NAME IS" + publico con smartphones y camaras grabando.
- Tema "machine learning / modelos": cartas tipo trading cards con conceptos escritos (World models, RL, Neuro symbolic, etc.).
- Tema "musica / creatividad": bateria, micro, instrumentos al lado del personaje.
- Tema "datos / numeros": graficas flotantes, hojas con tablas.
- Tema "ciudades / mobilidad": edificios y trafico simplificados.

### Silueta del publico (opcional)

Cuando el tema es atencion / fama, añadir silueta negra en primer plano de un grupo de personas vistas de espaldas levantando smartphones y camaras. Esa silueta queda recortada como contorno solido negro purpura sin detalle interno.

---

## 4. Prompt template para Nano Banana

Usar este template, sustituyendo `{{TOPIC}}` y opcionalmente `{{PROPS}}`:

```
Editorial flat vector illustration in the style of Quanta Magazine and Wired Ideas opinion section. A friendly fluffy yeti character with multiple small round white eyes (3 to 4 eyes arranged in a triangle on his face), a big happy smile showing square white teeth, long blonde shaggy fur covering most of his body, beige pinkish hands with 3 fingers, centered in the frame, frontal pose. The yeti is interacting with {{PROPS}} that represent the topic of {{TOPIC}}. Solid grape purple background, exact hex #6E3A7E, no gradient, no texture. The illustration is flat 2D vector style, no 3D, no isometric, no photorealism. Color palette is purple #6E3A7E for background, blonde beige #F4D9A3 for the yeti fur, red #E63946 for accent stickers or details, off white #FAFAFA for teeth and paper, with occasional secondary colors (blue, green, orange) only on small props. Friendly and playful but editorial and intelligent tone, like a magazine article hero image. No text overlays except small labels on stickers or cards if relevant. Aspect ratio 16:9, wide horizontal composition. High quality digital illustration, crisp vector lines, clean shapes.
```

### Variantes de `{{PROPS}}` segun topic

| Topic del articulo | PROPS sugeridos |
|--------------------|-----------------|
| Fama, viralidad, atencion | "wearing a HELLO MY NAME IS red sticker on his chest, with a silhouette of a crowd of people in the foreground holding up smartphones and cameras to take pictures of him" |
| Machine learning, modelos IA | "holding a fan of trading cards in his hands, each card showing a different ML concept written on it (World models, RL, Neuro-symbolic, Energy-based models, Program synthesis), the cards have colorful icons" |
| Musica, creatividad | "playing a drum kit beside him, with a microphone stand and guitar leaning nearby" |
| Datos, numeros, analitica | "surrounded by floating bar charts, pie charts and graph papers with simple data visualization" |
| Ciudades, mobilidad, urbanismo | "with simplified flat buildings, traffic lights and a metro icon floating around him" |
| Salud, bienestar | "holding a stethoscope and surrounded by simple medical icons (heart, pill, plus sign)" |
| Finanzas, dinero | "holding stacks of coins and floating dollar / euro symbols, with a simple line chart going up behind him" |
| Tecnologia, gadgets | "surrounded by floating smartphones, laptops and circuit board icons, holding a glowing chip in his hand" |
| Generico / fallback | "holding a magnifying glass and a notebook with question marks floating around him" |

### Notas sobre el prompt

- Mantener TODA la descripcion del personaje (multiples ojos, melena rubia, etc.) constante.
- Solo variar la parte de `{{PROPS}}`.
- Mantener siempre la mencion explicita del hex `#6E3A7E` para el fondo. Nano Banana respeta colores cuando se especifican asi.
- Insistir en "flat 2D vector, no 3D, no isometric" para evitar que el modelo derive a estilos populares de stock SaaS.

---

## 5. Dimensiones requeridas

| Etapa | Resolucion | Ratio |
|-------|------------|-------|
| Generacion bruta (output Nano Banana) | 1920x1080 (o lo mas proximo a 16:9 que devuelva el modelo) | 16:9 |
| Crop final entregable | 1600x900 | 16:9 |
| Version downscaled web ligera (opcional) | 1200x675 | 16:9 |

Nano Banana suele devolver imagenes en proporciones variables segun el prompt. Solicitar 16:9 explicitamente en el texto del prompt, y luego hacer crop al ratio exacto 16:9 en post procesamiento.

---

## 6. Post procesamiento (crop del watermark)

El modelo Gemini (Nano Banana) añade una **marca de agua visible** en forma de estrella de 4 puntas color claro semi transparente en la esquina inferior derecha de cada imagen generada (separada de la marca SynthID invisible).

### Como quitar el watermark

1. La estrella esta dentro de los ultimos 60 a 80 pixeles de la esquina inferior derecha de la imagen.
2. Hacer crop quitando esos pixeles de la parte inferior y derecha.
3. Reescalar al tamaño final 1600x900 manteniendo ratio 16:9.

### Estrategia recomendada

Generar la imagen a una resolucion mas grande de la final (por ejemplo 1920x1080) y luego crop a 1600x900 cortando margenes asimetricos (mas margen inferior y derecho para limpiar el watermark). Esto es lo que hace el script `generate_blog_main_image.py`.

---

## 7. Anti patron: que NO es el estilo

**Ejemplo de anti patron**: la imagen `AI-diplomacy-Tara-Jacoby.jpg` (encontrada en el proyecto AI Chips Economy) NO es el estilo establecido. Esa imagen presenta:

- Vista isometrica 3D de una mesa de reuniones con figuras humanas.
- Paleta azul electrico sobre fondo de circuito impreso verde.
- Estilo tipo cyberpunk / sci fi corporate.
- Sin personaje mascota recurrente.
- Composicion isometrica, no frontal.

Esa imagen es propiedad de la ilustradora Tara Jacoby y se reutilizo en un articulo concreto, pero NO representa el estilo canonico del blog. Si llega un articulo con esa estetica, el sistema content-factory debe generar una version nueva con el estilo canonico del yeti grape purple, no replicar la estetica isometrica azul.

### Senales de que un output esta fuera de estilo

- Fondo azul, negro, blanco o gradiente (debe ser grape purple solido).
- Personajes humanos realistas o stock (debe ser el yeti mascot).
- Perspectiva 3D o isometrica (debe ser flat frontal).
- Fotografia o render fotorrealista (debe ser vector flat).
- Tipografia grande en la imagen (debe limitarse a stickers pequeños).

---

## 8. Caso de uso correcto (gold standard)

El proyecto `project_09052026_siguiente-bestia` es la referencia gold standard del estilo. Sus assets canonicos:

- `assets/main.png` (2816x1536, articulo "La siguiente bestia"): yeti con sticker HELLO MY NAME IS rodeado de publico que le hace fotos.
- `assets/secondary.png` (2816x1536, mismo articulo): yeti tocando bateria con cartas ML en la mano.
- `assets/main_1600.png` y `assets/secondary_1600.png`: versiones reescaladas a 1600x872 para web.

Cualquier nueva imagen principal de blog debe poderse colocar junto a estas dos sin ruptura visual evidente. Si rompe la consistencia, hay que regenerar.

---

## Referencias cruzadas

- Script generador automatico: `/Users/cop/.claude/skills/content-factory/scripts/generate_blog_main_image.py`
- Skill subyacente: `/Users/cop/.claude/skills/imagen/SKILL.md`
- Reglas ortograficas globales: `/Users/cop/.claude/skills/content-factory/references/orthography-rules.md`
