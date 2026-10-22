# NOGUM v2 · Cada concepto, presentado antes de usarse

El autor, leyendo la v2 (página 13, las seis ideas), ha encontrado dos fallos que vienen de haber escrito por trozos. Hay que buscarlos en todo el libro antes de que él lo revise a mano.

## Fallo 1 · Conceptos dados por sabidos

«La primera mención a algo no debe dar nada por sentado. Jamás se mencionan de pasada conceptos que aún no se han presentado como si ya estuvieran.»

Ejemplo real, en las seis ideas (ya rehecho): «La Rejilla es escala, no habilidad: el tamaño de lo que mueves en todo un **ámbito**. Cuando a la historia ya no le interesa que **cierto enemigo tenga tirada**…». El lector aún no sabe qué es un ámbito, ni por qué un enemigo tendría o no tirada. Y la Llave se presentaba hablando de Disciplinas, compras y Limitada, la primera vez que se nombraba.

Cómo se arregla, por orden de preferencia:
1. **Contarlo con palabras de la calle**, sin el término técnico (como hace el autor: «la Rejilla dice el tamaño de los desafíos a los que te enfrentas»; «ese permiso narrativo para hacer cosas que están a otro nivel lo llamamos Llave»).
2. Si el término hace falta, **presentarlo ahí en media frase**, con un enlace a su casa: «el Estilo, un +2 que se tira cuando ya no puedes fallar (3.5)».
3. Si sobra, **quitarlo**.

Nunca: usar el término como si el lector ya lo conociera.

## Fallo 2 · Fantasmas de corrección

«El ancla no es el +4: es el rango.» Nadie ha dicho que lo sea. El texto contesta a una corrección del autor que el lector nunca vio.

No se escribe una regla como corrección de una versión anterior del juego: «no es X: es Y», «ya no», «antes se llamaba», «no se narra el éxito», «no es una regla de…», «sin excepción», «nada de…» cuando X es algo que solo existió en nuestros borradores o en el canon. Se dice lo que es, y punto. **Sí valen** los contrastes con otros juegos o con lo que el lector puede pensar por su cuenta (la tesis del libro los usa, y está bien), y las notas de historia en la columna `meta` cuando están marcadas como tales.

## El orden en que se presenta cada concepto

El lector lee de arriba abajo. Un concepto se puede usar como conocido **solo después** de su presentación. Antes, hay que aplicar el Fallo 1. (Las preguntas frecuentes, el glosario, la hoja de referencia, el cap. 9 y los apéndices van después de todo y pueden usar cualquier término.)

| Dónde se presenta | Conceptos |
|---|---|
| Introducción (`intro`) | el rol, el tono, los dos ejes (Optimismo y Caos) a grandes rasgos, la tesis |
| Las seis ideas (`ideas`) | la mesa manda; la sesión 0 (nombrada); el tono se lee en dos d10 y siete tarjetas; el Ancla = tu porcentaje de éxito, un bono de −2 a +4; la Rejilla = el tamaño de los desafíos, y que un nivel por encima deja al de abajo sin derecho a tirada; la Llave = permiso narrativo para hacer cosas a otro nivel; dos monederos (puntos de habilidad y Llaves); un nivel de Rejilla se puede cambiar por cinco Llaves |
| Cap. 0 | líneas rojas, la sesión 0 en detalle, «esto no vale», abuso de reglas / combo barato, tira solo si fallar es interesante, la muerte se pacta. **Ojo con 0.8 «Y de ahí salen los números»**: habla de cosas de los caps. 2–5 (puntos, salida, techos, experiencia, ritmo de Llaves, ventajas): todo en palabras de la calle y con enlace, nada como sabido |
| Cap. 1 | ejes, cuadrante, tarjeta de tono, lecturas (rojo, suma, mejor, peor de dos), TN, dificultad, bono total, pifia y crítico, bandas, éxito con coste, la Sala de Máquinas |
| Cap. 2 | Ancla (el rango de todas las fichas), ámbito, Dominio, Disciplina, Firma, pirámide y sus costes, Nulidad, Torpe, lista cerrada, acordeón, los bonos se acumulan, el margen por encima de +4, por debajo de −2, modificadores |
| Cap. 3 | nivel de Rejilla y derecho a tirada, lectura narrativa y tangible, ×100, escala, ser no es saber, los unos abundan, Estilo, quién la sube, los tres techos, lo cósmico, sincronización |
| Cap. 4 | Llave en detalle (toda una Disciplina contra cualquiera), anula lo que dice que anula, Esquiva/Absorción/Daño como frentes (presentados aquí en lo justo), n², Limitada, Llave propia / prestada / de un momento / en blanco, la Parca, permisos, hechizos |
| Cap. 5 | dos monederos en detalle, bote aparte, salida 1·1·1·1·2, experiencia de salida, unidad de cambio (5·n², 8·n²), la cuenta, mínimo 1, un solo uso, el Ajuste, equipo (Acceso, Recursos, permiso narrativo), devolver/prestar/regalar, progresión, ventajas y lacras |
| Cap. 6 | guardias e iniciativa, niveles de resultado, impacto y mitigación, etiquetas Daño/Esq/Abs en la ficha técnica, daño máximo 2, vida fractal (bloques, casillas, puntos), barras, umbral, consecuencias, curación, menú de costes |
| Cap. 7 | ficha de protagonista, completa, rápida, decorado, aspectos |
| Cap. 8 | diagnóstico del tono, tono por defecto, velocidades, disonancia |

Si encuentras un concepto que no está en la tabla, búscale su sitio (dónde se explica de verdad) y aplica la misma regla.

## Tu trabajo

Lee tus ficheros enteros, en orden de lectura, párrafo a párrafo (también tablas, recuadros, asides y pies). Para cada término técnico, pregúntate: ¿se ha presentado ya, más arriba en el libro? Si no, arréglalo (Fallo 1). Y busca los fantasmas de corrección (Fallo 2). Reescribe en la voz del libro (MAPA.md §2: frases cortas, sin condescendencia, sin absolutos). **No cambies ninguna regla ni quites ejemplos únicos**: el contenido conceptual está bien («en lo conceptual sí está muy bien, solo es la manera de contarlo»). Las seis ideas ya están rehechas por el coordinador: no las toques. La introducción es texto del autor: arregla solo lo imprescindible.

Escribe `src/v2/conceptos_<letra>.md` con cada cambio (fichero, sitio, término o fantasma, antes → después). Mantén los enlaces válidos y el HTML equilibrado.
