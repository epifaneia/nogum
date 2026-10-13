# -*- coding: utf-8 -*-
"""Seccion E: la tabla que ya intentaba ser una grafica, dibujada de verdad.

Las dos tablas (11 y 20 filas) estaban duplicadas del Apendice D, donde siguen
enteras. Aqui va la forma, que es lo que esta seccion argumenta."""
import io, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))

MENOS = u'−'
W = 540
PL, PR, PT = 34, 12, 14
ALTO = 118          # alto util de cada panel
GAP = 40            # entre paneles
TOPE = 0.20         # misma escala en los dos paneles: es el argumento

# repartos exactos
UNO = [(v, 0.10) for v in range(1, 11)]
MEJ = [(v, (2 * v - 1) / 100.0) for v in range(1, 11)]
PEO = [(v, (21 - 2 * v) / 100.0) for v in range(1, 11)]
SUM = [(s, (10 - abs(s - 11)) / 100.0) for s in range(2, 21)]

SERIES = [('uno', 'Solo el rojo', 'Red die only', 'g3'),
          ('mej', 'El mejor de los dos', 'Higher of the two', 'ok'),
          ('peo', 'El peor de los dos', 'Lower of the two', 'rd')]


def panel(datos, y0, ancho_grupo, series, en=False):
    """Barras agrupadas. datos: lista de (valor, [(clase, p), ...])"""
    s = []
    base = y0 + ALTO
    # lineas de referencia
    for p in (0.05, 0.10, 0.15, 0.20):
        yy = base - (p / TOPE) * ALTO
        s.append('<line class="gr" x1="%d" y1="%.1f" x2="%d" y2="%.1f"/>' % (PL, yy, W - PR, yy))
        s.append('<text class="gt" x="%d" y="%.1f" text-anchor="end">%d%%</text>' % (PL - 5, yy + 3.2, p * 100))
    s.append('<line class="ge" x1="%d" y1="%.1f" x2="%d" y2="%.1f"/>' % (PL, base, W - PR, base))
    for i, (val, barras) in enumerate(datos):
        gx = PL + i * ancho_grupo
        n = len(barras)
        bw = (ancho_grupo - 3) / float(n)
        for j, (cls, p) in enumerate(barras):
            h = (p / TOPE) * ALTO
            s.append('<rect class="b-%s" x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="1"><title>%d: %d%%</title></rect>'
                     % (cls, gx + 1.5 + j * bw, base - h, max(1.0, bw - 1.2), h, val, round(p * 100)))
        s.append('<text class="gt" x="%.1f" y="%.1f" text-anchor="middle">%d</text>'
                 % (gx + ancho_grupo / 2.0, base + 12, val))
    return s


def svg(en=False):
    H = PT + ALTO + 18 + GAP + ALTO + 18 + 14
    s = ['<svg class="nog" viewBox="0 0 %d %d" width="100%%" role="img" aria-label="%s" xmlns="http://www.w3.org/2000/svg">'
         % (W, H, 'Como se reparte cada lectura de los dos dados' if not en
            else 'How each reading of the two dice is distributed')]
    y0 = PT
    s.append('<text class="gh" x="%d" y="%d">%s</text>'
             % (PL, y0 - 3, ('Lecturas sobre 1–10' if not en else 'Readings over 1–10')))
    datos = [(v, [('g3', UNO[i][1]), ('ok', MEJ[i][1]), ('rd', PEO[i][1])]) for i, (v, _) in enumerate(UNO)]
    s += panel(datos, y0, (W - PL - PR) / 10.0, SERIES, en)
    y1 = y0 + ALTO + 18 + GAP
    s.append('<text class="gh" x="%d" y="%d">%s</text>'
             % (PL, y1 - 3, ('La suma, sobre 2–20 —la misma escala' if not en
                             else 'The sum, over 2–20 —the same scale')))
    s += panel([(v, [('bl', p)]) for v, p in SUM], y1, (W - PL - PR) / 19.0, None, en)
    return '\n'.join(s) + '\n</svg>'


def leyenda(en=False):
    it = [('b-g3', 'Solo el rojo (1d10)', 'Red die only (1d10)'),
          ('b-ok', 'El mejor de los dos', 'Higher of the two'),
          ('b-rd', 'El peor de los dos', 'Lower of the two'),
          ('b-bl', 'La suma (2d10)', 'The sum (2d10)')]
    return ('<p class="leyenda">' + ''.join('<span><i class="%s"></i>%s</span>' % (k, (ing if en else es))
                                            for k, es, ing in it) + '</p>')


PIE_ES = ('<b>La misma mano, cuatro lecturas.</b> El dado rojo solo es una recta: todas las caras valen lo mismo, '
          'y por eso es el caos neutro. El mejor de los dos sube hacia la derecha y el peor hacia la izquierda; '
          'son imágenes especulares, y ahí está el eje del optimismo dibujado. La suma es otra cosa: '
          'una campana que concentra casi todo en el centro y deja los extremos al 1&nbsp;%. '
          'Mira la diferencia de altura entre los dos paneles —es la misma escala—: ninguna barra de la suma '
          'pasa del 10&nbsp;%, mientras que el mejor de dos llega al 19&nbsp;%. Eso es lo que significa <em>orden</em> '
          'aquí: no que salgan números altos, sino que casi nunca salga una sorpresa.')
PIE_EN = ('<b>One hand of dice, four readings.</b> The red die alone is a straight line: every face is worth the same, '
          'which is why it is neutral chaos. The higher of the two climbs to the right and the lower to the left; '
          'they are mirror images, and that is the optimism axis, drawn. The sum is a different animal: '
          'a bell that packs almost everything into the middle and leaves the ends at 1&nbsp;%. '
          'Look at the difference in height between the two panels —it is the same scale—: no bar of the sum '
          'gets past 10&nbsp;%, while the higher of two reaches 19&nbsp;%. That is what <em>order</em> means here: '
          'not that high numbers come up, but that a surprise almost never does.')

VIEJO = {
    'frag_math.html': '<p>La tabla muestra cómo se reparte cada lectura. La barra es relativa al valor más frecuente de su columna.</p>',
    'frag_math.en.html': '<p>The table shows how each reading is distributed. The bar is relative to the most frequent value in its column.</p>',
}
NUEVO = {
    'frag_math.html': '<p>Así se reparte cada lectura. Las cifras exactas, valor a valor, están en el <a href="#apx-mates">Apéndice D</a>.</p>',
    'frag_math.en.html': '<p>This is how each reading is distributed. The exact figures, value by value, are in <a href="#apx-mates">Appendix D</a>.</p>',
}

import re
TW = re.compile(r'<div class="tw"><table class="t">.*?</table></div>\n?', re.S)
fal = []
for f, en in (('frag_math.html', False), ('frag_math.en.html', True)):
    s = io.open(f, encoding='utf-8').read()
    ini = s.find('<h3 id="maq-dados">')
    fin = s.find('<h3 id="maq-anclaje">')
    if ini < 0 or fin < 0:
        fal.append('%s: no localizo la seccion E' % f); continue
    sec = s[ini:fin]
    if len(TW.findall(sec)) != 2:
        fal.append('%s: esperaba 2 tablas en E, hay %d' % (f, len(TW.findall(sec)))); continue
    if VIEJO[f] not in sec:
        fal.append('%s: no encuentro la frase de la tabla' % f); continue
    fig = ('<figure class="fig auto"><div class="fig-box">%s</div><figcaption>%s</figcaption></figure>\n%s\n'
           % (svg(en), (PIE_EN if en else PIE_ES), leyenda(en)))
    sec = sec.replace(VIEJO[f], NUEVO[f], 1)
    primera = [True]

    def pon(m):
        if primera[0]:
            primera[0] = False
            return fig
        return ''
    sec = TW.sub(pon, sec)
    io.open(f, 'w', encoding='utf-8').write(s[:ini] + sec + s[fin:])
    print('  %-20s E: 2 tablas (11 y 20 filas) -> una grafica de dos paneles' % f)

if fal:
    print('FALLOS:')
    for m in fal:
        print('  ' + m)
    sys.exit(1)
print('listo')
