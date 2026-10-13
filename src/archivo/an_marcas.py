# -*- coding: utf-8 -*-
"""Inventario de marcas en el contenido publicable (tesis, juego, acelerado)."""
import io, os, re, json, collections
os.chdir(os.path.dirname(os.path.abspath(__file__)))

PUB = ['p3_tesis_es.html', 'p3_tesis_en.html', 'frag_intro.html', 'frag_intro.en.html',
       'frag_ch1a.html', 'frag_ch1a.en.html', 'frag_ch1b.html', 'frag_ch1b.en.html',
       'frag_ch2.html', 'frag_ch2.en.html', 'frag_ch3.html', 'frag_ch3.en.html',
       'frag_ch4.html', 'frag_ch4.en.html', 'frag_ch5.html', 'frag_ch5.en.html',
       'frag_ch67.html', 'frag_ch67.en.html', 'frag_cap8.html', 'frag_cap8.en.html',
       'frag_bazar.html', 'frag_bazar_a.en.html', 'frag_bazar_b.en.html',
       'frag_math.html', 'frag_math.en.html', 'frag_glosario.html', 'frag_glosario.en.html',
       'frag_acelerado.html', 'frag_acelerado.en.html']

MARCAS = {
 'juegos': ['D&amp;D', 'Pathfinder', 'OSR', 'Warhammer', 'The Witcher', 'Anillo Único', 'One Ring',
            'Leyenda de los 5 Anillos', 'L5R', '7th Sea', 'Yggdrasil', 'Star Wars', 'Cyberpunk',
            'Eclipse Phase', 'Altered Carbon', 'Mad Max', 'Fallout', 'Shadowrun', 'Cthulhu',
            'Vampiro', 'Mascarada', 'Masquerade', 'Kids on Bikes', 'Stranger Things',
            'Monster of the Week', 'Buffy', 'Blades in the Dark', 'Marvel', 'Dragon Ball',
            'Evangelion', 'Pacific Rim', 'Paranoia', 'Mundodisco', 'Discworld', 'GURPS', 'Fate',
            'HITOS', 'Apocalypse World', 'PbtA', 'Rolemaster', 'Savage Worlds', 'Deadlands',
            'Mass Effect', 'Toon', 'Tigre y Dragón', 'Crouching Tiger'],
 'personajes': ['Conan', 'Superman', 'Batman', 'Spider-Man', 'Godzilla', 'Hulk', 'Terminator',
                'MacGyver', 'Stark', 'Gandalf', 'Magneto', 'Luffy', 'John Wick', 'McClane',
                'Sherlock', 'Watson', 'Walter White', 'Rick S', 'Doctor Strange', 'Tormenta',
                'Capitán América', 'Captain America', 'Gimli', 'Asuka', 'Indiana Jones',
                'Guardianes de la Galaxia', 'Guardians of the Galaxy', 'James Bond', 'Elm Street',
                'Twin Peaks', 'Fargo', 'Juego de Tronos', 'Game of Thrones', '1984', 'Chernóbil',
                'Chernobyl', 'Omni-Man', 'Jedi', 'Sith', 'Wookiee', 'Saiyan'],
 'objetos': ['Kriptonita', 'Kryptonite', 'Vibranium', 'Batmóvil', 'Batmobile', 'Batarang',
             'Pip-Boy', 'Stealth Boy', 'Sandevistan', 'Kame', 'Genkidama', 'Taiyoken',
             'Nube Kinton', 'Semilla del Ermitaño', 'Namekiana', 'Pothala', 'Abanico Bancho',
             'Espada Z', 'Shunpo', 'Estrella del Norte', 'Rötschreck', 'Vorpalina', 'Vorpal',
             'Roca Fantasma', 'Toon Force', 'Iron Man', 'Molotov'],
}

hits = collections.OrderedDict()
for grupo, lista in MARCAS.items():
    for b in lista:
        tot, donde, ctx = 0, set(), None
        for f in PUB:
            if not os.path.exists(f):
                continue
            s = io.open(f, encoding='utf-8').read()
            n = s.count(b)
            if n:
                tot += n
                donde.add(f.replace('frag_', '').replace('.html', '').replace('p3_', ''))
                if ctx is None:
                    i = s.index(b)
                    ctx = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', s[max(0, i - 70):i + 70])).strip()
        if tot:
            hits[b] = {'g': grupo, 'n': tot, 'f': sorted(donde), 'ctx': ctx}

json.dump(hits, io.open('marcas.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('marcas con presencia:', len(hits), '| menciones:', sum(v['n'] for v in hits.values()))
for g in MARCAS:
    sub = [(k, v['n']) for k, v in hits.items() if v['g'] == g]
    print('\n--', g, len(sub))
    print(', '.join('%s(%d)' % x for x in sorted(sub, key=lambda x: -x[1])))
