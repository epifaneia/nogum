# -*- coding: utf-8 -*-
"""En el Acelerado el equipo solo cuesta dinero, y el dinero es tu nivel en Recursos."""
import io, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

ES = r"""<h4>2.9 El equipo: lo que puedes permitirte</h4>
<p>Aquí el equipo <strong>solo cuesta dinero</strong>, y el dinero es tu bono en <em>Recursos</em> (Social → Jerarquía → Recursos). Nada de puntos, nada de Llaves: si tu cajón llega, lo tienes.</p>
<div class="tw"><table class="t">
<thead><tr><th>Recursos</th><th>Quién eres</th><th>Lo que llevas encima</th></tr></thead>
<tbody>
<tr><td class="num">−2</td><td>No tienes nada y nadie te fía</td><td>Ropa, un cuchillo, lo que encuentres o te presten</td></tr>
<tr><td class="num">+0</td><td>Un sueldo, o un grupo que te cubre</td><td>Un arma pequeña, herramientas, un trasto con ruedas</td></tr>
<tr><td class="num">+1</td><td>Ahorros y contactos</td><td>Un arma seria, protección ligera, un vehículo decente</td></tr>
<tr><td class="num">+2</td><td>Dinero de verdad, o un patrón que paga</td><td>Material militar, armadura, un vehículo blindado</td></tr>
<tr><td class="num">+3</td><td>Mueves presupuestos que no son tuyos</td><td>Lo anterior, y un equipo de gente para usarlo</td></tr>
<tr><td class="num">+4</td><td>El dinero ha dejado de ser el problema</td><td>Lo que no debería existir</td></tr>
</tbody></table></div>
<ul>
<li><strong>Un escalón por encima, una vez por arco.</strong> Puedes conseguir algo que no te toca, pero nunca sale gratis: un favor que te van a cobrar, una deuda, un rastro, alguien que ahora sabe tu nombre.</li>
<li><strong>Lo robado o prestado funciona una escena entera.</strong> Después decides si te lo quedas, y entonces sí tiene que caber en tu cajón.</li>
<li><strong>El arma no te hace mejor, hace otra cosa.</strong> Lo que cambia son sus etiquetas: cuánto daño hace, si se puede esquivar y si la armadura sirve (2.6).</li>
</ul>
<aside class="meta"><p>En el manual completo el equipo tiene una economía entera detrás: lo que te hace <em>mejor</em> se paga con puntos de habilidad y lo que te deja hacer lo <em>imposible</em> se paga con Llaves, y hay un taller para ponerle precio a cualquier cosa que os inventéis. Aquí basta con el dinero. NOGUM te espera.</p></aside>
"""

EN = r"""<h4>2.9 Equipment: what you can afford</h4>
<p>Here equipment <strong>costs money and nothing else</strong>, and money is your bonus in <em>Resources</em> (Social → Hierarchy → Resources). No points, no Keys: if your drawer reaches, you have it.</p>
<div class="tw"><table class="t">
<thead><tr><th>Resources</th><th>Who you are</th><th>What you carry</th></tr></thead>
<tbody>
<tr><td class="num">−2</td><td>You have nothing and nobody gives you credit</td><td>Clothes, a knife, whatever you find or are lent</td></tr>
<tr><td class="num">+0</td><td>A wage, or a crew that covers you</td><td>A small weapon, tools, something with wheels</td></tr>
<tr><td class="num">+1</td><td>Savings and contacts</td><td>A serious weapon, light protection, a decent vehicle</td></tr>
<tr><td class="num">+2</td><td>Real money, or a patron who pays</td><td>Military hardware, armour, an armoured vehicle</td></tr>
<tr><td class="num">+3</td><td>You move budgets that are not yours</td><td>All of the above, and a team of people to use it</td></tr>
<tr><td class="num">+4</td><td>Money has stopped being the problem</td><td>What should not exist</td></tr>
</tbody></table></div>
<ul>
<li><strong>One step above, once per arc.</strong> You can get hold of something out of your league, but it is never free: a favour that will be called in, a debt, a trail, somebody who now knows your name.</li>
<li><strong>Stolen or borrowed gear works for a whole scene.</strong> Afterwards you decide whether to keep it, and then it does have to fit in your drawer.</li>
<li><strong>The weapon does not make you better, it does something else.</strong> What changes are its tags: how much damage it does, whether it can be dodged and whether armour helps (2.6).</li>
</ul>
<aside class="meta"><p>In the complete rulebook equipment has a whole economy behind it: what makes you <em>better</em> is paid for with skill points and what lets you do the <em>impossible</em> is paid for with Keys, and there is a workshop for pricing anything you invent. Here money is enough. NOGUM is waiting.</p></aside>
"""

for f, txt in (('frag_acelerado.html', ES), ('frag_acelerado.en.html', EN)):
    s = io.open(f, encoding='utf-8').read()
    k = s.index('<h3 id="ac-interfaz">')
    s = s[:k] + txt + '\n' + s[k:]
    # la hoja tambien lo dice
    s = s.replace('<tr><td>Equipo</td><td>Nombre + ', '<tr><td>Equipo <small>(lo que te permita Recursos)</small></td><td>Nombre + ')
    s = s.replace('<tr><td>Equipment</td><td>Name + ', '<tr><td>Equipment <small>(whatever Resources allows)</small></td><td>Name + ')
    io.open(f, 'w', encoding='utf-8').write(s)
    print(' ', f, 'ok')
