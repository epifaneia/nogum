# -*- coding: utf-8 -*-
"""El Cuaderno registra la tanda de las Llaves y cierra tres preguntas abiertas."""
import io, os, shutil
os.chdir(os.path.dirname(os.path.abspath(__file__)))
F = 'frag_editorial.html'
shutil.copyfile(F, F + '.bak_llaves')
s = io.open(F, encoding='utf-8').read()

ROWS = """<tr><td class="num"><span class="flag ed">ED-27</span></td><td><strong>Qué cubre una Llave.</strong> Una Disciplina para siempre, o un Ámbito entero durante una escena, y se elige la forma al comprarla. La Llave ancha se ata a una escena y no a un enemigo, por el argumento del autor: un monstruo que vuelve cuando ya sabes cómo matarlo ha dejado de ser un antagonista, y si vuelve cambiado ya no es el mismo. De paso, la escena queda consagrada como unidad de tiempo del juego: tono, Estilo, Llave ancha y arma robada se miden todos en escenas.</td><td><a href="#ch2-llave">2.3</a></td></tr>
<tr><td class="num"><span class="flag ed">ED-28</span></td><td><strong>Llave propia y Llave prestada.</strong> La comprada es permanente y se escribe; la que regala el Director por una buena idea dura una escena y no se apunta. Así el Director puede seguir premiando el ingenio sin inflar la ficha. El traspaso es una transacción, no un préstamo: el dueño libera y el otro paga de su monedero.</td><td><a href="#ch2-llave">2.3</a></td></tr>
<tr><td class="num"><span class="flag ed">ED-29</span></td><td><strong>El ×100.</strong> Cada nivel de Rejilla multiplica por cien el alcance: persona, sala, edificio, ciudad, país ya eran los peldaños; el número solo se pone delante. Se escribe como <em>alcance</em> y no como literalidad, para que nadie pregunte cuánto peso levanta un Físico 2. Con el número puesto, «un nivel de diferencia decide sin tirar» deja de parecer arbitrario: son dos ceros.</td><td><a href="#ch2-rejilla">2.4</a></td></tr>
<tr><td class="num"><span class="flag ed">ED-30</span></td><td><strong>Techo de Rejilla por universo.</strong> El nivel inicial lo pone la campaña y el techo lo pone el género. Las veinte recetas traen su techo por ámbito, y la Llave es la excepción pactada. Es la palanca que faltaba para que la emulación se notara fuera del tono y del equipo: en cyberpunk no existe un ingenio por cien, pero sí el exploit contra <em>esa</em> IA.</td><td><a href="#ch8-recetas">8.4</a></td></tr>
<tr><td class="num"><span class="flag ed">ED-31</span></td><td><strong>12 puntos, 14 con Arcano, y el bote aparte.</strong> La proporción es la razón: 40 casillas sin magia y 50 con ella dejan la misma escasez. El bote (+1 de Rejilla en un ámbito <em>o</em> 5 Llaves) no se cambia por puntos en ninguna dirección, para matar al héroe de Rejilla sin oficio. Y la elección no es neutra: diez casillas por cinco monedas contra una por una, «la libertad se paga al doble». Los 10 puntos del borrador quedan superados.</td><td><a href="#ch3-economia">3.5</a></td></tr>
<tr><td class="num"><span class="flag ed">ED-32</span></td><td><strong>La escalera cuadrada.</strong> Subir <em>n</em> niveles contra la misma cosa cuesta <em>n</em>² Llaves, con la escalera llana (3<em>n</em>−2) como regla opcional para quien quiera divinidad a plazos. Coinciden en 1 y 4, que es donde juega casi todo el mundo. Efecto que no hace falta escribir como prohibición: con cinco Llaves en el bote, nadie empieza por encima de +2.</td><td><a href="#ch2-llave">2.3</a></td></tr>
<tr><td class="num"><span class="flag ed">ED-33</span></td><td><strong>Los dos monederos.</strong> La experiencia deja de ser un contador: puntos de habilidad y Llaves son dos bolsas independientes, con la misma pregunta de velocidad hecha dos veces. El hallazgo que ordena el capítulo: los puntos saturan porque el Ancla corta en +4, y las Llaves no saturan nunca. De ahí la frase de cabecera: si quieres que la campaña escale, abre el grifo de las Llaves, no el de los puntos.</td><td><a href="#ch3-progreso">3.6</a></td></tr>
<tr><td class="num"><span class="flag ed">ED-34</span></td><td><strong>Los tres cerrojos del equipo.</strong> Dinero (el Acceso en Recursos, escrito en la ficha técnica), permiso narrativo y Llaves si el objeto rompe la Rejilla. Cierra un agujero clásico —una pistola de catálogo regalaba lo que un personaje paga con nueve Llaves— y convierte el saqueo en una decisión: lo robado funciona una escena gratis y luego se paga o se deja.</td><td><a href="#ch4-equipo">4.3</a></td></tr>
<tr><td class="num"><span class="flag ed">ED-35</span></td><td><strong>La lacra es la cicatriz de un bloque lleno.</strong> Dones y lacras no se compran: aparecen cuando se llena un bloque de la barra Mental o Espiritual y el personaje se cura. Eso ata la vida fractal con la ficha y obliga a escribir lo que faltaba, que era qué hace de verdad el daño mental y el espiritual bloque a bloque.</td><td><a href="#ch5-dano">5.5</a></td></tr>
<tr><td>El Bazar dice lo que cuesta</td><td>Los 294 objetos llevan <span class="tag">Acceso 0–3</span> derivado del daño y de la rareza en una sola pasada, y los doce que rompen la Rejilla llevan además su precio en Llaves. Las tablas de poderes —la Fuerza, el ki, las disciplinas, los superpoderes, los toon y el arsenal social— se quedan sin Acceso a propósito: no se compran con dinero, describen lo que ya eres. De paso se completaron 22 fichas técnicas que el borrador había dejado a medias.</td><td><a href="#apx-bazar">8.3</a></td></tr>
<tr><td>Las recetas eligen de verdad</td><td>El remapeo mecánico de las tarjetas había dejado frases que ofrecían la misma tarjeta dos veces («Épica o Épica»). Revisadas una a una, con una elección real y un contraste en cada caso. La predicción del autor se cumple con una excepción, y es la buena: <strong>la única receta de las veinte que usa la fila opresiva es la de Cthulhu</strong>, con Angustia, cuyos porcentajes reproducen el reparto del género.</td><td><a href="#ch8-recetas">8.4</a></td></tr>
"""

anchor = '<tr><td>El menú de la pifia</td>'
assert anchor in s
s = s.replace(anchor, ROWS + anchor)

CIERRES = [
 ('<li>Presupuestos de Rejilla por tipo de campaña (niveles iniciales).</li>',
  '<li>Presupuestos de Rejilla por tipo de campaña (niveles iniciales). <strong>Medio cerrado</strong>: '
  'los <em>techos</em> por universo ya están decididos receta a receta (ED-30); el nivel inicial sigue siendo '
  'decisión de la mesa.</li>'),
 ('<li>Capítulo de experiencia (costes y ritmos).</li>',
  '<li>Capítulo de experiencia (costes y ritmos). <strong>Cerrado</strong>: escrito en '
  '<a href="#ch3-progreso">3.6</a> con los dos monederos, las cinco velocidades, el mérito que suma encima de '
  'una base y la lista de lo que se premia.</li>'),
 ('<li>Capítulo de aspectos (dones y lacras) y su coste, incluida la etiqueta [Lento].</li>',
  '<li>Capítulo de aspectos (dones y lacras) y su coste. <strong>Cerrado en lo esencial</strong>: no tienen '
  'coste porque no se compran (ED-35). Sigue abierta la etiqueta [Lento].</li>'),
]
for a, b in CIERRES:
    assert a in s, a[:40]
    s = s.replace(a, b)

io.open(F, 'w', encoding='utf-8').write(s)
print('cuaderno al dia')
