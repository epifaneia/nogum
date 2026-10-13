# -*- coding: utf-8 -*-
"""Ultimos nombres de tarjeta del borrador que seguian vivos."""
import io, os, glob, re
os.chdir(os.path.dirname(os.path.abspath(__file__)))

ES = [
    ('la tarjeta Gonzo (T5: 1d10; pifia con 1–2, crítico con 9–10)',
     'la tarjeta Bola de nieve (dado rojo; pifia con 1–2, crítico con 9–10)'),
    ('la tarjeta Gonzo (Caos Alto)', 'la tarjeta Bola de nieve (caos alto)'),
    ('«cambiamos a Modo Gonzo»', '«cambiamos a Bola de nieve»'),
    ('en Modo Héroe', 'en Épica'),
    ('Cambio a Modo Héroe', 'Cambio a Épica'),
    ('Tarjeta 0', 'Primera marcha'),
    ('Malla Tonal', 'Malla Tonal'),  # el glosario lo cita a proposito como nombre retirado
]
EN = [
    ('the Gonzo card (T5: 1d10; fumble on 1–2, critical on 9–10)',
     'the Snowball card (red die; fumble on 1–2, critical on 9–10)'),
    ('the Gonzo card (High Chaos)', 'the Snowball card (high chaos)'),
    ('“we’re switching to Gonzo Mode”', '“we’re switching to Snowball”'),
    ("“we're switching to Gonzo Mode”", '“we’re switching to Snowball”'),
    ('in Hero Mode, practically certain', 'in Epic, practically certain'),
    ('in Hero Mode', 'in Epic'),
    ('Hero Mode', 'Epic'),
    ('Card 0', 'First Gear'),
]
n = 0
for f in sorted(glob.glob('frag_*.html')):
    if 'bak' in f or any(k in f for k in ('editorial', 'descartados', 'trazabilidad', 'math')):
        continue
    s = io.open(f, encoding='utf-8').read()
    o = s
    for a, b in (EN if '.en.' in f else ES):
        s = s.replace(a, b)
    if s != o:
        io.open(f, 'w', encoding='utf-8').write(s)
        n += 1
        print(' ', f)
print('archivos tocados:', n)
