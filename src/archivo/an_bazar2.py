# -*- coding: utf-8 -*-
"""Que pinta tienen las filas sin ficha tecnica."""
import io, os, re
os.chdir(os.path.dirname(os.path.abspath(__file__)))
s = io.open('frag_bazar.html', encoding='utf-8').read()

rows, sin, con = [], [], []
for tb in re.findall(r'<tbody>(.*?)</tbody>', s, re.S):
    for tr in re.findall(r'<tr>.*?</tr>', tb, re.S):
        tds = re.findall(r'<td[^>]*>(.*?)</td>', tr, re.S)
        if len(tds) != 6:
            continue
        rows.append(tds)
        (sin if 'Esq:' not in tds[2] else con).append(tds)
print('filas de 6 columnas:', len(rows), '| con Esq:', len(con), '| sin Esq:', len(sin))
out = []
for t in sin[:40]:
    out.append(' | '.join(re.sub(r'<[^>]+>', '', x).strip()[:40] for x in t))
io.open('tmp_sec.txt', 'w', encoding='utf-8').write('\n'.join(out))
print('muestra escrita')
