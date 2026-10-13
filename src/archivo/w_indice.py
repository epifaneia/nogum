# -*- coding: utf-8 -*-
"""Indice cruzado del Bazar: los 347 objetos ordenados por categoria y por Acceso.
Se genera desde app_data.json, asi que los dos idiomas salen del mismo sitio."""
import io, os, re, json
os.chdir(os.path.dirname(os.path.abspath(__file__)))
D = json.load(io.open('app_data.json', encoding='utf-8'))

CAT = ['arma', 'defensa', 'vehiculo', 'artefacto', 'util']
NAMES = {
 'arma':      ('Armas', 'Weapons'),
 'defensa':   ('Defensas', 'Defences'),
 'vehiculo':  ('Vehículos', 'Vehicles'),
 'artefacto': ('Artefactos y poderes', 'Artefacts and powers'),
 'util':      ('Útiles', 'Tools'),
}
RE_VEH = re.compile(u'\b(?:vehículos?|coche|moto|motocicleta|nave|caballo|montura|buggy|jetpack|barco|exoesqueleto|mecha|interceptor|aeronave|embarcación|carro|dron|carreta|vehicles?|cars?|bikes?|ships?|horses?|mounts?|boats?|exoskeletons?|aircraft|vessels?|drones?|steeds?|wagons?)\b', re.I)
RE_DEF = re.compile(u'\b(?:armadura|escudo|blindaje|absorbe|absorción|protección|casco|yelmo|cota|placas|chaleco|cobertura|barrera|coraza|armour|armor|shield|plating|soaks?|protection|helm|mail|plate|vest|cover|barrier)\b|campo de fuerza|force field|capa de desplazamiento', re.I)
RE_ART = re.compile(u'\b(?:poder(?:es)?|artefactos?|magia|mágico|técnicas?|mutación|mutaciones|ocultismo|místico|místicos|mística|disciplinas?|hechizo|ritual|reliquia|powers?|artefacts?|artifacts?|magic|techniques?|mutations?|occult|mystic|disciplines?|spell|relic)\b', re.I)


def classify(block_name, it):
    blob = ' '.join([it['n'][0], it['x'][0], it['m'][0]])
    if it['d'][0] not in ('—', '-', ''):
        if RE_VEH.search(it['n'][0]):
            return 'vehiculo'
        return 'arma'
    if RE_VEH.search(it['n'][0] + ' ' + it['x'][0]):
        return 'vehiculo'
    if RE_DEF.search(blob):
        return 'defensa'
    if RE_ART.search(block_name) or 'Llave' in it['m'][0] or 'Rejilla' in it['m'][0] or 'Grid' in it['m'][1]:
        return 'artefacto'
    if RE_ART.search(blob):
        return 'artefacto'
    return 'util'


rows = {c: [] for c in CAT}
for b in D['bazar']:
    world = b['n']
    for bl in b['blocks']:
        for it in bl['items']:
            c = classify(bl['n'][0], it)
            acc = re.search(r'(?:Acceso|Access) (\d)', it['m'][0] + it['m'][1])
            key = re.search(r'(\d+) (?:Llaves|Keys)', it['m'][0] + it['m'][1])
            pts = re.search(r'(\d+) (?:puntos?|points?)', it['m'][0] + it['m'][1])
            rows[c].append({
                'n': it['n'], 'w': world,
                'acc': int(acc.group(1)) if acc else None,
                'k': int(key.group(1)) if key else 0,
                'p': int(pts.group(1)) if pts else 0,
                'd': it['d'], 'e': it['e'],
            })

for c in CAT:
    rows[c].sort(key=lambda r: (r['acc'] if r['acc'] is not None else 9, -r['k'], r['n'][0]))


def esc(x):
    return x


def build(es):
    L = 0 if es else 1
    h = ['<h3 id="bz-indice">%s</h3>\n' % ('Índice del Bazar por categorías' if es else 'Bazaar index by category')]
    h.append('<p>%s</p>\n' % (
        'El catálogo está ordenado por mundos, porque así es como se lee el tono. Esta es la otra puerta: '
        'los mismos objetos ordenados por <strong>qué son</strong> y por <strong>cuánto cuestan</strong>, '
        'para cuando lo que buscas es un arma de Acceso 1 y te da igual de qué ambientación salga. '
        'La categoría es una ayuda de lectura, no una regla: un exoesqueleto es vehículo y defensa a la vez, '
        'y lo hemos puesto donde más se usa.'
        if es else
        'The catalogue is ordered by world, because that is how tone reads. This is the other door: '
        'the same objects ordered by <strong>what they are</strong> and <strong>what they cost</strong>, '
        'for when what you want is an Access 1 weapon and you do not care which setting it came from. '
        'The category is a reading aid, not a rule: an exoskeleton is both vehicle and defence, '
        'and we have filed it where it gets used.'))
    for c in CAT:
        rs = rows[c]
        h.append('<h4>%s <span class="small">(%d)</span></h4>\n' % (NAMES[c][L], len(rs)))
        h.append('<div class="tw"><table class="t idx">\n<thead><tr><th>%s</th><th>%s</th><th>%s</th><th class="num">%s</th></tr></thead>\n<tbody>\n'
                 % (('Objeto', 'De dónde', 'Qué hace', 'Precio') if es else ('Item', 'From', 'What it does', 'Price')))
        for r in rs:
            what = []
            if r['d'][L] not in ('—', '-', ''):
                what.append(r['d'][L])
            if r['e'][L] not in ('—', '-', ''):
                what.append(r['e'][L])
            price = []
            if r['acc'] is not None:
                price.append(('Acceso ' if es else 'Access ') + str(r['acc']))
            if r['p']:
                price.append('%d %s' % (r['p'], ('puntos' if r['p'] > 1 else 'punto') if es else ('points' if r['p'] > 1 else 'point')))
            if r['k']:
                price.append('%d %s' % (r['k'], 'Llaves' if es else 'Keys'))
            h.append('<tr><td>%s</td><td class="small">%s</td><td class="small">%s</td><td class="num small">%s</td></tr>\n'
                     % (r['n'][L], r['w'][L].replace('&amp;', '&'), ' · '.join(what) or '—', ' · '.join(price) or '—'))
        h.append('</tbody></table></div>\n')
    return ''.join(h)


def put(f, txt):
    s = io.open(f, encoding='utf-8').read()
    k = s.rindex('</section>')
    s = s[:k] + txt + s[k:]
    io.open(f, 'w', encoding='utf-8').write(s)
    print(' ', f, 'ok')


put('frag_bazar.html', build(True))
put('frag_bazar_b.en.html', build(False))
print({c: len(rows[c]) for c in CAT}, 'total', sum(len(rows[c]) for c in CAT))
