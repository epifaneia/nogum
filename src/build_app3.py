import json, os, re
D = os.path.dirname(os.path.abspath(__file__))
R = lambda n: open(os.path.join(D, n), encoding='utf-8').read()
css = R('paper.css'); tokens = css[:css.index('*{box-sizing')]
a2 = R('app2_body.html'); base = a2[a2.index('<style>') + 7:a2.index('</style>')].replace('%%TOKENS%%', tokens)
def js(o): return json.dumps(o, ensure_ascii=False).replace('</', '<' + chr(92) + '/')

# --- que la app y el manual no se separen otra vez -------------------------
# Al expulsar la receta 15 se quedaron atras la tabla de techos y los veinte
# mundos del atajo: seis mundos ensenaban la receta de al lado. Esto lo caza.
src = R('app4_body.html')
dat = json.load(open(os.path.join(D, 'app_data.json'), encoding='utf-8'))
_rs = [int(x) for x in re.findall(r"\{r:(\d+), n:\[", src)]
_n = len(dat['recipes'])
assert len(dat.get('techos', [])) == _n, 'hay %d recetas y %d juegos de techos' % (_n, len(dat.get('techos', [])))
assert len(dat['baul']) == 16, 'el Baul tiene %d reglas y el Codigo usa 16 bits' % len(dat['baul'])
assert sorted(_rs) == list(range(_n)), (
    'los %d mundos del atajo no apuntan a las %d recetas una vez cada uno: %s' % (len(_rs), _n, sorted(_rs)))

# Las otras tres piezas. La app se publica en dos sitios y cada uno necesita
# una URL distinta: relativa en la carpeta local, de artefacto en claude.ai.
URLS = json.load(open(os.path.join(D, 'urls.json'), encoding='utf-8'))
# tres destinos: la carpeta local, los artefactos y el sitio publico
PIEZAS = [('tesis', 'La Apuesta', 'The Wager', '../NOGUM_productos/NOGUM_tesis.html', 'apuesta.html'),
          ('juego', 'Juego', 'Game', '../NOGUM_productos/NOGUM_juego.html', 'juego.html'),
          ('acelerado', 'Acelerado', 'Accelerated', '../NOGUM_productos/NOGUM_acelerado.html', 'acelerado.html'),
          ('app', 'App', 'App', None, None)]
def prods(modo):
    def url(k, loc, web):
        if k == 'app': return None
        return {'local': loc, 'web': web}.get(modo, URLS[k])
    return js([{'es': e, 'en': n, 'url': url(k, loc, web)} for k, e, n, loc, web in PIEZAS])

DATA = js(dict(dat, firmas=json.load(open(os.path.join(D, 'firmas.json'), encoding='utf-8'))))
CANON = js(R('CANON.md'))
MARCAS = ('%' + '%BASECSS%' + '%', '%' + '%PRODS%' + '%')
BLOBS = ('%' + '%DATA%' + '%', '%' + '%CANON%' + '%')


def armar(modo):
    """Primero los marcadores de plantilla, DESPUES los blobs.

    El orden no es cosmetico. Los blobs inyectan texto libre, y ese texto puede
    contener algo que parezca un marcador: la bitacora los menciona por su
    nombre al documentarlos. Si los blobs van primero, la sustitucion siguiente
    pisa tambien la aparicion de dentro del blob, mete comillas sin escapar en
    una cadena JSON y revienta la app entera. Paso por eso una vez.
    """
    p = src.replace(MARCAS[0], base).replace(MARCAS[1], prods(modo))
    for m in MARCAS:
        assert m not in p, 'queda %s sin resolver' % m
    return p.replace(BLOBS[0], DATA).replace(BLOBS[1], CANON)


def comprueba(p, donde):
    """Que el canon embebido siga siendo JSON valido y el script, entero."""
    a = p.index('id="canon">') + len('id="canon">')
    b = p.index('</script>', a)
    try:
        json.loads(p[a:b])
    except Exception as e:
        raise SystemExit('%s: el canon embebido ya no es JSON valido (%s)' % (donde, e))
    assert 'var PRODS = [' in p, '%s: PRODS no se ha montado' % donde


art = armar('artifact'); comprueba(art, 'artefacto')
open(os.path.join(D, 'out3', 'nogum_app.html'), 'w', encoding='utf-8').write(art)

def envuelve(p):
    """La app sale sin esqueleto porque el artefacto se lo pone. Para el sitio
    y para la carpeta local hay que ponerselo nosotros."""
    i = p.index('</style>') + 8
    return ('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            + p[:i] + '\n</head>\n<body>\n' + p[i:] + '</body>\n</html>\n')


web = armar('web'); comprueba(web, 'web')
DOCS = os.path.join(D, '..', 'docs'); os.makedirs(DOCS, exist_ok=True)
open(os.path.join(DOCS, 'app.html'), 'w', encoding='utf-8').write(envuelve(web))

page = armar('local'); comprueba(page, 'local')
full = envuelve(page)
# relativo al repositorio: quien clone esto tiene que poder compilarlo
LOCAL_APP = os.path.join(D, '..', 'NOGUM_app', 'NOGUM_app.html')
os.makedirs(os.path.dirname(LOCAL_APP), exist_ok=True)
open(LOCAL_APP, 'w', encoding='utf-8').write(full)
print('KB', len(art.encode()) // 1024)
