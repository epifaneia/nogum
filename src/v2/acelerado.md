# NOGUM Acelerado · puesta al día con el canon (22 oct)

Ficheros: `src/frag_acelerado.html` (castellano) y `src/frag_acelerado.en.html` (inglés, traducción fiel del castellano corregido). Misma estructura que antes: mismos ids, mismos enlaces, mismas secciones. Solo cambia la tabla de ejemplos de armas, que pasa de 8 a 10 filas (la pistola se separa del arco, y entra el bláster).

Comprobación con script (`check_acel.py`, en el scratchpad): HTML equilibrado en los dos idiomas; ids, href, número de etiquetas de cada tipo, clases y las 86 marcas `src` son idénticos entre castellano e inglés. También se ha pasado el filtro de notas de `assemble3.py` por los dos ficheros: no queda ningún «ED-» ni ningún «C·» suelto en el texto del lector.

Marcas de origen nuevas: `C·<id>` (a2, a5, r2–r6, r10, l1, l2, l4, l6–l9, e2, e4, e8, c7, m3, x1) y `C·22oct` (las Aclaraciones).

## Cambios, por sitio (antes → después)

**Toda la obra**
- «DJ» / «Director de Juego (DJ)» → «Director» («Un Director de juego» la primera vez). (22·P22)
- «éxito parcial» → «éxito con coste», el nombre del completo: en la tabla de 2.1, el menú de costes, el combate en Caos, el Estilo, la Interfaz y las notas ED-15. Se dice siempre «solo en Caos», que es el único modo cuya tarjeta (Comedia negra) lo lleva. (22oct, éxito con coste no universal)
- Absolutos suavizados: «la TN no se mueve nunca» → «no se mueve»; «Una pifia es siempre un desastre…» → sin «siempre»; «Nunca “lo consigues, pero pierdes una casilla”» → «Mejor no…»; «nunca sale gratis» → «no sale gratis»; «nunca los dados» → «no los dados». (MAPA §2)

**0.4 Sesión 0**
- «el combo barato» se presenta en media frase: «el que abusa de las reglas». (CONCEPTOS, fallo 1)
- «el mundo y su techo» → «el mundo y hasta dónde puede crecer un personaje en él» (el techo aún no está presentado ahí).

**1.3 Modos**
- Terror: «De ahí le viene lo opresivo» (las 3 casillas). «En Terror el mundo no es más cruel: tú eres más frágil» → «lo opresivo no está en los dados: está en lo frágil que eres». (22oct, Terror)
- «Lo que cambia es que un cuchillo te mata» → «dos golpes serios te dejan fuera de combate». (m3; contradecía 2.7)
- Nota ED-A1: añadido que el autor confirma poco optimismo → Terror.
- Aside: «los cuatro existen en el manual completo… ya conoces cuatro de las siete tarjetas» → tres son tarjetas (Épica, Primera marcha, Comedia negra) y Terror es la Primera marcha con la vida corta, un asomo a una regla del completo; añadido que el completo tiene dados opresivos de verdad, demasiado extremos para una simplificación, y que Terror es «un terror para todos los públicos». (x1, 22oct)

**2.1** — nota ED-15: «las cuatro lecturas son las del completo» → tres tarjetas + Terror. (x1)

**2.2 Límites** (C)
- «Si pasa de +4, el DJ elige: o se tira a +4 o se narra el éxito sin tirar» → los bonos se acumulan, lo que se pueda, a criterio de la mesa; por encima de +4 se tira con +4 y lo que sobra sirve para algo más difícil y con más premio. Por debajo de −2, el Director decide si hay derecho a tirada; si lo hay, con −2. (a2, 22oct «por debajo de −2»)

**2.3 Habilidades**
- «la Fuerza» (franquicia) → «lo sobrenatural». (MAPA §2)
- «12 puntos, o 14 si tu personaje tiene Arcano» → 14 **para todos** si algún jugador de la mesa pone algo en Arcano; 12 si la magia existe pero no está al alcance de los jugadores. (22oct, 14 puntos)
- «Los bonos no se suman» → «Los escalones no se suman entre sí» (los bonos sí se acumulan, 2.2).

**2.4 Rejilla**
- Nivel 1: fuera «el consultor de Baker Street» (para el autor no es humano: es N2 Mental de la tabla 1) → «el boxeador, el profesor de química, el hacker».
- Nivel 2: «un humano excepcional o algo que ya no lo es»: el bárbaro de la estepa, el soldado del suero, la presencia del vampiro (tabla 1).
- Nivel 6: «No se tira: es decorado. El DJ lo narra» → «Un planeta, lo cósmico. Casi siempre injugable: la mayoría de universos no lo tienen, y lo que hay ahí se toca con Llaves». (22oct, lo cósmico)
- El ×100: ahora solo «si en tu mundo los números significan algo» (lectura tangible); en un mundo de cómic o de leyenda manda la historia y la escala la pone la mesa, o ninguna. (r2, r3)
- «Lo que se mide son las herramientas y la escala» → «la escala» (las herramientas son Llaves); añadido «si un salto de nivel te suena a cómic, es porque lo es». (r4)
- Idea 1: fuera «casi nunca es humana», «×100» y «las sirenas, un 3» (las sirenas son Llave: enormes en una sola cosa). La presencia del vampiro, 2 en Social; la humana realista, 1 en todo; por eso los unos abundan. (r4, criterios de las tablas)
- Idea 2: «da un permiso o rompe la Rejilla» → «da un permiso, anula una defensa o alcanza un nivel por encima». (e8)
- Idea 3: la Parca, Llave al daño, «aunque el daño, por sí solo, no se pague». (22oct, daño de nivel superior)
- Idea 5: «un nivel por encima, solo en lo que cubre» → «uno o varios niveles, y anula lo que dice que anula». (l2)
- «resueltos en el manual completo (2.6)» → «en el capítulo de la Llave del manual completo» (la numeración vieja ya no vale).
- Salto de poder: el monstruo de arriba «el golpe entra sin tirada, con el daño de su arma» → «no hay tirada, ni para dar ni para salvarse, y se narra la derrota». (P-v2 #10). Con Llave: «no se protege dos veces». (r10)
- La Llave (C): «Cada Llave te sube un nivel de Rejilla contra su objetivo» → te pone uno o varios niveles por encima y en esa tirada actúas como ese nivel (si eres 1 y te pone en 2, el de nivel 1 no tiene derecho a tirada; contra un 2, tiras con tu bono completo); la de la ficción cubre lo que diga la ficción y dura una escena; la propia, **toda una habilidad concreta, contra cualquier objetivo**. (l1, l2, l3)
- «bazooka» → «bazuca» (como en la idea 5).

**2.4 Las Llaves se compran**
- Bote: añadido 1·1·1·1·2 como **punto de partida recomendado**, con el 2 solo donde el universo lo permita. «El techo» único → los tres techos con su nombre: nivel máximo inicial, nivel máximo de los jugadores, nivel máximo del mundo; los tres son de Rejilla, y a las Llaves mejor no ponerles techo. (r5, r6)
- «Se puede empezar con más puntos… sabiendo que va contra la idea de este manual» (C) → es un punto de partida, no un límite: más alto o más bajo según lo que se emule; viene pensado para ciberpunk, y zombis u horror cósmico suelen pedir menos. (e4)
- Llave (C): fuera «una habilidad concreta contra su objetivo», «un ámbito entero contra su objetivo durante una escena» (la Llave ancha) y «Nunca una Firma». Ahora: toda una habilidad concreta, contra cualquier objetivo, para siempre (la Firma va dentro); «Armas contra los vampiros» es una Limitada, más barata a partir de dos niveles, y a un nivel cuesta lo mismo, así que conviene no limitarla (consejo). En blanco: «si alguien abusa, la mesa lo frena». (l1, l4, l5, l7, P-v2 #5)
- Cambio Rejilla/Llaves: «te llevas esas 5 Llaves» → «lo que vale en Llaves (5 por un nivel de más, 20 por dos)». (e2)
- n²: «contra la misma cosa» → «en la misma habilidad»; «nadie empieza más de dos niveles por encima» → «puedes subir dos niveles en una habilidad (4 Llaves), y te sobra una».
- Llave por sesión: con Llaves se compran los permisos (1 Llave, a ojo de buen cubero) y los niveles; el equipo, aquí, solo pide dinero. (l9, simplificación del equipo)
- Llave prestada: «sube lo que la ficción diga, dura una escena y no se paga». (l6)

**2.6 Combate**
- Escalera de resultados: «éxito con coste (solo en Caos)».
- Pifia del defensor (C): «el ataque sube un nivel de resultado… si llega a crítico, +1» → recibe todo el daño **+1**, y +2 si además el ataque fue crítico. Daño final: «+1 por crítico del atacante, +1 por pifia del defensor». (22oct, crítico y pifia se suman; P-final 1)
- Peligros sin atacante: fuera «Nunca matan: como mucho, fuera de combate». (l8; 2.7 ya lo cuenta)
- Esq: Nula: «no hay reacción que tirar» → «no hay esquiva que tirar: si el arma deja absorber, te queda la absorción» (con la pistola en Esq: Nula hacía falta).
- La Parca: «quedas fuera de combate» → «se te da fuera de combate, sin derecho a tirada» (frase del autor); fuera «Nunca mata». (l8)
- Etiquetas: Esq: Total añade «flechas»; Esq: Nula añade «las armas de fuego, a nivel 1: una bala no se esquiva»; Abs: Nula, fuera «láser» (en el Bazar el láser no penetra) → «la bala que atraviesa cualquier blindaje». (e8, Bazar v2)
- Ejemplos de armas (C), alineados con el Bazar v2: arco Esq: Total; **pistola, revólver** y **magnum, escopeta** con Esq: Nula; fila nueva **pistola bláster**, Esq: Total por convenio del género; «granada, bola de fuego» → «granada, explosivo de guerra» (la bola de fuego del Bazar es otra cosa); rifle láser Esq: Nula · Abs: Total. (e8, 22oct blásters)
- «Una granada Parca 2 en manos de un nivel 1 cuesta 1 Llave» → si la Parca es un poder tuyo, cuesta n² Llaves; si es equipo, aquí solo dinero, y la granada, de un solo uso, ni ocupa sitio. (simplificación del equipo; 22oct, un solo uso)

**2.7 Vida**
- «tres, nueve o veintisiete casillas» → «tres bloques, nueve casillas o veintisiete puntos» (también en 4). (c5)
- «En NOGUM nadie muere por una mala tirada» → «ningún protagonista muere por una mala tirada: la muerte se pacta». (m3)
- «Ni siquiera La Parca mata… La muerte, la locura…» → «La Parca, lo mismo: se le da fuera de combate, sin derecho a tirada; lo que venga después (una cicatriz, la locura, una transformación) se acuerda en la historia». Sin nombrar la muerte. (l8)
- «Los penalizadores… nunca bajas de −2» → se suman como cualquier modificador; por debajo de −2, el Director decide si queda derecho a tirada. (22oct, P-final 2)

**2.8 Masillas**: «A los masillas no se les cuentan casillas… El decorado lo declara el DJ» → los masillas son decorado: sin ficha ni tirada, actúan como un nivel por debajo de los jugadores, no hacen daño ni llevan casillas. (c7, P-v2 #20, 22oct masillas)

**2.9 Equipo**
- «Nada de puntos, nada de Llaves… Solo lo que rompe la Rejilla… cuesta además Llaves» (C) → **solo dinero**, también la pistola o la granada, que en el completo piden Llaves; lo que sí pide es sitio. (simplificación aprobada)
- Nueva viñeta **Tres objetos que importan**: con nombre y números en la ficha; para coger uno nuevo, sueltas uno; lo demás se da por hecho y no da bonos; lo de un solo uso no cuenta. (22oct, aceptado por el autor)
- Lo robado que te quedas tiene que caber también entre tus tres objetos.
- Aside: el completo cobra en puntos lo que te hace mejor, en Llaves lo que anula una defensa o hace lo imposible, y el daño es gratis. (e5, e8)

**3 Interfaz**: «Desafío por encima de la Rejilla, sin Llave» → «Algo por encima de tu nivel, sin Llave» (el tanque se queda: es una Llave de nivel 3 y la frase funciona igual). «Improvisar un enemigo»: el decorado, «sin ficha ni tirada».

**4 Puente**: la lista del completo añade las ventajas y lacras («los rasgos que no son habilidades, como la visión nocturna o una fobia»).

**Apéndice**
- Hoja: puntos «14 si algún jugador de la mesa lleva Arcano»; bote con la salida recomendada 1·1·1·1·2 (fuera «Por defecto, todo a nivel 1»); equipo «tres objetos»; Llaves «la habilidad concreta que sube, contra cualquier objetivo, y cuántos niveles; si es Limitada, apúntalo» (fuera el «un ámbito entero una escena»).
- Pregenerados, la frase de los puntos: Kira y Tomás gastan 12; Ysolde 14, y si juegan en su mesa, todos 14.
- **Kira**: pistola pesada Esq: Nula; tercer objeto, chaqueta blindada (+1 a absorber, Absorción +3 con ella); Llaves «Armas» e «Intimidación» (antes «contra drones», «contra corredores») y tres en blanco; «es una Nula» → «una nulidad»; «En mesa» enseña la Llave: dispara como nivel 2, el matón corriente no tira contra sus balas y contra un cromado de nivel 2 tira con su +4. Cuentas: 7+2+3 = 12. ✓
- **Tomás** (gastaba 14 sin Arcano): fuera Erudición → Ciencias y Influencia → Persuasión. Mental 8, Social 3, Físico 1 = 12. ✓ Revólver Esq: Nula; linterna y cuaderno «se dan por hechos». Llaves «Ocultismo» e «Investigación» (antes «contra los Profundos», «contra la secta»).
- **Ysolde**: la bola de fuego sale del equipo: «Su fuego (es su Arcano 2, no equipo)», con las etiquetas de la Bola de Fuego del Bazar (Daño 2 · Esq: Parcial · Abs: Máx 1), a escala de una sala. «Por defecto, los personajes empiezan en nivel 1 en todo» → «Su ficha es la salida recomendada, 1·1·1·1·2». Cuentas: 7+3+2+2 = 14. ✓

## Inglés

Rehecho entero desde el castellano corregido, reaprovechando el inglés viejo donde no cambiaba. Términos de `TRADUCCION.md` que corrigen al inglés viejo: «Director» → GM; «Dmg» → «Damage»; «lent Key» → «borrowed Key»; «Black comedy» → «Black Comedy»; «specialty» → «speciality»; «permission» → «permit»; «damage tracks» → «damage bars»; «ones are plentiful» → «ones are everywhere»; «the complete rulebook» → «the Complete Game» en todas partes. Los techos: starting maximum / player maximum / world maximum. Nuevos que he tenido que elegir: «three items that matter» (tres objetos que importan), «the serum soldier», «chromed-up merc» (cromado), «horror for all audiences».

## Dudas para el autor

1. **El fuego de Ysolde.** Lo he sacado del equipo: con Arcano 2 es ser de Rejilla en Arcano, y su fuego llega a una sala sin Llave (como el maestro de la Orden de la tabla 1). Pero el canon dice que el hechizo es un permiso y se paga con Llaves (l10), y la pregunta 19 del barrido (¿la bola de fuego Parca 2 paga Llave si no le saca nivel a su Arcano 2?) sigue sin respuesta. ¿Vale así, o el fuego de Ysolde debería costarle una Llave aparte?
2. **«Éxito parcial» → «éxito con coste».** He unificado al nombre del completo. Si preferías conservar «parcial» como palabra del Acelerado, se revierte en un momento.
3. **La Llave propia en el Acelerado es muy fuerte a nivel 1.** Con «Armas», Kira deja sin tirada a cualquier matón de nivel 1. Es lo que dice l2, y lo enseño así en su «En mesa», pero con 5 Llaves en el bote cualquier jugador puede hacerlo desde la primera sesión. ¿Lo quieres así de claro en el manual corto?
4. **Dos párrafos de edición que sí llegan al lector**: «Las preguntas son propias de este manual: el autor fijó el formato…» (1.2) y «Las frases de modo, bloque 2 y arma sin esquiva vienen de la interfaz verbal…» (3). El montaje solo borra la marca «Aprobado por el autor», no el párrafo. No los he tocado; ¿se quitan o se marcan como `flag ed`?
5. **Iniciativa por Destreza** y **un solo nivel de Rejilla para todo el PNJ**: son simplificaciones viejas del Acelerado que el canon no toca. Se quedan.
6. **Las preguntas del selector** siguen mandando «poco optimismo» a Terror con cualquier caos (ED-A1). Con tu respuesta (Terror es la lectura opresiva) encaja; lo apunto por si quieres revisar la casilla «poco optimismo + mucho caos».
