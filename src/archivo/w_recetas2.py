# -*- coding: utf-8 -*-
"""Los cinco reemplazos que fallaron por etiquetas o por comillas, hechos con regex."""
import io, os, re
os.chdir(os.path.dirname(os.path.abspath(__file__)))

ES = [
    (r'el tono es Bola de nieve \(<?[^)]*?Bola de nieve[^)]*?\)',
     'el tono es Bola de nieve (optimismo neutro, caos alto)'),
    (r'Tragedia \(Caos Bajo\) y rejilla mística inversa \(saber = locura\)\.',
     'Angustia (peor de 2d10 con bandas estrechas) y rejilla mística inversa (saber = locura).'),
]
EN = [
    (r'In canon: T3 Pulp/Drama \([^)]*?partial success\) or Snowball for more of a roulette\.',
     'In canon: Snowball (“yes, but it’s going to cost you”: red die, success at a cost and wide bands). '
     'If you want the city to be unfair as well as chaotic, Nightmare.'),
    (r'The author sets no tone; T3 Pulp/Drama fits',
     'The author sets no tone; Snowball fits'),
    (r'T3 Pulp/Drama \(1d10 with partial success on 6–7\)',
     'Snowball (1d10 with partial success on 6–7)'),
    (r'the tone is Snowball \(<?[^)]*?Snowball[^)]*?\)',
     'the tone is Snowball (neutral optimism, high chaos)'),
    (r'Tragedy \(Low Chaos\) and inverse mystic grid \(knowledge = madness\)\.',
     'Anguish (worst of 2d10 with narrow bands) and the inverse mystic grid (knowledge = madness).'),
]

for f, rules in (('frag_cap8.html', ES), ('frag_cap8.en.html', EN)):
    s = io.open(f, encoding='utf-8').read()
    for pat, rep in rules:
        s, n = re.subn(pat, rep, s, flags=re.S)
        print(f, n, pat[:44])
    io.open(f, 'w', encoding='utf-8').write(s)

for f in ('frag_cap8.html', 'frag_cap8.en.html'):
    s = io.open(f, encoding='utf-8').read()
    for bad in ('T3 Pulp', 'T6 Trage', 'T1 H', 'T5 Gonzo', 'T4 Terror'):
        if bad in s:
            print('  QUEDA:', f, bad)
print('listo')
