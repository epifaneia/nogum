# -*- coding: utf-8 -*-
"""Genera las dos listas del taller: el barrido de marcas y las banderas vivas."""
import io, os, re, json, importlib.util
os.chdir(os.path.dirname(os.path.abspath(__file__)))

spec = importlib.util.spec_from_file_location('md', 'marcas_data.py')
md = importlib.util.module_from_spec(spec); spec.loader.exec_module(md)

PUB = ['p3_tesis_es.html', 'p3_tesis_en.html', 'frag_intro.html', 'frag_intro.en.html',
       'frag_ch1a.html', 'frag_ch1a.en.html', 'frag_ch1b.html', 'frag_ch1b.en.html',
       'frag_ch2.html', 'frag_ch2.en.html', 'frag_ch3.html', 'frag_ch3.en.html',
       'frag_ch4.html', 'frag_ch4.en.html', 'frag_ch5.html', 'frag_ch5.en.html',
       'frag_ch67.html', 'frag_ch67.en.html', 'frag_cap8.html', 'frag_cap8.en.html',
       'frag_bazar.html', 'frag_bazar_a.en.html', 'frag_bazar_b.en.html',
       'frag_math.html', 'frag_math.en.html', 'frag_acelerado.html', 'frag_acelerado.en.html']
TXT = {f: io.open(f, encoding='utf-8').read() for f in PUB if os.path.exists(f)}


def claves(nombre):
    base = re.split(r' / |, ', re.sub(r'\s*\([^)]*\)', '', nombre))
    out = []
    for b in base:
        b = b.strip()
        if not b:
            continue
        out.append(b.replace('&', '&amp;'))
    return out


def cuenta(nombre):
    n, donde = 0, set()
    for k in claves(nombre):
        for f, s in TXT.items():
            c = s.count(k)
            if c:
                n += c
                donde.add(f.replace('frag_', '').replace('p3_', '').replace('.html', ''))
    return n, sorted(donde)


MARCAS = []
for gname, lista in md.GRUPOS:
    items = []
    for mid, nombre, riesgo, cands, nota in lista:
        n, donde = cuenta(nombre)
        items.append({'id': mid, 'n': nombre, 'r': riesgo, 'c': cands, 'nota': nota,
                      'veces': n, 'donde': donde[:6]})
    MARCAS.append({'g': gname, 'items': items})

# --- las recetas, con lo que ya dicen sin nombrar la marca
c8 = io.open('frag_cap8.html', encoding='utf-8').read()
RECETAS = []
for m in re.finditer(r'<div class="recipe">(.*?)</div>', c8, re.S):
    b = m.group(1)
    t = re.search(r'<p class="recipe-title">(.*?)</p>', b, re.S)
    r = re.search(r'<p class="recipe-ref">(.*?)</p>', b, re.S)
    lo = re.search(r'<strong>El lore:</strong>(.*?)</p>', b, re.S)
    cl = lambda x: re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', x)).strip() if x else ''
    RECETAS.append({'t': cl(t.group(1) if t else ''), 'ref': cl(r.group(1) if r else ''),
                    'lore': cl(lo.group(1) if lo else '')})

# --- las banderas, ya convertidas en preguntas con propuestas
spec2 = importlib.util.spec_from_file_location('pd', 'preguntas_data.py')
pd = importlib.util.module_from_spec(spec2); spec2.loader.exec_module(pd)
PREG = [{'id': q[0], 'b': q[1], 'd': q[2], 't': q[3], 'q': q[4], 'o': q[5]} for q in pd.P]

# cuantas banderas quedan en los ficheros, para dar el numero de verdad
import glob
nflags = 0
for nme in ['frag_intro', 'frag_ch1a', 'frag_ch1b', 'frag_ch2', 'frag_ch3', 'frag_ch4', 'frag_ch5',
            'frag_ch67', 'frag_cap8', 'frag_bazar', 'frag_math', 'frag_acelerado', 'frag_glosario']:
    if os.path.exists(nme + '.html'):
        nflags += len(re.findall(r'<span class="flag (?:pending|proposal)">',
                                 io.open(nme + '.html', encoding='utf-8').read()))

json.dump({'marcas': MARCAS, 'recetas': RECETAS, 'preguntas': PREG, 'nflags': nflags},
          io.open('taller_listas.json', 'w', encoding='utf-8'), ensure_ascii=False)
print('marcas:', sum(len(g['items']) for g in MARCAS),
      '| menciones:', sum(i['veces'] for g in MARCAS for i in g['items']),
      '| recetas:', len(RECETAS), '| preguntas:', len(PREG), '| banderas en ficheros:', nflags)
