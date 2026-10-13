# -*- coding: utf-8 -*-
"""Genera el Glosario (una idea, un nombre) y renombra los términos acordados en todo el manual."""
import io, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# término: (nombre, qué es, con qué se confundía)
TERMS_ES = [
    ('Cuadrante', 'El mapa de tonos: tres filas (de qué lado está el universo) por tres columnas (cuánto se le nota), con siete tarjetas y dos huecos.',
     'Antes se llamaba «Malla Tonal», y la palabra malla nombraba otras tres cosas en este mismo libro.'),
    ('Tarjeta', 'Cada una de las siete configuraciones de reglas del Cuadrante. Solo hay una encima de la mesa a la vez.', ''),
    ('Banda', 'El rango de números naturales que da pifia o crítico. «Banda de pifia 1–2» quiere decir que un 1 o un 2 en el número que usas es pifia.',
     'No confundas las bandas con el reparto de resultados (fallo, éxito con coste, éxito limpio), que va sobre el total y no sobre el dado.'),
    ('Éxito con coste', 'Lo consigues y el DJ elige el precio: tiempo, recurso, posición o fuego amigo. Ocupa la dificultad objetivo y el punto justo por debajo.',
     'Es la herramienta que tomamos prestada de la familia PbtA, con agradecimiento.'),
    ('Ámbito', 'Cada uno de los cinco terrenos de la pirámide de habilidades: Físico, Mental, Social, Técnico y Arcano. No se compra y no da bono.',
     'En el borrador esta capa se llamaba «Malla».'),
    ('Dominio', 'El segundo escalón de la pirámide, dentro de un Ámbito. Da +1.', ''),
    ('Disciplina', 'El tercer escalón, dentro de un Dominio. Da +2.', ''),
    ('Firma', 'El cuarto escalón: la habilidad concreta que te define y que todo el mundo reconoce. Da +3, o +4 si eres Gran Maestro.', ''),
    ('Rejilla', 'La escala de poder: mide con qué juegas y a qué escala, no cómo de bueno eres. Un nivel de diferencia ya decide la escena.',
     'En el borrador se llamaba «Malla» en unos sitios y «Rejilla» en otros.'),
    ('[Rejilla]', 'La etiqueta de equipo que dice cómo se comporta un objeto frente a la escala de poder: Estándar, Llave (Nivel X) o Ignora todo.',
     'Antes era la etiqueta [Malla].'),
    ('Llave', 'Lo que te permite afectar a algo que está por encima de tu nivel de Rejilla: un arma, una debilidad, una ayuda, un nombre verdadero. Con Llave, tiras con normalidad.', ''),
    ('Estilo', 'El +2 fijo que tienen todas las fichas completas, fuera de la pirámide. Se usa contra enemigos por debajo de tu nivel: ganas seguro y la tirada dice cómo de bien quedas.', ''),
    ('Guardia', 'Con qué actitud entras a la acción: Violencia, Treta o Especialidad. Se declara antes de tirar iniciativa y queda marcada en la ficha; si la mesa no elige, vale la última marcada.',
     'En el borrador se llamaba «Disposición».'),
    ('Vida fractal', 'Los tres bloques de salud que se miran de cerca o de lejos: tres casillas (La Cáscara), nueve (La Carne) o veintisiete (El Núcleo). Las proporciones no cambian, solo el zoom.', ''),
    ('Baúl', 'Las reglas opcionales que se encienden para una campaña entera.',
     'No lo confundas con el Bazar del Multiverso, que es el catálogo de equipo.'),
    ('Decorado', 'Lo que tiene función y nivel pero no tiene ficha ni vida: la multitud, el dragón dormido, la tormenta.', ''),
]
TERMS_EN = [
    ('Quadrant', 'The tone map: three rows (which side the universe is on) by three columns (how much it shows), with seven cards and two gaps.',
     'It used to be called the “Tonal Grid”, and the word grid named three other things in this same book.'),
    ('Card', 'Each of the seven rule configurations on the Quadrant. Only one sits on the table at a time.', ''),
    ('Band', 'The range of natural numbers that gives a fumble or a critical. “Fumble band 1–2” means a 1 or a 2 on the number you use is a fumble.',
     'Do not confuse the bands with the split of results (failure, success at a cost, clean success), which works on the total and not on the die.'),
    ('Success at a cost', 'You get it and the GM picks the price: time, a resource, position or friendly fire. It takes the target number and the point just below it.',
     'This is the tool we borrow from the PbtA family, with thanks.'),
    ('Sphere', 'Each of the five grounds of the skill pyramid: Physical, Mental, Social, Technical and Arcane. It is not bought and gives no bonus.',
     'In the draft this layer was called the “Grid”.'),
    ('Domain', 'The second step of the pyramid, inside a Sphere. Worth +1.', ''),
    ('Discipline', 'The third step, inside a Domain. Worth +2.', ''),
    ('Signature', 'The fourth step: the specific skill that defines you and that everyone recognises. Worth +3, or +4 for a Grand Master.', ''),
    ('Power Grid', 'The scale of power: it measures what you play with and at what scale, not how good you are. One level of difference already settles the scene.',
     'The draft called it “Grid” in some places and “Power Grid” in others.'),
    ('[Grid]', 'The gear tag that says how an item behaves against the scale of power: Standard, Key (Level X) or Ignores everything.',
     'It used to be the [Mesh] tag.'),
    ('Key', 'What lets you affect something above your Power Grid level: a weapon, a weakness, some help, a true name. With a Key, you roll as normal.', ''),
    ('Style', 'The flat +2 every full sheet carries, outside the pyramid. It is used against foes below your level: you win for certain and the roll says how good you look.', ''),
    ('Guard', 'The attitude you enter the action with: Violence, Trick or Specialty. It is declared before rolling initiative and marked on the sheet; if the table does not choose, the last mark applies.',
     'The draft called it “Stance”.'),
    ('Fractal Health', 'The three blocks of health you can look at close up or far away: three boxes (The Shell), nine (The Flesh) or twenty-seven (The Core). The proportions never change, only the zoom.', ''),
    ('Chest', 'The optional rules you switch on for a whole campaign.',
     'Do not confuse it with the Multiverse Bazaar, which is the equipment catalogue.'),
    ('Set dressing', 'Whatever has a function and a level but no sheet and no health: the crowd, the sleeping dragon, the storm.', ''),
]


def frag(terms, es):
    t = lambda a, b: a if es else b
    h = ['<section class="chapter" id="apx-glosario">']
    h.append('<h2>%s</h2>' % t('Glosario · una idea, un nombre', 'Glossary · one idea, one name'))
    h.append('<p>%s</p>' % t(
        'Este manual ha pasado por una limpieza de vocabulario: cada idea tiene un nombre y solo uno. Si vienes de un borrador anterior, aquí están las equivalencias.',
        'This rulebook has been through a vocabulary clean-up: each idea has one name and only one. If you come from an earlier draft, the equivalences are here.'))
    h.append('<dl class="glosario">')
    for name, what, note in terms:
        h.append('<dt>%s</dt><dd>%s%s</dd>' % (name, what, (' <span class="note">%s</span>' % note) if note else ''))
    h.append('</dl>')
    h.append('<aside class="meta"><p>%s</p></aside>' % t(
        'La palabra que más trabajo dio fue «malla»: llegó a significar cuatro cosas a la vez —el mapa de tonos, la capa de ámbitos, la escala de poder y una etiqueta de equipo—. Ahora son Cuadrante, Ámbito, Rejilla y [Rejilla]. Si en algún rincón del libro se nos ha escapado una malla que no sea la de una cota, es una errata.',
        'The word that gave most trouble was “grid”: it came to mean four things at once —the tone map, the sphere layer, the scale of power and a gear tag. They are now Quadrant, Sphere, Power Grid and [Grid]. If a stray grid is still hiding somewhere in the book, and it is not chainmail, it is a typo.'))
    h.append('</section>')
    return '\n'.join(h) + '\n'


io.open('frag_glosario.html', 'w', encoding='utf-8').write(frag(TERMS_ES, True))
io.open('frag_glosario.en.html', 'w', encoding='utf-8').write(frag(TERMS_EN, False))

# ---- renombrados en el resto del manual
MISS = []


def patch(fn, pairs):
    s = io.open(fn, encoding='utf-8').read()
    for a, b in pairs:
        if a not in s:
            MISS.append((fn, a[:60]))
            continue
        s = s.replace(a, b)
    io.open(fn, 'w', encoding='utf-8').write(s)


patch('frag_ch1a.html', [('1.2 La Malla Tonal (el mapa de tu historia)', '1.2 El Cuadrante (el mapa de tu historia)'),
                         ('La malla no es un menú cerrado', 'El Cuadrante no es un menú cerrado')])
patch('frag_ch1a.en.html', [('1.2 The Tonal Grid (the map of your story)', '1.2 The Quadrant (the map of your story)')])
patch('frag_ch3.html', [('la <strong>Malla</strong> es el continente', 'el <strong>Ámbito</strong> es el continente'),
                        ('en un ámbito de la Malla', 'en un Ámbito'),
                        ('fuera de la Malla', 'fuera de la pirámide'),
                        ('El sistema completo: Malla, Dominios', 'El sistema completo: Ámbitos, Dominios')])
patch('frag_ch5.html', [('<strong>Disposición', '<strong>Guardia'), ('Disposición', 'Guardia')])
patch('frag_ch5.en.html', [('<strong>Stance', '<strong>Guard')])
patch('frag_cap8.html', [('Malla Especial/Técnica', 'Ámbito Arcano/Técnico'),
                         ('la «Malla de Sombra» no es la Malla Tonal ni la Rejilla', 'la «Malla de Sombra» del borrador no es el Cuadrante ni la Rejilla'),
                         ('malla mística inversa', 'rejilla mística inversa')])
patch('frag_cap8.en.html', [('Special/Technical Mesh', 'Arcane/Technical Sphere')])
print('glosario escrito · faltan:', MISS if MISS else 'nada')
