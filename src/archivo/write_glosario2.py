# -*- coding: utf-8 -*-
"""Segunda pasada de renombrado: las mallas que quedaban y Disposición → Guardia."""
import io, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
MISS = []


def patch(fn, pairs):
    s = io.open(fn, encoding='utf-8').read()
    for a, b in pairs:
        if a not in s:
            MISS.append((fn, a[:60]))
            continue
        s = s.replace(a, b)
    io.open(fn, 'w', encoding='utf-8').write(s)


patch('frag_ch3.html', [('<strong>La Malla</strong> (5 ámbitos)', '<strong>Los Ámbitos</strong> (los 5)')])
patch('frag_ch4.html', [('como un sexto ámbito que no depende de la Malla', 'como un sexto ámbito que no depende de la pirámide')])
patch('frag_ch5.html', [('<span class="tag">Malla</span>', '<span class="tag">Rejilla</span>'),
                        ('disposiciones', 'guardias')])
patch('frag_ch5.en.html', [('<span class="tag">Mesh</span>', '<span class="tag">Grid</span>'),
                           ('stances', 'guards'), ('Stance', 'Guard'), ('stance', 'guard')])
patch('frag_ch67.html', [('El sistema completo: Malla, Dominios', 'El sistema completo: Ámbitos, Dominios')])
patch('frag_ch67.en.html', [('The complete system: Mesh, Domains', 'The complete system: Spheres, Domains')])
patch('frag_cap8.html', [('<tr><td>Malla mística inversa</td>', '<tr><td>Rejilla mística inversa</td>'),
                         ('<h4>Malla mística inversa</h4>', '<h4>Rejilla mística inversa</h4>'),
                         ('<strong>El fix:</strong> Malla de «Sombra».', '<strong>El fix:</strong> barra Espiritual de «Sombra».'),
                         ('<strong>El fix:</strong> Malla Especial (La Fuerza).', '<strong>El fix:</strong> Ámbito Arcano (La Fuerza).')])
patch('frag_cap8.en.html', [('Inverse mystical mesh', 'Inverse mystical grid'),
                            ('<h4>Inverse Mystical Mesh</h4>', '<h4>Inverse Mystical Grid</h4>')])
# la Guardia también en el capítulo de combate del Acelerado y en los recordatorios
for f in ('frag_acelerado.html',):
    s = io.open(f, encoding='utf-8').read()
    if 'Disposición' in s or 'disposición' in s:
        s = s.replace('Disposición', 'Guardia').replace('disposición', 'guardia')
        io.open(f, 'w', encoding='utf-8').write(s)
print('faltan:', MISS if MISS else 'nada')
