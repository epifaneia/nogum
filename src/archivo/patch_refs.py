# -*- coding: utf-8 -*-
"""Actualiza el resto del manual al modelo de siete tarjetas (referencias, malla de géneros, Acelerado)."""
import io, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
MISS = []


def patch(fn, pairs, need=True):
    s = io.open(fn, encoding='utf-8').read()
    for a, b in pairs:
        if a not in s:
            MISS.append((fn, a[:70]))
            continue
        s = s.replace(a, b)
    io.open(fn, 'w', encoding='utf-8').write(s)


# ---- 1.2 malla de géneros: tono y huecos
patch('frag_ch1a.html', [
    ('El universo te odia', 'El universo te pone a prueba'),
    ('<th>Caos medio<br><small>Aventura</small></th>', '<th>Caos medio<br><small>La costumbre</small></th>'),
    ('<p>La malla no es un menú cerrado',
     '<p><strong>Dos de estos nueve géneros no tienen tarjeta propia.</strong> La Épica clásica y el Thriller de supervivencia caen en la columna de la costumbre, donde el dado es plano y no hay forma de inclinar el tono sin mover la dificultad (el porqué está en el <a href="#ch1-maquinas">1.3</a>). Para jugarlos, coge la tarjeta vecina: la ordenada si quieres que el mundo se comporte, la caótica si quieres que haga ruido. Y si encuentras la regla que llena ese hueco, es tuya.</p>\n'
     '<p>La malla no es un menú cerrado'),
])
patch('frag_ch1a.en.html', [
    ('hates you', 'puts you to the test'),
    ('<th>Medium chaos<br><small>Adventure</small></th>', '<th>Medium chaos<br><small>The habit</small></th>'),
])

# ---- referencias a las tarjetas numeradas
patch('frag_ch4.html', [
    ('Cifras con la Tarjeta 0 (1d10 contra TN 6)', 'Cifras con la tarjeta Estándar (dado rojo contra TN 6)'),
    ('Con el peor de 2d10 (Tarjeta 4)', 'Con el peor de 2d10 (tarjeta Terror)'),
    ('Si el tono es optimista (Tarjeta 1)', 'Si el tono es optimista (tarjeta Héroe)'),
    ('11 en Realista, 14 en Tragedia', 'y 11 en la Realista'),
])
patch('frag_ch4.en.html', [
    ('Figures with Card 0 (1d10 against TN 6)', 'Figures with the Standard card (red die against TN 6)'),
    ('With the worst of 2d10 (Card 4)', 'With the lower of 2d10 (Terror card)'),
    ('If the tone is optimistic (Card 1)', 'If the tone is optimistic (Hero card)'),
    ('11 in Realist, 14 in Tragedy', 'and 11 on the Realist'),
])
patch('frag_ch67.html', [
    ('Tarjeta 4 y daño de nivel 1', 'tarjeta Terror y daño de nivel 1'),
    ('Tarjeta 2 y daño mental', 'tarjeta Realista y daño mental'),
    ('Y el DJ señala la Tarjeta 4', 'Y el DJ señala la tarjeta Terror'),
    ('el héroe elegido tira con la Tarjeta 1 mientras su compañero maldito tira con la 4',
     'el héroe elegido tira con la tarjeta Héroe mientras su compañero maldito tira con la Terror'),
    ('href="#ch1-malla">Malla Tonal</a> y coge la tarjeta que le corresponde',
     'href="#ch1-panel-cuadrante">cuadrante</a> y coge la tarjeta que le corresponde'),
])
patch('frag_ch67.en.html', [
    ('Card 4 and level 1 damage', 'Terror card and level 1 damage'),
    ('Card 2 and mental damage', 'Realist card and mental damage'),
    ('And the GM points at Card 4', 'And the GM points at the Terror card'),
    ('the chosen hero rolls with Card 1 while their cursed companion rolls with Card 4',
     'the chosen hero rolls with the Hero card while their cursed companion rolls with Terror'),
    ('href="#ch1-malla">Tonal Grid</a> and take the matching card',
     'href="#ch1-panel-cuadrante">quadrant</a> and take the matching card'),
])
patch('frag_cap8.html', [
    ('(como en la tarjeta T1 Héroe)', '(como en la tarjeta Héroe)'),
    ('<strong>tarjeta T1 Héroe', '<strong>tarjeta Héroe'),
    ('<strong>tarjeta T6 Tragedia', '<strong>receta Tragedia'),
])
patch('frag_cap8.en.html', [
    ('(as on the T1 Hero card)', '(as on the Hero card)'),
    ('<strong>T1 Hero card', '<strong>Hero card'),
    ('<strong>T6 Tragedy card', '<strong>Tragedy recipe'),
])

# ---- Acelerado: la banda pasa a ser la zona de roce del manual completo
patch('frag_acelerado.html', [
    ('Total 5 o menos: fallo · 6–7: <strong>éxito parcial</strong> · 8 o más: éxito',
     'Total 4 o menos: fallo · 5–6: <strong>éxito parcial</strong> · 7 o más: éxito'),
    ('Se adoptan las de la tarjeta Pulp del manual completo (5 o menos fallo, 6–7 parcial, 8 o más éxito), aplicadas al dado menor. Queda pendiente de que el autor lo confirme.',
     'Son las de la zona de roce del manual completo —la TN y el punto justo por debajo: 4 o menos fallo, 5–6 parcial, 7 o más éxito— aplicadas al dado menor. Confirmado por el autor.'),
    ('en Agobio, un profesional (+2) sale adelante un 49 % de las veces, pero solo la mitad de esas veces (25 %) s',
     'en Agobio, un profesional (+2) sale adelante un 64 % de las veces, pero solo un 36 % s'),
    ('en Agobio, el 49 % (y a menudo pagando)', 'en Agobio, el 64 %, y más de la mitad de esas veces pagando un precio'),
    ('Bandas de Agobio sobre el dado menor: 5 o menos fallo, 6–7 parcial, 8 o más éxito (las de la tarjeta Pulp)',
     'Bandas de Agobio sobre el dado menor: 4 o menos fallo, 5–6 parcial, 7 o más éxito (la zona de roce del manual completo)'),
])
patch('frag_acelerado.en.html', [
    ('Total 5 or less: failure · 6–7: <strong>partial success</strong> · 8 or more: success',
     'Total 4 or less: failure · 5–6: <strong>partial success</strong> · 7 or more: success'),
    ('in Dread, a professional (+2) gets through 49% of the time, but only half of those times (',
     'in Dread, a professional (+2) gets through 64% of the time, but only 36% of the time ('),
    ('in Dread, 49% (and often paying for it)', 'in Dread, 64%, and more than half of those times paying a price'),
])

print('faltan:', MISS if MISS else 'nada')
