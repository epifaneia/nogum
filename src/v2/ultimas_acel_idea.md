# Últimas decisiones (22 oct) en el Acelerado y La Idea

Ficheros tocados: `src/frag_acelerado.html`, `src/frag_acelerado.en.html`. `src/p_tesis_es.html` y `src/p_tesis_en.html` no necesitaban cambios (abajo). `src/p3_tesis_es.html` y `src/p3_tesis_en.html` se han regenerado desde los `p_tesis_*` con el mismo reemplazo que `make_covers.py` (`class="chapter cover"` → `class="cover"`), sin ejecutar make_covers; salen idénticos a los que había.

## A · Ysolde (Acelerado, los dos idiomas)

- **2.4, «Las Llaves se compran», viñeta del punto de partida** (C·e4): se nombra el concepto, que la ficha necesita: «Lo que reparta de más o de menos antes de jugar, en puntos o en Llaves, es la **experiencia de salida**.» / «Whatever it hands out above or below that before play, in points or in Keys, is the **starting experience**.»
- **2.4, viñeta de la Llave por sesión** (permisos): añadido «Un hechizo es uno de esos permisos: tu habilidad dice lo bien que lo lanzas y la Rejilla, a qué tamaño, pero lo que puedes hacer se paga con Llaves.» / «A spell is one of those permits: your skill says how well you cast it and the Grid how big, but what you can do is paid for in Keys.» + `C·l10`.
- **Párrafo de los pregenerados**: «Cada uno usa además su bote aparte» → «…su bote aparte, y Ysolde, 1 Llave de experiencia de salida para su fuego (abajo).» (EN igual.)
- **Ficha de Ysolde**: «Su fuego (es su Arcano 2, no equipo)» → «Su fuego (un hechizo, no equipo)». Línea nueva, con el formato del «Bote aparte» de Kira y Tomás: «**Bote aparte:** +1 nivel de Rejilla en Arcano, su 2. **Experiencia de salida:** 1 Llave, la de su fuego. Un hechizo es un permiso y se paga con Llaves: la Rejilla dice el tamaño, no qué puedes hacer. Con su Arcano 2 el fuego llega a la sala entera sin pagar más nivel, así que le basta 1 Llave; y como el bote se le fue en el 2, esa Llave la pone la experiencia de salida.» + `C·l10 C·e4`. EN: «Separate pot / Starting experience», misma frase.
- **La cuenta**: 14 puntos (7 + 3 + 2 + 2 + 0), bote = +1 Rejilla en Arcano, experiencia de salida = 1 Llave, gastada en el fuego. «En mesa» se queda como estaba (sigue siendo cierto: su 2 es su bote).

## H · «que la historia lo permita»

Sin cambios: ni el Acelerado ni La Idea (en ningún idioma) nombran el segundo cerrojo del equipo ni dicen «permiso narrativo» / «narrative permission». El Acelerado deja el equipo solo con dinero (2.9) y no habla de cerrojos.

## K · «Ámbito» con mayúscula (solo castellano)

- `frag_acelerado.html`: las 18 apariciones de «ámbito/ámbitos» eran el término del juego (2.2 tabla de bonos, 2.3, 2.4, nota lateral de 2.4, hoja de personaje) → «Ámbito/Ámbitos». No queda ninguna en minúscula. Las cabeceras de tabla ya iban en mayúscula.
- La Idea no usa la palabra.

## L · Nombres de Firmas y objetos (solo castellano)

Sin cambios: ya estaban con mayúscula solo inicial («Armas de fuego», «Cultos y grimorios», «Juego de manos», «Fuego», «Parkour»; el equipo va en minúscula como nombre común: «pistola pesada», «chaqueta blindada», «bastón»). «Gran Maestro» es la etiqueta del escalón, no el nombre de una Firma, y el v2 la escribe así: se queda. La Idea no nombra Firmas ni objetos.

## B y M

No aplican: ninguno de los cuatro ficheros habla de la escalera llana, de la Angustia o la Pesadilla como tarjetas («pesadilla» sale como palabra corriente), de la frase de la Realista sobre el +4, ni de los ejemplos del parkour y la natación o de «leer una calle».

## Comprobación (script `chk_acel_idea.py`, en el scratchpad)

- Acelerado ES/EN: HTML equilibrado en los dos; mismos ids (8), mismos href (2), mismas etiquetas (1180) y clases; 87 marcas `src`, iguales salvo la que ya era distinta antes («Aprobado por el autor» / «Approved by the author»).
- La Idea ES/EN (y p3): equilibrado; mismos href (1) y clases; los 9 ids van en el mismo orden con prefijo `es-`/`en-`, como siempre. Ya antes de esta tanda el castellano tenía un `<strong>` más que el inglés: no lo he tocado.
- `p3_tesis_*` = `p_tesis_*` con el reemplazo de make_covers: sí, los dos.

## Visto de paso, sin tocar (fuera de estas decisiones)

- `frag_acelerado.en.html` traduce «bloque» de vida como «lock» (2.7, Interfaz, 4); TRADUCCION.md pide «block».
- La Idea, cap. 6: «De ahí salen el tono, la escala, la letalidad…» y cap. 2 «la escala del conflicto»: si la decisión C (fuera la «escala de la partida» de la App) tiene que llegar también aquí, falta decidirlo.
