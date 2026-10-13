# -*- coding: utf-8 -*-
"""Arrastre de nombres viejos: Héroe/Terror/Estándar quedaron de la ronda anterior."""
import io, os, glob
os.chdir(os.path.dirname(os.path.abspath(__file__)))

ES = [('tarjeta Héroe', 'tarjeta Épica'), ('tarjeta Terror', 'tarjeta Angustia'),
      ('tarjeta Estándar', 'tarjeta Primera marcha')]
EN = [('Hero card', 'Epic card'), ('Terror card', 'Anguish card'), ('Standard card', 'First Gear card')]
SKIP = ('frag_editorial', 'frag_descartados', 'frag_trazabilidad')  # registro histórico

n = 0
for f in sorted(glob.glob('frag_*.html')) + ['p3_tesis_es.html', 'p3_tesis_en.html']:
    if 'bak' in f or any(k in f for k in SKIP):
        continue
    s = io.open(f, encoding='utf-8').read()
    o = s
    for a, b in (EN if '.en.' in f or f.endswith('_en.html') else ES):
        s = s.replace(a, b)
    if s != o:
        io.open(f, 'w', encoding='utf-8').write(s)
        n += 1

# la Tesis todavía prometía nueve casillas
s = io.open('p3_tesis_es.html', encoding='utf-8').read()
a = ('<li>Cruzados forman una <strong>malla tonal</strong> de nueve casillas que mapea los géneros. '
     'No es un menú cerrado: los tonos posibles son infinitos.</li>')
b = ('<li>Cruzados forman un <strong>cuadrante</strong> de nueve sitios que mapea los géneros, con siete tarjetas y dos huecos. '
     'Los huecos son de verdad: con un dado plano no hay forma de inclinar el tono sin mover la dificultad, y la dificultad no se toca. '
     'No es un menú cerrado: los tonos posibles son infinitos.</li>')
assert a in s
io.open('p3_tesis_es.html', 'w', encoding='utf-8').write(s.replace(a, b))

s = io.open('p3_tesis_en.html', encoding='utf-8').read()
for a, b in [('<strong>tonal grid</strong> of nine cells', '<strong>quadrant</strong> of nine places, with seven cards and two gaps,'),
             ('<strong>tonal grid</strong> of nine squares', '<strong>quadrant</strong> of nine places, with seven cards and two gaps,')]:
    if a in s:
        s = s.replace(a, b)
        break
io.open('p3_tesis_en.html', 'w', encoding='utf-8').write(s)

# canon: marcar el panel viejo como superado, para que la IA de la app no se contradiga
c = io.open('CANON.md', encoding='utf-8').read()
a = '- 1.4 Panel de Control: 6 Tarjetas de Tono (+ configuración por defecto). Canon (ED-2 corrige erratas del borrador):'
assert a in c
c = c.replace(a, '- 1.4 Panel de Control **[SUPERADO: ver §2bis, el cuadrante de siete tarjetas. Lo que sigue es el panel antiguo y se conserva solo como registro; no se responde con él]**: 6 Tarjetas de Tono (+ configuración por defecto). Canon (ED-2 corrige erratas del borrador):')
io.open('CANON.md', 'w', encoding='utf-8').write(c)
print('archivos con nombres corregidos:', n)
