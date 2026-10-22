# -*- coding: utf-8 -*-
"""El catalogo de Firmas de la app (firmas.json), sacado del libro.

Lee «Las 200 Firmas» de 9.2 (v2/fJ1_cap9a.html y su .en.html) y escribe
firmas.json: 40 entradas, una por Disciplina, en el orden en que la app las
busca (Ambito · Dominio · Disciplina: indice ai*8 + di*4 + si). Asi el
catalogo de la app no se queda atras cuando el libro cambia una Firma de
sitio o de nombre (DECISIONES-ultimas D y L).
  python -I extract_firmas.py
"""
import io, json, os, re
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def filas(ruta):
    s = io.open(ruta, encoding='utf-8').read()
    a = s.index('id="cat-firmas"') if 'id="cat-firmas"' in s else s.index('200 ')
    s = s[a:]
    out, dis = [], None
    for m in re.finditer(r'<tr><td class="small">(.*?)</td><td><strong>(.*?)</strong></td><td class="small">(.*?)</td></tr>', s):
        d, n, q = m.groups()
        if d.strip():
            dis = re.sub(r'<[^>]+>', '', d).split('·')[-1].strip()
        out.append((dis, re.sub(r'<[^>]+>', '', n).strip(), re.sub(r'<[^>]+>', '', q).strip()))
    return out

es, en = filas('v2/fJ1_cap9a.html'), filas('v2/fJ1_cap9a.en.html')
assert len(es) == len(en) == 200, (len(es), len(en))
# el orden de las 40 Disciplinas es el de la app: lo da el firmas.json anterior
viejo = json.load(io.open('firmas.json', encoding='utf-8'))
orden = [e['dis'] for e in viejo]
por = {}
for (de, ne, qe), (di, ni, qi) in zip(es, en):
    por.setdefault(de, {'dis': [de, di], 'items': []})['items'].append({'n': [ne, ni], 'd': [qe, qi]})
# los nombres se comparan sin mayusculas: manda como los escribe el libro
low = {k.lower(): v for k, v in por.items()}
assert sorted(low) == sorted(d[0].lower() for d in orden), set(low) ^ {d[0].lower() for d in orden}
nuevo = [low[d[0].lower()] for d in orden]
for e, d in zip(nuevo, orden):
    assert e['dis'][1].lower() == d[1].lower(), (e['dis'], d)
io.open('firmas.json', 'w', encoding='utf-8').write(json.dumps(nuevo, ensure_ascii=False, indent=1))
print('firmas.json: %d Disciplinas, %d Firmas' % (len(nuevo), sum(len(e['items']) for e in nuevo)))
