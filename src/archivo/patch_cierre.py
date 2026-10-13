# -*- coding: utf-8 -*-
"""Cierre del cuadrante: canon, cuaderno y Acelerado con las siete tarjetas definitivas."""
import io, os, re
os.chdir(os.path.dirname(os.path.abspath(__file__)))
MISS = []


def patch(fn, pairs):
    s = io.open(fn, encoding='utf-8').read()
    for a, b in pairs:
        if a not in s:
            MISS.append((fn, a[:70]))
            continue
        s = s.replace(a, b)
    io.open(fn, 'w', encoding='utf-8').write(s)


# ---------------- canon: sustituye el bloque de las siete ----------------
c = io.open('CANON.md', encoding='utf-8').read()
i = c.index('## 2bis. EL CUADRANTE DE SIETE TARJETAS')
j = c.index('\n## 3. Capítulo 2')
BLOQUE = """## 2bis. EL CUADRANTE DE SIETE TARJETAS (modelo vigente)
Sustituye al panel de 6 tarjetas + recetas. Cerrado por el autor tras el taller de palancas (18-20 septiembre 2026).
- **Ejes**: la FILA dice de qué lado está el universo (optimista / neutral / opresivo). La COLUMNA dice a qué precio (previsible / neutral = la costumbre / caótico).
- **Asimetría que gobierna el modelo (ED-24)**: las sorpresas buenas AMPLIFICAN (el crítico va donde ya ibas; nadie improvisa) y las malas RAMIFICAN (la pifia cierra la puerta que usabas y obliga a abrir otra). Por eso la misma palanca —quedarse un dado de dos— añade previsibilidad hacia arriba y caos hacia abajo, y por eso el peor de dos ya trae el caos puesto sin herramientas extra.
- **Las cinco palancas** y su vector (centro / dispersión / espectáculo):
  1. Lectura mejor o peor de 2d10: mueve el centro (media 7,15 o 3,85 frente a 5,5) Y concentra (DT 2,35 vs 2,87). Es DIAGONAL: vive en las esquinas de la columna previsible.
  2. Suma 2d10: no mueve el centro, concentra al máximo (DT 2,03 equivalente), apaga el espectáculo (extremos 3 %).
  3. Bandas naturales, en tres anchuras: ESTRECHA (los dos dados de acuerdo: doble 1 / doble 10), NORMAL (el número que usas: 1 / 10), ANCHA (ese y el de al lado: 1–2 / 9–10). Se leen SIEMPRE sobre el número que usas, así que se inclinan solas según el tono: en el mejor de dos, ensanchar da 4/36; en el peor, 36/4; en el rojo, 20/20.
  4. Éxito con coste (herramienta PbtA): ocupa LA TN Y EL PUNTO DE ENCIMA (total 6 o 7 con TN 6). No cambia cuántas veces sales adelante; solo cuántas de esas veces pagas (ED-23).
  5. TN: única palanca de optimismo puro, PERO NO se usa para construir el cuadrante (ED-19). Un número por lectura: 6 (dado, mejor, peor) y 11 (suma).
- **Palancas descartadas y por qué**: dados explosivos (rompen el anclaje [−2,+4]); mejor de 3 (mismo vector, más dados); mover el anclaje (obliga a rehacer fichas); que el jugador elija la lectura tras ver los dados (el tono lo ponen mesa y DJ antes de tirar); qué hace una pifia (no es palanca: es decisión del narrador; la complicación pequeña vive en el éxito con coste).
- **LAS SIETE** (cifras exactas con bono 0: pifia / fallo / coste / éxito / crítico → sale adelante; y el recorrido de −2 a +4):
  - **Épica** (optimista·previsible): mejor de 2d10, TN 6, bandas normales. 1/24/0/56/19 → 75 %. 51 → 99 %.
  - **Pulp desenfrenado** (optimista·caótico): mejor de 2d10, TN 6, pifia ancha (1–2), crítico normal (10), coste. 4/21/24/32/19 → 75 %. 51 → 96 %. El coste va del 32 % con −2 al 5 % con +4: el maestro no negocia.
  - **Realista** (neutral·previsible): suma 2d10, TN 11, extremos 2–3 / 19–20. 3/42/0/52/3 → 55 %. 36 → 85 %.
  - **Primera marcha** (neutral·neutral): dado rojo, TN 6, bandas normales. 10/40/0/40/10 → 50 %. 30 → 90 %. Es la vara de medir: diez puntos por escalón de bono.
  - **Bola de nieve** (neutral·caótico): dado rojo, TN 6, bandas anchas (1–2 / 9–10), coste. 20/30/20/10/20 → 50 %. 30 → 80 %.
  - **Angustia** (opresivo·previsible): peor de 2d10, TN 6, bandas estrechas (dobles). 1/74/0/24/1 → 25 %. 9 → 81 %. Es donde más pesa la ficha (72 puntos).
  - **Pesadilla** (opresivo·caótico): peor de 2d10, TN 6, bandas normales. 19/56/0/24/1 → 25 %. 9 → 81 %. Con +4 desaparece el fallo limpio: el gran maestro no falla, pifia.
- **La fila decide, la columna cobra**: en cada fila la caótica SALE ADELANTE EXACTAMENTE IGUAL DE A MENUDO que su compañera (Pulp = Épica, Bola = Primera marcha, Pesadilla = Angustia). Solo cambia el precio, y cada fila lo cobra en su moneda: arriba el coste, abajo la pifia, en medio las dos.
- **Cuánto improvisa el DJ** (pifia + coste, la cuenta que decide si una tarjeta aguanta una campaña): Épica 1 %, Angustia 1 %, Realista 3 %, Primera marcha 10 %, Pesadilla 19 %, Pulp 24 %, Bola de nieve 40 %. La escalera separa las tres columnas sin solaparse.
- **Aviso obligatorio en el manual**: el caos FRUSTRA salvo que la mesa acuerde explícitamente que se persigue la historia y no el éxito. La Pesadilla es para una noche sucia o una escena corta, no para una campaña de un año. Y en la Angustia, el fallo debe restar siempre algo (un camino, el tiempo, la ocasión) o el desgaste se vuelve tedio.
- **Dos huecos reales**: optimista·neutral y opresivo·neutral. Con dado plano no hay forma de inclinar el tono sin mover la TN, y la TN no se mueve. Se dibujan a la vista y se invita a rellenarlos. En la app, cuando el cuestionario cae en un hueco se pregunta a qué vecina arrimarse.
- **Lectura como espectro**: los ejes no son binarios; cerca de un borde se toma prestada una parte de la vecina (p. ej. la banda un paso más ancha, sin el coste).
- **Recetas que sí mueven la TN**: Tragedia = suma 2d10 vs TN 14 (3/69/0/25/3 → 28 % con bono 0; 15 → 64 %).
- **ED-18 (regla única de naturales)**: «mira el número que vas a usar; si cae en la banda de pifia, es pifia; si cae en la de crítico, es crítico». Con banda normal reproduce exactamente los valores antiguos (mejor de 2: 1 % y 19 % = doble 1 / cualquier 10; peor de 2: 19 % y 1 %). La suma conserva 2–3 y 19–20.
- **ED-19 (la TN no es palanca de tono)**: un número por lectura (6 y 11).
- **ED-20 (el centro es la costumbre, no la objetividad)**: la columna central es el dado plano porque es lo que hace el hobby, no porque sea el punto medio estadístico; de hecho es la lectura más aleatoria.
- **ED-21 (el centro caótico lleva las dos herramientas)**: bandas anchas y coste a la vez, porque ninguna inclina el tono.
- **ED-23 (dónde va el éxito con coste)**: en la TN y el punto de encima. En 5–6 ascendía un fallo a éxito con coste, o sea regalaba partidas; la herramienta de la que viene solo cobra peaje a lo que ya había salido bien.
- **ED-24 (crítico amplifica, pifia ramifica)**: por eso el pesimismo (fallar más) y el caos (fallar y además complicarse) entran juntos por la misma puerta en la fila opresiva, y por eso ahí basta con ensanchar la banda un paso.
- **ED-15 (revisada)**: en Acelerado, el Agobio junta lo que el manual completo separa (peor de dos + éxito con coste), porque allí solo hay tres modos y no hay eje de caos. El coste usa la misma regla: total 6 o 7. Profesional (+2): sale adelante el 49 %, y solo la mitad de esas veces sin pagar.
- **Tarjetas retiradas**: T0–T6 y las recetas del panel anterior quedan superadas por las siete. Su rastro se conserva en el Cuaderno de Diseño.
- **Nombres (decididos por el autor)**: Épica · Pulp desenfrenado · Realista · Primera marcha · Bola de nieve · Angustia · Pesadilla. En inglés: Epic · Unleashed Pulp · Realist · First Gear · Snowball · Anguish · Nightmare. «Primera marcha» además indica uso: se explica la primera, se empieza ahí mientras no haya tono claro y se vuelve ahí cuando la partida cambia de terreno. «Tragedia» conserva su nombre para sus propios dados (receta).
- **ED-22 (un nombre por idea)**: glosario cerrado. Cuadrante (el mapa de tonos), Ámbito (la capa de la pirámide), Rejilla (la escala de poder), [Rejilla] (la etiqueta de equipo), Guardia (antes «Disposición»), Banda (rango natural), Éxito con coste, Llave, Firma, Estilo, Vida fractal, Baúl frente a Bazar, Decorado. En inglés: Quadrant, Sphere, Power Grid, [Grid], Guard, Band, Success at a cost, Key, Signature, Style, Fractal Health, Chest, Set dressing.
"""
c = c[:i] + BLOQUE + c[j:]
io.open('CANON.md', 'w', encoding='utf-8').write(c)

# ---------------- cuaderno ----------------
e = io.open('frag_editorial.html', encoding='utf-8').read()
if 'ED-23' not in e:
    ROWS = """<tr><td class="num"><span class="flag ed">ED-23</span></td><td><strong>Dónde va el éxito con coste.</strong> En la TN y el punto de encima (total 6 o 7 con TN 6), nunca un punto más abajo. La versión anterior, en 5–6, ascendía un fallo a éxito con coste: regalaba partidas. Colocada arriba, la banda <strong>no cambia cuántas veces sales adelante</strong>, solo cuántas de esas veces pagas, que es lo que hace la herramienta de la que viene.</td><td><a href="#ch1-panel">1.4</a>, <a href="#maq-palancas">1.3 G</a></td></tr>
<tr><td class="num"><span class="flag ed">ED-24</span></td><td><strong>El crítico amplifica; la pifia ramifica.</strong> Una sorpresa buena va donde ya ibas y no obliga a nadie a inventar nada; una mala cierra la puerta que usabas y abre otra que no estaba. De ahí que la misma palanca añada previsibilidad hacia arriba y caos hacia abajo, y que en la fila opresiva el caos entre por la pifia en vez de por el coste: el peor de dos ya lo trae puesto.</td><td><a href="#maq-palancas">1.3 G</a></td></tr>
<tr><td>Las siete, cerradas</td><td>Cada tarjeta caótica sale adelante exactamente igual de a menudo que su compañera de fila; lo único que cambia es el precio. Y la cuenta que decide si una tarjeta aguanta una campaña es cuánto tiene que improvisar el DJ: 1&nbsp;% en Épica y Angustia, 3&nbsp;% en Realista, 10&nbsp;% en Primera marcha, 19&nbsp;% en Pesadilla, 24&nbsp;% en Pulp y 40&nbsp;% en Bola de nieve.</td><td><a href="#maq-cuadrante">1.3 I</a></td></tr>
<tr><td>El caos frustra</td><td>Decisión del autor: decirlo en el manual con todas las letras. La columna caótica solo funciona si la mesa ha acordado que se persigue la historia y no el éxito. Y la Angustia necesita su propia instrucción: que el fallo reste siempre algo, o el desgaste se vuelve tedio.</td><td><a href="#ch1-panel">1.4</a></td></tr>
"""
    anchor = '</tbody></table></div>\n\n<h3 id="ed-abiertas">'
    assert e.count(anchor) == 1
    e = e.replace(anchor, ROWS + anchor)
    io.open('frag_editorial.html', 'w', encoding='utf-8').write(e)

# ---------------- Acelerado ----------------
patch('frag_acelerado.html', [
    ('Total 4 o menos: fallo · 5–6: <strong>éxito parcial</strong> · 7 o más: éxito',
     'Total 5 o menos: fallo · 6 o 7: <strong>éxito parcial</strong> · 8 o más: éxito'),
    ('Son las de la zona de roce del manual completo —la TN y el punto justo por debajo: 4 o menos fallo, 5–6 parcial, 7 o más éxito— aplicadas al dado menor. Confirmado por el autor.',
     'Son las del manual completo: el éxito con coste ocupa la TN y el punto de encima (total 6 o 7), aplicado al dado menor. Nunca convierte un fallo en éxito; solo cobra peaje a lo que ya había salido bien. Confirmado por el autor.'),
    ('en Agobio, un profesional (+2) sale adelante un 64 % de las veces, pero solo un 36 % s',
     'en Agobio, un profesional (+2) sale adelante un 49 % de las veces, y solo la mitad de esas veces sin pagar nada: s'),
    ('en Agobio, el 64 %, y más de la mitad de esas veces pagando un precio',
     'en Agobio, el 49 %, y la mitad de esas veces pagando un precio'),
    ('Bandas de Agobio sobre el dado menor: 4 o menos fallo, 5–6 parcial, 7 o más éxito (la zona de roce del manual completo)',
     'Éxito con coste en Agobio, sobre el dado menor: total 6 o 7, la misma regla que el manual completo. En Acelerado el Agobio junta lo que el completo separa (peor de dos y éxito con coste), porque aquí no hay eje de caos'),
])
patch('frag_acelerado.en.html', [
    ('Total 4 or less: failure · 5–6: <strong>partial success</strong> · 7 or more: success',
     'Total 5 or less: failure · 6 or 7: <strong>partial success</strong> · 8 or more: success'),
    ('in Dread, a professional (+2) gets through 64% of the time, but only 36% of the time (',
     'in Dread, a professional (+2) gets through 49% of the time, and only half of those without paying (',
    ),
    ('in Dread, 64%, and more than half of those times paying a price',
     'in Dread, 49%, and half of those times paying a price'),
])
print('faltan:', MISS if MISS else 'nada')
