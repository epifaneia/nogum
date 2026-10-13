# -*- coding: utf-8 -*-
"""Las 27 respuestas del acta, aplicadas a las reglas."""
import io, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

SUB = {
 # ------------------------------------------------ puntos de suerte: no existen
 'frag_ch67.html': [
  ('El borrador menciona además unos «puntos de suerte» que no están definidos en ningún otro lugar. <span class="flag pending">Pendiente</span>',
   'El borrador mencionaba unos «puntos de suerte» para el villano: <strong>no existen</strong>. El antagonista gasta Llaves como todo el mundo, y si quieres que sobreviva a la escena, dale Llaves y que se note en la ficción. <span class="src">Decisión del autor</span>'),
 ],
 'frag_ch67.en.html': [
  ('The draft also mentions some “luck points” that are not defined anywhere else. <span class="flag pending">Pending</span>',
   'The draft mentioned “luck points” for the villain: <strong>they do not exist</strong>. The antagonist spends Keys like everybody else, and if you want them to survive the scene, give them Keys and let it show in the fiction. <span class="src">Author’s decision</span>'),
 ],
 # ------------------------------------------------ el detective: una Llave
 'frag_cap8.html': [
  ('<p>Queda por decidir si el «poder metanarrativo» de Sherlock (que el Director le dé pistas) es una Firma, un aspecto o una Llave. <span class="flag pending">Pendiente</span> <span class="src">T133</span></p>',
   '<p>El «poder metanarrativo» del detective —que el Director le dé pistas— <strong>es una Llave</strong>: una pista por escena, comprada y pagada como cualquier otra. Así deja de ser un favor del Director y pasa a ser algo que el jugador eligió tener. <span class="src">Decisión del autor</span></p>'),
  # flashbacks: se tiran
  ('<tr><td>Flashbacks</td><td>16</td><td>Concepto del autor; coste sin validar</td></tr>',
   '<tr><td>Flashbacks</td><td>16</td><td>Se tiran: ver abajo</td></tr>'),
  ('<tr><td>Relojes de progreso (y de viaje / suministros)</td><td>3, 16</td><td>Concepto del autor; cifras sin validar</td></tr>',
   '<tr><td>Relojes de progreso (y de viaje / suministros)</td><td>3, 16</td><td>Aprobado</td></tr>'),
  ('<tr><td>Transformación</td><td>18</td><td>Concepto del autor; cifras sin validar</td></tr>',
   '<tr><td>Transformación</td><td>18</td><td>Aprobado: termina siempre al acabar la escena</td></tr>'),
  ('<tr><td>Daño ambiental</td><td>10</td><td>Concepto del autor; cifras sin validar</td></tr>',
   '<tr><td>Daño ambiental</td><td>10</td><td>Aprobado: el daño sube con la exposición</td></tr>'),
  ('<tr><td>Vínculos</td><td>14</td><td>Concepto de receta; mecánica sin validar</td></tr>',
   '<tr><td>Vínculos</td><td>14</td><td>Aprobado: lo que cubre lo decide el universo</td></tr>'),
  ('<li><strong>Cambiar de funda</strong> causa <span class="tag">Daño Espiritual 1</span> <span class="tag">Esq: Nula</span> <span class="tag">Abs: Nula</span>. En esta receta la barra Espiritual se llama <strong>Identidad</strong>: si se vacía, el personaje olvida quién es y pasa a ser un PNJ. <span class="flag proposal">Propuesta sin validar</span> <span class="flag ed">ED-R2</span></li>',
   '<li><strong>Cambiar de funda</strong> causa <span class="tag">Daño Mental 1</span> <span class="tag">Esq: Nula</span> <span class="tag">Abs: Nula</span>. Aquí la barra Mental se llama <strong>Identidad</strong> (ED-39: no hay Arcano, así que no hay barra Espiritual). <strong>Vaciarla nunca retira la ficha.</strong> Lo que hay al otro lado es terapia —danza mental, reconstrucción, el tiempo— y vuelves siendo <em>un personaje muy distinto</em>, que es mucho mejor material de mesa que un hueco. Los casos severos no se juegan como protagonistas salvo acuerdo expreso, y perder la ficha solo pasa en partidas cortas donde ese final estaba pactado desde el principio. <span class="src">Decisión del autor</span> <span class="flag ed">ED-R2</span></li>'),
  ('<li><strong>Corrupción</strong> (barra Espiritual rebautizada) en grimdark; <strong>Empatía</strong> e <strong>Identidad</strong> (barra Mental rebautizada) en ciberpunk y mentes digitales, porque allí la pérdida es cognitiva y no sobrenatural. <em>Recetas 2, 8, 9.</em></li>',
   '<li><strong>Corrupción</strong> (barra Espiritual rebautizada) en grimdark; <strong>Humanidad</strong> e <strong>Identidad</strong> (barra Mental rebautizada) en ciberpunk y mentes digitales, porque allí la pérdida es cognitiva y no sobrenatural. <em>Recetas 2, 8, 9.</em></li>'),
  ('<p>Los nombres son del autor y de las recetas; los usos concretos de cada barra (qué la llena, qué la vacía) están sin validar. <span class="flag proposal">Propuesta sin validar</span>',
   '<p>Los nombres son del autor y de las recetas, y los usos concretos de cada barra están decididos en <a href="#ch8-tablas">las tablas de problemas</a> y en ED-39.'),
  ('<strong>Sangre</strong> (barra Mental rebautizada): el estrés del vampiro; se gasta para activar poderes. <em>Receta 13.</em>',
   '<strong>Sed</strong> (barra Mental rebautizada): el ansia del vampiro, que se juega como una abstinencia. <em>Receta 13.</em>'),
 ],
 # ------------------------------------------------ [Lento]
 'frag_ch3.html': [
  ('La etiqueta [Lento] sigue abierta.',
   'Y la etiqueta <strong>[Lento]</strong> ya tiene regla: una habilidad marcada así <strong>no sirve para tirar iniciativa</strong>. O entras con otra disposición, o vas el último. <span class="src">Decisión del autor</span>'),
 ],
 'frag_ch3.en.html': [
  ('The [Slow] tag is still open.',
   'And the <strong>[Slow]</strong> tag now has a rule: a skill marked that way <strong>cannot be used to roll initiative</strong>. Either you enter with a different stance, or you go last. <span class="src">Author’s decision</span>'),
 ],
}

for f, subs in SUB.items():
    s = io.open(f, encoding='utf-8').read()
    for a, b in subs:
        n = s.count(a)
        print('%-20s %d  %s' % (f, n, a[:48].replace('\n', ' ')))
        s = s.replace(a, b)
    io.open(f, 'w', encoding='utf-8').write(s)
