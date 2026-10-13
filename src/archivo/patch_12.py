# -*- coding: utf-8 -*-
"""1.2 El Cuadrante: el mapa pasa a mostrar las siete tarjetas vivas y los dos huecos."""
import io, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

TABLA_ES = """<div class="tw"><table class="t grid-tonal">
<thead><tr><th></th><th>Previsible<br><small>El mundo se comporta</small></th><th>La costumbre<br><small>Ni ordena ni hace ruido</small></th><th>Caótico<br><small>Todo tiene un precio</small></th></tr></thead>
<tbody>
<tr><th>Optimista<br><small>El universo está de tu parte</small></th>
<td><strong>Épica</strong><br>El héroe es competente y el mundo es fiable. Sabes que vas a ganar; lo que no sabes es cómo de bien.<br><em>Superman, James Bond, D&amp;D clásico</em></td>
<td class="hueco"><em>Hueco.</em> Con un dado plano no hay forma de inclinar el tono sin mover la dificultad, y la dificultad no se toca. Coge la vecina que más se te parezca.</td>
<td><strong>Pulp desenfrenado</strong><br>Vas a ganar, pero será un caos de explosiones y planes locos que salen bien de milagro, y cada victoria deja factura.<br><em>Guardianes de la Galaxia, Indiana Jones</em></td></tr>
<tr><th>Neutral<br><small>El universo es justo</small></th>
<td><strong>Realista</strong><br>La vida misma: justa y predecible. Consecuencias lógicas y planes que funcionan.<br><em>Drama policial, novela histórica</em></td>
<td><strong>Primera marcha</strong><br>Riesgo real, consecuencias reales, sin red de seguridad. La partida de siempre.<br><em>Juego de Tronos</em></td>
<td><strong>Bola de nieve</strong><br>Todo puede pasar. Empieza con una tontería que nadie mira y acaba siendo un incendio con vida propia.<br><em>Twin Peaks, Fargo</em></td></tr>
<tr><th>Opresivo<br><small>El universo te pone a prueba</small></th>
<td><strong>Angustia</strong><br>La realidad es fría, lógica y constante, y te desgasta en silencio. La derrota no es un susto: es la cuesta.<br><em>1984, Chernóbil</em></td>
<td class="hueco"><em>Hueco.</em> Lo mismo por el otro lado del mapa: sin curva no hay manera de que el mundo te apriete sin tocar la dificultad.</td>
<td><strong>Pesadilla</strong><br>La amenaza es absurda y aleatoria. El miedo no viene del monstruo: viene de que nada se comporta.<br><em>Pesadilla en Elm Street</em></td></tr>
</tbody></table></div>"""

PARR_ES = """<p><strong>Los dos huecos son de verdad.</strong> En la columna de la costumbre el dado es plano, y sobre un dado plano la única forma de inclinar el tono sería mover la dificultad: justo la fricción que este juego promete quitarte (el porqué está en el <a href="#ch1-maquinas">1.3</a>). Si tu partida cae ahí, coge la vecina: la previsible si quieres que el mundo se comporte, la caótica si quieres que te cobre. Y si encuentras la regla que llena el hueco sin tocar la dificultad, has escrito una tarjeta nueva.</p>
<p>Las siete tienen sus reglas, sus tablas y sus porcentajes en el <a href="#ch1-panel">1.4</a>. Aquí todavía no hay números: solo el sitio donde quieres que vivan tus jugadores, o donde quieres que vivan <em>en esta escena concreta</em>.</p>"""

TABLA_EN = """<div class="tw"><table class="t grid-tonal">
<thead><tr><th></th><th>Predictable<br><small>The world behaves</small></th><th>The habit<br><small>Neither orders nor charges</small></th><th>Chaotic<br><small>Everything has a price</small></th></tr></thead>
<tbody>
<tr><th>Optimistic<br><small>The universe is on your side</small></th>
<td><strong>Epic</strong><br>The hero is competent and the world is reliable. You know you are going to win; what you do not know is how well.<br><em>Superman, James Bond, classic D&amp;D</em></td>
<td class="hueco"><em>Gap.</em> With a flat die there is no way to tilt the tone without moving the difficulty, and the difficulty is never moved. Take whichever neighbour is closest.</td>
<td><strong>Unleashed Pulp</strong><br>You are going to win, but it will be a mess of explosions and mad plans that work by a miracle, and every victory leaves a bill.<br><em>Guardians of the Galaxy, Indiana Jones</em></td></tr>
<tr><th>Neutral<br><small>The universe is fair</small></th>
<td><strong>Realist</strong><br>Life itself: fair and predictable. Logical consequences and plans that work.<br><em>Police drama, historical fiction</em></td>
<td><strong>First Gear</strong><br>Real risk, real consequences, no safety net. The usual game.<br><em>Game of Thrones</em></td>
<td><strong>Snowball</strong><br>Anything can happen. It starts as something nobody is watching and ends up a fire with a life of its own.<br><em>Twin Peaks, Fargo</em></td></tr>
<tr><th>Oppressive<br><small>The universe puts you to the test</small></th>
<td><strong>Anguish</strong><br>Reality is cold, logical and relentless, and it wears you down in silence. Defeat is not a scare: it is the slope.<br><em>1984, Chernobyl</em></td>
<td class="hueco"><em>Gap.</em> The same on the other side of the map: with no curve there is no way for the world to squeeze you without touching the difficulty.</td>
<td><strong>Nightmare</strong><br>The threat is absurd and random. The fear does not come from the monster: it comes from nothing behaving.<br><em>A Nightmare on Elm Street</em></td></tr>
</tbody></table></div>"""

PARR_EN = """<p><strong>The two gaps are real.</strong> In the habit column the die is flat, and on a flat die the only way to tilt the tone would be to move the difficulty: exactly the friction this game promises to take away (the why is in <a href="#ch1-maquinas">1.3</a>). If your game lands there, take a neighbour: the predictable one if you want the world to behave, the chaotic one if you want it to charge you. And if you find the rule that fills the gap without touching the difficulty, you have written a new card.</p>
<p>All seven have their rules, tables and percentages in <a href="#ch1-panel">1.4</a>. There are no numbers here yet: only the place where you want your players to live, or where you want them to live <em>in this particular scene</em>.</p>"""


def patch(fn, tabla, parrafo, viejo_ini, viejo_fin):
    s = io.open(fn, encoding='utf-8').read()
    i = s.index('<div class="tw"><table class="t grid-tonal">')
    j = s.index('</table></div>', i) + len('</table></div>')
    s = s[:i] + tabla + s[j:]
    if viejo_ini in s:
        a = s.index(viejo_ini)
        b = s.index(viejo_fin, a) + len(viejo_fin)
        s = s[:a] + parrafo + s[b:]
    else:
        k = s.index(tabla) + len(tabla)
        s = s[:k] + '\n' + parrafo + s[k:]
    io.open(fn, 'w', encoding='utf-8').write(s)


patch('frag_ch1a.html', TABLA_ES, PARR_ES,
      '<p><strong>Dos de estos nueve géneros no tienen tarjeta propia.</strong>', 'es tuya.</p>')
patch('frag_ch1a.en.html', TABLA_EN, PARR_EN, '@@nada@@', '@@nada@@')
print('1.2 actualizado')
