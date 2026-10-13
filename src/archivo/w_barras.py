# -*- coding: utf-8 -*-
"""Las tres barras: el nombre lo pone el genero, la barra la pone la causa.
La Humanidad es Espiritu en vampiro y Mente en cyberpunk, y eso hay que decirlo bien."""
import io, os, re, shutil
os.chdir(os.path.dirname(os.path.abspath(__file__)))

NUEVO_ES = r"""<h4>Las barras con nombre propio <span class="small">(y en cuál cae cada una)</span></h4>
<p>Casi todos los géneros rebautizan una barra: Corrupción, Humanidad, Sombra, Empatía, Honor, Sangre. Eso está bien y es lo que hace que una ficha huela a su mundo. Pero antes de ponerle nombre hay que saber <strong>de qué barra cuelga</strong>, porque de eso depende cómo se cura, qué penaliza y qué pasa al vaciarla.</p>
<div class="rule">
<p class="rule-title">El nombre lo pone el género; la barra la pone la causa</p>
<ul>
<li><strong>Cuerpo</strong> si lo que te gasta es físico: heridas, agotamiento, hambre, veneno, frío.</li>
<li><strong>Mente</strong> si lo que te gasta es cognitivo: cordura, estrés, voluntad, miedo, presión. Lo que se rompe es tu cabeza, y nadie más vive ahí dentro.</li>
<li><strong>Espíritu</strong> si lo que te gasta es sobrenatural: algo entra, algo se queda, algo te reclama. Lo que se rompe es lo que te ata a ser tú, y suele tener voluntad propia.</li>
</ul>
<p>El ejemplo que lo enseña todo es la <strong>Humanidad</strong>, que aparece con el mismo nombre y casi el mismo efecto en dos géneros, y <em>no cae en la misma barra</em>:</p>
<div class="tw"><table class="t">
<thead><tr><th>Género</th><th>Cómo se pierde la Humanidad</th><th class="num">Barra</th></tr></thead>
<tbody>
<tr><td><strong>Gótico</strong> (vampiros)</td><td>Hay una <strong>Bestia</strong> dentro de ti, y cada vez que cedes gana terreno. Es otro que no eres tú</td><td class="num">Espíritu</td></tr>
<tr><td><strong>Cyberpunk</strong></td><td>No hay nadie dentro: es tu propia cabeza dejando de reconocer a los demás. La ciberpsicosis es una locura, no una posesión</td><td class="num">Mente</td></tr>
</tbody></table></div>
<p>Misma palabra, mismo casi efecto, distinta barra. Y las consecuencias son distintas de verdad: al vampiro se le cura con rituales, redención y arcos, y al cromado con descanso, apoyo y terapia. Al vampiro se le va el personaje a manos del Director; al cromado le da una crisis y sale de la escena.</p>
<p><strong>Y si en tu mundo no hay Arcano, no hay barra Espiritual.</strong> No es que esté vacía: es que no existe, igual que el Ámbito. Lo que en otro sitio sería Espíritu —perderte a ti mismo para siempre— cae en Mente, y la mesa pacta en la sesión cero si esa barra puede retirar una ficha.</p>
</div>
<div class="tw"><table class="t">
<thead><tr><th>Nombre del género</th><th>Dónde se usa</th><th class="num">Barra</th><th>Por qué</th></tr></thead>
<tbody>
<tr><td><strong>Cordura</strong> · Estrés</td><td>Terror, guerra, cautiverio</td><td class="num">Mente</td><td>Es tu cabeza y nada más</td></tr>
<tr><td><strong>Empatía</strong> · Ciberpsicosis</td><td>Cyberpunk</td><td class="num">Mente</td><td>Dejas de reconocer a la gente; no hay nadie dentro</td></tr>
<tr><td><strong>Identidad</strong></td><td>Mentes digitales, cambios de cuerpo</td><td class="num">Mente</td><td>Lo que se borra es la memoria de ser tú</td></tr>
<tr><td><strong>Honor</strong> · Reputación</td><td>Samuráis, cortes, superhéroes</td><td class="num">Mente</td><td>Vive fuera, pero te rompe por dentro (ED-11)</td></tr>
<tr><td><strong>Humanidad</strong> · la Bestia</td><td>Gótico, licántropos</td><td class="num">Espíritu</td><td>Hay otro ahí dentro esperando turno</td></tr>
<tr><td><strong>Corrupción</strong></td><td>Fantasía oscura, magia que cobra</td><td class="num">Espíritu</td><td>Algo entra y se queda</td></tr>
<tr><td><strong>Sombra</strong></td><td>Fantasía melancólica de viaje</td><td class="num">Espíritu</td><td>El mal del mundo pesa sobre ti aunque no te toque</td></tr>
<tr><td><strong>Sangre</strong> · Hambre</td><td>Gótico</td><td class="num">Cuerpo</td><td>Es combustible: se gasta y se repone. No confundir con la Bestia</td></tr>
<tr><td><strong>Fatiga</strong> · Suministros</td><td>Supervivencia, viaje</td><td class="num">Cuerpo</td><td>El camino, que también mata</td></tr>
</tbody></table></div>

<h4>Lo que se pierde <span class="small">(tira o elige cuando se llene un bloque)</span></h4>
<p>Dos tablas, una por barra, porque no se pierde lo mismo cuando te rompes la cabeza que cuando algo te ocupa.</p>
<p><strong>Mente</strong> · cordura, empatía, identidad, honor</p>
<div class="tw"><table class="t">
<thead><tr><th class="num">1d6</th><th>Cordura <small>(terror)</small></th><th>Empatía <small>(cyberpunk)</small></th><th>Identidad <small>(mentes digitales)</small></th></tr></thead>
<tbody>
<tr><td class="num">1</td><td>No soportas un ruido concreto</td><td>Las caras se te olvidan</td><td>Un recuerdo tuyo es de otro</td></tr>
<tr><td class="num">2</td><td>Repasas la escena todas las noches</td><td>Dejas de notar el frío y el dolor leve</td><td>Tu acento cambia sin que lo decidas</td></tr>
<tr><td class="num">3</td><td>Cuentas, tocas madera o rezas antes de actuar</td><td>Hablas de la gente como de inventario</td><td>No reconoces tu letra</td></tr>
<tr><td class="num">4</td><td>Evitas el sitio donde pasó, aunque haya que pasar</td><td>Prefieres la pantalla a la mesa</td><td>Contestas a un nombre que no es el tuyo</td></tr>
<tr><td class="num">5</td><td>Una cosa te da un miedo que no puedes explicar</td><td>Un implante te responde antes de que lo pienses</td><td>Sabes hacer algo que nunca aprendiste</td></tr>
<tr><td class="num">6</td><td>Tu gente te nota raro y te lo dice</td><td>Tu gente deja de llamarte</td><td>Alguien te quiere y no sabes por qué</td></tr>
</tbody></table></div>
<p><strong>Espíritu</strong> · corrupción, la Bestia, sombra. <span class="small">Solo en mundos con Arcano.</span></p>
<div class="tw"><table class="t">
<thead><tr><th class="num">1d6</th><th>Corrupción <small>(fantasía oscura)</small></th><th>La Bestia <small>(gótico)</small></th><th>Sombra <small>(viaje melancólico)</small></th></tr></thead>
<tbody>
<tr><td class="num">1</td><td>Los animales te rehúyen</td><td>Tu reflejo tarda en seguirte</td><td>Ya no te alegran las canciones</td></tr>
<tr><td class="num">2</td><td>Algo tuyo cambia de color</td><td>No soportas un símbolo concreto</td><td>Caminas más rápido que el grupo y no esperas</td></tr>
<tr><td class="num">3</td><td>Los símbolos sagrados te molestan</td><td>El hambre llega antes de lo que debería</td><td>Hablas de lo que harás cuando todo esto acabe, y no te crees</td></tr>
<tr><td class="num">4</td><td>Sueñas con algo que no es tuyo</td><td>Pierdes una costumbre humana: comer, dormir, respirar al hablar</td><td>Guardas algo que deberías haber tirado</td></tr>
<tr><td class="num">5</td><td>Tu poder sale torcido una vez por escena</td><td>Alguien que te quería te tiene miedo</td><td>Oyes que te llaman por tu nombre desde lejos</td></tr>
<tr><td class="num">6</td><td>Alguien de fuera reconoce lo que te está pasando</td><td>Le pones nombre a lo que llevas dentro</td><td>Dejas de contar los días</td></tr>
</tbody></table></div>
<p>Al vaciarse la barra entera, lo que marca el capítulo 5: la Mente te saca de la escena —pánico, catatonia, crisis— y el Espíritu pone el personaje en manos del Director, <strong>y solo si se pactó</strong>. <span class="flag ed">ED-39</span></p>
"""

NUEVO_EN = r"""<h4>Bars with a name of their own <span class="small">(and which one each falls under)</span></h4>
<p>Almost every genre renames a bar: Corruption, Humanity, Shadow, Empathy, Honour, Blood. That is good, and it is what makes a sheet smell of its world. But before naming it you have to know <strong>which bar it hangs from</strong>, because that decides how it heals, what it penalises and what happens when it empties.</p>
<div class="rule">
<p class="rule-title">The genre gives the name; the cause gives the bar</p>
<ul>
<li><strong>Body</strong> if what wears you down is physical: wounds, exhaustion, hunger, poison, cold.</li>
<li><strong>Mind</strong> if what wears you down is cognitive: sanity, stress, will, fear, pressure. What breaks is your head, and nobody else lives in there.</li>
<li><strong>Spirit</strong> if what wears you down is supernatural: something gets in, something stays, something claims you. What breaks is whatever ties you to being yourself, and it usually has a will of its own.</li>
</ul>
<p>The example that teaches the whole thing is <strong>Humanity</strong>, which turns up with the same name and almost the same effect in two genres and <em>does not fall under the same bar</em>:</p>
<div class="tw"><table class="t">
<thead><tr><th>Genre</th><th>How Humanity is lost</th><th class="num">Bar</th></tr></thead>
<tbody>
<tr><td><strong>Gothic</strong> (vampires)</td><td>There is a <strong>Beast</strong> inside you, and every time you give in it gains ground. It is someone who is not you</td><td class="num">Spirit</td></tr>
<tr><td><strong>Cyberpunk</strong></td><td>Nobody is inside: it is your own head ceasing to recognise other people. Cyberpsychosis is a madness, not a possession</td><td class="num">Mind</td></tr>
</tbody></table></div>
<p>Same word, almost the same effect, different bar. And the consequences really do differ: the vampire heals with rituals, redemption and arcs, the chrome job with rest, support and therapy. The vampire’s character passes into the Director’s hands; the chrome job has a breakdown and leaves the scene.</p>
<p><strong>And if there is no Arcane in your world, there is no Spiritual bar.</strong> Not empty: non-existent, exactly like the Sphere. Whatever would be Spirit elsewhere —losing yourself for good— falls under Mind, and the table agrees in session zero whether that bar can retire a character.</p>
</div>
<div class="tw"><table class="t">
<thead><tr><th>The genre’s name</th><th>Where it is used</th><th class="num">Bar</th><th>Why</th></tr></thead>
<tbody>
<tr><td><strong>Sanity</strong> · Stress</td><td>Horror, war, captivity</td><td class="num">Mind</td><td>It is your head and nothing else</td></tr>
<tr><td><strong>Empathy</strong> · Cyberpsychosis</td><td>Cyberpunk</td><td class="num">Mind</td><td>You stop recognising people; nobody is inside</td></tr>
<tr><td><strong>Identity</strong></td><td>Digital minds, body swaps</td><td class="num">Mind</td><td>What gets erased is the memory of being you</td></tr>
<tr><td><strong>Honour</strong> · Reputation</td><td>Samurai, courts, superheroes</td><td class="num">Mind</td><td>It lives outside, but it breaks you inside (ED-11)</td></tr>
<tr><td><strong>Humanity</strong> · the Beast</td><td>Gothic, werewolves</td><td class="num">Spirit</td><td>There is someone else in there waiting their turn</td></tr>
<tr><td><strong>Corruption</strong></td><td>Dark fantasy, magic that charges</td><td class="num">Spirit</td><td>Something gets in and stays</td></tr>
<tr><td><strong>Shadow</strong></td><td>Melancholy journey fantasy</td><td class="num">Spirit</td><td>The world’s evil weighs on you even when it does not touch you</td></tr>
<tr><td><strong>Blood</strong> · Hunger</td><td>Gothic</td><td class="num">Body</td><td>It is fuel: it is spent and refilled. Not to be confused with the Beast</td></tr>
<tr><td><strong>Fatigue</strong> · Supplies</td><td>Survival, travel</td><td class="num">Body</td><td>The road, which also kills</td></tr>
</tbody></table></div>

<h4>What gets lost <span class="small">(roll or pick when a block fills)</span></h4>
<p>Two tables, one per bar, because you do not lose the same things when your head breaks as when something moves in.</p>
<p><strong>Mind</strong> · sanity, empathy, identity, honour</p>
<div class="tw"><table class="t">
<thead><tr><th class="num">1d6</th><th>Sanity <small>(horror)</small></th><th>Empathy <small>(cyberpunk)</small></th><th>Identity <small>(digital minds)</small></th></tr></thead>
<tbody>
<tr><td class="num">1</td><td>You cannot stand one particular noise</td><td>You forget faces</td><td>One of your memories belongs to someone else</td></tr>
<tr><td class="num">2</td><td>You replay the scene every night</td><td>You stop feeling cold and minor pain</td><td>Your accent changes without your deciding</td></tr>
<tr><td class="num">3</td><td>You count, touch wood or pray before acting</td><td>You talk about people like inventory</td><td>You do not recognise your own handwriting</td></tr>
<tr><td class="num">4</td><td>You avoid the place where it happened, even when you must pass</td><td>You prefer the screen to the table</td><td>You answer to a name that is not yours</td></tr>
<tr><td class="num">5</td><td>Something frightens you in a way you cannot explain</td><td>An implant answers before you think it</td><td>You know how to do something you never learned</td></tr>
<tr><td class="num">6</td><td>Your people notice something is off and say so</td><td>Your people stop calling</td><td>Somebody loves you and you do not know why</td></tr>
</tbody></table></div>
<p><strong>Spirit</strong> · corruption, the Beast, shadow. <span class="small">Only in worlds with an Arcane sphere.</span></p>
<div class="tw"><table class="t">
<thead><tr><th class="num">1d6</th><th>Corruption <small>(dark fantasy)</small></th><th>The Beast <small>(gothic)</small></th><th>Shadow <small>(melancholy journey)</small></th></tr></thead>
<tbody>
<tr><td class="num">1</td><td>Animals avoid you</td><td>Your reflection lags behind you</td><td>Songs no longer cheer you</td></tr>
<tr><td class="num">2</td><td>Something of yours changes colour</td><td>One particular symbol becomes unbearable</td><td>You walk faster than the group and do not wait</td></tr>
<tr><td class="num">3</td><td>Holy symbols bother you</td><td>The hunger arrives earlier than it should</td><td>You talk about what you will do when this is over, and you do not believe it</td></tr>
<tr><td class="num">4</td><td>You dream something that is not yours</td><td>You lose a human habit: eating, sleeping, breathing while you talk</td><td>You keep something you should have thrown away</td></tr>
<tr><td class="num">5</td><td>Your power comes out crooked once per scene</td><td>Somebody who loved you is afraid of you</td><td>You hear your name called from far away</td></tr>
<tr><td class="num">6</td><td>An outsider recognises what is happening to you</td><td>You give a name to what you carry inside</td><td>You stop counting the days</td></tr>
</tbody></table></div>
<p>When a whole bar empties, what chapter 5 says: the Mind takes you out of the scene —panic, catatonia, breakdown— and the Spirit puts the character in the Director’s hands, <strong>and only if it was agreed</strong>. <span class="flag ed">ED-39</span></p>
"""


def swap(f, nuevo, start, end):
    shutil.copyfile(f, f + '.bak_barras')
    s = io.open(f, encoding='utf-8').read()
    i = s.index(start)
    j = s.index(end, i)
    s = s[:i] + nuevo + s[j:]
    io.open(f, 'w', encoding='utf-8').write(s)
    print(' ', f, 'reemplazado', j - i, 'caracteres')


swap('frag_cap8.html', NUEVO_ES, '<h4>Lo que se pierde', '<h4>Fallos de equipo')
swap('frag_cap8.en.html', NUEVO_EN, '<h4>What gets lost', '<h4>Equipment failures')

# --- las recetas que colgaban de la barra equivocada
FIX = [
 ('frag_cap8.html',
  [('La barra Espiritual puede llamarse Empatía y resentirse con cada implante',
    'La barra <strong>Mental</strong> puede llamarse Empatía y resentirse con cada implante: la ciberpsicosis es una locura, no una posesión, y en este mundo no hay Arcano, así que no hay barra Espiritual'),
   ('El daño a la Identidad va a la barra Espiritual rebautizada',
    'El daño a la Identidad va a la barra <strong>Mental</strong> rebautizada como Identidad: lo que se borra es la memoria de ser tú, y aquí tampoco hay Arcano'),
   ('La Sangre es la barra Mental rebautizada (el estrés): se tachan casillas para activar Dones y, si se vacía, llega el frenesí',
    'Son dos barras distintas y conviene no mezclarlas: la <strong>Sangre</strong> es combustible y va en la barra Física (se tachan casillas para activar Dones y, si se vacía, llega el frenesí), mientras que la <strong>Humanidad</strong> es la Bestia y va en la Espiritual, porque ahí dentro hay alguien que no eres tú')]),
 ('frag_cap8.en.html',
  [('The Spiritual track can be called Empathy and suffer with every implant',
    'The <strong>Mental</strong> track can be called Empathy and suffer with every implant: cyberpsychosis is a madness, not a possession, and this world has no Arcane sphere, so it has no Spiritual bar'),
   ('Identity damage goes to the renamed Spiritual track',
    'Identity damage goes to the <strong>Mental</strong> track renamed Identity: what gets erased is the memory of being you, and there is no Arcane here either'),
   ('Blood is the renamed Mental track (stress): boxes are marked off to activate Gifts and, if it empties, frenzy arrives',
    'They are two different bars and are best not mixed: <strong>Blood</strong> is fuel and sits on the Physical bar (boxes are marked off to activate Gifts and, if it empties, frenzy arrives), while <strong>Humanity</strong> is the Beast and sits on the Spiritual one, because in there is somebody who is not you')]),
]
for f, subs in FIX:
    s = io.open(f, encoding='utf-8').read()
    for a, b in subs:
        n = s.count(a)
        print('   ', f, n, a[:46])
        s = s.replace(a, b)
    io.open(f, 'w', encoding='utf-8').write(s)
