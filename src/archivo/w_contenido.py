# -*- coding: utf-8 -*-
"""Las ocho armas sociales que faltaban y los once objetos del Mundo Animado."""
import io, os, re
os.chdir(os.path.dirname(os.path.abspath(__file__)))
T = lambda x: '<span class="tag">%s</span>' % x
D = '—'


def fila(n, d, e, a, m, nota):
    f = lambda x: T(x) if x and x != D else D
    return ('<tr><td><strong>%s</strong></td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>\n'
            % (n, f(d), f(e), f(a), m or D, nota))


#  (es, en, dano_es, dano_en, esq_es, esq_en, abs_es, abs_en, efecto_es, efecto_en, nota_es, nota_en)
SOCIAL = [
 ('El Silencio Calculado', 'The Calculated Silence', 'Daño Social 1', 'Social Dmg 1', 'Esq: Nula', 'Dodge: None',
  'Abs: Reputación', 'Soak: Reputation', D, D,
  'No decir nada cuando toda la sala espera que digas algo. No se puede esquivar porque no ha pasado nada.',
  'Saying nothing when the whole room is waiting for you to speak. It cannot be dodged because nothing happened.'),
 ('La Pregunta Inocente', 'The Innocent Question', 'Daño Social 1', 'Social Dmg 1', 'Esq: Total', 'Dodge: Full',
  'Abs: Reputación', 'Soak: Reputation', D, D,
  'Preguntar en voz alta algo que no se puede contestar sin perder. Se esquiva contestando rápido y mal.',
  'Asking out loud something that cannot be answered without losing. It is dodged by answering fast and badly.'),
 ('El Elogio Envenenado', 'The Poisoned Compliment', 'Daño Social 2', 'Social Dmg 2', 'Esq: Difícil (−2)', 'Dodge: Hard (−2)',
  'Abs: Reputación', 'Soak: Reputation', D, D,
  'Alabarte en público justo por lo que te avergüenza. Protestar lo empeora: por eso la esquiva es difícil.',
  'Praising you in public for exactly what embarrasses you. Protesting makes it worse: hence the hard dodge.'),
 ('La Filtración', 'The Leak', 'Daño Social 2', 'Social Dmg 2', 'Esq: Nula', 'Dodge: None',
  'Abs: Nula', 'Soak: None', T('Permiso: lo privado') + ' se vuelve público', T('Permission: the private') + ' becomes public',
  'Lo que dijiste en confianza, en boca de todos. No hay reacción posible: ya está dicho.',
  'What you said in confidence, in everybody’s mouth. No reaction is possible: it has already been said.'),
 ('El Ultimátum Público', 'The Public Ultimatum', 'Daño Social 3', 'Social Dmg 3', 'Esq: Parcial', 'Dodge: Partial',
  'Abs: Reputación', 'Soak: Reputation', D, D,
  'Elige ahora y delante de todos. Aunque esquives, algo pierdes: por eso es Parcial.',
  'Choose now and in front of everybody. Even dodging, you lose something: hence Partial.'),
 ('La Deuda Recordada', 'The Debt Recalled', 'Daño Social 1', 'Social Dmg 1', 'Esq: Difícil (−2)', 'Dodge: Hard (−2)',
  'Abs: Total', 'Soak: Full', T('Permiso: un favor'), T('Permission: a favour'),
  'Te recuerdan en público lo que te dieron. Además del daño, te obliga a aceptar una petición o a quedar como un ingrato.',
  'They remind you in public of what they gave you. Besides the damage, you must accept a request or look ungrateful.'),
 ('El Desaire Calculado', 'The Calculated Snub', 'Daño Social 1', 'Social Dmg 1', 'Esq: Total', 'Dodge: Full',
  'Abs: Reputación', 'Soak: Reputation', D, D,
  'No saludarte. Barato, repetible y devastador si se hace delante de quien decide.',
  'Not greeting you. Cheap, repeatable and devastating if done in front of whoever decides.'),
 ('La Confesión Ajena', 'Somebody Else’s Confession', 'Daño Mental 2', 'Mental Dmg 2', 'Esq: Nula', 'Dodge: None',
  'Abs: Voluntad', 'Soak: Will', D, D,
  'Te cuentan algo que no querías saber, y a partir de ahora eres cómplice. Va a la Mental, no a la Social: no te quita reputación, te quita paz.',
  'They tell you something you did not want to know, and from now on you are an accomplice. It hits the Mental bar, not the Social one: it does not cost you reputation, it costs you peace.'),
]

TOON_ARMAS = [
 ('El Yunque Oportuno', 'The Timely Anvil', 'Daño 3', 'Dmg 3', 'Esq: Nula', 'Dodge: None', 'Abs: Nula', 'Soak: None', 0,
  'Cae desde arriba cuando hace gracia. No se esquiva porque no estaba ahí hasta que lo miraste.',
  'It falls from above whenever it is funny. It cannot be dodged because it was not there until you looked up.'),
 ('La Sartén', 'The Frying Pan', 'Daño 1', 'Dmg 1', 'Esq: Total', 'Dodge: Full', 'Abs: Nula', 'Soak: None', 0,
  'Suena como una campana y deja la cara marcada en el metal. La armadura no sirve: el ruido es el daño.',
  'It rings like a bell and leaves the face printed on the metal. Armour does not help: the sound is the damage.'),
 ('El Mazo de Feria', 'The Fairground Mallet', 'Daño 2', 'Dmg 2', 'Esq: Fácil (+2)', 'Dodge: Easy (+2)', 'Abs: Máx 1', 'Soak: Max 1', 0,
  'Enorme, lento y con un silbido que lo anuncia. Te aplana; a la escena siguiente ya estás bien.',
  'Huge, slow and with a whistle that announces it. It flattens you; by the next scene you are fine.'),
 ('La Caja de Cerillas Infinita', 'The Infinite Matchbox', 'Daño 1 (fuego)', 'Dmg 1 (fire)', 'Esq: Parcial', 'Dodge: Partial', 'Abs: Nula', 'Soak: None', 0,
  'Nunca se acaba, y de ella sale todo lo que quepa en una caja de cerillas, que es sorprendentemente mucho.',
  'It never runs out, and out of it comes anything that fits in a matchbox, which is surprisingly a lot.'),
 ('El Imán Gigante', 'The Giant Magnet', 'Daño 2', 'Dmg 2', 'Esq: Difícil (−2)', 'Dodge: Hard (−2)', 'Abs: Nula (Metal)', 'Soak: None (Metal)', 1,
  'Atrae todo el metal de la escena, incluidas las armas de tus amigos y las muelas de todo el mundo.',
  'It attracts every piece of metal in the scene, including your friends’ weapons and everybody’s fillings.'),
 ('La Pintura de Túnel', 'Tunnel Paint', D, D, D, D, D, D, 2,
  'Pintas un túnel en una pared y es un túnel. Solo funciona para quien lo pintó: los demás se dan contra el muro.',
  'You paint a tunnel on a wall and it is a tunnel. It only works for whoever painted it: everybody else hits the wall.'),
]

TOON_PODERES = [
 ('El Agujero Portátil', 'The Portable Hole', D, D, D, D, D, D,
  'Permiso: llevas un agujero doblado en el bolsillo y lo pones donde quieras. Una vez colocado, es un agujero de verdad.',
  'Permission: you carry a hole folded in your pocket and put it wherever you like. Once placed, it is a real hole.'),
 ('La Caída Diferida', 'The Delayed Fall', D, D, D, D, D, D,
  'Permiso: no caes hasta que miras abajo. Si nadie te lo recuerda, puedes cruzar un cañón andando.',
  'Permission: you do not fall until you look down. If nobody reminds you, you can walk across a canyon.'),
 ('El Disfraz Fino', 'The Thin Disguise', D, D, D, D, D, D,
  'Permiso: un bigote postizo te hace irreconocible para cualquiera, incluida tu madre y quien te esté persiguiendo.',
  'Permission: a fake moustache makes you unrecognisable to anyone, including your mother and whoever is chasing you.'),
 ('Los Patines Cohete', 'The Rocket Skates', 'Daño 2 (al chocar)', 'Dmg 2 (on impact)', 'Esq: Nula', 'Dodge: None', 'Abs: Máx 1', 'Soak: Max 1',
  'Permiso: velocidad absurda. La dirección no viene incluida, y el daño te lo llevas tú tan a menudo como el otro.',
  'Permission: absurd speed. Steering is not included, and you take the damage as often as they do.'),
 ('El Segundo de Más', 'The Extra Second', D, D, D, D, D, D,
  'Permiso: una acción extra por escena, hecha en el instante que hay entre que te caes y que tocas el suelo.',
  'Permission: one extra action per scene, taken in the moment between falling and hitting the ground.'),
]


def inserta(f, es, cab, filas):
    s = io.open(f, encoding='utf-8').read()
    i = s.find('<h4>' + cab)
    assert i > 0, (f, cab)
    j = s.find('</tbody>', i)
    s = s[:j] + filas + s[j:]
    io.open(f, 'w', encoding='utf-8').write(s)
    print('  +%d en %s (%s)' % (filas.count('<tr>'), cab, f))


L = lambda es, a, b: a if es else b
for f, es, cabs in (('frag_bazar.html', True, ('Arsenal social', 'Armas de tienda de bromas', 'Poderes toon')),
                    ('frag_bazar_b.en.html', False, ('Social arsenal', 'Joke-shop weapons', 'Cartoon powers'))):
    soc = ''.join(fila(L(es, x[0], x[1]), L(es, x[2], x[3]), L(es, x[4], x[5]), L(es, x[6], x[7]),
                       L(es, x[8], x[9]), L(es, x[10], x[11])) for x in SOCIAL)
    inserta(f, es, cabs[0], soc)
    arm = ''.join(fila(L(es, x[0], x[1]), L(es, x[2], x[3]), L(es, x[4], x[5]), L(es, x[6], x[7]),
                       T(('Acceso ' if es else 'Access ') + str(x[8])), L(es, x[9], x[10])) for x in TOON_ARMAS)
    inserta(f, es, cabs[1], arm)
    pod = ''.join(fila(L(es, x[0], x[1]), L(es, x[2], x[3]), L(es, x[4], x[5]), L(es, x[6], x[7]),
                       D, L(es, x[8], x[9])) for x in TOON_PODERES)
    inserta(f, es, cabs[2], pod)

# los recuentos del resumen
for f, subs in (('frag_bazar.html',
                 [('10. El Mundo Animado</td><td class="num">19', '10. El Mundo Animado</td><td class="num">30'),
                  ('El Duelo Social (extra)</td><td class="num">8', 'El Duelo Social (extra)</td><td class="num">16')]),
                ('frag_bazar_b.en.html',
                 [('10. The Animated World</td><td class="num">19', '10. The Animated World</td><td class="num">30'),
                  ('The Social Duel (extra)</td><td class="num">8', 'The Social Duel (extra)</td><td class="num">16')])):
    s = io.open(f, encoding='utf-8').read()
    for a, b in subs:
        print('  resumen:', s.count(a), a[:40])
        s = s.replace(a, b)
    io.open(f, 'w', encoding='utf-8').write(s)
