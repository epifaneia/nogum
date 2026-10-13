# -*- coding: utf-8 -*-
"""Montaje de la seccion H (tarjetas) y del Apendice D (cifras)."""
import io, os, re, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '.')
from w_tarjetas import (SIETE, CARTAS, tarjeta, tabla, conjunto, leyenda, grafica,
                        improvisa, pc, MENOS, FILA)

CARD = re.compile(r'<h4>(?P<h4>.*?)</h4>\s*<p><em>(?:Regla|Rule):</em>(?P<reg>.*?)</p>\s*'
                  r'<div class="tw">.*?</table></div>\s*(?P<pro><p><strong>.*?</p>)', re.S)

INTRO = {
    False: ('<p>Una ficha por tarjeta. La línea gruesa es lo que <strong>sale adelante</strong> '
            '—éxito con coste, éxito limpio y crítico juntos— y la otra gruesa es lo que no. '
            'Las tres finas cuentan de qué está hecho el resto. Debajo de cada gráfica, lo que de verdad '
            'le cuesta a la mesa: cuántas tiradas obligan al DJ a inventarse algo. '
            'Los cinco números exactos, bono a bono, están en el <a href="#apx-mates">Apéndice D</a>.</p>\n'),
    True: ('<p>One sheet per card. The thick line is what <strong>works out</strong> '
           '—success at a cost, clean success and critical together— and the other thick one is what does not. '
           'The three thin ones tell what the rest is made of. Under each chart, what it actually costs the table: '
           'how many rolls force the GM to invent something. '
           'The five exact figures, bonus by bonus, are in <a href="#apx-mates">Appendix D</a>.</p>\n')}

PIE = {
    False: ('<b>Las siete, juntas.</b> El color es la fila del Cuadrante —optimista, neutral, opresiva— '
            'y el trazo es la columna: continuo lo previsible, a rayas lo neutral, punteado lo caótico. '
            'Tres curvas parecen faltar y no faltan: están debajo de otra. Épica y Pulp, Primera marcha y '
            'Comedia negra, Angustia y Pesadilla coinciden bono a bono. Ahí está dibujado el eje del caos: '
            '<strong>no cambia cuánto sale adelante, cambia de qué está hecho</strong>. Y el eje del '
            'optimismo se estrecha con la ficha: con la ficha a ' + MENOS + '2 hay 42 puntos entre Épica y '
            'Angustia; con la ficha a +4 quedan 18. Un especialista en Angustia acierta tanto como un especialista '
            'en Comedia negra. Por eso en lo oscuro especializarse no es una opción: es la salida.'),
    True: ('<b>All seven, together.</b> Colour is the Quadrant row —optimistic, neutral, oppressive— '
           'and the stroke is the column: solid for predictable, dashed for neutral, dotted for chaotic. '
           'Three curves look missing and are not: they sit underneath another one. Epic and Pulp, First Gear and '
           'Black comedy, Anguish and Nightmare match bonus for bonus. That is the chaos axis, drawn: '
           '<strong>it does not change how much works out, it changes what it is made of</strong>. And the optimism '
           'axis narrows with the sheet: with the sheet at ' + MENOS + '2 there are 42 points between Epic and '
           'Anguish; with the sheet at +4 there are 18. A specialist in Anguish hits as often as a specialist in '
           'Black comedy. That is why in dark tones specialising is not an option: it is the way out.')}

APX_INTRO = {
    False: ('<p>Aquí están los números que las gráficas de <a href="#maq-siete">1.3&nbsp;H</a> '
            'dibujan pero no escriben. Allí se ve la forma de cada tarjeta de un vistazo; aquí están las '
            'cinco cifras de cada bono, que es lo que hace falta cuando quieres <em>comprobar</em> una en vez de '
            'reconocerla. Probabilidades exactas en&nbsp;%, de ' + MENOS + '2 a +4. <em>Sale adelante</em> = coste '
            '+ éxito + crítico, y cada fila suma 100&nbsp;%. La pifia y el crítico son naturales y '
            'tienen prioridad; el resto se resuelve con lectura + bono contra la TN de la tarjeta.</p>\n'),
    True: ('<p>These are the figures the charts in <a href="#maq-siete">1.3&nbsp;H</a> draw but do not write out. '
           'There you see the shape of each card at a glance; here are the five numbers for every bonus, which is '
           'what you need when you want to <em>check</em> one rather than recognise it. Exact probabilities in&nbsp;%, '
           'from ' + MENOS + '2 to +4. <em>Works out</em> = cost + success + critical, and each row adds up to '
           '100&nbsp;%. Fumble and critical are natural and take priority; the rest resolves as read + bonus against '
           'the card’s TN.</p>\n')}

TRAG_PROSA = {
    False: ('La misma lectura que la Realista con la vara tres puntos más alta, y el efecto no es proporcional: '
            'a bono 0 sale adelante el 28&nbsp;% en vez del 55&nbsp;%. La campana castiga el doble cada paso que '
            'alejas la meta de su centro. Por eso una receta puede mover la TN, pero tiene que decirlo para toda la '
            'campaña: moverla a mitad de partida no es subir la dificultad, es cambiar de género.'),
    True: ('The same read as the Realist with the bar three points higher, and the effect is not proportional: at '
           'bonus 0 it works out 28&nbsp;% of the time instead of 55&nbsp;%. The bell punishes twice over for every '
           'step you move the target away from its centre. That is why a recipe may move the TN, but has to say so '
           'for the whole campaign: moving it mid-game is not raising the difficulty, it is changing genre.')}

IDS = ['apxd-op', 'apxd-oc', 'apxd-np', 'apxd-nn', 'apxd-nc', 'apxd-pp', 'apxd-pc']


def monta(f, en):
    s = io.open(f + '.bak_graf', encoding='utf-8').read()

    # ---------------------------------------------------------- seccion H
    ini = s.find('<h3 id="maq-siete">')
    fin = s.find('<h3 id="maq-cuadrante">')
    if ini < 0 or fin < 0:
        return '%s: no localizo la seccion H' % f
    sec = s[ini:fin]
    hallados = CARD.findall(sec)
    if len(hallados) != 7:
        return '%s: esperaba 7 tarjetas en H, encuentro %d' % (f, len(hallados))
    cab = sec[:sec.find('</h3>') + 5] + '\n'
    out = [cab, INTRO[en],
           '<figure class="fig auto"><div class="fig-box">%s</div><figcaption>%s</figcaption></figure>\n'
           % (conjunto(en), PIE[en]),
           leyenda(en), '\n<div class="t7s">\n']
    for c, (h4, reg, pro) in zip(SIETE, hallados):
        out.append(tarjeta(c, h4, reg.strip(), pro.strip(), en) + '\n')
    out.append('</div>\n')
    s = s[:ini] + ''.join(out) + s[fin:]

    # ---------------------------------------------------- Apendice D: intro
    ai = s.find('<h3 id="apxd-op">')
    if ai < 0:
        return '%s: no localizo el Apendice D' % f
    h2 = s.rfind('</h2>', 0, ai)
    if h2 < 0:
        return '%s: no localizo el h2 del Apendice D' % f
    s = s[:h2 + 5] + '\n' + APX_INTRO[en] + s[ai:]

    # ------------------------------------------- Apendice D: siete tablas
    ai = s.find('<h3 id="apxd-op">')
    af = s.find('<h3 id="apxd-recetas">')
    if af < 0:
        return '%s: no localizo las recetas del Apendice D' % f
    viejo = s[ai:af]
    bloques = []
    for c, i_ in zip(SIETE, IDS):
        m = re.search(r'<h3 id="%s">(.*?)</h3>\s*<p>(.*?)</p>' % i_, viejo, re.S)
        if not m:
            return '%s: no encuentro el encabezado %s' % (f, i_)
        bloques.append('<h3 id="%s">%s</h3>\n<p>%s</p>\n%s\n' % (i_, m.group(1), m.group(2), tabla(c, en)))
    s = s[:ai] + ''.join(bloques) + s[af:]

    # --------------------------------- Apendice D: Tragedia, con su grafica
    base = s.find('<h3 id="apxd-recetas">')
    resto = s[base:]
    m = re.search(r'<h4>Trage\w+.*?</h4>\s*<div class="tw"><table class="t">.*?</table></div>\s*', resto, re.S)
    if not m:
        m = re.search(r'<div class="tw"><table class="t">.*?</table></div>\s*', resto, re.S)
    if not m:
        return '%s: no encuentro la tabla de Tragedia' % f
    trag = next(c for c in CARTAS if c[0] == 'TRAG')
    nuevo = ('<div class="t7" data-fila="rec"><div class="t7cab"><h4>%s</h4><span class="t7ax">%s</span></div>'
             '<div class="t7cuerpo"><div class="t7izq">%s<p class="t7pie">%s &rarr; &nbsp;·&nbsp; %s</p></div>'
             '<div class="t7der"><p class="t7how">%s</p><p>%s</p></div></div></div>\n%s\n'
             % ('Tragedia' if not en else 'Tragedy',
                ('Receta · la vara se mueve' if not en else 'Recipe · the bar moves'),
                grafica(trag, en),
                ('bono' if not en else 'bonus'),
                (('el DJ inventa algo en el %d&nbsp;%% de las tiradas' % pc(improvisa(trag, 0))) if not en
                 else ('the GM invents something on %d%% of rolls' % pc(improvisa(trag, 0)))),
                ('suma de 2d10 + bono · TN 14 · bandas 2–3 / 19–20.' if not en
                 else 'sum of 2d10 + bonus · TN 14 · bands 2–3 / 19–20.'),
                TRAG_PROSA[en], tabla(trag, en)))
    s = s[:base + m.start()] + nuevo + s[base + m.end():]

    # ------------------------------------------- fuera «Cifras corregidas»
    ci = s.find('<h3 id="apxd-corregidas">')
    if ci < 0:
        return '%s: no encuentro Cifras corregidas' % f
    cf = s.find('<h3 ', ci + 10)
    if cf < 0:
        cf = len(s)
    s = s[:ci] + s[cf:]

    io.open(f, 'w', encoding='utf-8').write(s)
    return None


fal = [m for m in (monta('frag_math.html', False), monta('frag_math.en.html', True)) if m]
if fal:
    print('FALLOS:')
    for m in fal:
        print('  ' + m)
    sys.exit(1)
print('seccion H: siete fichas con grafica | Apendice D: intro nueva, tablas regeneradas, Tragedia con ficha')
