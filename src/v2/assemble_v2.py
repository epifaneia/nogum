# Monta el Juego completo v2 (castellano) en un HTML local para compararlo con
# el viejo. No toca nada fuera de NOGUM_v2/: ni out3/, ni docs/, ni los p3_*.
# Las piezas comunes (licencia, numeros en rojo, limpieza editorial, lamina)
# se copian de assemble3.py leyendo su codigo, sin ejecutarlo: assemble3
# regenera las portadas viejas al importarse.
import ast, os, re, json, shutil, sys
from html.parser import HTMLParser

V2 = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.dirname(V2)
ROOT = os.path.dirname(SRC)
OUT = os.path.join(ROOT, 'NOGUM_v2')

def R(*p): return open(os.path.join(*p), encoding='utf-8').read()

# --- lo que se reaprovecha de assemble3.py
NEED = {'AUTOR', 'LICENCIA', 'LIC', 'COLOFON', 'colofon', 'NUM_H', 'num_rojo', 'FOTO', 'con_foto', 'limpia_editorial'}
code = R(SRC, 'assemble3.py')
ns = {'re': re}
for node in ast.parse(code).body:
    names = set()
    if isinstance(node, (ast.FunctionDef, ast.ClassDef)): names = {node.name}
    elif isinstance(node, ast.Assign): names = {t.id for t in node.targets if isinstance(t, ast.Name)}
    if names & NEED:
        exec(ast.get_source_segment(code, node), ns)

# --- el orden del libro nuevo
def parte(f):
    p = os.path.join(V2, f)
    if not os.path.exists(p):
        print('  FALTA', f); return ''
    return R(p)

def corta(s, marca):
    i = s.find(marca)
    return (s, '') if i < 0 else (s[:i], s[i:])

ch6, ch8 = corta(parte('fI_cap6_cap8.html'), '<section class="chapter" id="ch8"')
faq, glos = corta(parte('fH_faq_glosario.html'), '<section class="chapter" id="apx-glosario"')
bazar = parte('fK1_bazar_a.html') + parte('fK2_bazar_b.html') + parte('fK3_bazar_c.html')
ORDEN = [parte('p_juego_v2.html'), parte('fA_ideas_intro_0_1.html'), parte('fC_cap2.html'), parte('fD_cap3.html'),
         parte('fE_cap4.html'), parte('fF_cap5.html'), ch6, parte('fG_cap7.html'), ch8, faq,
         parte('fJ1_cap9a.html'), bazar, parte('fJ2_cap9b.html'), glos, parte('fB_apendices.html'),
         parte('fL_referencia.html')]

class Chk(HTMLParser):
    void = {'br', 'hr', 'img', 'input', 'meta', 'link', 'col', 'wbr', 'source'}
    def __init__(s):
        super().__init__(); s.st = []; s.err = []; s.ids = {}
    def handle_starttag(s, t, a):
        d = dict(a)
        if 'id' in d: s.ids[d['id']] = s.ids.get(d['id'], 0) + 1
        if t not in s.void: s.st.append(t)
    def handle_endtag(s, t):
        if t in s.void: return
        if not s.st or s.st[-1] != t:
            s.err.append((t, s.getpos()[0]))
            if t in s.st: del s.st[len(s.st) - 1 - s.st[::-1].index(t):]
        else: s.st.pop()

def informe(body):
    v = Chk(); v.feed(body)
    dups = sorted(k for k, n in v.ids.items() if n > 1)
    miss = sorted({h for h in re.findall(r'href="#([^"]+)"', body) if h not in v.ids})
    print(f'  etiquetas mal cerradas: {len(v.err)} {v.err[:6]}')
    print(f'  ids repetidos: {len(dups)} {dups[:12]}')
    print(f'  enlaces rotos: {len(miss)} {miss[:30]}')
    return dups, miss

def build():
    body = ''.join(ORDEN)
    # el Acelerado es otra pieza: se enlaza la version actual
    body = body.replace('href="#acelerado"', 'href="../src/out3/NOGUM_acelerado.html"')
    body = ns['limpia_editorial'](body)
    # las marcas de origen se quedan solo con su codigo (T…, ED-…, C·…): las de
    # texto («Aprobado por el autor», «Borrador»…) son notas de edicion
    SRCOK = re.compile(r'(?:\s*(?:T\d+(?:[–-]T?\d+)?|ED-[A-Z]?\d+|C·[a-z0-9]+(?:\s*·\s*[a-z0-9]+)?)\s*[,·]?\s*)+')
    def src(m):
        codes = re.findall(r'T\d+(?:[–-]T?\d+)?|ED-[A-Z]?\d+|C·[a-z0-9]+', m.group(1))
        if SRCOK.fullmatch(m.group(1)): return m.group(0)
        return ('<span class="src">' + ' '.join(codes) + '</span>') if codes else ''
    body = re.sub(r'<span class="src">([^<]*)</span>', src, body)
    body = ns['con_foto'](body, 'juego', 'local', 'es')
    body = body + ns['colofon']('es')
    body = ns['num_rojo'](body)
    informe(body)
    css = R(SRC, 'paper.css')
    cfg = json.dumps({'product': 'juego', 'title': {'es': 'NOGUM · Juego completo (v2)'}, 'langs': ['es'],
                      'chapterBreak': True, 'contents': True}, ensure_ascii=False)
    return ('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            '<title>NOGUM · Juego completo (v2)</title>\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@600;800&amp;family=Ibarra+Real+Nova:ital,wght@0,700;1,400&amp;family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&amp;family=JetBrains+Mono:wght@400;600&amp;display=swap">\n'
            f'<style>{css}</style>\n</head>\n<body>\n'
            '<header class="top">\n<button class="tool menu-btn" id="menuBtn" aria-controls="side" aria-expanded="false">Índice</button>\n'
            '<span class="brand"><span class="dice" aria-hidden="true"><i></i><i></i></span><b>NOGUM</b><small>Juego completo · v2</small></span>\n'
            '<nav class="products" aria-label="NOGUM"><a href="../src/out3/NOGUM_juego.html">El viejo</a><span aria-current="page">v2</span></nav>\n'
            '<button class="tool" id="printBtn" type="button">Imprimir</button>\n<button class="tool" id="themeBtn" type="button">Tema</button>\n</header>\n'
            '<div class="shell">\n<aside class="side" id="side">\n<div class="search"><label id="qLabel" for="q">Buscar</label><input id="q" type="search" autocomplete="off"></div>\n'
            '<ul class="results" id="results" hidden></ul>\n<ul class="stoc" id="stoc"></ul>\n</aside>\n'
            '<main><p class="status" id="status" role="status"></p><div id="book"></div></main>\n</div>\n'
            f'<script type="application/json" id="cfg">{cfg}</script>\n<template id="src-es">{body}</template>\n'
            f'<script>{js()}</script>\n</body>\n</html>\n')

def js():
    # los arreglos del maquetador ya viven en paper.js
    return R(SRC, 'paper.js')

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    page = build()
    open(os.path.join(OUT, 'NOGUM_juego_v2.html'), 'w', encoding='utf-8').write(page)
    img = os.path.join(ROOT, 'docs', 'img')
    if os.path.isdir(img):
        shutil.copytree(img, os.path.join(OUT, 'img'), dirs_exist_ok=True)
    print('NOGUM_v2/NOGUM_juego_v2.html', len(page.encode()) // 1024, 'KB')
