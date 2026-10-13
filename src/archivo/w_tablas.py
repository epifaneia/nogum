# -*- coding: utf-8 -*-
"""Las tablas de problemas que las recetas invocaban y no existian.
Ejemplos por genero, no un sistema exhaustivo."""
import io, os, shutil
os.chdir(os.path.dirname(os.path.abspath(__file__)))

ES = r"""<h3 id="ch8-tablas">Tablas de problemas</h3>
<p>Varias recetas del 8.4 mandan a estas tablas, así que aquí están. <strong>No son un sistema, son ejemplos</strong>: tiradas para cuando el Director quiere que el golpe deje algo y no se le ocurre qué. Ninguna es obligatoria, todas se pueden leer en vez de tirar, y la mitad no deberían estar en tu mesa: cada una lleva escrito para qué género es.</p>
<p>La regla que vale para todas: <strong>el problema no es un número, es algo que hacer</strong>. Si lo que sale no da juego esta noche, tira otra vez o coge el de al lado.</p>

<h4>Heridas graves <span class="small">(umbral 2 · todos los géneros, en dos sabores)</span></h4>
<p>Cuando se llena el segundo bloque de la barra Física (5.6). La columna que uses dice más de tu campaña que media sesión zero: la misma herida es una cicatriz interesante o tres semanas en cama.</p>
<div class="tw"><table class="t">
<thead><tr><th class="num">1d8</th><th>De aventura <small>(épica, pulp, acción)</small></th><th>Sucia <small>(realista, terror, grimdark)</small></th></tr></thead>
<tbody>
<tr><td class="num">1</td><td>Corte en la cara: sangra mucho y queda bien. Cicatriz permanente.</td><td>Hemorragia: cuenta atrás de tres turnos o alguien te cose.</td></tr>
<tr><td class="num">2</td><td>Brazo en cabestrillo el resto de la escena.</td><td>Brazo roto: una sola mano para todo, semanas.</td></tr>
<tr><td class="num">3</td><td>Cojeas aparatosamente; corres igual cuando hace falta.</td><td>Pierna inútil: alguien te arrastra o te quedas.</td></tr>
<tr><td class="num">4</td><td>Te quedas sin aire: pierdes el próximo turno.</td><td>Pulmón perforado: una frase por turno y toses sangre.</td></tr>
<tr><td class="num">5</td><td>Ves doble un rato: −2 a lo que exija puntería.</td><td>Conmoción: no recuerdas el orden de lo que acaba de pasar.</td></tr>
<tr><td class="num">6</td><td>Se te rompe lo que llevabas encima, no tú.</td><td>Herida que se infecta si no la tratan hoy.</td></tr>
<tr><td class="num">7</td><td>Quemadura vistosa: la ropa, el pelo, la ceja.</td><td>Quemadura de verdad: duele al moverte, −2 a todo lo físico.</td></tr>
<tr><td class="num">8</td><td>Te desmayas al final de la escena, cuando ya ha terminado.</td><td>Pierdes algo: un dedo, un ojo, el oído de un lado.</td></tr>
</tbody></table></div>

<h4>Enfermedad y agotamiento <span class="small">(supervivencia, histórico, viaje, asedio)</span></h4>
<p>Para campañas donde el enemigo es el camino. Se tira al final de una jornada dura, no en combate.</p>
<div class="tw"><table class="t">
<thead><tr><th class="num">1d6</th><th>Qué pasa</th><th>Hasta que…</th></tr></thead>
<tbody>
<tr><td class="num">1</td><td>Fiebre: −2 a todo lo Mental.</td><td>Dos noches de descanso de verdad.</td></tr>
<tr><td class="num">2</td><td>Disentería: no recuperas nada al descansar.</td><td>Agua limpia y tres días.</td></tr>
<tr><td class="num">3</td><td>Pies destrozados: el grupo avanza la mitad.</td><td>Alguien te cure o te carguen.</td></tr>
<tr><td class="num">4</td><td>Hambre: el primer bloque de la barra Física no se cura.</td><td>Una comida de verdad.</td></tr>
<tr><td class="num">5</td><td>Frío o insolación: −2 a lo Físico y mal humor.</td><td>Refugio, fuego o sombra.</td></tr>
<tr><td class="num">6</td><td>Contagias al que duerme a tu lado.</td><td>Os separéis, o os curéis los dos.</td></tr>
</tbody></table></div>

<h4>Locura y estrés <span class="small">(solo si tu campaña juega la barra Mental en serio)</span></h4>
<p>Terror, Cthulhu, guerra, cautiverio. <strong>Si tu mesa no quiere jugar esto, no lo juguéis</strong>: una tabla de locura es una herramienta de género, no una obligación, y hay mucha gente a la que estos temas le tocan de cerca. Se habla en la sesión cero y se quita sin pedir permiso.</p>
<div class="tw"><table class="t">
<thead><tr><th class="num">1d8</th><th>Lo que se rompe</th><th>Cómo se juega</th></tr></thead>
<tbody>
<tr><td class="num">1</td><td>Fijación</td><td>Solo ves la amenaza que te rompió. Lo demás te da igual hasta que la resuelvas.</td></tr>
<tr><td class="num">2</td><td>Mutismo</td><td>No hablas. Escribes, señalas, o te callas.</td></tr>
<tr><td class="num">3</td><td>Paranoia</td><td>No aceptas ayuda de nadie del grupo durante la escena.</td></tr>
<tr><td class="num">4</td><td>Ritual</td><td>Tienes que hacer algo —contar, tocar madera, rezar— antes de cada acción arriesgada.</td></tr>
<tr><td class="num">5</td><td>Huida</td><td>Tu primera reacción a cualquier sorpresa es poner distancia.</td></tr>
<tr><td class="num">6</td><td>Negación</td><td>Lo que has visto no ha pasado. Lo cuentas de otra manera, y te lo crees.</td></tr>
<tr><td class="num">7</td><td>Disociación</td><td>Narras en tercera persona. Tu cuerpo te importa menos de lo que debería.</td></tr>
<tr><td class="num">8</td><td>Un día bueno</td><td>Hoy no. Hoy aguantas, y la mesa lo nota más que si te hubieras roto.</td></tr>
</tbody></table></div>

<h4>Lo que se pierde <span class="small">(la barra Espiritual, con el nombre de cada género)</span></h4>
<p>La misma barra se llama distinto según dónde juegues, y lo que se pierde al vaciarla también. Tira o elige cuando se llene un bloque.</p>
<div class="tw"><table class="t">
<thead><tr><th class="num">1d6</th><th>Corrupción <small>(fantasía oscura)</small></th><th>Empatía <small>(cyberpunk)</small></th><th>La Bestia <small>(gótico)</small></th></tr></thead>
<tbody>
<tr><td class="num">1</td><td>Los animales te rehúyen</td><td>Las caras se te olvidan</td><td>Tu reflejo tarda en seguirte</td></tr>
<tr><td class="num">2</td><td>Algo tuyo cambia de color</td><td>Dejas de notar el frío y el dolor leve</td><td>No soportas un símbolo concreto</td></tr>
<tr><td class="num">3</td><td>Los símbolos sagrados te molestan</td><td>Hablas de la gente como de inventario</td><td>El hambre llega antes de lo que debería</td></tr>
<tr><td class="num">4</td><td>Sueñas con algo que no es tuyo</td><td>Prefieres la pantalla a la mesa</td><td>Pierdes una costumbre humana (comer, dormir, respirar al hablar)</td></tr>
<tr><td class="num">5</td><td>Tu poder sale torcido una vez por escena</td><td>Un implante te responde antes de que lo pienses</td><td>Alguien que te quería te tiene miedo</td></tr>
<tr><td class="num">6</td><td>Alguien de fuera reconoce lo que te está pasando</td><td>Tu gente deja de llamarte</td><td>Le pones nombre a lo que llevas dentro</td></tr>
</tbody></table></div>
<p>Al vaciarse la barra entera, lo que marca el capítulo 5: el personaje pasa a manos del Director, y <strong>solo si se pactó</strong>.</p>

<h4>Fallos de equipo <span class="small">(cyberpunk, postapocalíptico, steampunk)</span></h4>
<p>Para mundos donde las cosas están viejas o son demasiado nuevas. Se tira cuando la pifia afecta a un cacharro, no cada vez que se pifia.</p>
<div class="tw"><table class="t">
<thead><tr><th class="num">1d8</th><th>Qué le pasa al cacharro</th></tr></thead>
<tbody>
<tr><td class="num">1</td><td>Se encasquilla: una acción para arreglarlo.</td></tr>
<tr><td class="num">2</td><td>Se queda sin munición, carga o vapor, justo ahora.</td></tr>
<tr><td class="num">3</td><td>Funciona, pero hace un ruido que te delata.</td></tr>
<tr><td class="num">4</td><td>Pierde una etiqueta hasta que lo repares: la que más te dolía.</td></tr>
<tr><td class="num">5</td><td>Te quema, te corta o te da calambre: <span class="tag">Daño 1</span>.</td></tr>
<tr><td class="num">6</td><td>Se rompe del todo. Vale como chatarra o como pieza.</td></tr>
<tr><td class="num">7</td><td>Funciona de más: alcanza también a lo que no querías.</td></tr>
<tr><td class="num">8</td><td>Hace algo que no sabías que hacía. El Director decide qué.</td></tr>
</tbody></table></div>

<h4>Mutaciones y cambios del cuerpo <span class="small">(postapocalíptico, horror corporal, magia que cobra)</span></h4>
<p>No son premios ni castigos: son las dos cosas a la vez, que es de lo que va el género.</p>
<div class="tw"><table class="t">
<thead><tr><th class="num">1d8</th><th>El cambio</th><th>Lo que te da y lo que te cuesta</th></tr></thead>
<tbody>
<tr><td class="num">1</td><td>Piel dura</td><td>Absorbes 1 fijo · ya no pasas por humano de cerca</td></tr>
<tr><td class="num">2</td><td>Ojos de otro</td><td>Ves en la oscuridad · la luz fuerte te ciega</td></tr>
<tr><td class="num">3</td><td>Algo de más</td><td>Un permiso nuevo (agarrar, trepar, nadar) · no te vale la ropa ni el equipo</td></tr>
<tr><td class="num">4</td><td>Sangre rara</td><td>Los venenos no te hacen nada · tu sangre sí hace algo a los demás</td></tr>
<tr><td class="num">5</td><td>Voz nueva</td><td>+1 a intimidar · −2 a cualquier otra cosa social</td></tr>
<tr><td class="num">6</td><td>No duermes</td><td>No necesitas descansar · nunca recuperas la barra Mental del todo</td></tr>
<tr><td class="num">7</td><td>Creces</td><td>+1 a la potencia bruta · no cabes donde cabe el grupo</td></tr>
<tr><td class="num">8</td><td>Algo en la cabeza</td><td>Oyes lo que no se dice · no siempre es verdad</td></tr>
</tbody></table></div>
<p class="small">Las mutaciones con bono se compran como cualquier otra cosa que te hace mejor (el taller, en <a href="#bz-fabrica">8.3</a>): un punto por cada +1. Si el Director te la regala por la trama, es una lacra con premio y no cuesta nada: ya la estás pagando en la ficción.</p>
"""

EN = r"""<h3 id="ch8-tablas">Problem tables</h3>
<p>Several recipes in 8.4 point at these tables, so here they are. <strong>They are not a system, they are examples</strong>: rolls for when the Director wants the blow to leave something behind and cannot think what. None is compulsory, all of them can be read instead of rolled, and half of them should not be at your table: each one says which genre it is for.</p>
<p>The rule that covers all of them: <strong>a problem is not a number, it is something to do</strong>. If what comes up gives you nothing tonight, roll again or take the one next to it.</p>

<h4>Severe wounds <span class="small">(threshold 2 · every genre, in two flavours)</span></h4>
<p>When the second block of the Physical bar fills (5.6). Which column you use says more about your campaign than half a session zero: the same wound is either an interesting scar or three weeks in bed.</p>
<div class="tw"><table class="t">
<thead><tr><th class="num">1d8</th><th>Adventure <small>(epic, pulp, action)</small></th><th>Dirty <small>(realist, horror, grimdark)</small></th></tr></thead>
<tbody>
<tr><td class="num">1</td><td>Cut on the face: bleeds a lot and looks good. Permanent scar.</td><td>Bleeding: three-turn countdown or somebody stitches you.</td></tr>
<tr><td class="num">2</td><td>Arm in a sling for the rest of the scene.</td><td>Broken arm: one hand for everything, for weeks.</td></tr>
<tr><td class="num">3</td><td>You limp dramatically; you still run when it matters.</td><td>Useless leg: somebody drags you or you stay behind.</td></tr>
<tr><td class="num">4</td><td>Winded: you lose your next turn.</td><td>Punctured lung: one sentence per turn and you cough blood.</td></tr>
<tr><td class="num">5</td><td>You see double for a while: −2 to anything needing aim.</td><td>Concussion: you do not remember the order of what just happened.</td></tr>
<tr><td class="num">6</td><td>What you were carrying breaks, not you.</td><td>A wound that goes septic if untreated today.</td></tr>
<tr><td class="num">7</td><td>Showy burn: the clothes, the hair, the eyebrow.</td><td>A real burn: it hurts to move, −2 to anything physical.</td></tr>
<tr><td class="num">8</td><td>You pass out at the end of the scene, once it is over.</td><td>You lose something: a finger, an eye, the hearing on one side.</td></tr>
</tbody></table></div>

<h4>Disease and exhaustion <span class="small">(survival, historical, travel, siege)</span></h4>
<p>For campaigns where the enemy is the road. Rolled at the end of a hard day, not in combat.</p>
<div class="tw"><table class="t">
<thead><tr><th class="num">1d6</th><th>What happens</th><th>Until…</th></tr></thead>
<tbody>
<tr><td class="num">1</td><td>Fever: −2 to everything Mental.</td><td>Two nights of real rest.</td></tr>
<tr><td class="num">2</td><td>Dysentery: rest heals you nothing.</td><td>Clean water and three days.</td></tr>
<tr><td class="num">3</td><td>Ruined feet: the group moves at half speed.</td><td>Somebody heals you or carries you.</td></tr>
<tr><td class="num">4</td><td>Hunger: the first block of the Physical bar will not heal.</td><td>A real meal.</td></tr>
<tr><td class="num">5</td><td>Cold or sunstroke: −2 to the Physical and a foul mood.</td><td>Shelter, fire or shade.</td></tr>
<tr><td class="num">6</td><td>You infect whoever sleeps next to you.</td><td>You split up, or you both recover.</td></tr>
</tbody></table></div>

<h4>Madness and stress <span class="small">(only if your campaign plays the Mental bar seriously)</span></h4>
<p>Horror, Cthulhu, war, captivity. <strong>If your table does not want to play this, do not play it</strong>: a madness table is a genre tool, not an obligation, and these subjects hit close to home for plenty of people. You talk about it in session zero and you drop it without asking permission.</p>
<div class="tw"><table class="t">
<thead><tr><th class="num">1d8</th><th>What breaks</th><th>How it is played</th></tr></thead>
<tbody>
<tr><td class="num">1</td><td>Fixation</td><td>You only see the threat that broke you. Nothing else matters until you settle it.</td></tr>
<tr><td class="num">2</td><td>Mutism</td><td>You do not speak. You write, you point, or you stay quiet.</td></tr>
<tr><td class="num">3</td><td>Paranoia</td><td>You accept help from nobody in the group for the scene.</td></tr>
<tr><td class="num">4</td><td>Ritual</td><td>You have to do something —count, touch wood, pray— before every risky action.</td></tr>
<tr><td class="num">5</td><td>Flight</td><td>Your first reaction to any surprise is to put distance between you and it.</td></tr>
<tr><td class="num">6</td><td>Denial</td><td>What you saw did not happen. You tell it differently, and you believe it.</td></tr>
<tr><td class="num">7</td><td>Dissociation</td><td>You narrate in the third person. Your body matters to you less than it should.</td></tr>
<tr><td class="num">8</td><td>A good day</td><td>Not today. Today you hold, and the table notices it more than if you had broken.</td></tr>
</tbody></table></div>

<h4>What gets lost <span class="small">(the Spiritual bar, under each genre’s name)</span></h4>
<p>The same bar is called different things depending on where you play, and so is what you lose as it empties. Roll or pick when a block fills.</p>
<div class="tw"><table class="t">
<thead><tr><th class="num">1d6</th><th>Corruption <small>(dark fantasy)</small></th><th>Empathy <small>(cyberpunk)</small></th><th>The Beast <small>(gothic)</small></th></tr></thead>
<tbody>
<tr><td class="num">1</td><td>Animals avoid you</td><td>You forget faces</td><td>Your reflection lags behind you</td></tr>
<tr><td class="num">2</td><td>Something of yours changes colour</td><td>You stop feeling cold and minor pain</td><td>One particular symbol becomes unbearable</td></tr>
<tr><td class="num">3</td><td>Holy symbols bother you</td><td>You talk about people like inventory</td><td>The hunger arrives earlier than it should</td></tr>
<tr><td class="num">4</td><td>You dream something that is not yours</td><td>You prefer the screen to the table</td><td>You lose a human habit (eating, sleeping, breathing while you talk)</td></tr>
<tr><td class="num">5</td><td>Your power comes out crooked once per scene</td><td>An implant answers before you think it</td><td>Somebody who loved you is afraid of you</td></tr>
<tr><td class="num">6</td><td>An outsider recognises what is happening to you</td><td>Your people stop calling</td><td>You give a name to what you carry inside</td></tr>
</tbody></table></div>
<p>When the whole bar empties, what chapter 5 says: the character passes into the Director’s hands, and <strong>only if it was agreed</strong>.</p>

<h4>Equipment failures <span class="small">(cyberpunk, post-apocalyptic, steampunk)</span></h4>
<p>For worlds where things are either too old or too new. Rolled when the fumble hits a gadget, not every time somebody fumbles.</p>
<div class="tw"><table class="t">
<thead><tr><th class="num">1d8</th><th>What happens to the gadget</th></tr></thead>
<tbody>
<tr><td class="num">1</td><td>It jams: one action to clear it.</td></tr>
<tr><td class="num">2</td><td>Out of ammunition, charge or steam, right now.</td></tr>
<tr><td class="num">3</td><td>It works, but it makes a noise that gives you away.</td></tr>
<tr><td class="num">4</td><td>It loses a tag until repaired: the one you will miss most.</td></tr>
<tr><td class="num">5</td><td>It burns, cuts or shocks you: <span class="tag">Dmg 1</span>.</td></tr>
<tr><td class="num">6</td><td>It breaks for good. Worth scrap, or parts.</td></tr>
<tr><td class="num">7</td><td>It works too well: it also reaches what you did not want it to.</td></tr>
<tr><td class="num">8</td><td>It does something you did not know it did. The Director decides what.</td></tr>
</tbody></table></div>

<h4>Mutations and changes to the body <span class="small">(post-apocalyptic, body horror, magic that charges)</span></h4>
<p>They are neither rewards nor punishments: they are both at once, which is what the genre is about.</p>
<div class="tw"><table class="t">
<thead><tr><th class="num">1d8</th><th>The change</th><th>What it gives you and what it costs</th></tr></thead>
<tbody>
<tr><td class="num">1</td><td>Hard skin</td><td>You soak 1 fixed · you no longer pass for human up close</td></tr>
<tr><td class="num">2</td><td>Somebody else’s eyes</td><td>You see in the dark · bright light blinds you</td></tr>
<tr><td class="num">3</td><td>Something extra</td><td>A new permission (gripping, climbing, swimming) · clothes and gear no longer fit</td></tr>
<tr><td class="num">4</td><td>Strange blood</td><td>Poisons do nothing to you · your blood does something to everyone else</td></tr>
<tr><td class="num">5</td><td>A new voice</td><td>+1 to intimidate · −2 to anything else social</td></tr>
<tr><td class="num">6</td><td>You do not sleep</td><td>You need no rest · you never fully recover the Mental bar</td></tr>
<tr><td class="num">7</td><td>You grow</td><td>+1 to raw power · you do not fit where the group fits</td></tr>
<tr><td class="num">8</td><td>Something in your head</td><td>You hear what is not said · it is not always true</td></tr>
</tbody></table></div>
<p class="small">Mutations with a bonus are bought like anything else that makes you better (the workshop, in <a href="#bz-fabrica">8.3</a>): one point per +1. If the Director hands you one for the plot, it is a flaw with a prize and costs nothing: you are already paying for it in the fiction.</p>
"""

for f, txt, es in (('frag_cap8.html', ES, True), ('frag_cap8.en.html', EN, False)):
    shutil.copyfile(f, f + '.bak_tab')
    s = io.open(f, encoding='utf-8').read()
    k = s.index('<h3 id="ch8-skills">')
    s = s[:k] + txt + '\n' + s[k:]
    old_es = 'Nombradas; tablas sin escribir'
    old_en = 'Named; tables unwritten'
    s = s.replace(old_es, 'Escritas en «Tablas de problemas», aquí mismo')
    s = s.replace(old_en, 'Written in “Problem tables”, right here')
    a_es = 'El autor las nombra en sus recetas, pero aún no están escritas <span class="flag pending">Pendiente</span>'
    a_en = 'The author names them in his recipes, but they are not yet written <span class="flag pending">Pending</span>'
    s = s.replace(a_es, 'Escritas como ejemplos por género en «Tablas de problemas»')
    s = s.replace(a_en, 'Written as examples by genre in “Problem tables”')
    io.open(f, 'w', encoding='utf-8').write(s)
    print(' ', f, 'ok')
