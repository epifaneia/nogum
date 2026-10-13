# -*- coding: utf-8 -*-
"""La 15 sale, Mundodisco entra como 20, y la critica pasa a ser la del ciberpunk."""
import io, os, re, shutil
os.chdir(os.path.dirname(os.path.abspath(__file__)))

CRIT_ES = """<h4>Receta de crítica y mejora: «Alta tecnología, baja esperanza, dados equivocados»</h4>
<p>Algunas adaptaciones reales emularon un lore con la herramienta equivocada. Estas fichas dicen, sin rodeos, cómo debería haberse hecho. <span class="src">T122</span> <span class="src">T123</span></p>

<div class="recipe">
<p class="recipe-title">«ALTA TECNOLOGÍA, BAJA ESPERANZA, DADOS EQUIVOCADOS»</p>
<p class="recipe-ref">Ref: los manuales clásicos de cromo y alquiler · Alias: la ciudad que te cobra por respirar</p>
<p><strong>El diagnóstico:</strong> el género promete una cosa —que cada trabajo salga <em>casi</em> bien y la factura llegue después— y el motor entrega otra: una simulación letal y realista donde el plan sale o no sale, y si no sale, te mueres. Con esas reglas, la mesa aprende rápido que lo rentable es no arriesgar, y una partida de cromo en la que nadie arriesga es una partida de contabilidad. El fallo no es la letalidad: es que <strong>la letalidad sin «sí, pero» convierte el género en un simulador de evitar escenas</strong>.</p>
<p><strong>La solución NOGUM:</strong> esto pide <strong>Bola de nieve</strong> y no Realista. El dado rojo con éxito con coste y bandas anchas da exactamente lo que el género quiere: el trabajo sale, y sale con una deuda, un testigo, un implante que falla o un cadáver que no estaba en el plan. La letalidad no se quita, se mueve de sitio: va al <strong>zoom</strong> (La Cáscara, un golpe decide) y a las <strong>etiquetas</strong>, no a la probabilidad de acertar.</p>
<p><strong>Regla de oro, la factura:</strong> en esta receta el Director no puede decir «no pasa nada». Cada éxito con coste deja algo escrito en la ficha o en la ciudad, y a las tres sesiones los personajes ya no deciden por lo que quieren, sino por lo que deben. Eso es ciberpunk.</p>
<p class="recipe-canon">En el canon: Bola de nieve, zoom La Cáscara, la barra Mental llamada Humanidad (ED-39), el menú de los cuatro costes (5.6) como lista de facturas, y el equipo con sus tres cerrojos (<a href="#ch4-equipo">4.3</a>), que es donde el género vive: querer el cañón de riel y no poder pagarlo es la trama.</p>
<p class="recipe-grid"><strong>Techos de Rejilla</strong> <span class="small">(Fís · Men · Soc · Téc · Arc)</span>: <strong>2 · 1 · 4 · 2 · —</strong>. Los mismos que la receta 8: lo que cambia aquí no es el mundo, es el motor con el que se juega.</p>
</div>

<p>Y la otra adaptación que se hizo con la herramienta equivocada ya no está aquí: <strong>el mundo sostenido por quelonios es ahora la receta 20</strong>, con su diagnóstico intacto, porque además de crítica es una de las veinte que más se juegan.</p>
"""

CRIT_EN = """<h4>Critique-and-improvement recipe: “High tech, low hope, wrong dice”</h4>
<p>Some real adaptations emulated a lore with the wrong tool. These sheets say, bluntly, how it should have been done. <span class="src">T122</span> <span class="src">T123</span></p>

<div class="recipe">
<p class="recipe-title">“HIGH TECH, LOW HOPE, WRONG DICE”</p>
<p class="recipe-ref">Ref: the classic chrome-and-rent rulebooks · Alias: the city that charges you for breathing</p>
<p><strong>The diagnosis:</strong> the genre promises one thing —that every job comes off <em>almost</em> right and the bill arrives later— and the engine delivers another: a lethal, realistic simulation where the plan either works or it does not, and if it does not, you die. With those rules the table learns fast that the profitable move is not to take risks, and a chrome game where nobody takes risks is a bookkeeping game. The flaw is not the lethality: it is that <strong>lethality without “yes, but” turns the genre into a scene-avoidance simulator</strong>.</p>
<p><strong>The NOGUM fix:</strong> this calls for <strong>Snowball</strong>, not Realist. The red die with success at a cost and wide bands gives exactly what the genre wants: the job comes off, and it comes off with a debt, a witness, a failing implant or a body that was not in the plan. Lethality is not removed, it is moved: it goes to the <strong>zoom</strong> (The Shell, one blow decides) and to the <strong>tags</strong>, not to the odds of hitting.</p>
<p><strong>Golden rule, the bill:</strong> in this recipe the Director cannot say “nothing happens”. Every success at a cost leaves something written on the sheet or on the city, and three sessions in, the characters no longer decide by what they want but by what they owe. That is cyberpunk.</p>
<p class="recipe-canon">In canon: Snowball, The Shell zoom, the Mental bar called Humanity (ED-39), the menu of the four costs (5.6) as a list of bills, and equipment with its three locks (<a href="#ch4-equipo">4.3</a>), which is where the genre lives: wanting the railgun and not being able to pay for it is the plot.</p>
<p class="recipe-grid"><strong>Grid ceilings</strong> <span class="small">(Phy · Men · Soc · Tec · Arc)</span>: <strong>2 · 1 · 4 · 2 · —</strong>. The same as recipe 8: what changes here is not the world, it is the engine it is played with.</p>
</div>

<p>And the other adaptation made with the wrong tool is no longer here: <strong>the world on the back of chelonians is now recipe 20</strong>, with its diagnosis intact, because besides being a critique it is one of the twenty most played.</p>
"""


def quitar_15(s, titulo):
    i = s.find(titulo)
    assert i > 0, titulo
    a = s.rfind('<div class="recipe">', 0, i)
    b = s.find('</div>', s.find('recipe-grid', i)) + len('</div>')
    return s[:a] + s[b:]


def renumerar(s, pares):
    for viejo, nuevo in pares:
        s = s.replace(viejo, nuevo)
    return s


def mover_quelonios(s, cab, marca_ini, titulo_nuevo, bloque_fin, crit):
    """Saca la ficha de Mundodisco de la seccion de critica y la deja como receta 20."""
    i = s.find(cab)
    assert i > 0, cab
    j = s.find('<div class="recipe">', i)
    k = s.find('</div>', s.find('recipe-grid', j)) + len('</div>')
    ficha = s[j:k]
    s = s[:i] + crit + s[k:]
    ficha = ficha.replace(marca_ini, titulo_nuevo, 1)
    p = s.find(bloque_fin)
    assert p > 0, bloque_fin
    return s[:p] + ficha + '\n\n' + s[p:]


# ---------------- castellano
f = 'frag_cap8.html'
shutil.copyfile(f, f + '.bak_20')
s = io.open(f, encoding='utf-8').read()
s = quitar_15(s, '15. «CAZADORES ADOLESCENTES»')
s = renumerar(s, [('16. «LADRONES EN LA NIEBLA»', '15. «LADRONES EN LA NIEBLA»'),
                  ('17. «DIOSES EN PIJAMA Y PROBLEMAS ÉTICOS»', '16. «DIOSES EN PIJAMA Y PROBLEMAS ÉTICOS»'),
                  ('18. «EL TORNEO DE ARTES MARCIALES (GRITANDO)»', '17. «EL TORNEO DE ARTES MARCIALES (GRITANDO)»'),
                  ('19. «ROBOTS GIGANTES Y ANGUSTIA ADOLESCENTE»', '18. «ROBOTS GIGANTES Y ANGUSTIA ADOLESCENTE»'),
                  ('20. «LA DISTOPÍA HILARANTE»', '19. «LA DISTOPÍA HILARANTE»')])
s = mover_quelonios(s, '<h4>Receta de crítica y mejora: «El mundo sostenido por quelonios»</h4>',
                    '«EL MUNDO SOSTENIDO POR QUELONIOS»', '20. «EL MUNDO SOSTENIDO POR QUELONIOS»',
                    '<aside class="meta"><p>El autor tiene esta receta blindada', CRIT_ES)
# los numeros que citaba el baul
s = renumerar(s, [('<td>3, 16</td>', '<td>3, 15</td>'), ('<td>Flashbacks</td><td>16</td>', '<td>Flashbacks</td><td>15</td>'),
                  ('<td>Transformación</td><td>18</td>', '<td>Transformación</td><td>17</td>'),
                  ('<td>Sincronización</td><td>19</td>', '<td>Sincronización</td><td>18</td>'),
                  ('<td>Clones</td><td>20</td>', '<td>Clones</td><td>19</td>'),
                  ('<td>El DJ tira en oculto</td><td>20</td>', '<td>El DJ tira en oculto</td><td>19</td>'),
                  ('<em>Recetas:</em> 16 («Ladrones en la niebla»)', '<em>Recetas:</em> 15 («Ladrones en la niebla»)'),
                  ('<em>Recetas:</em> 18 («El torneo', '<em>Recetas:</em> 17 («El torneo'),
                  ('<em>Recetas:</em> 20 («La distopía', '<em>Recetas:</em> 19 («La distopía'),
                  ('Recetas: 20 («La distopía hilarante»)', 'Recetas: 19 («La distopía hilarante»)')])
io.open(f, 'w', encoding='utf-8').write(s)
print('ES: recetas reordenadas')

# ---------------- ingles
f = 'frag_cap8.en.html'
shutil.copyfile(f, f + '.bak_20')
s = io.open(f, encoding='utf-8').read()
s = quitar_15(s, '15. “TEENAGE SLAYERS WITH HOMEWORK”')
s = renumerar(s, [('16. “THIEVES IN THE FOG”', '15. “THIEVES IN THE FOG”'),
                  ('17. “GODS IN PYJAMAS WITH ETHICAL DILEMMAS”', '16. “GODS IN PYJAMAS WITH ETHICAL DILEMMAS”'),
                  ('18. “THE MARTIAL ARTS TOURNAMENT (NOW WITH SCREAMING)”', '17. “THE MARTIAL ARTS TOURNAMENT (NOW WITH SCREAMING)”'),
                  ('19. “GIANT ROBOTS AND TEENAGE ANGST”', '18. “GIANT ROBOTS AND TEENAGE ANGST”'),
                  ('20. “THE HILARIOUS DYSTOPIA”', '19. “THE HILARIOUS DYSTOPIA”')])
s = mover_quelonios(s, '<h4>Critique-and-improve recipe: “The world held up by chelonians”</h4>',
                    '“THE WORLD ON THE BACK OF CHELONIANS”', '20. “THE WORLD ON THE BACK OF CHELONIANS”',
                    '<aside class="meta"><p>The author has made this recipe bulletproof', CRIT_EN)
s = renumerar(s, [('<td>3, 16</td>', '<td>3, 15</td>'), ('<td>Flashbacks</td><td>16</td>', '<td>Flashbacks</td><td>15</td>'),
                  ('<td>Transformation</td><td>18</td>', '<td>Transformation</td><td>17</td>'),
                  ('<td>Synchronisation</td><td>19</td>', '<td>Synchronisation</td><td>18</td>'),
                  ('<td>Clones</td><td>20</td>', '<td>Clones</td><td>19</td>'),
                  ('<em>Recipes:</em> 16 (', '<em>Recipes:</em> 15 ('),
                  ('<em>Recipes:</em> 18 (', '<em>Recipes:</em> 17 ('),
                  ('<em>Recipes:</em> 20 (', '<em>Recipes:</em> 19 (')])
io.open(f, 'w', encoding='utf-8').write(s)
print('EN: recetas reordenadas')
