import os
D = os.path.dirname(os.path.abspath(__file__))
def W(n, s): open(os.path.join(D, n), 'w', encoding='utf-8').write(s)
def R(n): return open(os.path.join(D, n), encoding='utf-8').read()

MAP_ES = """<h3 id="inicio-mapa">Mapa rápido del sistema</h3>
<div class="tw"><table class="t">
<thead><tr><th>Pieza</th><th>Qué controla</th><th>Dónde</th></tr></thead>
<tbody>
<tr><td><strong>La Sesión 0</strong></td><td>El pacto de la mesa: las líneas rojas de cada uno, qué se va a sentir y qué soluciones pide el género.</td><td><a href="#ch0">Capítulo 0</a></td></tr>
<tr><td><strong>El Motor</strong>: Optimismo y Caos</td><td>Cómo se leen los dos d10 y, con ello, cómo se siente la escena.</td><td><a href="#ch1">Capítulo 1</a> · <a href="#ch1-panel">Tarjetas de tono</a></td></tr>
<tr><td><strong>El Ancla</strong>: competencia de −2 a +4</td><td>Lo bueno que eres. Nunca cambia con el género.</td><td><a href="#ch2-competencia">2.1</a> · <a href="#ch3">Capítulo 3</a></td></tr>
<tr><td><strong>La Vela</strong>: Rejilla 1–5</td><td>Lo grandes que son tus hazañas: habitación, oficina, edificio, ciudad, nación.</td><td><a href="#ch2-escala">2.2</a> · <a href="#ch2-llave">La Llave</a></td></tr>
<tr><td><strong>El Fractal</strong>: vida de 3, 9 o 27</td><td>Cuánto duele un golpe: la letalidad como dial de tono.</td><td><a href="#ch5-vida">5.4</a></td></tr>
<tr><td><strong>La Consola</strong></td><td>Cuándo y cómo cambiar el tono: por campaña, sesión, escena o personaje.</td><td><a href="#ch7">Capítulo 7</a></td></tr>
</tbody></table></div>"""
MAP_EN = """<h3 id="inicio-mapa">Quick map of the system</h3>
<div class="tw"><table class="t">
<thead><tr><th>Piece</th><th>What it controls</th><th>Where</th></tr></thead>
<tbody>
<tr><td><strong>Session Zero</strong></td><td>The table’s agreement: everyone’s red lines, what is going to be felt and what solutions the genre asks for.</td><td><a href="#ch0">Chapter 0</a></td></tr>
<tr><td><strong>The Engine</strong>: Optimism and Chaos</td><td>How the two d10 are read and, with that, how the scene feels.</td><td><a href="#ch1">Chapter 1</a> · <a href="#ch1-panel">Tone Cards</a></td></tr>
<tr><td><strong>The Anchor</strong>: competence from −2 to +4</td><td>How good you are. It never changes with the genre.</td><td><a href="#ch2-competencia">2.1</a> · <a href="#ch3">Chapter 3</a></td></tr>
<tr><td><strong>The Sail</strong>: Power Grid 1–5</td><td>How big your deeds are: room, office, building, city, nation.</td><td><a href="#ch2-escala">2.2</a> · <a href="#ch2-llave">The Key</a></td></tr>
<tr><td><strong>The Fractal</strong>: health of 3, 9 or 27</td><td>How much a hit hurts: lethality as a tone dial.</td><td><a href="#ch5-vida">5.4</a></td></tr>
<tr><td><strong>The Desk</strong></td><td>When and how to change tone: per campaign, session, scene or character.</td><td><a href="#ch7">Chapter 7</a></td></tr>
</tbody></table></div>"""

def cover(h2, kicker, official, official_lang, jokes, lede):
    lang = f' lang="{official_lang}"' if official_lang else ''
    first = jokes.split('|')[0]
    return f"""<section class="cover" id="portada">
<h2>{h2}</h2>
<div class="acro">
<p class="acro-kicker">{kicker}</p>
<p class="acro-letters">N·O·G·U·M</p>
<p class="acro-official"{lang}>{official}</p>
<p class="acro-joke"><button type="button" class="joke" data-jokes="{jokes}">({first})</button></p>
</div>
<p class="lede">{lede}</p>
</section>
"""
J_ES_JOKES = "Nos Olvidamos de Guardar Una Mesa|Narrativa Orgánica para Gamers Ultra Motivados|No Otro Gato Usando Magia"
J_EN_JOKES = "No One Gets Ur Mechanics|Not Our Game, U Mad?|Narrative Orgasm Generates Ultimate Mayhem"

W('p3_juego.es.html', cover('Juego completo', 'Edición en español · Manual del sistema', 'Narrative Ontology &amp; General Universal Mechanics', 'en', J_ES_JOKES, 'Donde la emoción dicta la física.') + """<section class="chapter" id="como-leer">
<h2>Cómo leer este manual</h2>
<p>El reglamento completo: el motor de tono, la Rejilla de Potencia, la creación de personajes, el combate y los apéndices con el Bazar del Multiverso y las 20 recetas.</p>
<div class="legend">
<span><span class="flag ed">ED-n</span> decisión editorial de congruencia</span>
<span><span class="flag proposal">Propuesta sin validar</span> idea no aprobada por el autor</span>
<span><span class="flag pending">Pendiente</span> hueco abierto</span>
<span><span class="src">T68</span> turno de origen</span>
</div>
""" + MAP_ES + "\n</section>\n")

W('p3_juego.en.html', cover('Complete Game', 'English edition · System rulebook', 'Narrativa Ontológica General Universal y Metafísica', 'es', J_EN_JOKES, 'Where emotion dictates physics.') + """<section class="chapter" id="como-leer">
<h2>How to read this rulebook</h2>
<p>The complete rules: the tone engine, the Power Grid, character creation, combat, and the appendices with the Multiverse Bazaar and the 20 recipes.</p>
<div class="legend">
<span><span class="flag ed">ED-n</span> editorial decision for consistency</span>
<span><span class="flag proposal">Unvalidated proposal</span> idea not approved by the author</span>
<span><span class="flag pending">Pending</span> open gap</span>
<span><span class="src">T68</span> source turn</span>
</div>
""" + MAP_EN + "\n</section>\n")

W('p3_acel.es.html', cover('NOGUM Acelerado', 'Protocolo de inmersión inmediata', 'Acelerado', '', 'Juega ahora, pregúntate por qué funciona luego|Nos Olvidamos de Guardar Una Mesa|No Otro Gato Usando Magia',
  'Un juego completo y sencillo para empezar esta misma tarde: cuatro modos de tono, una sola dificultad y nueve casillas de vida —tres en Terror—. Cuando se te quede pequeño, NOGUM te estará esperando.'))
W('p3_acel.en.html', cover('NOGUM Accelerated', 'Immediate immersion protocol', 'Accelerated', '', 'Play now, wonder why it works later|No One Gets Ur Mechanics|Not Our Game, U Mad?',
  'A complete, simple game you can start this very evening: four tone modes, one difficulty and nine health boxes —three in Terror—. When you outgrow it, NOGUM will be waiting.'))

for n in ['p_tesis_es.html', 'p_tesis_en.html']:
    W(n.replace('p_', 'p3_'), R(n).replace('class="chapter cover"', 'class="cover"'))

W('p3_cuaderno.es.html', """<section class="cover" id="portada">
<h2>Cuaderno de edición</h2>
<div class="acro">
<p class="acro-kicker">Documento interno · No es un producto</p>
<p class="acro-letters">N·O·G·U·M</p>
<p class="acro-official">Cuaderno de edición</p>
</div>
<p class="lede">Cómo se consolidó el material: 145 turnos de conversación (10 de febrero – 24 de mayo), el borrador del autor y trece fichas de resumen.</p>
</section>
<section class="chapter" id="resumen">
<h2>Resumen del proceso</h2>
<div class="tw"><table class="t">
<thead><tr><th>Paso</th><th>Qué contiene</th></tr></thead>
<tbody>
<tr><td><strong>1 · Auditoría de versiones</strong></td><td>%%N_DROP%% conceptos descartados, agrupados por área, con turno y motivo, y una lista de control final (<a href="#audit-descartados">Descartados</a>).</td></tr>
<tr><td><strong>2 · Trazabilidad</strong></td><td>Cronología por sesiones, hilos de cada requisito y cuestiones abiertas (<a href="#audit-traza">Trazabilidad</a>).</td></tr>
<tr><td><strong>3 · Núcleo final</strong></td><td>Los manuales consolidados: Tesis, Juego completo y Acelerado. Cada conflicto resuelto lleva su marca ED y se explica en <a href="#audit-editorial">Decisiones editoriales</a>.</td></tr>
</tbody></table></div>
<div class="legend">
<span><span class="flag ed">ED-n</span> decisión editorial</span>
<span><span class="flag proposal">Propuesta sin validar</span></span>
<span><span class="flag pending">Pendiente</span></span>
<span><span class="flag drop">Descartado</span></span>
<span><span class="src">T68</span> turno de origen</span>
</div>
</section>
""")
print('covers ok')
