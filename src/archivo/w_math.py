# -*- coding: utf-8 -*-
"""Bloque 6: la Sala de Maquinas aprende la economia de la ficha, y el glosario
suma las palabras nuevas (y corrige la que se quedo con la regla vieja)."""
import io, os, shutil
os.chdir(os.path.dirname(os.path.abspath(__file__)))

J_ES = r"""<h3 id="maq-economia">J. La economía de la ficha: puntos, Llaves y ceros</h3>
<p>Las tarjetas dicen cómo se tira. Esta sección dice <em>cuánto cuesta ser alguien</em>, que es la otra mitad del juego y suele estar peor pensada en los manuales que leemos.</p>

<h4>Por qué 12 y por qué 14</h4>
<p>La pirámide tiene cinco Ámbitos, cada uno con dos Dominios y ocho Disciplinas: <strong>diez casillas por Ámbito</strong>. Sin magia hay cuatro Ámbitos en juego, o sea cuarenta casillas; con magia, cincuenta.</p>
<div class="tw"><table class="t">
<thead><tr><th>Universo</th><th class="num">Casillas</th><th class="num">Puntos</th><th class="num">Cobertura</th></tr></thead>
<tbody>
<tr><td>Sin Arcano</td><td class="num">40</td><td class="num">12</td><td class="num">30 %</td></tr>
<tr><td>Con Arcano</td><td class="num">50</td><td class="num">14</td><td class="num">28 %</td></tr>
</tbody></table></div>
<p>Dos puntos más por diez casillas más mantienen la escasez casi idéntica. Ese es todo el misterio del 14: no es una recompensa por jugar con magia, es que la ficha ha crecido y había que pagar el alquiler.</p>

<h4>La anchura es barata y la libertad es cara</h4>
<p>El bote aparte ofrece dos monedas por el mismo precio, y no son equivalentes:</p>
<div class="tw"><table class="t">
<thead><tr><th>Compra</th><th class="num">Cubre</th><th class="num">Cuesta</th><th class="num">Por casilla</th></tr></thead>
<tbody>
<tr><td>+1 nivel de Rejilla en un Ámbito</td><td class="num">10</td><td class="num">5</td><td class="num">0,5</td></tr>
<tr><td>Una Llave</td><td class="num">1</td><td class="num">1</td><td class="num">1</td></tr>
</tbody></table></div>
<p><strong>La libertad se paga al doble.</strong> Y tiene su razón: la Rejilla te la marca el universo con su techo, mientras que la Llave la eliges tú y apunta a lo que a ti te importa. Hay además una propiedad bonita que sale sola de esos números: subir dos niveles contra <em>una sola cosa</em> cuesta 4 Llaves, y subir un nivel entero en <em>todo un Ámbito</em> cuesta 5. Hiperespecializarse cuesta casi lo mismo que ser grande en general, así que el sistema empuja a repartir sin prohibir al monstruo de un solo truco.</p>

<h4>Dos Grandes Maestros, y el tercero lo paga la tarjeta</h4>
<p>Un +4 cuesta cuatro puntos: Dominio 1, Disciplina 1, Firma 2. Cubrir los cuatro Ámbitos para no ser Nulidad en ninguno cuesta otros cuatro. Con doce puntos, la cuenta sale sola: <strong>dos Grandes Maestros y la espalda cubierta</strong>, o tres maestrías y un agujero de −2 en algún sitio.</p>
<p>Y aquí es donde el motor y la economía se tocan, que es lo que esta sección existe para enseñar. Lo que cuesta ese agujero <em>no lo decide la ficha</em>: lo decide la tarjeta, porque un −2 no vale lo mismo en todas.</p>
<div class="tw"><table class="t">
<thead><tr><th>Tarjeta</th><th class="num">Sale adelante con −2</th><th>Lo que significa el agujero</th></tr></thead>
<tbody>
<tr><td>Épica · Pulp desenfrenado</td><td class="num">51 %</td><td>Casi no duele: sigues sacando adelante la mitad</td></tr>
<tr><td>Realista</td><td class="num">36 %</td><td>Se nota, pero se vive</td></tr>
<tr><td>Primera marcha · Bola de nieve</td><td class="num">30 %</td><td>Un tercio: hay que evitar esas escenas</td></tr>
<tr><td>Angustia · Pesadilla</td><td class="num">9 %</td><td>Una sentencia: no vuelvas a intentarlo</td></tr>
</tbody></table></div>
<p>El mismo personaje de tres maestrías es una ganga en una campaña épica y un suicidio en una de Angustia. Ninguna regla de creación dice eso; lo dicen los dados.</p>

<h4>Las dos escaleras</h4>
<p>Subir contra una misma cosa cuesta, por defecto, <strong><em>n</em>²</strong> Llaves. La alternativa del manual es <strong>3<em>n</em>−2</strong>:</p>
<div class="tw"><table class="t">
<thead><tr><th>Subir</th><th class="num">Cuadrada (<em>n</em>²)</th><th class="num">Llana (3<em>n</em>−2)</th><th class="num">Alcance</th></tr></thead>
<tbody>
<tr><td>+1</td><td class="num">1</td><td class="num">1</td><td class="num">×100</td></tr>
<tr><td>+2</td><td class="num">4</td><td class="num">4</td><td class="num">×10<sup>4</sup></td></tr>
<tr><td>+3</td><td class="num">9</td><td class="num">7</td><td class="num">×10<sup>6</sup></td></tr>
<tr><td>+4</td><td class="num">16</td><td class="num">10</td><td class="num">×10<sup>8</sup></td></tr>
<tr><td>+5</td><td class="num">25</td><td class="num">13</td><td class="num">×10<sup>10</sup></td></tr>
</tbody></table></div>
<p>Coinciden en 1 y en 4, que es donde juega casi todo el mundo, y solo se separan cuando alguien va a por la divinidad. Puesto junto al ×100 de la Rejilla, lo que compras es esto: <strong>el alcance crece como 100<sup>n</sup> y el precio como <em>n</em>²</strong>. Es decir, el precio crece con el <em>cuadrado del logaritmo</em> de lo que consigues. Es un trato ridículamente bueno para el jugador, y es a propósito: la escena en la que un mortal mata a un dios tiene que ser posible. Lo que la frena no es el precio, es el monedero.</p>

<h4>El monedero de Llaves es el único grifo sin fondo</h4>
<p>Los puntos de habilidad saturan: el Ancla corta en +4, hay cincuenta casillas y a partir de cierto momento solo compras anchura. Las Llaves no saturan nunca, porque siempre hay otra Disciplina, otra escena y otro objeto del Bazar. A una Llave por sesión, en veinte sesiones el grupo ha movido veinte Llaves: cuatro niveles de Rejilla repartidos, o un +4 contra una sola cosa con cuatro de propina.</p>
<p>De ahí la frase que debería estar en la primera página de cualquier campaña larga: <strong>si quieres que la campaña escale, abre el grifo de las Llaves, no el de los puntos.</strong></p>
"""

J_EN = r"""<h3 id="maq-economia">J. The economy of the sheet: points, Keys and zeros</h3>
<p>The cards say how you roll. This section says <em>what it costs to be somebody</em>, which is the other half of the game and is usually worse thought out in the rulebooks we read.</p>

<h4>Why 12 and why 14</h4>
<p>The pyramid has five Spheres, each with two Domains and eight Disciplines: <strong>ten slots per Sphere</strong>. Without magic there are four Spheres in play, that is forty slots; with magic, fifty.</p>
<div class="tw"><table class="t">
<thead><tr><th>Universe</th><th class="num">Slots</th><th class="num">Points</th><th class="num">Coverage</th></tr></thead>
<tbody>
<tr><td>No Arcane</td><td class="num">40</td><td class="num">12</td><td class="num">30 %</td></tr>
<tr><td>With Arcane</td><td class="num">50</td><td class="num">14</td><td class="num">28 %</td></tr>
</tbody></table></div>
<p>Two more points for ten more slots keeps the scarcity almost identical. That is the whole mystery of the 14: it is not a reward for playing with magic, it is that the sheet grew and the rent had to be paid.</p>

<h4>Breadth is cheap and freedom is expensive</h4>
<p>The separate pot offers two coins at the same price, and they are not equivalent:</p>
<div class="tw"><table class="t">
<thead><tr><th>Purchase</th><th class="num">Covers</th><th class="num">Costs</th><th class="num">Per slot</th></tr></thead>
<tbody>
<tr><td>+1 Grid level in one Sphere</td><td class="num">10</td><td class="num">5</td><td class="num">0.5</td></tr>
<tr><td>One Key</td><td class="num">1</td><td class="num">1</td><td class="num">1</td></tr>
</tbody></table></div>
<p><strong>Freedom costs double.</strong> And there is a reason: the universe sets your Grid with its ceiling, whereas you choose the Key and it points at what matters to you. There is also a pretty property that falls out of those numbers: climbing two levels against <em>one single thing</em> costs 4 Keys, and climbing one whole level across <em>an entire Sphere</em> costs 5. Hyper-specialising costs almost the same as being big in general, so the system nudges you to spread out without forbidding the one-trick monster.</p>

<h4>Two Grand Masters, and the third one is paid for by the card</h4>
<p>A +4 costs four points: Domain 1, Discipline 1, Signature 2. Covering the four Spheres so as not to be Null anywhere costs another four. With twelve points the sum does itself: <strong>two Grand Masters with your back covered</strong>, or three masteries and a −2 hole somewhere.</p>
<p>And this is where the engine and the economy touch, which is what this section exists to show. What that hole costs you is <em>not decided by the sheet</em>: it is decided by the card, because a −2 is not worth the same on all of them.</p>
<div class="tw"><table class="t">
<thead><tr><th>Card</th><th class="num">Succeeds at −2</th><th>What the hole means</th></tr></thead>
<tbody>
<tr><td>Epic · Unleashed Pulp</td><td class="num">51 %</td><td>It barely hurts: you still pull off half of it</td></tr>
<tr><td>Realist</td><td class="num">36 %</td><td>You feel it, but you live with it</td></tr>
<tr><td>First Gear · Snowball</td><td class="num">30 %</td><td>A third: avoid those scenes</td></tr>
<tr><td>Anguish · Nightmare</td><td class="num">9 %</td><td>A death sentence: do not try again</td></tr>
</tbody></table></div>
<p>The same three-mastery character is a bargain in an epic campaign and suicide in an Anguish one. No creation rule says so; the dice do.</p>

<h4>The two ladders</h4>
<p>Climbing against the same thing costs, by default, <strong><em>n</em>²</strong> Keys. The rulebook’s alternative is <strong>3<em>n</em>−2</strong>:</p>
<div class="tw"><table class="t">
<thead><tr><th>Climb</th><th class="num">Square (<em>n</em>²)</th><th class="num">Flat (3<em>n</em>−2)</th><th class="num">Reach</th></tr></thead>
<tbody>
<tr><td>+1</td><td class="num">1</td><td class="num">1</td><td class="num">×100</td></tr>
<tr><td>+2</td><td class="num">4</td><td class="num">4</td><td class="num">×10<sup>4</sup></td></tr>
<tr><td>+3</td><td class="num">9</td><td class="num">7</td><td class="num">×10<sup>6</sup></td></tr>
<tr><td>+4</td><td class="num">16</td><td class="num">10</td><td class="num">×10<sup>8</sup></td></tr>
<tr><td>+5</td><td class="num">25</td><td class="num">13</td><td class="num">×10<sup>10</sup></td></tr>
</tbody></table></div>
<p>They agree at 1 and at 4, which is where almost everybody plays, and they only part company when someone goes for divinity. Set next to the Grid’s ×100, what you are buying is this: <strong>reach grows like 100<sup>n</sup> and the price like <em>n</em>²</strong>. That is, the price grows with the <em>square of the logarithm</em> of what you get. It is a ridiculously good deal for the player, and it is deliberate: the scene where a mortal kills a god has to be possible. What holds it back is not the price, it is the wallet.</p>

<h4>The Key wallet is the only bottomless tap</h4>
<p>Skill points saturate: the Anchor cuts off at +4, there are fifty slots, and past a certain point you are only buying breadth. Keys never saturate, because there is always another Discipline, another scene and another object in the Bazaar. At one Key per session, twenty sessions in the group has moved twenty Keys: four Grid levels spread around, or a +4 against one single thing with four to spare.</p>
<p>Hence the line that belongs on the first page of any long campaign: <strong>if you want the campaign to escalate, open the Key tap, not the points one.</strong></p>
"""

GLO_ES = r"""<dt>Bote aparte</dt><dd>Lo que recibe cada personaje además de sus 12 o 14 puntos: <strong>+1 nivel de Rejilla</strong> en un Ámbito, <strong>o</strong> 5 Llaves. No se cambia por puntos en ninguna dirección. <span class="note">La anchura cuesta media moneda por casilla y la libertad una entera: la libertad se paga al doble.</span></dd>
<dt>Llave propia</dt><dd>La que se compra y se escribe: una Disciplina para siempre, o un Ámbito entero durante una escena. Permanente y tuya.</dd>
<dt>Llave prestada</dt><dd>La que da el Director por la trama o por una buena idea. Dura una escena, no sube de nivel y no se apunta en la ficha.</dd>
<dt>Monedero</dt><dd>Cada una de las dos bolsas de experiencia: la de puntos de habilidad y la de Llaves. Crecen a ritmos distintos y no se mezclan. <span class="note">El de Llaves es el mando de potencia de la campaña.</span></dd>
<dt>Techo</dt><dd>Hasta dónde puede subir la Rejilla de un personaje en un Ámbito <em>en ese universo</em>. Lo pone el género, no la campaña, y la Llave es su excepción pactada.</dd>
<dt>Acceso</dt><dd>El nivel de Recursos que hace falta para que un objeto esté a tu alcance: 0 cotidiano, 1 arma seria, 2 material militar, 3 lo que no debería existir.</dd>
<dt>Escena</dt><dd>La unidad de tiempo de este juego. Dura lo que dura una situación con tensión propia: un duelo, un interrogatorio, el asalto entero a un castillo. El tono, el Estilo, la Llave ancha y el arma robada se miden todos en escenas.</dd>
<dt>Lacra</dt><dd>La cicatriz de un bloque lleno: lo que queda cuando se te llena la barra Mental o Espiritual y luego te curas. No tiene número, tiene consecuencias. <span class="note">Su gemela buena es el don, y tampoco se compra.</span></dd>
"""

GLO_EN = r"""<dt>Separate pot</dt><dd>What each character gets on top of their 12 or 14 points: <strong>+1 Grid level</strong> in one Sphere, <strong>or</strong> 5 Keys. It does not trade for points in either direction. <span class="note">Breadth costs half a coin per slot and freedom a whole one: freedom costs double.</span></dd>
<dt>Own Key</dt><dd>The one you buy and write down: one Discipline for ever, or a whole Sphere for one scene. Permanent and yours.</dd>
<dt>Lent Key</dt><dd>The one the Director gives you for the plot or for a good idea. It lasts one scene, does not go up a level and is not written on the sheet.</dd>
<dt>Wallet</dt><dd>Each of the two experience bags: skill points and Keys. They grow at different rates and do not mix. <span class="note">The Key one is the campaign’s power dial.</span></dd>
<dt>Ceiling</dt><dd>How far a character’s Grid can climb in a Sphere <em>in that universe</em>. It is set by the genre, not by the campaign, and the Key is its agreed exception.</dd>
<dt>Access</dt><dd>The level of Resources needed for an object to be within your reach: 0 everyday, 1 serious weapon, 2 military hardware, 3 what should not exist.</dd>
<dt>Scene</dt><dd>This game’s unit of time. It lasts as long as a situation with its own tension: a duel, an interrogation, the whole assault on a castle. Tone, Style, the wide Key and the looted weapon are all measured in scenes.</dd>
<dt>Flaw</dt><dd>The scar of a filled block: what is left when your Mental or Spiritual bar fills up and you later heal. It has no number, it has consequences. <span class="note">Its good twin is the gift, and that is not bought either.</span></dd>
"""


def do(es):
    f = 'frag_math%s.html' % ('' if es else '.en')
    shutil.copyfile(f, f + '.bak_econ')
    s = io.open(f, encoding='utf-8').read()
    k = s.index('<section class="chapter" id="apx-mates">')
    s = s[:k] + (J_ES if es else J_EN) + '\n' + s[k:]
    io.open(f, 'w', encoding='utf-8').write(s)

    f = 'frag_glosario%s.html' % ('' if es else '.en')
    shutil.copyfile(f, f + '.bak_econ')
    s = io.open(f, encoding='utf-8').read()
    k = s.rindex('</dl>')
    s = s[:k] + (GLO_ES if es else GLO_EN) + s[k:]
    bad_es = 'Ocupa la dificultad objetivo y el punto justo por debajo.'
    good_es = 'Ocupa la dificultad objetivo y el punto justo por encima (con TN 6, los totales 6 y 7).'
    bad_en = 'It occupies the target difficulty and the point just below it.'
    good_en = 'It occupies the target difficulty and the point just above it (with TN 6, totals 6 and 7).'
    if es:
        if bad_es in s:
            s = s.replace(bad_es, good_es); print('  glosario: corregido el exito con coste')
        else:
            print('  AVISO: no estaba la frase vieja del exito con coste (ES)')
    else:
        if bad_en in s:
            s = s.replace(bad_en, good_en); print('  glossary: cost fixed')
        else:
            print('  AVISO: frase del exito con coste no encontrada (EN)')
    io.open(f, 'w', encoding='utf-8').write(s)


do(True)
do(False)
print('sala de maquinas y glosario al dia')
