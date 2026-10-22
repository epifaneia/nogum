import re, json, os, html as H
D = os.path.dirname(os.path.abspath(__file__))
V2 = os.path.join(D, 'v2')
def R(n): return open(os.path.join(D, n), encoding='utf-8').read()
def R2(n): return open(os.path.join(V2, n), encoding='utf-8').read()
# las banderas y las notas de procedencia no forman parte del nombre de nada
FUERA = re.compile(r'<span class="(?:flag[^"]*|src)">.*?</span>', re.S)
def txt(s): return H.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', FUERA.sub(' ', s)))).strip()

# --- el Bazar (9.3 del Juego completo v2) -----------------------------------
# Las tablas del catalogo tienen 8 columnas desde la v2:
#   Objeto · Daño · Esq · Abs · Acceso · Puntos · Llaves · Notas
# (antes 6, con «Acceso / Rejilla» en una sola). Lo que no es catalogo se salta:
# la lectura de la ficha (con su recuadro bz-precios), el taller (con sus casos
# resueltos, bz-casos), el resumen y el indice.
NO_CATALOGO = ('bz-lectura', 'bz-fabrica', 'bz-resumen', 'bz-indice', 'bz-precios', 'bz-casos')
NCOL = 8
def bazar(src):
    out = []
    for m in re.finditer(r'<h3 id="(bz-[^"]+)"[^>]*>(.*?)</h3>(.*?)(?=<h3 id="bz-|\Z)', src, re.S):
        sid, title, body = m.group(1), m.group(2), m.group(3)
        if sid in NO_CATALOGO: continue
        title = txt(title)
        blocks = []
        parts = re.split(r'<h4([^>]*)>(.*?)</h4>', body)
        # sin h4: un solo bloque con el nombre de la seccion
        if len(parts) == 1: parts = ['', '', title, body]
        for k in range(1, len(parts), 3):
            attrs, bname, bbody = parts[k], txt(parts[k + 1]), parts[k + 2]
            hid = re.search(r'id="([^"]+)"', attrs)
            if hid and hid.group(1) in NO_CATALOGO: continue
            items = []
            for tb in re.findall(r'<tbody>(.*?)</tbody>', bbody, re.S):
                for tr in re.findall(r'<tr>(.*?)</tr>', tb, re.S):
                    cells = re.findall(r'<td[^>]*>(.*?)</td>', tr, re.S)
                    assert len(cells) == NCOL, (sid, bname, len(cells), txt(tr)[:80])
                    items.append([txt(c) for c in cells] + [cells[7]])
            if items: blocks.append({'name': bname, 'items': items})
        out.append({'id': sid[3:], 'name': title, 'blocks': blocks})
    return out

es = bazar(R2('fK1_bazar_a.html') + R2('fK2_bazar_b.html') + R2('fK3_bazar_c.html'))
en = bazar(R2('fK1_bazar_a.en.html') + R2('fK2_bazar_b.en.html') + R2('fK3_bazar_c.en.html'))
assert [x['id'] for x in es] == [x['id'] for x in en], ([x['id'] for x in es], [x['id'] for x in en])
# --- categoria de cada objeto (misma logica que el indice del manual)
W_VEH = set(u"""vehiculo vehiculos coche coches moto motocicleta nave naves caballo caballos montura monturas
buggy jetpack barco barcos exoesqueleto interceptor aeronave embarcacion carro carreta dron drones batmovil
camion servoarmadura mecha
vehicle vehicles car cars bike bikes ship ships horse horses mount mounts boat boats exoskeleton aircraft
vessel vessels drone steed wagon truck""".split())
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


def nota_corta(raw):
    """La nota sin «La cuenta:», que explica el precio y nombra de paso
    armaduras, escudos y Llaves que el objeto no tiene: con ella dentro, la
    mitad del catalogo caia en «Defensas»."""
    return txt(re.split(r'<em>\s*(?:La cuenta|The tally)\s*:?\s*</em>', raw)[0])


def num(s):
    m = re.match(r'\s*(\d+)', s or '')
    return int(m.group(1)) if m else 0


def categoria(block_name, it, nota):
    name = _w(it['n'][0] + ' ' + it['n'][1])
    blob = name | _w(nota)
    if it['d'][0] not in (u'—', '-', ''):
        return 'vehiculo' if (name & W_VEH and not (name & W_ARMA)) else 'arma'
    if name & W_VEH:
        return 'vehiculo'
    if blob & W_DEF:
        return 'defensa'
    if _w(block_name) & W_ART or blob & W_ART:
        return 'artefacto'
    if num(it['k'][0]) > 0 or 'Rejilla' in nota:
        return 'artefacto'
    return 'util'


BZ = []
for x, y in zip(es, en):
    assert len(x['blocks']) == len(y['blocks']), x['id']
    blocks = []
    for bx, by in zip(x['blocks'], y['blocks']):
        assert len(bx['items']) == len(by['items']), (x['id'], bx['name'])
        items = []
        for ix, iy in zip(bx['items'], by['items']):
            # las tres columnas de coste son numeros: tienen que coincidir en los dos idiomas
            assert [num(ix[c]) for c in (4, 5, 6)] == [num(iy[c]) for c in (4, 5, 6)], (x['id'], ix[0], iy[0])
            jt = {'n': [ix[0], iy[0]], 'd': [ix[1], iy[1]], 'e': [ix[2], iy[2]], 'a': [ix[3], iy[3]],
                  'm': [ix[4], iy[4]], 'p': [ix[5], iy[5]], 'k': [ix[6], iy[6]], 'x': [ix[7], iy[7]]}
            jt['c'] = categoria(bx['name'], jt, nota_corta(ix[8]))
            items.append(jt)
        blocks.append({'n': [bx['name'], by['name']], 'items': items})
    BZ.append({'id': x['id'], 'n': [x['name'], y['name']], 'blocks': blocks})


# --- el Baul (9.1) ------------------------------------------------------------
# El Codigo de la mesa guarda las reglas del Baul por su numero de bit, y los
# Codigos viejos tienen 16. Por eso la lista NO sigue el orden del manual: van
# primero las dieciseis de siempre, en su orden de siempre, y detras las nuevas
# (la escalera llana es la 17, bit 16). Un Codigo viejo se lee igual.
BAUL_BITS = [  # nombre en el manual v2 (castellano), por bit
    'Relojes de progreso', 'Flashbacks', 'Pacto del diablo', 'Daño explosivo',
    'Rejilla mística inversa', 'Destino (Wyrd)', 'Fundas (el cuerpo como equipo)', 'Clones',
    'El Director tira en oculto', 'Tablas de dados', 'Transformación', 'Sincronización',
    'Daño ambiental', 'Barras propias (Honor, Reputación y otras)', 'Vínculos', 'Menú de los 4 costes',
    'La escalera llana']
def baul_modulos(s):
    ini = s.index('id="ch9-baul"')
    fin = s.index('id="ch9-tablas"')
    trozo = s[ini:fin]
    out = []
    for m in re.finditer(r'<h4[^>]*>(.*?)</h4>(.*?)(?=<h4|\Z)', trozo, re.S):
        cuerpo = re.sub(r'<aside class="meta">.*?</aside>', ' ', m.group(2), flags=re.S)
        cuerpo = re.sub(r'<table.*?</table>', ' ', cuerpo, flags=re.S)
        out.append((txt(m.group(1)), txt(cuerpo)))
    return out
b_es, b_en = baul_modulos(R2('fJ1_cap9a.html')), baul_modulos(R2('fJ1_cap9a.en.html'))
assert len(b_es) == len(b_en) == len(BAUL_BITS), (len(b_es), len(b_en))
nombres = [n for n, _ in b_es]
assert sorted(nombres) == sorted(BAUL_BITS), set(nombres) ^ set(BAUL_BITS)
orden = [nombres.index(n) for n in BAUL_BITS]   # posicion en el manual de cada bit
BAUL = [[b_es[i][0], b_en[i][0]] for i in orden]
BAUL_LONG = [[b_es[i][1], b_en[i][1]] for i in orden]

c9 = R2('fJ2_cap9b.html'); c9e = R2('fJ2_cap9b.en.html')
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
    """El nivel maximo de los jugadores de cada receta (3.7), leido de su ficha
    impresa (9.4). Antes habia una tabla copiada a mano dentro de la app, y se
    quedo atras al expulsar la receta 15: seis recetas llevaban los techos de
    la de al lado."""
    out = {}
    for m in re.finditer(r'<p class="recipe-title">(.*?)</p>(.*?)<p class="recipe-grid">(.*?)</p>', s, re.S):
        n = re.match(r'\s*(\d+)\.', txt(m.group(1)))
        g = re.search(r'<strong>\s*([0-9—]+(?:\s*·\s*[0-9—]+){4})\s*</strong>', m.group(3))
        if n and g:
            out[int(n.group(1)) - 1] = [0 if x.strip() == '—' else int(x.strip())
                                        for x in g.group(1).split('·')]
    assert sorted(out) == list(range(len(out))), 'faltan techos de alguna receta: %s' % sorted(out)
    return [out[i] for i in range(len(out))]

REC = [list(p) for p in zip(recipes(c9), recipes(c9e))]
TEC = techos(c9)
assert len(recipes(c9)) == len(recipes(c9e)) == 20, (len(recipes(c9)), len(recipes(c9e)))
assert len(REC) == len(TEC), 'hay %d recetas y %d juegos de techos' % (len(REC), len(TEC))
assert TEC == techos(c9e), 'los techos de las recetas no coinciden entre el castellano y el ingles'
prev = json.load(open(os.path.join(D, 'app_data.json'), encoding='utf-8'))
data = dict(prev)
data.update({'bazar': BZ, 'baul': BAUL, 'baulLong': BAUL_LONG, 'recipes': REC, 'techos': TEC})
data.pop('baulManual', None)
# --- vocabulario retirado -------------------------------------------------
# Ya no se arrastra nada del manual viejo (baulLong se regenera desde la v2),
# pero si alguien vuelve a meter una clave a mano, esto lo caza.
MUERTOS = [('Cáscara', 'Letal'), ('El Núcleo', 'Guerra'), ('La Carne', 'Táctico'),
           ('The Shell', 'Lethal'), ('The Core', 'War'),
           ('Bola de nieve', 'Comedia negra'), ('Regla del Margen', 'retirada'),
           ('Llave ancha', 'retirada (la Llave es tan grande como diga la escena)'),
           ('Wide Key', 'retirada'), ('Llave estrecha', 'Llave (toda una Disciplina)'),
           ('El DJ', 'el Director'), (' DJ ', 'Director'), ('Malla Tonal', 'Cuadrante'),
           ('2·x²', 'retirada'), ('como mucho', 'sin absolutos')]
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
