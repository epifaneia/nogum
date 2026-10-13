# -*- coding: utf-8 -*-
"""El Acceso explicado donde se explica la ficha tecnica: 5.3 y la entrada del Bazar."""
import io, os, shutil
os.chdir(os.path.dirname(os.path.abspath(__file__)))

ROW_ES = r"""<tr><td rowspan="2"><span class="tag">Acceso N</span><br><small>¿Está a tu alcance?</small></td><td>0 · 1 · 2 · 3</td><td>Nivel de <em>Recursos</em> que hace falta para tenerlo: 0 cotidiano, 1 arma seria, 2 material militar, 3 lo que no debería existir. Es el primero de los tres cerrojos del equipo (<a href="#ch4-equipo">4.3</a>).</td><td>Bate (0), escopeta (2), rifle antimaterial (3)</td></tr>
<tr><td>N Llaves</td><td>Si el objeto rompe la Rejilla, además cuesta Llaves de tu monedero: el cuadrado del nivel al que llega.</td><td>Coche (N2, 4 Llaves), cañón de riel (N3, 9 Llaves)</td></tr>
"""

ROW_EN = r"""<tr><td rowspan="2"><span class="tag">Access N</span><br><small>Is it within your reach?</small></td><td>0 · 1 · 2 · 3</td><td>The level of <em>Resources</em> you need to have it: 0 everyday, 1 serious weapon, 2 military hardware, 3 what should not exist. It is the first of the three locks on equipment (<a href="#ch4-equipo">4.3</a>).</td><td>Baseball bat (0), shotgun (2), anti-materiel rifle (3)</td></tr>
<tr><td>N Keys</td><td>If the object breaks the Grid, it also costs Keys from your wallet: the square of the level it reaches.</td><td>Car (N2, 4 Keys), railgun (N3, 9 Keys)</td></tr>
"""

NOTAG_ES = r"""<div class="rule">
<p class="rule-title">Lo que no lleva etiqueta no es un ataque</p>
<p>Las tres etiquetas de combate solo tienen sentido en algo que hace daño. Una linterna, una cuerda o un mapa no llevan <span class="tag">Esq</span> ni <span class="tag">Abs</span> porque no atacan a nadie; si alguien usa la palanca como arma, se lee <span class="tag">Esq: Total</span> <span class="tag">Abs: Total</span>, que es el valor por defecto de cualquier cosa que no diga lo contrario.</p>
<p>Y con la regla de que <strong>la defensa gana los empates</strong> (5.2), estas tres etiquetas han pasado a ser la principal superficie de equilibrio del juego: un arma de <span class="tag">Esq: Total</span> se para casi siempre y una de <span class="tag">Esq: Nula</span> no se para nunca. Ahí está la diferencia entre un duelo largo y un tiroteo corto, y por eso conviene elegirlas con cuidado al inventar un arma nueva.</p>
</div>
"""

NOTAG_EN = r"""<div class="rule">
<p class="rule-title">Anything without tags is not an attack</p>
<p>The three combat tags only make sense on something that does damage. A torch, a rope or a map carry no <span class="tag">Dodge</span> or <span class="tag">Soak</span> because they attack nobody; if someone swings the crowbar as a weapon, read it as <span class="tag">Dodge: Full</span> <span class="tag">Soak: Full</span>, which is the default value of anything that does not say otherwise.</p>
<p>And with the rule that <strong>defence wins ties</strong> (5.2), these three tags have become the game’s main balance surface: a <span class="tag">Dodge: Full</span> weapon is stopped almost every time and a <span class="tag">Dodge: None</span> one is never stopped. That is the difference between a long duel and a short gunfight, which is why they are worth choosing carefully when you invent a new weapon.</p>
</div>
"""

DL_ES = r"""<dt><span class="tag">Acceso N</span> · <span class="tag">N Llaves</span></dt>
<dd>Lo que te cuesta tenerlo. <strong>Acceso</strong> es el nivel de <em>Recursos</em> (Social → Jerarquía → Recursos) que hace falta para que ese objeto esté a tu alcance: 0 cotidiano, 1 arma seria, 2 material militar, 3 lo que no debería existir. Y si el objeto rompe la Rejilla, cuesta además <strong>Llaves</strong> de tu monedero (<a href="#ch4-equipo">4.3</a>). Los Accesos de este catálogo están derivados del daño y de la rareza en una sola pasada: el Director puede mover cualquiera un escalón sin que se rompa nada.</dd>
"""

DL_EN = r"""<dt><span class="tag">Access N</span> · <span class="tag">N Keys</span></dt>
<dd>What it costs you to have it. <strong>Access</strong> is the level of <em>Resources</em> (Social → Hierarchy → Resources) you need for that object to be within your reach: 0 everyday, 1 serious weapon, 2 military hardware, 3 what should not exist. And if the object breaks the Grid, it also costs <strong>Keys</strong> from your wallet (<a href="#ch4-equipo">4.3</a>). The Access values in this catalogue were derived from damage and rarity in a single pass: the Director can move any of them one step without breaking anything.</dd>
"""

PODERES_ES = r"""<p><strong>Las tablas de poderes no llevan Acceso.</strong> La Fuerza, el ki, las disciplinas de sangre, los superpoderes, los poderes toon y el arsenal social no se compran con dinero: describen lo que ya eres, según tu Rejilla y tu ficha. Por eso en esas tablas la última columna solo habla de niveles y efectos. Y un objeto que la ficción te regala como ambientación —el coche de la familia, el caballo del pueblo— es decorado: solo cuesta Llaves el día que lo compras como el arma de nivel que es.</p>
"""

PODERES_EN = r"""<p><strong>The power tables carry no Access.</strong> The Force, ki, blood disciplines, superpowers, toon powers and the social arsenal are not bought with money: they describe what you already are, according to your Grid and your sheet. That is why in those tables the last column only talks about levels and effects. And an object the fiction hands you as scenery —the family car, the village horse— is scenery: it only costs Keys the day you buy it as the levelled weapon it is.</p>
"""


def do(es):
    # --- 5.3
    f = 'frag_ch5%s.html' % ('' if es else '.en')
    shutil.copyfile(f, f + '.bak_acc')
    s = io.open(f, encoding='utf-8').read()
    anchor = '<tr><td>Ignora todo</td>' if es else '<tr><td>Ignores everything</td>'
    if anchor not in s:
        raise SystemExit('ancla de 5.3 no encontrada en ' + f)
    i = s.index(anchor)
    j = s.index('</tr>', i) + 5
    s = s[:j] + '\n' + (ROW_ES if es else ROW_EN) + s[j:]
    k = s.index('<p>Catálogo completo' if es else '<p>Full catalogue')
    s = s[:k] + (NOTAG_ES if es else NOTAG_EN) + s[k:]
    io.open(f, 'w', encoding='utf-8').write(s)

    # --- entrada del Bazar
    for f in (['frag_bazar.html'] if es else ['frag_bazar_a.en.html']):
        shutil.copyfile(f, f + '.bak_acc2')
        s = io.open(f, encoding='utf-8').read()
        k = s.index('</dl>')
        s = s[:k] + (DL_ES if es else DL_EN) + s[k:]
        k = s.index('</dl>') + 5
        s = s[:k] + '\n' + (PODERES_ES if es else PODERES_EN) + s[k:]
        s = s.replace('significa usar la tarjeta Gonzo (T5)', 'significa usar la tarjeta Bola de nieve')
        s = s.replace('means using the Gonzo card (T5)', 'means using the Snowball card')
        io.open(f, 'w', encoding='utf-8').write(s)


do(True)
do(False)
print('ficha tecnica documentada en 5.3 y en el Bazar')
