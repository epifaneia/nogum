# -*- coding: utf-8 -*-
"""Revision 1: que los numeros de la app y los del manual digan lo mismo."""
import io, os, re, json, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
PROB = []


def p(sev, txt):
    PROB.append((sev, txt))
    print('%-5s %s' % (sev, txt))


cap8 = io.open('frag_cap8.html', encoding='utf-8').read()
app = io.open('app4_body.html', encoding='utf-8').read()
data = json.load(io.open('app_data.json', encoding='utf-8'))

# ---------------------------------------------- 1. techos de Rejilla por receta
print('=' * 70)
print(' 1. Techos de Rejilla: la app (TECHO) contra lo impreso en el 8.4')
print('=' * 70)
# lo impreso: cada ficha de receta lleva "Techos de Rejilla ... : <b>a · b · c · d · e</b>"
manual = {}
for m in re.finditer(r'<p class="recipe-title">(.*?)</p>(.*?)<p class="recipe-grid">(.*?)</p>', cap8, re.S):
    tit = re.sub(r'<[^>]+>', '', m.group(1)).strip()
    g = m.group(3)
    nums = re.search(r'<strong>\s*([0-9—\u2014]+(?:\s*·\s*[0-9—\u2014]+){4})\s*</strong>', g)
    if not nums:
        p('AVISO', 'receta sin techos legibles: %s' % tit[:50]); continue
    vals = [0 if x.strip() in ('—', '\u2014') else int(x.strip()) for x in nums.group(1).split('·')]
    n = re.match(r'\s*(\d+)\.', tit)
    if n:
        manual[int(n.group(1))] = (tit, vals)

# los techos ya no se copian en la app: se leen del manual al generar los datos
techo = dict(enumerate(data.get('techos', [])))
print('recetas con techos impresos: %d   juegos de techos en los datos: %d' % (len(manual), len(techo)))
if 'var TECHO' in app:
    p('ERROR', 'ha vuelto a aparecer una tabla de techos copiada a mano en la app')

# KNOWN[i].r dice que receta usa cada mundo; TECHO va indexado por receta (0..19)
for num in sorted(manual):
    tit, vals = manual[num]
    i = num - 1
    if i not in techo:
        p('ERROR', 'receta %d sin techos en los datos' % num); continue
    if techo[i] != vals:
        p('ERROR', 'receta %d «%s»: manual %s  app %s' % (num, tit[:38], vals, techo[i]))
if len(techo) != len(manual):
    p('AVISO', 'TECHO tiene %d filas y el manual %d recetas numeradas' % (len(techo), len(manual)))

# ------------------------------------------------- 2. el presupuesto 12 / 14
print()
print('=' * 70)
print(' 2. Presupuesto de puntos, coste de Llaves y el acordeon')
print('=' * 70)
for pat, donde, que in (
        (r'function budget\(\)\{ return arcOpen\(\) \? 14 : 12; \}', app, 'app: budget 14/12'),
        (r'function keyCost\(k\)\{ var n = k\.lv \|\| 1; return n \* n; \}', app, 'app: Llaves n al cuadrado'),
        (r'12\s*(?:puntos|slots)|doce puntos', cap8, 'manual: 12 puntos'),
        (r'14\s*puntos|catorce puntos', cap8, 'manual: 14 puntos')):
    print('  %-34s %s' % (que, 'si' if re.search(pat, donde) else 'NO ENCONTRADO'))

juego = io.open('out3/nogum_juego.html', encoding='utf-8').read()
for q, pat in (('acordeon 8 / 22 / 44', r'\b8\b.{0,80}\b22\b.{0,80}\b44\b'),
               ('escalera 1 4 9 16 25', r'1,?\s*4,?\s*9,?\s*16,?\s*25'),
               ('x100 de la Rejilla', r'×100'),
               ('ancla menos2 mas4', r'−2\s*(?:y|a|and)\s*\+4')):
    print('  %-34s %s' % ('manual: ' + q, 'si' if re.search(pat, juego) else 'NO'))

# -------------------------------------------- 3. la escalera de la Rejilla x100
print()
print('=' * 70)
print(' 3. La escalera de alcance de la app contra el x100')
print('=' * 70)
g = re.search(r'var GRIDN = \[null,(.*?)\];', app, re.S)
if g:
    esperado = ['×1', '×100', '×10.000', '×1.000.000', '×100.000.000']
    hay = re.findall(r'·\s*(×[0-9.]+)', g.group(1))
    hay = [x for i, x in enumerate(hay) if i % 2 == 0]
    if hay != esperado:
        p('ERROR', 'GRIDN no sigue el x100: %s' % hay)
    else:
        print('  GRIDN: %s  correcto' % ' '.join(hay))

# ------------------------------------------------ 4. el Baul: 16 y la mascara
print()
print('=' * 70)
print(' 4. El Baul, el Codigo y los datos')
print('=' * 70)
print('  reglas del Baul en los datos: %d %s' % (len(data['baul']), '' if len(data['baul']) == 16 else '<-- ROMPE LA MASCARA DE 16 BITS'))
if len(data['baul']) != 16:
    p('ERROR', 'el Baul tiene %d reglas: el Codigo usa una mascara de 16 bits' % len(data['baul']))
print('  textos largos del Baul: %d' % len(data['baulLong']))
if len(data['baulLong']) != len(data['baul']):
    p('ERROR', 'baul y baulLong no cuadran')
print('  recetas en los datos: %d' % len(data['recipes']))
if len(data['recipes']) != 20:
    p('ERROR', 'hay %d recetas y deberian ser 20' % len(data['recipes']))

# los cuatro grupos del Baul tienen que cubrir 0..15 sin repetir
gm = re.search(r'var BAUL_GROUPS = \[(.*?)\n\];', app, re.S)
ks = [int(x) for x in re.findall(r'k:\[([0-9,]+)\]', gm.group(1))[0].split(',')] if gm else []
todos = []
for grp in re.findall(r'k:\[([0-9,]+)\]', gm.group(1) if gm else ''):
    todos += [int(x) for x in grp.split(',')]
if sorted(todos) != list(range(16)):
    p('ERROR', 'BAUL_GROUPS no cubre 0..15 exactamente: %s' % sorted(todos))
else:
    print('  BAUL_GROUPS cubre las 16 sin repetir: si')

# el reparto por peso del formulario tiene que cubrir tambien las 16
bo = re.search(r'var BAUL_ORD = \[(.*?)\n\];', app, re.S)
pesos = []
for L, H in re.findall(r'\{light:\[([0-9,]*)\], heavy:\[([0-9,]*)\]\}', bo.group(1) if bo else ''):
    pesos += [int(x) for x in L.split(',') if x] + [int(x) for x in H.split(',') if x]
if sorted(pesos) != list(range(16)):
    p('ERROR', 'BAUL_ORD no cubre 0..15 exactamente: %s' % sorted(pesos))
else:
    print('  BAUL_ORD (peso) cubre las 16 sin repetir: si')
# y cada regla tiene que estar en el mismo tema en los dos sitios
if gm and bo:
    tema_g = {}
    for gi, grp in enumerate(re.findall(r'k:\[([0-9,]+)\]', gm.group(1))):
        for x in grp.split(','):
            tema_g[int(x)] = gi
    tema_o = {}
    for gi, (L, H) in enumerate(re.findall(r'\{light:\[([0-9,]*)\], heavy:\[([0-9,]*)\]\}', bo.group(1))):
        for x in (L + ',' + H).split(','):
            if x:
                tema_o[int(x)] = gi
    malas = [k for k in tema_g if tema_g[k] != tema_o.get(k)]
    if malas:
        p('ERROR', 'reglas en temas distintos entre BAUL_GROUPS y BAUL_ORD: %s' % malas)
    else:
        print('  cada regla, en el mismo tema en los dos sitios: si')

# ------------------------------------------- 5. secciones del Bazar y recuentos
print()
print('=' * 70)
print(' 5. El Bazar: lo que dicen los datos y lo que dice el resumen del manual')
print('=' * 70)
cuentas = {}
for bz in data['bazar']:
    n = sum(len(b['items']) for b in bz['blocks'])
    cuentas[bz['n'][0]] = n
bazar = io.open('frag_bazar.html', encoding='utf-8').read()
res = dict((re.sub(r'<[^>]+>', '', a).strip(), int(b))
           for a, b in re.findall(r'<tr><td>(.*?)</td><td class="num">(\d+)</td>', bazar))
for nom, n in sorted(cuentas.items()):
    corto = nom
    esperado = res.get(corto)
    marca = ''
    if esperado is None:
        marca = '(no esta en la tabla resumen)'
    elif esperado != n:
        marca = '<-- el resumen dice %d' % esperado
        p('ERROR', 'Bazar «%s»: %d objetos de verdad, el resumen dice %d' % (corto, n, esperado))
    print('  %-46s %4d  %s' % (corto[:46], n, marca))
print('  TOTAL de objetos: %d' % sum(cuentas.values()))

# nombres sin fugas de banderas
fuga = [bz['n'][0] for bz in data['bazar'] if 'T12' in bz['n'][0] or 'Pendiente' in bz['n'][0] or 'Escrito a' in bz['n'][0]]
if fuga:
    p('ERROR', 'nombres de seccion con texto de bandera: %s' % fuga)
else:
    print('  nombres de seccion limpios de banderas: si')
malos = []
for bz in data['bazar']:
    for bl in bz['blocks']:
        for it in bl['items']:
            if not it.get('c'):
                malos.append(it['n'][0])
if malos:
    p('AVISO', '%d objetos sin categoria (no salen en el buscador por arbol): %s' % (len(malos), malos[:4]))
else:
    print('  todos los objetos tienen categoria: si')

print()
print('=' * 70)
print('PROBLEMAS: %d errores, %d avisos' % (len([x for x in PROB if x[0] == 'ERROR']), len([x for x in PROB if x[0] == 'AVISO'])))
print('=' * 70)
