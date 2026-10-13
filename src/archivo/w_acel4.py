# -*- coding: utf-8 -*-
"""El Acelerado pasa de tres modos a cuatro.

Fuera el Agobio (peor de dos + coste), que era una tarjeta que no existe en el
Cuadrante y que cargaba al DJ con un 35-51 % de tiradas que inventar. En su
lugar, cuatro modos que SI son configuraciones legales del manual completo:

  Optimista = Epica            (mejor de dos)
  Neutro    = Primera marcha   (solo el rojo)
  Caos      = Comedia negra    (solo el rojo, bandas anchas, exito parcial)
  Terror    = Primera marcha + vida Letal (3 casillas)

La oscuridad deja de venir de la lectura del dado y viene de la vida. Y el 3
va anclado al Terror, no es un interruptor: asi el jugador se asoma al mando de
la letalidad sin tener que decidir cuando encenderlo.
"""
import io, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))

ES = 'frag_acelerado.html'
EN = 'frag_acelerado.en.html'
fal = []


def rep(f, s, a, b, q):
    if s.count(a) != 1:
        fal.append('%s :: %s (%d veces)' % (f, q, s.count(a)))
        return s
    return s.replace(a, b, 1)


# ---------------------------------------------------------------- castellano
s = io.open(ES, encoding='utf-8').read()

s = rep(ES, s, '<tr><td><strong>Lo normal</strong></td><td>Neutro</td><td>Neutro</td><td>Agobio <span class="flag ed">ED-A1</span></td></tr>\n'
              '<tr><td><strong>Poco</strong></td><td>Agobio</td><td>Agobio</td><td>Agobio</td></tr>',
        '<tr><td><strong>Lo normal</strong></td><td>Neutro</td><td>Neutro</td><td>Caos <span class="flag ed">ED-A1</span></td></tr>\n'
        '<tr><td><strong>Poco</strong></td><td>Terror</td><td>Terror</td><td>Terror</td></tr>', 'cruce filas')
s = rep(ES, s, '<tr><td><strong>Mucho</strong></td><td>Épico</td><td>Épico</td><td>Épico</td></tr>',
        '<tr><td><strong>Mucho</strong></td><td>Optimista</td><td>Optimista</td><td>Optimista</td></tr>', 'cruce mucho')

s = rep(ES, s,
        '<p>El optimismo es el que elige el modo. El caos solo cambia el resultado en una casilla. En este manual, la única herramienta de caos es el <strong>éxito parcial</strong> («sí, pero…»), y solo lo tiene el modo Agobio. Por eso un mundo con optimismo normal y <strong>mucho</strong> caos se juega en Agobio. Si el optimismo es alto, el caos se juega en Épico: el universo te quiere, aunque se ría de ti.</p>',
        '<p>El optimismo elige el modo y el caos decide una casilla. Son cuatro, y cada uno cambia una cosa y solo una:</p>\n'
        '<ul>\n'
        '<li><strong>Optimista</strong> cambia <em>el dado</em>: tiras dos y te quedas el mayor.</li>\n'
        '<li><strong>Neutro</strong> no cambia nada. Es la referencia.</li>\n'
        '<li><strong>Caos</strong> cambia <em>de qué está hecho el resultado</em>: mismo dado, bandas más anchas y éxitos que cobran peaje.</li>\n'
        '<li><strong>Terror</strong> cambia <em>lo que aguantas</em>: mismo dado que Neutro, pero tres casillas de vida en vez de nueve.</li>\n'
        '</ul>\n'
        '<p>Mira bien el tercero, porque es lo más raro y lo más importante de este manual: <strong>Caos y Neutro sacan adelante exactamente el mismo número de tiradas</strong>, un 50&nbsp;% con la ficha a cero y un 70&nbsp;% con la ficha a +2. El caos no te hace fallar más. Cambia de qué está hecho lo que te pasa: donde Neutro reparte éxitos y fallos limpios, Caos reparte pifias, críticos y victorias con factura.</p>\n'
        '<p>Y el cuarto es la otra forma de hacer daño. <strong>En Terror el mundo no es más cruel: tú eres más frágil.</strong> Tiras igual que en Neutro y aciertas igual de a menudo. Lo que cambia es que un cuchillo te mata. El manual completo llama a eso la <em>vida fractal</em> y la deja en tus manos; aquí viene puesta, para que la veas funcionar sin tener que decidir nada.</p>',
        'parrafo del cruce')

s = rep(ES, s,
        '<p><strong>ED-A1.</strong> El autor fijó los tres modos y que el caos «se nota» en Neutro frente a Agobio, pero no la tabla de cruce. Decisión editorial: optimismo normal + caos mucho = Agobio, y optimismo alto = Épico con cualquier caos.</p>',
        '<p><strong>ED-A1.</strong> El autor fijó los cuatro modos, sus lecturas y que el 3 de vida va anclado al Terror y no es un interruptor. La tabla de cruce es decisión editorial: optimismo alto = Optimista con cualquier caos; optimismo normal + caos mucho = Caos; optimismo bajo = Terror con cualquier caos.</p>',
        'ED-A1')

s = rep(ES, s,
        '<aside class="meta"><p>¿Echas de menos algún tono? ¿Un mundo que sea un reloj suizo y a la vez cruel? ¿Una ruleta rusa donde un 9 ya es un milagro? Agobio, epicidad y neutralidad son suficientes para empezar y cubren a grandes rasgos todo. Cuando se te queden pequeños, NOGUM tiene nueve modos y te está esperando. <span class="src">T135</span></p></aside>',
        '<aside class="meta"><p>¿Echas de menos algún tono? ¿Un mundo que sea un reloj suizo y a la vez cruel? ¿Una ruleta rusa donde un 9 ya es un milagro? ¿Oscuro <em>y</em> caótico a la vez? Estos cuatro cubren a grandes rasgos todo y son suficientes para empezar. Y no son un invento aparte: los cuatro existen en el manual completo —Optimista es la Épica, Neutro es la Primera marcha, Caos es la Comedia negra y Terror es la Primera marcha con la vida corta—. Cuando se te queden pequeños, ya conoces cuatro de las siete tarjetas. <span class="src">T135</span></p></aside>',
        'aside tonos')
io.open(ES, 'w', encoding='utf-8').write(s)

# ------------------------------------------------------------------- english
s = io.open(EN, encoding='utf-8').read()
s = rep(EN, s, '<tr><td><strong>Normal</strong></td><td>Neutral</td><td>Neutral</td><td>Dread <span class="flag ed">ED-A1</span></td></tr>\n'
              '<tr><td><strong>Little</strong></td><td>Dread</td><td>Dread</td><td>Dread</td></tr>',
        '<tr><td><strong>Normal</strong></td><td>Neutral</td><td>Neutral</td><td>Chaos <span class="flag ed">ED-A1</span></td></tr>\n'
        '<tr><td><strong>Little</strong></td><td>Terror</td><td>Terror</td><td>Terror</td></tr>', 'cruce filas')
io.open(EN, 'w', encoding='utf-8').write(s)

if fal:
    print('FALLOS:')
    for m in fal:
        print('  ' + m)
    sys.exit(1)
print('cruce y explicacion: hechos')
