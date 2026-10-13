# -*- coding: utf-8 -*-
"""La regla de la Parca en el 5.3, y los ejemplos grandes en el catalogo generico."""
import io, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
fal = []


def sub(f, a, b, n=1):
    s = io.open(f, encoding='utf-8').read()
    if s.count(a) != n:
        fal.append('%s (%d!=%d) %s' % (f, s.count(a), n, a[:58])); return
    io.open(f, 'w', encoding='utf-8').write(s.replace(a, b, n))


# ------------------------------------------------- 1. la fila de Dano 3 se va
sub('frag_ch5.html',
    '<tr><td>3 · Masivo</td><td>«A comer con San Pedro»: fuera de combate en escala sucia.</td><td>Explosivos, armas pesadas, magia de guerra, caídas de 20 m</td></tr>',
    '<tr><td><strong>La Parca</strong></td><td>No tacha casillas: las tacha <em>todas</em>. No es un valor de daño, es otra cosa; se explica debajo.</td><td>Artillería, explosivos de guerra, un coche a toda velocidad, la caída de verdad</td></tr>')
sub('frag_ch5.en.html',
    '<tr><td>3 · Massive</td><td>“Off to meet Saint Peter”: out of the fight on the gritty scale.</td><td>Explosives, heavy weapons, battle magic, 20 m falls</td></tr>',
    '<tr><td><strong>The Reaper</strong></td><td>It does not cross boxes: it crosses <em>all</em> of them. It is not a damage value, it is another thing; explained below.</td><td>Artillery, war explosives, a car at full speed, a real fall</td></tr>')

# ------------------------------------------------- 2. la regla, detras de la tabla
ANC_ES = '<p><span class="flag drop">Descartado</span> Los tipos de daño con nombre (Sucio, Letal, Absoluto)'
PARCA_ES = """<h4 id="ch5-parca">La Parca: lo que no es un arma</h4>
<p><strong>El daño máximo de un arma es 2.</strong> Ese es el techo, y es a propósito: 1 y 2 son <em>el daño que tiene sentido tirar</em>. Un arma de guerra se distingue de un cuchillo por sus otras tres etiquetas —no se esquiva, no se absorbe, llega lejos—, no por un número más grande.</p>
<p>Lo que está por encima no es un arma mejor: es <strong>un acontecimiento</strong>. Un cañón de asedio, un coche a ciento veinte, el aliento de un dragón, una bomba. A eso lo llamamos <strong>la Parca</strong>, y funciona como la Rejilla, no como el daño:</p>
<div class="rule"><p class="rule-title">La Parca</p>
<p>Cada Parca lleva un <strong>nivel de Rejilla</strong>. Contra quien esté <strong>por debajo</strong> de ese nivel no hay tirada de daño: <strong>muere</strong>, o queda fuera de la historia de la forma que corresponda a esa barra. Contra quien esté <strong>a su altura o por encima</strong>, hace <strong>Daño 2</strong> y se juega como cualquier otro golpe.</p>
<p>Es la misma frase de siempre (<a href="#ch2-llave">2.4</a>): por debajo del nivel es imposible, y la Llave es la excepción pactada. Aquí lo imposible es sobrevivir.</p></div>
<p><strong>Esto no se esquiva: se evita.</strong> La Parca no es un problema de combate, es un problema de ficción. No se resuelve con una tirada mejor, se resuelve no estando ahí, cortándole la mecha, convenciendo a quien la dispara o subiendo de Rejilla antes de que llegue. Un Director que apunta con una Parca a un personaje que no la aguanta no está proponiendo un combate: está anunciando una muerte. Que se note en la mesa, y que se vea venir.</p>
<p><strong>Y existe en las cuatro barras.</strong> La Parca física te mata. La <strong>social</strong> te mata la cara: hay pruebas, y mañana no eres nadie. La <strong>mental</strong> te mata la cabeza. La <strong>espiritual</strong> te mata eso que llevas dentro, se llame como se llame en tu mundo. No vacía la barra: la <strong>tacha</strong>.</p>
<p class="note">En el Mundo Animado la Parca también existe y también mata — durante dos viñetas. El yunque cae, el personaje queda plano, y en la escena siguiente está entero. Ahí lo que se tacha es la dignidad.</p>
"""
ANC_EN = '<p><span class="flag drop">Dropped</span> The named damage types (Dirty, Lethal, Absolute)'
PARCA_EN = """<h4 id="ch5-parca">The Reaper: what is not a weapon</h4>
<p><strong>A weapon’s maximum damage is 2.</strong> That is the ceiling, and it is deliberate: 1 and 2 are <em>the damage it makes sense to roll for</em>. A weapon of war is told apart from a knife by its other three tags —no dodging, no soaking, long reach— not by a bigger number.</p>
<p>What lies above that is not a better weapon: it is <strong>an event</strong>. A siege gun, a car at seventy, a dragon’s breath, a bomb. We call that <strong>the Reaper</strong>, and it works like the Grid, not like damage:</p>
<div class="rule"><p class="rule-title">The Reaper</p>
<p>Every Reaper carries a <strong>Grid level</strong>. Against anyone <strong>below</strong> that level there is no damage roll: they <strong>die</strong>, or leave the story in whatever way that track implies. Against anyone <strong>at that level or above</strong>, it deals <strong>Damage 2</strong> and plays like any other blow.</p>
<p>It is the same old sentence (<a href="#ch2-llave">2.4</a>): below the level it is impossible, and the Key is the agreed exception. Here, what is impossible is surviving.</p></div>
<p><strong>This is not dodged: it is avoided.</strong> The Reaper is not a combat problem, it is a fiction problem. It is not solved with a better roll; it is solved by not being there, by cutting the fuse, by talking down whoever is holding it, or by climbing the Grid before it arrives. A Director who points a Reaper at a character who cannot take it is not proposing a fight: they are announcing a death. Let that show at the table, and let it be seen coming.</p>
<p><strong>And it exists on all four tracks.</strong> The physical Reaper kills you. The <strong>social</strong> one kills your face: there is evidence, and tomorrow you are nobody. The <strong>mental</strong> one kills your head. The <strong>spiritual</strong> one kills whatever you carry inside, whatever your world calls it. It does not empty the track: it <strong>crosses it out</strong>.</p>
<p class="note">In the Animated World the Reaper exists too, and it kills too — for two panels. The anvil falls, the character goes flat, and in the next scene they are whole. What gets crossed out there is their dignity.</p>
"""
for f, anc, txt in (('frag_ch5.html', ANC_ES, PARCA_ES), ('frag_ch5.en.html', ANC_EN, PARCA_EN)):
    sub(f, anc, txt + anc)

# ------------------- 3. la Parca grande, en el catalogo generico de piezas sueltas
NUEVAS_ES = """<tr><td><strong>La bomba de los mil soles</strong></td><td><span class="tag parca">La Parca · Rejilla 4</span></td><td><span class="tag">Esq: Nula</span></td><td><span class="tag">Abs: Nula</span></td><td><span class="tag">Acceso 3</span> <span class="tag">16 Llaves</span> <span class="tag">Rejilla: Nivel 4</span></td><td>Borra una ciudad. No es equipo de personaje: es un argumento. Normalmente está en manos de alguien a quien hay que convencer.</td></tr>
<tr><td><strong>La luna que no era una luna</strong></td><td><span class="tag parca">La Parca · Rejilla 5</span></td><td><span class="tag">Esq: Nula</span></td><td><span class="tag">Abs: Nula</span></td><td><span class="tag">Acceso —</span> <span class="tag">25 Llaves</span> <span class="tag">Rejilla: Nivel 5</span></td><td>Apunta a un país entero y lo apaga. Nadie la aguanta. Se juega buscando el tubo de escape.</td></tr>
<tr><td><strong>La lanza que cae del cielo</strong></td><td><span class="tag parca">La Parca · Rejilla 4</span></td><td><span class="tag">Esq: Nula</span></td><td><span class="tag">Abs: Nula</span></td><td><span class="tag">Acceso 3</span> <span class="tag">16 Llaves</span> <span class="tag">Rejilla: Nivel 4</span></td><td>Un poste de metal soltado desde muy arriba. Sin explosivo, sin aviso y sin discusión.</td></tr>
<tr><td><strong>La lista</strong></td><td><span class="tag parca">La Parca · Rejilla 3</span></td><td><span class="tag">Esq: Nula</span></td><td><span class="tag">Abs: Nula</span></td><td><span class="tag">Acceso 2</span> <span class="tag">9 Llaves</span> <span class="tag">Rejilla: Nivel 3</span></td><td>Parca social: tu nombre aparece donde no debía, con fechas. No te matan; dejas de existir para quien decide.</td></tr>
<tr><td><strong>Lo que viste de verdad</strong></td><td><span class="tag parca">La Parca · Rejilla 3</span></td><td><span class="tag">Esq: Nula</span></td><td><span class="tag">Abs: Nula</span></td><td><span class="tag">Acceso —</span> <span class="tag">9 Llaves</span> <span class="tag">Rejilla: Nivel 3</span></td><td>Parca mental o espiritual: lo entiendes del todo, de una vez y para siempre. Lo de antes no vuelve.</td></tr>
"""
NUEVAS_EN = """<tr><td><strong>The bomb of a thousand suns</strong></td><td><span class="tag parca">The Reaper · Grid 4</span></td><td><span class="tag">Dodge: None</span></td><td><span class="tag">Soak: None</span></td><td><span class="tag">Access 3</span> <span class="tag">16 Keys</span> <span class="tag">Grid: Level 4</span></td><td>It erases a city. This is not character equipment: it is a plot. It is usually in the hands of somebody who has to be talked round.</td></tr>
<tr><td><strong>The moon that was not a moon</strong></td><td><span class="tag parca">The Reaper · Grid 5</span></td><td><span class="tag">Dodge: None</span></td><td><span class="tag">Soak: None</span></td><td><span class="tag">Access —</span> <span class="tag">25 Keys</span> <span class="tag">Grid: Level 5</span></td><td>It points at a whole country and switches it off. Nobody survives it. You play it looking for the exhaust port.</td></tr>
<tr><td><strong>The spear that falls from the sky</strong></td><td><span class="tag parca">The Reaper · Grid 4</span></td><td><span class="tag">Dodge: None</span></td><td><span class="tag">Soak: None</span></td><td><span class="tag">Access 3</span> <span class="tag">16 Keys</span> <span class="tag">Grid: Level 4</span></td><td>A metal post dropped from very high up. No explosive, no warning and no argument.</td></tr>
<tr><td><strong>The list</strong></td><td><span class="tag parca">The Reaper · Grid 3</span></td><td><span class="tag">Dodge: None</span></td><td><span class="tag">Soak: None</span></td><td><span class="tag">Access 2</span> <span class="tag">9 Keys</span> <span class="tag">Grid: Level 3</span></td><td>A social Reaper: your name turns up where it should not, with dates. They do not kill you; you stop existing for whoever decides.</td></tr>
<tr><td><strong>What you really saw</strong></td><td><span class="tag parca">The Reaper · Grid 3</span></td><td><span class="tag">Dodge: None</span></td><td><span class="tag">Soak: None</span></td><td><span class="tag">Access —</span> <span class="tag">9 Keys</span> <span class="tag">Grid: Level 3</span></td><td>A mental or spiritual Reaper: you understand it completely, all at once and for good. What you were before does not come back.</td></tr>
"""
for f, nom, filas in (('frag_bazar.html', 'Arma de asedio', NUEVAS_ES),
                      ('frag_bazar_b.en.html', 'Siege weapon', NUEVAS_EN)):
    s = io.open(f, encoding='utf-8').read()
    i = s.find('<strong>' + nom + '</strong>')
    if i < 0:
        fal.append('%s: no encuentro %s' % (f, nom)); continue
    j = s.find('</tr>', i) + 5
    io.open(f, 'w', encoding='utf-8').write(s[:j] + '\n' + filas + s[j:])
    print('  %s: cinco Parca grandes anadidas' % f)

if fal:
    print('FALLOS:')
    for x in fal:
        print('  ' + x)
    sys.exit(1)
print('la regla de la Parca escrita')
