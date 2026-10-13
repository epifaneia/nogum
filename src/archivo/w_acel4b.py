# -*- coding: utf-8 -*-
"""Segunda pasada: la tabla de tiradas, el exito parcial, la vida y las
menciones sueltas de Agobio."""
import io, os, re, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
fal = []


def rep(f, s, a, b, q, n=1):
    if s.count(a) != n:
        fal.append('%s :: %s (%d, esperaba %d)' % (f, q, s.count(a), n))
        return s
    return s.replace(a, b, n)


ES, EN = 'frag_acelerado.html', 'frag_acelerado.en.html'
s = io.open(ES, encoding='utf-8').read()

# -------- la tabla de la tirada unica
s = rep(ES, s,
 '<tr><td><strong>Épico</strong></td><td>El <strong>mayor</strong> de los dos</td><td>Doble 1</td><td>Un 10 en cualquiera</td><td>Total 6 o más: éxito</td></tr>\n'
 '<tr><td><strong>Neutro</strong></td><td><strong>Solo el rojo</strong> (el azul no cuenta)</td><td>1 en el rojo</td><td>10 en el rojo</td><td>Total 6 o más: éxito</td></tr>\n'
 '<tr><td><strong>Agobio</strong></td><td>El <strong>menor</strong> de los dos</td><td>Un 1 en cualquiera</td><td>Doble 10</td><td>Total 5 o menos: fallo · 6 o 7: <strong>éxito parcial</strong> · 8 o más: éxito <span class="flag ed">ED-15</span></td></tr>',
 '<tr><td><strong>Optimista</strong></td><td>El <strong>mayor</strong> de los dos</td><td>Doble 1</td><td>Un 10 en cualquiera</td><td>Total 6 o más: éxito</td></tr>\n'
 '<tr><td><strong>Neutro</strong></td><td><strong>Solo el rojo</strong> (el azul no cuenta)</td><td>1 en el rojo</td><td>10 en el rojo</td><td>Total 6 o más: éxito</td></tr>\n'
 '<tr><td><strong>Caos</strong></td><td><strong>Solo el rojo</strong> (el azul no cuenta)</td><td>1 <strong>o 2</strong> en el rojo</td><td>9 <strong>o 10</strong> en el rojo</td><td>Total 5 o menos: fallo · 6 o 7: <strong>éxito parcial</strong> · 8 o más: éxito <span class="flag ed">ED-15</span></td></tr>\n'
 '<tr><td><strong>Terror</strong></td><td><strong>Solo el rojo</strong> (el azul no cuenta)</td><td>1 en el rojo</td><td>10 en el rojo</td><td>Total 6 o más: éxito · <strong>y solo 3 casillas de vida</strong> (2.6)</td></tr>',
 'tabla de tirada')

# -------- el exito parcial
s = rep(ES, s, '<p><strong>Éxito parcial (solo en Agobio).</strong>',
        '<p><strong>Éxito parcial (solo en Caos).</strong>', 'exito parcial')

s = rep(ES, s,
 '<p><strong>ED-15.</strong> El autor dijo «peor de dos dados + éxito parcial», sin fijar las bandas. Son las del manual completo: el éxito con coste ocupa la TN y el punto de encima (total 6 o 7), aplicado al dado menor. Nunca convierte un fallo en éxito; solo cobra peaje a lo que ya había salido bien.',
 '<p><strong>ED-15.</strong> Las bandas del modo Caos son exactamente las de la tarjeta Comedia negra del manual completo: dado rojo, pifia con 1 o 2, crítico con 9 o 10, y el éxito con coste ocupando la TN y el punto de encima (total 6 o 7). Nunca convierte un fallo en éxito; solo cobra peaje a lo que ya había salido bien.',
 'ED-15')

# -------- el aside de los porcentajes
i = s.find('<aside class="meta"><p>Mismo personaje (+2), misma tarea:')
j = s.find('</aside>', i)
if i < 0 or j < 0:
    fal.append('%s :: aside de porcentajes' % ES)
else:
    s = s[:i] + ('<aside class="meta"><p>Mismo personaje (+2), misma tarea. En <strong>Optimista</strong> lo consigue el 91&nbsp;% de las veces. En <strong>Neutro</strong>, el 70&nbsp;%. '
                 'En <strong>Caos</strong>, también el 70&nbsp;% —leíste bien, el mismo número— pero tres de cada siete de esas veces pagando un precio, y con el doble de pifias y el doble de críticos. '
                 'En <strong>Terror</strong>, otra vez el 70&nbsp;%: lo que cambia es que ahora dos golpes le dejan fuera. '
                 'No has tocado la ficha en ningún momento: has cambiado la atmósfera tres veces de tres maneras distintas.</p></aside>') + s[j + 8:]

# -------- la vida
s = rep(ES, s,
 '<p>Todo personaje tiene <strong>9 casillas de vida</strong>, en tres bloques de tres. Cada punto de daño tacha una casilla.</p>',
 '<p>Todo personaje tiene <strong>9 casillas de vida</strong>, en tres bloques de tres. Cada punto de daño tacha una casilla.</p>\n'
 '<div class="rule"><p class="rule-title">Salvo en Terror</p>\n'
 '<p>En el modo <strong>Terror</strong> no son nueve: son <strong>3 casillas</strong>, un solo bloque. Al llenarlo estás fuera de combate. '
 'Con el daño de este manual eso significa que <strong>dos impactos serios te sacan de la escena</strong>, y que la granada de la tabla de armas no es una amenaza: es el final.</p>\n'
 '<p>No es un interruptor que tengas que acordarte de encender. Viene con el modo, y es la única pieza de este manual que te deja asomarte a lo que el completo llama <strong>vida fractal</strong>: ahí la letalidad es un mando y lo giras tú, con tres, nueve o veintisiete casillas.</p></div>',
 'vida 3 en terror')

# -------- menciones sueltas
s = rep(ES, s, '<p><strong>En Agobio</strong>, un éxito parcial en combate',
        '<p><strong>En Caos</strong>, un éxito parcial en combate', 'combate')
s = rep(ES, s, '<li><strong>Fallo</strong> (y, en Agobio, el éxito parcial):',
        '<li><strong>Fallo</strong> (y, en Caos, el éxito parcial):', 'estilo')
s = rep(ES, s, '<tr><td>Empezamos en modo Agobio</td>',
        '<tr><td>Empezamos en modo Terror</td>', 'tabla de arranque')
s = rep(ES, s, '<tr><td>Modo de la partida</td><td>Épico / Neutro / Agobio.</td></tr>',
        '<tr><td>Modo de la partida</td><td>Optimista / Neutro / Caos / Terror.</td></tr>', 'hoja de referencia')
s = rep(ES, s,
 '<li><strong>ED-A1.</strong> Tabla de cruce del selector: optimismo alto → Épico; optimismo bajo → Agobio; optimismo normal → Neutro, salvo con caos «mucho», que va a Agobio (la única herramienta de caos del manual).</li>',
 '<li><strong>ED-A1.</strong> Tabla de cruce del selector: optimismo alto → Optimista; optimismo bajo → Terror; optimismo normal → Neutro, salvo con caos «mucho», que va a Caos.</li>',
 'ED-A1 lista')
io.open(ES, 'w', encoding='utf-8').write(s)
if fal:
    print('FALLOS:')
    for m in fal:
        print('  ' + m)
    sys.exit(1)
print('castellano: tabla, parcial, vida y menciones')
