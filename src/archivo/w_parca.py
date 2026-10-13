# -*- coding: utf-8 -*-
"""La Parca: lo que no es un arma. Reescalona el dano del bazar."""
import io, os, re, sys, json, glob
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# nombre en castellano -> nivel de Rejilla que hay que tener para sobrevivir
PARCA = {
    # genericas
    'Arma inevitable': 2,
    'Arma de asedio': 3,
    # neon
    'Cañón de Riel (Railgun)': 2,
    # oeste
    'Dinamita': 2,
    'Gatling de Vapor (portátil)': 2,
    # opera
    'Granada Térmica': 2,
    # gotico
    'Granada de Fósforo': 2,
    'Amuleto Solar': 3,
    # postapo
    'Interceptor V8': 2,
    # terror
    'Coche (atropello)': 2,
    # supers
    'Coche Blindado (El coche blindado del justiciero)': 3,
    'Control del Clima (Rayo)': 3,
    # fantasia
    'Aliento de Dragón': 3,
    # wuxia
    'Disco Destructor': 3,
    'Onda de energía a dos manos (rayo)': 3,
    # toon: la Parca existe, pero alli es un chiste y te levantas en la escena siguiente
    'Bomba Redonda Negra': 2,
    'El Yunque (Caída)': 2,
    'El Yunque Oportuno': 2,
    'Dinamita con Mecha Larga': 2,
    # social y mental
    'El Chantaje (la Prueba)': 2,
    'La Verdad Cósmica': 3,
}

data = json.load(io.open('app_data.json', encoding='utf-8'))
EN = {}
for bz in data['bazar']:
    for bl in bz['blocks']:
        for it in bl['items']:
            EN[it['n'][0]] = it['n'][1]

faltan = [n for n in PARCA if n not in EN]
if faltan:
    print('NO ENCUENTRO ESTOS OBJETOS:')
    for n in faltan:
        print('   ' + n)
    sys.exit(1)

FICH = [f for f in glob.glob('frag_bazar*.html') if '.bak' not in f]
cambios = {'parca': 0, 'baja': 0}

for f in FICH:
    s = io.open(f, encoding='utf-8').read()
    orig = s
    ingles = '.en.' in f
    # 1. los que pasan a Parca
    for es, niv in PARCA.items():
        nom = EN[es] if ingles else es
        i = s.find('<strong>' + nom + '</strong>')
        if i < 0:
            continue
        j = s.find('</tr>', i)
        fila = s[i:j]
        nueva = re.sub(r'<span class="tag">(?:Daño|Dmg)[^<]*</span>',
                       '<span class="tag parca">%s · %s %d</span>'
                       % ('The Reaper' if ingles else 'La Parca', 'Grid' if ingles else 'Rejilla', niv),
                       fila, count=1)
        if nueva != fila:
            s = s[:i] + nueva + s[j:]
            cambios['parca'] += 1
    # 2. todo lo demas que siguiera en 3 o mas baja a 2: el tope de un arma es 2
    def baja(m):
        cambios['baja'] += 1
        return m.group(1) + '2' + m.group(3)
    s = re.sub(r'(<span class="tag">(?:Daño|Dmg)\s*)([3-9])([^<]*</span>)', baja, s)
    if s != orig:
        io.open(f, 'w', encoding='utf-8').write(s)
        print('  %-26s tocado' % f)

print()
print('Parca marcada: %d filas   ·   bajadas a Dano 2: %d' % (cambios['parca'], cambios['baja']))
