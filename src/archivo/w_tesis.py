# -*- coding: utf-8 -*-
"""La Tesis incorpora las dos ideas de nivel tesis que salieron de esta tanda:
el x100 como medida de la Vela, y quien es dueno de cada cambio."""
import io, os, shutil
os.chdir(os.path.dirname(os.path.abspath(__file__)))

ES_A = ('<li><strong>La Vela:</strong> la Rejilla de Potencia mide la escala de impacto '
        '(habitación, oficina, edificio, ciudad, nación). Por eso uno rompe una isla y el otro una mandíbula.</li>')
ES_B = ('<li><strong>La Vela:</strong> la Rejilla de Potencia mide la escala de impacto '
        '(habitación, oficina, edificio, ciudad, nación), y cada peldaño multiplica por cien tu alcance. '
        'Por eso uno rompe una isla y el otro una mandíbula: no es que sea mejor, es que juega con dos ceros más.</li>')

ES_C = ('<li>La <strong>Llave</strong> es la excepción narrativa que permite tocar un nivel superior: '
        'la kriptonita, el guerrero dormido tras el festín, mil hackers coordinados.</li>')
ES_D = (ES_C + '\n<li><strong>El universo pone el techo; la Llave es la excepción que se compra.</strong> '
        'Un techo sin excepciones aburre y una excepción sin techo rompe el juego. Por eso en una partida '
        'cyberpunk no existe un ingenio por cien, pero sí existe el exploit que funciona contra <em>esa</em> IA.</li>')

ES_DUENOS = """
<section class="chapter" id="es-duenos">
<h2>5bis · Quién es dueño de cada cambio</h2>
<ul>
<li>Casi todos los juegos meten en el mismo saco de puntos tres cosas que no se parecen en nada, y por eso el guerrero de nivel quince es a la vez más hábil, más poderoso en el mundo y más curtido: solo hay un contador.</li>
<li>Aquí se separan y cada una tiene dueño. <strong>El mundo</strong> (la Rejilla) lo mueve el Director cuando los hechos lo justifican. <strong>Las cicatrices</strong> (dones y lacras) las pone la ficción: ocurren, no se compran. <strong>La competencia</strong> la decide la mesa, y son dos monederos distintos: puntos de habilidad y Llaves.</li>
<li>Y se nota en el ritmo, que es lo que de verdad define una campaña: los puntos solo te ensanchan, porque el Ancla los corta en +4; las Llaves abren equipo y rompen techos, y no saturan nunca. <strong>Si quieres que la campaña escale, abre el grifo de las Llaves, no el de los puntos.</strong></li>
<li>La consecuencia bonita: los personajes se ensanchan, el Director sube el mundo, y el desafío vuelve solo sin que nadie toque una tabla.</li>
</ul>
</section>
"""

EN_A = ('<li><strong>The Sail:</strong> the Power Grid measures the scale of impact '
        '(room, office, building, city, nation). That is why one breaks an island and the other a jaw.</li>')
EN_B = ('<li><strong>The Sail:</strong> the Power Grid measures the scale of impact '
        '(room, office, building, city, nation), and every rung multiplies your reach by a hundred. '
        'That is why one breaks an island and the other a jaw: not because he is better, but because he is '
        'playing with two more zeros.</li>')

EN_C = ('<li>The <strong>Key</strong> is the narrative exception that lets you touch a higher level: '
        'kryptonite, the warrior asleep after the feast, a thousand coordinated hackers.</li>')
EN_D = (EN_C + '\n<li><strong>The universe sets the ceiling; the Key is the exception you buy.</strong> '
        'A ceiling with no exceptions is boring and an exception with no ceiling breaks the game. That is why '
        'in a cyberpunk game there is no wits-times-a-hundred, but there is the exploit that works against '
        '<em>that</em> AI.</li>')

EN_DUENOS = """
<section class="chapter" id="en-owners" lang="en">
<h2>5bis · Who owns each kind of change</h2>
<ul>
<li>Almost every game throws three completely different things into the same bag of points, which is why the level fifteen fighter is at once more skilled, more powerful in the world and more scarred: there is only one counter.</li>
<li>Here they are separated and each has an owner. <strong>The world</strong> (the Grid) is moved by the Director when the facts justify it. <strong>The scars</strong> (gifts and flaws) are placed by the fiction: they happen, they are not bought. <strong>Competence</strong> is decided by the table, and it is two different wallets: skill points and Keys.</li>
<li>And it shows in the pacing, which is what really defines a campaign: points only make you wider, because the Anchor cuts them off at +4; Keys open up equipment and break ceilings, and they never saturate. <strong>If you want the campaign to escalate, open the Key tap, not the points one.</strong></li>
<li>The pretty consequence: the characters widen, the Director raises the world, and the challenge comes back on its own without anybody touching a table.</li>
</ul>
</section>
"""


def do(f, a, b, c, d, sec, after):
    shutil.copyfile(f, f + '.bak_llaves')
    s = io.open(f, encoding='utf-8').read()
    for x, y in ((a, b), (c, d)):
        if x not in s:
            print('  no encontrado en', f, ':', x[:50])
        s = s.replace(x, y)
    k = s.index(after)
    s = s[:k] + sec + s[k:]
    io.open(f, 'w', encoding='utf-8').write(s)
    print(' ', f, 'ok')


do('p3_tesis_es.html', ES_A, ES_B, ES_C, ES_D, ES_DUENOS, '<section class="chapter" id="es-accidente">')
do('p3_tesis_en.html', EN_A, EN_B, EN_C, EN_D, EN_DUENOS, '<section class="chapter" id="en-accident" lang="en">')
