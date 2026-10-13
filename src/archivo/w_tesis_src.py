# -*- coding: utf-8 -*-
"""La Tesis, esta vez en su fichero de verdad (p_tesis_*), que es de donde se regenera."""
import io, os, re, shutil, importlib.util
os.chdir(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location('mm', 'marcas_map.py')
mm = importlib.util.module_from_spec(spec); spec.loader.exec_module(mm)

ES_DUENOS = """
<section class="chapter" id="es-duenos">
<h2>5bis · Quién es dueño de cada cambio</h2>
<ul>
<li>Casi todos los juegos meten en el mismo saco de puntos tres cosas que no se parecen en nada, y por eso el guerrero de nivel quince es a la vez más hábil, más poderoso en el mundo y más curtido: solo hay un contador.</li>
<li>Aquí se separan y cada una tiene dueño. <strong>El mundo</strong> (la Rejilla) lo mueve el Director cuando los hechos lo justifican. <strong>Las cicatrices</strong> (dones y lacras) las pone la ficción: ocurren, no se compran. <strong>La competencia</strong> la decide la mesa, y son dos monederos distintos: puntos de habilidad y Llaves.</li>
<li>Y se nota en el ritmo, que es lo que de verdad define una campaña: los puntos solo te ensanchan, porque el Ancla los corta en +4; las Llaves abren equipo y rompen techos, y no saturan nunca. <strong>Si quieres que la campaña escale, abre el grifo de las Llaves, no el de los puntos.</strong></li>
<li>La consecuencia bonita: los personajes se ensanchan, el Director sube el mundo, y el desafío vuelve solo sin que nadie toque una tabla.</li>
</ul>
</section>
"""
EN_DUENOS = """
<section class="chapter" id="en-owners" lang="en">
<h2>5bis · Who owns each kind of change</h2>
<ul>
<li>Almost every game throws three completely different things into the same bag of points, which is why the level fifteen fighter is at once more skilled, more powerful in the world and more scarred: there is only one counter.</li>
<li>Here they are separated and each has an owner. <strong>The world</strong> (the Grid) is moved by the Director when the facts justify it. <strong>The scars</strong> (gifts and flaws) are placed by the fiction: they happen, they are not bought. <strong>Competence</strong> is decided by the table, and it is two different wallets: skill points and Keys.</li>
<li>And it shows in the pacing, which is what really defines a campaign: points only make you wider, because the Anchor cuts them off at +4; Keys open up equipment and break ceilings, and they never saturate. <strong>If you want the campaign to escalate, open the Key tap, not the points one.</strong></li>
<li>The pretty consequence: the characters widen, the Director raises the world, and the challenge comes back on its own without anybody touching a table.</li>
</ul>
</section>
"""

SUB = {
 'p_tesis_es.html': [
  ('Cruzados forman una <strong>malla tonal</strong> de nueve casillas que mapea los géneros. No es un menú cerrado: los tonos posibles son infinitos.',
   'Cruzados forman el <strong>Cuadrante</strong>, un mapa de tres filas por tres columnas donde viven siete tarjetas de reglas y dos huecos honrados. No es un menú cerrado: los tonos posibles son infinitos.'),
  ('<li><strong>La Vela:</strong> la Rejilla de Potencia mide la escala de impacto (habitación, oficina, edificio, ciudad, nación). Por eso uno rompe una isla y el otro una mandíbula.</li>',
   '<li><strong>La Vela:</strong> la Rejilla de Potencia mide la escala de impacto (habitación, oficina, edificio, ciudad, nación), y cada peldaño multiplica por cien tu alcance. Por eso uno rompe una isla y el otro una mandíbula: no es que sea mejor, es que juega con dos ceros más.</li>'),
 ],
 'p_tesis_en.html': [
  ('Crossed, they form a nine-cell <strong>tonal grid</strong> that maps genres. It is not a closed menu: the possible tones are endless.',
   'Crossed, they form the <strong>Quadrant</strong>, a three-by-three map holding seven rules cards and two honest gaps. It is not a closed menu: the possible tones are endless.'),
  ('<li><strong>The Sail:</strong> the Power Grid measures the scale of impact (room, office, building, city, nation). That is why one breaks an island and the other a jaw.</li>',
   '<li><strong>The Sail:</strong> the Power Grid measures the scale of impact (room, office, building, city, nation), and every rung multiplies your reach by a hundred. That is why one breaks an island and the other a jaw: not because he is better, but because he is playing with two more zeros.</li>'),
 ],
}
for f, subs in SUB.items():
    shutil.copyfile(f, f + '.bak_src')
    s = io.open(f, encoding='utf-8').read()
    for a, b in subs:
        print('%-18s %d  %s' % (f, s.count(a), a[:46]))
        s = s.replace(a, b)
    io.open(f, 'w', encoding='utf-8').write(s)

# el techo y la Llave, detras de la bala de la Llave
TECHO = [
 ('p_tesis_es.html', 'la kriptonita, el guerrero dormido tras el festín, mil hackers coordinados.</li>',
  '<li><strong>El universo pone el techo; la Llave es la excepción que se compra.</strong> Un techo sin excepciones aburre y una excepción sin techo rompe el juego. Por eso en una partida de cromo y lluvia no existe un ingenio por cien, pero sí existe el exploit que funciona contra <em>esa</em> IA.</li>'),
 ('p_tesis_en.html', 'kryptonite, the warrior asleep after the feast, a thousand hackers in sync.</li>',
  '<li><strong>The universe sets the ceiling; the Key is the exception you buy.</strong> A ceiling with no exceptions is boring and an exception with no ceiling breaks the game. That is why in a game of chrome and rain there is no wits-times-a-hundred, but there is the exploit that works against <em>that</em> AI.</li>'),
]
for f, marca, add in TECHO:
    s = io.open(f, encoding='utf-8').read()
    i = s.find(marca)
    if i < 0:
        print('  techo NO:', f); continue
    j = i + len(marca)
    s = s[:j] + '\n' + add + s[j:]
    io.open(f, 'w', encoding='utf-8').write(s)
    print('  techo ok:', f)

# la seccion 5bis
for f, sec, anchor in (('p_tesis_es.html', ES_DUENOS, '<section class="chapter" id="es-accidente">'),
                       ('p_tesis_en.html', EN_DUENOS, '<section class="chapter" id="en-accident"')):
    s = io.open(f, encoding='utf-8').read()
    i = s.find(anchor)
    if i < 0:
        print('  5bis NO:', f); continue
    s = s[:i] + sec.replace('class="chapter"', 'class="chapter cover"' if False else 'class="chapter"') + s[i:]
    io.open(f, 'w', encoding='utf-8').write(s)
    print('  5bis ok:', f)

# y el barrido
PARES = sorted(mm.INLINE, key=lambda x: -len(x[0]))
PRE = r'(</strong>\s|</em>\s|<br>|<td>|<li>|<p>|\. |: |» |«|\? |! |— |– )'
tot = 0
for f in ['p_tesis_es.html', 'p_tesis_en.html']:
    es = f.endswith('_es.html')
    s = io.open(f, encoding='utf-8').read()
    for a, b_es, b_en in PARES:
        b = b_es if es else b_en
        if a in s:
            tot += s.count(a)
            B = b[0].upper() + b[1:]
            s = re.sub(PRE + re.escape(a), lambda m: m.group(1) + B, s)
            s = s.replace(a, b)
    for n in sorted({b for _, b, _ in mm.INLINE} | {c for _, _, c in mm.INLINE}, key=lambda x: -len(x)):
        if n and n[0].islower():
            s = re.sub(PRE + re.escape(n), lambda m: m.group(1) + n[0].upper() + n[1:], s)
    for pat, rep in [(r'\ba el ', 'al '), (r'\bde el ', 'del '), (r'\bel el ', 'el '), (r'\bla el ', 'el '), (r'\bthe the ', 'the ')]:
        s = re.sub(pat, rep, s)
    io.open(f, 'w', encoding='utf-8').write(s)
print('marcas en la Tesis:', tot)
