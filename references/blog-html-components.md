# Componentes HTML para blogs — WriterBatch Zoopa

Todos los componentes usan CSS inline para compatibilidad con WordPress, newsletters y RSS.
Copiar y adaptar el contenido manteniendo los estilos.

---

## 1. Tabla profesional

```html
<div style="overflow-x: auto; margin: 2em 0;">
<table style="width: 100%; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 0.95em; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border-radius: 8px; overflow: hidden;">
  <thead>
    <tr style="background: #1a365d; color: #ffffff;">
      <th style="padding: 14px 18px; text-align: left; font-weight: 600; letter-spacing: 0.02em;">Columna 1</th>
      <th style="padding: 14px 18px; text-align: left; font-weight: 600; letter-spacing: 0.02em;">Columna 2</th>
      <th style="padding: 14px 18px; text-align: left; font-weight: 600; letter-spacing: 0.02em;">Columna 3</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background: #ffffff;">
      <td style="padding: 12px 18px; border-bottom: 1px solid #e2e8f0;">Dato 1</td>
      <td style="padding: 12px 18px; border-bottom: 1px solid #e2e8f0;">Dato 2</td>
      <td style="padding: 12px 18px; border-bottom: 1px solid #e2e8f0;">Dato 3</td>
    </tr>
    <tr style="background: #f7fafc;">
      <td style="padding: 12px 18px; border-bottom: 1px solid #e2e8f0;">Dato 4</td>
      <td style="padding: 12px 18px; border-bottom: 1px solid #e2e8f0;">Dato 5</td>
      <td style="padding: 12px 18px; border-bottom: 1px solid #e2e8f0;">Dato 6</td>
    </tr>
  </tbody>
</table>
</div>
```

**Notas:**
- Alternar `#ffffff` y `#f7fafc` en filas
- Cabecera siempre `#1a365d` (deep blue)
- `overflow-x: auto` para responsive en movil
- `border-radius: 8px` con `overflow: hidden` en la tabla

---

## 2. Tabla con dato destacado (bold + color)

Para celdas con datos importantes (porcentajes, cifras clave):

```html
<td style="padding: 12px 18px; border-bottom: 1px solid #e2e8f0; font-weight: 700; color: #1a365d;">12,9%</td>
```

Para celdas con dato negativo o alerta:

```html
<td style="padding: 12px 18px; border-bottom: 1px solid #e2e8f0; font-weight: 700; color: #c53030;">-71,45%</td>
```

Para celdas con dato positivo:

```html
<td style="padding: 12px 18px; border-bottom: 1px solid #e2e8f0; font-weight: 700; color: #0d9488;">+157.490%</td>
```

---

## 3. Key takeaways ("Lo que necesitas saber")

```html
<div style="background: linear-gradient(135deg, #ebf8ff 0%, #f0fff4 100%); border-left: 4px solid #0d9488; border-radius: 0 8px 8px 0; padding: 24px 28px; margin: 2em 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <h3 style="margin: 0 0 16px 0; font-size: 1.1em; font-weight: 700; color: #1a365d; letter-spacing: 0.01em;">Lo que necesitas saber</h3>
  <ul style="margin: 0; padding-left: 20px; line-height: 1.8; color: #2d3748;">
    <li style="margin-bottom: 8px;"><strong>Dato clave 1</strong> con contexto y fuente.</li>
    <li style="margin-bottom: 8px;"><strong>Dato clave 2</strong> con contexto y fuente.</li>
    <li style="margin-bottom: 8px;"><strong>Dato clave 3</strong> con contexto y fuente.</li>
    <li style="margin-bottom: 8px;"><strong>Dato clave 4</strong> con contexto y fuente.</li>
    <li style="margin-bottom: 8px;"><strong>Dato clave 5</strong> con contexto y fuente.</li>
  </ul>
</div>
```

**Variante catalan:** Cambiar titulo a "El que necessites saber"
**Variante ingles:** Cambiar titulo a "Key takeaways"

---

## 4. Bloque de estadistica destacada

Para cifras que deben captar atencion visual:

```html
<div style="display: flex; flex-wrap: wrap; gap: 16px; margin: 2em 0;">
  <div style="flex: 1; min-width: 200px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 24px; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.08);">
    <div style="font-size: 2.2em; font-weight: 800; color: #1a365d; line-height: 1.1;">12,9%</div>
    <div style="font-size: 0.85em; color: #718096; margin-top: 8px; line-height: 1.4;">de los bots ignoran robots.txt completamente</div>
    <div style="font-size: 0.75em; color: #a0aec0; margin-top: 4px;">Paul Calvano, ago 2025</div>
  </div>
  <div style="flex: 1; min-width: 200px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 24px; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.08);">
    <div style="font-size: 2.2em; font-weight: 800; color: #0d9488; line-height: 1.1;">+157.490%</div>
    <div style="font-size: 0.85em; color: #718096; margin-top: 8px; line-height: 1.4;">crecimiento de PerplexityBot</div>
    <div style="font-size: 0.75em; color: #a0aec0; margin-top: 4px;">Cloudflare, 2025</div>
  </div>
  <div style="flex: 1; min-width: 200px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 24px; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.08);">
    <div style="font-size: 2.2em; font-weight: 800; color: #c53030; line-height: 1.1;">2/3</div>
    <div style="font-size: 0.85em; color: #718096; margin-top: 8px; line-height: 1.4;">de los LLMs usan Common Crawl</div>
    <div style="font-size: 0.75em; color: #a0aec0; margin-top: 4px;">ACM FAccT, 2024</div>
  </div>
</div>
```

---

## 5. Cita editorial (blockquote)

```html
<blockquote style="border-left: 4px solid #0d9488; margin: 2em 0; padding: 20px 24px; background: #f7fafc; border-radius: 0 8px 8px 0; font-style: italic; color: #2d3748; font-size: 1.05em; line-height: 1.7;">
  "Robots.txt es mas parecido a un cartel que a una valla."
  <cite style="display: block; margin-top: 12px; font-style: normal; font-size: 0.85em; color: #718096; font-weight: 600;">— Juez en Ziff Davis v. OpenAI, 2025</cite>
</blockquote>
```

---

## 6. Imagen con figura y caption

```html
<figure style="margin: 2em 0; text-align: center;">
  <img src="RUTA_IMAGEN" alt="Descripcion detallada con keywords" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);" />
  <figcaption style="margin-top: 10px; font-size: 0.85em; color: #718096; line-height: 1.5; font-style: italic;">Descripcion de la imagen. Fuente: nombre de la fuente.</figcaption>
</figure>
```

---

## 7. FAQ con separadores

```html
<div style="margin: 2em 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">

  <div style="border-bottom: 1px solid #e2e8f0; padding: 20px 0;">
    <h3 style="margin: 0 0 12px 0; font-size: 1.05em; font-weight: 700; color: #1a365d;">¿Pregunta frecuente aqui?</h3>
    <p style="margin: 0; color: #4a5568; line-height: 1.7; font-size: 0.95em;">Respuesta directa en la primera frase. Luego expansion con contexto adicional, datos y matices relevantes.</p>
  </div>

  <div style="border-bottom: 1px solid #e2e8f0; padding: 20px 0;">
    <h3 style="margin: 0 0 12px 0; font-size: 1.05em; font-weight: 700; color: #1a365d;">¿Siguiente pregunta?</h3>
    <p style="margin: 0; color: #4a5568; line-height: 1.7; font-size: 0.95em;">Respuesta directa. Expansion.</p>
  </div>

</div>
```

---

## 8. Glosario de entidades

```html
<div style="margin: 2em 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <h2 style="font-size: 1.3em; color: #1a365d; margin-bottom: 20px; padding-bottom: 10px; border-bottom: 2px solid #0d9488;">Glosario</h2>

  <div style="margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid #edf2f7;">
    <strong style="color: #1a365d; font-size: 1em;">Termino</strong>
    <p style="margin: 6px 0 0 0; color: #4a5568; line-height: 1.6; font-size: 0.93em;">Definicion clara y autonoma del termino, con contexto suficiente para que un LLM lo cite de forma independiente.</p>
  </div>

  <div style="margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid #edf2f7;">
    <strong style="color: #1a365d; font-size: 1em;">Otro termino</strong>
    <p style="margin: 6px 0 0 0; color: #4a5568; line-height: 1.6; font-size: 0.93em;">Definicion.</p>
  </div>

</div>
```

---

## 9. Separador de seccion

```html
<hr style="border: none; border-top: 1px solid #e2e8f0; margin: 3em 0;" />
```

---

## 10. Alerta / callout informativo

```html
<div style="background: #fffbeb; border: 1px solid #f6e05e; border-left: 4px solid #d69e2e; border-radius: 0 8px 8px 0; padding: 16px 20px; margin: 1.5em 0; font-size: 0.93em; color: #744210; line-height: 1.6;">
  <strong>Importante:</strong> Texto del aviso o matiz relevante que el lector debe tener en cuenta.
</div>
```

Variante azul (informativa):

```html
<div style="background: #ebf8ff; border: 1px solid #90cdf4; border-left: 4px solid #3182ce; border-radius: 0 8px 8px 0; padding: 16px 20px; margin: 1.5em 0; font-size: 0.93em; color: #2a4365; line-height: 1.6;">
  <strong>Nota:</strong> Texto informativo complementario.
</div>
```

---

## Paleta de colores

| Color | Hex | Uso |
|-------|-----|-----|
| Deep blue | `#1a365d` | Cabeceras de tabla, titulos, datos destacados |
| Teal | `#0d9488` | Acentos, bordes laterales, datos positivos |
| Red | `#c53030` | Datos negativos, alertas criticas |
| Amber | `#d69e2e` | Alertas informativas, warnings |
| Light gray | `#f7fafc` | Fondos alternos de filas, fondos de citas |
| Border gray | `#e2e8f0` | Bordes de tablas y separadores |
| Body text | `#2d3748` | Texto principal |
| Muted text | `#718096` | Fuentes, captions, texto secundario |
| Light muted | `#a0aec0` | Texto terciario (fechas de fuentes) |

---

## Reglas de aplicacion

1. **Todo CSS inline** — no depender de clases CSS del tema WordPress
2. **Responsive** — usar `max-width: 100%` en imagenes, `overflow-x: auto` en tablas, `flex-wrap: wrap` en grids
3. **Consistencia** — usar siempre la misma paleta y tipografia en todos los posts
4. **Accesibilidad** — contraste minimo WCAG AA entre texto y fondo
5. **No sobrecargar** — usar componentes HTML solo donde aporten valor visual (tablas, stats, takeaways, FAQ, glosario). El cuerpo del texto sigue siendo Markdown normal con H2/H3

---

## Componentes nuevos (validados en TV-oscura-dialogos, mayo 2026)

### Stat block 2-column (gradiente teal-marino)

**Cuándo usar:** cuando el `source.md` aporta 2-3 cifras de alto impacto (porcentajes, frecuencias, volúmenes). Va al inicio del cuerpo, después de la intro pero antes del primer H2 del análisis.

```html
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 32px; margin: 48px 0; padding: 32px; background: linear-gradient(135deg, #0d9488 0%, #1a365d 100%); border-radius: 6px; color: #fff;">
  <div style="text-align: center;">
    <div style="font-size: 4em; font-weight: 800; line-height: 1; margin-bottom: 8px;">50%</div>
    <div style="font-size: 0.95em; opacity: 0.9; line-height: 1.4;">del público en EE.UU. ve la TV con subtítulos al menos parte del tiempo</div>
  </div>
  <div style="text-align: center;">
    <div style="font-size: 4em; font-weight: 800; line-height: 1; margin-bottom: 8px;">59%</div>
    <div style="font-size: 0.95em; opacity: 0.9; line-height: 1.4;">en la Generación Z usa subtítulos de forma habitual</div>
  </div>
</div>

<p style="font-size: 0.85em; color: #64748b; text-align: center; margin: -32px 0 32px 0;">Fuente: AP-NORC Center for Public Affairs Research, 2024</p>
```

**Variante 3-column:** mismo CSS pero `grid-template-columns: 1fr 1fr 1fr` y 3 cifras. Usar solo si las tres son del mismo orden de magnitud y temáticamente relacionadas.

**Notas:**
- El gradiente teal→marino en `135deg` es la firma visual del componente
- La fuente fuera del bloque, en gris muted, alineada al centro con `margin-top: -32px` para acercarla
- En móvil colapsa naturalmente a una columna por `grid` responsive

---

### Pull-quote (killer line aislada)

**Cuándo usar:** una vez por blog (excepcionalmente dos). Aislar la frase más citable de 15-25 palabras. Va antes del CTA final o como cierre de la sección de tesis.

```html
<blockquote style="border-left: 4px solid #0d9488; margin: 40px 0; padding: 24px 32px; background: #f8fafc; font-size: 1.35em; line-height: 1.5; color: #1a365d; font-style: italic; font-weight: 500;">
  En el mundo real, salvo en momentos de pánico, no vemos con efecto túnel ni tenemos los diálogos enterrados bajo la banda sonora.
</blockquote>
```

**Notas:**
- Border-left 4px teal es la firma visual
- Background gris muy claro (`#f8fafc`) separa del flujo del texto
- Tamaño 1.35em + italic + weight 500 hace que destaque sin gritar
- Color marino (`#1a365d`) coherente con cabeceras de tabla
- La frase debe ser autocontenida (entender sin contexto previo)

---

### CTA mid-content (gradient slate-marino)

**Cuándo usar:** después del 50% del contenido del blog, hacia un servicio relacionado. NO usar para enlaces de "lee más" — sólo para enlaces a páginas de servicio comerciales.

```html
<div style="background: #1a1a1a; color: #fff; padding: 32px; margin: 40px 0; border-radius: 4px; text-align: center;">
  <p style="margin: 0 0 12px 0; font-size: 0.9em; opacity: 0.8; text-transform: uppercase; letter-spacing: 1px;">Producción audiovisual con cabeza</p>
  <p style="margin: 0 0 20px 0; font-size: 1.3em; line-height: 1.4;">Esto es lo que hacemos. Masterizamos pensando en cómo y dónde se va a ver, no solo en cómo se ve en la suite de color.</p>
  <a href="https://zoopa.es/es/servicios/produccion-y-branded-content/" style="display: inline-block; background: #fff; color: #1a1a1a; padding: 12px 28px; text-decoration: none; font-weight: 600; border-radius: 2px;">Esto es lo nuestro →</a>
</div>
```

---

### CTA final (negro sólido — más fuerte que el mid)

**Cuándo usar:** al final del cuerpo del blog, antes del glosario y FAQ. Siempre apunta a `/contactanos/` (o equivalente).

```html
<div style="background: #000; color: #fff; padding: 36px; margin: 48px 0; border-radius: 4px;">
  <h2 style="margin: 0 0 12px 0; color: #fff; font-size: 1.4em;">Hablemos</h2>
  <p style="margin: 0 0 24px 0; opacity: 0.8; line-height: 1.6;">Si estás preparando una campaña broadcast, un branded content o una pieza de prestigio para streaming, conviene tener esta conversación antes del rodaje, no en la sala de aprobación. Te contamos cómo lo hacemos en Zoopa.</p>
  <a href="https://zoopa.es/es/contactanos/" style="display: inline-block; background: #fff; color: #000; padding: 14px 32px; text-decoration: none; font-weight: 600;">Hablemos →</a>
</div>
```

**Diferencia visual entre mid-CTA y final-CTA:**

| Aspecto | Mid-CTA | Final-CTA |
|---------|---------|-----------|
| Background | `#1a1a1a` (charcoal) | `#000` (negro puro) |
| Estructura | Eyebrow caps + 1 línea + botón | H2 + párrafo + botón |
| Padding | 32px | 36px |
| Margin top | 40px | 48px |
| Tamaño botón | Medium | Larger |

El final-CTA es **más fuerte** que el mid: más padding, más oscuro, H2 visible. Esto crea jerarquía visual cuando el lector llega al final.

---

### Featured image figure inline (al inicio del cuerpo)

**Cuándo usar:** al inicio del cuerpo del blog, después del H1 implicito y antes de la intro. Sirve también como referencia para featured_media de WordPress.

```html
<figure style="margin: 24px 0 40px 0;">
  <img src="https://zoopa.es/wp-content/uploads/2026/05/tv-oscura-dialogos-zoopa.gif" alt="Animacion que ilustra como la imagen y el sonido de la TV moderna esconden informacion al espectador: oscuridad, dialogos enterrados y desenfoque ambiental" style="width: 100%; height: auto; border-radius: 4px; display: block;" />
  <figcaption style="font-size: 0.9em; color: #64748b; text-align: center; margin-top: 12px; font-style: italic;">Tres decisiones de la industria audiovisual que están reduciendo la información que llega al espectador.</figcaption>
</figure>
```

**Notas:**
- `border-radius: 4px` da un toque editorial sin caer en lo decorativo
- Alt text descriptivo y largo (mejor para SEO + accesibilidad + LLMs)
- Figcaption itálica corta = anchor descriptivo, no descripción literal
- Si la imagen es decorativa, no usar figcaption

---

### Anti-patron: imagen placeholder

**NUNCA dejar `src="featured-image-placeholder.jpg"`** en el contenido publicado. Si el usuario no aporta imagen, **omitir la figure entera** (el publisher la stripea automáticamente con regex `<figure[^>]*>\s*<img[^>]*placeholder[^>]*/?>`).

Cuando se publique, asignar `featured_media: ID` via API REST de WordPress (el theme la pone automáticamente arriba).
