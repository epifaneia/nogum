# -*- coding: utf-8 -*-
"""Las siete tarjetas: distribuciones exactas por enumeración (bono -2..+4)."""
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

# id: (fila, columna, nombre, lectura, TN, banda(lo,hi) o None, pifia<=, critico>=)
CARDS = [
    ('OP', 'Optimista', 'Previsible', 'Mejor de dos',                 'mejor', 6,  None,     1, 10),
    ('OC', 'Optimista', 'Caótico',    'Mejor de dos + banda + ruido', 'mejor', 6,  (5, 6),   2, 9),
    ('NP', 'Neutral',   'Previsible', 'Suma de los dos',              'suma',  11, None,     3, 19),
    ('NN', 'Neutral',   'Neutral',    'Solo el dado rojo',            'rojo',  6,  None,     1, 10),
    ('NC', 'Neutral',   'Caótico',    'Dado rojo + banda + ruido',    'rojo',  6,  (5, 6),   2, 9),
    ('PP', 'Opresivo',  'Previsible', 'Peor de dos',                  'peor',  6,  None,     1, 10),
    ('PC', 'Opresivo',  'Caótico',    'Peor de dos + banda + ruido',  'peor',  6,  (5, 6),   2, 9),
]
# variantes que quedan pendientes de decidir
VARIANTS = [
    ('NC-', 'Neutral', 'Caótico', 'Dado rojo + banda, sin ruido (descartada)', 'rojo', 6, (5, 6), 1, 10),
    ('NP-', 'Neutral', 'Previsible', 'Suma, naturales puros 2 y 20',  'suma', 11, None,  2, 20),
    ('PC-', 'Opresivo', 'Caótico', 'Peor de dos + banda, sin ruido',  'peor', 6, (5, 6), 1, 10),
    ('TRAG', 'Opresivo', 'Previsible', 'Tragedia: suma con TN 14 (receta)', 'suma', 14, None, 3, 19),
    ('AGOB', 'Opresivo', 'Caótico', 'Acelerado · Agobio: peor de dos + banda', 'peor', 6, (5, 6), 1, 10),
]


def dist(card, b):
    _, _, _, _, read, tn, band, fn, cn = card
    rd = READ[read]
    single = read == 'rojo'
    space = [(x, x) for x in range(1, 11)] if single else TWO
    out = dict.fromkeys(KEYS, 0)
    for r in space:
        v = rd(r)
        if v <= fn:
            k = 'pifia'
        elif v >= cn:
            k = 'critico'
        else:
            t = v + b
            if band:
                k = 'fallo' if t < band[0] else ('parcial' if t <= band[1] else 'exito')
            else:
                k = 'exito' if t >= tn else 'fallo'
        out[k] += 1
    n = len(space)
    d = {k: F(out[k], n) for k in KEYS}
    d['gana'] = d['parcial'] + d['exito'] + d['critico']
    d['limpio'] = d['exito'] + d['critico']
    d['efectivo'] = d['exito'] + d['critico'] + d['parcial'] / 2
    return d


def table(cards, title):
    print('\n=== %s ===' % title)
    print('%-4s %-30s %5s %6s %6s %7s %6s %7s %7s %8s' % ('id', 'tarjeta', 'bono', 'pifia', 'fallo', 'parcial', 'éxito', 'crítico', 'gana', 'efectivo'))
    for c in cards:
        for b in BON:
            d = dist(c, b)
            print('%-4s %-30s %5s %5.0f%% %5.0f%% %6.0f%% %5.0f%% %6.0f%% %6.0f%% %7.0f%%' % (
                c[0] if b == BON[0] else '', c[3] if b == BON[0] else '', ('+%d' % b) if b > 0 else b,
                100*d['pifia'], 100*d['fallo'], 100*d['parcial'], 100*d['exito'], 100*d['critico'], 100*d['gana'], 100*d['efectivo']))
        print()


table(CARDS, 'LAS SIETE')
table(VARIANTS, 'VARIANTES PENDIENTES')

print('=== comprobaciones ===')
for b in BON:
    print(' bono %+d  efectivo: previsible %3.0f/%3.0f/%3.0f  caótico %3.0f/%3.0f/%3.0f' % (
        b,
        *[100*float(dist(c, b)['efectivo']) for c in CARDS if c[2] == 'Previsible'],
        *[100*float(dist(c, b)['efectivo']) for c in CARDS if c[2] == 'Caótico']))

print('\n=== estados que desaparecen (probabilidad 0) ===')
for c in CARDS:
    for b in BON:
        d = dist(c, b)
        zero = [k for k in KEYS if d[k] == 0]
        if zero:
            print('  %-30s bono %+d: sin %s' % (c[3], b, ', '.join(zero)))

print('\n=== naturales por lectura (regla del valor leído) ===')
for read in ('rojo', 'mejor', 'peor'):
    rd = READ[read]
    space = [(x, x) for x in range(1, 11)] if read == 'rojo' else TWO
    p1 = sum(1 for r in space if rd(r) == 1) / len(space)
    p10 = sum(1 for r in space if rd(r) == 10) / len(space)
    p12 = sum(1 for r in space if rd(r) <= 2) / len(space)
    p910 = sum(1 for r in space if rd(r) >= 9) / len(space)
    print('  %-6s  1:%5.0f%%  10:%5.0f%%   |ruido| 1-2:%5.0f%%  9-10:%5.0f%%' % (read, 100*p1, 100*p10, 100*p12, 100*p910))

data = {}
for c in CARDS + VARIANTS:
    data[c[0]] = dict(row=c[1], col=c[2], name=c[3], read=c[4], tn=c[5], band=c[6], fum=c[7], cri=c[8],
                      rows={str(b): {k: float(v) for k, v in dist(c, b).items()} for b in BON})
json.dump(data, open('siete.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('\nsiete.json escrito')
