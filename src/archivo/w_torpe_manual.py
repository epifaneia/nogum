# -*- coding: utf-8 -*-
"""Torpe -1 y la Firma a +4, en el manual."""
import io, os, re, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
fal = []


def sub(f, a, b, n=1):
    s = io.open(f, encoding='utf-8').read()
    if s.count(a) != n:
        fal.append('%s (%d!=%d) %s' % (f, s.count(a), n, a[:58])); return
    io.open(f, 'w', encoding='utf-8').write(s.replace(a, b, n))


# ---------------------------------------------- 1. la Regla de la Nulidad
VIEJA_ES = """<p>En cuanto compras cualquier cosa dentro de ese ámbito, la nulidad desaparece en <strong>todo</strong> el ámbito: lo que no tengas comprado lo tiras con <strong>+0</strong>. No sabes de eso, pero sabes de cosas cercanas y al menos distingues lo que sería una tontería. <span class="src">T106</span></p>
</div>"""
NUEVA_ES = """<p>En cuanto compras cualquier cosa dentro de ese ámbito, la nulidad desaparece —pero no del todo—. Lo que caiga en <strong>tu columna</strong>, el Dominio que has tocado, lo tiras con <strong>+0</strong>: no sabes de eso, pero sabes de cosas cercanas y al menos distingues lo que sería una tontería. Lo que caiga en <strong>la otra columna del ámbito</strong> lo tiras con <strong>−1</strong>: estás <strong>torpe</strong>. <span class="src">T106</span> <span class="src">T131</span></p>
</div>
<p><strong>Torpe no es ignorante.</strong> Quien nunca ha intentado algo tira con +0: no sabe, pero tampoco estorba. Torpe es peor, y es peor por una razón concreta: <em>tienes el ámbito, pero con la mitad equivocada</em>. Eres puro Vigor y te toca una acrobacia. Eres pura Erudición y te toca leer una calle. No te falta el músculo ni la cabeza: te falta el pie, y por eso duele más que no saber nada.</p>
<p>Y por eso la ficha pesa. Cinco Ámbitos de dos Dominios son <strong>diez columnas</strong>, y con doce puntos no se cubren todas. <strong>Vas a estar torpe en algo, y esa es la decisión.</strong> Un personaje ancho casi nunca está torpe y casi nunca brilla; uno profundo brilla en lo suyo y se arrastra fuera de ello. Las dos fichas son legales y el juego no premia a ninguna: premia que en la mesa se sepa cuál ha hecho cada uno, y que se reparta el trabajo en consecuencia.</p>"""
sub('frag_ch3.html', VIEJA_ES, NUEVA_ES)

VIEJA_EN = """<p>The moment you buy anything inside that sphere, the nullity disappears across <strong>the whole</strong> sphere: whatever you have not bought you roll at <strong>+0</strong>. You know nothing about it, but you know about nearby things and you can at least tell what would be stupid. <span class="src">T106</span></p>
</div>"""
NUEVA_EN = """<p>The moment you buy anything inside that sphere, the nullity disappears —but not entirely—. Whatever falls in <strong>your column</strong>, the Domain you have touched, you roll at <strong>+0</strong>: you know nothing about it, but you know about nearby things and you can at least tell what would be stupid. Whatever falls in <strong>the sphere’s other column</strong> you roll at <strong>−1</strong>: you are <strong>clumsy</strong>. <span class="src">T106</span> <span class="src">T131</span></p>
</div>
<p><strong>Clumsy is not ignorant.</strong> Somebody who has never tried a thing rolls at +0: they do not know, but they do not get in the way either. Clumsy is worse, and it is worse for a specific reason: <em>you have the sphere, but with the wrong half of it</em>. You are pure Vigour and you are asked to tumble. You are pure Erudition and you are asked to read a street. You are not short of muscle or of brains: you are short of footing, and that hurts more than knowing nothing.</p>
<p>And that is why the sheet matters. Five Spheres of two Domains each make <strong>ten columns</strong>, and twelve points do not cover them all. <strong>You are going to be clumsy at something, and that is the decision.</strong> A broad character is almost never clumsy and almost never shines; a deep one shines at their own thing and drags everywhere else. Both sheets are legal and the game rewards neither: it rewards the table knowing which one each player made, and splitting the work accordingly.</p>"""
sub('frag_ch3.en.html', VIEJA_EN, NUEVA_EN)

# ------------------------------------------- 2. la Firma ya no tiene dos pasos
sub('frag_ch3.html', '¿Firma? Tiras a +3 o +4.', '¿Firma? Tiras a +4.')
sub('frag_ch3.en.html', 'Signature? You roll at +3 or +4.', 'Signature? You roll at +4.')
sub('frag_glosario.html', 'Da +3, o +4 si eres Gran Maestro.',
    'Da <strong>+4</strong>. No tiene escalones: una Firma es la cima de esa Disciplina o no es una Firma.')
sub('frag_glosario.en.html', 'Worth +3, or +4 for a Grand Master.',
    'Worth <strong>+4</strong>. It has no steps: a Signature is the top of that Discipline or it is not a Signature.')
sub('frag_ch3.html', 'los personajes vivirán en +3 y +4 en lo suyo',
    'los personajes vivirán en +2 y +4 en lo suyo')
sub('frag_ch3.en.html', 'the characters will live at +3 and +4 in their own field',
    'the characters will live at +2 and +4 in their own field')
# el acordeon
for f in ('frag_ch3.html', 'frag_math.html'):
    s = io.open(f, encoding='utf-8').read()
    io.open(f, 'w', encoding='utf-8').write(s.replace('Firmas de Gran Maestro', 'Firmas'))
for f in ('frag_ch3.en.html', 'frag_math.en.html'):
    s = io.open(f, encoding='utf-8').read()
    io.open(f, 'w', encoding='utf-8').write(s.replace('Grand Master Signatures', 'Signatures'))

# ------------------------------- 3. las tablas de probabilidad pierden el +3
for f in ('frag_math.html', 'frag_math.en.html'):
    s = io.open(f, encoding='utf-8').read()
    n = len(re.findall(r'<tr><td>\+3</td>.*?</tr>\n?', s))
    s = re.sub(r'<tr><td>\+3</td>.*?</tr>\n?', '', s)
    io.open(f, 'w', encoding='utf-8').write(s)
    print('  %-20s %d filas de +3 fuera de las tablas' % (f, n))

# --------------------------------------- 4. un resto del barrido de marcas
sub('frag_ch2.html', 'El pirata de goma (<em>One Piece</em>) es', 'El pirata de goma es')
sub('frag_ch2.en.html', 'The rubber pirate (<em>One Piece</em>) is', 'The rubber pirate is')

if fal:
    print('FALLOS:')
    for x in fal:
        print('  ' + x)
    sys.exit(1)
print('manual: Torpe, Firma a +4 y una marca menos')
