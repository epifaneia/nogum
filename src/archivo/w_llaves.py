# -*- coding: utf-8 -*-
"""Bloque 1: la Llave comprada (2.3), el x100 y el techo del universo (2.4),
los 12/14 puntos con bote aparte (3.5) y el capitulo de experiencia (3.6). ES + EN."""
import io, os, shutil
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------- 2.3 ES
LLAVE_ES = r"""
<div class="rule">
<p class="rule-title">Qué cubre una Llave</p>
<p><strong>Una Llave es una Disciplina para siempre, o un Ámbito entero durante una escena.</strong> Eliges la forma al comprarla. <span class="flag ed">ED-27</span></p>
<ul>
<li><strong>Estrecha y permanente.</strong> Una de las ocho Disciplinas del Ámbito, elegida por ti y para siempre: «Armas contra los vampiros». Es tacaña a propósito. Una espada no te da cobertura contra el aliento del dragón, porque aguantar el aliento es Entereza y tú compraste Armas.</li>
<li><strong>Ancha y de escena.</strong> Si la Llave es muy concreta, cubre el <em>Ámbito entero</em>, pero solo durante una escena: el duelo, o el asalto al castillo con sus aliados dentro.</li>
</ul>
<p>La Llave ancha no se ata a un enemigo, se ata a una <strong>escena</strong>. Un monstruo que vuelve cuando ya sabéis cómo matarlo ha dejado de ser un antagonista; y si vuelve con algo nuevo, ya no es el mismo bicho y tu Llave no le sirve. La escena es la unidad de tiempo de este juego, igual que para el tono y para el Estilo.</p>
</div>

<h4>Subir contra la misma cosa</h4>
<p>Una Llave te pone <strong>un nivel por encima</strong>. Para subir más contra lo mismo, la escalera es cuadrada: subir <em>n</em> niveles cuesta <em>n</em>² Llaves. <span class="flag ed">ED-32</span></p>
<div class="tw"><table class="t">
<thead><tr><th>Lo que subes</th><th class="num">Llaves</th><th>Tu alcance contra esa cosa</th></tr></thead>
<tbody>
<tr><td>+1 nivel</td><td class="num">1</td><td>×100</td></tr>
<tr><td>+2</td><td class="num">4</td><td>×10.000</td></tr>
<tr><td>+3</td><td class="num">9</td><td>×1.000.000</td></tr>
<tr><td>+4</td><td class="num">16</td><td>×100.000.000</td></tr>
<tr><td>+5</td><td class="num">25</td><td>×10.000.000.000</td></tr>
</tbody></table></div>
<p>De ahí sale sola una regla que no hace falta escribir como prohibición: con las cinco Llaves del bote de creación (<a href="#ch3-economia">3.5</a>), <strong>nadie empieza pasando de +2</strong>. Cuatro Llaves te compran diez mil veces tu alcance contra una cosa y te sobra una. El tercer peldaño se gana jugando.</p>
<div class="rule">
<p class="rule-title">Regla opcional · La escalera llana</p>
<p>Este es un manual universal y en algún momento alguien querrá llegar a dios. Si no quieres que el precio se dispare, usa <strong>3<em>n</em>−2</strong>: 1, 4, 7, 10, 13. Coincide con la cuadrada en los dos primeros peldaños —donde juega casi todo el mundo— y solo se separa cuando se va a por la divinidad. La cuadrada dice «la divinidad se conquista en campaña»; la llana dice «la divinidad se compra a plazos». Las dos son defendibles; por defecto va la cuadrada, porque <em>n</em>² se recuerda sin tabla.</p>
</div>

<h4>Llave propia y Llave prestada</h4>
<dl>
<dt>Llave propia</dt>
<dd>Comprada en la creación o con el monedero de experiencia (<a href="#ch3-progreso">3.6</a>). Es <strong>permanente</strong>, se escribe en la ficha con su objetivo y su nivel, y se pacta con el Director antes de empezar. No te la quita nadie.</dd>
<dt>Llave prestada</dt>
<dd>La da el Director por la trama o para premiar el ingenio: «se te ocurre usar el agua bendita». No se paga, no sube de nivel y <strong>no se apunta en la ficha</strong>: vive en la escena y se va con ella. <span class="flag ed">ED-28</span></dd>
</dl>
<p>Con esa distinción el Director puede seguir regalando ideas sin inflar al personaje, y quien pagó la suya sabe que es suya.</p>

<h4>Prestar y traspasar</h4>
<p>Lo de un solo uso se declara y ya: le das la bala de plata a quien dispara mejor y se acabó. Lo permanente se <strong>traspasa</strong>: el dueño libera su Llave y el otro la paga con su monedero. Es una transacción y no un préstamo, y eso obliga al grupo a decidir a quién le sirve más, en vez de pasarse el amuleto de mano en mano sin que nadie pague nunca.</p>
<p>Y hay una línea que resuelve casi todos los casos de mesa: <strong>lo que se lleva en la mano se presta; lo que se lleva en la cabeza, no.</strong> El agua bendita cambia de dueño. Saber el nombre verdadero, no.</p>
<p>El equipo que rompe la Rejilla —el cañón de riel que agujerea un tanque— también se compra con Llaves, y tiene sus tres cerrojos en <a href="#ch4-equipo">4.3</a>.</p>
"""

# ---------------------------------------------------------------- 2.4 ES
X100_ES = r"""
<div class="rule">
<p class="rule-title">Un nivel son dos ceros</p>
<p>Cada peldaño de la Rejilla multiplica por cien tu <strong>alcance</strong>: a cuánta gente llegas, qué tamaño de problema tocas, cuánto mundo mueves de una vez. <span class="flag ed">ED-29</span></p>
<div class="tw"><table class="t">
<thead><tr><th>Nivel</th><th class="num">Alcance</th><th>La imagen</th></tr></thead>
<tbody>
<tr><td>1</td><td class="num">×1</td><td>Una persona</td></tr>
<tr><td>2</td><td class="num">×100</td><td>Una sala llena</td></tr>
<tr><td>3</td><td class="num">×10.000</td><td>Un edificio, un barrio</td></tr>
<tr><td>4</td><td class="num">×1.000.000</td><td>Una ciudad</td></tr>
<tr><td>5</td><td class="num">×100.000.000</td><td>Un país</td></tr>
</tbody></table></div>
<p>Los peldaños ya estaban ahí —persona, sala, edificio, ciudad, país—; el número solo los pone delante. Y con el número delante, la regla dura de este capítulo deja de parecer arbitraria: cuando alguien te saca un nivel no es que sea «mejor que tú», es que está jugando con <strong>dos ceros más</strong>. Por eso no hay tirada.</p>
<p><strong>Es alcance, no literalidad.</strong> Un Físico 2 no levanta cien veces más peso ni corre cien veces más rápido: se enfrenta a cien veces más mundo a la vez. El número es una imagen, no una tabla de equivalencias. En cuanto alguien pregunte «¿entonces cuánto pesa eso?», la respuesta es «lo que pida la escena».</p>
<p>Y hace más dramática la Llave: lo que compras con ella es pelear <strong>cien veces por encima de tu peso</strong>, contra una cosa concreta.</p>
<p class="small">Regla opcional: si tu campaña es de callejón y el ×100 te suena a cómic, usa <strong>×10 por nivel</strong>. La escala narrativa no cambia —sigues yendo de la persona al país—, solo cambia el tamaño del asombro. <span class="flag proposal">Propuesta sin validar</span></p>
</div>
"""

TECHO_ES = r"""
<h4>El techo del universo</h4>
<p>El <strong>nivel inicial</strong> lo pone la campaña; el <strong>techo</strong> lo pone el universo. En una partida cyberpunk no existe un Mental 2 por mucho que la campaña dure veinte sesiones: no hay ingenio por cien. Lo que sí hay son cromados al borde de la psicosis, que llegan a Físico 2, y ahí se acaba el género. Cada una de las veinte recetas (<a href="#ch8-recetas">8.4</a>) trae su techo por ámbito, y ese techo es, más que el tono o que el equipo, lo que hace que un universo se sienta como ese universo. <span class="flag ed">ED-30</span></p>
<p>La Rejilla sigue subiendo con la historia, pero contra ese techo. Y la Llave es la excepción pactada: <strong>en cyberpunk no puedes tener un ingenio por cien, pero sí puedes tener el exploit que funciona contra esa IA.</strong> Un techo sin excepciones aburre; una excepción sin techo rompe. Aquí el techo es permanente y la excepción se compra.</p>
"""

# ---------------------------------------------------------------- 3.5 ES
ECON_ES = r"""<h3 id="ch3-economia">3.5 La economía de la escasez</h3>
<p>NOGUM reparte <strong>12 puntos</strong> de habilidad, o <strong>14</strong> si el universo tiene Arcano. El número no es un capricho: sin magia hay cuatro Ámbitos, ocho Dominios y treinta y dos Disciplinas, cuarenta casillas; con magia son cincuenta. Doce sobre cuarenta y catorce sobre cincuenta son la misma proporción, así que la ficha se siente igual de escasa se juegue donde se juegue. <span class="flag ed">ED-31</span></p>
<p>Doce puntos te obligan a gestionar la escasez: si quieres destacar en algo, casi te obligan a ser una nulidad en algún sitio. Más puntos abren la puerta a fichas sin debilidades, que suelen ser menos interesantes. Pero jugar a NOGUM es un pacto entre caballeros: este manual no dedicará una sola línea a diseñar cortafuegos contra el juego sucio. El tipo de personajes que pide la historia se acuerda en la mesa, de forma madura. Dicho esto, da tantos puntos como te apetezca: el manual está para ajustarse a tu campaña. <span class="src">Borrador, T107</span></p>

<div class="rule">
<p class="rule-title">El bote aparte</p>
<p>Además de los puntos, cada personaje recibe <strong>un bote que no se mezcla</strong>: o <strong>+1 nivel de Rejilla en un Ámbito</strong>, o <strong>5 Llaves propias</strong>. No hay cambio entre los dos botes en ninguna dirección: los puntos no compran Llaves y las Llaves no compran puntos.</p>
<p>El motivo es de mesa y no de matemáticas. Si se pudieran cambiar, aparecería el héroe de Rejilla sin oficio ni trasfondo: alguien enorme que no sabe hacer nada, que es el personaje más aburrido que se puede llevar a una partida. Obligando a gastar los doce puntos en habilidades, todo el mundo llega con un oficio debajo del poder.</p>
<p><strong>Y la elección no es neutra.</strong> Un nivel de Rejilla cubre un Ámbito entero: sus dos Dominios y sus ocho Disciplinas, <strong>diez casillas por cinco monedas</strong>. Una Llave cubre una casilla por una moneda. La anchura es barata, pero te la marca el universo con su techo; la libertad es cara, pero la eliges tú y apunta a lo que a ti te importa. <strong>La libertad se paga al doble.</strong></p>
</div>

<p>Doce puntos te obligan a elegir entre ser un <strong>generalista competente</strong> o un <strong>especialista con fallos</strong>.</p>

<div class="example">
<p class="example-title">Caso A · El héroe de acción (especialista)</p>
<p>Quiere ser el mejor disparando (+4) y muy duro (+3).</p>
<div class="tw"><table class="t">
<thead><tr><th>Compra</th><th>Resultado</th><th class="num">Coste</th></tr></thead>
<tbody>
<tr><td>Físico → Vigor → Entereza → Firma «Aguantar el dolor» (1 punto)</td><td>Vigor +1 · Entereza +2 · Aguantar el dolor +3</td><td class="num">3</td></tr>
<tr><td>Físico → Vigor (ya pagado) → Armas → Firma «Pistolas» (2 puntos)</td><td>Armas +2 · Pistolas +4</td><td class="num">3</td></tr>
<tr><td>Técnico → Operaciones → Pilotaje</td><td>Operaciones +1 · Pilotaje +2</td><td class="num">2</td></tr>
<tr><td>Mental → Ingenio → Alerta</td><td>Ingenio +1 · Alerta +2</td><td class="num">2</td></tr>
<tr><td>Físico → Destreza</td><td>Destreza +1</td><td class="num">1</td></tr>
<tr><td>Mental → Ingenio (ya pagado) → Táctica</td><td>Táctica +2</td><td class="num">1</td></tr>
<tr><td>Social → nada · Arcano → nada</td><td>Nulidad −2 en ambos</td><td class="num">0</td></tr>
<tr><td colspan="2"><strong>Total</strong></td><td class="num"><strong>12</strong></td></tr>
</tbody></table></div>
<p><strong>Bote aparte:</strong> cinco Llaves, todas estrechas: «Armas contra los cromados», «Alerta contra las emboscadas», y tres sin gastar, para la sesión cero. O, si prefiere ser grande antes que preciso, +1 de Rejilla en Físico y ninguna Llave.</p>
<p><strong>Resultado:</strong> es letal disparando (+4), duro (+3), sabe conducir y no le pillan por sorpresa. Pero tiene <strong>Nulidad (−2)</strong> en todo lo social. Si tiene que desescalar un conflicto con palabras, tirará con −2… y la situación probablemente acabe a tiros.</p>
<p><span class="flag ed">ED-4</span> El borrador contaba 4 puntos para la rama de Pistolas y usaba un modelo concreto («Colt 45») como Firma de +4. Con la regla de un punto por +1, la rama cuesta 3, y el +4 es la misma Firma con su segundo punto.</p>
</div>

<div class="example">
<p class="example-title">Caso B · El superviviente (generalista)</p>
<p>Quiere estar preparado para todo.</p>
<ul>
<li>Compra un Dominio en cada ámbito (5 puntos): ya no es nulo en nada. Tira con +1 en sus Dominios y con +0 en todo lo demás.</li>
<li>Sube siete Disciplinas a +2 (7 puntos): Atletismo, Entereza, Ciencias, Alerta, Persuasión, Mecánica y Proyección.</li>
<li><strong>Bote aparte:</strong> +1 de Rejilla en Social. No es más listo ni más fuerte que antes; es que ahora le escucha una sala entera.</li>
</ul>
<p><strong>Resultado:</strong> es una navaja suiza utilísima, pero nunca brillará con un +4.</p>
</div>

<div class="rule">
<p class="rule-title">Cuánto cuesta ser una nulidad, y lo decide la tarjeta</p>
<p>Para no ser Nulidad en ningún sitio basta con un Dominio en cada Ámbito: cuatro puntos en un universo sin magia. Te quedan ocho, que son exactamente <strong>dos Grandes Maestros</strong> (Dominio 1 + Disciplina 1 + Firma 2 = 4 puntos cada uno). El tercero solo sale si renuncias a cubrir un Ámbito entero y te quedas en −2 allí. El sistema cobra el peaje solo, sin que haya que prohibir nada: <strong>el precio de las Firmas es ser una nulidad</strong>.</p>
<p>Lo que ese peaje cuesta <em>en mesa</em> no lo decide la ficha. Lo decide la tarjeta:</p>
<div class="tw"><table class="t">
<thead><tr><th>Tarjeta</th><th class="num">Lo que saca adelante tu −2</th></tr></thead>
<tbody>
<tr><td>Épica · Pulp desenfrenado</td><td class="num">51 %</td></tr>
<tr><td>Realista</td><td class="num">36 %</td></tr>
<tr><td>Primera marcha · Bola de nieve</td><td class="num">30 %</td></tr>
<tr><td>Angustia · Pesadilla</td><td class="num">9 %</td></tr>
</tbody></table></div>
<p>En una campaña épica, dejarte un Ámbito vacío casi no duele: sigues sacando adelante la mitad de lo que intentas con él. En Angustia es una sentencia. El mismo personaje de tres maestrías es una ganga en un sitio y un suicidio en otro, y eso <strong>lo decide el tono, no una regla de creación</strong>.</p>
</div>
<p>El sistema funciona. Tú decides dónde poner el foco.</p>

"""

# ---------------------------------------------------------------- 3.6 ES
PROG_ES = r"""<h3 id="ch3-progreso">3.6 Progresión: los dos monederos</h3>
<p>Casi todos los juegos meten en el mismo saco de puntos tres cosas que no se parecen en nada, y así les va: el guerrero de nivel quince es a la vez más hábil, más poderoso en el mundo y más curtido, porque solo hay un contador. Aquí se separan, y cada una tiene un dueño distinto.</p>
<div class="tw"><table class="t">
<thead><tr><th>Qué cambia</th><th>Quién es su dueño</th><th>Cómo se mueve</th></tr></thead>
<tbody>
<tr><td><strong>El mundo</strong> · la Rejilla</td><td>El Director</td><td>No se compra. Sube cuando los hechos lo justifican, pactada en la mesa, y contra el techo del universo</td></tr>
<tr><td><strong>Las cicatrices</strong> · dones y lacras</td><td>La ficción</td><td>No se compran: ocurren durante la partida</td></tr>
<tr><td><strong>La competencia</strong> · puntos y Llaves</td><td>La mesa</td><td>Dos monederos, con su ritmo acordado en la sesión cero</td></tr>
</tbody></table></div>

<h4>Dos bolsas que crecen a ritmos distintos</h4>
<p>La experiencia no es un contador: son <strong>dos monederos independientes</strong>. <span class="flag ed">ED-33</span></p>
<ul>
<li><strong>Puntos de habilidad.</strong> Compran pirámide: Dominios, Disciplinas y Firmas, con los mismos precios de la creación.</li>
<li><strong>Llaves.</strong> Compran Llaves propias, suben la escalera cuadrada contra una misma cosa y pagan el equipo que rompe la Rejilla (<a href="#ch4-equipo">4.3</a>).</li>
</ul>
<p>Son la misma pregunta hecha dos veces, y conviene hacerla dos veces, porque los dos grifos no hacen lo mismo:</p>
<div class="rule">
<p class="rule-title">El monedero de Llaves es el mando de potencia de la campaña</p>
<p>Los puntos de habilidad solo te <strong>ensanchan</strong>: el Ancla los corta en +4, así que por muchos que des, nadie se vuelve más alto, solo bueno en más cosas. Las Llaves, en cambio, abren equipo y rompen techos de Rejilla, y eso no satura nunca: siempre hay otra Disciplina, otra escena, otro objeto que comprar.</p>
<p>Por eso el ritmo por defecto de las Llaves es <strong>lento: una por sesión</strong>, y conviene ser tacaño con ellas, porque muchas se van en equipo. Si quieres que la campaña escale, abre el grifo de las Llaves. Si lo que quieres es que los personajes sepan hacer más cosas, abre el de los puntos. No son intercambiables y no deben darse juntos sin pensarlo.</p>
</div>

<h4>Pregunta 1 · ¿Cómo crecen los personajes?</h4>
<div class="tw"><table class="t">
<thead><tr><th>Opción</th><th>Regla</th><th>Se siente como</th></tr></thead>
<tbody>
<tr><td><strong>Quietos</strong></td><td>0</td><td>One-shots y campañas donde lo que cambia es el mundo, no la ficha</td></tr>
<tr><td><strong>Despacio</strong></td><td>+1 por arco (varias sesiones)</td><td>Novela: cada punto se nota y se recuerda</td></tr>
<tr><td><strong>Deprisa</strong></td><td>+1 por sesión</td><td>Serie de televisión: se ve crecer capítulo a capítulo</td></tr>
<tr><td><strong>Muy deprisa</strong></td><td>+2 por sesión</td><td>Shōnen: al final saben hacer de todo</td></tr>
<tr><td><strong>A saltos</strong></td><td>+5 por arco y nada entre medias</td><td>El salto de tiempo. Casi obliga a mover la Rejilla a la vez</td></tr>
</tbody></table></div>
<p>La misma pregunta, otra vez, para las Llaves. Por defecto: una por sesión, y si la campaña va de equipo —cyberpunk, saqueo, superhéroes de gadget— tenla más presente, porque ahí el monedero de Llaves es la tienda.</p>

<h4>Pregunta 2 · ¿Quién crece?</h4>
<p>Solo si la respuesta anterior no es «quietos»: <strong>todos por igual</strong>, o <strong>quien se lo gane en la historia</strong>. Y una advertencia que viene de muchas mesas: repartir solo por méritos hace que el fuerte se haga más fuerte y que la mesa discuta quién se lo ha ganado.</p>
<p>La forma sana es que <strong>el mérito sume encima de una base</strong>, no que la sustituya. Todos reciben lo que marca el ritmo, y quien haya tenido un momento gordo se lleva +1 extra. Así el reparto nunca castiga al jugador tímido.</p>

<h4>Qué se premia</h4>
<p>NOGUM es un manual narrativo y premia narrativa. Esta es la lista corta:</p>
<ol>
<li>Resolver el conflicto central del arco.</li>
<li>Jugar una lacra en contra propia cuando no convenía.</li>
<li>Encontrar una Llave, o dársela a otro.</li>
<li>Pagar un coste gordo por el grupo.</li>
<li>Cerrar un hilo de la historia personal del personaje.</li>
<li>Fallar de forma memorable y asumir las consecuencias.</li>
<li>Sobrevivir a una noche en una tarjeta más dura que la de la campaña.</li>
</ol>
<p>El sexto tiene un padre ilustre: hay juegos que te dan experiencia precisamente cuando fallas, y es una idea excelente. Otros premian usar una habilidad hasta dominarla, o ganar combates. Son enfoques legítimos y este manual no los recoge porque mide otra cosa; si tu mesa los quiere, conviértelos en una entrada más de esta lista y listo.</p>

<div class="rule">
<p class="rule-title">La experiencia no puede romper la matemática</p>
<p>Ninguna tirada pasa de +4, así que la experiencia <strong>no hace a nadie más alto: solo más ancho</strong>. Con +1 por sesión, a las veinte sesiones un personaje ha triplicado su ficha y sigue sin pasar de +4. Crecer es ser bueno en más cosas, no ser un dios en una.</p>
<p>Y ahí se cierra un circuito con la Rejilla: los personajes se ensanchan, el Director sube el mundo, y el desafío vuelve solo sin que nadie toque una tabla. El aviso que trae de la mano: en una campaña de crecimiento rápido los personajes vivirán en +3 y +4 en lo suyo, y varias tarjetas pierden ahí el fallo limpio. La respuesta no es recortar puntos, es mover la Rejilla. Si el mundo no sube, el juego se vuelve un paseo.</p>
</div>

<h4>Dones y lacras: no se compran, ocurren</h4>
<p>Las ventajas y desventajas no están en ningún bote. Aparecen durante la partida, y tienen un origen mecánico concreto: <strong>una lacra es la cicatriz de un bloque lleno</strong>. Cuando se te llena un bloque de la barra Mental o Espiritual y luego te curas, el −2 se va pero queda algo con nombre: el insomnio, la deuda, el tic, el miedo al agua. El don funciona igual por el otro lado, cuando la ficción te lo debe. Los detalles, con sus umbrales y sus ejemplos, están en <a href="#ch5-dano">5.5</a>. <span class="flag ed">ED-35</span></p>
<p><strong>Tesis del autor:</strong> crecimiento rápido, bonificación por el buen juego narrativo y experiencia fija en los hitos de campaña. Los hitos sirven como incentivo; la experiencia sirve para gestionar las expectativas de la campaña. <span class="src">T37</span></p>
</section>
"""

# ---------------------------------------------------------------- 2.3 EN
LLAVE_EN = r"""
<div class="rule">
<p class="rule-title">What one Key covers</p>
<p><strong>A Key is one Discipline for ever, or a whole Sphere for one scene.</strong> You pick the shape when you buy it. <span class="flag ed">ED-27</span></p>
<ul>
<li><strong>Narrow and permanent.</strong> One of the Sphere’s eight Disciplines, chosen by you and yours for good: “Weapons against vampires”. It is stingy on purpose. A sword gives you no cover against the dragon’s breath, because surviving the breath is Fortitude and you bought Weapons.</li>
<li><strong>Wide and scene-long.</strong> If the Key is very specific, it covers the <em>whole Sphere</em>, but only for one scene: the duel, or the assault on the castle with its allies inside.</li>
</ul>
<p>The wide Key is not tied to an enemy, it is tied to a <strong>scene</strong>. A monster that comes back once you know how to kill it has stopped being an antagonist; and if it comes back with something new, it is not the same creature and your Key does not work on it. The scene is this game’s unit of time, as it already was for tone and for Style.</p>
</div>

<h4>Going higher against the same thing</h4>
<p>One Key puts you <strong>one level above</strong>. To climb further against the same thing the ladder is square: going up <em>n</em> levels costs <em>n</em>² Keys. <span class="flag ed">ED-32</span></p>
<div class="tw"><table class="t">
<thead><tr><th>What you climb</th><th class="num">Keys</th><th>Your reach against that thing</th></tr></thead>
<tbody>
<tr><td>+1 level</td><td class="num">1</td><td>×100</td></tr>
<tr><td>+2</td><td class="num">4</td><td>×10,000</td></tr>
<tr><td>+3</td><td class="num">9</td><td>×1,000,000</td></tr>
<tr><td>+4</td><td class="num">16</td><td>×100,000,000</td></tr>
<tr><td>+5</td><td class="num">25</td><td>×10,000,000,000</td></tr>
</tbody></table></div>
<p>Out of that comes a rule nobody has to write as a prohibition: with the five Keys in the creation pot (<a href="#ch3-economia">3.5</a>), <strong>nobody starts above +2</strong>. Four Keys buy you ten thousand times your reach against one thing and you still have one left. The third rung is earned in play.</p>
<div class="rule">
<p class="rule-title">Optional rule · The flat ladder</p>
<p>This is a universal rulebook and sooner or later someone will want to reach godhood. If you would rather the price did not explode, use <strong>3<em>n</em>−2</strong>: 1, 4, 7, 10, 13. It agrees with the square ladder on the first two rungs —where almost every table plays— and only parts company when someone goes for divinity. The square one says “divinity is conquered in play”; the flat one says “divinity is bought in instalments”. Both are defensible; the square one is the default, because <em>n</em>² is remembered without a table.</p>
</div>

<h4>Own Keys and lent Keys</h4>
<dl>
<dt>Own Key</dt>
<dd>Bought at creation or with the experience wallet (<a href="#ch3-progreso">3.6</a>). It is <strong>permanent</strong>, written on the sheet with its target and its level, and agreed with the Director before play starts. Nobody can take it from you.</dd>
<dt>Lent Key</dt>
<dd>Given by the Director for the plot or to reward a good idea: “it occurs to you to use the holy water”. It is not paid for, it does not go up a level and it is <strong>not written on the sheet</strong>: it lives in the scene and leaves with it. <span class="flag ed">ED-28</span></dd>
</dl>
<p>With that distinction the Director can keep handing out ideas without inflating the character, and whoever paid for theirs knows it is theirs.</p>

<h4>Lending and handing over</h4>
<p>A single-use Key is simply declared: you give the silver bullet to whoever shoots best and that is that. A permanent one is <strong>handed over</strong>: the owner releases their Key and the other pays for it out of their own wallet. It is a transaction and not a loan, which forces the group to decide who it serves best, instead of passing the amulet from hand to hand with nobody ever paying.</p>
<p>And one line settles almost every table case: <strong>what you carry in your hand can be lent; what you carry in your head cannot.</strong> The holy water changes owner. Knowing the true name does not.</p>
<p>Equipment that breaks the Grid —the railgun that punches through a tank— is also bought with Keys, and has its three locks in <a href="#ch4-equipo">4.3</a>.</p>
"""

X100_EN = r"""
<div class="rule">
<p class="rule-title">One level is two zeros</p>
<p>Every rung of the Grid multiplies your <strong>reach</strong> by a hundred: how many people you get to, how big a problem you touch, how much world you move at once. <span class="flag ed">ED-29</span></p>
<div class="tw"><table class="t">
<thead><tr><th>Level</th><th class="num">Reach</th><th>The image</th></tr></thead>
<tbody>
<tr><td>1</td><td class="num">×1</td><td>One person</td></tr>
<tr><td>2</td><td class="num">×100</td><td>A full room</td></tr>
<tr><td>3</td><td class="num">×10,000</td><td>A building, a district</td></tr>
<tr><td>4</td><td class="num">×1,000,000</td><td>A city</td></tr>
<tr><td>5</td><td class="num">×100,000,000</td><td>A country</td></tr>
</tbody></table></div>
<p>The rungs were already there —person, room, building, city, country—; the number just puts itself in front of them. And with the number in front, this chapter’s hard rule stops looking arbitrary: when someone has a level on you they are not “better than you”, they are playing with <strong>two more zeros</strong>. That is why there is no roll.</p>
<p><strong>It is reach, not literal truth.</strong> A Physical 2 does not lift a hundred times more weight or run a hundred times faster: they face a hundred times more world at once. The number is an image, not a conversion table. The moment someone asks “so how much does that weigh?”, the answer is “whatever the scene needs”.</p>
<p>And it makes the Key more dramatic: what you buy with it is fighting <strong>a hundred times above your weight</strong>, against one specific thing.</p>
<p class="small">Optional rule: if your campaign is a back-alley one and ×100 sounds too much like comics, use <strong>×10 per level</strong>. The narrative scale does not change —you still go from the person to the country—, only the size of the astonishment. <span class="flag proposal">Unvalidated proposal</span></p>
</div>
"""

TECHO_EN = r"""
<h4>The ceiling of the universe</h4>
<p>The <strong>starting level</strong> is set by the campaign; the <strong>ceiling</strong> is set by the universe. In a cyberpunk game there is no such thing as a Mental 2, however long the campaign runs: there is no wits-times-a-hundred. What there is are chrome jobs on the edge of psychosis, who reach Physical 2, and there the genre ends. Each of the twenty recipes (<a href="#ch8-recetas">8.4</a>) carries its ceiling per sphere, and that ceiling is what makes a universe feel like that universe — more than tone, more than equipment. <span class="flag ed">ED-30</span></p>
<p>The Grid still rises with the story, but against that ceiling. And the Key is the agreed exception: <strong>in cyberpunk you cannot have wits times a hundred, but you can have the exploit that works against that AI.</strong> A ceiling with no exceptions is boring; an exception with no ceiling breaks the game. Here the ceiling is permanent and the exception is bought.</p>
"""

ECON_EN = r"""<h3 id="ch3-economia">3.5 The economy of scarcity</h3>
<p>NOGUM hands out <strong>12 skill points</strong>, or <strong>14</strong> if the universe has an Arcane sphere. The number is not a whim: without magic there are four Spheres, eight Domains and thirty-two Disciplines — forty slots; with magic there are fifty. Twelve out of forty and fourteen out of fifty are the same proportion, so the sheet feels equally scarce wherever you play. <span class="flag ed">ED-31</span></p>
<p>Twelve points force you to manage scarcity: if you want to stand out at something, they practically force you to be Null somewhere. More points open the door to sheets with no weaknesses, which are usually less interesting. But playing NOGUM is a gentlemen’s agreement: this rulebook will not devote a single line to building firewalls against foul play. The kind of characters the story calls for is agreed at the table, like adults. That said, hand out as many points as you like: the rulebook is there to fit your campaign. <span class="src">Draft, T107</span></p>

<div class="rule">
<p class="rule-title">The separate pot</p>
<p>On top of the points, every character gets <strong>a pot that does not mix</strong>: either <strong>+1 Grid level in one Sphere</strong>, or <strong>5 own Keys</strong>. There is no exchange between the two pots in either direction: points do not buy Keys and Keys do not buy points.</p>
<p>The reason is a table reason, not a mathematical one. If they could be exchanged, you would get the Grid hero with no trade and no background: someone enormous who cannot do anything, the most boring character anyone can bring to a game. By forcing all twelve points into skills, everybody turns up with a trade underneath the power.</p>
<p><strong>And the choice is not neutral.</strong> One Grid level covers a whole Sphere: its two Domains and its eight Disciplines, <strong>ten slots for five coins</strong>. A Key covers one slot for one coin. Breadth is cheap, but the universe sets its ceiling for you; freedom is expensive, but you choose it and it points at what matters to you. <strong>Freedom costs double.</strong></p>
</div>

<p>Twelve points force you to choose between being a <strong>competent generalist</strong> or a <strong>flawed specialist</strong>.</p>

<div class="example">
<p class="example-title">Case A · The action hero (specialist)</p>
<p>Wants to be the best shot (+4) and very tough (+3).</p>
<div class="tw"><table class="t">
<thead><tr><th>Purchase</th><th>Result</th><th class="num">Cost</th></tr></thead>
<tbody>
<tr><td>Physical → Vigour → Fortitude → Signature “Shrug Off Pain” (1 point)</td><td>Vigour +1 · Fortitude +2 · Shrug Off Pain +3</td><td class="num">3</td></tr>
<tr><td>Physical → Vigour (already paid) → Weapons → Signature “Pistols” (2 points)</td><td>Weapons +2 · Pistols +4</td><td class="num">3</td></tr>
<tr><td>Technical → Operations → Driving</td><td>Operations +1 · Driving +2</td><td class="num">2</td></tr>
<tr><td>Mental → Wits → Alertness</td><td>Wits +1 · Alertness +2</td><td class="num">2</td></tr>
<tr><td>Physical → Dexterity</td><td>Dexterity +1</td><td class="num">1</td></tr>
<tr><td>Mental → Wits (already paid) → Tactics</td><td>Tactics +2</td><td class="num">1</td></tr>
<tr><td>Social → nothing · Arcane → nothing</td><td>Null −2 in both</td><td class="num">0</td></tr>
<tr><td colspan="2"><strong>Total</strong></td><td class="num"><strong>12</strong></td></tr>
</tbody></table></div>
<p><strong>Separate pot:</strong> five Keys, all narrow — “Weapons against chrome jobs”, “Alertness against ambushes”, and three left unspent for session zero. Or, if he would rather be big than precise, +1 Grid in Physical and no Keys at all.</p>
<p><strong>Result:</strong> he is lethal with a gun (+4), tough (+3), can drive and is hard to surprise. But he is <strong>Null (−2)</strong> at everything social. If he has to talk a conflict down, he rolls at −2… and the situation will probably end in gunfire.</p>
<p><span class="flag ed">ED-4</span> The draft counted 4 points for the Pistols branch and used a specific model (“Colt 45”) as a +4 Signature. With one point per +1, the branch costs 3, and the +4 is the same Signature with its second point.</p>
</div>

<div class="example">
<p class="example-title">Case B · The survivor (generalist)</p>
<p>Wants to be ready for anything.</p>
<ul>
<li>Buys a Domain in every sphere (5 points): no longer Null anywhere. Rolls at +1 in their Domains and +0 at everything else.</li>
<li>Raises seven Disciplines to +2 (7 points): Athletics, Fortitude, Sciences, Alertness, Persuasion, Mechanics and Projection.</li>
<li><strong>Separate pot:</strong> +1 Grid in Social. No cleverer and no stronger than before; it is just that now a whole room listens.</li>
</ul>
<p><strong>Result:</strong> a very useful Swiss army knife, who will never shine with a +4.</p>
</div>

<div class="rule">
<p class="rule-title">What being Null costs — and the card decides it</p>
<p>To avoid being Null anywhere, one Domain in each Sphere is enough: four points in a universe without magic. That leaves eight, which is exactly <strong>two Grand Masters</strong> (Domain 1 + Discipline 1 + Signature 2 = 4 points each). The third only appears if you give up covering a whole Sphere and sit at −2 there. The system charges the toll by itself, with nothing to forbid: <strong>the price of Signatures is being Null</strong>.</p>
<p>What that toll costs you <em>at the table</em> is not decided by the sheet. It is decided by the card:</p>
<div class="tw"><table class="t">
<thead><tr><th>Card</th><th class="num">What your −2 still pulls off</th></tr></thead>
<tbody>
<tr><td>Epic · Unleashed Pulp</td><td class="num">51 %</td></tr>
<tr><td>Realist</td><td class="num">36 %</td></tr>
<tr><td>First Gear · Snowball</td><td class="num">30 %</td></tr>
<tr><td>Anguish · Nightmare</td><td class="num">9 %</td></tr>
</tbody></table></div>
<p>In an epic campaign, leaving a Sphere empty barely hurts: you still pull off half of what you attempt with it. In Anguish it is a death sentence. The very same three-mastery character is a bargain in one place and suicide in another, and that is <strong>decided by the tone, not by a creation rule</strong>.</p>
</div>
<p>The system works. You decide where to put the focus.</p>

"""

PROG_EN = r"""<h3 id="ch3-progreso">3.6 Progression: the two wallets</h3>
<p>Almost every game throws three completely different things into the same bag of points, and it shows: the level fifteen fighter is at once more skilled, more powerful in the world and more scarred, because there is only one counter. Here they are separated, and each one has a different owner.</p>
<div class="tw"><table class="t">
<thead><tr><th>What changes</th><th>Who owns it</th><th>How it moves</th></tr></thead>
<tbody>
<tr><td><strong>The world</strong> · the Grid</td><td>The Director</td><td>Not bought. It rises when the facts justify it, agreed at the table, and against the universe’s ceiling</td></tr>
<tr><td><strong>The scars</strong> · gifts and flaws</td><td>The fiction</td><td>Not bought: they happen in play</td></tr>
<tr><td><strong>Competence</strong> · points and Keys</td><td>The table</td><td>Two wallets, at a pace agreed in session zero</td></tr>
</tbody></table></div>

<h4>Two bags that grow at different rates</h4>
<p>Experience is not one counter: it is <strong>two independent wallets</strong>. <span class="flag ed">ED-33</span></p>
<ul>
<li><strong>Skill points.</strong> They buy pyramid: Domains, Disciplines and Signatures, at the same prices as at creation.</li>
<li><strong>Keys.</strong> They buy own Keys, climb the square ladder against the same thing, and pay for equipment that breaks the Grid (<a href="#ch4-equipo">4.3</a>).</li>
</ul>
<p>It is the same question asked twice, and it is worth asking twice, because the two taps do not do the same thing:</p>
<div class="rule">
<p class="rule-title">The Key wallet is the campaign’s power dial</p>
<p>Skill points only make you <strong>wider</strong>: the Anchor cuts them off at +4, so however many you hand out, nobody gets taller — only good at more things. Keys, on the other hand, open up equipment and break Grid ceilings, and that never saturates: there is always another Discipline, another scene, another object to buy.</p>
<p>That is why the default pace for Keys is <strong>slow: one per session</strong>, and it is worth being stingy with them, because many are spent on equipment. If you want the campaign to escalate, open the Key tap. If what you want is for the characters to know how to do more things, open the points tap. They are not interchangeable and should not be opened together without thinking about it.</p>
</div>

<h4>Question 1 · How do the characters grow?</h4>
<div class="tw"><table class="t">
<thead><tr><th>Option</th><th>Rule</th><th>Feels like</th></tr></thead>
<tbody>
<tr><td><strong>Still</strong></td><td>0</td><td>One-shots and campaigns where what changes is the world, not the sheet</td></tr>
<tr><td><strong>Slow</strong></td><td>+1 per arc (several sessions)</td><td>A novel: every point is noticed and remembered</td></tr>
<tr><td><strong>Fast</strong></td><td>+1 per session</td><td>A TV series: you watch them grow episode by episode</td></tr>
<tr><td><strong>Very fast</strong></td><td>+2 per session</td><td>Shōnen: by the end they can do everything</td></tr>
<tr><td><strong>In leaps</strong></td><td>+5 per arc and nothing in between</td><td>The time skip. It almost demands moving the Grid at the same time</td></tr>
</tbody></table></div>
<p>The same question, again, for Keys. By default: one per session, and if the campaign is about equipment —cyberpunk, looting, gadget superheroes— keep an eye on it, because there the Key wallet is the shop.</p>

<h4>Question 2 · Who grows?</h4>
<p>Only if the previous answer is not “still”: <strong>everyone equally</strong>, or <strong>whoever earns it in the story</strong>. And a warning that comes from many tables: handing out purely on merit makes the strong stronger and makes the table argue about who deserved it.</p>
<p>The healthy shape is for <strong>merit to add on top of a base</strong>, not to replace it. Everyone gets what the pace says, and whoever had a big moment takes +1 extra. That way the split never punishes the shy player.</p>

<h4>What gets rewarded</h4>
<p>NOGUM is a narrative rulebook and it rewards narrative. This is the short list:</p>
<ol>
<li>Resolving the arc’s central conflict.</li>
<li>Playing a flaw against your own interest when it was inconvenient.</li>
<li>Finding a Key, or giving one to someone else.</li>
<li>Paying a heavy cost for the group.</li>
<li>Closing a thread of the character’s personal story.</li>
<li>Failing memorably and owning the consequences.</li>
<li>Surviving a night on a harder card than the campaign’s.</li>
</ol>
<p>The sixth has an illustrious parent: there are games that give you experience precisely when you fail, and it is an excellent idea. Others reward using a skill until you master it, or winning fights. Those are legitimate approaches and this rulebook does not carry them because it measures something else; if your table wants them, turn them into one more entry on this list and be done with it.</p>

<div class="rule">
<p class="rule-title">Experience cannot break the maths</p>
<p>No roll goes past +4, so experience <strong>makes nobody taller: only wider</strong>. At +1 per session, twenty sessions in, a character has tripled their sheet and still does not go past +4. Growing means being good at more things, not being a god at one.</p>
<p>And there a circuit closes with the Grid: the characters widen, the Director raises the world, and the challenge comes back on its own without anybody touching a table. The warning that comes with it: in a fast-growth campaign the characters will live at +3 and +4 in their own field, and several cards lose the clean failure up there. The answer is not to cut points, it is to move the Grid. If the world does not rise, the game turns into a stroll.</p>
</div>

<h4>Gifts and flaws: not bought, they happen</h4>
<p>Advantages and disadvantages are in no pot. They appear in play, and they have a concrete mechanical origin: <strong>a flaw is the scar of a filled block</strong>. When a block of your Mental or Spiritual bar fills up and you later heal, the −2 goes away but something named stays behind: the insomnia, the debt, the tic, the fear of water. The gift works the same way from the other side, when the fiction owes you one. The details, with their thresholds and examples, are in <a href="#ch5-dano">5.5</a>. <span class="flag ed">ED-35</span></p>
<p><strong>The author’s thesis:</strong> fast growth, a bonus for good narrative play and fixed experience at campaign milestones. Milestones work as incentives; experience is there to manage the campaign’s expectations. <span class="src">T37</span></p>
</section>
"""


def patch(fn, llave, x100, techo, econ, prog):
    shutil.copyfile(fn[0], fn[0] + '.bak_llaves')
    s = io.open(fn[0], encoding='utf-8').read()
    # 2.3: antes del encabezado de 2.4
    k = s.index('<h3 id="ch2-rejilla">')
    s = s[:k] + llave + '\n' + s[k:]
    # 2.4: el x100 va delante del primer recuadro de la seccion
    k = s.index('<div class="rule">', s.index('<h3 id="ch2-rejilla">'))
    s = s[:k] + x100.strip() + '\n\n' + s[k:]
    # techo: al final de 2.4
    k = s.index('<h3 id="ch2-sintesis">')
    s = s[:k] + techo + '\n' + s[k:]
    io.open(fn[0], 'w', encoding='utf-8').write(s)

    shutil.copyfile(fn[1], fn[1] + '.bak_llaves')
    s = io.open(fn[1], encoding='utf-8').read()
    a = s.index('<h3 id="ch3-economia">')
    b = s.index('<h3 id="ch3-progreso">')
    s = s[:a] + econ + prog
    io.open(fn[1], 'w', encoding='utf-8').write(s)


patch(('frag_ch2.html', 'frag_ch3.html'), LLAVE_ES, X100_ES, TECHO_ES, ECON_ES, PROG_ES)
patch(('frag_ch2.en.html', 'frag_ch3.en.html'), LLAVE_EN, X100_EN, TECHO_EN, ECON_EN, PROG_EN)
print('bloque 1 escrito')
for f in ('frag_ch2.html', 'frag_ch2.en.html', 'frag_ch3.html', 'frag_ch3.en.html'):
    print(' ', f, os.path.getsize(f), 'bytes')
