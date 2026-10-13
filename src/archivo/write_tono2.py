# -*- coding: utf-8 -*-
"""Reescribe G/H/I de la Sala de Máquinas (1.3) y el Apéndice D con el cuadrante de siete tarjetas."""
import io, os
from write_tono import ES, EN, IDS, BON, D, pct, r, bonus_table, quad_table, banda

os.chdir(os.path.dirname(os.path.abspath(__file__)))

WHY = {
 'OP': ('El mejor de dos hace dos cosas a la vez: sube la media de 5,5 a 7,15 y estrecha la dispersión (desviación típica 2,35 frente a 2,87 del dado plano). Es la única palanca que empuja en diagonal, y por eso ocupa la esquina optimista de la columna ordenada. Su 19&nbsp;% de críticos no la vuelve caótica: un crítico confirma el rumbo, no lo parte.',
        'Keeping the higher of two does two things at once: it raises the mean from 5.5 to 7.15 and narrows the spread (standard deviation 2.35 against the flat die’s 2.87). It is the only lever that pushes diagonally, which is why it sits in the optimistic corner of the ordered column. Its 19&nbsp;% criticals do not make it chaotic: a critical confirms the direction, it does not break it.'),
 'OC': ('La misma lectura y la misma probabilidad de salir adelante que la Épica, bono a bono. Lo único que cambia es el precio: el éxito con coste cobra peaje a los que aciertan justo, y eso son 32 de cada 100 tiradas para un personaje flojo y solo 5 para un gran maestro. Cuanto mejor eres, menos negocias.',
        'The same reading and the same chance of working out as the Epic, bonus by bonus. The only difference is the price: success at a cost charges a toll on those who just make it, and that is 32 rolls in 100 for a weak character and only 5 for a grand master. The better you are, the less you negotiate.'),
 'NP': ('La campana. Los extremos caen al 3&nbsp;%, el bono manda de principio a fin y el salto entre escalones se va suavizando (9, 10, 9, 8, 7 y 6 puntos): un mundo donde mejorar rinde cada vez menos, que es lo que pasa en un mundo de reloj.',
        'The bell curve. The extremes drop to 3&nbsp;%, the bonus rules from start to finish and each step gets gentler (9, 10, 9, 8, 7 and 6 points): a world where improving pays less and less, which is what a clockwork world does.'),
 'NN': ('Un solo dado lineal: cada cara vale un 10&nbsp;% y el bono mueve la aguja de diez en diez. Ojo con el nombre de la columna: un dado plano no es el punto medio estadístico —de hecho es lo más aleatorio que hay aquí— sino el <strong>punto medio de la costumbre</strong>. Es lo que hace casi todo el hobby, y por eso es la referencia contra la que se mide el resto. <span class="flag ed">ED-20</span>',
        'A single linear die: each face is worth 10&nbsp;% and the bonus moves the needle ten points at a time. Careful with the column’s name: a flat die is not the statistical middle —it is in fact the most random thing here— but the <strong>middle of the habit</strong>. It is what most of the hobby does, and that is why it is the yardstick for the rest. <span class="flag ed">ED-20</span>'),
 'NC': ('La costumbre con las dos herramientas encima. Sale adelante igual que la Primera marcha, pero la pifia y el crítico se doblan hasta el 20&nbsp;% y un quinto de lo que consigues viene con factura. Es la única tarjeta donde los cinco resultados rondan la misma probabilidad. <span class="flag ed">ED-21</span>',
        'The habit with both tools on top. It works out as often as First Gear, but fumble and critical double to 20&nbsp;% and a fifth of what you get comes with a bill. It is the only card where all five outcomes sit at roughly the same probability. <span class="flag ed">ED-21</span>'),
 'PP': ('El espejo exacto de la Épica: media 3,85 y las bandas pegadas al suelo, un 1&nbsp;% arriba y otro abajo. Y el dato que sorprende: es la tarjeta donde más pesa la ficha, del 9&nbsp;% al 81&nbsp;%, porque el peor de dos amontona los resultados justo en la zona donde el bono decide.',
        'The exact mirror of the Epic: mean 3.85 and both bands pinned to the floor, 1&nbsp;% above and 1&nbsp;% below. And the surprising figure: it is the card where the sheet weighs most, from 9&nbsp;% to 81&nbsp;%, because the lower of two piles results up exactly where the bonus decides.'),
 'PC': ('La misma lectura que la Angustia con la banda un paso más ancha, y ahí está la demostración del eje: <strong>sale adelante exactamente igual de a menudo</strong> en los siete bonos, porque con el peor de dos un 1 no llega a la TN ni con +4. Lo único que cambia es que dieciocho de cada cien fallos pasan de callarse a hablar. Y con +4 el fallo limpio desaparece: el gran maestro ya no falla, pifia.',
        'The same reading as Anguish with the band one step wider, and there is the proof of the axis: <strong>it works out exactly as often</strong> at all seven bonuses, because with the lower of two a 1 never reaches the TN, not even at +4. The only change is that eighteen failures in a hundred stop being silent. And at +4 clean failure disappears: the grand master no longer fails, they fumble.'),
}
LEVERS = [
 ('1. La lectura: el mejor o el peor de dos', '1. The reading: the higher or the lower of two',
  'Sube la media a 7,15 o la baja a 3,85', 'Raises the mean to 7.15 or lowers it to 3.85',
  'La estrecha (2,35)', 'Narrows it (2.35)',
  'Dobla los dieces (19&nbsp;%) o los unos (19&nbsp;%)', 'Doubles tens (19&nbsp;%) or ones (19&nbsp;%)',
  'Esquinas de la columna previsible', 'Corners of the predictable column'),
 ('2. La suma de los dos', '2. The sum of the two',
  'No lo mueve', 'Does not move it',
  'La estrecha al máximo (2,03)', 'Narrows it as far as it goes (2.03)',
  'Lo apaga: extremos al 3&nbsp;%', 'Switches it off: extremes at 3&nbsp;%',
  'Centro de la columna previsible', 'Centre of the predictable column'),
 ('3. Las bandas: estrecha, normal o ancha', '3. The bands: narrow, normal or wide',
  'No lo mueve', 'Does not move it',
  'No la cambia', 'Does not change it',
  'Lo multiplica o lo apaga: 20/20 en el rojo, 4/36 en el mejor, 36/4 en el peor', 'Multiplies or mutes it: 20/20 on the red die, 4/36 on the higher, 36/4 on the lower',
  'Toda la fila opresiva y la columna caótica', 'The whole oppressive row and the chaotic column'),
 ('4. El éxito con coste (la herramienta PbtA)', '4. Success at a cost (the PbtA tool)',
  'No lo mueve: solo cobra a los que ya ganaban', 'Does not move it: it only charges those who were already winning',
  'No la cambia', 'Does not change it',
  'Convierte cuatro resultados en cinco', 'Turns four outcomes into five',
  'Columna caótica de las filas optimista y neutral', 'Chaotic column of the optimistic and neutral rows'),
 ('5. La dificultad (TN)', '5. The difficulty (TN)',
  'Es la única palanca de optimismo puro', 'The only lever of pure optimism',
  'No la cambia', 'Does not change it',
  'No lo cambia', 'Does not change it',
  'Fuera del cuadrante: solo en recetas', 'Outside the quadrant: recipes only'),
]


def sec_G(L):
    es = L is ES
    t = lambda a, b: a if es else b
    h = ['<h3 id="maq-palancas">%s</h3>' % t('G. Las cinco palancas', 'G. The five levers')]
    h.append('<p>' + t(
        'Un sistema de tonos se construye moviendo cinco cosas, y casi todas las discusiones sobre dados se enredan porque mezclan tres efectos distintos. Aquí van separados: el <strong>centro</strong> (cuántas veces sale adelante), la <strong>dispersión</strong> (cuánto manda el dado frente a la ficha) y el <strong>espectáculo</strong> (cada cuánto pasa algo memorable). Una palanca puede mover uno, dos o los tres.',
        'A tone system is built by moving five things, and most arguments about dice get tangled because they mix three different effects. Here they are kept apart: the <strong>centre</strong> (how often it works out), the <strong>spread</strong> (how much the die rules over the sheet) and the <strong>spectacle</strong> (how often something memorable happens). A lever can move one, two or all three.') + '</p>')
    h.append('<div class="tw"><table class="t"><thead><tr><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr></thead><tbody>' % (
        t('Palanca', 'Lever'), t('Centro', 'Centre'), t('Dispersión', 'Spread'), t('Espectáculo', 'Spectacle'), t('Dónde se usa', 'Where it is used')))
    for row in LEVERS:
        i = 0 if es else 1
        h.append('<tr><td><strong>%s</strong></td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % (
            row[0 + i], row[2 + i], row[4 + i], row[6 + i], row[8 + i]))
    h.append('</tbody></table></div>')
    h.append('<p>' + t(
        '<strong>La palanca 1 es diagonal</strong>, y ese es el hallazgo que ordena todo lo demás: quedarse el mejor de dos es optimista <em>y</em> ordenado a la vez, porque amontona los resultados arriba. Por eso las lecturas de dos dados viven en las esquinas de la columna ordenada y no en el centro.',
        '<strong>Lever 1 is diagonal</strong>, and that is the finding that puts everything else in order: keeping the higher of two is optimistic <em>and</em> orderly at once, because it piles results up at the top. That is why the two-dice readings live in the corners of the ordered column and not in the middle.') + '</p>')
    h.append('<p>' + t(
        '<strong>Y el crítico y la pifia no pesan igual.</strong> Una sorpresa buena <em>amplifica</em>: el crítico va donde ya ibas y nadie tiene que inventar nada. Una sorpresa mala <em>ramifica</em>: la pifia cierra la puerta que estabas usando y obliga a abrir otra que no estaba. Por eso la misma palanca añade previsibilidad hacia arriba y caos hacia abajo, y por eso el peor de dos ya trae el caos puesto sin necesidad de ninguna herramienta más. <span class="flag ed">ED-24</span>',
        '<strong>And criticals and fumbles do not weigh the same.</strong> A good surprise <em>amplifies</em>: the critical goes where you were already going and nobody has to invent anything. A bad surprise <em>branches</em>: the fumble closes the door you were using and forces another one open that was not there. That is why the same lever adds predictability upwards and chaos downwards, and why the lower of two already carries the chaos without needing any further tool. <span class="flag ed">ED-24</span>') + '</p>')
    h.append('<p>' + t(
        '<strong>Las bandas se aplican al número que usas</strong>, no a los dados sueltos, y por eso se inclinan solas hacia el tono de la casilla: con el mejor de dos, ensancharlas casi solo trae milagros (4&nbsp;% de pifias contra 36&nbsp;% de críticos) y con el peor casi solo desastres (36&nbsp;% contra 4&nbsp;%). La misma herramienta, otro efecto según el tono, sin una sola regla extra.',
        '<strong>The bands apply to the number you use</strong>, not to the individual dice, and that is why they lean towards the tone of their cell on their own: with the higher of two, widening them brings almost nothing but miracles (4&nbsp;% fumbles against 36&nbsp;% criticals) and with the lower almost nothing but disasters (36&nbsp;% against 4&nbsp;%). The same tool, a different effect depending on the tone, without a single extra rule.') + '</p>')
    h.append('<p>' + t(
        '<strong>El éxito con coste ocupa la TN y el punto de encima.</strong> Ahí, y no un punto más abajo: si la banda bajara al punto anterior estaría ascendiendo un fallo a éxito, es decir, regalando partidas, y eso no es lo que hace la herramienta de la que viene. Colocada así <strong>no cambia cuántas veces sales adelante</strong>, solo cuántas de esas veces pagas. <span class="flag ed">ED-23</span>',
        '<strong>Success at a cost takes the TN and the point above it.</strong> There, and not one point lower: a band one step down would be promoting a failure into a success, which is giving games away, and that is not what the tool it comes from does. Placed like this it <strong>does not change how often you get there</strong>, only how often you pay. <span class="flag ed">ED-23</span>') + '</p>')
    h.append('<p>' + t(
        '<strong>La dificultad se queda quieta a propósito.</strong> Un número para las tiradas de un dado (6) y otro para las sumas (11), y se acabó. Mover la TN sería la palanca de optimismo más limpia que existe, pero obliga a la mesa a recordar un número distinto en cada escena, y esa es exactamente la fricción que este juego promete quitarte. Solo las <em>recetas</em> la tocan, y lo dicen en voz alta.',
        '<strong>The difficulty stays put on purpose.</strong> One number for single-die rolls (6) and another for sums (11), and that is that. Moving the TN would be the cleanest optimism lever there is, but it forces the table to remember a different number in every scene, and that is exactly the friction this game promises to take away. Only the <em>recipes</em> touch it, and they say so out loud.') + '</p>')
    h.append('<p><strong>%s</strong></p>' % t(
        'Una palanca por columna, y la fila elige la dirección. Esa es toda la arquitectura del cuadrante.',
        'One lever per column, and the row picks the direction. That is the whole architecture of the quadrant.'))
    h.append('<h4>%s</h4>' % t('Las palancas que existen y no usamos', 'The levers that exist and we do not use'))
    h.append('<dl>')
    for a, b in [
        (('Dados explosivos', 'Exploding dice'),
         ('Un 10 vuelve a tirarse y se suma. Cola infinita: rompe el anclaje de [−2, +4] y con él todas las etiquetas de daño.',
          'A 10 is rolled again and added. An infinite tail: it breaks the [−2, +4] anchor and, with it, every damage tag.')),
        (('Quedarse el mejor de tres', 'Keeping the best of three'),
         ('Empuja en la misma dirección que la palanca 1, pero más fuerte y con un dado más en la mesa. No aporta un tono que no tengamos.',
          'It pushes in the same direction as lever 1, only harder and with one more die on the table. It does not add a tone we do not already have.')),
        (('Mover el anclaje [−2, +4]', 'Moving the [−2, +4] anchor'),
         ('Decide si manda la ficha o el dado, así que es una palanca de verdad. Pero cambiarla obliga a repasar todas las fichas, y la tesis del juego es cambiar de reglas sin tocar la ficha.',
          'It decides whether the sheet or the die rules, so it is a real lever. But changing it means revisiting every sheet, and the thesis of this game is changing rules without touching the sheet.')),
        (('Que el jugador elija la lectura al ver los dados', 'Letting the player pick the reading after seeing the dice'),
         ('Convierte el caos en decisión, que es elegante, pero mueve el tono al lado del jugador. El tono lo ponen la mesa y el DJ antes de tirar; si nadie dice nada, vale el de la campaña.',
          'It turns chaos into a decision, which is elegant, but it moves tone to the player’s side of the table. Tone is set by the table and the GM before the roll; if nobody says otherwise, the campaign’s tone applies.')),
        (('Qué hace una pifia', 'What a fumble does'),
         ('No es una palanca de reglas. Una pifia es un fallo bien feo, y cuánto duele lo decide quien narra, según el tono y la mesa. La complicación pequeña ya tiene su sitio: el éxito con coste.',
          'It is not a rules lever. A fumble is an ugly failure, and how much it hurts is decided by whoever is narrating, according to the tone and the table. The small complication already has its place: success at a cost.')),
    ]:
        i = 0 if es else 1
        h.append('<dt>%s</dt><dd>%s</dd>' % (a[i], b[i]))
    h.append('</dl>')
    return '\n'.join(h)


def regla(cid, L):
    c = D[cid]
    t = lambda a, b: a if L is ES else b
    rd = {'rojo': t('dado rojo', 'red die only'), 'mejor': t('mejor de 2d10', 'higher of 2d10'),
          'peor': t('peor de 2d10', 'lower of 2d10'), 'suma': t('suma de 2d10', 'sum of 2d10')}[c['read']]
    s = '%s + %s · TN %d · %s %s / %s' % (rd, t('bono', 'bonus'), c['tn'], t('bandas', 'bands'), banda(cid, 0, L), banda(cid, 1, L))
    if c['coste']:
        s += ' · ' + t('coste si el total es %d o %d' % (c['tn'], c['tn'] + 1), 'cost if the total is %d or %d' % (c['tn'], c['tn'] + 1))
    return s


def sec_H(L):
    es = L is ES
    t = lambda a, b: a if es else b
    h = ['<h3 id="maq-siete">%s</h3>' % t('H. Las siete tarjetas, una a una', 'H. The seven cards, one by one')]
    h.append('<p>%s</p>' % t(
        'Cada tabla va del nulo (−2) al gran maestro (+4). <em>Sale adelante</em> suma el éxito con coste, el éxito limpio y el crítico. Cada fila suma 100&nbsp;%.',
        'Each table runs from the useless (−2) to the grand master (+4). <em>Works out</em> adds success at a cost, clean success and critical. Each row adds up to 100&nbsp;%.'))
    for cid in IDS:
        h.append('<h4>%s (%s) %s</h4>' % (L['name'][cid], L['cell'][cid], L['quote'][cid]))
        h.append('<p><em>%s</em> %s.</p>' % (t('Regla:', 'Rule:'), regla(cid, L)))
        h.append(bonus_table(cid, L))
        h.append('<p><strong>%s</strong> %s</p>' % (t('Por qué encaja:', 'Why it fits:'), WHY[cid][0 if es else 1]))
    return '\n'.join(h)


def sec_I(L):
    es = L is ES
    t = lambda a, b: a if es else b
    h = ['<h3 id="maq-cuadrante">%s</h3>' % t('I. El cuadrante: siete tarjetas y dos huecos', 'I. The quadrant: seven cards and two gaps')]
    h.append('<p>%s</p>' % t(
        'Nueve sitios, siete tarjetas. Los dos huecos están donde el universo tiene postura pero el dado no tiene curva, y ahí no hay nada que hacer sin mover la dificultad. Se dejan a la vista.',
        'Nine places, seven cards. The two gaps sit where the universe has a stance but the die has no curve, and there is nothing to be done there without moving the difficulty. They are left in plain sight.'))
    h.append(quad_table(L))
    h.append('<div class="rule"><p class="rule-title">%s</p><p>%s</p><p>%s</p></div>' % (
        t('La fila decide; la columna cobra', 'The row decides; the column charges'),
        t('En cada fila, la tarjeta caótica <strong>sale adelante exactamente igual de a menudo</strong> que su compañera. Pulp da el mismo 51 · 64 · 75 · 84 · 91 · 96 que la Épica; la Bola de nieve, el mismo 30 · 40 · 50 · 60 · 70 · 80 que la Primera marcha; y la Pesadilla, el mismo 9 · 16 · 25 · 36 · 49 · 64 · 81 que la Angustia. Lo único que cambia es el precio.',
          'In each row, the chaotic card <strong>works out exactly as often</strong> as its companion. Pulp gives the same 51 · 64 · 75 · 84 · 91 · 96 as the Epic; Snowball the same 30 · 40 · 50 · 60 · 70 · 80 as First Gear; and Nightmare the same 9 · 16 · 25 · 36 · 49 · 64 · 81 as Anguish. The only difference is the price.'),
        t('Y cada fila cobra en su moneda: arriba lo cobra el <strong>coste</strong>, abajo lo cobra la <strong>pifia</strong>, y en el medio las dos cosas a la vez. Por eso la columna caótica no necesita la misma herramienta en las tres filas: necesita la que sea barata en cada una.',
          'And each row charges in its own coin: at the top the <strong>cost</strong> charges, at the bottom the <strong>fumble</strong> does, and in the middle both at once. That is why the chaotic column does not need the same tool in all three rows: it needs whichever one is cheap in each.')))
    h.append('<p>%s</p>' % t(
        'La cuenta que más le importa al DJ es otra: <strong>cada cuántas tiradas tiene que inventar algo</strong>, sumando pifias y costes. Sale 1&nbsp;% en la Épica y en la Angustia, 3&nbsp;% en la Realista, 10&nbsp;% en la Primera marcha, 19&nbsp;% en la Pesadilla, 24&nbsp;% en el Pulp y 40&nbsp;% en la Bola de nieve. Esa escalera separa las tres columnas sin que se toquen, y es la que conviene mirar antes de elegir tarjeta para una campaña larga.',
        'The figure that matters most to the GM is a different one: <strong>how often they have to invent something</strong>, adding up fumbles and costs. It comes to 1&nbsp;% on the Epic and on Anguish, 3&nbsp;% on the Realist, 10&nbsp;% on First Gear, 19&nbsp;% on Nightmare, 24&nbsp;% on Pulp and 40&nbsp;% on Snowball. That ladder separates the three columns without any overlap, and it is the one to look at before picking a card for a long campaign.'))
    h.append('<p>%s</p>' % t(
        'Dos efectos de borde que son decisiones, no casualidades. Con +4, <strong>el coste casi desaparece</strong> en las tarjetas que lo llevan (del 32&nbsp;% al 5&nbsp;% en el Pulp): el maestro ya no negocia. Y en la Pesadilla, con ese mismo +4, <strong>desaparece el fallo limpio</strong>: lo que no sale es siempre un desastre. La competencia no te quita el caos; te cambia la moneda con la que lo pagas.',
        'Two edge effects that are decisions, not accidents. At +4, <strong>the cost almost disappears</strong> on the cards that carry it (from 32&nbsp;% to 5&nbsp;% on Pulp): the master no longer negotiates. And on Nightmare, at that same +4, <strong>clean failure disappears</strong>: whatever does not work out is always a disaster. Competence does not take the chaos away from you; it changes the coin you pay it in.'))
    h.append('<aside class="meta"><p>%s</p></aside>' % t(
        'No lo leas como nueve cajas cerradas. Las dos preguntas del cuestionario colocan tu partida en un punto del mapa, y lo normal es caer cerca de un borde: entonces te quedas con la lectura de tu casilla y tomas prestada solo una parte de la vecina —la banda un paso más ancha, por ejemplo, sin el coste—. Y si caes en un hueco, ya sabes lo que hay: ese sitio está vacío y es tuyo.',
        'Do not read it as nine closed boxes. The two questions of the questionnaire place your game at a point on the map, and landing near an edge is the normal case: then you keep your cell’s reading and borrow only part of its neighbour —the band one step wider, say, without the cost. And if you land in a gap, you know what you have: that place is empty, and it is yours.'))
    return '\n'.join(h)


def apxD(L):
    es = L is ES
    t = lambda a, b: a if es else b
    h = []
    for cid in IDS:
        h.append('<h3 id="apxd-%s">%s · %s</h3>' % (cid.lower(), L['name'][cid], L['cell'][cid]))
        h.append('<p>%s.</p>' % regla(cid, L))
        h.append(bonus_table(cid, L))
    h.append('<h3 id="apxd-recetas">%s</h3>' % t('Recetas: cuando la dificultad sí se mueve', 'Recipes: when the difficulty does move'))
    h.append('<p>%s</p>' % t(
        'El cuadrante no toca la TN, pero una receta puede hacerlo si lo dice claro y para toda la campaña. La <strong>Tragedia</strong> es la única del manual: la suma de siempre con la vara puesta en 14. El mismo mundo de reloj, pero con la esperanza fuera del alcance.',
        'The quadrant never touches the TN, but a recipe may do so if it says so clearly and for the whole campaign. <strong>Tragedy</strong> is the only one in the manual: the usual sum with the bar set at 14. The same clockwork world, with hope out of reach.'))
    h.append('<h4>%s</h4>' % t('Tragedia · suma de 2d10 vs TN 14', 'Tragedy · sum of 2d10 vs TN 14'))
    h.append(bonus_table('TRAG', L))
    return '\n'.join(h)


def patch(path, L, ill):
    s = io.open(path, encoding='utf-8').read()
    a, b = s.index('<h3 id="maq-tarjetas">'), s.index('<div class="rule"><p class="rule-title">%s</p>' % ill)
    s = s[:a] + sec_G(L) + '\n' + sec_H(L) + '\n' + sec_I(L) + '\n' + s[b:]
    a = s.index('<h3 id="apxd-')
    b = s.index('<h3 id="apxd-medias">')
    s = s[:a] + apxD(L) + '\n' + s[b:]
    io.open(path, 'w', encoding='utf-8').write(s)
    print('parcheado', path, len(s.encode()) // 1024, 'KB')


patch('frag_math.html', ES, 'La ilusión del +4')
patch('frag_math.en.html', EN, 'The +4 illusion')
