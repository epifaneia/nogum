# -*- coding: utf-8 -*-
"""Las curvas de las siete tarjetas, calculadas y dibujadas en SVG.

Un diagrama no lleva tono: es el sistema dibujandose a si mismo. Por eso puede
estar en el manual (ver la Tesis, «por que no hay ilustraciones»)."""
import itertools

TIR = list(itertools.product(range(1, 11), repeat=2))   # (rojo, blanco)

# modo, TN, banda de pifia (sobre la lectura), banda de critico, hay coste
CARTAS = [
    ('EPICA', 'Épica', 'Epic', 'mejor', 6, 'doble1', 'algun10', False, '#9a6b16'),
    ('PULP', 'Pulp desenfrenado', 'Unleashed Pulp', 'mejor', 6, 'leido12', 'algun10', True, '#a8502a'),
    ('REAL', 'Realista', 'Realist', 'suma', 11, 'suma23', 'suma1920', False, '#2a56a0'),
    ('PRIM', 'Primera marcha', 'First Gear', 'rojo', 6, 'rojo1', 'rojo10', False, '#2e7d6b'),
    ('BOLA', 'Comedia negra', 'Black comedy', 'rojo', 6, 'rojo12', 'rojo910', True, '#7a3f6d'),
    ('ANG', 'Angustia', 'Anguish', 'peor', 6, 'doble1', 'doble10', False, '#1f6f8b'),
    ('PES', 'Pesadilla', 'Nightmare', 'peor', 6, 'algun1', 'doble10', False, '#8d3c3c'),
    # la octava: no esta en el Cuadrante porque no cambia la lectura, cambia la vara
    ('TRAG', 'Tragedia', 'Tragedy', 'suma', 14, 'suma23', 'suma1920', False, '#5b3f99'),
]


def lectura(modo, r, b):
    if modo == 'mejor':
        return max(r, b)
    if modo == 'peor':
        return min(r, b)
    if modo == 'suma':
        return r + b
    return r


def pifia(k, r, b):
    v = {'doble1': r == 1 and b == 1, 'leido12': max(r, b) <= 2, 'suma23': r + b <= 3,
         'rojo1': r == 1, 'rojo12': r <= 2, 'algun1': min(r, b) == 1}
    return v[k]


def critico(k, r, b):
    v = {'algun10': max(r, b) == 10, 'suma1920': r + b >= 19, 'rojo10': r == 10,
         'rojo910': r >= 9, 'doble10': r == 10 and b == 10}
    return v[k]


def reparto(c, bono):
    """Devuelve (pifia, fallo, coste, exito, critico) en tanto por uno."""
    _, _, _, modo, tn, kp, kc, hay_coste, _ = c
    n = len(TIR)
    p = f = co = e = cr = 0
    for r, b in TIR:
        v = lectura(modo, r, b) + bono
        es_p = pifia(kp, r, b)
        es_c = critico(kc, r, b)
        if es_c:
            cr += 1
        elif es_p:
            p += 1
        elif v >= tn:
            if hay_coste and v in (tn, tn + 1):
                co += 1
            else:
                e += 1
        else:
            f += 1
    return (p / n, f / n, co / n, e / n, cr / n)


def sale(c, bono):
    """Sale adelante = coste + exito + critico."""
    p, f, co, e, cr = reparto(c, bono)
    return co + e + cr


BONOS = list(range(-2, 5))

if __name__ == '__main__':
    print('%-20s %s' % ('tarjeta', '  '.join('%+d' % b for b in BONOS)))
    for c in CARTAS:
        print('%-20s %s' % (c[1], '  '.join('%3.0f%%' % (sale(c, b) * 100) for b in BONOS)))
    print()
    print('reparto a bono 0 (pifia / fallo / coste / exito / critico):')
    for c in CARTAS:
        print('  %-20s %s' % (c[1], ' '.join('%3.0f%%' % (x * 100) for x in reparto(c, 0))))
