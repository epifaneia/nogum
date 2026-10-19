import re, html, os, json, sys
from html.parser import HTMLParser
D = os.path.dirname(os.path.abspath(__file__))
def R(n): return open(os.path.join(D, n), encoding='utf-8').read()
exec(open(os.path.join(D, 'make_covers.py'), encoding='utf-8').read())

URLS = json.load(open(os.path.join(D, 'urls.json'), encoding='utf-8'))
# tres destinos y cada uno con sus enlaces: la carpeta local, los artefactos
# de claude.ai y el sitio publico que sirve GitHub Pages.
WEB = {'tesis': 'idea.html', 'juego': 'juego.html', 'acelerado': 'acelerado.html',
       'cuaderno': 'cuaderno.html', 'app': 'app.html'}
LOCAL = {'tesis': 'NOGUM_tesis.html', 'juego': 'NOGUM_juego.html', 'acelerado': 'NOGUM_acelerado.html',
         'cuaderno': 'NOGUM_cuaderno.html', 'app': '../NOGUM_app/NOGUM_app.html'}
CSS = R('paper.css'); JS = R('paper.js')

def juego(lang):
    sfx = '' if lang == 'es' else '.en'
    f = lambda n: R(n + sfx + '.html')
    math = f('frag_math')
    m13, mD = math.split('<section class="chapter" id="apx-mates">', 1)
    mD = '<section class="chapter" id="apx-mates">' + mD
    if lang == 'es':
        bazar = R('frag_bazar.html')
    else:
        a = R('frag_bazar_a.en.html'); b = R('frag_bazar_b.en.html')
        a = a[:a.rstrip().rfind('</section>')]
        b = b.split('\n', 1)[1]
        bazar = a + b
    cap8 = f('frag_cap8')
    k = cap8.find('<h3 id="ch8-recetas"')
    h84 = '8.4 Simulación de manuales' if lang == 'es' else '8.4 Rulebook Emulation'
    cap8 = cap8[:k] + '</section>\n' + bazar + f'\n<section class="chapter" id="ch8b">\n<h2>{h84}</h2>\n' + cap8[k:]
    return ''.join([R(f'p3_juego.{lang}.html'), f('frag_intro'), f('frag_ch1a'), m13, f('frag_ch1b'), f('frag_ch2'),
                    f('frag_ch3'), f('frag_ch4'), f('frag_ch5'), f('frag_ch67'), cap8, f('frag_glosario'), mD])

drop = R('frag_descartados.html').split('dr-verificacion')[0].count('class="flag drop"')
PRODUCTS = {
    'tesis': dict(title={'es': 'NOGUM · La Idea', 'en': 'NOGUM · The Idea'}, langs=['es', 'en'], chapterBreak=False, contents=True,
                  src={'es': R('p3_tesis_es.html'), 'en': R('p3_tesis_en.html')}),
    'juego': dict(title={'es': 'NOGUM · Juego completo', 'en': 'NOGUM · Complete Game'}, langs=['es', 'en'], chapterBreak=True, contents=True,
                  src={'es': juego('es'), 'en': juego('en')}),
    'acelerado': dict(title={'es': 'NOGUM Acelerado', 'en': 'NOGUM Accelerated'}, langs=['es', 'en'], chapterBreak=True, contents=True,
                      src={'es': R('p3_acel.es.html') + R('frag_acelerado.html'), 'en': R('p3_acel.en.html') + R('frag_acelerado.en.html')}),
    'cuaderno': dict(title={'es': 'NOGUM · Cuaderno de edición', 'en': 'NOGUM · Editing Notebook'}, langs=['es'], chapterBreak=True, contents=True,
                     src={'es': R('p3_cuaderno.es.html').replace('%%N_DROP%%', str(drop)) + R('frag_editorial.html') + R('frag_descartados.html') + R('frag_trazabilidad.html')}),
}
NAV = {'tesis': ('La Idea', 'The Idea'), 'juego': ('Juego', 'Game'), 'acelerado': ('Acelerado', 'Accelerated'),
       'cuaderno': ('Cuaderno', 'Notebook'), 'app': ('App', 'App')}
MANUALS = ['tesis', 'juego', 'acelerado']
# NOGUM se publica como un pack de cinco piezas, y las cinco se enlazan
# entre si desde todas. El orden es el de lectura, no el de importancia.
# El Cuaderno no va en el pack: es el diario de trabajo, y un «como se hizo»
# publicado antes de que nadie haya jugado no informa, presume. Sigue siendo
# un producto y sigue enlazando a los demas; simplemente no se anuncia.
PIEZAS = ['tesis', 'juego', 'acelerado', 'app']
PACK = {
  'tesis': ('Por qué el juego es así: el argumento entero, sin reglas.',
            'Why the game is like this: the whole argument, with no rules.'),
  'juego': ('El manual completo: el motor, los personajes, el peligro, el Bazar y las veinte recetas.',
            'The complete manual: the engine, characters, danger, the Bazaar and the twenty recipes.'),
  'acelerado': ('El mismo juego en quince páginas: cuatro modos de tono y la vida que trae cada uno.',
                'The same game in fifteen pages: four tone modes and the health each one brings.'),
  'cuaderno': ('Qué se decidió, qué se tiró y por qué. El diario de la edición.',
               'What was decided, what was dropped and why. The editing diary.'),
  'app': ('Monta la mesa con cuatro formularios, haz las fichas y pásalas con el Código.',
          'Set up the table with four forms, build the sheets and pass them on with the Code.'),
}
IDS = {p: set().union(*[set(re.findall(r'\bid="([^"]+)"', s)) for s in c['src'].values()]) for p, c in PRODUCTS.items()}

def href_for(p, mode):
    if mode == 'local': return LOCAL[p]
    if mode == 'web': return WEB[p]
    return URLS[p]

def nav(me, mode):
    out = []
    for p in (PIEZAS + ['cuaderno'] if me == 'cuaderno' else PIEZAS):
        es, en = NAV[p]
        if p == me:
            # El producto en el que ya estas no es un enlace: apuntaba a
            # #portada, que solo existe en el Cuaderno, asi que en los otros
            # tres era un enlace muerto.
            out.append(f'<span aria-current="page" data-i18n-es="{es}" data-i18n-en="{en}">{es}</span>')
        else:
            tgt = '' if mode in ('local', 'web') else ' target="_blank" rel="noopener"'
            out.append(f'<a href="{href_for(p, mode)}"{tgt} data-i18n-es="{es}" data-i18n-en="{en}">{es}</a>')
    return '<nav class="products" aria-label="NOGUM">' + ''.join(out) + '</nav>'

def pack(me, mode, lang):
    """Las cinco piezas, en la portada de cada una. La que estas leyendo no es
    un enlace: se marca para que se vea donde estas dentro del pack."""
    en = lang == 'en'
    h = (('NOGUM son cinco piezas', 'NOGUM is five pieces') if me == 'cuaderno'
         else ('NOGUM son cuatro piezas', 'NOGUM is four pieces'))[en]
    otras = 4 if me == 'cuaderno' else 3
    sub_ = (('Se leen por separado y se usan juntas. Las otras %d están a un clic.' % otras),
            ('They are read separately and used together. The other %d are one click away.' % otras))[en]
    filas = []
    for p in (PIEZAS + ['cuaderno'] if me == 'cuaderno' else PIEZAS):
        nom = NAV[p][1 if en else 0]
        que = PACK[p][1 if en else 0]
        aqui = ' class="aqui"' if p == me else ''
        if p == me:
            cab = '<strong>%s</strong> <em>%s</em>' % (nom, ('estás aquí', 'you are here')[en])
        else:
            tgt = '' if mode in ('local', 'web') else ' target="_blank" rel="noopener"'
            cab = '<a href="%s"%s>%s</a>' % (href_for(p, mode), tgt, nom)
        filas.append('<li%s>%s<span>%s</span></li>' % (aqui, cab, que))
    return ('<div class="pack"><p class="pack-h">%s</p><p class="pack-t">%s</p><ol>%s</ol></div>\n'
            % (h, sub_, ''.join(filas)))

AUTOR = 'Daniel Martín'
LICENCIA = 'CC BY-SA 4.0'
LIC = {'es': 'https://creativecommons.org/licenses/by-sa/4.0/deed.es',
       'en': 'https://creativecommons.org/licenses/by-sa/4.0/'}

COLOFON = {
 'es': ('<section class="chapter colofon" id="{l}-licencia"><h2>Licencia</h2>'
        '<p class="lede">Esta obra se publica bajo <a href="{u}" target="_blank" rel="noopener">'
        'Creative Commons Atribución-CompartirIgual 4.0</a>. Puedes copiarla, traducirla, modificarla '
        'y construir encima, también con ánimo de lucro, con dos condiciones: <strong>cita al autor</strong> '
        'y <strong>publica lo que construyas bajo la misma licencia</strong>.</p>'
        '<p><strong>Cómo se cita.</strong> «NOGUM, de {a} · {c}», con enlace al original donde el medio '
        'lo permita.</p>'
        '<p><strong>Las reglas son libres.</strong> Las mecánicas de juego no son objeto de derechos de '
        'autor. Puedes escribir material compatible con este sistema sin pedirle permiso a nadie: la '
        'licencia cubre este <em>texto</em>, no el motor. Si lo que quieres es construir sobre NOGUM, '
        'ya puedes.</p>'
        '<p><strong>Lo que la licencia no cubre.</strong> El nombre <strong>NOGUM</strong> y sus signos '
        'de identidad. El contenido es libre; el nombre se queda con su autor, para que nadie firme en '
        'su lugar.</p>'
        '<p class="note">{a} · {c}</p></section>\n'),
 'en': ('<section class="chapter colofon" id="{l}-licencia"><h2>Licence</h2>'
        '<p class="lede">This work is published under <a href="{u}" target="_blank" rel="noopener">'
        'Creative Commons Attribution-ShareAlike 4.0</a>. You may copy it, translate it, modify it and '
        'build on it, commercially included, on two conditions: <strong>credit the author</strong> and '
        '<strong>release whatever you build under the same licence</strong>.</p>'
        '<p><strong>How to credit it.</strong> “NOGUM, by {a} · {c}”, with a link to the original '
        'wherever the medium allows one.</p>'
        '<p><strong>The rules are free.</strong> Game mechanics are not subject to copyright. You can '
        'write material compatible with this system without asking anyone: the licence covers this '
        '<em>text</em>, not the engine. If what you want is to build on NOGUM, you already can.</p>'
        '<p><strong>What the licence does not cover.</strong> The name <strong>NOGUM</strong> and its '
        'identifying marks. The content is free; the name stays with its author, so that nobody signs '
        'in his place.</p>'
        '<p class="note">{a} · {c}</p></section>\n')}


def colofon(lang):
    """La licencia, al final de cada pieza.

    Tres cosas y las tres hacen falta: como se cita, que el nombre NOGUM no
    entra en la licencia, y que las reglas se pueden usar sin permiso. Lo
    ultimo no anade nada legalmente (las mecanicas no son objeto de derechos
    de autor) pero quita la duda que frena a quien querria escribir algo.
    """
    return COLOFON[lang].format(l=lang, u=LIC[lang], a=AUTOR, c=LICENCIA)


# El numero de cada titular, en el rojo del dado: «Capitulo 3 ·», «3.5»,
# «1 ·», «Apendice D ·» y las recetas del Bazar, «1.». Solo se envuelve el
# numero; el buscador y el indice lateral leen textContent y no lo notan.
NUM_H = re.compile(r'(<h[23]\b[^>]*>)(\s*)(?:((?:Capítulo|Chapter|Apéndice|Appendix)\s+)([0-9]+|[A-Z])\b'
                   r'|([0-9]+(?:\.[0-9]+)*\.?)(?=\s))')

def num_rojo(body):
    def r(m):
        if m.group(3):
            return m.group(1) + m.group(2) + m.group(3) + '<span class="hn">%s</span>' % m.group(4)
        return m.group(1) + m.group(2) + '<span class="hn">%s</span>' % m.group(5)
    return NUM_H.sub(r, body)


def con_pack(body, me, mode, lang):
    """Lo mete dentro de la portada, justo antes de cerrarla."""
    i = body.find('<section class="cover"')
    if i < 0:
        return body
    j = body.find('</section>', i)
    if j < 0:
        return body
    return body[:j] + pack(me, mode, lang) + body[j:]

def limpia_editorial(body):
    """Fuera las notas de edicion de los manuales.

    Dos formas distintas de aparecer, y se tratan distinto:
      - un bloque que EMPIEZA por la bandera es una nota entera -> se borra el bloque
      - una bandera al final de una frase util es solo una marca -> se borra la marca
    Lo de «aprobado / propuesta del asistente / pendiente» tampoco va al manual:
    el lector no tiene por que saber que estaba en duda. Todo queda en el
    Cuaderno, que es el sitio de eso."""
    CL = r'flag (?:ed|drop|pending|proposal)'
    # 1. bloques que son la nota entera
    for tag in ('p', 'li', 'aside', 'td', 'th'):
        body = re.sub(r'<' + tag + r'[^>]*>\s*<span class="' + CL + r'"[^>]*>.*?</' + tag + '>', '', body, flags=re.S)
    # 2. marcas sueltas dentro de texto que si vale
    body = re.sub(r'\s*<span class="' + CL + r'"[^>]*>.*?</span>', '', body, flags=re.S)
    # 3. parentesis y comas que quedan colgando
    body = re.sub(r'\(\s*\)', '', body)
    body = re.sub(r'\s+([.,;:])', r'\1', body)
    return body

def fix_cross(body, me, mode):
    def rep(m):
        i = m.group(1)
        if i in IDS[me]: return m.group(0)
        for p, s in IDS.items():
            if p != me and i in s:
                tgt = '' if mode in ('local', 'web') else ' target="_blank" rel="noopener"'
                return f'href="{href_for(p, mode)}"{tgt}'
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
        else: s.st.pop()

def check(me, lang, body):
    v = V(); v.feed(body)
    dups = [k for k, n in v.ids.items() if n > 1]
    miss = sorted({h for h in re.findall(r'href="#([^"]+)"', body) if h not in v.ids})
    ext = len(re.findall(r'href="(?:https?:|NOGUM_)', body))
    print(f'  {me}/{lang}: errors={v.err[:4]} dups={dups[:4]} missing={miss[:8]} crosslinks={ext} app_links={body.count("4BmVxG2cLT1qkgPU6NqBUQ")}')

def build(me, mode):
    c = PRODUCTS[me]
    cfg = json.dumps({'product': me, 'title': c['title'], 'langs': c['langs'], 'chapterBreak': c['chapterBreak'], 'contents': c['contents']}, ensure_ascii=False)
    tpls = ''
    for l in c['langs']:
        b = fix_cross(c['src'][l], me, mode)
        if me != 'cuaderno': b = limpia_editorial(b)
        b = con_pack(b, me, mode, l)
        b = b + colofon(l)
        b = num_rojo(b)
        if mode == 'artifact': check(me, l, b)
        tpls += f'<template id="src-{l}">{b}</template>\n'
    sub_es = {'tesis': 'La Idea', 'juego': 'Juego completo', 'acelerado': 'Acelerado', 'cuaderno': 'Cuaderno de edición'}[me]
    sub_en = {'tesis': 'The Idea', 'juego': 'Complete game', 'acelerado': 'Accelerated', 'cuaderno': 'Editing notebook'}[me]
    head = (f'<title>{c["title"]["es"]}</title>\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@600;800&amp;family=Ibarra+Real+Nova:ital,wght@0,700;1,400&amp;family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&amp;family=JetBrains+Mono:wght@400;600&amp;display=swap">\n'
            f'<style>{CSS}</style>\n')
    body = (f'<header class="top">\n<button class="tool menu-btn" id="menuBtn" aria-controls="side" aria-expanded="false">Índice</button>\n'
            f'<span class="brand"><span class="dice" aria-hidden="true"><i></i><i></i></span><b>NOGUM</b><small data-i18n-es="{sub_es}" data-i18n-en="{sub_en}">{sub_es}</small></span>\n'
            f'{nav(me, mode)}\n'
            '<div class="lang" role="group" aria-label="Idioma / Language"><button type="button" data-lang="es" aria-pressed="true">ES</button><button type="button" data-lang="en" aria-pressed="false">EN</button></div>\n'
            '<button class="tool" id="printBtn" type="button">Imprimir</button>\n<button class="tool" id="themeBtn" type="button">Tema</button>\n</header>\n'
            '<div class="shell">\n<aside class="side" id="side">\n<div class="search"><label id="qLabel" for="q">Buscar</label><input id="q" type="search" autocomplete="off"></div>\n'
            '<ul class="results" id="results" hidden></ul>\n<ul class="stoc" id="stoc"></ul>\n</aside>\n'
            '<main><p class="status" id="status" role="status"></p><div id="book"></div></main>\n</div>\n'
            f'<script type="application/json" id="cfg">{cfg}</script>\n{tpls}<script>{JS}</script>\n')
    page = head + body
    # El esqueleto lo pone claude.ai en los artefactos, pero NO GitHub Pages:
    # sin <!doctype> el navegador entra en modo quirks (las tablas, por
    # ejemplo, dejan de heredar el tamano de letra), sin viewport el movil
    # dibuja la pagina a ancho de escritorio, y sin charset quien la guarde
    # o la abra desde disco ve «Ã­ndice». La version web estuvo asi (T159).
    if mode in ('local', 'web'):
        i = page.index('</style>') + 8
        page = ('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
                + page[:i] + '\n</head>\n<body>\n' + page[i:] + '</body>\n</html>\n')
    return page

if __name__ == '__main__':
    out = os.path.join(D, 'out3'); os.makedirs(out, exist_ok=True)
    local_dir = sys.argv[1] if len(sys.argv) > 1 else None
    # OJO: en Windows el sistema de ficheros no distingue mayusculas, asi que
    # 'nogum_tesis.html' y 'NOGUM_tesis.html' eran EL MISMO FICHERO y la version
    # local pisaba a la de artefacto. Resultado: los enlaces del pack publicados
    # apuntaban a ficheros locales inexistentes. Las de artefacto van aparte.
    art = os.path.join(out, 'art'); os.makedirs(art, exist_ok=True)
    docs = os.path.join(D, '..', 'docs'); os.makedirs(docs, exist_ok=True)
    for p in PRODUCTS:
        a = build(p, 'artifact')
        open(os.path.join(art, f'{p}.html'), 'w', encoding='utf-8').write(a)
        l = build(p, 'local')
        open(os.path.join(out, LOCAL[p]), 'w', encoding='utf-8').write(l)
        if local_dir: open(os.path.join(local_dir, LOCAL[p]), 'w', encoding='utf-8').write(l)
        w = build(p, 'web')
        open(os.path.join(docs, WEB[p]), 'w', encoding='utf-8').write(w)
        print(p, 'KB', len(a.encode()) // 1024)
