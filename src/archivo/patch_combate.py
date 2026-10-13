# -*- coding: utf-8 -*-
"""Cierra el combate: empates a la defensa, pifia del defensor, Estilo sin coste y menú de la pifia."""
import io, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
MISS = []


def patch(fn, pairs):
    s = io.open(fn, encoding='utf-8').read()
    for a, b in pairs:
        if a not in s:
            MISS.append((fn, a[:70]))
            continue
        s = s.replace(a, b, 1)
    io.open(fn, 'w', encoding='utf-8').write(s)


# ---------------------------------------------------------------- 5.2 mitigación (ES)
MIT_ES_OLD = """<dt>Fallo</dt><dd>Te comes todo el daño.</dd>"""
MIT_ES_NEW = """<dt>Fallo</dt><dd>Te comes todo el daño.</dd>"""

patch('frag_ch5.html', [
    # la defensa gana los empates
    ('<p class="formula-line">Daño recibido = daño del arma (+1 si el atacante sacó crítico) − reducción del defensor, dentro de los límites de la ficha técnica.',
     '''<div class="rule"><p class="rule-title">La defensa gana los empates <span class="flag ed">ED-25</span></p>
<p>Los dos habéis tirado contra la misma TN, así que lo único que hay que mirar es <strong>quién llegó más arriba</strong>. No se comparan totales ni márgenes: se comparan niveles.</p>
<ul>
<li><strong>El defensor iguala o supera al atacante</strong> (los dos éxitos, los dos críticos, o el defensor por encima): no hay daño. La parada es perfecta.</li>
<li><strong>El atacante queda por encima</strong> y el defensor sacó éxito o éxito con coste: daño del arma <strong>−1</strong>.</li>
<li><strong>El defensor falla</strong>: daño completo.</li>
<li><strong>El defensor pifia</strong>: el ataque <strong>sube un escalón</strong> en la escala de la tarjeta activa, y después se comparan los niveles. Fallo pasa a éxito (o a éxito con coste en las tarjetas que lo llevan), y éxito pasa a crítico. El crítico es el techo: no sube más.</li>
</ul>
<p><strong>Las etiquetas mandan sobre el empate.</strong> Un arma con <span class="tag">Esq: Parcial</span> te deja comiendo al menos 1 punto aunque iguales, porque es un área, una ráfaga o fuego: no se esquiva del todo. Y con <span class="tag">Esq: Nula</span> ni siquiera hay reacción que tirar. Ahí está la diferencia entre un duelo y un tiroteo.</p>
<p><strong>Defensa con coste</strong> (en las tarjetas que la llevan): reduce como un éxito, −1, y además el DJ cobra un precio del menú de costes. Sales vivo, pero sueltas el arma, pierdes la posición o acabas donde no querías.</p>
<p><strong>Doble pifia:</strong> la pifia del atacante manda. El golpe no conecta igualmente —la del defensor solo lo sube a fallo— y los dos quedan en ridículo delante de quien estuviera mirando.</p></div>
<div class="rule"><p class="rule-title">El menú de la pifia</p>
<p>La pifia es un <strong>fallo bien feo</strong>: no sale, y además pasa algo. Cuánto duele lo decide la mesa y el tono, pero para no improvisar a pelo una de cada cinco tiradas en las tarjetas duras, aquí tienes seis puertas:</p>
<ol>
<li><strong>Se cierra un camino.</strong> La vía que estabas usando deja de estar disponible: la cerradura se traba, el contacto deja de fiarse, el puente cede.</li>
<li><strong>Se gasta algo que no se repone.</strong> La última carga, el último vial, el favor que te debían.</li>
<li><strong>Dejas un rastro.</strong> Alguien sabrá que estuviste ahí, y no en el buen sentido.</li>
<li><strong>La amenaza se acerca un paso.</strong> El reloj avanza, la patrulla dobla la esquina, el ritual llega a su siguiente verso.</li>
<li><strong>Se rompe lo que llevas.</strong> El arma, la herramienta, la radio. No siempre para siempre.</li>
<li><strong>Alguien se fija en ti.</strong> Y ahora tienes un problema con nombre propio.</li>
</ol>
<p>En la columna previsible, la pifia <strong>cierra una puerta</strong>: el camino que probaste ya no está. En la caótica, <strong>abre una rama</strong>: aparece algo nuevo que nadie había puesto ahí. Misma frecuencia, distinto tamaño.</p></div>
<p class="formula-line">Daño recibido = daño del arma (+1 si el atacante sacó crítico) − reducción del defensor, dentro de los límites de la ficha técnica.'''),
])

# ---------------------------------------------------------------- 5.2 mitigación (EN)
patch('frag_ch5.en.html', [
    ('<p class="formula-line">Damage taken = weapon damage',
     '''<div class="rule"><p class="rule-title">The defender wins ties <span class="flag ed">ED-25</span></p>
<p>Both of you rolled against the same TN, so all you have to look at is <strong>who got further up</strong>. Totals and margins are never compared: levels are.</p>
<ul>
<li><strong>The defender matches or beats the attacker</strong> (both successes, both criticals, or the defender above): no damage at all. A perfect parry.</li>
<li><strong>The attacker ends up above</strong> and the defender rolled a success or a success at a cost: weapon damage <strong>−1</strong>.</li>
<li><strong>The defender fails</strong>: full damage.</li>
<li><strong>The defender fumbles</strong>: the attack <strong>goes up one step</strong> on the active card’s ladder, and then the levels are compared. A failure becomes a success (or a success at a cost on the cards that carry it), and a success becomes a critical. The critical is the ceiling: it goes no higher.</li>
</ul>
<p><strong>Tags override the tie.</strong> A weapon with <span class="tag">Dodge: Partial</span> leaves you eating at least 1 point even when you match it, because it is an area, a burst or fire: it cannot be fully avoided. And with <span class="tag">Dodge: None</span> there is no reaction to roll at all. That is the difference between a duel and a gunfight.</p>
<p><strong>Defence at a cost</strong> (on the cards that carry it): it reduces like a success, −1, and the GM also charges a price from the cost menu. You walk away alive, but you drop the weapon, lose the position or end up where you did not want to be.</p>
<p><strong>Double fumble:</strong> the attacker’s fumble rules. The blow does not connect anyway —the defender’s only bumps it up to a failure— and both of them look ridiculous in front of whoever was watching.</p></div>
<div class="rule"><p class="rule-title">The fumble menu</p>
<p>A fumble is an <strong>ugly failure</strong>: it does not work, and something else happens too. How much it hurts is up to the table and the tone, but so that you are not improvising from scratch on one roll in five on the hard cards, here are six doors:</p>
<ol>
<li><strong>A route closes.</strong> The way you were using is no longer available: the lock jams, the contact stops trusting you, the bridge gives way.</li>
<li><strong>Something spends that does not come back.</strong> The last charge, the last vial, the favour they owed you.</li>
<li><strong>You leave a trace.</strong> Someone will know you were there, and not in the good way.</li>
<li><strong>The threat takes a step closer.</strong> The clock ticks on, the patrol turns the corner, the ritual reaches its next verse.</li>
<li><strong>What you are carrying breaks.</strong> The weapon, the tool, the radio. Not always for good.</li>
<li><strong>Someone notices you.</strong> And now you have a problem with a name.</li>
</ol>
<p>In the predictable column the fumble <strong>closes a door</strong>: the path you tried is gone. In the chaotic one it <strong>opens a branch</strong>: something new turns up that nobody had put there. Same frequency, different size.</p></div>
<p class="formula-line">Damage taken = weapon damage'''),
])

# ---------------------------------------------------------------- 4.5 B · Estilo (ES)
patch('frag_ch4.html', [
    ('<li><strong>La tirada de Estilo:</strong> tiras una vez con la tarjeta de tono activa + <strong>Estilo (+2)</strong>, para ver <em>cómo</em> ganas.</li>',
     '<li><strong>La tirada de Estilo:</strong> tiras una vez con la tarjeta de tono activa + <strong>Estilo (+2)</strong>, para ver <em>cómo</em> ganas. <strong>El Estilo nunca cuesta</strong>: en las tarjetas con éxito con coste, esa banda se lee aquí como éxito a secas. Se tira Estilo precisamente cuando ya no se puede fallar. <span class="flag ed">ED-26</span></li>'),
    ('<tr><td>Pifia</td><td>Aun así ganas, pero quedas <strong>mal</strong>. Los enemigos no pueden hacerte daño, pero tu propio ridículo puede causarte daño de estrés; depende de lo en serio que se tome el personaje a sí mismo (¡a lo mejor le hace gracia!).</td></tr>',
     '<tr><td>Pifia</td><td>Lo consigues, pero <strong>te ves ridículo</strong>. Ganas igual: eso nunca estuvo en duda. Lo que se te cae es la pose.</td></tr>'),
    ('<tr><td>Fallo</td><td>Ganas (eso nunca estuvo en duda), pero sin lucirte o de forma sucia: tropiezas, te manchas de sangre, tardas demasiado o rompes algo que no debías. Narra la escena con sobriedad.</td></tr>',
     '<tr><td>Fallo</td><td>Lo consigues <strong>de la forma más olvidable y anodina</strong>. Funciona, se acabó, y quizá nadie estaba mirando.</td></tr>'),
    ('<tr><td>Éxito</td><td>No solo vences: vences <strong>con estilo</strong>. Eficaz y limpio; piruetas y caras de asombro.</td></tr>',
     '<tr><td>Éxito</td><td><strong>Molas muchísimo.</strong> Eficaz y limpio, con piruetas y caras de asombro.</td></tr>'),
    ('<tr><td>Crítico</td><td>Sencillamente <strong>legendario</strong>. Coreografía de cine: impresionas a los presentes, eliminas a varios enemigos en una sola acción fluida, nacen rumores. Aplica todo el sabor que quieras.</td></tr>',
     '<tr><td>Crítico</td><td><strong>Lúcete.</strong> Describe tú la escena, y que sea inolvidable: coreografía de cine, varios enemigos en una sola acción fluida, rumores que nacen esa noche. Si encaja con lo que está pasando, el DJ puede darte además una ventaja temporal.</td></tr>'),
])
patch('frag_ch4.en.html', [
    ('<strong>The Style roll:</strong> you roll once with the active Tone Card + ',
     '<strong>The Style roll:</strong> <strong>Style never costs</strong>: on the cards with success at a cost, that band reads here as a plain success, because you roll Style precisely when you can no longer fail. <span class="flag ed">ED-26</span> You roll once with the active Tone Card + '),
    ('<tr><td>Fumble</td><td>You still win, but you look <strong>bad</strong>. The enemies cannot hurt you, but your own embarrassment can deal you stress damage; it depends on how seriously the character takes themselves (maybe they find it funny!).</td></tr>',
     '<tr><td>Fumble</td><td>You get there, but <strong>you look ridiculous</strong>. You win anyway: that was never in doubt. What you drop is the pose.</td></tr>'),
    ('<tr><td>Failure</td><td>You win (that was never in doubt), but without flair or in a messy way: you trip, get covered in blood, take too long or break something you shouldn’t have. Narrate the scene soberly.</td></tr>',
     '<tr><td>Failure</td><td>You get there in <strong>the most forgettable, unremarkable way</strong>. It works, that is all, and maybe nobody was even watching.</td></tr>'),
    ('<tr><td>Success</td><td>You don’t just win: you win <strong>with style</strong>. Effective and clean; pirouettes and astonished faces.</td></tr>',
     '<tr><td>Success</td><td><strong>You look magnificent.</strong> Effective and clean, with pirouettes and astonished faces.</td></tr>'),
    ('<tr><td>Critical</td><td>Simply <strong>legendary</strong>. Movie choreography: you impress everyone present, take out several enemies in a single fluid action, rumours are born. Add all the flavour you like.</td></tr>',
     '<tr><td>Critical</td><td><strong>Show off.</strong> You describe the scene, and make it unforgettable: movie choreography, several enemies in one fluid action, rumours born that night. If it fits what is happening, the GM may also hand you a temporary advantage.</td></tr>'),
])

print('faltan:', MISS if MISS else 'nada')
