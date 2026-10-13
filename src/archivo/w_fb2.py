# -*- coding: utf-8 -*-
"""Feedback de lectura: capitulos 2, 3 y 4."""
import io, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
fal = []


def sub(f, a, b, n=1):
    s = io.open(f, encoding='utf-8').read()
    if s.count(a) != n:
        fal.append('%s (%d) %s' % (f, s.count(a), a[:52])); return
    io.open(f, 'w', encoding='utf-8').write(s.replace(a, b, n))


# -------- 8 · un universo puede no permitir NINGUN 2, y entonces van Llaves
sub('frag_ch2.html',
    '<strong>Si no quieres ese 2, te llevas 5 Llaves</strong> (<a href="#ch3-economia">3.5</a>): o eres grande donde tu mundo deja ser grande, o eres pequeño y muy concreto en lo que tú elijas.',
    '<strong>Si no quieres ese 2, te llevas 5 Llaves</strong> (<a href="#ch3-economia">3.5</a>): o eres grande donde tu mundo deja ser grande, o eres pequeño y muy concreto en lo que tú elijas. '
    'Y ojo, porque esto se lee mal con facilidad: <strong>ese 2 no es una obligación de colocarlo</strong>, es la escala que tu universo deja alcanzar. '
    'Hay mundos que <strong>no permiten ningún 2</strong> —un realista, unos zombis, cualquier cosa donde nadie levante un coche— y su receta marca cinco unos. '
    'Ahí no hay nada que elegir: <strong>todo el mundo empieza en [1,1,1,1,1] y se lleva las 5 Llaves</strong>, que es como se compra el ser grande en un sitio donde ser grande no viene de serie.')
sub('frag_ch2.en.html',
    '<strong>If you do not want that 2, you take 5 Keys</strong>',
    '<strong>If you do not want that 2, you take 5 Keys</strong>')

# -------- 11 · la lista cerrada: decir que la app las acota
sub('frag_ch3.html',
    '<h3 id="ch3-lista">3.2 La lista cerrada (el esqueleto de tu personaje)</h3>\n<p>NOGUM quiere ponértelo fácil',
    '<h3 id="ch3-lista">3.2 La lista cerrada (el esqueleto de tu personaje)</h3>\n'
    '<p class="note"><strong>Antes de que te abrume:</strong> una lista de cuarenta Disciplinas asusta en una página, y con razón. '
    'La hemos mantenido porque <strong>la app la acota por ti</strong>: te enseña solo lo que tu mundo permite y te lleva por ella sin que tengas que leerla entera. '
    'Este manual está escrito para que <strong>no tengas que consultar ninguna lista</strong>. Si en cambio te gusta leer catálogos largos a la vieja usanza, '
    'los tienes enteros en los apéndices (<a href="#ch8-skills">8.2</a>) y en el Bazar (<a href="#apx-bazar">8.3</a>): están ahí por gusto, no por obligación.</p>\n'
    '<p>NOGUM quiere ponértelo fácil')

# -------- 12 · el peaje, releido a la luz del -1
sub('frag_ch3.html',
    'Para no ser Nulidad en ningún sitio basta con un Dominio en cada Ámbito: cuatro puntos en un universo sin magia. Te quedan ocho, que son exactamente <strong>dos Grandes Maestros</strong> (Dominio 1 + Disciplina 1 + Firma 2 = 4 puntos cada uno). El tercero solo sale si renuncias a cubrir un Ámbito entero y te quedas en −2 allí. El sistema cobra el peaje solo, sin que haya que prohibir nada: <strong>el precio de las Firmas es ser una nulidad</strong>. Y por debajo hay un segundo peaje más barato y más frecuente: cubrir las <strong>diez columnas</strong> para no estar torpe en ninguna cuesta diez puntos de doce, así que casi todas las fichas están torpes en alguna parte. Eso no es un defecto de la ficha: es su forma.',
    'Hay <strong>dos peajes</strong>, y conviene no confundirlos.</p>\n'
    '<p><strong>El caro, el −2.</strong> Para no ser Nulidad en ningún sitio basta con un Dominio en cada Ámbito: cuatro puntos en un universo sin magia, cinco con él. '
    'Te quedan ocho, que son exactamente <strong>dos Grandes Maestros</strong> (Dominio 1 + Disciplina 1 + Firma 2 = 4 puntos cada uno). El tercero solo sale si renuncias a un Ámbito entero y te quedas en −2 allí. '
    'El sistema cobra solo, sin prohibir nada: <strong>el precio de las Firmas es ser una nulidad</strong>.</p>\n'
    '<p><strong>El barato, el −1.</strong> Quitarte el Torpe de encima es otra cosa: son <strong>diez columnas</strong>, una por Dominio, y cubrirlas todas cuesta <strong>diez puntos de doce</strong>. '
    'Nadie lo hace, porque dejaría dos para profundidad. Así que <strong>casi todas las fichas están torpes en alguna parte</strong>, y eso no es un defecto: es la forma de la ficha. '
    'La diferencia entre las dos fichas típicas está justo ahí: la ancha casi nunca está torpe y casi nunca brilla; la profunda brilla en lo suyo y se arrastra fuera. '
    'Las dos son legales, y lo único que el juego pide es que en la mesa se sepa cuál ha hecho cada uno.')

# -------- 14 · falta el -1 en el peso de la competencia
sub('frag_ch4.html',
    '<li><strong>La Nulidad (−2): el lastre.</strong>',
    '<li><strong>El Torpe (−1): el pie cambiado.</strong> Tienes el ámbito pero esa columna está vacía. Tu probabilidad baja del 50&nbsp;% al 40&nbsp;%: un poco, y se nota. '
    'Con el peor de 2d10 (tarjeta Angustia) cae al 16&nbsp;%, y ahí ya no es poco. Es lo que le pasa al forzudo cuando le piden una acrobacia.</li>\n'
    '<li><strong>La Nulidad (−2): el lastre.</strong>')

if fal:
    print('FALLOS:')
    for x in fal:
        print('  ' + x)
    sys.exit(1)
print('8, 11, 12 y 14 aplicados')
