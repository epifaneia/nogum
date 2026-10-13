# -*- coding: utf-8 -*-
"""Seccion H: una tarjeta por tarjeta, con la grafica del taller.

Reemplaza a w_graficas.py. Trabaja desde los respaldos *.bak_graf (el estado
con las tablas originales) para ser idempotente.

Cada tarjeta trae:
  - encabezado con su casilla del Cuadrante y color por fila
  - la linea de regla
  - la grafica del taller: sale / no sale gruesas, critico / coste / pifia
    finas, la raya de «cambia de bando» y la cifra de sale adelante en cada bono
  - cuanto le toca inventar al DJ (pifia + coste), que es la carga real de mesa
  - la prosa de «Por que encaja», que ya estaba y no esta en ningun otro sitio
Las cifras exactas, las cinco columnas, siguen en el Apendice D.
"""
import io, os, re, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '.')
from curvas import CARTAS, reparto, sale, BONOS

MENOS = u'−'
SIETE = [c for c in CARTAS if c[0] != 'TRAG']
FILA = {'EPICA': 'opt', 'PULP': 'opt', 'REAL': 'neu', 'PRIM': 'neu',
        'BOLA': 'neu', 'ANG': 'opr', 'PES': 'opr', 'TRAG': 'rec'}
COL = {'EPICA': '', 'PULP': 'dot', 'REAL': '', 'PRIM': 'dash', 'BOLA': 'dot',
       'ANG': '', 'PES': 'dot', 'TRAG': ''}


def sgn(b):
    return ('%+d' % b).replace('-', MENOS)


def pc(x):
    return int(round(x * 100))


def improvisa(c, bono):
    """Lo que obliga al DJ a inventar: la pifia y el exito con coste."""
    p, f, co, e, cr = reparto(c, bono)
    return p + co


# ------------------------------------------------------------ la grafica
GW, GH = 380, 215
GL, GR, GT, GB = 32, 16, 16, 28


def X(b):
    return GL + (b + 2) * (GW - GL - GR) / 6.0


def Y(v):
    return GT + (1 - v) * (GH - GT - GB)


def grafica(c, en=False):
    nom = c[2] if en else c[1]
    s = ['<svg class="nog t7g" viewBox="0 0 %d %d" width="100%%" role="img" aria-label="%s" '
         'xmlns="http://www.w3.org/2000/svg">'
         % (GW, GH, ('%s: cuanto sale adelante segun el bono' % nom) if not en
            else ('%s: how much works out by bonus' % nom))]
    for g in range(11):
        v = g / 10.0
        fuerte = g in (0, 5, 10) or g == 2.5
        s.append('<line class="gr%s" x1="%d" y1="%.1f" x2="%d" y2="%.1f"/>'
                 % ('' if g % 5 == 0 else ' fino', GL, Y(v), GW - GR, Y(v)))
    for v in (0, .5, 1):
        s.append('<text class="gt" x="%d" y="%.1f" text-anchor="end">%d</text>' % (GL - 6, Y(v) + 3.5, v * 100))
    s.append('<line class="ge" x1="%d" y1="%.1f" x2="%d" y2="%.1f"/>' % (GL, Y(0), GW - GR, Y(0)))
    for b in BONOS:
        s.append('<text class="gt" x="%.1f" y="%d" text-anchor="middle">%s</text>' % (X(b), GH - 9, sgn(b)))
    # las tres finas: de que esta hecho lo que no sale (y el critico)
    # reparto() devuelve (pifia, fallo, coste, exito, critico): 0,1,2,3,4
    finas = [('k-critico', 4, 'crítico', 'critical'),
             ('k-parcial', 2, 'coste', 'cost'),
             ('k-pifia', 0, 'pifia', 'fumble')]
    for cls, idx, es, ing in finas:
        pts = ' '.join('%.1f,%.1f' % (X(b), Y(reparto(c, b)[idx])) for b in BONOS)
        s.append('<polyline class="t7fina %s" points="%s"/>' % (cls, pts))
        for b in BONOS:
            v = reparto(c, b)[idx]
            s.append('<circle class="t7pf %s" cx="%.1f" cy="%.1f" r="2.2"><title>%s %s: %d%%</title></circle>'
                     % (cls, X(b), Y(v), (ing if en else es), sgn(b), pc(v)))
    # donde cruza el 50 %: cambia de bando
    prev = None
    for b in BONOS:
        v = sale(c, b)
        if prev is not None and ((prev[1] < .5 <= v) or (prev[1] >= .5 > v)):
            t = (.5 - prev[1]) / (v - prev[1])
            xc = X(prev[0]) + t * (X(b) - X(prev[0]))
            s.append('<line class="t7cruce" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>' % (xc, Y(0), xc, Y(1)))
            s.append('<text class="gt" x="%.1f" y="%.1f">%s</text>'
                     % (xc + 4, Y(1) + 8, 'cambia de bando' if not en else 'switches sides'))
        prev = (b, v)
    # las dos gruesas
    for cls, fn in (('k-fallo', lambda b: 1 - sale(c, b)), ('k-exito', lambda b: sale(c, b))):
        pts = ' '.join('%.1f,%.1f' % (X(b), Y(fn(b))) for b in BONOS)
        s.append('<polyline class="t7gruesa %s" points="%s"/>' % (cls, pts))
        for b in BONOS:
            s.append('<circle class="t7pg %s" cx="%.1f" cy="%.1f" r="3.4"/>' % (cls, X(b), Y(fn(b))))
    for b in BONOS:
        v = sale(c, b)
        s.append('<text class="t7num" x="%.1f" y="%.1f" text-anchor="middle">%d</text>'
                 % (X(b), Y(v) + (-8 if v >= .5 else 15), pc(v)))
    return '\n'.join(s) + '\n</svg>'


def leyenda(en=False):
    g = [('k-exito', 'sale adelante', 'works out'), ('k-fallo', 'no sale', 'does not')]
    f = [('k-critico', 'crítico', 'critical'), ('k-parcial', 'con coste', 'at a cost'), ('k-pifia', 'pifia', 'fumble')]
    h = '<p class="t7leg">'
    h += ''.join('<span><i class="gruesa %s"></i>%s</span>' % (k, (ing if en else es)) for k, es, ing in g)
    h += '<span class="sep">·</span>'
    h += ''.join('<span><i class="fina %s"></i>%s</span>' % (k, (ing if en else es)) for k, es, ing in f)
    h += '<span class="note">%s</span></p>' % (
        'sale adelante = con coste, limpio o crítico' if not en else 'works out = at a cost, clean or critical')
    return h


def tabla(c, en=False):
    cab = (['Bono', 'Pifia', 'Fallo', 'Coste', 'Éxito', 'Crít.', 'Sale adelante'] if not en
           else ['Bonus', 'Fumble', 'Failure', 'Cost', 'Success', 'Crit.', 'Works out'])
    h = ['<div class="tw"><table class="t t7n"><thead><tr>' +
         ''.join('<th%s>%s</th>' % (' class="num"' if i else '', x) for i, x in enumerate(cab)) + '</tr></thead><tbody>']
    for b in BONOS:
        r = reparto(c, b)
        h.append('<tr><td>%s</td>%s<td class="num"><strong>%d&nbsp;%%</strong></td></tr>'
                 % (sgn(b), ''.join('<td class="num">%d&nbsp;%%</td>' % pc(v) for v in r), pc(sale(c, b))))
    return '\n'.join(h) + '</tbody></table></div>'


def tarjeta(c, h4, regla, prosa, en=False):
    """h4: 'Nombre (Fila · Columna) «frase»' tal como ya estaba en el manual."""
    m = re.match(r'^(.*?)\s*\(([^)]*)\)\s*(.*)$', h4.strip())
    nom, eje, frase = (m.group(1), m.group(2), m.group(3)) if m else (h4, '', '')
    inv = improvisa(c, 0)
    h = ['<div class="t7" data-fila="%s">' % FILA[c[0]]]
    h.append('<div class="t7cab"><h4>%s</h4><span class="t7ax">%s</span></div>' % (nom, eje))
    if frase:
        h.append('<p class="t7frase">%s</p>' % frase)
    h.append('<div class="t7cuerpo">')
    h.append('<div class="t7izq">%s<p class="t7pie">%s &rarr; &nbsp;·&nbsp; %s</p></div>'
             % (grafica(c, en),
                ('bono' if not en else 'bonus'),
                (('el DJ inventa algo en el %d&nbsp;%% de las tiradas' % pc(inv)) if not en
                 else ('the GM invents something on %d%% of rolls' % pc(inv)))))
    h.append('<div class="t7der"><p class="t7how">%s</p>%s</div>' % (regla, prosa))
    h.append('</div>')
    # la tabla no: los cinco numeros exactos viven en el Apendice D, que es
    # para lo que existe un apendice. Aqui manda la forma.
    return '\n'.join(h) + '\n</div>'


# ---------------------------------------------------------------- la vista de conjunto
CW, CH = 540, 250
CL, CR, CT, CB = 40, 150, 10, 34


def cx(i):
    return CL + i * (CW - CL - CR) / (len(BONOS) - 1.0)


def cy(v):
    return CT + (1 - v) * (CH - CT - CB)


def conjunto(en=False):
    s = ['<svg class="nog" viewBox="0 0 %d %d" width="100%%" role="img" aria-label="%s" '
         'xmlns="http://www.w3.org/2000/svg">'
         % (CW, CH, 'Lo que sale adelante en las siete tarjetas, bono a bono' if not en
            else 'What works out on the seven cards, bonus by bonus')]
    for p in (0, .25, .5, .75, 1):
        s.append('<line class="gr" x1="%d" y1="%.1f" x2="%.1f" y2="%.1f"/>' % (CL, cy(p), CW - CR + 4, cy(p)))
        s.append('<text class="gt" x="%d" y="%.1f" text-anchor="end">%d%%</text>' % (CL - 6, cy(p) + 3.5, p * 100))
    for i, b in enumerate(BONOS):
        s.append('<text class="gt" x="%.1f" y="%d" text-anchor="middle">%s</text>' % (cx(i), CH - CB + 18, sgn(b)))
    s.append('<text class="gt" x="%.1f" y="%d" text-anchor="middle">%s</text>'
             % ((CL + CW - CR) / 2.0, CH - 3, 'bono de la ficha' if not en else 'sheet bonus'))
    cls_fila = {'opt': 'ok', 'neu': 'bl', 'opr': 'rd'}
    for c in SIETE:
        k = cls_fila[FILA[c[0]]]
        pts = ' '.join('%.1f,%.1f' % (cx(i), cy(sale(c, b))) for i, b in enumerate(BONOS))
        s.append('<polyline class="gl %s %s" points="%s"/>' % (k, COL[c[0]], pts))
        s.append('<circle class="f-%s" cx="%.1f" cy="%.1f" r="2.4"/>' % (k, cx(len(BONOS) - 1), cy(sale(c, 4))))
    et = sorted(((cy(sale(c, 4)), c) for c in SIETE), key=lambda t: t[0])
    ys = []
    for yy, c in et:
        if ys and yy - ys[-1] < 12:
            yy = ys[-1] + 12
        ys.append(yy)
    for (yy0, c), yy in zip(et, ys):
        s.append('<line class="gr" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
                 % (cx(len(BONOS) - 1) + 3, yy0, CW - CR + 6, yy))
        s.append('<text class="gn f-%s" x="%.1f" y="%.1f">%s <tspan class="gt">%d%%</tspan></text>'
                 % (cls_fila[FILA[c[0]]], CW - CR + 9, yy + 3.5, c[2] if en else c[1], pc(sale(c, 4))))
    return '\n'.join(s) + '\n</svg>'
