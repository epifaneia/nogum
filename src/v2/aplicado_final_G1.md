# Aplicado: DECISIONES-final 1, 2 y 3 (agente G1, 22 oct)

Fuente: `DECISIONES-final.md` y `src/CANON.md`, bloque «Respuestas a PREGUNTAS-final». Marca de origen nueva: `C·22oct`.

## 1. La pifia del defensor

- **fI 6.2, Paso 2** (casa): el defensor solo tira si el ataque ha conectado; «nadie se lanza hacia la bala que no le iba a dar». Si el atacante pifia o falla, no hay tirada de defensa.
- **fI 6.2, tabla «La defensa gana los empates»**: la fila Pifia pasa de «el ataque sube un escalón… fallo pasa a éxito… el crítico es el techo» a «Daño completo, y sube un nivel: +1».
- **fI 6.2**: fuera el párrafo «Doble pifia».
- **fI 6.8 Aclaraciones**: «¿Daño 3?» → con un crítico **o con la pifia del defensor**. «Héroe y monstruo con tarjetas distintas» → se quita «el escalón que sube la pifia del defensor se cuenta en la tarjeta del atacante» (ya no hay escalón); queda «cada uno leído en su tarjeta».
- **fI 8.3** (tonos por personaje): la misma frase, igual.
- **fH FAQ (peligro)**: nueva línea «El ataque ha fallado. ¿Tira el defensor? ¿Y si pifia?» → 6.2.
- **fH glosario, Pifia y crítico**: «el crítico del atacante suma +1 al daño, y la pifia del defensor, también».
- **fL referencia**: Impacto «Pifia o fallo, no conecta: no hay defensa»; fila pifia de la tabla → «completo, +1».

## 2. Las penalizaciones de las barras se suman

- **fI 6.5** (casa, tras la tabla de bloques): «no se suma… sigues a −2, no a −4» → se suman: Herido en Física y Mental, y la acción pide las dos cosas, −4. El total sigue en el Ancla: por debajo de −2, el Director decide si hay tirada, y si la hay, con −2 (enlace a `#ch2-limites`, 2.5). Se conserva lo de las tres formas de quedarte fuera.
- **fH FAQ**: «¿Tiro a −4?» → «¿Se suman?» (mismo enlace, 6.5).
- **fL referencia, Barras**: «Sus penalizadores se suman.» Para no alargar, «cuando el Director declara que estáis a salvo» → «al estar a salvo» (el detalle sigue en 6.4).
- Glosario: no tenía entrada de barras con «no se suma»; nada que tocar. fC 2.5 ya decía que se acumula; sin cambios.

## 3. Sincronización: juegas con la ficha del mecha

- **fD 3.8** (casa): entradilla «hereda su ficha y su nivel» → «juega con la ficha del mecha (o la del traje, o la de la entidad), con su nivel… Si hay ficha, la cambia». Fuera «aquí basta con mover tu posición en la Rejilla» (la versión rápida). Receta 18: «hereda el nivel 4… con la misma ficha» → «juega con la ficha del robot, de nivel 4». Nueva `aside.meta`: «Es un mecha: demasiado cool para no darle el protagonismo que merece». El enlace al precio pasa de `#ch5-equipo` a `#ch5-sincro` (más preciso, mismo 5.6).
- **fD 3.4 (por ámbitos, la lista del Físico)**: «heredando el nivel de un traje o de un mecha» → «jugando con la ficha de un traje o de un mecha».
- **fF 5.6, «Lo que hereda la escala»**: «que te hace heredar su nivel» → «con cuya ficha juegas mientras lo llevas, con su nivel en todo un ámbito». Precio sin tocar.
- **fH FAQ (Rejilla)**: nueva línea «Piloto un mecha. ¿Juego con mi ficha o con la suya?» → 3.8.
- **fH glosario, Sincronización** y **fJ1 Baúl, Sincronización**: «juega con la ficha del mecha, con su nivel, mientras dure» (y se añade «se fusiona»).
- **fL referencia**: «hereda su nivel» → «juega con su ficha».
- **fK1 Bazar** (solo frases): taller de etiquetas («juega con su ficha y su nivel»), tabla de tipos, fila Vehículo («con un mecha o un exoesqueleto, mientras lo pilotas, juegas con su ficha») y Exoesqueleto Militar («juegas con la ficha y el nivel del traje»). Precios intactos. fK2: sin frases que contradigan; sin cambios.

## Comprobación

- Script: HTML equilibrado en todos los ficheros tocados; los únicos avisos son los de siempre (`<section>` abierta en fK1 y cerrada en fK3, a propósito). Enlaces internos: todos válidos; el único «roto» es `#acelerado`, que lo reescribe `assemble_v2.py`.
- fL: 11 901 → 11 904 bytes.

## Para otros / dudas

- **fJ2 (receta 18, no es mío)**, líneas ~186–187: «Dentro, hereda el nivel 4 del robot… con la misma ficha» y «Dos techos en la misma ficha». Contradicen la decisión 3: dentro del robot se juega con la ficha del robot.
- **Duda sin zanjar:** crítico del atacante + pifia del defensor, ¿+2 al daño (Daño 2 → 4)? La regla vieja ponía el crítico de techo; la nueva no lo dice. Lo he dejado sin decir.
