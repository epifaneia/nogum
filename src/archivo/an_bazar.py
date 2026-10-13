# -*- coding: utf-8 -*-
"""Radiografia del Bazar antes de tocarlo: cabeceras, filas y etiquetas."""
import io, os, re, collections
os.chdir(os.path.dirname(os.path.abspath(__file__)))
s = io.open('frag_bazar.html', encoding='utf-8').read()

heads = re.findall(r'<thead><tr>(.*?)</tr></thead>', s, re.S)
c = collections.Counter()
for h in heads:
    cols = tuple(re.findall(r'<th[^>]*>(.*?)</th>', h, re.S))
    c[cols] += 1
print('--- cabeceras distintas:', len(c))
for cols, n in c.most_common():
    print(' ', n, '|', ' / '.join(x.replace('<br>', ' ')[:22] for x in cols))

rows = re.findall(r'<tr><td>(?!<strong>Objeto).*?</tr>', s, re.S)
print('--- filas de tbody:', len(re.findall(r'<tbody>(.*?)</tbody>', s, re.S)))
tot = 0
for tb in re.findall(r'<tbody>(.*?)</tbody>', s, re.S):
    tot += len(re.findall(r'<tr>', tb))
print('--- filas totales:', tot)
print('--- Dano N:', len(re.findall(r'Daño \d', s)))
print('--- Esq:', len(re.findall(r'Esq:', s)))
print('--- Rejilla: Llave N:', re.findall(r'Rejilla: Llave N(\d)', s))
print('--- Rejilla: otros:', collections.Counter(re.findall(r'Rejilla: ([^<]{0,18})', s)).most_common(12))
print('--- h3/h4:', len(re.findall(r'<h3', s)), len(re.findall(r'<h4', s)))
