# -*- coding: utf-8 -*-
"""Los ejemplos trabajados, rehechos: la Firma cuesta 2 y existe el Torpe."""
import io, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
fal = []


def sub(f, a, b, n=1):
    s = io.open(f, encoding='utf-8').read()
    if s.count(a) != n:
        fal.append('%s (%d!=%d) %s' % (f, s.count(a), n, a[:56])); return
    io.open(f, 'w', encoding='utf-8').write(s.replace(a, b, n))


# ------------------------------------------------------------------ CASO A es
sub('frag_ch3.html', 'Quiere ser el mejor disparando (+4) y muy duro (+3).',
    'Quiere ser el mejor disparando (+4) y aguantar lo que le echen (+4).')
sub('frag_ch3.html',
    '<tr><td>Físico → Vigor → Entereza → Firma «Aguantar el dolor» (1 punto)</td><td>Vigor +1 · Entereza +2 · Aguantar el dolor +3</td><td class="num">3</td></tr>',
    '<tr><td>Físico → Vigor → Entereza → Firma «Aguantar el dolor»</td><td>Vigor +1 · Entereza +2 · Aguantar el dolor +4</td><td class="num">4</td></tr>')
sub('frag_ch3.html',
    '<tr><td>Físico → Vigor (ya pagado) → Armas → Firma «Pistolas» (2 puntos)</td><td>Armas +2 · Pistolas +4</td><td class="num">3</td></tr>',
    '<tr><td>Físico → Vigor (ya pagado) → Armas → Firma «Pistolas»</td><td>Armas +2 · Pistolas +4</td><td class="num">3</td></tr>')
sub('frag_ch3.html',
    '<tr><td>Físico → Destreza</td><td>Destreza +1</td><td class="num">1</td></tr>\n',
    '')
sub('frag_ch3.html',
    '<tr><td>Social → nada · Arcano → nada</td><td>Nulidad −2 en ambos</td><td class="num">0</td></tr>',
    '<tr><td>Social → nada · Arcano → nada</td><td>Nulidad −2 en ambos</td><td class="num">0</td></tr>\n'
    '<tr><td>Lo que deja sin tocar dentro de lo suyo</td><td>Torpe −1 en Destreza, en Erudición y en Artificio</td><td class="num">0</td></tr>')
sub('frag_ch3.html',
    'es letal disparando (+4), duro (+3), sabe conducir y no le pillan por sorpresa. Pero tiene <strong>Nulidad (−2)</strong> en todo lo social.',
    'es letal disparando (+4), aguanta lo que le echen (+4), sabe conducir y no le pillan por sorpresa. Pero tiene <strong>Nulidad (−2)</strong> en todo lo social y en lo arcano, y está <strong>Torpe (−1)</strong> en Destreza, en Erudición y en Artificio: es un armario que no trepa, no recuerda fechas y no arregla nada.')

# ------------------------------------------------------------------ CASO B es
sub('frag_ch3.html',
    '<li>Compra un Dominio en cada ámbito (5 puntos): ya no es nulo en nada. Tira con +1 en sus Dominios y con +0 en todo lo demás.</li>',
    '<li>Compra un Dominio en cada ámbito (5 puntos): ya no es <strong>nulo</strong> en ninguno. Tira con +1 en sus cinco Dominios y con <strong>−1</strong> en los otros cinco: no es nulo en ningún sitio, pero sigue estando <strong>torpe</strong> en media ficha.</li>')
sub('frag_ch3.html',
    '<p><strong>Resultado:</strong> es una navaja suiza utilísima, pero nunca brillará con un +4.</p>',
    '<p><strong>Resultado:</strong> es una navaja suiza utilísima, pero nunca brillará con un +4. Si quisiera además quitarse el −1 de encima tendría que comprar <strong>las diez columnas</strong>, y entonces no le quedaría casi nada para profundidad: diez puntos de doce. Esa es la tercera ficha posible, la <em>ancha del todo</em>, y es la que menos falla y la que menos luce.</p>')
sub('frag_ch3.html',
    'El sistema cobra el peaje solo, sin que haya que prohibir nada: <strong>el precio de las Firmas es ser una nulidad</strong>.',
    'El sistema cobra el peaje solo, sin que haya que prohibir nada: <strong>el precio de las Firmas es ser una nulidad</strong>. Y por debajo hay un segundo peaje más barato y más frecuente: cubrir las <strong>diez columnas</strong> para no estar torpe en ninguna cuesta diez puntos de doce, así que casi todas las fichas están torpes en alguna parte. Eso no es un defecto de la ficha: es su forma.')

# ------------------------------------------------------------------ CASO A en
sub('frag_ch3.en.html', 'Wants to be the best shot (+4) and very tough (+3).',
    'Wants to be the best shot (+4) and to take whatever comes (+4).')
sub('frag_ch3.en.html',
    'he is lethal with a gun (+4), tough (+3), can drive and is hard to surprise. But he has <strong>Null (−2)</strong> in everything social.',
    'he is lethal with a gun (+4), takes whatever comes (+4), can drive and is hard to surprise. But he has <strong>Null (−2)</strong> in everything social and arcane, and he is <strong>Clumsy (−1)</strong> at Dexterity, Erudition and Artifice: a wardrobe that cannot climb, cannot remember a date and cannot fix a thing.')

if fal:
    print('FALLOS:')
    for x in fal:
        print('  ' + x)
    sys.exit(1)
print('ejemplos rehechos (es completo, en parcial)')
