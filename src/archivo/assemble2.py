import re, html, os, json
from html.parser import HTMLParser
D = os.path.dirname(os.path.abspath(__file__))
def R(n): return open(os.path.join(D, n), encoding='utf-8').read()
UP = os.path.join(D, 'urls.json')
URLS = json.load(open(UP, encoding='utf-8')) if os.path.exists(UP) else {}
CSS = R('base.css') + R('book.css')
JS = R('book.js')

cap8 = R('frag_cap8.html'); bazar = R('frag_bazar.html'); math = R('frag_math.html')
m13, mD = math.split('<section class="chapter" id="apx-mates">', 1)
mD = '<section class="chapter" id="apx-mates">' + mD
k = cap8.find('<h3 id="ch8-recetas"')
cap8 = cap8[:k] + '</section>\n' + bazar + '\n<section class="chapter" id="ch8b">\n<h2>8.4 Simulación de manuales</h2>\n' + cap8[k:]
reglas = ''.join([R('frag_intro.html'), R('frag_ch1a.html'), m13, R('frag_ch1b.html'), R('frag_ch2.html'),
                  R('frag_ch3.html'), R('frag_ch4.html'), R('frag_ch5.html'), R('frag_ch67.html')])
apend = cap8 + mD

PRODUCTS = {
    'juego': dict(title='NOGUM Juego Completo', sub='Juego completo', views=[
        ('inicio', 'Portada', R('p_juego_home.html'), 0), ('reglas', 'Reglas', reglas, 1), ('apendices', 'Apéndices', apend, 1)]),
    'acelerado': dict(title='NOGUM Acelerado', sub='Acelerado', views=[
        ('inicio', 'Portada', R('p_acel_home.html'), 0), ('manual', 'Manual', R('frag_acelerado.html'), 1)]),
    'tesis': dict(title='NOGUM Tesis', sub='Tesis filosófica', views=[
        ('es', 'Español', R('p_tesis_es.html'), 1), ('en', 'English', R('p_tesis_en.html'), 1)]),
    'cuaderno': dict(title='NOGUM Cuaderno de Edición', sub='Cuaderno de edición', views=[
        ('inicio', 'Resumen', R('frag_home.html'), 0), ('decisiones', 'Decisiones', R('frag_editorial.html'), 1),
        ('descartados', 'Descartados', R('frag_descartados.html'), 1), ('traza', 'Trazabilidad', R('frag_trazabilidad.html'), 1)]),
}
ORDER = ['tesis', 'juego', 'acelerado', 'app', 'cuaderno']
LABELS = {'tesis': 'Tesis', 'juego': 'Juego', 'acelerado': 'Acelerado', 'app': 'App', 'cuaderno': 'Cuaderno'}
IDS = {p: set(re.findall(r'\bid="([^"]+)"', ''.join(v[2] for v in c['views']))) for p, c in PRODUCTS.items()}

def clean(t): return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', t)).strip()

def toc_for(view, label, body):
    out = [f'<li class="g" data-view="{view}">{html.escape(label)}</li>']
    pat = r'<section class="chapter[^"]*" id="([^"]+)"[^>]*>\s*<h2>(.*?)</h2>|<h3 id="([^"]+)"[^>]*>(.*?)</h3>'
    for m in re.finditer(pat, body, re.S):
        if m.group(1):
            out.append(f'<li><a class="h2" data-view="{view}" href="#{m.group(1)}">{html.escape(clean(m.group(2)))}</a></li>')
        else:
            t = re.sub(r'\s*(Propuesta sin validar|Unvalidated proposal|Pendiente|Descartado|ED-[\w-]+)\s*', ' ', clean(m.group(4))).strip()
            out.append(f'<li><a class="h3" data-view="{view}" href="#{m.group(3)}">{html.escape(t)}</a></li>')
    return '\n'.join(out)

def products_nav(me):
    out = []
    for p in ORDER:
        if p == me:
            out.append(f'<a aria-current="page" href="#">{LABELS[p]}</a>')
        elif URLS.get(p):
            out.append(f'<a href="{URLS[p]}" target="_blank" rel="noopener">{LABELS[p]}</a>')
    return '<nav class="products" aria-label="Productos NOGUM">' + ''.join(out) + '</nav>'

def fix_cross(body, me):
    def rep(m):
        i = m.group(1)
        if i in IDS[me]:
            return m.group(0)
        for p, s in IDS.items():
            if i in s and URLS.get(p):
                return f'href="{URLS[p]}" target="_blank" rel="noopener"'
        return m.group(0)
    return re.sub(r'href="#([^"]+)"', rep, body)

class V(HTMLParser):
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
            s.err.append(t)
            if t in s.st: del s.st[len(s.st) - 1 - s.st[::-1].index(t):]
        else:
            s.st.pop()

def build(me):
    c = PRODUCTS[me]
    toc = ''.join(toc_for(v, l, b) for v, l, b, _ in c['views'])
    tabs = ''.join(f'<button role="tab" data-view="{v}" aria-selected="false">{html.escape(l)}</button>' for v, l, _, _ in c['views'])
    views = ''.join(f'<div class="view" data-view="{v}" data-paged="{p}" hidden>{fix_cross(b, me)}</div>' for v, l, b, p in c['views'])
    head = ('<title>%s</title>\n<link rel="preconnect" href="https://fonts.googleapis.com">\n'
            '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@600;800&amp;family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&amp;family=JetBrains+Mono:wght@400;600&amp;display=swap">\n'
            '<style>%s</style>\n') % (c['title'], CSS)
    body = (f'<div data-product="{me}">\n<header class="top">\n'
            '<button class="menu-btn" id="menuBtn" aria-controls="side" aria-expanded="false">Índice</button>\n'
            f'<span class="brand"><span class="dice" aria-hidden="true"><i></i><i></i></span><b>NOGUM</b><small>{html.escape(c["sub"])}</small></span>\n'
            f'<nav class="tabs" role="tablist" aria-label="Secciones">{tabs}</nav>\n{products_nav(me)}\n'
            '<button class="theme" id="themeBtn" aria-label="Cambiar tema">Tema</button>\n</header>\n'
            '<div class="shell">\n<aside class="side" id="side" aria-label="Índice y búsqueda">\n'
            '<div class="search"><label for="q" class="search-hint">Buscar en este documento</label>'
            '<input id="q" type="search" placeholder="Llave, Estilo, Vorpalina…" autocomplete="off"></div>\n'
            '<ul class="results" id="results" hidden></ul>\n'
            f'<ul class="toc" id="toc">{toc}</ul>\n</aside>\n<main id="main">{views}</main>\n</div>\n</div>\n'
            f'<script>{JS}</script>\n')
    page = head + body
    v = V(); v.feed(page)
    dups = [k for k, n in v.ids.items() if n > 1]
    names = [x[0] for x in c['views']]
    miss = sorted({h for h in re.findall(r'href="#([^"]+)"', page) if h not in v.ids and h not in names and "'" not in h and '+' not in h})
    print(me, 'errors', v.err[:5], 'dups', dups[:5], 'missing', miss[:15], 'KB', len(page.encode()) // 1024)
    return page

def full_doc(page):
    i = page.index('</style>') + len('</style>')
    return ('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            + page[:i] + '\n</head>\n<body>\n' + page[i:] + '\n</body>\n</html>\n')

def build_app():
    canon = json.dumps(R('CANON.md'), ensure_ascii=False).replace('</', '<\\/')
    page = R('app_body.html').replace('%%CSS%%', CSS).replace('%%PRODUCTS%%', products_nav('app')).replace('%%DIGEST%%', canon)
    v = V(); v.feed(page)
    print('app errors', v.err[:5], 'KB', len(page.encode()) // 1024)
    return page

if __name__ == '__main__':
    out = os.path.join(D, 'out'); os.makedirs(out, exist_ok=True)
    for p in list(PRODUCTS) + ['app']:
        pg = build_app() if p == 'app' else build(p)
        open(os.path.join(out, f'nogum_{p}.html'), 'w', encoding='utf-8').write(pg)
        open(os.path.join(out, f'full_{p}.html'), 'w', encoding='utf-8').write(full_doc(pg))
