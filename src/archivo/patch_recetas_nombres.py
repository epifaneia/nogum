# -*- coding: utf-8 -*-
"""Las veinte recetas apuntaban a tarjetas retiradas: se remapean a la que tiene los mismos dados."""
import io, os, glob, re
os.chdir(os.path.dirname(os.path.abspath(__file__)))

MAP_ES = [
    ('T1 Héroe', 'Épica'), ('Épica Clásica', 'Épica'), ('Épica clásica', 'Épica'),
    ('T0 Estándar', 'Primera marcha'), ('T2 Realista', 'Realista'),
    ('T3 Pulp / Drama', 'Bola de nieve'), ('T3 Pulp/Drama', 'Bola de nieve'),
    ('T5 Gonzo', 'Bola de nieve'), ('Comedia Negra', 'Bola de nieve'),
    ('T4 Terror', 'Pesadilla'), ('Pulp Desatado', 'Pulp desenfrenado'), ('Pulp desatado', 'Pulp desenfrenado'),
    ('Fantasía de Poder', 'Épica'), ('Fantasía de poder', 'Épica'),
    ('Realismo Gris', 'Realista'), ('Realismo gris', 'Realista'),
    ('Terror Purista', 'Angustia'), ('Terror purista', 'Angustia'),
    ('Thriller de Supervivencia', 'Pesadilla'), ('Thriller de supervivencia', 'Pesadilla'),
    ('Drama de Acción', 'Primera marcha'), ('Drama de acción', 'Primera marcha'),
]
MAP_EN = [
    ('T1 Hero', 'Epic'), ('Classic Epic', 'Epic'), ('T0 Standard', 'First Gear'), ('T2 Realist', 'Realist'),
    ('T3 Pulp / Drama', 'Snowball'), ('T5 Gonzo', 'Snowball'), ('Black Comedy', 'Snowball'),
    ('T4 Terror', 'Nightmare'), ('Unleashed Pulp', 'Unleashed Pulp'),
    ('Power Fantasy', 'Epic'), ('Grey Realism', 'Realist'), ('Purist Horror', 'Anguish'),
    ('Survival Thriller', 'Nightmare'), ('Action Drama', 'First Gear'),
]
SKIP = ('editorial', 'descartados', 'trazabilidad', 'math')  # registro histórico y tabla de erratas

n = 0
for f in sorted(glob.glob('frag_*.html')):
    if 'bak' in f or any(k in f for k in SKIP):
        continue
    s = io.open(f, encoding='utf-8').read()
    o = s
    for a, b in (MAP_EN if '.en.' in f else MAP_ES):
        s = s.replace(a, b)
    if s != o:
        io.open(f, 'w', encoding='utf-8').write(s)
        n += 1
        print('remapeado', f)
print('archivos:', n)

# la pregunta abierta del cuaderno sobre diferenciar Fantasía de poder y Épica clásica queda resuelta
e = io.open('frag_editorial.html', encoding='utf-8').read()
a = 'Diferenciar Fantasía de poder y Épica clásica, y diseñar las recetas Pulp desatado y Pesadilla.'
if a in e:
    e = e.replace(a, 'Diferenciar Fantasía de poder y Épica clásica, y diseñar las recetas Pulp desatado y Pesadilla. <strong>Cerrado</strong>: el cuadrante de siete tarjetas elimina la distinción —las dos eran el mismo mejor de dos— y convierte aquellas recetas en el Pulp desenfrenado y la Pesadilla actuales.')
    io.open('frag_editorial.html', 'w', encoding='utf-8').write(e)
    print('pregunta abierta cerrada en el cuaderno')

# estilo para los huecos del mapa 1.2
c = io.open('paper.css', encoding='utf-8').read()
if 'grid-tonal td.hueco' not in c:
    c += '\n.grid-tonal td.hueco{color:var(--ink-3);background:repeating-linear-gradient(135deg,transparent,transparent 6px,var(--rule-2) 6px,var(--rule-2) 7px)}\n'
    io.open('paper.css', 'w', encoding='utf-8').write(c)
    print('css del hueco añadido')
