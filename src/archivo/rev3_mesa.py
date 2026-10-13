# -*- coding: utf-8 -*-
"""Revision de producto: los numeros que se notan en la mesa."""
import io, os, re, json, itertools
os.chdir(os.path.dirname(os.path.abspath(__file__)))
D = json.load(io.open('app_data.json', encoding='utf-8'))

print('=' * 74)
print(' 1. La curva real de cada tarjeta, por bono (TN 6, dos d10)')
print('=' * 74)
CAR = {
    'Epica':      ('mejor', 6), 'Pulp':       ('mejor', 6),
    'Realista':   ('suma', 11), 'Primera':    ('rojo', 6),
    'Bola':       ('rojo', 6),  'Angustia':   ('peor', 6),
    'Pesadilla':  ('peor', 6),  'Tragedia':   ('suma', 14),
}
tiradas = list(itertools.product(range(1, 11), repeat=2))
print('  %-11s %s' % ('tarjeta', '  '.join('%+d' % b for b in range(-2, 5))))
for n, (modo, tn) in CAR.items():
    fila = []
    for b in range(-2, 5):
        ok = 0
        for a, c in tiradas:
            v = max(a, c) if modo == 'mejor' else min(a, c) if modo == 'peor' else (a + c) if modo == 'suma' else a
            if v + b >= tn:
                ok += 1
        fila.append('%3d%%' % round(ok * 100.0 / len(tiradas)))
    print('  %-11s %s' % (n, '  '.join(fila)))

print()
print('=' * 74)
print(' 2. El Acceso: que puede comprar quien NO tiene Recursos')
print('=' * 74)
acc = {0: 0, 1: 0, 2: 0, 3: 0, 9: 0}
por_uni = {}
for bz in D['bazar']:
    c = {0: 0, 1: 0, 2: 0, 3: 0, 9: 0}
    for bl in bz['blocks']:
        for it in bl['items']:
            m = re.search(r'(?:Acceso|Access) (\d)', it['m'][0] or '')
            k = int(m.group(1)) if m else 9
            acc[k] += 1
            c[k] += 1
    por_uni[bz['n'][0]] = c
tot = sum(acc.values())
print('  Acceso 0: %3d   Acceso 1: %3d   Acceso 2: %3d   Acceso 3: %3d   sin precio: %3d   (total %d)'
      % (acc[0], acc[1], acc[2], acc[3], acc[9], tot))
compra = acc[0]
print('  Un personaje SIN Recursos (bono -2) solo alcanza Acceso 0: %d de %d objetos con precio (%d%%)'
      % (compra, tot - acc[9], round(compra * 100.0 / max(tot - acc[9], 1))))
print('  Con Recursos amplio (+1) alcanza: %d (%d%%)' % (acc[0] + acc[1], round((acc[0] + acc[1]) * 100.0 / max(tot - acc[9], 1))))
print('  Con Recursos concreto (+2) alcanza: %d (%d%%)' % (acc[0] + acc[1] + acc[2], round((acc[0] + acc[1] + acc[2]) * 100.0 / max(tot - acc[9], 1))))
print()
print('  Por universo, cuantos objetos quedan fuera de alcance sin Recursos:')
for n, c in sorted(por_uni.items(), key=lambda x: -(x[1][2] + x[1][3])):
    con_precio = c[0] + c[1] + c[2] + c[3]
    if not con_precio:
        continue
    print('    %-44s %2d de %2d (Acceso 2-3)' % (n[:44], c[2] + c[3], con_precio))

print()
print('=' * 74)
print(' 3. Dano contra zoom: cuantos golpes hacen falta')
print('=' * 74)
dmg = {}
for bz in D['bazar']:
    for bl in bz['blocks']:
        for it in bl['items']:
            m = re.search(r'(?:Daño|Dmg)\s*(\d)', it['d'][0] or '')
            if m:
                dmg[int(m.group(1))] = dmg.get(int(m.group(1)), 0) + 1
print('  objetos por Dano: ' + '  '.join('Dano %d: %d' % (k, dmg[k]) for k in sorted(dmg)))
print()
print('  %-16s %-10s %-10s %-10s' % ('zoom', 'unidades', 'Dano 1', 'Dano 3'))
for z, u, s in (('La Cascara', 3, 9), ('La Carne', 9, 3), ('El Nucleo', 27, 1)):
    print('  %-16s %-10d %-10s %-10s' % (z, u, '%d golpes' % u, '%d golpes' % max(1, (u + 2) // 3)))
print('  (en La Cascara, tres impactos de cualquier arma dejan fuera de combate)')

print()
print('=' * 74)
print(' 4. El acordeon contra el presupuesto')
print('=' * 74)
print('  Presupuesto inicial: 12 puntos (14 si hay Arcano)')
for n, c in (('Disciplina plegada', 8), ('Dominio plegado', 22), ('Ambito plegado', 44)):
    print('    %-20s %2d puntos  -> %s' % (n, c, 'cabe de salida' if c <= 12 else 'NO cabe: solo con progresion'))
print('  Con 1 punto por sesion, el Dominio llega hacia la sesion %d y el Ambito hacia la %d.' % (22 - 12, 44 - 12))

print()
print('=' * 74)
print(' 5. Llaves: lo que cuesta subir de Rejilla')
print('=' * 74)
print('  Monedero por defecto: 1 Llave por sesion. Bote inicial: 5 Llaves.')
for lv in range(1, 6):
    print('    nivel +%d contra lo mismo: %2d Llaves  -> sesion %2d si se guarda todo' % (lv, lv * lv, max(0, lv * lv - 5)))

print()
print('=' * 74)
print(' 6. Las veinte recetas: reparto de tarjetas y de techos')
print('=' * 74)
cap8 = io.open('frag_cap8.html', encoding='utf-8').read()
TARJ = ['Epica', 'Pulp desenfrenado', 'Realista', 'Primera marcha', 'Bola de nieve', 'Angustia', 'Pesadilla', 'Tragedia']
cuenta = dict((t, 0) for t in TARJ)
for m in re.finditer(r'<p class="recipe-title">(.*?)</p>(.*?)<p class="recipe-grid">', cap8, re.S):
    cuerpo = re.sub(r'<[^>]+>', ' ', m.group(2))
    for t in TARJ:
        if t.lower() in cuerpo.lower():
            cuenta[t] += 1
            break
for t in TARJ:
    print('    %-20s %2d recetas %s' % (t, cuenta[t], '#' * cuenta[t]))
sin = [i + 1 for i, x in enumerate(D['techos']) if x[4] == 0]
print('  Recetas sin Arcano (12 puntos): %s' % sin)
alto = [i + 1 for i, x in enumerate(D['techos']) if max(x) >= 5]
print('  Recetas con algun techo 5 (sin tope real): %s' % alto)

print()
print('=' * 74)
print(' 7. Cabos: banderas vivas y cosas sin cerrar')
print('=' * 74)
aud = io.open('auditoria.txt', encoding='utf-8').read()
print('  banderas vivas: %d' % aud.count('\n[')) if '\n[' in aud else None
for l in aud.split('\n'):
    if l.startswith('['):
        print('    ' + l[:112])
