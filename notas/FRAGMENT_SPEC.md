# Especificación de fragmentos HTML (para ensamblar en una sola página)

Escribe SOLO un fragmento HTML (sin <html>, <head>, <body>, <style>, <script>, sin estilos inline). Idioma: español. Codificación UTF-8.
El fragmento se incrusta dentro de un contenedor ya estilado. Usa exclusivamente estas piezas:

- Contenedor raíz: `<section class="chapter" id="ID-DADO">` … `</section>` (puede haber varias secciones si se indica).
- Títulos: `<h2>` (uno por sección), `<h3 id="ID-UNICO">`, `<h4>`. Todos los h3 llevan id único con el prefijo indicado (p. ej. `bz-fantasia`). No uses <h1>.
- Texto: `<p>`, `<ul>/<ol>/<li>`, `<strong>`, `<em>`, `<blockquote>` (citas del autor), `<dl><dt><dd>`.
- Tablas: SIEMPRE envueltas: `<div class="tw"><table class="t">…</table></div>` con `<thead>` y `<tbody>`. Para números usa `<td class="num">`.
- Caja de regla: `<div class="rule"><p class="rule-title">Título</p> … </div>`
- Nota lateral en tono informal («columna meta»): `<aside class="meta"><p>…</p></aside>`
- Etiquetas técnicas de equipo: `<span class="tag">Daño 2</span>` `<span class="tag">Esq: Total</span>` `<span class="tag">Abs: Máx 1</span>` `<span class="tag">Malla: Llave N4</span>` etc.
- Marcas de estado (inline, al final del elemento afectado):
  - `<span class="flag proposal">Propuesta sin validar</span>` → idea del asistente que el autor nunca aprobó.
  - `<span class="flag pending">Pendiente</span>` → hueco que el autor dejó abierto.
  - `<span class="flag ed">ED-n</span>` → decisión editorial de congruencia (define en tu texto qué se cambió).
  - `<span class="flag drop">Descartado</span>` → solo en fragmentos de auditoría.
- Referencias a la fuente: `<span class="src">T68</span>` (turno de la conversación) o `<span class="src">Borrador</span>`.
- Nada de emojis como marcadores. Nada de imágenes externas. Escapa `<`, `>` y `&` en el texto.

Normas de contenido:
- Lee `CANON.md` (mismo directorio) antes de escribir: es la verdad. Si una fuente contradice el canon, manda el canon; si el canon no lo cubre, marca la duda.
- Terminología canónica: Optimismo / Caos; Malla Tonal (3×3 de tonos); Rejilla de Potencia (niveles N1–N5, N6 decorado); Malla de competencias (5 ámbitos: Físico, Mental, Social, Técnico, Arcano); Dominio / Disciplina / Firma; Tarjetas de Tono (T0–T6); TN; Estilo; Llave; Vida Fractal (Cáscara / Carne / Núcleo); barras Física, Mental, Espiritual; etiquetas [Daño] [Esq] [Abs] [Malla].
- Etiquetas canónicas: Daño 0–3 (y especiales: Masivo, Absoluto, Infinito, Mental N, Social N). Esq: Total / Parcial / Nula / Difícil (−2 a la esquiva) / Fácil (+2 a la esquiva). Abs: Total / Máx N / Nula (y especiales: Mente, Voluntad, Reputación = se resiste con la barra/competencia mental o social). Malla: Llave N (dañar hasta nivel N) / Nivel N (el objeto opera en ese nivel) / Ignora todo.
- NO uses las etiquetas descartadas Tipo A/B/C, [VELOZ], [LETAL], [ÁREA], [INEVITABLE] como reglas (puedes mencionarlas solo en auditoría).
