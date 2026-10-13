# -*- coding: utf-8 -*-
"""La doctrina de las barras, tambien donde viven las barras (5.5), y en el canon."""
import io, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

ES = r"""<div class="rule">
<p class="rule-title">El nombre lo pone el género; la barra la pone la causa</p>
<p>Casi todos los géneros rebautizan una barra, y está bien: Corrupción, Humanidad, Sombra, Empatía, Honor, Sangre. Lo que no se puede elegir a gusto es <strong>de qué barra cuelga</strong>, porque de eso dependen la curación, la penalización y lo que pasa al vaciarla. <span class="flag ed">ED-39</span></p>
<p><strong>Cuerpo</strong> si lo que te gasta es físico. <strong>Mente</strong> si es cognitivo: tu cabeza rompiéndose, y nadie más vive ahí dentro. <strong>Espíritu</strong> si es sobrenatural: algo entra, algo se queda, algo te reclama, y suele tener voluntad propia.</p>
<p>El ejemplo que lo enseña todo es la <strong>Humanidad</strong>, que con el mismo nombre y casi el mismo efecto cae en barras distintas: en el gótico hay una <strong>Bestia</strong> dentro de ti que gana terreno cada vez que cedes, y eso es Espíritu; en cyberpunk no hay nadie dentro —la ciberpsicosis es tu propia cabeza dejando de reconocer a los demás—, y eso es Mente. Por eso al vampiro se le cura con rituales y arcos y al cromado con descanso y terapia.</p>
<p><strong>Y si en tu mundo no hay Arcano, no hay barra Espiritual:</strong> no está vacía, no existe, igual que el Ámbito. Lo que en otro sitio sería Espíritu cae en Mente, y la mesa pacta si esa barra puede retirar una ficha. La lista completa de nombres por género, con sus tablas de lo que se pierde, está en <a href="#ch8-tablas">las tablas de problemas</a>.</p>
</div>
"""

EN = r"""<div class="rule">
<p class="rule-title">The genre gives the name; the cause gives the bar</p>
<p>Almost every genre renames a bar, and that is fine: Corruption, Humanity, Shadow, Empathy, Honour, Blood. What cannot be chosen to taste is <strong>which bar it hangs from</strong>, because healing, penalties and what happens when it empties all depend on that. <span class="flag ed">ED-39</span></p>
<p><strong>Body</strong> if what wears you down is physical. <strong>Mind</strong> if it is cognitive: your head breaking, and nobody else lives in there. <strong>Spirit</strong> if it is supernatural: something gets in, something stays, something claims you, and it usually has a will of its own.</p>
<p>The example that teaches the whole thing is <strong>Humanity</strong>, which with the same name and almost the same effect falls under different bars: in the gothic there is a <strong>Beast</strong> inside you that gains ground every time you give in, and that is Spirit; in cyberpunk nobody is inside —cyberpsychosis is your own head ceasing to recognise other people—, and that is Mind. Which is why the vampire heals with rituals and arcs and the chrome job with rest and therapy.</p>
<p><strong>And if there is no Arcane in your world, there is no Spiritual bar:</strong> not empty, non-existent, exactly like the Sphere. Whatever would be Spirit elsewhere falls under Mind, and the table agrees whether that bar can retire a character. The full list of genre names, with their tables of what gets lost, is in <a href="#ch8-tablas">the problem tables</a>.</p>
</div>
"""

for f, txt, anchor in (('frag_ch5.html', ES, '<h4>Las palabras son armas</h4>'),
                       ('frag_ch5.en.html', EN, '<h4>Words are weapons</h4>')):
    s = io.open(f, encoding='utf-8').read()
    k = s.index(anchor)
    s = s[:k] + txt + '\n' + s[k:]
    io.open(f, 'w', encoding='utf-8').write(s)
    print(' ', f, 'ok')

f = 'CANON.md'
s = io.open(f, encoding='utf-8').read()
old = '- Marcador de disposición (autor, 17 sep):'
new = """- **ED-39. El nombre lo pone el genero; la barra la pone la causa.** Hay tres barras y no mas: Cuerpo (fisico: heridas, agotamiento), Mente (cognitivo: cordura, estres, voluntad) y Espiritu (sobrenatural). Un genero puede rebautizar una barra, pero no elegir de cual cuelga. Caso canonico, por decision del autor: la **Humanidad** es ESPIRITU en el gotico (hay una Bestia dentro, alguien que no eres tu) y MENTE en cyberpunk (la ciberpsicosis es una locura, no una posesion). Mismo nombre, casi el mismo efecto, distinta barra, y por eso distinta curacion y distinto final. Reparto: Cordura/Estres, Empatia/Ciberpsicosis, Identidad y Honor/Reputacion van a **Mente**; Humanidad/la Bestia, Corrupcion y Sombra van a **Espiritu**; Sangre/Hambre y Fatiga/Suministros van a **Cuerpo** (la Sangre es combustible, no es la Bestia).
  - Corolario: **si en el mundo no hay Arcano, no hay barra Espiritual** (no esta vacia: no existe, igual que el Ambito). Lo que seria Espiritu cae en Mente y la mesa pacta si esa barra puede retirar una ficha. Afecta a las recetas 8 (Empatia) y 9 (Identidad), que pasan de Espiritual a Mental.
- Marcador de disposición (autor, 17 sep):"""
assert old in s
s = s.replace(old, new)
io.open(f, 'w', encoding='utf-8').write(s)
print('canon ok')

f = 'frag_editorial.html'
s = io.open(f, encoding='utf-8').read()
ROW = """<tr><td class="num"><span class="flag ed">ED-39</span></td><td><strong>El nombre lo pone el género; la barra la pone la causa.</strong> Corrección del autor sobre un borrador que colgaba Empatía e Identidad de la barra Espiritual por costumbre. Hay tres barras —Cuerpo, Mente y Espíritu— y el género puede rebautizarlas, pero no elegir de cuál cuelgan. El caso que lo enseña es la Humanidad: en el gótico hay una Bestia dentro y eso es Espíritu; en cyberpunk no hay nadie dentro, la ciberpsicosis es una locura, y eso es Mente. Y el corolario que ordena medio capítulo 8: <strong>sin Arcano no hay barra Espiritual</strong>, igual que no hay Ámbito.</td><td><a href="#ch5-dano">5.5</a></td></tr>
"""
anchor = '<tr><td>El menú de la pifia</td>'
assert anchor in s
s = s.replace(anchor, ROW + anchor)
io.open(f, 'w', encoding='utf-8').write(s)
print('cuaderno ok')
