# -*- coding: utf-8 -*-
"""Indice cruzado del Bazar, version con clasificador por palabras sueltas
(sin fronteras de regex, que se comian los acentos)."""
import io, os, re, json
os.chdir(os.path.dirname(os.path.abspath(__file__)))
D = json.load(io.open('app_data.json', encoding='utf-8'))

CAT = ['arma', 'defensa', 'vehiculo', 'artefacto', 'util']
NAMES = {
    'arma': ('Armas', 'Weapons'),
    'defensa': ('Defensas', 'Defences'),
    'vehiculo': ('Vehículos', 'Vehicles'),
    'artefacto': ('Artefactos y poderes', 'Artefacts and powers'),
    'util': ('Útiles', 'Tools'),
}
W_VEH = set('''vehiculo vehiculos coche coches moto motocicleta nave naves caballo caballos montura monturas
buggy jetpack barco barcos exoesqueleto interceptor aeronave embarcacion carro carreta dron drones
batmovil vehicle vehicles car cars bike bikes ship ships horse horses mount mounts boat boats exoskeleton
aircraft vessel vessels drone steed wagon'''.split())
W_DEF = set('''armadura armaduras escudo escudos blindaje blindajes absorbe absorcion proteccion protector
casco yelmo cota placas chaleco cobertura barrera coraza armour armor shield shields plating soak soaks
protection helm mail plate plates vest cover barrier kevlar'''.split())
W_ART = set('''poder poderes artefacto artefactos magia magico magica tecnica tecnicas mutacion mutaciones
ocultismo mistico misticos mistica disciplina disciplinas hechizo hechizos ritual rituales reliquia amuleto
talisman power powers artefact artefacts artifact artifacts magic magical technique techniques mutation
mutations occult mystic discipline disciplines spell spells relic charm'''.split())

W_ARMA = set('''ballesta espada pistola rifle dinamita bomba granada cuchillo daga hacha lanza arco
escopeta revolver fusil canon katana sable latigo martillo maza garrote bate navaja estoque subfusil
mandoble cimitarra jabalina honda mosquete trabuco crossbow sword pistol gun knife dagger axe spear bow
shotgun rifle hammer mace club bat blade musket grenade bomb dynamite'''.split())

ACC = {u'á': 'a', u'é': 'e', u'í': 'i', u'ó': 'o', u'ú': 'u', u'ü': 'u', u'ñ': 'n'}


def words(txt):
    t = txt.lower()
    t = ''.join(ACC.get(c, c) for c in t)
    return set(re.findall(r'[a-z0-9]+', t))


def classify(block_name, it):
    name = words(it['n'][0] + ' ' + it['n'][1])
    blob = name | words(it['x'][0] + ' ' + it['m'][0])
    blk = words(block_name)
    if it['d'][0] not in (u'—', '-', ''):
        return 'vehiculo' if (name & W_VEH and not (name & W_ARMA)) else 'arma'
    if name & W_VEH:
        return 'vehiculo'
    if blob & W_DEF:
        return 'defensa'
    if blk & W_ART or blob & W_ART:
        return 'artefacto'
    if 'Llave' in it['m'][0] or 'Rejilla' in it['m'][0]:
        return 'artefacto'
    return 'util'


rows = {c: [] for c in CAT}
for b in D['bazar']:
    for bl in b['blocks']:
        for it in bl['items']:
            c = classify(bl['n'][0], it)
            both = it['m'][0] + ' ' + it['m'][1]
            acc = re.search(r'(?:Acceso|Access) (\d)', both)
            key = re.search(r'(\d+) (?:Llaves|Keys)', both)
            pts = re.search(r'(\d+) (?:puntos?|points?)', both)
            rows[c].append({'n': it['n'], 'w': b['n'],
                            'acc': int(acc.group(1)) if acc else None,
                            'k': int(key.group(1)) if key else 0,
                            'p': int(pts.group(1)) if pts else 0,
                            'd': it['d'], 'e': it['e']})
for c in CAT:
    rows[c].sort(key=lambda r: (r['acc'] if r['acc'] is not None else 9, -r['k'], r['n'][0]))


def build(es):
    L = 0 if es else 1
    h = ['<h3 id="bz-indice">%s</h3>\n' % (u'Índice del Bazar por categorías' if es else 'Bazaar index by category')]
    h.append('<p>%s</p>\n' % (
        u'El catálogo está ordenado por mundos, porque así es como se lee el tono. Esta es la otra puerta: los mismos objetos ordenados por <strong>qué son</strong> y por <strong>cuánto cuestan</strong>, para cuando lo que buscas es un arma de Acceso 1 y te da igual de qué ambientación salga. La categoría es una ayuda de lectura y no una regla: un exoesqueleto es vehículo y defensa a la vez, y está donde más se usa.'
        if es else
        'The catalogue is ordered by world, because that is how tone reads. This is the other door: the same objects ordered by <strong>what they are</strong> and <strong>what they cost</strong>, for when what you want is an Access 1 weapon and you do not care which setting it came from. The category is a reading aid and not a rule: an exoskeleton is both vehicle and defence, and it sits where it gets used.'))
    for c in CAT:
        rs = rows[c]
        h.append('<h4>%s <span class="small">(%d)</span></h4>\n' % (NAMES[c][L], len(rs)))
        h.append('<div class="tw"><table class="t idx">\n<thead><tr><th>%s</th><th>%s</th><th>%s</th><th class="num">%s</th></tr></thead>\n<tbody>\n'
                 % ((u'Objeto', u'De dónde', u'Qué hace', 'Precio') if es else ('Item', 'From', 'What it does', 'Price')))
        for r in rs:
            what = [x for x in (r['d'][L], r['e'][L]) if x not in (u'—', '-', '')]
            price = []
            if r['acc'] is not None:
                price.append((u'Acceso ' if es else 'Access ') + str(r['acc']))
            if r['p']:
                price.append('%d %s' % (r['p'], (u'puntos' if r['p'] > 1 else u'punto') if es else ('points' if r['p'] > 1 else 'point')))
            if r['k']:
                price.append('%d %s' % (r['k'], u'Llaves' if es else 'Keys'))
            h.append('<tr><td>%s</td><td class="small">%s</td><td class="small">%s</td><td class="num small">%s</td></tr>\n'
                     % (r['n'][L], r['w'][L], u' · '.join(what) or u'—', u' · '.join(price) or u'—'))
        h.append('</tbody></table></div>\n')
    return ''.join(h)


def put(f, txt):
    s = io.open(f, encoding='utf-8').read()
    k = s.rindex('</section>')
    io.open(f, 'w', encoding='utf-8').write(s[:k] + txt + s[k:])
    print(' ', f, 'ok')


put('frag_bazar.html', build(True))
put('frag_bazar_b.en.html', build(False))
print({c: len(rows[c]) for c in CAT}, 'total', sum(len(rows[c]) for c in CAT))
