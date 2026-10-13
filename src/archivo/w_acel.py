# -*- coding: utf-8 -*-
"""Bloque 5: el Acelerado se lo lleva todo. 12/14 puntos, bote aparte, Llaves y el x100."""
import io, os, re, shutil
os.chdir(os.path.dirname(os.path.abspath(__file__)))

R = [
 # --- puntos
 ('<p>Tienes <strong>10 puntos</strong>. Cada punto sube un escalón en una rama, y para subir un escalón hay que haber pagado el anterior:',
  '<p>Tienes <strong>12 puntos</strong>, o <strong>14</strong> si tu mundo tiene Arcano (son diez casillas más que cubrir). Cada punto sube un escalón en una rama, y para subir un escalón hay que haber pagado el anterior:'),
 ('<p>You have <strong>10 points</strong>. Each point climbs one rung of a branch, and to climb a rung you must have paid for the one below:',
  '<p>You have <strong>12 points</strong>, or <strong>14</strong> if your world has an Arcane sphere (that is ten more slots to cover). Each point climbs one rung of a branch, and to climb a rung you must have paid for the one below:'),
 # --- hoja
 ('<tr><td>Puntos gastados</td><td>__ / 10</td></tr>',
  '<tr><td>Puntos gastados</td><td>__ / 12 (14 si hay Arcano)</td></tr>\n'
  '<tr><td>Bote aparte</td><td>+1 nivel de Rejilla en un ámbito <strong>o</strong> 5 Llaves. No se cambia por puntos.</td></tr>'),
 ('<tr><td>Points spent</td><td>__ / 10</td></tr>',
  '<tr><td>Points spent</td><td>__ / 12 (14 if there is an Arcane sphere)</td></tr>\n'
  '<tr><td>Separate pot</td><td>+1 Grid level in one sphere <strong>or</strong> 5 Keys. It does not trade for points.</td></tr>'),
 ('<tr><td>Llaves</td><td>Qué te permite afectar a algo de nivel superior.</td></tr>',
  '<tr><td>Llaves</td><td>Cada una, con su objetivo escrito: una habilidad concreta para siempre, o un ámbito entero en una escena.</td></tr>'),
 ('<tr><td>Keys</td><td>What lets you affect something of a higher level.</td></tr>',
  '<tr><td>Keys</td><td>Each one with its target written down: one specific skill for ever, or a whole sphere for one scene.</td></tr>'),
 # --- pregenerados: de 10 a 12/14
 ('Cada uno gasta exactamente 10 puntos.',
  'Kira gasta 12 porque en su mundo no hay magia; los otros dos gastan 14. Cada uno usa además su bote aparte.'),
 ('Each one spends exactly 10 points.',
  'Kira spends 12 because there is no magic in her world; the other two spend 14. Each also uses their separate pot.'),
 # Kira
 ('<td>Vigor +1 → Armas +2 → Armas de fuego +4 · Destreza +1 → Acrobacia +2</td><td class="num">6</td>',
  '<td>Vigor +1 → Armas +2 → Armas de fuego +4 · Vigor → Entereza +2 · Destreza +1 → Acrobacia +2</td><td class="num">7</td>'),
 ('<td>Vigour +1 → Weapons +2 → Firearms +4 · Dexterity +1 → Acrobatics +2</td><td class="num">6</td>',
  '<td>Vigour +1 → Weapons +2 → Firearms +4 · Vigour → Fortitude +2 · Dexterity +1 → Acrobatics +2</td><td class="num">7</td>'),
 ('<td>Jerarquía +1 → Intimidación +2</td><td class="num">2</td>',
  '<td>Jerarquía +1 → Intimidación +2 · Jerarquía → Contactos +2</td><td class="num">3</td>'),
 ('<td>Hierarchy +1 → Intimidation +2</td><td class="num">2</td>',
  '<td>Hierarchy +1 → Intimidation +2 · Hierarchy → Contacts +2</td><td class="num">3</td>'),
 ('<p><strong>En mesa:</strong> dispara a +4 y esquiva bien, pero con cualquier aparato es una Nula (−2): si hay que abrir una puerta electrónica, que lo haga otro.</p>',
  '<p><strong>Bote aparte:</strong> 5 Llaves — «Armas de fuego contra drones», «Intimidación contra corredores» y tres sin gastar, para la sesión cero.</p>\n'
  '<p><strong>En mesa:</strong> dispara a +4 y esquiva bien, pero con cualquier aparato es una Nula (−2): si hay que abrir una puerta electrónica, que lo haga otro.</p>'),
 ('<p><strong>At the table:</strong> she shoots at +4 and dodges well, but with any kind of device she is Null (−2): if an electronic door needs opening, someone else does it.</p>',
  '<p><strong>Separate pot:</strong> 5 Keys — “Firearms against drones”, “Intimidation against runners” and three left unspent for session zero.</p>\n'
  '<p><strong>At the table:</strong> she shoots at +4 and dodges well, but with any kind of device she is Null (−2): if an electronic door needs opening, someone else does it.</p>'),
 # Tomas
 ('<td>Erudición +1 → Ocultismo +2 → Cultos y grimorios +3 · Erudición → Humanidades +2 · Ingenio +1 → Investigación +2 → Archivos y bibliotecas +3</td><td class="num">7</td>',
  '<td>Erudición +1 → Ocultismo +2 → Cultos y grimorios +3 · Erudición → Humanidades +2 · Erudición → Ciencias +2 · Ingenio +1 → Investigación +2 → Archivos y bibliotecas +3 · Ingenio → Alerta +2</td><td class="num">9</td>'),
 ('<td>Influencia +1 → Empatía +2</td><td class="num">2</td>',
  '<td>Influencia +1 → Empatía +2 · Influencia → Engaño +2 · Influencia → Persuasión +2</td><td class="num">4</td>'),
 ('<p><strong>En mesa:</strong> sabe más que nadie de lo que no debería existir, pero no puede tocarlo (Arcano vacío) y cualquier monstruo está por encima de su nivel. Su juego es encontrar Llaves.',
  '<p><strong>Bote aparte:</strong> 5 Llaves, que son su personaje entero — «Ocultismo contra los Profundos», «Investigación contra la secta», y tres por descubrir.</p>\n'
  '<p><strong>En mesa:</strong> sabe más que nadie de lo que no debería existir, pero no puede tocarlo (Arcano vacío) y cualquier monstruo está por encima de su nivel. Su juego es encontrar Llaves.'),
 # Ysolde
 ('<td>Don +1 → Proyección +2 → Fuego +4 · Don → Protección +2</td><td class="num">5</td>',
  '<td>Don +1 → Proyección +2 → Fuego +4 · Don → Protección +2 · Ritual +1 → Invocación +2</td><td class="num">7</td>'),
 ('<td>Erudición +1 → Ocultismo +2</td><td class="num">2</td>',
  '<td>Erudición +1 → Ocultismo +2 · Erudición → Humanidades +2</td><td class="num">3</td>'),
 ('<td>Influencia +1</td><td class="num">1</td>',
  '<td>Influencia +1 → Persuasión +2</td><td class="num">2</td>'),
 ('Nivel 2 en Arcano es una elección de ejemplo; por defecto, los personajes empiezan en nivel 1.',
  'Su nivel 2 en Arcano <strong>es su bote aparte</strong>: ha gastado ahí lo que los otros dos se gastan en Llaves. Por defecto, los personajes empiezan en nivel 1 en todo.'),
 # --- nombres viejos de tarjeta
 ('los de las tarjetas T1, T0 y T4 del manual completo',
  'los de las tarjetas Épica, Primera marcha y Pesadilla del manual completo'),
 ('those of cards T1, T0 and T4 in the complete rulebook',
  'those of the Epic, First Gear and Nightmare cards in the complete rulebook'),
]

LLAVE_ES = r"""<div class="rule"><p class="rule-title">Las Llaves se compran</p>
<ul>
<li>En la creación, el <strong>bote aparte</strong> te da <strong>5 Llaves</strong>, o <strong>+1 nivel de Rejilla</strong> en un ámbito. No se cambia por puntos de habilidad: todo el mundo llega con un oficio.</li>
<li>Cada Llave es <strong>una habilidad concreta para siempre</strong> («Armas contra los vampiros») o <strong>un ámbito entero durante una escena</strong>, si es muy específica. Se elige al comprarla y se escribe con su objetivo.</li>
<li>Para subir más contra la misma cosa: 1, 4, 9 Llaves. Con cinco en el bote, nadie empieza por encima de +2.</li>
<li>Durante la campaña, el Director da <strong>una Llave por sesión</strong>. Ese grifo es el mando de potencia de la partida: con Llaves se compra también el equipo que rompe la Rejilla.</li>
<li>Y lo que el Director te regala por una buena idea —«se te ocurre usar el agua bendita»— es una <strong>Llave prestada</strong>: dura una escena y no se apunta.</li>
</ul></div>
"""
LLAVE_EN = r"""<div class="rule"><p class="rule-title">Keys are bought</p>
<ul>
<li>At creation, the <strong>separate pot</strong> gives you <strong>5 Keys</strong>, or <strong>+1 Grid level</strong> in one sphere. It does not trade for skill points: everyone turns up with a trade.</li>
<li>Each Key is <strong>one specific skill for ever</strong> (“Weapons against vampires”) or <strong>a whole sphere for one scene</strong>, if it is very specific. You choose when you buy it, and you write down its target.</li>
<li>To climb further against the same thing: 1, 4, 9 Keys. With five in the pot, nobody starts above +2.</li>
<li>During the campaign the Director hands out <strong>one Key per session</strong>. That tap is the game’s power dial: Keys also buy the equipment that breaks the Grid.</li>
<li>And what the Director gives you for a good idea —“it occurs to you to use the holy water”— is a <strong>lent Key</strong>: it lasts one scene and is not written down.</li>
</ul>
"""

X100_ES = ('<p>Cada nivel multiplica por cien tu <strong>alcance</strong>: ×1 una persona, ×100 una sala, '
           '×10.000 un edificio, ×1.000.000 una ciudad, ×100.000.000 un país. Cuando alguien te saca un nivel '
           'no es que sea mejor que tú: es que juega con dos ceros más, y por eso no hay tirada.</p>\n')
X100_EN = ('<p>Each level multiplies your <strong>reach</strong> by a hundred: ×1 one person, ×100 a room, '
           '×10,000 a building, ×1,000,000 a city, ×100,000,000 a country. When someone has a level on you they '
           'are not better than you: they are playing with two more zeros, and that is why there is no roll.</p>\n')


def do(es):
    f = 'frag_acelerado%s.html' % ('' if es else '.en')
    shutil.copyfile(f, f + '.bak_llaves')
    s = io.open(f, encoding='utf-8').read()
    hit = 0
    for a, b in R:
        if a in s:
            s = s.replace(a, b, 1); hit += 1
    print(f, 'reemplazos:', hit)
    k = s.index('<p>Si no sabes qué nivel poner' if es else "<p>If you don't know which level")
    s = s[:k] + (X100_ES if es else X100_EN) + s[k:]
    anchor = '<aside class="meta"><p>¿Por qué Batman' if es else '<aside class="meta"><p>Why can Batman'
    k = s.index(anchor)
    s = s[:k] + (LLAVE_ES if es else LLAVE_EN) + s[k:]
    io.open(f, 'w', encoding='utf-8').write(s)


do(True)
do(False)
