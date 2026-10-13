# -*- coding: utf-8 -*-
"""Las graficas del taller, traidas a la Sala de Maquinas.

Un diagrama no lleva tono: es el sistema dibujandose a si mismo, asi que puede
estar en el manual (ver la Tesis, «por que no hay ilustraciones»). Las tablas
completas de las siete tarjetas siguen enteras en el Apendice D.

Sustituye:
  * seccion H: las siete tablas de 7 filas -> una grafica de curvas + siete
    graficas de barras apiladas (la misma tabla, dibujada)
  * elimina «Cifras corregidas», que es trabajo editorial, no manual
Conserva: los <h4>, la linea de «Regla:» y la prosa de «Por que encaja».
"""
import io, os, re, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '.')
from curvas import CARTAS, reparto, sale, BONOS

MENOS = u'−'

# fila del Cuadrante -> color ; columna -> trazo
FILA = {'EPICA': 'ok', 'PULP': 'ok', 'REAL': 'bl', 'PRIM': 'bl',
        'BOLA': 'bl', 'ANG': 'rd', 'PES': 'rd'}
COL = {'EPICA': '', 'PULP': 'dot', 'REAL': '', 'PRIM': 'dash',
       'BOLA': 'dot', 'ANG': '', 'PES': 'dot'}

ESTILO = ''   # los estilos viven en paper.css: dentro de <style> contaminarian
              # el indice del buscador, que lee textContent

W, H = 540, 250
PL, PR, PT, PB = 40, 150, 10, 34


def x(i):
    return PL + i * (W - PL - PR) / (len(BONOS) - 1.0)


def y(v):
    return PT + (1 - v) * (H - PT - PB)


def curvas_svg(en=False):
    s = ['<svg class="nog" viewBox="0 0 %d %d" width="100%%" role="img" aria-label="%s" '
         'xmlns="http://www.w3.org/2000/svg">'
         % (W, H, 'Lo que sale adelante en las siete tarjetas, bono a bono' if not en
            else 'What works out on the seven cards, bonus by bonus')]
    s.append(ESTILO)
    for p in (0, .25, .5, .75, 1):
        s.append('<line class="gr" x1="%d" y1="%.1f" x2="%.1f" y2="%.1f"/>' % (PL, y(p), W - PR + 4, y(p)))
        s.append('<text class="gt" x="%d" y="%.1f" text-anchor="end">%d%%</text>' % (PL - 6, y(p) + 3.5, p * 100))
    for i, b in enumerate(BONOS):
        s.append('<text class="gt" x="%.1f" y="%d" text-anchor="middle">%s</text>'
                 % (x(i), H - PB + 18, ('%+d' % b).replace('-', MENOS)))
    s.append('<text class="gt" x="%.1f" y="%d" text-anchor="middle">%s</text>'
             % ((PL + W - PR) / 2.0, H - 3, 'bono de la ficha' if not en else 'sheet bonus'))
    # curvas, de abajo arriba para que las etiquetas salgan ordenadas
    for c in CARTAS:
        k = c[0]
        cls = '%s %s' % (FILA[k], COL[k])
        pts = ' '.join('%.1f,%.1f' % (x(i), y(sale(c, b))) for i, b in enumerate(BONOS))
        s.append('<polyline class="gl %s" points="%s"/>' % (cls, pts))
        s.append('<circle class="f-%s" cx="%.1f" cy="%.1f" r="2.4"/>'
                 % (FILA[k], x(len(BONOS) - 1), y(sale(c, 4))))
    # etiquetas con separacion minima
    et = sorted(((y(sale(c, 4)), c) for c in CARTAS), key=lambda t: t[0])
    ys = []
    for yy, c in et:
        if ys and yy - ys[-1] < 12:
            yy = ys[-1] + 12
        ys.append(yy)
    for (yy0, c), yy in zip(et, ys):
        s.append('<line class="gr" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
                 % (x(len(BONOS) - 1) + 3, yy0, W - PR + 6, yy))
        s.append('<text class="gn f-%s" x="%.1f" y="%.1f">%s <tspan class="gt">%d%%</tspan></text>'
                 % (FILA[c[0]], W - PR + 9, yy + 3.5, c[2] if en else c[1], round(sale(c, 4) * 100)))
    return '\n'.join(s) + '\n</svg>'


# pifia, fallo, coste, exito, critico
BAN = [('pifia', 'fumble', 'pifia'), ('fallo', 'failure', 'fallo'),
       ('coste', 'cost', 'parcial'), (u'éxito', 'success', 'exito'),
       (u'crítico', 'critical', 'critico')]

BW, BRH, BPL, BPR = 540, 23, 34, 54


def barras_svg(c, en=False):
    """La tabla de la tarjeta, dibujada: una barra de 100 % por cada bono."""
    h = len(BONOS) * BRH + 20
    s = ['<svg class="nog" viewBox="0 0 %d %d" width="100%%" role="img" aria-label="%s" '
         'xmlns="http://www.w3.org/2000/svg">'
         % (BW, h, ('Reparto de resultados de %s según el bono' % c[1]) if not en
            else ('Outcome split for %s by bonus' % c[2]))]
    ancho = BW - BPL - BPR
    for i, b in enumerate(BONOS):
        rep = reparto(c, b)
        yy = i * BRH + 2
        s.append('<text class="bt" x="%d" y="%.1f" text-anchor="end">%s</text>'
                 % (BPL - 7, yy + 13, ('%+d' % b).replace('-', MENOS)))
        partes = [(v, k) for v, (es, ing, k) in zip(rep, BAN) if v > 0]
        hueco, xx = 1.5, 0.0
        util = ancho - hueco * max(0, len(partes) - 1)
        for v, k in partes:
            an = v * util
            s.append('<rect class="k-%s" x="%.1f" y="%.1f" width="%.1f" height="16" rx="2"><title>%s: %d%%</title></rect>'
                     % (k, BPL + xx, yy, max(0.6, an), k, round(v * 100)))
            xx += an + hueco
        s.append('<text class="bs" x="%d" y="%.1f">%d%%</text>' % (BW - BPR + 7, yy + 13, round(sale(c, b) * 100)))
    s.append('<text class="bt" x="0" y="%d">%s</text>' % (h - 4, 'bono' if not en else 'bonus'))
    s.append('<text class="bt" x="%d" y="%d">%s</text>'
             % (BW - BPR + 7, h - 4, 'sale' if not en else 'works'))
    return '\n'.join(s) + '\n</svg>'


def leyenda(en=False):
    return ('<p class="leyenda">' + ''.join(
        '<span><i class="k-%s"></i>%s</span>' % (k, (ing if en else es)) for es, ing, k in BAN) + '</p>')


# ------------------------------------------------------------------ montaje
TW = re.compile(r'<div class="tw"><table class="t">.*?</table></div>\n?', re.S)
fal = []
for f, en in (('frag_math.html', False), ('frag_math.en.html', True)):
    s = io.open(f, encoding='utf-8').read()
    ini = s.find('<h3 id="maq-siete">')
    fin = s.find('<h3 id="maq-cuadrante">')
    if ini < 0 or fin < 0:
        fal.append('%s: no localizo la seccion H (%d, %d)' % (f, ini, fin)); continue
    sec = s[ini:fin]
    n_tab = len(TW.findall(sec))
    if n_tab != 7:
        fal.append('%s: esperaba 7 tablas en H, encuentro %d' % (f, n_tab)); continue

    # una barra por tarjeta, en el orden en que aparecen en la seccion
    orden = iter(CARTAS)

    def pon(m):
        c = next(orden)
        return '<div class="graf">%s</div>\n' % barras_svg(c, en)
    sec2 = TW.sub(pon, sec)
    try:
        next(orden); fal.append('%s: sobran tarjetas sin dibujar' % f); continue
    except StopIteration:
        pass

    # intro + grafica de curvas justo tras el parrafo de cabecera
    p0 = sec2.find('</h3>') + 5
    if p0 < 5:
        fal.append('%s: no encuentro el encabezado de H' % f); continue
    intro = (('<p>Cada tarjeta trae su gráfica: una barra por cada bono, del nulo (%s2) al gran '
              'maestro (+4), y cada barra suma 100&nbsp;%%. A la derecha, lo que <em>sale adelante</em>: '
              'éxito con coste, éxito limpio y crítico sumados. Las mismas cifras, fila a fila, '
              'están en el <a href="#apx-mates">Apéndice D</a>.</p>\n' % MENOS)
             if not en else
             ('<p>Each card brings its own chart: one bar per bonus, from the void (%s2) to the grand '
              'master (+4), and each bar adds up to 100&nbsp;%%. On the right, what <em>works out</em>: '
              'success at a cost, clean success and critical, added together. The same figures, row by row, '
              'are in <a href="#apx-mates">Appendix D</a>.</p>\n' % MENOS))
    pie = (('<b>Las siete, juntas.</b> El color es la fila del Cuadrante —optimista, neutral, '
            'opresiva— y el trazo es la columna: continuo lo previsible, a rayas lo neutral, '
            'punteado lo caótico. Tres curvas parecen faltar y no faltan: están debajo de otra. '
            'Épica y Pulp, Primera marcha y Comedia negra, Angustia y Pesadilla coinciden bono a bono. '
            'Ahí está dibujado el eje del caos: <strong>no cambia cuánto sale adelante, cambia de '
            'qué está hecho</strong> —y eso lo cuentan las barras de cada tarjeta, no esta gráfica. '
            'El eje del optimismo sí mueve la línea, y mira dónde: con la ficha a %s2 hay 42 puntos entre '
            'Épica y Angustia; con la ficha a +4 quedan 18. Un especialista en Angustia acierta tanto como un '
            'especialista en Comedia negra. Por eso en lo oscuro especializarse no es una opción: es la salida.'
            % MENOS)
           if not en else
           ('<b>All seven, together.</b> Colour is the Quadrant row —optimistic, neutral, '
            'oppressive— and the stroke is the column: solid for predictable, dashed for neutral, '
            'dotted for chaotic. Three curves look missing and are not: they sit underneath another one. '
            'Epic and Pulp, First Gear and Black comedy, Anguish and Nightmare match bonus for bonus. '
            'That is the chaos axis, drawn: <strong>it does not change how much works out, it changes what '
            'it is made of</strong> —and that is what each card’s bars tell, not this chart. '
            'The optimism axis does move the line, and look where: with the sheet at %s2 there are 42 points '
            'between Epic and Anguish; with the sheet at +4 there are 18. A specialist in Anguish hits as '
            'often as a specialist in Black comedy. That is why in dark tones specialising is not an option: '
            'it is the way out.' % MENOS))
    g1 = ('<figure class="fig auto"><div class="fig-box">%s</div><figcaption>%s</figcaption></figure>\n'
          % (curvas_svg(en), pie))
    sec2 = sec2[:p0] + '\n' + intro + g1 + leyenda(en) + '\n' + sec2[p0:]

    # fuera «Cifras corregidas»: es trabajo editorial, no manual
    s2 = s[:ini] + sec2 + s[fin:]
    ci = s2.find('<h3 id="apxd-corregidas">')
    if ci < 0:
        fal.append('%s: no encuentro Cifras corregidas' % f); continue
    cf = s2.find('<h3 ', ci + 10)
    if cf < 0:
        cf = len(s2)
    quitado = cf - ci
    s2 = s2[:ci] + s2[cf:]
    io.open(f, 'w', encoding='utf-8').write(s2)
    print('  %-20s H: 7 tablas -> 7 graficas + curvas | Cifras corregidas fuera (%d car.)'
          % (f, quitado))

if fal:
    print('FALLOS:')
    for m in fal:
        print('  ' + m)
    sys.exit(1)
print('listo')
