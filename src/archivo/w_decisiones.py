# -*- coding: utf-8 -*-
"""Seis decisiones del autor, aplicadas. Y la Sangre, que es ansia y va en Mente."""
import io, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

SUBS = {
 # ---------------------------------------------------------------- 1. fuera el dial x10
 'frag_ch2.html': [
  ('<p class="small">Regla opcional: si tu campaña es de callejón y el ×100 te suena a cómic, usa <strong>×10 por nivel</strong>. La escala narrativa no cambia —sigues yendo de la persona al país—, solo cambia el tamaño del asombro. <span class="flag proposal">Propuesta sin validar</span></p>',
   '<p class="small"><strong>No hay una versión en ×10.</strong> Un salto de diez veces es justo lo que ya separa un −2 de un +4: eso lo compra la pirámide, no la Rejilla. El ×100 suena a cómic porque <em>es</em> cómic, y si en tu campaña se sale de madre, la respuesta no es encoger la escala: es <strong>dejar a todo el mundo en Rejilla 1 y jugar con los puntos de habilidad</strong>. Para lo de en medio ya está la Llave pequeña: un ordenador con conexión te deja apagar un edificio entero sin ser nivel 3.</p>'),
  ('<p>Rick Sánchez (<em>Rick y Morty</em>) crea universos con su intelecto: es nivel 5 «si no 6». <span class="flag pending">Pendiente</span></p>',
   '<p>El científico que viaja entre mundos y crea universos con el intelecto es nivel 5, «si no 6». <span class="src">Tabla aprobada por el autor</span></p>'),
  ('<li><strong>Presupuestos de Rejilla por tipo de campaña.</strong> Callejera [1,1,1,1,1]; Héroes de acción [2,1,1,1,1]; Leyendas [3,2,2,1,1]. <span class="flag proposal">Propuesta sin validar</span> <span class="src">T91</span></li>',
   '<li><strong>El reparto inicial es [2,1,1,1,1]</strong>, y el 2 no se elige libremente: es <strong>el único que el universo permite</strong>, el que dice el techo de la receta (<a href="#ch8-recetas">8.4</a>). En cyberpunk ese 2 es el Físico del cromado; en una campaña de cortes, el Social. <strong>Si no quieres ese 2, te llevas 5 Llaves</strong> (<a href="#ch3-economia">3.5</a>): o eres grande donde tu mundo deja ser grande, o eres pequeño y muy concreto en lo que tú elijas. <span class="src">Decisión del autor</span></li>'),
 ],
 # ---------------------------------------------------------------- 2. el Estilo no cura
 'frag_ch4.html': [
  ('Recuperar salud o estrés con un crítico de Estilo es una idea que el autor no llegó a validar. <span class="flag proposal">Propuesta sin validar</span>',
   '<strong>Un crítico de Estilo no cura.</strong> Recuperar salud con una floritura no tiene sentido; el estrés se puede negociar en la mesa, pero nunca de forma automática, y el efecto concreto lo decide el Director con el jugador. <span class="src">Decisión del autor</span>'),
 ],
 # ---------------------------------------------------------------- 3 y 4. iniciativa y absorcion
 'frag_ch5.html': [
  ('<p>Iniciativa fija para PNJ (12 para masillas, 16 para jefes). <span class="flag proposal">Propuesta sin validar</span></p>',
   '<p><strong>Nada de iniciativa fija.</strong> También los PNJ declaran guardia y tiran: es una tirada enfrentada con la habilidad de la disposición elegida, y las masillas llevan sus dos o tres números básicos para resolverla sin ficha. <span class="src">Decisión del autor</span></p>'),
  ('Qué hace falta exactamente para poder absorber (¿basta la dureza o se necesita armadura?) no está decidido. <span class="flag pending">Pendiente</span>',
   '<strong>Siempre se absorbe con la habilidad</strong>, se lleve armadura o no: el cuerpo es la primera protección. Lo que decide si sirve de algo son las etiquetas del arma —<span class="tag">Abs: Máx N</span> y <span class="tag">Abs: Nula</span>, que es donde vive «esto te atraviesa la piel»— y los bonos que sume la protección que lleves. Por defecto, normal. <span class="src">Decisión del autor</span>'),
 ],
}

for f, subs in SUBS.items():
    s = io.open(f, encoding='utf-8').read()
    for a, b in subs:
        n = s.count(a)
        print('%-18s %d  %s' % (f, n, a[:52]))
        s = s.replace(a, b)
    io.open(f, 'w', encoding='utf-8').write(s)

# ---------------------------------------------------------------- 5. la Sangre es ansia
SANGRE = [
 ('frag_cap8.html',
  [('<tr><td><strong>Sangre</strong> · Hambre</td><td>Gótico</td><td class="num">Cuerpo</td><td>Es combustible: se gasta y se repone. No confundir con la Bestia</td></tr>',
    '<tr><td><strong>Sed</strong> · Sangre</td><td>Gótico</td><td class="num">Mente</td><td>Es <strong>ansia</strong>: el estrés de una adicción, no un depósito. No confundir con la Bestia, que es Espíritu</td></tr>'),
   ('Son dos barras distintas y conviene no mezclarlas: la <strong>Sangre</strong> es combustible y va en la barra Física (se tachan casillas para activar Dones y, si se vacía, llega el frenesí), mientras que la <strong>Humanidad</strong> es la Bestia y va en la Espiritual, porque ahí dentro hay alguien que no eres tú',
    'Son dos barras distintas y conviene no mezclarlas. La <strong>Sed</strong> va en la barra <strong>Mental</strong>, porque es <em>ansia</em>: funciona como un síndrome de abstinencia, no como un depósito de combustible. Cuanto más llena, peor te concentras, peor mides el riesgo y más barato te sale ceder; al llenarse del todo llega el frenesí. La <strong>Humanidad</strong> es la Bestia y va en la <strong>Espiritual</strong>, porque ahí dentro hay alguien que no eres tú. Los manuales viejos trataban la sangre como una piscina de puntos; aquí se juega como lo que de verdad da juego en mesa: el mono')]),
 ('frag_cap8.en.html',
  [('<tr><td><strong>Blood</strong> · Hunger</td><td>Gothic</td><td class="num">Body</td><td>It is fuel: it is spent and refilled. Not to be confused with the Beast</td></tr>',
    '<tr><td><strong>Thirst</strong> · Blood</td><td>Gothic</td><td class="num">Mind</td><td>It is <strong>craving</strong>: the stress of an addiction, not a tank. Not to be confused with the Beast, which is Spirit</td></tr>'),
   ('They are two different bars and are best not mixed: <strong>Blood</strong> is fuel and sits on the Physical bar (boxes are marked to activate Gifts and, if it empties, frenzy sets in), while <strong>Humanity</strong> is the Beast and sits on the Spiritual one, because in there is somebody who is not you',
    'They are two different bars and are best not mixed. <strong>Thirst</strong> sits on the <strong>Mental</strong> bar, because it is <em>craving</em>: it works like withdrawal, not like a fuel tank. The fuller it gets, the worse you concentrate, the worse you judge risk and the cheaper giving in looks; when it fills completely, frenzy sets in. <strong>Humanity</strong> is the Beast and sits on the <strong>Spiritual</strong> bar, because in there is somebody who is not you. The old rulebooks treated blood as a pool of points; here it is played as the thing that actually gives you a scene: the craving')]),
]
for f, subs in SANGRE:
    s = io.open(f, encoding='utf-8').read()
    for a, b in subs:
        n = s.count(a)
        print('%-20s %d  %s' % (f, n, a[:46]))
        s = s.replace(a, b)
    io.open(f, 'w', encoding='utf-8').write(s)

# la tabla de «lo que se pierde» de Mente gana una columna de Sed
ADD_ES = ('<th>Identidad <small>(mentes digitales)</small></th>',
          '<th>Identidad <small>(mentes digitales)</small></th><th>Sed <small>(gótico)</small></th>')
FILAS_ES = ['Te fijas en el pulso de quien te habla', 'Calculas cuánto aguantas sin beber',
            'Te molesta el olor de la comida', 'Pierdes el hilo a media frase',
            'Alguien normal te parece lento y torpe', 'Ya no te acuerdas de tener hambre de lo otro']
ADD_EN = ('<th>Identity <small>(digital minds)</small></th>',
          '<th>Identity <small>(digital minds)</small></th><th>Thirst <small>(gothic)</small></th>')
FILAS_EN = ['You watch the pulse of whoever is talking', 'You work out how long you can last without feeding',
            'The smell of food bothers you', 'You lose the thread halfway through a sentence',
            'An ordinary person looks slow and clumsy to you', 'You no longer remember being hungry for anything else']

import re
for f, (a, b), filas in (('frag_cap8.html', ADD_ES, FILAS_ES), ('frag_cap8.en.html', ADD_EN, FILAS_EN)):
    s = io.open(f, encoding='utf-8').read()
    i = s.index(a)
    s = s[:i] + b + s[i + len(a):]
    j = s.index('</thead>', i)
    k = s.index('</tbody>', j)
    body = s[j:k]
    rows = body.split('</tr>')
    out, n = [], 0
    for r in rows:
        if '<td' in r and n < 6:
            r = r + '<td>' + filas[n] + '</td>'
            n += 1
        out.append(r)
    s = s[:j] + '</tr>'.join(out) + s[k:]
    io.open(f, 'w', encoding='utf-8').write(s)
    print(f, 'columna de Sed anadida:', n)
