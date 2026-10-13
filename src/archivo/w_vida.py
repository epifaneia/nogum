# -*- coding: utf-8 -*-
"""La vida fractal se renombra: Letal (3) · Tactico (9) · Guerra (27).
Los nombres viejos describian donde estaba la camara; estos dicen que le pasa
al personaje, y se ordenan solos. Las claves internas NO se tocan: alimentan
el campo Z del Codigo de mesa."""
import io, os, re, glob, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))

PARES = [
    # castellano
    ('del Núcleo', 'de Guerra'),
    ('La Cáscara', 'Letal'), ('la Cáscara', 'Letal'),
    ('La Carne', 'Táctico'), ('la Carne', 'Táctico'),
    ('El Núcleo', 'Guerra'), ('el Núcleo', 'Guerra'),
    # ingles
    ('the Core zoom', 'the War zoom'),
    ('The Shell', 'Lethal'), ('the Shell', 'Lethal'),
    ('The Flesh', 'Tactical'), ('the Flesh', 'Tactical'),
    ('The Core', 'War'),
]
FICH = [x for x in glob.glob('frag_*.html') if '.bak' not in x] + ['app4_body.html']
tot = 0
for f in sorted(FICH):
    s = io.open(f, encoding='utf-8').read()
    o = s
    for a, b in PARES:
        if a in s:
            tot += s.count(a)
            s = s.replace(a, b)
    if s != o:
        io.open(f, 'w', encoding='utf-8').write(s)
        print('  %-24s tocado' % f)
print('%d nombres cambiados' % tot)

# el numero junto al nombre, en la app
s = io.open('app4_body.html', encoding='utf-8').read()
a = "  cascara:{n:['Letal','Lethal'], units:3, size:9},"
if a in s:
    print('  claves internas intactas: cascara/carne/nucleo (el Codigo usa Z1/Z2/Z3)')
else:
    print('  AVISO: revisa el objeto ZOOM de la app')

# comprobacion: que no quede ninguno y que las claves sigan
resto = 0
for f in sorted(FICH):
    s = io.open(f, encoding='utf-8').read()
    for pat in ('Cáscara', 'The Shell', 'The Flesh'):
        resto += len(re.findall(pat, s))
print('restos de los nombres viejos: %d' % resto)
for k in ("cascara:", "carne:", "nucleo:"):
    if k not in io.open('app4_body.html', encoding='utf-8').read():
        print('  ERROR: falta la clave %s' % k); sys.exit(1)
print('las tres claves internas siguen en su sitio')
