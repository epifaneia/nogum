# -*- coding: utf-8 -*-
"""Las cinco piezas, enlazadas desde todas y presentadas juntas en cada portada."""
import io, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
fal = []


def sub(f, a, b, n=1):
    s = io.open(f, encoding='utf-8').read()
    if s.count(a) != n:
        fal.append('%s (%d!=%d) %s' % (f, s.count(a), n, a[:62])); return
    io.open(f, 'w', encoding='utf-8').write(s.replace(a, b, n))


A = 'assemble3.py'

# ------------------------------------------- 1. la app es una pieza mas
sub(A, "LOCAL = {'tesis': 'NOGUM_tesis.html', 'juego': 'NOGUM_juego.html', 'acelerado': 'NOGUM_acelerado.html', 'cuaderno': 'NOGUM_cuaderno.html'}",
    "LOCAL = {'tesis': 'NOGUM_tesis.html', 'juego': 'NOGUM_juego.html', 'acelerado': 'NOGUM_acelerado.html',\n"
    "         'cuaderno': 'NOGUM_cuaderno.html', 'app': '../NOGUM_app/NOGUM_app.html'}")
sub(A, "NAV = {'tesis': ('Tesis', 'Thesis'), 'juego': ('Juego', 'Game'), 'acelerado': ('Acelerado', 'Accelerated'), 'cuaderno': ('Cuaderno', 'Notebook')}\n"
       "MANUALS = ['tesis', 'juego', 'acelerado']",
    "NAV = {'tesis': ('Tesis', 'Thesis'), 'juego': ('Juego', 'Game'), 'acelerado': ('Acelerado', 'Accelerated'),\n"
    "       'cuaderno': ('Cuaderno', 'Notebook'), 'app': ('App', 'App')}\n"
    "MANUALS = ['tesis', 'juego', 'acelerado']\n"
    "# NOGUM se publica como un pack de cinco piezas, y las cinco se enlazan\n"
    "# entre si desde todas. El orden es el de lectura, no el de importancia.\n"
    "PIEZAS = ['tesis', 'juego', 'acelerado', 'cuaderno', 'app']\n"
    "PACK = {\n"
    "  'tesis': ('Por que el juego es asi: el argumento entero, sin reglas.',\n"
    "            'Why the game is like this: the whole argument, with no rules.'),\n"
    "  'juego': ('El manual completo: el motor, los personajes, el peligro, el Bazar y las veinte recetas.',\n"
    "            'The complete manual: the engine, characters, danger, the Bazaar and the twenty recipes.'),\n"
    "  'acelerado': ('El mismo juego en quince paginas: tres modos de tono y nueve casillas de vida.',\n"
    "                'The same game in fifteen pages: three tone modes and nine health boxes.'),\n"
    "  'cuaderno': ('Que se decidio, que se tiro y por que. El diario de la edicion.',\n"
    "               'What was decided, what was dropped and why. The editing diary.'),\n"
    "  'app': ('Monta la mesa con cuatro formularios, haz las fichas y pasalas con el Codigo.',\n"
    "          'Set up the table with four forms, build the sheets and pass them on with the Code.'),\n"
    "}")

# --------------------------------- 2. la barra de arriba lleva las cinco
sub(A, """def nav(me, mode):
    items = MANUALS + (['cuaderno'] if me == 'cuaderno' else [])
    out = []
    for p in items:""",
    """def nav(me, mode):
    out = []
    for p in PIEZAS:""")

# ------------------------------------- 3. el pack, presentado en la portada
sub(A, "def fix_cross(body, me, mode):",
    '''def pack(me, mode, lang):
    """Las cinco piezas, en la portada de cada una. La que estas leyendo no es
    un enlace: se marca para que se vea donde estas dentro del pack."""
    en = lang == 'en'
    h = ('NOGUM son cinco piezas', 'NOGUM is five pieces')[en]
    sub_ = ('Esta es la %s. Las otras cuatro estan a un clic.',
            'This is the %s. The other four are one click away.')[en]
    filas = []
    for p in PIEZAS:
        nom = NAV[p][1 if en else 0]
        que = PACK[p][1 if en else 0]
        aqui = ' class="aqui"' if p == me else ''
        if p == me:
            cab = '<strong>%s</strong> <em>%s</em>' % (nom, ('estas aqui', 'you are here')[en])
        else:
            tgt = '' if mode == 'local' else ' target="_blank" rel="noopener"'
            cab = '<a href="%s"%s>%s</a>' % (href_for(p, mode), tgt, nom)
        filas.append('<li%s>%s<span>%s</span></li>' % (aqui, cab, que))
    return ('<div class="pack"><p class="pack-h">%s</p><p class="pack-t">%s</p><ol>%s</ol></div>\\n'
            % (h, sub_ % (NAV[me][1 if en else 0]), ''.join(filas)))

def con_pack(body, me, mode, lang):
    """Lo mete dentro de la portada, justo antes de cerrarla."""
    i = body.find('<section class="cover"')
    if i < 0:
        return body
    j = body.find('</section>', i)
    if j < 0:
        return body
    return body[:j] + pack(me, mode, lang) + body[j:]

def fix_cross(body, me, mode):''')

if fal:
    print('FALLOS:')
    for x in fal:
        print('  ' + x)
    sys.exit(1)
print('assemble3: piezas, barra y pack listos (falta engancharlo en build)')
