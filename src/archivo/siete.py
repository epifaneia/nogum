# -*- coding: utf-8 -*-
"""Las siete tarjetas: distribuciones exactas por enumeración (bono -2..+4).

Tres bandas naturales, todas sobre EL NÚMERO QUE USAS, todas ciegas al bono:
  pifia    estrecha (los dos dados de acuerdo) · normal (1) · ancha (1-2)
  coste    aciertas por poco: el total iguala la TN o la supera por uno
  crítico  estrecha (los dos dados de acuerdo) · normal (10) · ancha (9-10)
La suma lleva siempre sus propios extremos: 2-3 y 19-20.
"""
import itertools, json, os
from fractions import Fraction as F

os.chdir(os.path.dirname(os.path.abspath(__file__)))
TWO = list(itertools.product(range(1, 11), repeat=2))
BON = [-2, -1, 0, 1, 2, 3, 4]
KEYS = ['pifia', 'fallo', 'parcial', 'exito', 'critico']

READ = {
    'rojo':  lambda r: r[0],
    'mejor': lambda r: max(r),
    'peor':  lambda r: min(r),
    'suma':  lambda r: r[0] + r[1],
}

# id, fila, columna, nombre, lectura, TN, coste natural, banda pifia, banda crítico
CARDS = [
    ('OP', 'Optimista', 'Previsible', 'Mejor de dos',                          'mejor', 6,  False, 'normal',   'normal'),
    ('OC', 'Optimista', 'Caótico',    'Mejor de dos + coste, pifia ancha',     'mejor', 6,  True,  'ancha',    'normal'),
    ('NP', 'Neutral',   'Previsible', 'Suma de los dos',                       'suma',  11, False, 'normal',   'normal'),
    ('NN', 'Neutral',   'Neutral',    'Solo el dado rojo',                     'rojo',  6,  False, 'normal',   'normal'),
    ('NC', 'Neutral',   'Caótico',    'Dado rojo + coste, bandas anchas',      'rojo',  6,  True,  'ancha',    'ancha'),
    ('PP', 'Opresivo',  'Previsible', 'Peor de dos, bandas estrechas',         'peor',  6,  False, 'estrecha', 'estrecha'),
    ('PC', 'Opresivo',  'Caótico',    'Peor de dos, bandas normales',          'peor',  6,  False, 'normal',   'normal'),
]
VARIANTS = [
    ('TRAG', 'Opresivo', 'Previsible', 'Tragedia: suma con TN 14 (receta)',    'suma',  14, False, 'normal', 'normal'),
    ('OCA',  'Optimista', 'Caótico',   '[alt] Pulp con crítico ancho',         'mejor', 6,  True,  'ancha', 'ancha'),
    ('AGOB', 'Opresivo', 'Caótico',   'Acelerado · Agobio: peor + coste',     'peor',  6,  True,  'normal', 'normal'),
    ('NCA',  'Neutral',  'Caótico',    '[alt] Bola con coste sobre el total',  'rojo',  6,  'total', 'ancha', 'ancha'),
]


def nat(read, bp, bc, coste, r, v):
    """pifia / critico / parcial natural, o None. Todo sobre el número que usas."""
    if read == 'suma':
        if v <= 3:
            return 'pifia'
        if v >= 19:
            return 'critico'
    else:
        if bp == 'estrecha':
            if r[0] == 1 and r[1] == 1:
                return 'pifia'
        elif bp == 'normal':
            if v <= 1:
                return 'pifia'
        elif v <= 2:
            return 'pifia'
        if bc == 'estrecha':
            if r[0] == 10 and r[1] == 10:
                return 'critico'
        elif bc == 'normal':
            if v >= 10:
                return 'critico'
        elif v >= 9:
            return 'critico'
    if coste == 'nat56' and 5 <= v <= 6:
        return 'parcial'
    return None


def dist(card, b):
    _, _, _, _, read, tn, coste, bp, bc = card
    rd = READ[read]
    space = [(x, x) for x in range(1, 11)] if read == 'rojo' else TWO
    out = dict.fromkeys(KEYS, 0)
    for r in space:
        v = rd(r)
        k = nat(read, bp, bc, coste, r, v)
        if k is None:
            t = v + b
            if coste is True and tn <= t <= tn + 1:
                k = 'parcial'
            else:
                k = 'exito' if t >= tn else 'fallo'
        out[k] += 1
    n = len(space)
    d = {k: F(out[k], n) for k in KEYS}
    d['gana'] = d['parcial'] + d['exito'] + d['critico']
    d['limpio'] = d['exito'] + d['critico']
    d['efectivo'] = d['exito'] + d['critico'] + d['parcial'] / 2
    d['improvisa'] = d['pifia'] + d['parcial']
    return d


def table(cards, title):
    print('\n=== %s ===' % title)
    print('%-5s %-38s %5s %6s %6s %7s %6s %7s %7s' % ('id', 'tarjeta', 'bono', 'pifia', 'fallo', 'coste', 'éxito', 'crítico', 'gana'))
    for c in cards:
        for b in BON:
            d = dist(c, b)
            print('%-5s %-38s %5s %5.0f%% %5.0f%% %6.0f%% %5.0f%% %6.0f%% %6.0f%%' % (
                c[0] if b == BON[0] else '', c[3] if b == BON[0] else '', ('+%d' % b) if b > 0 else b,
                100*d['pifia'], 100*d['fallo'], 100*d['parcial'], 100*d['exito'], 100*d['critico'], 100*d['gana']))
        print()


table(CARDS, 'LAS SIETE')
table(VARIANTS, 'VARIANTES Y RECETAS')

print('=== resumen: sale adelante ===')
print('%-34s %s' % ('tarjeta', '  '.join('%+d' % b for b in BON)))
for c in CARDS:
    print('%-34s %s' % (c[3][:34], '  '.join('%2.0f%%' % (100*dist(c, b)['gana']) for b in BON)))
print('\n=== el DJ improvisa (pifia + coste) ===')
for c in CARDS:
    print('%-34s %s' % (c[3][:34], '  '.join('%2.0f%%' % (100*dist(c, b)['improvisa']) for b in BON)))
print('\n=== peso de la ficha (gana a +4 menos gana a -2) ===')
for c in CARDS:
    print('%-34s %3.0f puntos' % (c[3][:34], 100*float(dist(c, 4)['gana'] - dist(c, -2)['gana'])))

for b in BON:
    assert dist(CARDS[5], b)['gana'] == dist(CARDS[6], b)['gana'], 'la pareja opresiva ya no empata'

data = {}
for c in CARDS + VARIANTS:
    data[c[0]] = dict(row=c[1], col=c[2], name=c[3], read=c[4], tn=c[5], coste=c[6], bp=c[7], bc=c[8],
                      rows={str(b): {k: float(v) for k, v in dist(c, b).items()} for b in BON})
json.dump(data, open('siete.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('\nsiete.json escrito')
