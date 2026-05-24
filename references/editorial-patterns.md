# Editorial Patterns — recursos que separan posicionamiento de divulgación

> Estos patrones son **opcionales pero recomendados**. Aplicar al menos 2 de 4 en cada blog post hace la diferencia entre "post genérico del sector" y "post de Zoopa que se cita".

Validados en producción en el post TV-oscura-dialogos (mayo 2026).

---

## Pattern 1 — Killer line + Pull quote

**Qué es:** una sola frase de 15-25 palabras tan potente que alguien la recortaría como cita en LinkedIn.

**Cómo construirla:** debe ser **autocontenida** (entiende sin contexto), **memorable** (analogía concreta o paradoja), y **defensiva del posicionamiento** (no reformula lo evidente).

**Ejemplos reales (TV oscura):**

> *"En el mundo real, salvo en momentos de pánico, no vemos con efecto túnel ni tenemos los diálogos enterrados bajo la banda sonora."*

> *"La realidad no la vemos con un transfoco."*

**Reglas:**
- 1 killer line por blog (excepcionalmente 2)
- Aislar tipográficamente con `<blockquote>` estilizado (ver componente "Pull-quote blockquote" en `blog-html-components.md`)
- Repetir la línea en derivados: LinkedIn lo cita textual, X la pone en tweet 7 del hilo, Substack la cita como cierre

**Cómo pedirla en el system prompt:**

> *"Identifica 1 frase de 15-25 palabras del contenido que sea citable de forma autónoma. Trátala como pull-quote en el blog (HTML blockquote estilizado) y reusala textualmente en LinkedIn, X, Threads y Substack como anchor compartible."*

---

## Pattern 2 — La paradoja explícita

**Qué es:** nombrar la contradicción interna de un sector, fenómeno o práctica. Cuando hay tensión real en algo y nadie la dice, decirla te da posicionamiento.

**Estructura:**

1. Observación A
2. Observación B (contradictoria con A)
3. Síntesis: *"todo tiene que parecer lo que no es"* o equivalente

**Ejemplo (TV oscura):**

> *"La IA generativa ha popularizado un tipo de imagen que los realizadores humanos están imitando. No porque quieran que su pieza parezca IA, sino porque es tendencia. Mientras tanto, cualquier producción que efectivamente se hace con IA recibe la presión inversa: parecer lo menos sintética posible. **El resultado es una encrucijada donde todo tiene que parecer lo que no es.**"*

**Cuándo aplicar:** cuando el ángulo del proyecto identifica una **decisión sectorial cuestionable**. Si el post es divulgación neutra (ej: "5 trends de 2026"), no hay paradoja → no forzar.

**Cómo pedirla en el system prompt:**

> *"Si el ángulo del usuario identifica una práctica sectorial cuestionable, busca la paradoja: ¿qué dos cosas opuestas están pasando a la vez en el sector? Nómbrala explícitamente con una frase concentrada (ej: 'todo tiene que parecer lo que no es')."*

---

## Pattern 3 — "Cuándo X suma y cuándo X resta" (disclaimer de honestidad)

**Qué es:** un mini-bloque (subsección H3 o párrafo) que matiza la tesis principal. Reconoce el valor legítimo de la práctica criticada antes de criticarla a fondo.

**Por qué es crítico:** sin él, el post parece anti-arte / radical / poco serio. Con él, suena adulto y técnicamente honesto.

**Ejemplo (TV oscura):**

> *"### Cuándo el desenfoque suma y cuándo resta*
>
> *El desenfoque selectivo es una herramienta poderosa cuando se usa para guiar la mirada del espectador hacia algo específico — un rostro, un detalle, una emoción. Suma cuando ayuda a entender la escena. Resta cuando se convierte en estética por defecto, cuando todo el plano está borroso menos un punto. Suma cuando es una decisión. Resta cuando es un reflejo."*

**Cuándo aplicar:** siempre que la tesis principal sea "esta práctica de la industria es un error". Sin matizar, el post pierde credibilidad.

**Cómo pedirla en el system prompt:**

> *"Si la tesis ataca una práctica sectorial, incluir una subsección 'Cuándo X suma y cuándo resta' (donde X es la práctica) que matice. Estructura: cuándo es decisión deliberada y útil vs cuándo es reflejo/moda contraproducente. Esto inmuniza el resto del post contra el reproche de absolutismo."*

---

## Pattern 4 — Caso real con cliente nombrado

**Qué es:** una anécdota concreta con un cliente real (con o sin nombre real, según NDA). Lo que vivió la productora/agencia y la lección sacada.

**Por qué funciona:** convierte el post de divulgación en posicionamiento. La autoridad no la dan los datos de Variety — la da la firma "esto lo vivimos con [cliente]".

**Ejemplos reales (TV oscura):**

- *"Producimos para la productora de Carles Porta una serie de True Crime..."* (caso 1)
- *"Trabajamos con PortAventura. En una pieza sobre la Shambala..."* (caso 2)

**Reglas:**

- 1-2 casos por post (no más, satura)
- Cada caso necesita **tensión** (problema concreto), **decisión** (qué se hizo), **lección** (regla extraída)
- Si hay NDA, pedir al usuario un anonimizado pero específico ("un proyecto reciente para una marca de gran consumo")
- Siempre preguntar al usuario en PASO 1: *"¿Tienes 1-2 anécdotas reales con clientes nombrados?"* (ver `content-brief-structure.md` bloque 3)

**Cómo pedirla en el system prompt:**

> *"En la sección 'Lo que vemos desde la trinchera' (o equivalente), incluir uno o dos casos reales con clientes nombrados que el usuario haya proporcionado en el bloque 3 del source.md. Cada caso debe seguir la estructura: tensión → decisión → lección. Si el usuario no proporcionó casos, dejar placeholder visible y avisar."*

---

## Bonus — Stat block de cifras

**Qué es:** dos o tres cifras grandes destacadas en bloque visual. Ver componente "Stat block 2-column" en `blog-html-components.md`.

**Cuándo aplicar:** si el bloque 2 (hechos curados) del `source.md` tiene cifras de impacto (porcentajes, frecuencias, volúmenes), promocionar 2-3 al bloque visual destacado al inicio del post.

**Ejemplo (TV oscura):** el "50% / 59%" (50% del público en EE.UU. usa subtítulos / 59% en Gen Z) en bloque gradiente teal-marino al inicio.

**Cómo pedirlo:** *"Si el source.md contiene 2-3 cifras de alto impacto, generar un stat block visual al inicio del cuerpo del blog usando el componente HTML 'Stat block 2-column gradient'."*

---

## Cómo combinarlos en un post

Aplicación recomendada para un blog post de 2.000+ palabras:

1. **Hook intro** + introduce las cifras de impacto (las del stat block)
2. **Stat block** visual con 2-3 cifras
3. **Key takeaways** (componente HTML)
4. Cuerpo del análisis
5. **Pattern 2 — Paradoja** explícita en una sección destacada
6. **Pattern 4 — Caso real** con cliente nombrado (sección "Lo que vemos desde la trinchera")
7. **Pattern 3 — Disclaimer "cuándo X suma y cuándo resta"** como subsección que matiza
8. Recomendaciones prácticas
9. **Pattern 1 — Killer line** aislado en pull-quote, antes del CTA final
10. CTA final
11. Glosario + FAQ

No todos los posts usan los 4 patterns. **Mínimo recomendado: 2 de 4** (siempre el caso real + uno más). Mejor calidad: los 4.

---

*Patrones extraídos del trabajo en TV-oscura-dialogos (Zoopa, mayo 2026). Owner: Carlos Ortet.*
