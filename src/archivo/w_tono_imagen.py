# -*- coding: utf-8 -*-
"""La postura sobre las imagenes, en la Tesis. Toda imagen lleva tono."""
import io, os, re, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
fal = []


def sub(f, a, b, n=1):
    s = io.open(f, encoding='utf-8').read()
    if s.count(a) != n:
        fal.append('%s (%d!=%d) %s' % (f, s.count(a), n, a[:58])); return
    io.open(f, 'w', encoding='utf-8').write(s.replace(a, b, n))


# ------------------------------------------- 1. el capitulo que faltaba por color
s = io.open('paper.css', encoding='utf-8').read()
a = '.sheet[data-cap="intro"]{--cap:#4b6ea8}'
if '.sheet[data-cap="como-leer"]' not in s:
    io.open('paper.css', 'w', encoding='utf-8').write(
        s.replace(a, '.sheet[data-cap="como-leer"]{--cap:#6b7382}\n' + a, 1))
    print('  color para «Como leer este manual»')

# ------------------------------------- 2. la postura, en la Tesis (es y en)
TESIS_ES = """<h3 id="es-sin-imagenes">Por qué este manual no lleva ilustraciones</h3>
<p>No es que no haya habido presupuesto. Es que <strong>toda imagen lleva tono</strong>.</p>
<p>Dibuja a un guerrero con una espada y ya has decidido algo: si el trazo es limpio y heroico, el libro promete épica; si está sucio y la sangre pesa, promete miseria; si tiene los ojos grandes, promete otra cosa. No hay forma de ilustrar sin elegir. Y un manual cuyo argumento entero es <em>que el tono es un mando y lo pones tú</em> no puede permitirse decidirlo por ti en la primera página.</p>
<p>Un libro ilustrado te dice cómo se juega antes de que lo leas. Este no quiere decirte eso. Quiere que la misma ficha sirva para el pirata de goma y para el sicario que venga perros, y una ilustración de cualquiera de los dos le quita sitio al otro.</p>
<p>Así que la ausencia es una postura: <strong>la portada no pone el tono, lo pone la mesa</strong>. Lo único que puede aparecer dibujado aquí son <strong>diagramas</strong> —el sistema explicándose a sí mismo—, porque un esquema no cuenta una historia. El Cuadrante dibujado es el Cuadrante; un orco dibujado ya es un género.</p>
<p>Si algún día hay arte, irá donde no estorbe: en las recetas, que sí tienen tono porque ese es justo su trabajo. En el núcleo, no.</p>
"""
TESIS_EN = """<h3 id="en-sin-imagenes">Why this manual has no illustrations</h3>
<p>It is not that there was no budget. It is that <strong>every image carries tone</strong>.</p>
<p>Draw a warrior with a sword and you have already decided something: if the line is clean and heroic, the book promises epic; if it is dirty and the blood has weight, it promises misery; if the eyes are big, it promises something else again. There is no way to illustrate without choosing. And a manual whose whole argument is <em>that tone is a dial and you are the one who sets it</em> cannot afford to settle that for you on page one.</p>
<p>An illustrated book tells you how it plays before you read it. This one does not want to say that. It wants the same sheet to serve the rubber pirate and the hitman who avenges dogs, and an illustration of either one takes room away from the other.</p>
<p>So the absence is a position: <strong>the cover does not set the tone; the table does</strong>. The only thing that may be drawn here is a <strong>diagram</strong> —the system explaining itself— because a schematic tells no story. A drawn Quadrant is the Quadrant; a drawn orc is already a genre.</p>
<p>If there is ever art, it will go where it does no harm: in the recipes, which do have a tone because that is precisely their job. Not in the core.</p>
"""
for f, txt, marca in (('p_tesis_es.html', TESIS_ES, 'es'), ('p_tesis_en.html', TESIS_EN, 'en')):
    try:
        s = io.open(f, encoding='utf-8').read()
    except IOError:
        fal.append('no existe %s' % f); continue
    if 'sin-imagenes' in s:
        print('  %s: ya estaba' % f); continue
    # va al final, antes de cerrar la ultima seccion
    i = s.rstrip().rfind('</section>')
    if i < 0:
        fal.append('%s: no encuentro donde meterlo' % f); continue
    io.open(f, 'w', encoding='utf-8').write(s[:i] + txt + s[i:])
    print('  %s: postura escrita' % f)

if fal:
    print('FALLOS:')
    for x in fal:
        print('  ' + x)
    sys.exit(1)
print('listo')
