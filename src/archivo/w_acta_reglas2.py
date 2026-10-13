# -*- coding: utf-8 -*-
"""Segunda tanda del acta: flashbacks, transformacion, ambiental, vinculos,
la Humanidad del ciberpunk y la Generacion de los vampiros."""
import io, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

ES = [
 # --------------------------------------------- flashbacks: se tiran
 ('<p>Un jugador puede interrumpir el presente para narrar una escena del pasado que resuelve el problema actual («No tengo la llave… pero ayer soborné al guardia»). Para hacerlo paga un coste: <strong>tacha 1 casilla de su barra Mental</strong> (el estrés de haberlo tenido todo previsto) o <strong>gasta un recurso de equipo</strong>. Si el flashback exige una acción arriesgada, se tira como cualquier otra. <span class="flag proposal">Propuesta sin validar</span> <span class="src">T117</span></p>',
  '<p>Un jugador puede interrumpir el presente para narrar una escena del pasado que resuelve el problema actual («No tengo la llave… pero ayer soborné al guardia»). <strong>El flashback no se paga: se tira.</strong></p>'
  '<ul>'
  '<li>Tira la habilidad que corresponda al plan contra el TN de la tarjeta activa.</li>'
  '<li><strong>Éxito:</strong> el flashback ocurrió, y tienes lo que fuiste a buscar.</li>'
  '<li><strong>Cada punto por encima del TN</strong> te da un detalle más que puedes meter dentro: un objeto que dejaste preparado, una salida, alguien colocado en el sitio justo.</li>'
  '<li><strong>Fallo:</strong> el plan existía, pero salió torcido y lo descubres ahora.</li>'
  '<li><strong>Pifia:</strong> el pasado te delata; el menú de la pifia (5.2) decide cómo.</li>'
  '</ul>'
  '<p>Así el flashback deja de ser una moneda y pasa a ser una escena con riesgo, que es para lo que la mesa lo quiere. <span class="src">Decisión del autor</span></p>'),
 # --------------------------------------------- transformacion
 ('Como todo modificador temporal (4.4), la transformación lleva una <strong>condición de fin</strong> anotada: al acabar la escena, al llenar un bloque de vida o al gastar una casilla de la barra Espiritual por turno. <span class="flag proposal">Propuesta sin validar</span> <span class="src">T116</span>',
  'Como todo modificador temporal (4.4), la transformación tiene siempre la misma <strong>condición de fin</strong>: <strong>se acaba al acabar la escena</strong>. Sin variantes, sin contadores y sin gastar casillas por turno: lo que el género pide es que dure lo que dura la pelea. <span class="src">Decisión del autor</span>'),
 # --------------------------------------------- ambiental
 ('Un entorno hostil (radiación, frío extremo, vacío, gas) inflige daño <strong>por cada escena de exposición</strong>, sin tirada de ataque: por ejemplo, radiación <span class="tag">Daño 1</span> <span class="tag">Esq: Nula</span> <span class="tag">Abs: Nula</span>. La protección adecuada (traje, refugio, antídoto) funciona como permiso narrativo: con ella, el daño se puede absorber o desaparece. <span class="flag proposal">Propuesta sin validar</span> <span class="src">T127</span>',
  'Un entorno hostil (radiación, frío extremo, vacío, gas) inflige daño <strong>por cada escena de exposición</strong> y sin tirada de ataque, y <strong>el daño sube según te quedas</strong>: <span class="tag">Daño 1</span> la primera escena, <span class="tag">Daño 2</span> la segunda, <span class="tag">Daño 3</span> la tercera, siempre <span class="tag">Esq: Nula</span> <span class="tag">Abs: Nula</span>. El contador vuelve a cero en cuanto sales. La protección adecuada (traje, refugio, antídoto) funciona como permiso narrativo: con ella, el daño se puede absorber o desaparece. <span class="src">Decisión del autor</span>'),
 # --------------------------------------------- vinculos
 ('<li><strong>Como escudo.</strong> Puede desviar daño Mental hacia un vínculo, que se resiente en la ficción (una discusión, un abandono, una herida). Se sacrifica la vida personal para salvar la mente.</li>\n</ul>\n<p><span class="flag proposal">Propuesta sin validar</span> <span class="src">T119</span> <span class="src">Borrador</span></p>',
  '<li><strong>Como escudo.</strong> Puede desviar daño hacia un vínculo, que se resiente en la ficción: una discusión, un abandono, una herida. Se sacrifica la vida personal para salvar lo otro.</li>\n</ul>\n'
  '<p><strong>Qué barra puede escudar lo decide el universo.</strong> Por defecto, la Mental. En el gótico, además la Espiritual: aferrarse a alguien que te quiere es justo lo que frena a la Bestia, y por eso allí los vínculos son media ficha. <span class="src">Decisión del autor</span></p>'),
 # --------------------------------------------- receta 8: Humanidad
 ('La barra <strong>Mental</strong> puede llamarse Empatía y resentirse con cada implante: la ciberpsicosis es una locura, no una posesión, y en este mundo no hay Arcano, así que no hay barra Espiritual <span class="flag proposal">Propuesta sin validar</span>.',
  'La barra <strong>Mental</strong> se llama aquí <strong>Humanidad</strong> y se resiente con cada implante: la ciberpsicosis es una locura, no una posesión, y en este mundo no hay Arcano, así que no hay barra Espiritual. Es el mismo nombre que usa el gótico a propósito (ED-39): <em>la misma palabra, la misma pérdida, y sin embargo otra barra</em>, porque allí hay una Bestia dentro y aquí no hay nadie.'),
 # --------------------------------------------- receta 13: la Generacion
 ('En el canon: la Generación es el nivel de Rejilla (por ejemplo, neonato 1, príncipe 3, matusalén 5 <span class="flag proposal">Propuesta sin validar</span>).',
  'En el canon: nada de escalera de Generaciones. <strong>Todos los vampiros son Rejilla 2 en lo sobrenatural</strong>, y de base también en Físico, que no es exagerado: un humano sin Llave <strong>pierde automáticamente</strong>, y eso es exactamente lo que el género quiere decir. Los saltos siguen siendo de uno en uno, y uno es ×100. Si quieres distinguir a un neonato de un matusalén, no subas la Rejilla: <strong>dale Llaves</strong> —Entereza, Sigilo, Intimidación—, que es más fino y no rompe la escala.'),
 ('aquí se juega como lo que de verdad da juego en mesa: el mono <span class="flag proposal">Propuesta sin validar</span>.',
  'aquí se juega como lo que de verdad da juego en mesa: el mono.'),
 # --------------------------------------------- flags de «dalo por bueno»
 ('<span class="flag proposal">Propuesta sin validar</span> <span class="src">T126</span> Magia rúnica',
  '<span class="src">Aprobado por el autor</span> <span class="src">T126</span> Magia rúnica'),
]

s = io.open('frag_cap8.html', encoding='utf-8').read()
for a, b in ES:
    n = s.count(a)
    print('%d  %s' % (n, a[:60].replace('\n', ' ')))
    s = s.replace(a, b)
io.open('frag_cap8.html', 'w', encoding='utf-8').write(s)

# la homonimia de Vinculos ya no es hipotetica: el Arcano esta cerrado
s = io.open('frag_cap8.html', encoding='utf-8').read()
a = 'Ojo con la homonimia: «Vínculos» es también una de las cuatro Disciplinas propuestas para Ritual (8.2). Si se confirman las dos, a una habrá que cambiarle el nombre.'
b = 'Ojo con la homonimia: «Vínculos» es también una de las cuatro Disciplinas de Ritual (8.2), ya confirmadas. Se distinguen por el contexto —la Disciplina se tira, el vínculo se escribe en la ficha— pero si en tu mesa chocan, llama «Lazos» a los del corazón.'
print(s.count(a), 'homonimia')
io.open('frag_cap8.html', 'w', encoding='utf-8').write(s.replace(a, b))
