# -*- coding: utf-8 -*-
"""Las mismas seis decisiones, en ingles."""
import io, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

SUBS = {
 'frag_ch2.en.html': [
  ('<p class="small">Optional rule: if your campaign is a back-alley one and ×100 sounds too much like comics, use <strong>×10 per level</strong>. The narrative scale does not change —you still go from the person to the country—, only the size of the astonishment. <span class="flag proposal">Unvalidated proposal</span></p>',
   '<p class="small"><strong>There is no ×10 version.</strong> A tenfold jump is exactly what already separates a −2 from a +4: the pyramid buys that, not the Grid. ×100 sounds like comics because it <em>is</em> comics, and if it gets out of hand in your campaign the answer is not to shrink the scale: it is to <strong>leave everybody at Grid 1 and play with skill points</strong>. For everything in between there is the small Key: a computer with a connection lets you shut down a whole building without being level 3.</p>'),
  ('<p>Rick Sanchez (<em>Rick and Morty</em>) creates universes with his intellect: he is level 5 “if not 6”. <span class="flag pending">Pending</span></p>',
   '<p>The scientist who travels between worlds and creates universes with his intellect is level 5, “if not 6”. <span class="src">Table approved by the author</span></p>'),
  ('<li><strong>Grid budgets by campaign type.</strong> Street-level [1,1,1,1,1]; Action heroes [2,1,1,1,1]; Legends [3,2,2,1,1]. <span class="flag proposal">Unvalidated proposal</span>',
   '<li><strong>The starting spread is [2,1,1,1,1]</strong>, and the 2 is not freely chosen: it is <strong>the only one the universe allows</strong>, the one the recipe’s ceiling names (<a href="#ch8-recetas">8.4</a>). In cyberpunk that 2 is the chrome job’s Physical; in a game of courts, the Social. <strong>If you do not want that 2, you take 5 Keys instead</strong> (<a href="#ch3-economia">3.5</a>): either you are big where your world lets you be big, or you are small and very specific at whatever you choose. <span class="src">Author’s decision</span>'),
 ],
 'frag_ch4.en.html': [
  ('Recovering health or stress with a Style critical is an idea the author never got round to validating. <span class="flag proposal">Unvalidated proposal</span>',
   '<strong>A Style critical does not heal.</strong> Recovering health with a flourish makes no sense; stress can be negotiated at the table, but never automatically, and the specific effect is decided by the Director together with the player. <span class="src">Author’s decision</span>'),
 ],
 'frag_ch5.en.html': [
  ('<p>Fixed initiative for NPCs (12 for mooks, 16 for bosses). <span class="flag proposal">Unvalidated proposal</span></p>',
   '<p><strong>No fixed initiative.</strong> NPCs declare a stance and roll too: it is an opposed roll using the skill of the chosen stance, and mooks carry their two or three basic numbers so it can be settled without a sheet. <span class="src">Author’s decision</span></p>'),
  ('Exactly what is needed to be able to soak (is toughness enough, or is armour required?) has not been decided. <span class="flag pending">Pending</span>',
   '<strong>You always soak with the skill</strong>, armour or no armour: the body is the first protection. What decides whether it helps are the weapon’s tags —<span class="tag">Soak: Max N</span> and <span class="tag">Soak: None</span>, which is where “this goes through your skin” lives— and whatever bonus your protection adds. By default, normal. <span class="src">Author’s decision</span>'),
 ],
}
for f, subs in SUBS.items():
    s = io.open(f, encoding='utf-8').read()
    for a, b in subs:
        n = s.count(a)
        print('%-20s %d  %s' % (f, n, a[:50]))
        s = s.replace(a, b)
    io.open(f, 'w', encoding='utf-8').write(s)

# ---- el bote aparte: el +1 de Rejilla ya no es libre
BOTE = [
 ('frag_ch3.html',
  ('o <strong>+1 nivel de Rejilla en un Ámbito</strong>, o <strong>5 Llaves propias</strong>',
   'o <strong>+1 nivel de Rejilla</strong> —en el único Ámbito que tu universo permite, el que marca el techo de la receta—, o <strong>5 Llaves propias</strong>')),
 ('frag_ch3.en.html',
  ('either <strong>+1 Grid level in one Sphere</strong>, or <strong>5 own Keys</strong>',
   'either <strong>+1 Grid level</strong> —in the one Sphere your universe allows, the one the recipe’s ceiling names—, or <strong>5 own Keys</strong>')),
 ('frag_acelerado.html',
  ('<tr><td>Bote aparte</td><td>+1 nivel de Rejilla en un ámbito <strong>o</strong> 5 Llaves. No se cambia por puntos.</td></tr>',
   '<tr><td>Bote aparte</td><td>+1 nivel de Rejilla en el ámbito que permita tu mundo <strong>o</strong> 5 Llaves. No se cambia por puntos.</td></tr>')),
 ('frag_acelerado.en.html',
  ('<tr><td>Separate pot</td><td>+1 Grid level in one sphere <strong>or</strong> 5 Keys. It does not trade for points.</td></tr>',
   '<tr><td>Separate pot</td><td>+1 Grid level in whichever sphere your world allows <strong>or</strong> 5 Keys. It does not trade for points.</td></tr>')),
]
for f, (a, b) in BOTE:
    s = io.open(f, encoding='utf-8').read()
    print('%-22s %d  bote' % (f, s.count(a)))
    io.open(f, 'w', encoding='utf-8').write(s.replace(a, b))
