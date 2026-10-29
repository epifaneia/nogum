# -*- coding: utf-8 -*-
"""Las tablas del Apendice B contra el modelo de probabilidad.

El Apendice B imprime, para cada una de las ocho tarjetas (las siete del
Cuadrante y la Tragedia), el reparto de una tirada bono a bono: pifia, fallo,
coste, exito, critico y lo que sale adelante. Esas cifras se escribieron una
vez desde `curvas.py`, pero viven en el fragmento como texto: si alguien cambia
una banda de pifia en el modelo, o retoca a mano una celda en un idioma y no en
el otro, el libro y el sistema dejan de decir lo mismo sin que nada se queje.

Esto lo caza. Lee las ocho tablas de cada idioma (fB_apendices.html y su espejo
.en.html), recalcula cada fila con `curvas.reparto` y `curvas.sale`, redondeadas
a entero como se imprimen, y compara. Ocho tablas, siete bonos (de -2 a +4):
56 filas por idioma.

Sale con codigo 1 si falta una tabla o una fila, o si una sola cifra no cuadra.
"""
import io, os, re, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from curvas import CARTAS, reparto, sale, BONOS

# El orden en que el apendice imprime las tablas (el del Cuadrante y, al final,
# la excepcion declarada). Cada tabla va debajo de su <h3>/<h4>, pero el orden
# basta y es lo que se comprueba: ocho tablas, en este orden, ni una mas.
ORDEN = ['EPICA', 'PULP', 'REAL', 'PRIM', 'BOLA', 'ANG', 'PES', 'TRAG']
C = {c[0]: c for c in CARTAS}

FRAG = [('es', 'v2/fB_apendices.html', '<h2>Apéndice B'),
        ('en', 'v2/fB_apendices.en.html', '<h2>Appendix B')]


def bono(celda):
    # «−2», «+0», «+4»: el menos tipografico es U+2212
    return int(celda.replace('−', '-').replace('+', ''))


fallos = []
total = 0
L = '=' * 68
print(L); print(' APENDICE B CONTRA curvas.py'); print(L)
for lengua, ruta, marca in FRAG:
    s = io.open(ruta, encoding='utf-8').read()
    if marca not in s:
        fallos.append('%s: no encuentro «%s»' % (ruta, marca)); continue
    s = s[s.index(marca):]
    tablas = re.findall(r'<table class="t t7n">.*?</table>', s, re.S)
    if len(tablas) != len(ORDEN):
        fallos.append('%s: %d tablas, se esperaban %d' % (lengua, len(tablas), len(ORDEN)))
    filas = malas = 0
    for k, t in zip(ORDEN, tablas):
        vistos = []
        for b_txt, resto in re.findall(r'<tr><td>(.*?)</td>(.*?)</tr>', t):
            b = bono(b_txt)
            vistos.append(b)
            impreso = [int(x) for x in re.findall(r'(\d+)&nbsp;%', resto)]
            modelo = [round(x * 100) for x in reparto(C[k], b)] + [round(sale(C[k], b) * 100)]
            filas += 1
            if impreso != modelo:
                malas += 1
                fallos.append('%s %s bono %+d: impreso %s, modelo %s' % (lengua, C[k][1], b, impreso, modelo))
        if vistos != BONOS:
            fallos.append('%s %s: bonos %s, se esperaban %s' % (lengua, C[k][1], vistos, BONOS))
    total += filas
    print('  %s  tablas:%d  filas:%d  discrepancias:%d' % (lengua, len(tablas), filas, malas))

print(); print(L)
if fallos:
    print(' RESULTADO: %d problema(s)' % len(fallos))
    for x in fallos: print('  - ' + x)
else:
    print(' RESULTADO: limpio. %d filas comparadas.' % total)
print(L)
sys.exit(1 if fallos else 0)
