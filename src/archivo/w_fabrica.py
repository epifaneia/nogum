# -*- coding: utf-8 -*-
"""El taller: como se fabrica lo que no esta en la lista. Va delante del catalogo."""
import io, os, shutil
os.chdir(os.path.dirname(os.path.abspath(__file__)))

ES = r"""<h3 id="bz-taller">El taller: cómo se fabrica lo que no está en la lista</h3>
<p>Ninguna lista de objetos es suficiente, y menos en un manual universal. Así que antes del catálogo va la fábrica: con estas cuatro páginas puedes poner precio a cualquier cosa que se os ocurra, y el catálogo pasa a ser lo que de verdad es, <strong>una tabla de equivalencias</strong> donde miras cuánto cuesta algo parecido y extrapolas.</p>

<h4>Tres monedas, tres cosas distintas</h4>
<p>Esto es lo único que hay que entender. Un objeto puede pedirte hasta tres pagos, y cada uno sale de un sitio: <span class="flag ed">ED-36</span></p>
<div class="tw"><table class="t">
<thead><tr><th>Moneda</th><th>Paga</th><th>Sale de</th><th>Ejemplo</th></tr></thead>
<tbody>
<tr><td><strong>Recursos</strong><br><small>el Acceso</small></td><td><strong>Tenerlo.</strong> Todo lo que el objeto <em>es</em>: su daño, si se esquiva, si la armadura sirve, su alcance</td><td>Tu nivel en Recursos y la ficción</td><td>La espada, el rifle, el coche</td></tr>
<tr><td><strong>Puntos</strong><br><small>de habilidad</small></td><td><strong>Que te haga mejor.</strong> Cualquier bono a una tirada: defender mejor, dar mejor</td><td>Los 12 o 14 puntos de la ficha</td><td>La cota de malla, la espada de maestro armero</td></tr>
<tr><td><strong>Llaves</strong></td><td><strong>Que te deje hacer lo imposible.</strong> Permisos y niveles de Rejilla</td><td>El bote aparte y el monedero</td><td>Las gafas de rayos X, la servoarmadura</td></tr>
</tbody></table></div>
<p>La cota de malla no tiene nada de extraordinario en su mundo: no hay ningún permiso que pedir. Tiene un precio en dinero y te hace defender mejor, así que se paga con Recursos y con puntos, y no toca las Llaves. El cañón de riel, en cambio, te deja agujerear un tanque: eso ninguna habilidad lo hace, y por eso cuesta Llaves.</p>

<h4>La cuenta</h4>
<ol>
<li><strong>Describe el objeto</strong> en una frase, como si se lo contaras a la mesa.</li>
<li><strong>Ponle etiquetas</strong>: <span class="tag">Daño N</span>, <span class="tag">Esq</span>, <span class="tag">Abs</span>, <span class="tag">Rejilla</span>. Son gratis: describen lo que el objeto es, y se pagan con el <span class="tag">Acceso</span>.</li>
<li><strong>Cuenta los bonos.</strong> Cada +1 a una tirada cuesta <strong>1 punto</strong>, igual que en la pirámide. Un objeto que da +2 cuesta 2 puntos.</li>
<li><strong>Cuenta los permisos.</strong> Cada cosa que ninguna habilidad puede hacer —volar, ver a través, respirar donde no se puede— cuesta <strong>1 Llave</strong>.</li>
<li><strong>Cuenta la Rejilla.</strong> Si el objeto opera un nivel por encima, cuesta <strong>N² Llaves</strong> (nivel 2 = 4, nivel 3 = 9).</li>
<li><strong>Ajusta</strong> lo que la cuenta no haya sabido decir, y ya está.</li>
</ol>
<div class="rule">
<p class="rule-title">Las dos pruebas que evitan el 90 % de los errores</p>
<ul>
<li><strong>Si una habilidad ya lo hace, no es un poder: es un bono.</strong> «Sentir cuándo te mienten» no es un permiso, es Empatía; «aguantar el dolor» es Entereza; «correr mucho» es Atletismo. Si lo compras como poder estás pagando dos veces por algo que la pirámide ya vende.</li>
<li><strong>Si te hace ganar a cosas de un nivel por encima, no es un permiso: es Rejilla.</strong> Ver a través de una pared es un permiso de 1 Llave. Ser indetectable para un edificio entero de guardias es un nivel de Rejilla contra la detección, y se paga al cuadrado.</li>
</ul>
</div>

<h4>El Ajuste: lo que la cuenta no sabe decir</h4>
<p>Hay poderes que no se dejan desglosar. La cuenta dice 1 Llave y en mesa resuelven la partida entera; o la cuenta dice 9 y resulta que el chisme solo funciona si lo llevas puesto y te lo pueden robar. Para eso está el Ajuste: miras <strong>lo que el poder hace y la cuenta no ha pagado</strong>, y multiplicas. <span class="flag ed">ED-37</span></p>
<div class="tw"><table class="t">
<thead><tr><th>Etiqueta</th><th>Qué significa</th><th class="num">Puntos y Llaves</th></tr></thead>
<tbody>
<tr><td><strong>Limitado</strong></td><td>Vale menos de lo que dice la cuenta porque tiene correas: solo mientras lo llevas puesto, una vez por escena, solo con luz, te lo pueden quitar</td><td class="num">÷2</td></tr>
<tr><td><strong>Completo</strong></td><td>La cuenta es toda la verdad</td><td class="num">×1</td></tr>
<tr><td><strong>Potenciado</strong></td><td>Hace lo que dice <em>y además</em> algo que no está en la cuenta</td><td class="num">×2</td></tr>
<tr><td><strong>Desatado</strong></td><td>La cuenta se queda muy corta: no tiene condiciones y ni la ficción te lo quita</td><td class="num">×3</td></tr>
</tbody></table></div>
<p>Se redondea hacia arriba y <strong>nada baja de 1</strong>: un poder que ya cuesta una sola Llave no se puede abaratar, solo encarecer. El Ajuste multiplica puntos y Llaves, nunca el Acceso, aunque un poder Desatado rara vez está al alcance de cualquiera.</p>
<div class="rule">
<p class="rule-title">El Ajuste solo paga lo que la cuenta no ha pagado ya</p>
<p>Este es el error que vais a cometer, así que va en negrita. Si ya has desglosado el poder —le has puesto su nivel de Rejilla, sus permisos y sus bonos—, <strong>no lo cobres otra vez con la etiqueta</strong>. El Ajuste vive justo donde el sistema no llega, y se retira solo en cuanto el sistema llega.</p>
<p>Para que dos mesas distintas no tasen lo mismo de forma distinta, una sola pregunta de calibración: <strong>¿cuántas escenas resuelve esto que no hayas pagado ya?</strong> Ninguna, y encima con correas: Limitado. Lo que dice la cuenta: Completo. Una escena entera suya: Potenciado. Cambia cómo se juega la campaña: Desatado.</p>
<p>Se pacta al comprarlo y se escribe al lado del poder. Si el juego demuestra que estaba mal tasado, se vuelve a etiquetar y se ajusta el precio: una subjetividad que multiplica por tres necesita puerta de salida. Y si algo te pide más de ×3, no es un poder: es un nivel de Rejilla que no has visto, o es decorado.</p>
</div>

<div class="example">
<p class="example-title">La misma palabra, tres precios</p>
<p>La invisibilidad es el ejemplo perfecto, porque es una palabra que nombra tres cosas distintas según la mesa.</p>
<div class="tw"><table class="t">
<thead><tr><th>Qué es en la ficción</th><th>La cuenta</th><th>Ajuste</th><th class="num">Precio</th></tr></thead>
<tbody>
<tr><td>Una <strong>capa</strong>: solo mientras la llevas puesta, se cae, te la roban</td><td>permiso: 1 Llave</td><td>Limitado</td><td class="num">1 Llave · Acceso 2</td></tr>
<tr><td><strong>Invisibilidad a voluntad</strong>: resuelve la infiltración entera</td><td>permiso: 1 Llave</td><td>Potenciado</td><td class="num">2 Llaves</td></tr>
<tr><td><strong>Indetectable</strong> por ningún medio, humano o no</td><td>Rejilla 3 contra la detección: 9 Llaves</td><td>Completo</td><td class="num">9 Llaves</td></tr>
</tbody></table></div>
<p>Fíjate en la tercera fila: cuando la cuenta por fin sabe describir el poder, <strong>la etiqueta sobra</strong>.</p>
</div>

<h4>Las cuatro categorías</h4>
<p>Todo lo que se puede fabricar cabe en cuatro cajones, y cada uno se hace con piezas distintas. (Lo que no entra en ninguno —una cuerda, un mapa, un botiquín— es un <strong>útil</strong>: cuesta Acceso y nada más.)</p>
<div class="tw"><table class="t">
<thead><tr><th>Categoría</th><th>De qué se hace</th><th>Lo que suele costar</th></tr></thead>
<tbody>
<tr><td><strong>Arma</strong></td><td>Daño, Esq y Abs. Si alcanza por encima de tu nivel, Rejilla</td><td>Acceso. Puntos solo si además te hace apuntar mejor</td></tr>
<tr><td><strong>Defensa</strong></td><td>Un bono a la reacción, o una absorción fija, o cambiar la etiqueta del atacante</td><td>Acceso y puntos. Llaves solo si para lo imparable</td></tr>
<tr><td><strong>Vehículo</strong></td><td>Un nivel de Rejilla y, mientras lo pilotas, Sincronización (<a href="#ch2-rejilla">2.4</a>)</td><td>Acceso y Llaves</td></tr>
<tr><td><strong>Artefacto</strong></td><td>Permisos y bonos: da poderes</td><td>Las tres, según lo que dé</td></tr>
</tbody></table></div>

<h4>Lo que te puedes permitir: los seis cajones de Recursos</h4>
<p>El Acceso de un objeto es el nivel de <em>Recursos</em> que hace falta para tenerlo (Social → Jerarquía → Recursos). Tu bono en esa Disciplina dice en qué cajón vives:</p>
<div class="tw"><table class="t">
<thead><tr><th>Recursos</th><th>Quién eres</th><th>Lo que compras</th><th>Ejemplos</th></tr></thead>
<tbody>
<tr><td class="num">−2</td><td>No tienes nada y nadie te fía</td><td>Acceso 0, y lo que encuentres</td><td>Ropa, un cuchillo de cocina, lo que te presten</td></tr>
<tr><td class="num">+0</td><td>Un sueldo, o un grupo que te cubre</td><td>Acceso 0 siempre; 1 con esfuerzo</td><td>Una pistola de segunda mano, una moto vieja</td></tr>
<tr><td class="num">+1</td><td>Ahorros, contactos, una cuenta de gastos</td><td>Acceso 1 siempre; 2 con esfuerzo</td><td>Rifle de caza, chaleco, un coche decente</td></tr>
<tr><td class="num">+2</td><td>Dinero de verdad, o un patrón que paga</td><td>Acceso 2 siempre; 3 con esfuerzo</td><td>Armadura militar, coche blindado, un laboratorio</td></tr>
<tr><td class="num">+3</td><td>Mueves presupuestos que no son tuyos</td><td>Acceso 2 sin pestañear; 3 a menudo</td><td>Helicóptero, quirófano, un equipo entero</td></tr>
<tr><td class="num">+4</td><td>El dinero ha dejado de ser el problema</td><td>Acceso 3 siempre</td><td>Lo que no debería existir</td></tr>
</tbody></table></div>
<div class="rule">
<p class="rule-title">El tirón de Recursos</p>
<p>«Con esfuerzo» quiere decir <strong>una vez por arco</strong>, y nunca sale gratis: consigues algo un escalón por encima de tu cajón y la mesa anota el precio, que no es dinero. Un favor que te van a cobrar, una deuda, un rastro, alguien que ahora sabe tu nombre. Es el mismo menú que el de la pifia (<a href="#ch5-golpes">5.2</a>), y convierte «quiero un helicóptero» en una trama en vez de en una discusión.</p>
<p>Y recuerda lo que ya sabes: <strong>lo robado, prestado o conseguido en la ficción funciona una escena entera gratis</strong>. El Acceso dice lo que puedes <em>tener</em>, no lo que puedes <em>usar</em> esta noche.</p>
</div>

<div class="rule">
<p class="rule-title">Aviso: el equipo come de los puntos</p>
<p>Si tu campaña va de poderes —superhéroes, mechas, magos con artefactos, cromados hasta las cejas—, los doce puntos se evaporan en la ficha de equipo y los personajes salen sabiendo hacer muy poco. La herramienta es obvia: <strong>sube el presupuesto</strong>. Dieciséis, dieciocho, veinte. El manual no te va a decir cuántos, porque depende de cuánto cacharro quieras en mesa.</p>
<p>Lo que sí te dice es el precio de subirlos, y conviene saberlo antes: <strong>cuantos más puntos repartas, menos se nota la especialización.</strong> El Ancla corta en +4, así que lo único que crece es la anchura. Con doce hay dos Grandes Maestros y un agujero que duele; con veinte, todo el mundo sabe hacer de todo y nadie es <em>el</em> que sabe hacer algo. Ninguna de las dos está mal: la primera hace equipos de especialistas que se necesitan, la segunda hace héroes completos de cómic. Elige a sabiendas.</p>
</div>

<h4>Cómo encontrar lo que buscas en el catálogo</h4>
<p>Son casi trescientos objetos. Si sabes lo que quieres, cuatro preguntas te dejan en la tabla correcta:</p>
<div class="tw"><table class="t">
<thead><tr><th>Pregunta</th><th>Sí</th><th>No</th></tr></thead>
<tbody>
<tr><td><strong>1. ¿Hace daño?</strong></td><td>Ve a 2</td><td>Ve a 3</td></tr>
<tr><td><strong>2. ¿Alcanza a más de una persona a la vez?</strong></td><td>Arma con Rejilla, o vehículo armado</td><td>Arma: busca por su Daño</td></tr>
<tr><td><strong>3. ¿Te protege de algo?</strong></td><td>Defensa: busca por lo que absorbe</td><td>Ve a 4</td></tr>
<tr><td><strong>4. ¿Te deja hacer algo que no podrías?</strong></td><td>Artefacto: busca por el permiso</td><td>Útil: cuesta solo Acceso</td></tr>
</tbody></table></div>
<p>Y si lo que buscas no existe, ya sabes fabricarlo. El índice por categorías está al final del apéndice.</p>
"""

EN = r"""<h3 id="bz-taller">The workshop: how to build what is not on the list</h3>
<p>No list of objects is ever enough, least of all in a universal rulebook. So the factory comes before the catalogue: with these four pages you can price anything your table dreams up, and the catalogue becomes what it really is, <strong>a table of equivalences</strong> where you look up what something similar costs and extrapolate.</p>

<h4>Three currencies, three different things</h4>
<p>This is the only thing you have to understand. An object can ask you for up to three payments, and each one comes from a different place: <span class="flag ed">ED-36</span></p>
<div class="tw"><table class="t">
<thead><tr><th>Currency</th><th>Pays for</th><th>Comes from</th><th>Example</th></tr></thead>
<tbody>
<tr><td><strong>Resources</strong><br><small>Access</small></td><td><strong>Having it.</strong> Everything the object <em>is</em>: its damage, whether it can be dodged, whether armour helps, its reach</td><td>Your Resources level and the fiction</td><td>The sword, the rifle, the car</td></tr>
<tr><td><strong>Points</strong><br><small>skill points</small></td><td><strong>Making you better.</strong> Any bonus to a roll: defending better, hitting better</td><td>The sheet’s 12 or 14 points</td><td>The chainmail, the master-forged sword</td></tr>
<tr><td><strong>Keys</strong></td><td><strong>Letting you do the impossible.</strong> Permissions and Grid levels</td><td>The separate pot and the wallet</td><td>The X-ray goggles, the powered armour</td></tr>
</tbody></table></div>
<p>There is nothing extraordinary about chainmail in its own world: there is no permission to ask for. It has a price in money and it makes you defend better, so it is paid with Resources and points, and it does not touch Keys. The railgun, on the other hand, lets you punch a hole in a tank: no skill does that, and that is why it costs Keys.</p>

<h4>The sum</h4>
<ol>
<li><strong>Describe the object</strong> in one sentence, as if you were telling the table about it.</li>
<li><strong>Tag it</strong>: <span class="tag">Dmg N</span>, <span class="tag">Dodge</span>, <span class="tag">Soak</span>, <span class="tag">Grid</span>. They are free: they describe what the object is, and they are paid for with <span class="tag">Access</span>.</li>
<li><strong>Count the bonuses.</strong> Every +1 to a roll costs <strong>1 point</strong>, exactly as in the pyramid. An object that gives +2 costs 2 points.</li>
<li><strong>Count the permissions.</strong> Everything no skill can do —flying, seeing through walls, breathing where you cannot— costs <strong>1 Key</strong>.</li>
<li><strong>Count the Grid.</strong> If the object operates a level above, it costs <strong>N² Keys</strong> (level 2 = 4, level 3 = 9).</li>
<li><strong>Adjust</strong> whatever the sum failed to say, and you are done.</li>
</ol>
<div class="rule">
<p class="rule-title">The two tests that prevent 90 % of the mistakes</p>
<ul>
<li><strong>If a skill already does it, it is not a power: it is a bonus.</strong> “Sensing when you are being lied to” is not a permission, it is Empathy; “shrugging off pain” is Fortitude; “running fast” is Athletics. Buying it as a power means paying twice for something the pyramid already sells.</li>
<li><strong>If it makes you beat things a level above you, it is not a permission: it is Grid.</strong> Seeing through a wall is a 1-Key permission. Being undetectable to a whole building full of guards is a Grid level against detection, and it is paid for squared.</li>
</ul>
</div>

<h4>The Adjustment: what the sum cannot say</h4>
<p>Some powers refuse to be itemised. The sum says 1 Key and at the table they solve the whole session; or the sum says 9 and it turns out the gadget only works while you are wearing it and can be stolen. That is what the Adjustment is for: you look at <strong>what the power does that the sum has not paid for</strong>, and you multiply. <span class="flag ed">ED-37</span></p>
<div class="tw"><table class="t">
<thead><tr><th>Tag</th><th>What it means</th><th class="num">Points and Keys</th></tr></thead>
<tbody>
<tr><td><strong>Limited</strong></td><td>Worth less than the sum says because it comes with strings: only while worn, once per scene, only in daylight, it can be taken from you</td><td class="num">÷2</td></tr>
<tr><td><strong>Complete</strong></td><td>The sum is the whole truth</td><td class="num">×1</td></tr>
<tr><td><strong>Enhanced</strong></td><td>It does what it says <em>and also</em> something the sum does not cover</td><td class="num">×2</td></tr>
<tr><td><strong>Unleashed</strong></td><td>The sum falls far short: no conditions, and not even the fiction takes it away</td><td class="num">×3</td></tr>
</tbody></table></div>
<p>Round up, and <strong>nothing goes below 1</strong>: a power that already costs a single Key cannot be made cheaper, only dearer. The Adjustment multiplies points and Keys, never Access, although an Unleashed power is rarely within everybody’s reach.</p>
<div class="rule">
<p class="rule-title">The Adjustment only pays for what the sum has not paid already</p>
<p>This is the mistake you are going to make, so here it is in bold. If you have already itemised the power —given it its Grid level, its permissions and its bonuses—, <strong>do not charge for it again with the tag</strong>. The Adjustment lives exactly where the system does not reach, and it withdraws the moment the system reaches.</p>
<p>So that two different tables do not price the same thing differently, one calibration question: <strong>how many scenes does this solve that you have not already paid for?</strong> None, and with strings attached: Limited. What the sum says: Complete. A whole scene of its own: Enhanced. It changes how the campaign is played: Unleashed.</p>
<p>It is agreed when bought and written next to the power. If play proves it was mispriced, re-tag it and adjust: a subjective thing that multiplies by three needs a way out. And if something asks for more than ×3, it is not a power: it is a Grid level you have not spotted, or it is scenery.</p>
</div>

<div class="example">
<p class="example-title">The same word, three prices</p>
<p>Invisibility is the perfect example, because it is one word naming three different things depending on the table.</p>
<div class="tw"><table class="t">
<thead><tr><th>What it is in the fiction</th><th>The sum</th><th>Adjustment</th><th class="num">Price</th></tr></thead>
<tbody>
<tr><td>A <strong>cloak</strong>: only while you wear it, it slips, it gets stolen</td><td>permission: 1 Key</td><td>Limited</td><td class="num">1 Key · Access 2</td></tr>
<tr><td><strong>Invisibility at will</strong>: it solves the whole infiltration</td><td>permission: 1 Key</td><td>Enhanced</td><td class="num">2 Keys</td></tr>
<tr><td><strong>Undetectable</strong> by any means, human or otherwise</td><td>Grid 3 against detection: 9 Keys</td><td>Complete</td><td class="num">9 Keys</td></tr>
</tbody></table></div>
<p>Look at the third row: once the sum can finally describe the power, <strong>the tag becomes unnecessary</strong>.</p>
</div>

<h4>The four categories</h4>
<p>Everything you can build fits in four drawers, and each one is made of different parts. (Whatever fits in none of them —a rope, a map, a first-aid kit— is a <strong>tool</strong>: it costs Access and nothing else.)</p>
<div class="tw"><table class="t">
<thead><tr><th>Category</th><th>What it is made of</th><th>What it usually costs</th></tr></thead>
<tbody>
<tr><td><strong>Weapon</strong></td><td>Damage, Dodge and Soak. If it reaches above your level, Grid</td><td>Access. Points only if it also makes you aim better</td></tr>
<tr><td><strong>Defence</strong></td><td>A bonus to the reaction, or fixed soak, or changing the attacker’s tag</td><td>Access and points. Keys only if it stops the unstoppable</td></tr>
<tr><td><strong>Vehicle</strong></td><td>A Grid level and, while you pilot it, Synchronisation (<a href="#ch2-rejilla">2.4</a>)</td><td>Access and Keys</td></tr>
<tr><td><strong>Artefact</strong></td><td>Permissions and bonuses: it grants powers</td><td>All three, depending on what it gives</td></tr>
</tbody></table></div>

<h4>What you can afford: the six drawers of Resources</h4>
<p>An object’s Access is the level of <em>Resources</em> you need in order to have it (Social → Hierarchy → Resources). Your bonus in that Discipline says which drawer you live in:</p>
<div class="tw"><table class="t">
<thead><tr><th>Resources</th><th>Who you are</th><th>What you buy</th><th>Examples</th></tr></thead>
<tbody>
<tr><td class="num">−2</td><td>You have nothing and nobody gives you credit</td><td>Access 0, and whatever you find</td><td>Clothes, a kitchen knife, whatever you are lent</td></tr>
<tr><td class="num">+0</td><td>A wage, or a crew that covers you</td><td>Access 0 always; 1 with effort</td><td>A second-hand pistol, an old motorbike</td></tr>
<tr><td class="num">+1</td><td>Savings, contacts, an expense account</td><td>Access 1 always; 2 with effort</td><td>Hunting rifle, vest, a decent car</td></tr>
<tr><td class="num">+2</td><td>Real money, or a patron who pays</td><td>Access 2 always; 3 with effort</td><td>Military armour, armoured car, a laboratory</td></tr>
<tr><td class="num">+3</td><td>You move budgets that are not yours</td><td>Access 2 without blinking; 3 often</td><td>Helicopter, operating theatre, a whole team</td></tr>
<tr><td class="num">+4</td><td>Money has stopped being the problem</td><td>Access 3 always</td><td>What should not exist</td></tr>
</tbody></table></div>
<div class="rule">
<p class="rule-title">The Resources pull</p>
<p>“With effort” means <strong>once per arc</strong>, and it is never free: you get hold of something one step above your drawer and the table writes down the price, which is not money. A favour that will be called in, a debt, a trail, somebody who now knows your name. It is the same menu as the fumble’s (<a href="#ch5-golpes">5.2</a>), and it turns “I want a helicopter” into a plot instead of an argument.</p>
<p>And remember what you already know: <strong>anything stolen, borrowed or obtained in the fiction works free for a whole scene</strong>. Access says what you can <em>have</em>, not what you can <em>use</em> tonight.</p>
</div>

<div class="rule">
<p class="rule-title">Warning: equipment eats into your points</p>
<p>If your campaign is about powers —superheroes, mechs, wizards with artefacts, chrome to the eyeballs—, the twelve points evaporate into the equipment list and the characters turn up knowing how to do very little. The tool is obvious: <strong>raise the budget</strong>. Sixteen, eighteen, twenty. The rulebook is not going to tell you how many, because it depends on how much hardware you want on the table.</p>
<p>What it will tell you is the price of raising it, and it is worth knowing beforehand: <strong>the more points you hand out, the less specialisation shows.</strong> The Anchor cuts off at +4, so the only thing that grows is breadth. With twelve there are two Grand Masters and a hole that hurts; with twenty, everybody can do everything and nobody is <em>the one</em> who can do something. Neither is wrong: the first makes teams of specialists who need each other, the second makes complete comic-book heroes. Choose knowingly.</p>
</div>

<h4>How to find what you are after in the catalogue</h4>
<p>There are almost three hundred objects. If you know what you want, four questions drop you on the right table:</p>
<div class="tw"><table class="t">
<thead><tr><th>Question</th><th>Yes</th><th>No</th></tr></thead>
<tbody>
<tr><td><strong>1. Does it do damage?</strong></td><td>Go to 2</td><td>Go to 3</td></tr>
<tr><td><strong>2. Does it reach more than one person at a time?</strong></td><td>Weapon with Grid, or armed vehicle</td><td>Weapon: look it up by its Damage</td></tr>
<tr><td><strong>3. Does it protect you from something?</strong></td><td>Defence: look it up by what it soaks</td><td>Go to 4</td></tr>
<tr><td><strong>4. Does it let you do something you could not?</strong></td><td>Artefact: look it up by the permission</td><td>Tool: it costs Access only</td></tr>
</tbody></table></div>
<p>And if what you are after does not exist, you now know how to build it. The index by category is at the end of the appendix.</p>
"""


def do(f, txt, anchor):
    shutil.copyfile(f, f + '.bak_taller')
    s = io.open(f, encoding='utf-8').read()
    k = s.index(anchor)
    s = s[:k] + txt + '\n' + s[k:]
    io.open(f, 'w', encoding='utf-8').write(s)
    print(' ', f, 'ok')


do('frag_bazar.html', ES, '<h3 id="bz-fantasia"')
do('frag_bazar_a.en.html', EN, '<h3 id="bz-fantasia"')
