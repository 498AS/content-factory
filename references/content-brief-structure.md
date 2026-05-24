# Content Brief Structure — el `source.md` que produce buen contenido

> **Regla cero:** `source.md` no es un research dump. Es un **brief curado con tesis**. El 80% de la calidad del output depende de esto.

Esta guía aplica al PASO 1 (preguntas pre-publicación). Antes de generar nada, exigir al usuario que el `source.md` cumple los 3 bloques. Si no, devolver al usuario y pedir que los rellene.

---

## Los tres bloques obligatorios

### Bloque 1 — Tesis (1 párrafo, 60-100 palabras)

**Qué es:** la afirmación central que va a defender el contenido. Una posición clara, no neutral.

**Reglas:**
- Una sola tesis por proyecto
- Toma una posición, no resume "lo que se dice"
- Debe poder discutirse (si alguien podría estar en desacuerdo, vas bien)
- Frases cortas, directas, sin hedging

**Ejemplo (TV oscura, post real Zoopa 2026-05):**

> *"La televisión y las series se ven cada vez más oscuras, más borrosas, y los diálogos se entienden peor — por la misma razón. La industria audiovisual ha tomado en pocos años tres decisiones que reducen la información que llega al espectador. La audiencia ha respondido por su cuenta: subtítulos siempre activados. Es momento de decir lo que se calla en el sector: la industria está cometiendo un error claro."*

**Anti-ejemplo (NO hacer):**

> *"En este artículo vamos a hablar de los problemas que tienen las series modernas con la oscuridad y los diálogos."*

(Esto es índice, no tesis. No defiende nada.)

---

### Bloque 2 — Hechos curados (5-15 bullets con dato + fuente + fecha)

**Qué es:** la materia prima factual citable. Cada bullet es un insight atómico que el modelo puede redistribuir entre piezas.

**Reglas:**
- Cada bullet incluye: **dato concreto + fuente identificable + fecha**
- Datos deben ser auto-contenidos (un LLM los puede citar individualmente)
- 5 bullets mínimo, 15 máximo (más datos = piezas saturadas)
- Mezclar tipos: estadísticas, casos concretos, declaraciones públicas, contextos técnicos

**Ejemplo (TV oscura):**

```
- Encuesta AP-NORC (Estados Unidos, 2024): el 50% de los espectadores
  estadounidenses usa subtítulos al menos parte del tiempo.
- Game of Thrones, S08E03 "The Long Night" (HBO, abril 2019): el director
  de fotografía Fabian Wagner defendió que la serie se vea "como una
  película, en una habitación oscura". (Fuente: IndieWire, 2019)
- 30+ dB de diferencia entre explosión y susurro en mezclas Atmos
  cinematográficas (Fuente: SlashFilm 2024)
```

---

### Bloque 3 — Ángulo de marca (3-5 bullets con anécdotas reales firmadas)

**Qué es:** lo que diferencia el contenido de divulgación genérica. Casos REALES con clientes nombrados, lecciones de oficio, opiniones firmadas.

**Reglas:**
- Anécdotas con **clientes nombrados** (con o sin NDA)
- Lecciones de oficio en primera persona ("nosotros vemos cada semana...")
- Recomendaciones específicas, no genéricas
- 3-5 bullets, no más (saturación = pierde fuerza)

**Ejemplo (TV oscura):**

```
- Producimos para la productora de Carles Porta una serie de True Crime.
  El realizador pide imagen "más cinematográfica". Carles, el director,
  insiste en ser lo más realistas posible. Carles tiene razón: la realidad
  no la vemos con un transfoco.

- Trabajamos con PortAventura. En una pieza sobre la Shambala el cliente
  celebró un plano con bokeh agresivo: "Eso es calidad". Probablemente
  porque una GoPro no consigue ese efecto. Cinematográfico equivale, en
  el código actual, a lo que tu teléfono no puede filmar.

- Nuestra recomendación operativa: pista de diálogo separada con
  normalización LUFS propia, color grading condicional al destino,
  test de visionado en pantallas reales del público (no en los Sony
  del estudio).
```

---

## La pregunta crítica del PASO 1

**Antes de empezar a generar, preguntar al usuario:**

> *"¿Tienes 1-2 anécdotas reales de proyectos con clientes nombrados (con o sin NDA) que ilustren el ángulo? Sin esto el post sale como divulgación; con esto sale como posicionamiento."*

Si dice no, recomendarle parar y volver con material. Si dice "lo añado en breve", capturar como TODO en el `source.md` y bloquear PASO 4 (generación) hasta que esté.

### Plantilla de placeholder

Cuando el usuario aún no tiene anécdotas reales, dejar este placeholder en el bloque 3:

```
[EJEMPLO 1 — historia real de un proyecto reciente]
Cliente: <cliente o "branded content interno">
Tensión: <qué problema apareció>
Decisión: <qué se hizo>
Lección: <qué se sacó>
```

El skill detecta `[EJEMPLO N` y avisa al usuario antes de generar.

---

## Por qué esta estructura funciona

| Bloque | Aporta |
|--------|--------|
| Tesis | Posición clara → contenido con voz, no neutro |
| Hechos curados | Materia prima citable → cada pieza tiene datos distintos sin inventar |
| Ángulo de marca | Autoridad de oficio → posicionamiento, no divulgación |

Sin tesis: el post es resumen del estado del arte. Sin hechos curados: el post inventa o se queda corto. Sin ángulo: el post es publicable en cualquier blog del sector — no posiciona.

**Los tres son no-negociables.** Si falta uno, el output se nota.

---

## Validador automático (opcional)

Si quieres exigir esta estructura programáticamente, el `_system/validators/validate_brief.py` (a crear) puede:

1. Detectar si `source.md` tiene secciones `## 1. Tesis`, `## 2. Hechos curados`, `## 3. Ángulo`
2. Contar bullets en bloque 2 (>=5 obligatorio)
3. Detectar `[EJEMPLO ` placeholders sin rellenar
4. Avisar al PASO 4 si falla

Documentar como TODO si interesa hacerlo.

---

*Patrón validado en proyecto TV-oscura-dialogos (mayo 2026). Owner: Carlos Ortet · Zoopa.*
