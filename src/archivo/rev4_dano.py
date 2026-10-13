# -*- coding: utf-8 -*-
"""El tope de dano de un arma es 2. A ver cuanto se ha saltado eso el bazar."""
import io, os, re, json
os.chdir(os.path.dirname(os.path.abspath(__file__)))
D = json.load(io.open('app_data.json', encoding='utf-8'))

tres, dos_duros, raros = [], [], []
for bz in D['bazar']:
    for bl in bz['blocks']:
        for it in bl['items']:
            d = it['d'][0] or ''
            e = it['e'][0] or ''
            a = it['a'][0] or ''
            m = re.search(r'(?:Daño|Dmg)[^0-9]*(\d+)', d)
            if not m:
                continue
            n = int(m.group(1))
            fila = (bz['n'][0], bl['n'][0], it['n'][0], d, e, a)
            if n >= 3:
                tres.append(fila)
            elif n == 2 and 'Nula' in e and 'Nula' in a:
                dos_duros.append(fila)

print('=' * 78)
print(' Objetos con Dano 3 o mas (el canon dice que el tope de un arma es 2)')
print('=' * 78)
print(' total: %d' % len(tres))
porsec = {}
for s, b, n, d, e, a in tres:
    porsec.setdefault(s, []).append((b, n, d, e, a))
for s in sorted(porsec, key=lambda x: -len(porsec[x])):
    print('\n  %s  (%d)' % (s, len(porsec[s])))
    for b, n, d, e, a in porsec[s]:
        print('     %-34s %-16s %-22s %s' % (n[:34], d[:16], e[:22], a[:20]))

print()
print('=' * 78)
print(' Los que ya cumplen el patron del canon: Dano 2, Esq Nula, Abs Nula')
print('=' * 78)
print(' total: %d' % len(dos_duros))
for s, b, n, d, e, a in dos_duros[:14]:
    print('   %-30s %-34s' % (n[:30], s[:34]))

print()
print('=' * 78)
print(' Cuantos golpes hacen falta con el tope en 2')
print('=' * 78)
for z, u in (('La Cascara', 3), ('La Carne', 9), ('El Nucleo', 27)):
    print('   %-12s  Dano 1: %2d golpes   Dano 2: %2d golpes' % (z, u, (u + 1) // 2))
