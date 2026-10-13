# -*- coding: utf-8 -*-
"""Los numeros de las dos propuestas: la Firma a +4 y la nulidad por columna."""
import itertools

TIR = list(itertools.product(range(1, 11), repeat=2))
CARTA = {'Epica': ('mejor', 6), 'Realista': ('suma', 11), 'Bola de nieve': ('rojo', 6),
         'Angustia': ('peor', 6), 'Pesadilla': ('peor', 6)}


def pct(carta, bono):
    modo, tn = CARTA[carta]
    ok = 0
    for a, c in TIR:
        v = max(a, c) if modo == 'mejor' else min(a, c) if modo == 'peor' else (a + c) if modo == 'suma' else a
        if v + bono >= tn:
            ok += 1
    return ok * 100.0 / len(TIR)


print('=' * 78)
print(' 1. QUITAR EL +3: lo que cambia la Firma')
print('=' * 78)
print('  escalera vieja: -2  ·  +0  ·  +1  ·  +2  ·  +3  ·  +4')
print('  escalera nueva: -2  ·  +0  ·  +1  ·  +2  ·  +4   (la Firma salta dos)')
print()
print('  %-14s %7s %7s %7s   %s' % ('tarjeta', '+2', '+3', '+4', 'lo que gana la Firma'))
for c in CARTA:
    a, b, d = pct(c, 2), pct(c, 3), pct(c, 4)
    print('  %-14s %6.0f%% %6.0f%% %6.0f%%   antes +%.0f, ahora +%.0f puntos' % (c, a, b, d, b - a, d - a))
print()
print('  El salto de la Firma se duplica en todas, y en Angustia pasa de +15 a +32.')
print('  Dicho de otra forma: la especializacion es el doble de decisiva, y mucho')
print('  mas en los tonos oscuros, que es justo donde dices que hay que')
print('  especializarse para sobrevivir. Las dos cosas apuntan al mismo sitio.')

print()
print('=' * 78)
print(' 2. LA NULIDAD POR COLUMNA: cuanto cuesta no ser Nulo')
print('=' * 78)
print('  5 ambitos x 2 dominios = 10 columnas, 4 disciplinas cada una.')
print('  Abrir un dominio cuesta 1 punto. Presupuesto: 12 (14 con Arcano).')
print()
print('  %-30s %-22s %s' % ('modelo', 'cubrir todo cuesta', 'queda para profundidad'))
print('  %-30s %-22s %s' % ('hoy (nulo por ambito)', '5 de 12 puntos', '7 puntos'))
print('  %-30s %-22s %s' % ('propuesta (nulo por columna)', '10 de 12 puntos', '2 puntos'))

print()
print('=' * 78)
print(' 3. Tres fichas tipo, y cuanto les sale el -2 en la mesa')
print('=' * 78)
# (nombre, dominios abiertos de 10, disciplinas, firmas, coste)
FICHAS = [
    ('Especialista puro', 3, 5, 2, 3 + 5 + 2 * 2),
    ('Especialista normal', 4, 5, 1, 4 + 5 + 2),
    ('Equilibrado', 6, 5, 0, 6 + 5),
    ('Generalista', 10, 2, 0, 10 + 2),
]
print('  %-22s %-9s %-11s %-7s %s' % ('ficha', 'columnas', 'coste', 'nulo%', 'reparto de bonos'))
for n, dom, dis, fir, coste in FICHAS:
    nulo = (10 - dom) / 10.0
    # dentro de lo cubierto: las disciplinas dan +2, las firmas +4, el resto +0
    base = dom * 4
    con2 = min(dis, base)
    con4 = min(fir, con2)
    con2 -= con4
    con0 = base - con2 - con4
    rep = []
    for et, k in (('-2', (10 - dom) * 4), ('+0', con0), ('+2', con2), ('+4', con4)):
        if k:
            rep.append('%s:%d' % (et, k))
    print('  %-22s %-9s %-11s %-7s %s' % (n, '%d/10' % dom, '%d pts' % coste, '%.0f%%' % (nulo * 100), ' '.join(rep)))

print()
print('=' * 78)
print(' 4. Lo que pasa de verdad: exito medio por ficha y tarjeta')
print('=' * 78)
print('  (suponiendo que lo que pide el Director se reparte por igual entre las 40')
print('   disciplinas: es un suelo, porque en la practica se juega a lo que sabes)')
print()
MOD = {
    'hoy: nulo por ambito': lambda dom: 0.0,
    'propuesta: nulo por columna': lambda dom: (10 - dom) / 10.0,
    'intermedio: -1 si el ambito esta abierto': None,
}
for carta in ('Epica', 'Bola de nieve', 'Angustia'):
    print('  --- %s' % carta)
    print('     %-22s %-12s %-12s %s' % ('ficha', 'hoy', 'por columna', 'intermedio (-1)'))
    for n, dom, dis, fir, coste in FICHAS:
        base = dom * 4
        con4 = min(fir, base)
        con2 = min(dis, base - con4)
        con0 = base - con2 - con4
        fuera = (10 - dom) * 4
        # hoy: lo de fuera sale a +0 (el ambito esta abierto casi siempre)
        hoy = (con4 * pct(carta, 4) + con2 * pct(carta, 2) + (con0 + fuera) * pct(carta, 0)) / 40.0
        # columna: lo de fuera sale a -2
        col = (con4 * pct(carta, 4) + con2 * pct(carta, 2) + con0 * pct(carta, 0) + fuera * pct(carta, -2)) / 40.0
        # intermedio: fuera del dominio pero dentro del ambito -> -1; ambito cerrado -> -2
        amb_abiertos = min(5, dom)            # ambitos tocados
        col_cerradas_en_amb_abierto = max(0, amb_abiertos * 2 - dom)
        col_cerradas_fuera = 10 - dom - col_cerradas_en_amb_abierto
        inter = (con4 * pct(carta, 4) + con2 * pct(carta, 2) + con0 * pct(carta, 0)
                 + col_cerradas_en_amb_abierto * 4 * pct(carta, -1)
                 + col_cerradas_fuera * 4 * pct(carta, -2)) / 40.0
        print('     %-22s %-12s %-12s %s' % (n, '%.0f%%' % hoy, '%.0f%%' % col, '%.0f%%' % inter))
    print()

print('=' * 78)
print(' 5. El caso que me preocupa: especialista + nulidad por columna + Angustia')
print('=' * 78)
n, dom, dis, fir, coste = FICHAS[1]
fuera = (10 - dom) * 4
print('  Un especialista normal (4 columnas de 10) en Angustia:')
print('    %d de 40 disciplinas a -2, y a -2 en Angustia se acierta el %.0f%%.' % (fuera, pct('Angustia', -2)))
print('    Seis de cada diez cosas que le pidan, las falla nueve de cada diez veces.')
print('    Exito medio de la ficha: %.0f%%.' % (
    (min(fir, dom * 4) * pct('Angustia', 4) + min(dis, dom * 4 - fir) * pct('Angustia', 2)
     + (dom * 4 - min(fir, dom * 4) - min(dis, dom * 4 - fir)) * pct('Angustia', 0)
     + fuera * pct('Angustia', -2)) / 40.0))
