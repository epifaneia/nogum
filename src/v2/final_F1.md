# final_F1 · Revisión final de `fA_ideas_intro_0_1.html`

Ámbito: Introducción, Las seis ideas, cap. 0, cap. 1 (1.1–1.5, con las siete tarjetas). Leído entero en orden de lectura. Las seis ideas, sin tocar (no tenían erratas). En la Introducción, solo erratas y frases rotas.

## Cifras de las tarjetas contra el Apéndice B (`fB_apendices.html`, `apx-mates`)

Todas las cifras cuadran: pifia, crítico, «sale adelante» con bono 0, éxito con coste (solo Pulp y Comedia negra, total 6 o 7), la tabla del cuadrante de `ch1-panel-cuadrante` y las frases de los textos de las tarjetas:

| Tarjeta | Pifia | Crítico | Bono 0 | Frases comprobadas |
|---|---|---|---|---|
| Épica | 1 · 1 % | 10 · 19 % | 75 % | «la mitad de las veces» con −2 (51 %) |
| Pulp desenfrenado | 1–2 · 4 % | 10 · 19 % | 75 % | igual que la Épica hasta +3; +4: 96 frente a 99; coste 5 % con +4 |
| Realista | 2–3 · 3 % | 19–20 · 3 % | 55 % | — |
| Primera marcha | 1 · 10 % | 10 · 10 % | 50 % | diez puntos por escalón |
| Comedia negra | 1–2 · 20 % | 9–10 · 20 % | 50 % | igual que la Primera marcha hasta +3; +4: 80 frente a 90; pifia + coste = 40 % |
| Angustia | doble 1 · 1 % | doble 10 · 1 % | 25 % | 9 → 81 %; recuadro de la fila opresiva: 9 / 25 / 49 / 81 |
| Pesadilla | 1 · 19 % | 10 · 1 % | 25 % | 18 puntos más de pifia que la Angustia; con +4, fallo limpio 0 % |

Tres frases no casaban del todo con las tablas y se han ajustado (abajo, cambios 7, 8 y 9).

## Cambios

| # | Sitio | Tipo | Antes → después |
|---|---|---|---|
| 1 | `intro-manual`, «La trampa del tono predeterminado» | frase rota (concordancia) | «El ejemplo contrario… **es** los sistemas de comedia negra» → «… **son** los sistemas de comedia negra» |
| 2 | `intro-manual`, «Deconstruyendo el tono» | frase rota | «como el de *el del sombrero y el látigo*» → «como el del *aventurero del sombrero y el látigo*» |
| 3 | `intro-manual`, «El feliz accidente» | errata (concordancia) | «ayudado a hacer**le** a tus partidas preguntas» → «hacer**les**» |
| 4 | 1.1, Optimismo alto y Caos bajo | errata (mayúscula tras dos puntos, como en los otros ejemplos) | «*Ejemplo:* El del sombrero…» / «*Ejemplo:* El consultor…» → «el del sombrero…» / «el consultor…» |
| 5 | 1.2, tabla, casilla Realista | errata (mayúscula; las otras casillas van en minúscula) | «*Drama policial, novela histórica*» → «*drama policial…*» |
| 6 | 1.2, tabla, casilla Pulp desenfrenado | cifra (absoluto que la tarjeta contradice: con +4 el coste es 5 %, «el maestro no negocia») | «y cada victoria deja factura» → «y más de una victoria deja factura» |
| 7 | 1.3, «Dos dados, cuatro lecturas», último párrafo | cifra + repetición | «añade… **bandas más anchas** de pifia y de crítico; y dos de sus tarjetas, el Pulp desenfrenado y la Comedia negra, también el éxito con coste» → «ensancha sobre esas lecturas la **banda de pifia** (en la Comedia negra, también la de crítico), y dos de sus tarjetas añaden el éxito con coste». Pulp y Pesadilla tienen el mismo crítico que su vecina previsible (19 % y 1 %); solo la Comedia negra ensancha las dos. Las dos tarjetas ya se nombran en el paso 4 de `ch1-leer`. |
| 8 | 1.4, tarjeta Pulp desenfrenado | cifra | «Con un personaje flojo, un tercio **de lo que consigue** viene con factura» → «un tercio **de las tiradas**». Con −2, el coste es el 32 % de las tiradas, pero el 63 % de lo que sale adelante (32 de 51). Ver duda 1. |
| 9 | 1.4, tarjeta Comedia negra | cifra | «pifia, coste y crítico rondan el 20 % **siempre**» → «… **con casi cualquier ficha**» (el coste baja al 10 % con −2 y con +4) |
| 10 | 1.3, `ch1-leer`, paso 1 | voz (absoluto en texto de regla) | «Tira **siempre** los dos d10, uno rojo y uno azul.» → «Tira los dos d10, uno rojo y uno azul, también cuando solo cuente el rojo.» |
| 11 | 1.3, `ch1-sala` | voz (absoluto) | «Y como se tira siempre con algo entre −2 y +4» → «Y como lo que se suma a los dados va de −2 a +4» |
| 12 | 1.3, `ch1-pifias`, segundo párrafo | repetición dentro del apartado | «El precio del éxito con coste lo pone el Director (tiempo, un recurso, la posición, fuego amigo: 6.6)» → «El precio del éxito con coste puede ser tiempo, un recurso, la posición o fuego amigo (6.6)». Que lo elige el Director ya lo dice el paso 4. |

Comprobado con un script al acabar: HTML equilibrado, sin dobles espacios, comillas «» cerradas, ninguna marca `src` pegada a la palabra, todos los `href="#…"` apuntan a ids de `src/v2/f*.html`, menos `#acelerado`, que el montaje (`assemble_v2.py`, línea 73) reescribe al Acelerado. Ids sin tocar.

## Dudas para el autor

1. **Pulp, «un personaje flojo»** (cambio 8). La frase vieja era cierta con bono 0 (24 de 75 éxitos llevan coste: un tercio de lo que consigue) y la nueva lo es con −2 (32 % de las tiradas). Si «flojo» quería decir +0, se puede volver a «un tercio de lo que consigue» y cambiar «flojo» por «del montón».
2. **Angustia, «la tarjeta donde más pesa la ficha, del 9 % al 81 %»**. La Pesadilla tiene exactamente la misma subida (9 → 81). No es falso, pero está empatada. Se ha dejado así.
3. **Introducción, «Pero en una fantasía heroica clásica, el sistema acababa de destruir la inmersión»**. El ejemplo es una crónica de superhéroes de la Edad de Plata, no fantasía heroica. ¿Quería decir «en una ficción heroica clásica»? Es contenido del autor y no se ha tocado.
4. **Introducción, «space opera» y «la ópera de estrellas»** van juntas en el mismo párrafo (pilar «La emoción como pulso de la narrativa»). Si «la ópera de estrellas» es el arquetipo de una franquicia concreta, está bien; si no, se puede unificar.
5. **Tarjetas, fila «Sale adelante (bono 0)»**. El autor dijo que a la tabla de la hoja de referencia le sobra el porcentaje con +0. En las tarjetas se ha dejado, porque es la cifra que usa la tabla del cuadrante. ¿Se quita también aquí?
