# La Idea · barrido contra el canon (22 oct)

**Fuente real**: `src/p_tesis_es.html` y `src/p_tesis_en.html`. Los `p3_tesis_*` los regenera `make_covers.py` (línea 73: copia `p_tesis_*` cambiando `class="chapter cover"` por `class="cover"`). Se editó la fuente y se regeneraron los `p3_` con esa misma transformación (sin ejecutar `make_covers.py` entero, que reescribe también las portadas del Juego y del Acelerado).

## Cambios (castellano → inglés)

| Sitio | Motivo | Antes → después (es) | Antes → después (en) |
|---|---|---|---|
| §2, «La vida» | m3 (la muerte se pacta; ninguna tirada mata) | «un cuchillo te mata» → «un cuchillo te saca de la escena» | «a knife kills you» → «a knife takes you off the scene» |
| §3, siete tarjetas | t2: es el **cuadrante**; «rejilla» en minúscula choca con la Rejilla | «en una rejilla de tres por tres» → «en un cuadrante de tres por tres» | «on a three-by-three grid» → «on a three-by-three quadrant» |
| §3, Sala de Máquinas | Índice nuevo: ahora es el Apéndice A (`apx-maquinas`), no un capítulo (`ch1-maquinas`) | «un capítulo entero… `#ch1-maquinas`» → «un apéndice entero… `#apx-maquinas`»; «el capítulo más denso del libro» → «la parte más densa del libro» | «a whole chapter… `#ch1-maquinas`» → «a whole appendix… `#apx-maquinas`»; «the densest chapter in the book» → «the densest part of the book» |
| §5, el ancla | a1: el ancla es el rango **de todas las fichas** (el total puede pasarse con modificadores, a2) | «y ahí se acaba, siempre, para todo el mundo» → «y ahí se acaba, en todas las fichas, para todo el mundo» | «stops there, always, for everyone» → «stops there, on every sheet, for everyone» |
| §5, la Rejilla | Definición canónica: el tamaño de los desafíos (la cámara/zoom no es la Rejilla) | «que dice a qué distancia está la cámara» → «que dice el tamaño de los desafíos a los que te enfrentas» | «saying how far away the camera is» → «saying how big the challenges you face are» |
| §7, Acelerado | x1: los cuatro modos son tres tarjetas legales y asomarse a una regla (Terror = Neutro con 3 de vida) | «ya conocéis cuatro de las siete tarjetas» → «ya conocéis tres de las siete tarjetas y uno de los controles, la letalidad» | «you already know four of the seven cards» → «…three of the seven cards and one of the controls, lethality» |
| §8, El Acelerado | x1, ídem | «cuatro séptimas partes del cuadrante» → «tres de las siete tarjetas, y a mover la letalidad» | «four sevenths of the grid» → «three of the seven cards, and how to move lethality» |
| §1, feliz accidente (solo en) | TRADUCCION: «Game Master» la primera vez | — | «each GM» → «each Game Master (GM)» |

## Comprobado y sin cambios
- «Director» en todo el castellano; no hay «DJ». No aparecen «Vela», «Sail», «Ancla/Vela» ni «malla».
- Éxito con coste: el ensayo solo habla de «acertar por los pelos» como algo que *puede* cobrar peaje (compatible con que solo lo lleven dos tarjetas); el «éxito con coste» de §1 es de otros juegos (contraste legítimo).
- «Seis escalones»: −2, −1, 0, +1, +2, +4 (el +3 no existe en ficha, resp. 24): correcto.
- «Baúl de dieciséis reglas»: la tabla de 9.1 tiene 17 filas, una de ellas la Sincronización (núcleo): 16 opcionales. Correcto.
- «Veinte recetas», Caos = Comedia negra (mismo número de éxitos, el doble de pifias y críticos), sesión 0 (m1, m2): correctos.
- Fantasmas de corrección: ninguno. Los «no es…» del ensayo contrastan con otros juegos o con lo que el lector puede pensar.

## Pendiente / aviso
- El enlace `#apx-maquinas` solo resuelve cuando el Juego que se monte sea el v2. El Juego viejo (`frag_math.html`) aún usa `ch1-maquinas`; con `assemble3.py` tal cual, ese enlace queda sin destino entre productos hasta que se monte la v2.
- §4 dice que cada módulo del baúl trae «su coste de atención declarado por escrito y su aviso de cuándo estorba»; la tabla de 9.1 v2 solo da qué hace y en qué recetas aparece. No contradice el canon; no se toca, pero conviene mirarlo.
