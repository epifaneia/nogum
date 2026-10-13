# -*- coding: utf-8 -*-
"""Fichas tecnicas incompletas: lleva dano pero le falta Esq o Abs."""
import io, os, re, collections
os.chdir(os.path.dirname(os.path.abspath(__file__)))
s = io.open('frag_bazar.html', encoding='utf-8').read()

tx = lambda x: re.sub(r'<[^>]+>', ' ', x).strip()
inc, full, esq_c, dmg_c = [], 0, collections.Counter(), collections.Counter()
for tb in re.findall(r'<tbody>(.*?)</tbody>', s, re.S):
    for tr in re.findall(r'<tr>.*?</tr>', tb, re.S):
        tds = re.findall(r'<td[^>]*>(.*?)</td>', tr, re.S)
        if len(tds) != 6:
            continue
        name, dmg, esq, ab = tx(tds[0]), tds[1], tds[2], tds[3]
        hasd = ('Daño' in dmg) or ('Daño' in tds[4])
        if hasd:
            d = re.search(r'Daño[^<]*?(\d)', dmg)
            dmg_c[d.group(1) if d else '?'] += 1
            e = re.search(r'Esq: *([A-Za-zÁ-ú]+)', esq)
            esq_c[e.group(1) if e else 'SIN'] += 1
            if 'Esq:' not in esq or 'Abs:' not in ab:
                inc.append((name, tx(dmg), tx(esq), tx(ab), tx(tds[5])[:60]))
        elif 'Esq:' in esq:
            full += 1
print('objetos con dano:', sum(dmg_c.values()), dict(dmg_c))
print('etiqueta de esquiva:', dict(esq_c))
print('con Esq pero sin dano:', full)
print('--- incompletos:', len(inc))
io.open('tmp_sec.txt', 'w', encoding='utf-8').write('\n'.join(' | '.join(x) for x in inc))
