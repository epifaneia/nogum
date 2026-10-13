# -*- coding: utf-8 -*-
"""¿A quien premia cada modelo de nulidad? Con el factor que falta: en la mesa,
cada uno resuelve lo suyo. Busco el punto en que especializarse vuelve a ganar."""
import itertools

TIR = list(itertools.product(range(1, 11), repeat=2))
CARTA = {'Epica': ('mejor', 6), 'Bola de nieve': ('rojo', 6), 'Angustia': ('peor', 6)}


def pct(carta, bono):
    modo, tn = CARTA[carta]
    ok = 0
    for a, c in TIR:
        v = max(a, c) if modo == 'mejor' else min(a, c) if modo == 'peor' else (a + c if modo == 'suma' else a)
        if v + bono >= tn:
            ok += 1
    return ok * 100.0 / len(TIR)


def ficha(dom, dis, fir4, pres=12):
    """coste = 1 por dominio + 1 por disciplina + 2 por Firma(+4)"""
    return dom + dis + 2 * fir4 <= pres


def media(carta, dom, dis, fir4, modelo, dirigido):
    """dirigido = parte de las tiradas que caen dentro de lo que el personaje cubre."""
    dentro = dom * 4
    n4 = min(fir4, dentro)
    n2 = min(dis, dentro - n4)
    n0 = dentro - n4 - n2
    # media dentro de lo cubierto
    m_dentro = (n4 * pct(carta, 4) + n2 * pct(carta, 2) + n0 * pct(carta, 0)) / max(dentro, 1)
    # media fuera
    if modelo == 'ambito':
        m_fuera = pct(carta, 0)
    elif modelo == 'columna':
        m_fuera = pct(carta, -2)
    else:  # intermedio
        amb = min(5, dom)
        cerr_dentro = max(0, amb * 2 - dom)
        cerr_fuera = 10 - dom - cerr_dentro
        tot = cerr_dentro + cerr_fuera
        m_fuera = ((cerr_dentro * pct(carta, -1) + cerr_fuera * pct(carta, -2)) / tot) if tot else pct(carta, 0)
    return dirigido * m_dentro + (1 - dirigido) * m_fuera


ESP = (4, 5, 1)      # especialista: 4 columnas, 5 disciplinas, 1 Firma  -> 11 pts
GEN = (10, 2, 0)     # generalista: las 10 columnas, 2 disciplinas       -> 12 pts

print('=' * 78)
print(' 1. Quien gana segun cuanto le dejen jugar a lo suyo')
print('=' * 78)
print('  "dirigido" = parte de las tiradas que caen donde el personaje tiene algo.')
print('  Un generalista siempre esta dentro (cubre las diez columnas).')
print()
for carta in CARTA:
    print('  --- %s' % carta)
    print('     %-10s %-22s %-22s %s' % ('dirigido', 'especialista (columna)', 'generalista (columna)', 'quien gana'))
    for d in (0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0):
        e = media(carta, ESP[0], ESP[1], ESP[2], 'columna', d)
        g = media(carta, GEN[0], GEN[1], GEN[2], 'columna', 1.0)
        print('     %-10s %-22s %-22s %s' % ('%.0f%%' % (d * 100), '%.0f%%' % e, '%.0f%%' % g,
                                             'especialista' if e > g else 'generalista'))
    print()

print('=' * 78)
print(' 2. El punto de equilibrio exacto')
print('=' * 78)
for carta in CARTA:
    g = media(carta, GEN[0], GEN[1], GEN[2], 'columna', 1.0)
    be = None
    for i in range(0, 1001):
        d = i / 1000.0
        if media(carta, ESP[0], ESP[1], ESP[2], 'columna', d) >= g:
            be = d
            break
    print('  %-16s el especialista empata con el generalista si resuelve lo suyo el %.0f%% de las veces'
          % (carta, be * 100 if be is not None else 100))
print()
print('  Con la nulidad de hoy (por ambito), ese numero es:')
for carta in CARTA:
    g = media(carta, GEN[0], GEN[1], GEN[2], 'ambito', 1.0)
    be = None
    for i in range(0, 1001):
        d = i / 1000.0
        if media(carta, ESP[0], ESP[1], ESP[2], 'ambito', d) >= g:
            be = d
            break
    print('  %-16s %.0f%%' % (carta, be * 100 if be is not None else 100))

print()
print('=' * 78)
print(' 3. Si sube el presupuesto, ¿se arregla?')
print('=' * 78)
print('  Con nulidad por columna, cuanto presupuesto hace falta para que un')
print('  especialista pueda abrir las diez columnas y ademas tener fondo:')
print()
print('  %-6s %-34s %s' % ('pres.', 'ficha que cabe', 'Bola de nieve, dirigido 60%'))
for pres in (12, 14, 16, 18, 20):
    dom = 10
    resto = pres - dom
    fir4 = min(2, resto // 2)
    dis = resto - 2 * fir4
    v = media('Bola de nieve', dom, dis, fir4, 'columna', 0.6)
    print('  %-6s %-34s %.0f%%' % (pres, '10 columnas + %d disc + %d Firma' % (dis, fir4), v))

print()
print('=' * 78)
print(' 4. Resumen de los tres modelos, ficha especialista, dirigido 65%')
print('=' * 78)
print('  %-14s %-16s %-16s %s' % ('tarjeta', 'hoy (ambito)', 'columna', 'intermedio -1'))
for carta in CARTA:
    a = media(carta, ESP[0], ESP[1], ESP[2], 'ambito', 0.65)
    b = media(carta, ESP[0], ESP[1], ESP[2], 'columna', 0.65)
    c = media(carta, ESP[0], ESP[1], ESP[2], 'inter', 0.65)
    print('  %-14s %-16s %-16s %s' % (carta, '%.0f%%' % a, '%.0f%%' % b, '%.0f%%' % c))
