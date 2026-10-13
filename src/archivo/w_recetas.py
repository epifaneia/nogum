# -*- coding: utf-8 -*-
"""Bloque 4: el pase de las veinte recetas.
Cada una elige de verdad su tarjeta del cuadrante y trae su techo de Rejilla."""
import io, os, re, shutil
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# --- 1. arreglos de tarjeta: el remapeo mecanico dejo frases con la misma tarjeta dos veces
FIX_ES = [
    ('tono Épica (receta de referencia del capítulo 1: Mejor de 2d10, crítico con cualquier 10, pifia con doble 1) o Épica si se quiere aún más fiabilidad.',
     'tono Épica (la receta de referencia del capítulo 1: mejor de 2d10, TN 6, crítico con cualquier 10 y pifia con 1). Si quieres que limpiar la sala salga caro de vez en cuando, Pulp desenfrenado: los mismos dados, pero con éxito con coste y pifia ancha.'),
    ('el ámbito Arcano se llama aquí La Fuerza (Don para los usos innatos). Épica o Épica.',
     'el ámbito Arcano se llama aquí La Fuerza (Don para los usos innatos). Épica para la trilogía clásica; Pulp desenfrenado si tu mesa prefiere la cantina, las persecuciones y las facturas.'),
    ('Bola de nieve («Sí, pero te va a costar», con éxito parcial) o Bola de nieve si se quiere más ruleta.',
     'Bola de nieve («sí, pero te va a costar»: dado rojo, éxito con coste y bandas anchas). Si quieres que la ciudad sea injusta además de caótica, Pesadilla.'),
    ('Tono: Optimismo Neutro y Caos Alto (la tecnología falla), es decir, Bola de nieve o Bola de nieve.',
     'Tono: optimismo neutro y caos alto, porque la tecnología falla: Bola de nieve.'),
    ('«Optimismo Muy Bajo» es T6 Tragedia (Caos Bajo: la muerte es lógica) o Pesadilla si se quiere algo de suerte.',
     '«Optimismo Muy Bajo» es <strong>Angustia</strong>, y es la única receta de las veinte que vive en la fila opresiva. Sus números son los del género: 9 · 16 · 25 · 36 · 49 · 64 · 81 por ciento según tu bono, el mismo reparto que separa al profano del especialista en los manuales de la Llamada. Para una noche de locura pura, Pesadilla.'),
    ('Épica o Épica. El monstruo está un nivel por encima',
     'Épica, o Primera marcha si quieres que el instituto pese tanto como el monstruo. El monstruo está un nivel por encima'),
    ('el tono es Bola de nieve (Bola de nieve: Optimismo Neutro, Caos Alto)',
     'el tono es Bola de nieve (optimismo neutro, caos alto)'),
    ('T6 Tragedia', 'Tragedia'),
    ('T6 Tragedia (Caos Bajo) y rejilla mística inversa (saber = locura).',
     'Angustia (peor de 2d10 con bandas estrechas) y rejilla mística inversa (saber = locura).'),
]
FIX_EN = [
    ('In canon: Epic tone (the reference recipe from chapter 1: Best of 2d10, critical on any 10, fumble on double 1) or Epic for even more reliability.',
     'In canon: Epic tone (the reference recipe from chapter 1: best of 2d10, TN 6, critical on any 10 and fumble on a 1). If you want clearing the room to come at a price now and then, Unleashed Pulp: the same dice, but with success at a cost and a wide fumble band.'),
    ('the Arcane sphere is called The Force here (Gift for innate uses). Epic or Epic.',
     'the Arcane sphere is called The Force here (Gift for innate uses). Epic for the classic trilogy; Unleashed Pulp if your table prefers the cantina, the chases and the bills.'),
    ('T3 Pulp/Drama (“Yes, but it’s going to cost you”, with partial success) or Snowball for more of a roulette.',
     'Snowball (“yes, but it’s going to cost you”: red die, success at a cost and wide bands). If you want the city to be unfair as well as chaotic, Nightmare.'),
    ('Tone: Neutral Optimism and High Chaos (technology fails), in other words T3 Pulp/Drama or Snowball.',
     'Tone: neutral optimism and high chaos, because the technology fails: Snowball.'),
    ('“Very Low Optimism” is T6 Tragedy (Low Chaos: death is logical) or Nightmare if you want a bit of luck.',
     '“Very Low Optimism” is <strong>Anguish</strong>, and it is the only one of the twenty recipes that lives on the oppressive row. Its numbers are the genre’s own: 9 · 16 · 25 · 36 · 49 · 64 · 81 per cent depending on your bonus, the same spread that separates the layman from the specialist in the Call rulebooks. For a night of pure madness, Nightmare.'),
    ('Epic or Epic. The monster is one level above',
     'Epic, or First Gear if you want school to weigh as much as the monster. The monster is one level above'),
    ('the tone is Snowball (Snowball: Neutral Optimism, High Chaos)',
     'the tone is Snowball (neutral optimism, high chaos)'),
    ('T6 Tragedy', 'Tragedy'),
    ('T6 Tragedy (Low Chaos) and the inverse mystic grid (knowing = madness).',
     'Anguish (worst of 2d10 with narrow bands) and the inverse mystic grid (knowing = madness).'),
]

# --- 2. techos de Rejilla, receta a receta: (Fis, Men, Soc, Tec, Arc, nota ES, nota EN)
TECHOS = [
 ('3','2','3','2','4', 'El arquimago llega a magia de asedio; el guerrero, a limpiar un barrio.',
                        'The archmage reaches siege magic; the fighter, clearing a district.'),
 ('2','2','3','2','3', 'Nadie es grande aquí. La magia es lo único que rompe el techo, y te corrompe al hacerlo.',
                        'Nobody is big here. Magic is the only thing that breaks the ceiling, and it corrupts you as it does.'),
 ('2','2','3','2','4', 'Los magos del mundo son antiguos y pocos; el resto sois gente andando.',
                        'The world’s wizards are ancient and few; the rest of you are people walking.'),
 ('2','2','4','2','3', 'El techo alto es el social: una frase bien dicha mueve una provincia.',
                        'The high ceiling is the social one: one well-placed sentence moves a province.'),
 ('2','2','3','2','—', 'Sin magia y sin techos altos: todo el espectáculo cabe en el nivel 2.',
                        'No magic and no high ceilings: the whole spectacle fits inside level 2.'),
 ('2','1','2','1','2', 'El techo general es 2, como pide la receta: aquí lo que crece es el destino, no el personaje.',
                        'The general ceiling is 2, as the recipe asks: what grows here is destiny, not the character.'),
 ('3','2','4','3','4', 'El maestro de la Fuerza llega a 4; el contrabandista, a 2 con su nave.',
                        'The Force master reaches 4; the smuggler, 2 with his ship.'),
 ('2','1','4','2','—', 'El techo que define el género: el cromado llega a Físico 2 y ahí se acaba, el ingenio no pasa de 1 por mucho implante, y el hacker toca el nivel 3 solo con una Llave.',
                        'The ceiling that defines the genre: the chrome job reaches Physical 2 and that is that, wits never pass 1 however many implants, and the hacker touches level 3 only with a Key.'),
 ('3','3','3','4','—', 'El cuerpo es equipo: el techo físico lo pone la funda que puedas pagar.',
                        'The body is equipment: the physical ceiling is set by the sleeve you can afford.'),
 ('2','1','2','2','2', 'Mundo pequeño y mezquino. Lo que sube no es la Rejilla: es la gasolina.',
                        'A small, mean world. What goes up is not the Grid: it is the petrol.'),
 ('2','2','3','3','3', 'Los dragones corporativos son de nivel 4–5 en Social, pero son PNJ: tu techo es 3.',
                        'The corporate dragons are level 4–5 in Social, but they are NPCs: your ceiling is 3.'),
 ('1','1','2','1','1', 'Todo el mundo es nivel 1 y así se queda. Por eso los dioses son decorado y no se tira contra ellos.',
                        'Everyone is level 1 and stays there. That is why the gods are scenery and you do not roll against them.'),
 ('2','2','4','1','3', 'La Generación es el techo: neonato 1, príncipe 3. El 5 existe en el mundo y duerme debajo de la ciudad.',
                        'Generation is the ceiling: neonate 1, prince 3. The 5 exists in the world and sleeps under the city.'),
 ('1','1','1','1','—', 'Todos a 1, sin excepciones: ese es el chiste y ese es el terror. El monstruo está en 3.',
                        'Everyone at 1, no exceptions: that is the joke and that is the horror. The monster sits at 3.'),
 ('2','1','2','1','2', 'El instituto es nivel 1; lo que sube de nivel son los monstruos, y por eso hacen falta Llaves.',
                        'School is level 1; what goes up a level are the monsters, which is why Keys are needed.'),
 ('2','1','3','2','2', 'La banda sube de nivel social con cada golpe: el techo 3 es la ciudad entera a tus pies.',
                        'The crew climbs the social ladder with every score: ceiling 3 is the whole city at your feet.'),
 ('5','5','4','5','5', 'La excepción: aquí el 5 es la línea de salida, no el final de campaña.',
                        'The exception: here level 5 is the starting line, not the end of the campaign.'),
 ('5','2','2','2','5', 'Lo físico y el ki no tienen techo práctico; todo lo demás sigue siendo gente normal gritando.',
                        'Physical and ki have no practical ceiling; everything else is still ordinary people shouting.'),
 ('4','1','2','3','—', 'Dos techos en la misma ficha: 1 fuera del robot, 4 dentro. Eso es la Sincronización.',
                        'Two ceilings on the same sheet: 1 outside the robot, 4 inside. That is Synchronisation.'),
 ('1','1','2','2','2', 'Nadie pasa de 1 en lo que importa, y el Ordenador está en 5. Ese desnivel es el chiste.',
                        'Nobody passes 1 at what matters, and the Computer sits at 5. That gap is the joke.'),
 ('2','2','3','2','3', 'Magia nuclear e inestable con techo 3: lo justo para que el chiste tenga consecuencias.',
                        'Nuclear, unstable magic with a ceiling of 3: just enough for the joke to have consequences.'),
]

LAB_ES = ('<p class="recipe-grid"><strong>Techos de Rejilla</strong> '
          '<span class="small">(Fís · Men · Soc · Téc · Arc)</span>: <strong>%s</strong>. %s</p>')
LAB_EN = ('<p class="recipe-grid"><strong>Grid ceilings</strong> '
          '<span class="small">(Phy · Men · Soc · Tec · Arc)</span>: <strong>%s</strong>. %s</p>')

INTRO_ES = """<p><strong>Cada receta trae su techo de Rejilla</strong> (<a href="#ch2-rejilla">2.4</a>): hasta dónde puede crecer un personaje en cada ámbito <em>en ese universo</em>, por mucho que dure la campaña. El nivel inicial lo pone la mesa; el techo lo pone el género, y es lo que hace que un mundo se sienta como ese mundo. La Llave es la excepción pactada al techo, y los PNJ legendarios pueden estar por encima: un techo de jugador no es un techo de mundo.</p>
"""
INTRO_EN = """<p><strong>Every recipe carries its Grid ceilings</strong> (<a href="#ch2-rejilla">2.4</a>): how far a character can grow in each sphere <em>in that universe</em>, however long the campaign runs. The starting level is set by the table; the ceiling is set by the genre, and it is what makes a world feel like that world. The Key is the agreed exception to the ceiling, and legendary NPCs can sit above it: a player ceiling is not a world ceiling.</p>
"""


def do(es):
    f = 'frag_cap8%s.html' % ('' if es else '.en')
    shutil.copyfile(f, f + '.bak_rec')
    s = io.open(f, encoding='utf-8').read()
    for a, b in (FIX_ES if es else FIX_EN):
        if a not in s:
            print('  no encontrado:', a[:60])
        s = s.replace(a, b)
    # el techo, dentro de cada ficha de receta
    parts, pos, i = [], 0, 0
    for m in re.finditer(r'<div class="recipe">.*?</div>', s, re.S):
        parts.append(s[pos:m.start()])
        blk = m.group(0)
        t = TECHOS[i]
        line = (LAB_ES if es else LAB_EN) % (' · '.join(t[:5]), t[5] if es else t[6])
        k = blk.rindex('</div>')
        parts.append(blk[:k] + line + '\n' + blk[k:])
        pos, i = m.end(), i + 1
    parts.append(s[pos:])
    s = ''.join(parts)
    print('  recetas con techo:', i)
    k = s.index('<h4>Bloque A' if es else '<h4>Block A')
    s = s[:k] + (INTRO_ES if es else INTRO_EN) + s[k:]
    io.open(f, 'w', encoding='utf-8').write(s)


do(True)
do(False)

css = io.open('paper.css', encoding='utf-8').read()
if 'recipe-grid' not in css:
    css += ('\n.recipe-grid{margin:6px 0 0;padding-top:6px;border-top:1px dotted var(--rule-2);'
            'font-size:.92em;color:var(--ink-2)}\n')
    io.open('paper.css', 'w', encoding='utf-8').write(css)
    print('css de los techos anadido')
