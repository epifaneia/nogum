import re, json, os, html as H
D = os.path.dirname(os.path.abspath(__file__))
def R(n): return open(os.path.join(D, n), encoding='utf-8').read()
# las banderas y las notas de procedencia no forman parte del nombre de nada
FUERA = re.compile(r'<span class="(?:flag[^"]*|src)">.*?</span>', re.S)
def txt(s): return H.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', FUERA.sub(' ', s)))).strip()

def bazar(src):
    out = []
    for m in re.finditer(r'<h3 id="(bz-[^"]+)"[^>]*>(.*?)</h3>(.*?)(?=<h3 id="bz-|\Z)', src, re.S):
        sid, title, body = m.group(1), m.group(2), m.group(3)
        if sid in ('bz-lectura', 'bz-resumen', 'bz-fabrica', 'bz-indice'): continue
        title = txt(re.sub(r'<span class="flag[^"]*">.*?</span>', '', title))
        blocks = []
        parts = re.split(r'<h4[^>]*>(.*?)</h4>', body)
        if len(parts) == 1: parts = ['', title, body]
        for k in range(1, len(parts), 2):
            bname, bbody = txt(parts[k]), parts[k + 1]
            items = []
            for tb in re.findall(r'<tbody>(.*?)</tbody>', bbody, re.S):
                for tr in re.findall(r'<tr>(.*?)</tr>', tb, re.S):
                    cells = [txt(c) for c in re.findall(r'<td[^>]*>(.*?)</td>', tr, re.S)]
                    if len(cells) >= 6:
                        items.append(cells[:6])
            if items: blocks.append({'name': bname, 'items': items})
        out.append({'id': sid[3:], 'name': title, 'blocks': blocks})
    return out

es = bazar(R('frag_bazar.html'))
a = R('frag_bazar_a.en.html'); b = R('frag_bazar_b.en.html')
en = bazar(a + b)
assert [x['id'] for x in es] == [x['id'] for x in en], ([x['id'] for x in es], [x['id'] for x in en])
# --- categoria de cada objeto (misma logica que el indice del manual)
W_VEH = set(u"""vehiculo vehiculos coche coches moto motocicleta nave naves caballo caballos montura monturas
buggy jetpack barco barcos exoesqueleto interceptor aeronave embarcacion carro carreta dron drones batmovil
vehicle vehicles car cars bike bikes ship ships horse horses mount mounts boat boats exoskeleton aircraft
vessel vessels drone steed wagon""".split())
W_ARMA = set(u"""ballesta espada pistola rifle dinamita bomba granada cuchillo daga hacha lanza arco escopeta
revolver fusil canon katana sable latigo martillo maza garrote bate navaja estoque subfusil mandoble cimitarra
jabalina honda mosquete trabuco crossbow sword pistol gun knife dagger axe spear bow shotgun hammer mace club
bat blade musket grenade bomb dynamite""".split())
W_DEF = set(u"""armadura armaduras escudo escudos blindaje blindajes absorbe absorcion proteccion protector
casco yelmo cota placas chaleco cobertura barrera coraza armour armor shield shields plating soak soaks
protection helm mail plate plates vest cover barrier kevlar""".split())
W_ART = set(u"""poder poderes artefacto artefactos magia magico magica tecnica tecnicas mutacion mutaciones
ocultismo mistico misticos mistica disciplina disciplinas hechizo hechizos ritual rituales reliquia amuleto
talisman power powers artefact artefacts artifact artifacts magic magical technique techniques mutation
mutations occult mystic discipline disciplines spell spells relic charm""".split())
ACCENTS = {u'á': 'a', u'é': 'e', u'í': 'i', u'ó': 'o', u'ú': 'u', u'ü': 'u', u'ñ': 'n'}


def _w(t):
    t = ''.join(ACCENTS.get(c, c) for c in t.lower())
    return set(re.findall(r'[a-z0-9]+', t))


def categoria(block_name, it):
    name = _w(it['n'][0] + ' ' + it['n'][1])
    blob = name | _w(it['x'][0] + ' ' + it['m'][0])
    if it['d'][0] not in (u'—', '-', ''):
        return 'vehiculo' if (name & W_VEH and not (name & W_ARMA)) else 'arma'
    if name & W_VEH:
        return 'vehiculo'
    if blob & W_DEF:
        return 'defensa'
    if _w(block_name) & W_ART or blob & W_ART:
        return 'artefacto'
    if 'Llave' in it['m'][0] or 'Rejilla' in it['m'][0]:
        return 'artefacto'
    return 'util'


BZ = []
for x, y in zip(es, en):
    assert len(x['blocks']) == len(y['blocks']), x['id']
    blocks = []
    for bx, by in zip(x['blocks'], y['blocks']):
        assert len(bx['items']) == len(by['items']), (x['id'], bx['name'])
        items = [{'n': [ix[0], iy[0]], 'd': [ix[1], iy[1]], 'e': [ix[2], iy[2]], 'a': [ix[3], iy[3]], 'm': [ix[4], iy[4]], 'x': [ix[5], iy[5]]}
                 for ix, iy in zip(bx['items'], by['items'])]
        for jt in items:
            jt['c'] = categoria(bx['name'], jt)
        blocks.append({'n': [bx['name'], by['name']], 'items': items})
    BZ.append({'id': x['id'], 'n': [x['name'], y['name']], 'blocks': blocks})


c8 = R('frag_cap8.html'); c8e = R('frag_cap8.en.html')
def baul(s):
    ini = s.index('id="ch8-baul"')
    fin = s.index('id="ch8-tablas"') if 'id="ch8-tablas"' in s else s.index('id="ch8-skills"')
    return [txt(h) for h in re.findall(r'<h4[^>]*>(.*?)</h4>', s[ini:fin])]
def recipes(s):
    """Una receta es la que lleva numero. Las fichas de critica no llevan, asi
    que ya no pueden desplazar la lista si alguien las mueve de sitio."""
    out = []
    for t in re.findall(r'<p class="recipe-title">(.*?)</p>', s):
        x = txt(t)
        if re.match(r'\s*\d+\.', x):
            out.append(x)
    return out

def techos(s):
    """Los techos de Rejilla de cada receta, leidos de su ficha impresa (8.4).
    Antes habia una tabla copiada a mano dentro de la app, y se quedo atras al
    expulsar la receta 15: seis recetas llevaban los techos de la de al lado."""
    out = {}
    for m in re.finditer(r'<p class="recipe-title">(.*?)</p>(.*?)<p class="recipe-grid">(.*?)</p>', s, re.S):
        n = re.match(r'\s*(\d+)\.', txt(m.group(1)))
        g = re.search(r'<strong>\s*([0-9—]+(?:\s*·\s*[0-9—]+){4})\s*</strong>', m.group(3))
        if n and g:
            out[int(n.group(1)) - 1] = [0 if x.strip() == '—' else int(x.strip())
                                        for x in g.group(1).split('·')]
    assert sorted(out) == list(range(len(out))), 'faltan techos de alguna receta: %s' % sorted(out)
    return [out[i] for i in range(len(out))]

BAUL = [list(p) for p in zip(baul(c8), baul(c8e))]
REC = [list(p) for p in zip(recipes(c8), recipes(c8e))]
TEC = techos(c8)
assert len(REC) == len(TEC), 'hay %d recetas y %d juegos de techos' % (len(REC), len(TEC))
prev = json.load(open(os.path.join(D, 'app_data.json'), encoding='utf-8'))
data = dict(prev)
data.update({'bazar': BZ, 'baul': BAUL, 'recipes': REC, 'techos': TEC})
# --- vocabulario retirado -------------------------------------------------
# baulLong y otras claves NO se regeneran: se arrastran de la version anterior
# (data = dict(prev)). Por eso pueden quedarse con texto que el manual ya ha
# cambiado, como paso con los nombres viejos de la vida fractal. Esto lo caza.
MUERTOS = [('Cáscara', 'Letal'), ('El Núcleo', 'Guerra'), ('La Carne', 'Táctico'),
           ('The Shell', 'Lethal'), ('The Core', 'War'),
           ('Bola de nieve', 'Comedia negra'), ('Regla del Margen', 'retirada')]
def _hojas(o, ruta=''):
    if isinstance(o, str):
        yield ruta, o
    elif isinstance(o, dict):
        for k, v in o.items():
            yield from _hojas(v, ruta + '.' + str(k))
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from _hojas(v, ruta + '[%d]' % i)
_sucio = [(r, viejo, nuevo) for r, t in _hojas(data) for viejo, nuevo in MUERTOS if viejo in t]
if _sucio:
    for r, viejo, nuevo in _sucio[:12]:
        print('  VOCABULARIO RETIRADO en %s: "%s" deberia ser "%s"' % (r, viejo, nuevo))
    raise SystemExit('app_data.json arrastra %d texto(s) con vocabulario retirado' % len(_sucio))

json.dump(data, open(os.path.join(D, 'app_data.json'), 'w', encoding='utf-8'), ensure_ascii=False)
print("recetas", len(REC), "techos", len(TEC))
print("bazar", [(b["id"], sum(len(k['items']) for k in b['blocks'])) for b in BZ])
print('baul', len(BAUL), 'recipes', len(REC))
