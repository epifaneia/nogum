# -*- coding: utf-8 -*-
"""Recuadro de la fila opresiva, canon, cuaderno, Acelerado y recordatorios de la app."""
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


# ---------------- 1.4: de dónde viene la fila opresiva ----------------
patch('write_tono.py', [
    ("""    h.append('<div class="rule"><p class="rule-title">%s</p><p>%s</p></div>' % (
        t('Una receta aparte: la Tragedia', 'A recipe apart: Tragedy'),""",
     """    h.append('<div class="rule"><p class="rule-title">%s</p><p>%s</p></div>' % (
        t('De dónde viene la fila opresiva', 'Where the oppressive row comes from'),
        t('No es una esquina teórica del mapa: es la emulación de una familia que existe y se juega. Fíjate en lo que hace la Angustia —9&nbsp;% con −2, 25&nbsp;% con 0, 49&nbsp;% con +2 y 81&nbsp;% con +4— y compáralo con La Llamada de Cthulhu, donde una habilidad sin entrenar anda por el 5–20&nbsp;%, un investigador corriente por el 25–35&nbsp;% y un especialista en lo suyo por el 70–80&nbsp;%. Es la misma distribución. Lo que allí se guarda en la ficha, aquí se guarda en la tarjeta, y por eso puedes entrar y salir de ese tono sin reescribir un personaje. La diferencia está en el reparto: allí el especialista tiene su rincón donde sí acierta, y aquí la tirada es igual de dura para todos. Por eso funciona mejor en formato corto —una noche, un acto, una escena—, igual que Ten Candles, Dread o Trophy, que llegan al mismo sitio por otro camino. Avísalo antes de empezar.',
          'It is not a theoretical corner of the map: it is the emulation of a family of games that exists and gets played. Look at what Anguish does —9&nbsp;% at −2, 25&nbsp;% at 0, 49&nbsp;% at +2 and 81&nbsp;% at +4— and compare it with Call of Cthulhu, where an untrained skill sits around 5–20&nbsp;%, an ordinary investigator around 25–35&nbsp;% and a specialist in their field around 70–80&nbsp;%. It is the same distribution. What is stored in the character sheet there is stored in the card here, which is why you can step in and out of that tone without rewriting a character. The difference is the spread: there the specialist has their corner where they do land things, and here the roll is equally hard for everyone. That is why it works better in short form —one night, one act, one scene— just like Ten Candles, Dread or Trophy, which get to the same place by another road. Say so before you start.')))
    h.append('<div class="rule"><p class="rule-title">%s</p><p>%s</p></div>' % (
        t('Una receta aparte: la Tragedia', 'A recipe apart: Tragedy'),"""),
])

# ---------------- canon ----------------
c = io.open('CANON.md', encoding='utf-8').read()
if 'ED-25' not in c:
    a = '- **Tarjetas retiradas**'
    NEW = """- **ED-25 (la defensa gana los empates)**: atacante y defensor tiran contra la misma TN y se comparan NIVELES, nunca totales ni márgenes (ED-17 sigue en pie). Defensor iguala o supera → sin daño. Atacante por encima con defensor en éxito o éxito con coste → daño −1. Defensor falla → daño completo. Defensor pifia → el ataque sube un escalón en la escala de la tarjeta activa (fallo→éxito o →con coste; éxito→crítico; el crítico es el techo) y luego se comparan. LAS ETIQUETAS MANDAN SOBRE EL EMPATE: Esq Parcial obliga a un mínimo de 1 aunque empates; Esq Nula impide la reacción. Defensa con coste: reduce como éxito (−1) y el DJ cobra un precio. Doble pifia: manda la del atacante, no conecta. Consecuencia medida: con la Primera marcha y los dos a +1, el defensor iguala o supera el 68 % de las veces, así que los duelos con Esq Total se alargan y los tiroteos con Esq Nula o Parcial siguen siendo letales. Esto convierte las etiquetas de esquiva en la principal superficie de equilibrio del juego.
- **ED-26 (el Estilo nunca cuesta)**: en las tarjetas con éxito con coste, esa banda se lee como éxito en la tirada de Estilo, porque el Estilo se tira cuando ya no se puede fallar. Resultados: pifia = lo consigues pero te ves ridículo (sin daño de estrés; se retira esa propuesta del borrador); fallo = lo consigues de la forma más olvidable, quizá nadie miraba; éxito = molas muchísimo; crítico = lúcete, describe la escena, y el DJ puede dar una ventaja temporal si encaja.
- **Menú de la pifia (seis puertas)**: se cierra un camino · se gasta algo que no se repone · dejas un rastro · la amenaza se acerca un paso · se rompe lo que llevas · alguien se fija en ti. En la columna previsible la pifia CIERRA una puerta; en la caótica ABRE una rama. Misma frecuencia, distinto tamaño.
- **La fila opresiva es material de simulación**, no una esquina teórica: la Angustia (9/25/49/81) reproduce la distribución de La Llamada de Cthulhu y Warhammer. Lo que allí vive en la ficha, aquí vive en la tarjeta, y por eso se puede entrar y salir del tono sin rehacer personajes. Diferencia clave: allí el especialista se escapa del pesimismo en su rincón; aquí no se escapa nadie, y por eso conviene el formato corto (como Ten Candles, Dread o Trophy).
- **Tarjetas retiradas**"""
    c = c.replace(a, NEW, 1)
    io.open('CANON.md', 'w', encoding='utf-8').write(c)

# ---------------- cuaderno ----------------
e = io.open('frag_editorial.html', encoding='utf-8').read()
if 'ED-25' not in e:
    ROWS = """<tr><td class="num"><span class="flag ed">ED-25</span></td><td><strong>La defensa gana los empates.</strong> Se comparan niveles, no totales, así que la tirada enfrentada sigue retirada (ED-17). Si el defensor iguala al atacante no hay daño; si el atacante queda por encima, −1; si el defensor pifia, el ataque sube un escalón. Las etiquetas mandan sobre el empate, y ahí está la diferencia entre un duelo y un tiroteo. Consecuencia medida: con la Primera marcha y los dos a +1, el defensor iguala o supera el 68&nbsp;% de las veces, de modo que las peleas con esquiva Total se vuelven coreografía larga y las armas con Esq Nula o Parcial recuperan el miedo.</td><td><a href="#ch5-golpes">5.2</a></td></tr>
<tr><td class="num"><span class="flag ed">ED-26</span></td><td><strong>El Estilo nunca cuesta.</strong> En las tarjetas con éxito con coste, esa banda se lee como éxito en la tirada de Estilo: se tira precisamente cuando ya no se puede fallar. Se reescriben los cuatro resultados con las palabras del autor y se retira el daño de estrés por ridículo que proponía el borrador.</td><td><a href="#ch4-malla">4.5</a></td></tr>
<tr><td>El menú de la pifia</td><td>Seis puertas para no improvisar a pelo cuando una de cada cinco tiradas se estrella: se cierra un camino, se gasta algo que no se repone, dejas un rastro, la amenaza se acerca, se rompe lo que llevas, alguien se fija en ti. Con la regla de tamaño: en la columna previsible la pifia cierra una puerta; en la caótica abre una rama.</td><td><a href="#ch5-golpes">5.2</a></td></tr>
<tr><td>La fila opresiva, situada</td><td>No es una esquina teórica del cuadrante: la Angustia reproduce la distribución de La Llamada de Cthulhu y Warhammer (9 · 25 · 49 · 81&nbsp;%). Lo que allí se guarda en la ficha, aquí se guarda en la tarjeta, y por eso se entra y se sale del tono sin rehacer personajes. La diferencia está en el reparto, y por eso el aviso de formato corto.</td><td><a href="#ch1-panel">1.4</a></td></tr>
"""
    anchor = '</tbody></table></div>\n\n<h3 id="ed-abiertas">'
    assert e.count(anchor) == 1
    io.open('frag_editorial.html', 'w', encoding='utf-8').write(e.replace(anchor, ROWS + anchor))

# ---------------- Acelerado ----------------
patch('frag_acelerado.html', [
    ('<p><strong>En Agobio</strong>, un éxito parcial en combate cuenta como éxito, pero el DJ añade un coste del menú',
     '<p><strong>La defensa gana los empates.</strong> Los dos tiráis contra la misma TN: si el defensor iguala el nivel del atacante o lo supera, no hay daño; si el atacante queda por encima, el daño baja en 1; si el defensor pifia, el ataque sube un escalón. Y las etiquetas mandan sobre el empate: con <span class="tag">Esq: Parcial</span> comes al menos 1 aunque iguales, y con <span class="tag">Esq: Nula</span> no hay reacción que tirar.</p>\n<p><strong>En Agobio</strong>, un éxito parcial en combate cuenta como éxito, pero el DJ añade un coste del menú'),
])
patch('frag_acelerado.en.html', [
    ('<p><strong>In Dread</strong>, a partial success in combat counts as a success, but the GM adds a cost from the menu',
     '<p><strong>The defender wins ties.</strong> You both roll against the same TN: if the defender matches the attacker’s level or beats it, there is no damage; if the attacker ends up above, damage drops by 1; if the defender fumbles, the attack goes up one step. And tags override the tie: with <span class="tag">Dodge: Partial</span> you eat at least 1 even when you match it, and with <span class="tag">Dodge: None</span> there is no reaction to roll.</p>\n<p><strong>In Dread</strong>, a partial success in combat counts as a success, but the GM adds a cost from the menu'),
])

# ---------------- app: recordatorios ----------------
patch('app4_body.html', [
    ("'<li>' + esc(t('Defenderse: esquivar o absorber, si el arma lo permite. Éxito −1, crítico −2.','Defend: dodge or soak, if the weapon allows it. Success −1, critical −2.')) + '</li>'",
     "'<li>' + esc(t('Defenderse: si igualas el nivel del atacante o lo superas, no hay daño. Si él queda por encima, daño −1. Si pifias, el ataque sube un escalón.','Defend: if you match the attacker’s level or beat it, no damage. If they end up above, damage −1. If you fumble, the attack goes up one step.')) + '</li><li>' + esc(t('Las etiquetas mandan sobre el empate: Esq Parcial come 1 como mínimo, Esq Nula no deja reaccionar.','Tags override the tie: Partial dodge always eats at least 1, None allows no reaction.')) + '</li>'"),
    ("(estilo() ? '<li>' + esc(t('Estilo +2: contra enemigos menores ganas seguro; la tirada dice cómo de bien quedas.','Style +2: against lesser foes you win for sure; the roll says how good you look.')) + '</li>' : '')",
     "(estilo() ? '<li>' + esc(t('Estilo +2: contra enemigos menores ganas seguro y nunca cuesta; la tirada dice cómo quedas. Pifia: ridículo. Fallo: olvidable. Éxito: molas. Crítico: lúcete.','Style +2: against lesser foes you win for sure and it never costs; the roll says how you look. Fumble: ridiculous. Failure: forgettable. Success: magnificent. Critical: show off.')) + '</li>' : '')"),
])
print('faltan:', MISS if MISS else 'nada')
