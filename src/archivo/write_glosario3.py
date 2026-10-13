# -*- coding: utf-8 -*-
"""Pasada de vocabulario en la edición inglesa: Mesh → Sphere/Grid, Tonal Grid → Quadrant, Stance → Guard."""
import io, os, re
os.chdir(os.path.dirname(os.path.abspath(__file__)))

PAIRS = [
    ('the “Shadow Mesh” is neither the Tonal Grid nor the Power Grid', 'the draft’s “Shadow Mesh” is neither the Quadrant nor the Power Grid'),
    ('“Shadow” Mesh', '“Shadow” Spiritual track'),
    ('Special Mesh (The Force)', 'Arcane Sphere (The Force)'),
    ('Inverse mystic mesh', 'Inverse mystic grid'),
    ('inverse mystic mesh', 'inverse mystic grid'),
    ('invisible to the Mystic Mesh', 'invisible to the Mystic Grid'),
    ('<strong>the Mesh</strong> is the continent', '<strong>the Sphere</strong> is the continent'),
    ('<strong>The Mesh</strong> (5 spheres)', '<strong>The Spheres</strong> (all 5)'),
    ('in a sphere of the Mesh', 'in a Sphere'),
    ('section outside the Mesh', 'section outside the pyramid'),
    ('like a sixth sphere that does not depend on the Mesh', 'like a sixth sphere that does not depend on the pyramid'),
    ('The full system: the Mesh, Domains', 'The full system: Spheres, Domains'),
    ('Tonal Grid', 'Quadrant'),
]
GUARD = [('Stances', 'Guards'), ('Stance', 'Guard'), ('stances', 'guards'), ('stance', 'guard')]
KEEP = ('the universe has a stance',)  # uso corriente, no término

n = 0
for f in sorted(os.listdir('.')):
    if not (f.startswith('frag_') and f.endswith('.en.html')) or 'bak' in f:
        continue
    s = io.open(f, encoding='utf-8').read()
    o = s
    for a, b in PAIRS:
        s = s.replace(a, b)
    for a, b in GUARD:
        if a in s and not any(k in s for k in KEEP):
            s = s.replace(a, b)
        elif a in s:
            # respeta el uso corriente y cambia solo el término
            s = re.sub(r'(?<!has a )' + a, b, s)
    if s != o:
        io.open(f, 'w', encoding='utf-8').write(s)
        n += 1
print('archivos tocados:', n)
