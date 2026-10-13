# -*- coding: utf-8 -*-
"""El acordeon: la maestria se pliega hacia arriba. Es la escalera larga de los puntos."""
import io, os, shutil
os.chdir(os.path.dirname(os.path.abspath(__file__)))

ES = r"""
<div class="rule">
<p class="rule-title">El acordeón: la maestría se pliega hacia arriba</p>
<p>Si eres Gran Maestro con la pistola, con el rifle, con la espada y con el arco, ya no eres un especialista en cuatro cosas: <strong>eres Gran Maestro de las Armas</strong>. Y si lo eres de las cuatro Disciplinas de Vigor, eres Gran Maestro del Vigor entero. La maestría no se amontona: se pliega. <span class="flag ed">ED-38</span></p>
<div class="tw"><table class="t">
<thead><tr><th>Cuando tienes…</th><th>Se pliega en</th><th>Y entonces tiras</th></tr></thead>
<tbody>
<tr><td><strong>3 Firmas</strong> de Gran Maestro en la misma Disciplina</td><td>La <strong>Disciplina</strong> entera</td><td>+4 en cualquier cosa de esa Disciplina, tenga Firma o no</td></tr>
<tr><td><strong>3 Disciplinas</strong> plegadas del mismo Dominio</td><td>El <strong>Dominio</strong> entero</td><td>+4 en todo el Dominio</td></tr>
<tr><td>Los <strong>2 Dominios</strong> plegados</td><td>El <strong>Ámbito</strong> entero</td><td>+4 en todo lo que caiga en ese Ámbito</td></tr>
</tbody></table></div>
<p>Es la otra forma de crecer, y la única que le queda a los puntos cuando ya tienes tu +4: el Ancla sigue sin moverse —nadie pasa de +4 en la vida—, pero <strong>el +4 se va ensanchando</strong> hasta cubrirlo todo. Un personaje que ha plegado el Físico no es más fuerte que el que tiene una sola Firma: es que ya no hay nada físico que no sepa hacer.</p>
<p>Y es cara de verdad, que es lo que la hace un objetivo de campaña y no un truco de creación:</p>
<div class="tw"><table class="t">
<thead><tr><th>Plegar…</th><th class="num">Puntos</th><th>Cuánto es eso</th></tr></thead>
<tbody>
<tr><td>Una Disciplina</td><td class="num">8</td><td>Dos tercios de una ficha nueva</td></tr>
<tr><td>Un Dominio</td><td class="num">22</td><td>Una campaña corta entera</td></tr>
<tr><td>Un Ámbito</td><td class="num">44</td><td>Cuarenta sesiones a punto por sesión</td></tr>
</tbody></table></div>
<p>Con doce puntos en la creación, lo máximo que cabe es una Disciplina plegada y poco más, así que nadie llega a la mesa siendo el mejor del mundo en un terreno completo. Plegar un Ámbito es, literalmente, el final de una campaña larga: ahí es donde van los puntos cuando ya no queda nada que aprender.</p>
<p class="small">Si en tu mesa tres se os hace mucho o poco, es el único número que tiene este acordeón: subidlo a cuatro para que la maestría total sea casi inalcanzable, o bajadlo a dos para campañas de héroes competentes desde el principio.</p>
</div>
"""

EN = r"""
<div class="rule">
<p class="rule-title">The accordion: mastery folds upwards</p>
<p>If you are a Grand Master with the pistol, the rifle, the sword and the bow, you are no longer a specialist in four things: <strong>you are a Grand Master of Weapons</strong>. And if you are one in all four Disciplines of Vigour, you are a Grand Master of the whole of Vigour. Mastery does not pile up: it folds. <span class="flag ed">ED-38</span></p>
<div class="tw"><table class="t">
<thead><tr><th>When you have…</th><th>It folds into</th><th>And then you roll</th></tr></thead>
<tbody>
<tr><td><strong>3 Grand Master Signatures</strong> in the same Discipline</td><td>The whole <strong>Discipline</strong></td><td>+4 at anything in that Discipline, Signature or not</td></tr>
<tr><td><strong>3 folded Disciplines</strong> from the same Domain</td><td>The whole <strong>Domain</strong></td><td>+4 across the Domain</td></tr>
<tr><td>Both <strong>folded Domains</strong></td><td>The whole <strong>Sphere</strong></td><td>+4 at anything falling in that Sphere</td></tr>
</tbody></table></div>
<p>It is the other way to grow, and the only one left to points once you have your +4: the Anchor still does not move —nobody ever goes past +4— but <strong>the +4 keeps widening</strong> until it covers everything. A character who has folded the Physical sphere is no stronger than one with a single Signature: it is just that there is no longer anything physical they cannot do.</p>
<p>And it is genuinely expensive, which is what makes it a campaign goal rather than a creation trick:</p>
<div class="tw"><table class="t">
<thead><tr><th>Folding…</th><th class="num">Points</th><th>How much that is</th></tr></thead>
<tbody>
<tr><td>One Discipline</td><td class="num">8</td><td>Two thirds of a fresh sheet</td></tr>
<tr><td>One Domain</td><td class="num">22</td><td>A whole short campaign</td></tr>
<tr><td>One Sphere</td><td class="num">44</td><td>Forty sessions at one point per session</td></tr>
</tbody></table></div>
<p>With twelve points at creation, the most that fits is one folded Discipline and little else, so nobody arrives at the table as the best in the world at a complete field. Folding a Sphere is, literally, the end of a long campaign: that is where points go when there is nothing left to learn.</p>
<p class="small">If three feels like too many or too few at your table, it is the only number this accordion has: raise it to four to make total mastery nearly unreachable, or drop it to two for campaigns of competent heroes from the start.</p>
</div>
"""

PROG_ES = r"""<div class="rule">
<p class="rule-title">Adónde van los puntos cuando ya no queda nada que aprender</p>
<p>El Ancla corta en +4 y eso no se negocia, así que a partir de cierto momento los puntos solo compran anchura. Lo que les da una meta es <strong>el acordeón</strong> (<a href="#ch3-firmas">3.3</a>): tres Firmas de Gran Maestro pliegan la Disciplina entera, tres Disciplinas pliegan el Dominio, los dos Dominios pliegan el Ámbito. Ocho puntos, veintidós y cuarenta y cuatro.</p>
<p>Así los dos monederos tienen cada uno su escalera larga y no se parecen en nada: <strong>las Llaves suben hacia fuera</strong> —cada peldaño multiplica por cien tu alcance contra algo concreto— y <strong>los puntos suben hacia dentro</strong>, ensanchando el +4 hasta que no queda nada de ese terreno que no sepas hacer. Uno te hace tocar más mundo; el otro, no fallar nunca en el tuyo.</p>
</div>
"""

PROG_EN = r"""<div class="rule">
<p class="rule-title">Where points go when there is nothing left to learn</p>
<p>The Anchor cuts off at +4 and that is not negotiable, so past a certain point skill points only buy breadth. What gives them a goal is <strong>the accordion</strong> (<a href="#ch3-firmas">3.3</a>): three Grand Master Signatures fold the whole Discipline, three Disciplines fold the Domain, both Domains fold the Sphere. Eight points, twenty-two and forty-four.</p>
<p>That way each wallet has its own long ladder and they look nothing alike: <strong>Keys climb outwards</strong> —every rung multiplies your reach against one specific thing by a hundred— and <strong>points climb inwards</strong>, widening the +4 until there is nothing in that field you cannot do. One makes you touch more world; the other makes you never fail in your own.</p>
</div>
"""

MAQ_ES = r"""<h4>El acordeón: la escalera larga de los puntos</h4>
<p>Las Llaves tienen su escalera cuadrada; los puntos tienen el acordeón, y conviene ver los dos números juntos porque crecen de formas distintas.</p>
<div class="tw"><table class="t">
<thead><tr><th>Peldaño</th><th class="num">Puntos</th><th class="num">Casillas que cubre a +4</th><th class="num">Precio por casilla</th></tr></thead>
<tbody>
<tr><td>Una Firma de Gran Maestro</td><td class="num">4</td><td class="num">1</td><td class="num">4</td></tr>
<tr><td>Una Disciplina plegada</td><td class="num">8</td><td class="num">1 Disciplina entera</td><td class="num">—</td></tr>
<tr><td>Un Dominio plegado</td><td class="num">22</td><td class="num">4 Disciplinas</td><td class="num">5,5</td></tr>
<tr><td>Un Ámbito plegado</td><td class="num">44</td><td class="num">8 Disciplinas y 2 Dominios</td><td class="num">4,4</td></tr>
</tbody></table></div>
<p>La cuenta de los ocho: Dominio 1, Disciplina 1 y tres Firmas de Gran Maestro a 2 cada una. La del Dominio: la primera Disciplina plegada cuesta 8 y las dos siguientes 7 cada una, porque el Dominio ya está pagado. La del Ámbito: dos Dominios a 22.</p>
<p>Y fíjate en la última columna, que es la que cuenta la historia: <strong>el precio por casilla casi no baja</strong>. Plegar no es un descuento por volumen, es simplemente la única forma de seguir gastando cuando el Ancla ya no te deja subir. Por eso el acordeón no rompe nada: no añade números a la tirada, solo quita huecos del mapa. Al final del camino, un personaje con el Físico plegado y otro recién hecho con una sola Firma <em>tiran exactamente lo mismo</em> cuando los dos hacen lo suyo. La diferencia es que al primero ya no hay forma de pillarle fuera de su terreno.</p>
"""

MAQ_EN = r"""<h4>The accordion: the long ladder of points</h4>
<p>Keys have their square ladder; points have the accordion, and it is worth seeing both sets of numbers together because they grow in different ways.</p>
<div class="tw"><table class="t">
<thead><tr><th>Rung</th><th class="num">Points</th><th class="num">Slots covered at +4</th><th class="num">Price per slot</th></tr></thead>
<tbody>
<tr><td>One Grand Master Signature</td><td class="num">4</td><td class="num">1</td><td class="num">4</td></tr>
<tr><td>One folded Discipline</td><td class="num">8</td><td class="num">1 whole Discipline</td><td class="num">—</td></tr>
<tr><td>One folded Domain</td><td class="num">22</td><td class="num">4 Disciplines</td><td class="num">5.5</td></tr>
<tr><td>One folded Sphere</td><td class="num">44</td><td class="num">8 Disciplines and 2 Domains</td><td class="num">4.4</td></tr>
</tbody></table></div>
<p>The sum behind the eight: Domain 1, Discipline 1 and three Grand Master Signatures at 2 each. Behind the Domain: the first folded Discipline costs 8 and the next two cost 7 each, because the Domain is already paid for. Behind the Sphere: two Domains at 22.</p>
<p>And look at the last column, which is where the story is: <strong>the price per slot barely drops</strong>. Folding is not a bulk discount, it is simply the only way left to spend once the Anchor will not let you climb. That is why the accordion breaks nothing: it adds no numbers to the roll, it only removes gaps from the map. At the end of the road, a character with a folded Physical sphere and a freshly made one with a single Signature <em>roll exactly the same</em> when each does their own thing. The difference is that nobody can catch the first one outside their field any more.</p>
"""

GLO_ES = ('<dt>Acordeón</dt><dd>La regla que pliega la maestría hacia arriba: tres Firmas de Gran Maestro '
          'convierten la Disciplina entera en +4, tres Disciplinas el Dominio, y los dos Dominios el Ámbito. '
          '<span class="note">No sube el techo: lo ensancha. Es la escalera larga de los puntos, como la '
          'escalera cuadrada lo es de las Llaves.</span></dd>\n')
GLO_EN = ('<dt>Accordion</dt><dd>The rule that folds mastery upwards: three Grand Master Signatures turn the '
          'whole Discipline into +4, three Disciplines the Domain, and both Domains the Sphere. '
          '<span class="note">It does not raise the ceiling: it widens it. It is the long ladder of points, '
          'as the square ladder is of Keys.</span></dd>\n')


def do(es):
    sfx = '' if es else '.en'
    f = 'frag_ch3%s.html' % sfx
    shutil.copyfile(f, f + '.bak_acord')
    s = io.open(f, encoding='utf-8').read()
    k = s.index('<h3 id="ch3-extras">')
    s = s[:k] + (ES if es else EN) + '\n' + s[k:]
    # la nota de progresion
    anchor = '<h4>Dones y lacras' if es else '<h4>Gifts and flaws'
    k = s.index(anchor)
    s = s[:k] + (PROG_ES if es else PROG_EN) + '\n' + s[k:]
    # el catalogo ya esta agrupado: se cierra la pregunta
    old_es = 'Catálogo de Firmas en el <a href="#ch8-skills">apartado 8.2</a>. Cómo agruparlo sigue sin decidir. <span class="flag pending">Pendiente</span>'
    new_es = 'Catálogo de doscientas Firmas en el <a href="#ch8-skills">apartado 8.2</a>, ordenado por Disciplina: cinco por cada una, que es como se buscan en mesa.'
    old_en = 'Signature catalogue in <a href="#ch8-skills">section 8.2</a>. How to group it is still undecided. <span class="flag pending">Pending</span>'
    new_en = 'A catalogue of two hundred Signatures in <a href="#ch8-skills">section 8.2</a>, ordered by Discipline: five for each, which is how they get looked up at the table.'
    if es:
        s = s.replace(old_es, new_es) if old_es in s else s
    else:
        s = s.replace(old_en, new_en) if old_en in s else s
    io.open(f, 'w', encoding='utf-8').write(s)

    f = 'frag_math%s.html' % sfx
    s = io.open(f, encoding='utf-8').read()
    anchor = '<h4>El monedero de Llaves es el único grifo sin fondo</h4>' if es else '<h4>The Key wallet is the only bottomless tap</h4>'
    k = s.index(anchor)
    s = s[:k] + (MAQ_ES if es else MAQ_EN) + '\n' + s[k:]
    io.open(f, 'w', encoding='utf-8').write(f and s)

    f = 'frag_glosario%s.html' % sfx
    s = io.open(f, encoding='utf-8').read()
    k = s.rindex('</dl>')
    s = s[:k] + (GLO_ES if es else GLO_EN) + s[k:]
    io.open(f, 'w', encoding='utf-8').write(s)
    print(' ', 'ES' if es else 'EN', 'ok')


do(True)
do(False)
