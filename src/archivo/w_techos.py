# -*- coding: utf-8 -*-
"""Los techos salen del manual, y los veinte mundos vuelven a apuntar a su receta."""
import io, os, re, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
fal = []


def sub(fichero, a, b, n=1):
    s = io.open(fichero, encoding='utf-8').read()
    if s.count(a) != n:
        fal.append('%s (%d!=%d) %s' % (fichero, s.count(a), n, a[:64])); return
    io.open(fichero, 'w', encoding='utf-8').write(s.replace(a, b, n))


# ------------------------------- 1. el extractor saca los techos del capitulo 8
sub('extract_app_data.py',
    "BZ.append({'id': x['id'], 'n': [x['name'], y['name']], 'blocks': blocks})",
    "BZ.append({'id': x['id'], 'n': [x['name'], y['name']], 'blocks': blocks})")
s = io.open('extract_app_data.py', encoding='utf-8').read()
if 'def techos(' not in s:
    i = s.index("def baul(s):")
    TECH = '''def techos(s):
    """Los techos de Rejilla de cada receta, leidos de la ficha impresa.
    Asi no hay una tabla a mano que se quede atras cuando se renumeran."""
    out = {}
    for m in re.finditer(r'<p class="recipe-title">(.*?)</p>(.*?)<p class="recipe-grid">(.*?)</p>', s, re.S):
        tit = txt(m.group(1))
        g = re.search(r'<strong>\\s*([0-9\\u2014]+(?:\\s*\\u00b7\\s*[0-9\\u2014]+){4})\\s*</strong>', m.group(3))
        n = re.match(r'\\s*(\\d+)\\.', tit)
        if not (g and n):
            continue
        out[int(n.group(1)) - 1] = [0 if x.strip() == '\\u2014' else int(x.strip())
                                    for x in g.group(1).split('\\u00b7')]
    return [out[i] for i in range(len(out))] if sorted(out) == list(range(len(out))) else []


'''
    s = s[:i] + TECH + s[i:]
    io.open('extract_app_data.py', 'w', encoding='utf-8').write(s)
    print('extract_app_data.py: funcion techos() anadida')

s = io.open('extract_app_data.py', encoding='utf-8').read()
if "'techos'" not in s:
    s = s.replace("data.update({'bazar': BZ, 'baul': BAUL, 'recipes': REC})",
                  "data.update({'bazar': BZ, 'baul': BAUL, 'recipes': REC, 'techos': techos(c8)})")
    print('extract_app_data.py: techos al json')
# una receta es la que lleva numero: asi una ficha de critica no desplaza nada
s = s.replace("def recipes(s): return [txt(t) for t in re.findall(r'<p class=\"recipe-title\">(.*?)</p>', s)][:20]",
              "def recipes(s):
"
              "    out = []
"
              "    for t in re.findall(r'<p class=\"recipe-title\">(.*?)</p>', s):
"
              "        x = txt(t)
"
              "        if re.match(r'\s*\d+\.', x):
"
              "            out.append(x)
"
              "    return out")
io.open('extract_app_data.py', 'w', encoding='utf-8').write(s)

# -------------------------------------- 2. la app deja de llevar la tabla a mano
s = io.open('app4_body.html', encoding='utf-8').read()
i = s.index('/* techos de Rejilla por receta (8.4): fis, men, soc, tec, arc; 0 = no existe */')
j = s.index('function arcOpen(){')
NUEVO = """/* Los techos de Rejilla (8.4) vienen de los datos, leidos de las fichas impresas
   del capitulo 8. Antes habia aqui una tabla a mano y se quedo atras cuando se
   expulso la receta 15: seis recetas tenian los techos de la de al lado. */
function techoReceta(r){ var t = DATA.techos && DATA.techos[r]; return (t && t.length === 5) ? t : null; }
"""
s = s[:i] + NUEVO + s[j:]
s = s.replace("if (M.known && M.world !== null) { var tc = TECHO[KNOWN[M.world].r]; return tc ? tc[4] > 0 : true; }",
              "if (M.known && M.world !== null) { var tc = techoReceta(KNOWN[M.world].r); return tc ? tc[4] > 0 : true; }")
s = s.replace("if (M.known && M.world !== null) { var tc = TECHO[KNOWN[M.world].r]; if (tc) return tc; }",
              "if (M.known && M.world !== null) { var tc = techoReceta(KNOWN[M.world].r); if (tc) return tc; }")
io.open('app4_body.html', 'w', encoding='utf-8').write(s)
if 'TECHO[' in s:
    fal.append('todavia queda alguna lectura de TECHO[')
print('app4_body.html: los techos vienen de los datos')

# ------------------------------- 3. los veinte mundos, cada uno con su receta
s = io.open('app4_body.html', encoding='utf-8').read()
# fuera el mundo huerfano: su receta era la 15 expulsada por repetir la 14
VIEJO = ("  {r:14, n:['Instituto de día, caza de monstruos de noche','High school by day, monster hunting by night'], "
         "h:['Drama juvenil con estacas','Teen drama with stakes'], p:['alto','medio','carne',1,true,['gotico','terror'],[]]},\n")
if s.count(VIEJO) != 1:
    fal.append('no encuentro el mundo huerfano del instituto')
else:
    s = s.replace(VIEJO, '')

# los seis que quedaron desplazados bajan uno
for viejo, nuevo in ((15, 14), (16, 15), (17, 16), (18, 17), (19, 18)):
    a = '  {r:%d, n:[' % viejo
    if s.count(a) != 1:
        fal.append('r=%d aparece %d veces' % (viejo, s.count(a))); continue
    s = s.replace(a, '  {r:%d, n:[' % nuevo, 1)

# y entra el mundo que faltaba: la receta 20 no tenia ninguno
ULTIMO = ("  {r:18, n:['Una distopía de risa con un ordenador loco','A hilarious dystopia run by a mad computer'], "
          "h:['Todos son traidores, tú también','Everyone is a traitor, you too'], "
          "p:['neutro','alto','cascara',1,false,['neon','toon'],[7,8],'locura']}\n")
NUEVO_MUNDO = (ULTIMO.rstrip('\n') + ',\n'
               "  {r:19, n:['Un mundo plano a lomos de una tortuga gigante','A flat world on the back of a giant turtle'], "
               "h:['Sátira fantástica y burocrática','Fantasy satire and bureaucracy'], "
               "p:['neutro','alto','carne',1,true,['fantasia','social'],[]]}\n")
if s.count(ULTIMO) != 1:
    fal.append('no encuentro el ultimo mundo de KNOWN')
else:
    s = s.replace(ULTIMO, NUEVO_MUNDO, 1)

# las familias: «mundo actual» pierde uno y «los raros» gana a los quelonios
sub_fam = ("  {id:'mo', n:['Mundo actual y misterio','Present day and mystery'], s:['Horror, vampiros, niños valientes y ladrones','Horror, vampires, brave kids and thieves'], k:[11,12,13,14,15]},\n"
           "  {id:'ra', n:['Los raros y maravillosos','The weird and wonderful'], s:['Superhéroes, anime, mechas y distopía','Superheroes, anime, mechas and dystopia'], k:[16,17,18,19]}")
nueva_fam = ("  {id:'mo', n:['Mundo actual y misterio','Present day and mystery'], s:['Horror, vampiros, niños valientes y ladrones','Horror, vampires, brave kids and thieves'], k:[11,12,13,14]},\n"
             "  {id:'ra', n:['Los raros y maravillosos','The weird and wonderful'], s:['Superhéroes, anime, mechas, distopía y sátira','Superheroes, anime, mechas, dystopia and satire'], k:[15,16,17,18,19]}")
if s.count(sub_fam) != 1:
    fal.append('no encuentro las familias mo y ra')
else:
    s = s.replace(sub_fam, nueva_fam, 1)

io.open('app4_body.html', 'w', encoding='utf-8').write(s)

if fal:
    print('FALLOS:')
    for x in fal:
        print('  ' + x)
    sys.exit(1)
print('los veinte mundos apuntan a sus veinte recetas')
