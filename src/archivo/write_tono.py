# -*- coding: utf-8 -*-
"""Reescribe el capítulo de Tarjetas de Tono (1.4) con el cuadrante de siete tarjetas."""
import io, json, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
D = json.load(open('siete.json', encoding='utf-8'))
BON = [-2, -1, 0, 1, 2, 3, 4]
IDS = ['OP', 'OC', 'NP', 'NN', 'NC', 'PP', 'PC']

ES = dict(
    name={'OP': 'Épica', 'OC': 'Pulp desenfrenado', 'NP': 'Realista', 'NN': 'Primera marcha', 'NC': 'Bola de nieve', 'PP': 'Angustia', 'PC': 'Pesadilla'},
    cell={'OP': 'Optimista · Previsible', 'OC': 'Optimista · Caótico', 'NP': 'Neutral · Previsible', 'NN': 'Neutral · Neutral',
          'NC': 'Neutral · Caótico', 'PP': 'Opresivo · Previsible', 'PC': 'Opresivo · Caótico'},
    quote={'OP': '«Soy el mejor en lo que hago.»', 'OC': '«Sale, pero prepárate para pagarlo.»',
           'NP': '«La vida es justa y predecible.»', 'NN': '«Todavía no sabemos qué tono queremos: empezamos aquí.»',
           'NC': '«Empieza siendo una tontería.»', 'PP': '«No quiero tirar.»', 'PC': '«No deberíamos haber venido.»'},
    roll={'OP': '2d10, <strong>quédate el ALTO</strong> + bono', 'OC': '2d10, <strong>quédate el ALTO</strong> + bono',
          'NP': '2d10, <strong>SUMA los dados</strong> + bono', 'NN': 'Solo el dado <strong>rojo</strong> + bono',
          'NC': 'Solo el dado <strong>rojo</strong> + bono', 'PP': '2d10, <strong>quédate el BAJO</strong> + bono',
          'PC': '2d10, <strong>quédate el BAJO</strong> + bono'},
    fx={
        'OP': 'Pifiar es casi imposible y uno de cada cinco golpes es memorable. Hasta quien no tiene nada que hacer aquí gana la mitad de las veces: los personajes brillan. Si el bono se sale del ancla, no tires: narra el éxito.',
        'OC': 'Sale adelante exactamente igual de a menudo que en la Épica; lo que cambia es el precio. Con un personaje flojo, un tercio de lo que consigue viene con factura; con un gran maestro, casi nada: <strong>el maestro no negocia</strong>. Anime, wuxia, capa y espada.',
        'NP': 'Curva de campana: los resultados se agrupan en el centro y casi nada es memorable. Planificar funciona; improvisar, no. Es la única tarjeta donde una investigación larga aguanta sin que un dado la parta.',
        'NN': 'La costumbre del hobby: un dado, sin curvas. Cada escalón de bono vale exactamente diez puntos. <strong>Empieza aquí</strong> mientras no tengáis claro el tono, y <strong>vuelve aquí</strong> cuando la partida cambie de terreno y no sepáis todavía dónde estáis. Es la vara con la que se miden las otras seis.',
        'NC': 'Sale adelante como en la Primera marcha, pero nada es seguro y nada es gratis: pifia, coste y crítico rondan el 20&nbsp;% siempre. Cada peaje suelto parece una tontería y tres escenas después la partida baja sola por la ladera. Es la que más le pide al DJ: cuatro de cada diez tiradas traen algo que inventar.',
        'PP': 'Falla mucho y falla callado. Es la tarjeta donde más pesa la ficha, del 9&nbsp;% al 81&nbsp;%: aquí no da miedo el monstruo, da miedo el dado. <strong>Que el fallo reste siempre algo</strong> —un camino, el tiempo, la ocasión—, o el desgaste se convierte en tedio.',
        'PC': 'La misma tirada que la Angustia: sale adelante exactamente igual de a menudo. Lo que cambia es que dieciocho de cada cien fallos pasan a hablar. Y con +4 ocurre algo notable: el fallo limpio desaparece, así que <strong>el gran maestro ya no falla: pifia</strong>.'},
    axes={'OP': 'Optimismo alto · Caos bajo', 'OC': 'Optimismo alto · Caos alto', 'NP': 'Optimismo neutro · Caos bajo',
          'NN': 'Optimismo neutro · Caos neutro', 'NC': 'Optimismo neutro · Caos alto', 'PP': 'Optimismo bajo · Caos bajo',
          'PC': 'Optimismo bajo · Caos alto'},
)
EN = dict(
    name={'OP': 'Epic', 'OC': 'Unleashed Pulp', 'NP': 'Realist', 'NN': 'First Gear', 'NC': 'Snowball', 'PP': 'Anguish', 'PC': 'Nightmare'},
    cell={'OP': 'Optimistic · Predictable', 'OC': 'Optimistic · Chaotic', 'NP': 'Neutral · Predictable', 'NN': 'Neutral · Neutral',
          'NC': 'Neutral · Chaotic', 'PP': 'Oppressive · Predictable', 'PC': 'Oppressive · Chaotic'},
    quote={'OP': '“I’m the best at what I do.”', 'OC': '“It works — now get ready to pay for it.”',
           'NP': '“Life is fair and predictable.”', 'NN': '“We don’t know what tone we want yet: we start here.”',
           'NC': '“It starts as nothing much.”', 'PP': '“I don’t want to roll.”', 'PC': '“We should never have come here.”'},
    roll={'OP': '2d10, <strong>keep the HIGHER</strong> + bonus', 'OC': '2d10, <strong>keep the HIGHER</strong> + bonus',
          'NP': '2d10, <strong>SUM the dice</strong> + bonus', 'NN': 'The <strong>red</strong> die only + bonus',
          'NC': 'The <strong>red</strong> die only + bonus', 'PP': '2d10, <strong>keep the LOWER</strong> + bonus',
          'PC': '2d10, <strong>keep the LOWER</strong> + bonus'},
    fx={
        'OP': 'Fumbling is almost impossible and one blow in five is memorable. Even someone with no business being here wins half the time: the characters shine. If the bonus runs past the anchor, do not roll: narrate the success.',
        'OC': 'It works out exactly as often as on the Epic; what changes is the price. For a weak character, a third of what they get comes with a bill; for a grand master, almost none: <strong>the master does not negotiate</strong>. Anime, wuxia, cloak and sword.',
        'NP': 'A bell curve: results cluster in the middle and almost nothing is memorable. Planning works; improvising does not. It is the only card where a long investigation survives without a die breaking it.',
        'NN': 'The hobby’s habit: one die, no curves. Every step of bonus is worth exactly ten points. <strong>Start here</strong> while the tone is still unclear, and <strong>come back here</strong> when the game moves to new ground and you do not know where you are yet. It is the yardstick for the other six.',
        'NC': 'It works out as often as on First Gear, but nothing is safe and nothing is free: fumble, cost and critical all sit near 20&nbsp;% throughout. Each single toll looks like nothing much, and three scenes later the game is rolling downhill on its own. It is the card that asks most of the GM: four rolls in ten bring something to invent.',
        'PP': 'It fails often and it fails quietly. This is where the sheet weighs most, from 9&nbsp;% to 81&nbsp;%: what frightens you here is not the monster, it is the die. <strong>Make the failure always take something away</strong> —a route, the time, the chance— or the grind turns into tedium.',
        'PC': 'The same roll as Anguish: it works out exactly as often. What changes is that eighteen failures in a hundred start to speak. And at +4 something striking happens: clean failure disappears, so <strong>the grand master no longer fails: they fumble</strong>.'},
    axes={'OP': 'High optimism · Low chaos', 'OC': 'High optimism · High chaos', 'NP': 'Neutral optimism · Low chaos',
          'NN': 'Neutral optimism · Neutral chaos', 'NC': 'Neutral optimism · High chaos', 'PP': 'Low optimism · Low chaos',
          'PC': 'Low optimism · High chaos'},
)


def pct(x):
    return '%d&nbsp;%%' % round(x * 100)


def r(cid, b):
    return D[cid]['rows'][str(b)]


def banda(cid, side, L):
    """Texto de la banda natural: estrecha / normal / ancha, o los extremos de la suma."""
    c = D[cid]
    es = L is ES
    if c['read'] == 'suma':
        return ('2–3', '19–20')[side]
    w = c['bp'] if side == 0 else c['bc']
    if w == 'estrecha':
        return ('doble 1', 'doble 10')[side] if es else ('double 1', 'double 10')[side]
    if w == 'normal':
        return ('1', '10')[side]
    return ('1–2', '9–10')[side]


def rules_dl(cid, L):
    c, d0 = D[cid], r(cid, 0)
    t = lambda a, b: a if L is ES else b
    h = '<dl class="card-rules">'
    h += '<dt>%s</dt><dd>%s</dd>' % (t('Tirada', 'Roll'), L['roll'][cid])
    h += '<dt>TN</dt><dd>%d</dd>' % c['tn']
    h += '<dt>%s</dt><dd>%s · %s</dd>' % (t('Banda de pifia', 'Fumble band'), banda(cid, 0, L), pct(d0['pifia']))
    h += '<dt>%s</dt><dd>%s · %s</dd>' % (t('Banda de crítico', 'Critical band'), banda(cid, 1, L), pct(d0['critico']))
    if c['coste']:
        h += '<dt>%s</dt><dd>%s</dd>' % (t('Éxito con coste', 'Success at a cost'),
                                         t('Si aciertas justo (total %d o %d), el DJ elige el precio' % (c['tn'], c['tn'] + 1),
                                           'If you just make it (total %d or %d), the GM picks the price' % (c['tn'], c['tn'] + 1)))
    h += '<dt>%s</dt><dd>%s</dd>' % (t('Sale adelante (bono 0)', 'Works out (bonus 0)'), pct(d0['gana']))
    return h + '</dl>'


def card_html(cid, L):
    return ('<article class="card" id="tono-%s">\n<p class="card-kicker">%s</p>\n<h4>%s</h4>\n'
            '<p class="card-axes">%s</p>\n<p class="card-quote">%s</p>\n%s\n<p class="card-fx">%s</p>\n</article>\n') % (
        cid.lower(), L['cell'][cid], L['name'][cid], L['axes'][cid], L['quote'][cid], rules_dl(cid, L), L['fx'][cid])


def bonus_table(cid, L):
    t = lambda a, b: a if L is ES else b
    h = ('<div class="tw"><table class="t"><thead><tr><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr></thead><tbody>' %
         (t('Bono', 'Bonus'), t('Pifia', 'Fumble'), t('Fallo', 'Failure'), t('Coste', 'Cost'), t('Éxito', 'Success'), t('Crítico', 'Critical'), t('Sale adelante', 'Works out')))
    for b in BON:
        d = r(cid, b)
        h += '<tr><td>%s</td>' % (('+%d' % b) if b > 0 else ('%d' % b).replace('-', '−'))
        for k in ('pifia', 'fallo', 'parcial', 'exito', 'critico'):
            h += '<td class="num">%s</td>' % pct(d[k])
        h += '<td class="num"><strong>%s</strong></td></tr>' % pct(d['gana'])
    return h + '</tbody></table></div>'


def quad_table(L):
    t = lambda a, b: a if L is ES else b
    rows = [('Optimista', 'Optimistic', ['OP', None, 'OC']), ('Neutral', 'Neutral', ['NP', 'NN', 'NC']), ('Opresivo', 'Oppressive', ['PP', None, 'PC'])]
    h = ('<div class="tw"><table class="t"><thead><tr><th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr></thead><tbody>' %
         (t('El universo…', 'The universe…'), t('Previsible (ordena)', 'Predictable (orders)'), t('Neutral (la costumbre)', 'Neutral (the habit)'), t('Caótico (cobra)', 'Chaotic (charges)')))
    for es, en, ids in rows:
        h += '<tr><td><strong>%s</strong></td>' % (es if L is ES else en)
        for cid in ids:
            if cid is None:
                h += '<td><em>%s</em></td>' % t('Hueco: aquí no hay tarjeta', 'Gap: no card here')
            else:
                d = r(cid, 0)
                h += '<td><strong>%s</strong><br><span class="note">%s · %s %s · %s %s</span></td>' % (
                    L['name'][cid], pct(d['gana']) + t(' sale adelante', ' works out'),
                    t('pifia', 'fumble'), pct(d['pifia']), t('crítico', 'critical'), pct(d['critico']))
        h += '</tr>'
    return h + '</tbody></table></div>'


def ch1b(L):
    t = lambda a, b: a if L is ES else b
    h = ['<section class="chapter" id="ch1-panel">']
    h.append('<h2>%s</h2>' % t('1.4 El Panel de Control (las Tarjetas de Tono)', '1.4 The Control Panel (the Tone Cards)'))
    h.append('<p>' + t(
        'Olvídate de memorizar tablas. Como Director de Juego de NOGUM tu trabajo es llevar el ritmo, no las matemáticas. Todas las reglas de cada modo están condensadas en <strong>tarjetas de tono</strong>. Imprime la hoja o tenla en la pantalla. Cuando la escena cambie, mira la tarjeta que toca: <strong>esa es la única regla que existe en ese momento</strong>.',
        'Forget memorising tables. As a NOGUM game master your job is to carry the pace, not the maths. Every rule of each mode is condensed into <strong>tone cards</strong>. Print the sheet or keep it on screen. When the scene changes, look at the card that applies: <strong>that is the only rule that exists right now</strong>.') + '</p>')
    h.append('<div class="rule">\n<p class="rule-title">%s</p>\n<ol>' % t('Cómo se lee cualquier tarjeta', 'How to read any card'))
    h.append('<li>' + t('Tira siempre los <strong>dos d10</strong>, uno rojo y uno azul. La tarjeta te dice qué número usas: solo el rojo, la suma, el más alto o el más bajo.',
                        'Always roll <strong>both d10s</strong>, one red and one blue. The card tells you which number you use: the red one only, the sum, the higher or the lower.') + '</li>')
    h.append('<li>' + t('<strong>Mira ese número antes de sumar nada: si cae en la banda de pifia, es pifia; si cae en la de crítico, es crítico.</strong> Las bandas tienen prioridad sobre todo lo demás y no dependen del bono. <span class="flag ed">ED-1</span> <span class="flag ed">ED-18</span>',
                        '<strong>Look at that number before adding anything: if it falls in the fumble band, it is a fumble; if it falls in the critical band, it is a critical.</strong> The bands take priority over everything else and do not depend on the bonus. <span class="flag ed">ED-1</span> <span class="flag ed">ED-18</span>') + '</li>')
    h.append('<li>' + t('Si no hay pifia ni crítico, súmale tu <strong>bono total</strong> (habilidad + dificultad + equipo + efectos, siempre entre −2 y +4; ver <a href="#ch4">capítulo 4</a>) y compáralo con la <strong>TN</strong> de la tarjeta.',
                        'If there is no fumble and no critical, add your <strong>total bonus</strong> (skill + difficulty + gear + effects, always between −2 and +4; see <a href="#ch4">chapter 4</a>) and compare it with the card’s <strong>TN</strong>.') + '</li>')
    h.append('<li>' + t('En las tarjetas que lo llevan, <strong>acertar justo cuesta</strong>: si el total iguala la TN o la supera por uno, lo consigues y el DJ elige el precio. Nunca convierte un fallo en éxito: solo cobra peaje a lo que ya había salido bien. <span class="flag ed">ED-23</span>',
                        'On the cards that carry it, <strong>just making it costs you</strong>: if the total equals the TN or beats it by one, you get there and the GM picks the price. It never turns a failure into a success: it only charges a toll on what had already worked. <span class="flag ed">ED-23</span>') + '</li>')
    h.append('</ol>\n</div>')
    h.append('<div class="cards">\n')
    for cid in IDS:
        h.append(card_html(cid, L))
    h.append('</div>')
    h.append('<div class="rule"><p class="rule-title">%s</p><p>%s</p></div>' % (
        t('Aviso: el caos frustra', 'A warning: chaos frustrates'),
        t('Las tres tarjetas de la columna caótica solo funcionan si la mesa ha acordado que <strong>lo que se persigue es la historia, no el éxito</strong>, porque muchas veces no vais a conseguirlo. Con la Bola de nieve el DJ tiene que inventar algo en cuatro de cada diez tiradas, y con la Pesadilla una de cada cinco acciones se estrella pase lo que pase en la ficha. La Pesadilla está pensada para una noche sucia o para una escena corta dentro de una campaña; una campaña larga con ella agota. Dilo antes de empezar y nadie se sentirá castigado.',
          'The three cards in the chaotic column only work if the table has agreed that <strong>what you are chasing is the story, not success</strong>, because much of the time you will not get there. On Snowball the GM has to invent something on four rolls in ten, and on Nightmare one action in five crashes whatever the sheet says. Nightmare is built for one dirty night or a short scene inside a campaign; a long campaign on it wears people out. Say so before you start and nobody will feel punished.')))
    h.append('<div class="rule"><p class="rule-title">%s</p><p>%s</p></div>' % (
        t('De dónde viene la fila opresiva', 'Where the oppressive row comes from'),
        t('No es una esquina teórica del mapa: es la emulación de una familia que existe y se juega. Fíjate en lo que hace la Angustia —9&nbsp;% con −2, 25&nbsp;% con 0, 49&nbsp;% con +2 y 81&nbsp;% con +4— y compáralo con La Llamada de Cthulhu, donde una habilidad sin entrenar anda por el 5–20&nbsp;%, un investigador corriente por el 25–35&nbsp;% y un especialista en lo suyo por el 70–80&nbsp;%. Es la misma distribución. Lo que allí se guarda en la ficha, aquí se guarda en la tarjeta, y por eso puedes entrar y salir de ese tono sin reescribir un personaje. La diferencia está en el reparto: allí el especialista tiene su rincón donde sí acierta, y aquí la tirada es igual de dura para todos. Por eso funciona mejor en formato corto —una noche, un acto, una escena—, igual que Ten Candles, Dread o Trophy, que llegan al mismo sitio por otro camino. Avísalo antes de empezar.',
          'It is not a theoretical corner of the map: it is the emulation of a family of games that exists and gets played. Look at what Anguish does —9&nbsp;% at −2, 25&nbsp;% at 0, 49&nbsp;% at +2 and 81&nbsp;% at +4— and compare it with Call of Cthulhu, where an untrained skill sits around 5–20&nbsp;%, an ordinary investigator around 25–35&nbsp;% and a specialist in their field around 70–80&nbsp;%. It is the same distribution. What is stored in the character sheet there is stored in the card here, which is why you can step in and out of that tone without rewriting a character. The difference is the spread: there the specialist has their corner where they do land things, and here the roll is equally hard for everyone. That is why it works better in short form —one night, one act, one scene— just like Ten Candles, Dread or Trophy, which get to the same place by another road. Say so before you start.')))
    h.append('<div class="rule"><p class="rule-title">%s</p><p>%s</p></div>' % (
        t('Una receta aparte: la Tragedia', 'A recipe apart: Tragedy'),
        t('El cuadrante nunca toca la dificultad, pero una receta sí puede, si lo dice claro y vale para toda la campaña. La <strong>Tragedia</strong> es la única del manual: la suma de la Realista con la vara puesta en 14. El mismo mundo de reloj, con la esperanza fuera del alcance. Su tabla está en el <a href="#apxd-recetas">Apéndice D</a>.',
          'The quadrant never touches the difficulty, but a recipe may, if it says so clearly and holds for the whole campaign. <strong>Tragedy</strong> is the only one in the rulebook: the Realist’s sum with the bar set at 14. The same clockwork world, with hope out of reach. Its table is in <a href="#apxd-recetas">Appendix D</a>.')))
    h.append('<h3 id="ch1-panel-cuadrante">%s</h3>' % t('El cuadrante: dónde cae tu partida', 'The quadrant: where your game falls'))
    h.append('<p>' + t(
        'Las dos preguntas del cuestionario colocan tu partida en un cuadrante. La fila dice <strong>de qué lado está el universo</strong>; la columna, <strong>a qué precio</strong>. No pienses en casillas cerradas: piensa en un mapa donde tu partida cae en algún sitio. Si cae cerca de un borde, es mestiza, y puedes quedarte con la lectura de una casilla y tomar prestada solo una parte de la vecina.',
        'The two questions in the questionnaire place your game on a quadrant. The row says <strong>which side the universe is on</strong>; the column says <strong>at what price</strong>. Do not think in closed boxes: think of a map where your game lands somewhere. If it lands near an edge it is a hybrid, and you can keep one cell’s reading and borrow only part of its neighbour.') + '</p>')
    h.append(quad_table(L))
    h.append('<aside class="meta"><p>' + t(
        '<strong>Los dos huecos son de verdad.</strong> No hay tarjeta optimista ni opresiva en la columna de la costumbre, y no es un olvido: con un dado plano, la única forma de inclinar el tono sería mover la dificultad, y mover la dificultad es justo la fricción que este juego promete quitarte. Si encuentras la regla que rellena ese hueco sin tocar la TN, has escrito una tarjeta nueva. Escríbela en el margen: para eso está el margen.',
        '<strong>The two gaps are real.</strong> There is no optimistic or oppressive card in the habit column, and that is not an oversight: with a flat die, the only way to tilt the tone would be to move the difficulty, and moving the difficulty is exactly the friction this game promises to take away. If you find the rule that fills that gap without touching the TN, you have written a new card. Write it in the margin: that is what the margin is for.') + '</p></aside>')
    h.append('<p><strong>%s</strong> %s</p>' % (
        t('Nota de diseño.', 'Design note.'),
        t('Al imprimir esto verás que la redundancia es tu amiga. No tienes que recordar que «en la suma el éxito es 11»: miras la Realista y ahí está. Si cambias a Angustia, tus ojos van a esa tarjeta y ves que el éxito es 6. <strong>Cero memoria. Cien por cien narrativa.</strong>',
          'Once you print this you will see that redundancy is your friend. You do not have to remember that “on the sum, success is 11”: you look at the Realist and there it is. Switch to Anguish and your eyes go to that card and see that success is 6. <strong>Zero memory. A hundred per cent narrative.</strong>')))
    h.append('</section>')
    return '\n'.join(h) + '\n'


if __name__ == '__main__':
    io.open('frag_ch1b.html', 'w', encoding='utf-8').write(ch1b(ES))
    io.open('frag_ch1b.en.html', 'w', encoding='utf-8').write(ch1b(EN))
    print('frag_ch1b escrito (ES/EN)')
