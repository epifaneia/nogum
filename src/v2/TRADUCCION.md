# NOGUM v2 · Traducción al inglés

Estás traduciendo al inglés uno o varios fragmentos del Juego completo v2 (castellano, en `src/v2/`). El castellano está cerrado y aprobado por el autor: **la traducción lo sigue fielmente**, sin añadir, quitar ni reordenar.

## Salida

Para cada `src/v2/fX….html` escribe `src/v2/fX….en.html` con **exactamente la misma estructura**: mismas secciones, mismos ids, mismas clases, mismas tablas con el mismo número de filas y columnas, mismos enlaces `href="#…"`, mismas marcas `<span class="src">…</span>` (sin traducir: son códigos) y mismas banderas `flag`. Solo cambia el texto visible. Los números de apartado y de capítulo, iguales. Comprueba con un script al acabar: mismo número de etiquetas de cada tipo, mismos ids, mismos href, HTML equilibrado.

## Reaprovecha el inglés que ya existe

Mucho texto del castellano v2 viene del libro viejo, que ya tiene traducción en `src/frag_*.en.html` (`frag_intro.en.html`, `frag_ch0.en.html`, `frag_ch1a/1b.en.html`, `frag_math.en.html`, `frag_ch2…ch5.en.html`, `frag_ch67.en.html`, `frag_cap8.en.html`, `frag_bazar_a/b.en.html`, `frag_glosario.en.html`). Cuando un pasaje castellano v2 sea el mismo que el viejo, **usa esa traducción** (corrigiéndola si el castellano ha cambiado). Cuando el castellano es nuevo o ha cambiado, traduce tú. Para pasar por script los bloques largos (tablas, SVG del apéndice), copia la estructura y sustituye el texto.

## Estilo

Inglés británico (colour, armour, neighbourhood). Texto principal serio y claro, frases cortas; las notas `<aside class="meta">` informales y con gracia. Nunca condescendiente. Sin absolutos en el texto de reglas («never», «always», «at most» → «usually», «at most tables»…). Arquetipos, nunca nombres con copyright: si el castellano dice «el trepamuros», el inglés dice «the wall-crawler», no el nombre del personaje.

## Términos (obligatorios)

Mandan sobre `GLOSSARY_EN.md` (raíz), que es más viejo: «Ancla/Vela», «Malla Tonal» y los nombres viejos de tarjetas ya no se usan.

| Castellano | English |
|---|---|
| Director (de juego) | GM (Game Master la primera vez) |
| PJ / PNJ | PC / NPC |
| Las seis ideas | The Six Ideas |
| La mesa manda | The Table Rules |
| Capítulo 0 · La mesa manda | Chapter 0 · The Table Rules |
| Capítulo 1 · El tono | Chapter 1 · Tone |
| Capítulo 2 · Lo que sabes (el Ancla) | Chapter 2 · What You Know (the Anchor) |
| Capítulo 3 · Lo que eres (la Rejilla) | Chapter 3 · What You Are (the Grid) |
| Capítulo 4 · A quién afectas (la Llave) | Chapter 4 · Who You Can Touch (the Key) |
| Capítulo 5 · Lo que cuesta (la cuenta) | Chapter 5 · What It Costs (the Tally) |
| Capítulo 6 · El peligro | Chapter 6 · Danger |
| Capítulo 7 · Las fichas | Chapter 7 · Sheets |
| Capítulo 8 · La consola de mezclas | Chapter 8 · The Mixing Desk |
| Capítulo 9 · La caja de herramientas | Chapter 9 · The Toolbox |
| Preguntas frecuentes | Frequently Asked Questions |
| Glosario | Glossary |
| Apéndice A · La Sala de Máquinas / B · Tablas completas | Appendix A · The Engine Room / B · Full Tables |
| Hoja de referencia | Reference Sheet |
| Aclaraciones | Clarifications |
| sesión 0 | session zero |
| líneas rojas | red lines |
| el combo barato | the cheap combo |
| tarjeta de tono | tone card |
| Cuadrante | Quadrant |
| Optimismo / Caos | Optimism / Chaos |
| Épica · Pulp desenfrenado · Realista · Primera marcha · Comedia negra · Angustia · Pesadilla | Epic · Unleashed Pulp · Realist · First Gear · Black Comedy · Anguish · Nightmare |
| Tragedia | Tragedy |
| TN | TN (target number) |
| dado rojo / azul; suma; mejor/peor de dos | red/blue die; sum; best/worst of two |
| pifia / crítico / éxito con coste | fumble / critical / success at a cost |
| bono, bono total, dificultad | bonus, total bonus, difficulty |
| el Ancla | the Anchor |
| Ámbito / Dominio / Disciplina / Firma | Sphere / Domain / Discipline / Signature |
| pirámide | pyramid |
| Nulidad / Torpe | Null / Clumsy |
| lista cerrada | closed list |
| acordeón | accordion |
| Estilo | Style |
| la Rejilla, nivel de Rejilla | the Grid, Grid level |
| lectura narrativa / tangible | narrative / tangible reading |
| derecho a tirada | right to roll |
| los unos abundan | ones are everywhere |
| nivel máximo inicial / del mundo / de los jugadores | starting maximum / world maximum / player maximum |
| Sincronización | Synchronisation |
| la Llave | the Key |
| Llave Limitada / en blanco / prestada / de un momento / propia | Limited Key / blank Key / borrowed Key / momentary Key / own Key |
| anula lo que dice que anula | cancels what it says it cancels |
| la Parca | the Reaper |
| permiso | permit |
| hechizo | spell |
| la cuenta | the tally |
| dos monederos; puntos de habilidad; Llaves | two purses; skill points; Keys |
| bote aparte | separate pot |
| salida; experiencia de salida | start; starting experience |
| unidad de cambio | exchange rate |
| el Ajuste: Limitado / Completo / Potenciado / Desatado | the Adjustment: Limited / Complete / Enhanced / Unleashed |
| Acceso; Recursos | Access; Resources |
| los tres cerrojos | the three locks |
| permiso narrativo | narrative permission |
| un solo uso | single use |
| ventaja / lacra | advantage / flaw |
| Don (Dominio de Arcano) | Gift |
| guardia (Violencia, Treta, Especialidad) | guard (Violence, Trick, Speciality) |
| niveles de resultado; impacto; mitigación | result levels; impact; mitigation |
| Esq / Abs / Daño (etiquetas) | Dodge / Soak / Damage (tags; keep the short forms Esq→Dodge, Abs→Soak in tables) |
| vida fractal: bloques, casillas, puntos; Letal / Táctico / Guerra | fractal health: blocks, boxes, points; Lethal / Tactical / War |
| barras (Física, Mental, Espiritual) | bars (Physical, Mental, Spiritual) |
| umbral; consecuencia | threshold; consequence |
| ficha de protagonista / completa / rápida; decorado; masillas | protagonist sheet / full sheet / quick sheet; scenery; mooks |
| el Baúl de reglas | the Rules Chest |
| el Bazar del Multiverso | the Multiverse Bazaar |
| receta; menú degustación; expedientes | recipe; tasting menu; case files |
| la Piedra Rosetta | the Rosetta Stone |
| escalera llana | flat ladder |

Si un término no está aquí, usa el que tenga el inglés viejo en `src/frag_*.en.html`; si tampoco, elige uno claro y apúntalo en tu registro para que los demás lo vean.

## Registro

`src/v2/trad_<letra>.md`: términos nuevos que hayas tenido que elegir, pasajes dudosos y la comprobación de estructura. Informe final corto.
