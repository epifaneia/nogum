# -*- coding: utf-8 -*-
"""Bloque 2: los tres cerrojos del equipo (4.3), el dano mental y espiritual con
la lacra (5.5), el catalogo ampliado de consecuencias (5.6) y el titulo del 7.3."""
import io, os, shutil
os.chdir(os.path.dirname(os.path.abspath(__file__)))

CERROJOS_ES = r"""
<h4>Los tres cerrojos del equipo</h4>
<p>Que algo acabe escrito en tu ficha no es solo cuestión de dinero. Son tres permisos, y la ficha técnica de cada objeto (<a href="#apx-bazar">8.3</a>) dice cuáles te pide: <span class="flag ed">ED-34</span></p>
<ol>
<li><strong>El dinero</strong>, que aquí es tu nivel en <em>Recursos</em> (Social → Jerarquía → Recursos). Cada objeto trae su <span class="tag">Acceso N</span>: lo cotidiano pide 0, el arma seria 1, el material militar 2, y lo que no debería existir 3. Si no llegas, no es que sea caro: es que no está a tu alcance, y conseguirlo es una trama.</li>
<li><strong>El permiso narrativo</strong>: que tenga sentido que eso esté en tus manos aquí y ahora.</li>
<li><strong>El permiso del ritmo</strong>: si el objeto rompe la Rejilla —lleva <span class="tag">Rejilla: Llave Nx</span>— cuesta además <strong>x² Llaves</strong> de tu monedero, la misma escalera cuadrada de <a href="#ch2-llave">2.3</a>. Un cañón de riel, que es Llave N3, cuesta nueve Llaves.</li>
</ol>
<p>El tercer cerrojo cierra un agujero clásico. Sin él, una pistola de catálogo regala gratis lo que un personaje paga con nueve Llaves. Con él, el cañón de riel sigue siendo brutal y quien pagó las suyas no se siente estafado.</p>
<div class="rule">
<p class="rule-title">Lo robado funciona una escena</p>
<p>Un arma robada, prestada o conseguida en la ficción <strong>se usa una escena entera sin pagar nada</strong>. Le quitas el cañón de riel al mercenario muerto, lo usas, y al acabar la escena decides: o gastas las Llaves y es tuyo, o lo dejas tirado.</p>
<p>Así el saqueo vuelve a ser una decisión en vez de una escalada, que es el problema clásico de todos los juegos con catálogo de equipo. Y encaja con la distinción de las Llaves: la Llave del equipo es la que <strong>se puede perder</strong> —vive en el objeto, te la quitan, se gasta, se rompe—; la Llave propia es la que <strong>eres tú</strong>.</p>
</div>
"""

CERROJOS_EN = r"""
<h4>The three locks on equipment</h4>
<p>Getting something written on your sheet is not only a question of money. It is three permissions, and each object’s spec sheet (<a href="#apx-bazar">8.3</a>) says which ones it asks of you: <span class="flag ed">ED-34</span></p>
<ol>
<li><strong>The money</strong>, which here is your level in <em>Resources</em> (Social → Hierarchy → Resources). Every object carries its <span class="tag">Access N</span>: everyday things ask for 0, a serious weapon 1, military hardware 2, and what should not exist at all 3. If you fall short it is not that it is expensive: it is out of your reach, and getting hold of it is a plot.</li>
<li><strong>Narrative permission</strong>: that it makes sense for this to be in your hands here and now.</li>
<li><strong>The permission of pace</strong>: if the object breaks the Grid —it carries <span class="tag">Grid: Key Nx</span>— it also costs <strong>x² Keys</strong> from your wallet, the same square ladder as in <a href="#ch2-llave">2.3</a>. A railgun, which is Key N3, costs nine Keys.</li>
</ol>
<p>The third lock closes a classic hole. Without it, a catalogue pistol hands out for free what a character pays nine Keys for. With it, the railgun is still brutal and whoever paid for theirs does not feel cheated.</p>
<div class="rule">
<p class="rule-title">Looted gear works for one scene</p>
<p>A weapon stolen, borrowed or obtained in the fiction <strong>can be used for a whole scene without paying anything</strong>. You take the railgun off the dead merc, you use it, and when the scene ends you decide: either you spend the Keys and it is yours, or you leave it on the floor.</p>
<p>That turns looting back into a decision instead of an escalation, which is the classic problem of every game with an equipment catalogue. And it fits the distinction between Keys: the equipment Key is the one that <strong>can be lost</strong> —it lives in the object, it can be taken, spent or broken—; your own Key is the one that <strong>is you</strong>.</p>
</div>
"""

DANO_ES = r"""
<h4>Qué hace de verdad el daño mental y el espiritual</h4>
<p>La barra es la misma y los umbrales son los mismos; lo que cambia es qué significa llenarlos. Esta es la lectura por bloque, para que el Director no tenga que improvisar dos veces la misma escena:</p>
<div class="tw"><table class="t">
<thead><tr><th>Bloque</th><th>Mental (estrés, cordura)</th><th>Espiritual (esencia, corrupción)</th></tr></thead>
<tbody>
<tr><td><strong>1 · Sano</strong><br><small>sin penalización</small></td><td>Se nota, pero aguantas: fumas más, hablas de menos, repasas la escena por la noche. Es color, no mecánica.</td><td>Algo se ha enfriado. Duermes mal, las oraciones suenan huecas, el animal de la casa te rehúye.</td></tr>
<tr><td><strong>2 · Herido −2</strong><br><small>primer bloque lleno</small></td><td>Evitas lo que te rompió. No puedes mentir con soltura, ni liderar, ni fingir calma: cualquier acción que exija serenidad va a −2.</td><td>La corrupción es visible para quien sabe mirar. Los símbolos sagrados molestan, los poderes salen torcidos, la gente se aparta sin saber por qué.</td></tr>
<tr><td><strong>3 · Crítico −4</strong><br><small>segundo bloque lleno</small></td><td>Paranoia o colapso. No aceptas ayuda, o no distingues amigo de amenaza. Las acciones complejas se caen solas.</td><td>Ya no eres del todo tuyo: el Director dicta una de tus acciones por escena, o tus poderes cobran el doble.</td></tr>
<tr><td><strong>Llena</strong></td><td>Fuera de la escena: pánico, catatonia, crisis. No es muerte; es que ya no puedes participar.</td><td>El personaje pasa a manos del Director como monstruo, villano o avatar, y <strong>solo si se pactó</strong> (ED-12).</td></tr>
</tbody></table></div>
<p>Un detalle que importa en mesa: la penalización de las tres barras es la misma y <strong>no se suma tres veces</strong>. Si vas Herido en Física y en Mental, sigues a −2, no a −4. Lo que empeora no es el número: es que hay tres formas distintas de quedarte fuera, y los enemigos listos eligen la que tienes más llena.</p>

<div class="rule">
<p class="rule-title">La lacra es la cicatriz de un bloque lleno</p>
<p>Las ventajas y las desventajas no se compran en ningún bote (<a href="#ch3-progreso">3.6</a>): ocurren. Y ocurren aquí. <strong>Cuando se te llena un bloque de la barra Mental o Espiritual y luego te curas, el menos dos se va pero queda algo con nombre.</strong> <span class="flag ed">ED-35</span></p>
<p>Ese algo es la lacra: el insomnio, la deuda, el tic, el miedo al agua, el nombre que no puedes pronunciar. No lleva número; lleva consecuencias. Y el día que la juegues en contra tuya cuando no te convenía, es una de las siete cosas que esta mesa premia.</p>
<p>El don funciona igual por el otro lado, cuando la ficción te lo debe: la cicatriz que te hace reconocible, el favor del moribundo, la calma rara de quien ya ha estado allí.</p>
</div>
"""

DANO_EN = r"""
<h4>What mental and spiritual damage actually does</h4>
<p>The bar is the same and the thresholds are the same; what changes is what filling them means. This is the reading block by block, so the Director does not have to improvise the same scene twice:</p>
<div class="tw"><table class="t">
<thead><tr><th>Block</th><th>Mental (stress, sanity)</th><th>Spiritual (essence, corruption)</th></tr></thead>
<tbody>
<tr><td><strong>1 · Healthy</strong><br><small>no penalty</small></td><td>It shows, but you are holding: you smoke more, talk less, replay the scene at night. Colour, not mechanics.</td><td>Something has gone cold. You sleep badly, prayers ring hollow, the house animal avoids you.</td></tr>
<tr><td><strong>2 · Wounded −2</strong><br><small>first block full</small></td><td>You avoid whatever broke you. You cannot lie smoothly, lead, or fake calm: any action that needs composure takes −2.</td><td>The corruption is visible to anyone who knows how to look. Holy symbols bother you, powers come out crooked, people step aside without knowing why.</td></tr>
<tr><td><strong>3 · Critical −4</strong><br><small>second block full</small></td><td>Paranoia or collapse. You refuse help, or you cannot tell friend from threat. Complex actions fall apart on their own.</td><td>You are no longer entirely your own: the Director dictates one of your actions per scene, or your powers charge double.</td></tr>
<tr><td><strong>Full</strong></td><td>Out of the scene: panic, catatonia, breakdown. Not death; you simply cannot take part any more.</td><td>The character passes into the Director’s hands as monster, villain or avatar, and <strong>only if it was agreed</strong> (ED-12).</td></tr>
</tbody></table></div>
<p>One detail that matters at the table: the penalty is the same on all three bars and <strong>it does not stack three times</strong>. If you are Wounded in Physical and in Mental, you are still at −2, not −4. What gets worse is not the number: it is that there are three different ways to be taken out, and clever enemies aim at whichever bar is fullest.</p>

<div class="rule">
<p class="rule-title">A flaw is the scar of a filled block</p>
<p>Advantages and disadvantages are not bought from any pot (<a href="#ch3-progreso">3.6</a>): they happen. And they happen here. <strong>When a block of your Mental or Spiritual bar fills up and you later heal, the minus two goes away but something named stays behind.</strong> <span class="flag ed">ED-35</span></p>
<p>That something is the flaw: the insomnia, the debt, the tic, the fear of water, the name you cannot say out loud. It carries no number; it carries consequences. And the day you play it against your own interest when it did not suit you, it is one of the seven things this table rewards.</p>
<p>The gift works the same way from the other side, when the fiction owes you one: the scar that makes you recognisable, the dying man’s favour, the strange calm of someone who has already been there.</p>
</div>
"""

# -- 5.6: la lista ampliada que estaba pendiente
AMPL_ES = r"""
<h4>Cinco ejemplos por umbral</h4>
<p>La lista corta de arriba es la que se usa en mesa; esta es la despensa, para no repetir siempre «ojo hinchado». Tira una, o elige la que encaje con cómo te han golpeado.</p>
<div class="tw"><table class="t">
<thead><tr><th>Barra</th><th>Umbral 1 · Herida moderada (−2)</th><th>Umbral 2 · Herida grave (−4)</th></tr></thead>
<tbody>
<tr><td><strong>Física</strong></td><td>Ojo hinchado (falla la percepción) · Mano rota (nada a dos manos) · Costillas fisuradas (no puedes correr ni gritar) · Tobillo torcido (mitad de movimiento) · Sordera de un oído (pierdes la dirección del sonido)</td><td>Hemorragia arterial (cuenta atrás de 3 turnos) · Pierna inútil (movimiento 0) · Brazo colgando (una sola mano para todo) · Pulmón perforado (una frase por turno) · Conmoción (confundes el orden de lo que pasa)</td></tr>
<tr><td><strong>Mental</strong></td><td>Temblor (nada de Sigilo ni de pulso fino) · Duda (no puedes liderar) · Flashback (pierdes el primer turno de cada combate) · Tartamudeo (no puedes mentir con soltura) · Fijación (solo ves la amenaza que te rompió)</td><td>Paranoia (no aceptas ayuda de aliados) · Alucinaciones (el Director decide si lo que ves está ahí) · Mutismo (no hablas, escribes) · Furia (atacas a lo más cercano si te hieren) · Disociación (narras en tercera persona; no te importa tu propio cuerpo)</td></tr>
<tr><td><strong>Espiritual</strong></td><td>Aura gris (los animales te rehúyen) · Mala suerte (el Director repite una tirada contra ti por escena) · Sin reflejo (los espejos y las cámaras te odian) · Insomnio (no recuperas en descansos cortos) · Nombre marcado (los seres del otro lado saben cómo llamarte)</td><td>Posesión parcial (el Director dicta una de tus acciones por escena) · Vacío mágico (tus poderes cuestan el doble) · Hambre (necesitas algo que no deberías necesitar) · Sombra ajena (tu sombra no hace lo que tú) · Pacto abierto (algo tiene derecho a pedirte un favor)</td></tr>
</tbody></table></div>
<p>En tono épico se eligen las vistosas y se curan con una cerveza; en una partida sucia se eligen las que estorban y tardan semanas. La misma tabla sirve para las dos mesas porque lo que cambia no es la lista: es cuánto dura.</p>
"""

AMPL_EN = r"""
<h4>Five examples per threshold</h4>
<p>The short list above is the one used at the table; this is the pantry, so that it is not always “swollen eye”. Roll one, or pick whichever fits how you were hit.</p>
<div class="tw"><table class="t">
<thead><tr><th>Bar</th><th>Threshold 1 · Moderate wound (−2)</th><th>Threshold 2 · Severe wound (−4)</th></tr></thead>
<tbody>
<tr><td><strong>Physical</strong></td><td>Swollen eye (perception fails) · Broken hand (nothing two-handed) · Cracked ribs (no running, no shouting) · Twisted ankle (half movement) · Deaf in one ear (you lose the direction of sound)</td><td>Arterial bleeding (3-turn countdown) · Useless leg (movement 0) · Hanging arm (one hand for everything) · Punctured lung (one sentence per turn) · Concussion (you confuse the order of events)</td></tr>
<tr><td><strong>Mental</strong></td><td>Tremor (no Stealth, no fine control) · Doubt (you cannot lead) · Flashback (you lose the first turn of every fight) · Stammer (you cannot lie smoothly) · Fixation (you only see the threat that broke you)</td><td>Paranoia (you refuse help from allies) · Hallucinations (the Director decides whether what you see is there) · Mutism (you do not speak, you write) · Fury (you attack whatever is nearest if wounded) · Dissociation (you narrate in the third person; your own body stops mattering)</td></tr>
<tr><td><strong>Spiritual</strong></td><td>Grey aura (animals avoid you) · Bad luck (the Director rerolls one roll against you per scene) · No reflection (mirrors and cameras hate you) · Insomnia (short rests no longer heal you) · Marked name (things on the other side know what to call you)</td><td>Partial possession (the Director dictates one of your actions per scene) · Magical void (your powers cost double) · Hunger (you need something you should not need) · Borrowed shadow (your shadow does not follow you) · Open pact (something has the right to ask you a favour)</td></tr>
</tbody></table></div>
<p>In an epic tone you pick the showy ones and they heal with a beer; in a dirty game you pick the ones that get in the way and they take weeks. The same table serves both because what changes is not the list: it is how long it lasts.</p>
"""


def do(es):
    sfx = '' if es else '.en'
    # ---- 4.3
    f = 'frag_ch4%s.html' % sfx
    shutil.copyfile(f, f + '.bak_eq')
    s = io.open(f, encoding='utf-8').read()
    k = s.index('<h3 id="ch4-modificadores">')
    s = s[:k] + (CERROJOS_ES if es else CERROJOS_EN) + '\n' + s[k:]
    io.open(f, 'w', encoding='utf-8').write(s)

    # ---- 5.5 y 5.6
    f = 'frag_ch5%s.html' % sfx
    shutil.copyfile(f, f + '.bak_eq')
    s = io.open(f, encoding='utf-8').read()
    k = s.index('<h3 id="ch5-consecuencias">')
    s = s[:k] + (DANO_ES if es else DANO_EN) + '\n' + s[k:]
    # la lista ampliada, al final de 5.6, y se retira el pendiente
    old_es = 'La lista ampliada (cinco ejemplos por umbral y ámbito) está por escribir. <span class="flag pending">Pendiente</span>'
    old_en = 'The expanded list (five examples per threshold and sphere) is yet to be written. <span class="flag pending">Pending</span>'
    old = old_es if es else old_en
    if old in s:
        s = s.replace(old, '')
    else:
        print('  aviso: no estaba el pendiente de 5.6 en', f)
    k = s.index('<h4>Curación</h4>' if es else '<h4>Healing</h4>')
    s = s[:k] + (AMPL_ES if es else AMPL_EN) + '\n' + s[k:]
    # la tarjeta 3 ya no existe
    s = s.replace('(Tarjeta 3 y recetas de caos alto)', '(Pulp desenfrenado, Bola de nieve y cualquier receta de caos alto)')
    s = s.replace('(Card 3 and high-chaos recipes)', '(Unleashed Pulp, Snowball and any high-chaos recipe)')
    io.open(f, 'w', encoding='utf-8').write(s)

    # ---- 7.3: el titulo chocaba con la curva de crecimiento de verdad
    f = 'frag_ch67%s.html' % sfx
    shutil.copyfile(f, f + '.bak_eq')
    s = io.open(f, encoding='utf-8').read()
    if es:
        s = s.replace('7.3 La curva de crecimiento (las tres velocidades)', '7.3 Las tres velocidades del tono')
    else:
        s = s.replace('7.3 The growth curve (the three speeds)', '7.3 The three speeds of tone')
    io.open(f, 'w', encoding='utf-8').write(s)


do(True)
do(False)
print('bloque 2 escrito')
