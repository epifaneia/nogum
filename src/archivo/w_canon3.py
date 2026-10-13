# -*- coding: utf-8 -*-
"""Canon y Cuaderno: el acordeon (ED-38), las Firmas, las tablas y el Arcano cerrado."""
import io, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

f = 'CANON.md'
s = io.open(f, encoding='utf-8').read()
old = '- Marcador de disposición (autor, 17 sep):'
new = """- **ED-38. El acordeon** (regla del autor, recuperada de la conversacion): la maestria se pliega hacia arriba. **3 Firmas de Gran Maestro en la misma Disciplina** la convierten entera en +4; **3 Disciplinas plegadas** pliegan el Dominio; **los 2 Dominios** pliegan el Ambito. No sube el techo (el Ancla sigue cortando en +4): lo ensancha, quitando huecos del mapa. Precios: 8 puntos una Disciplina (Dominio 1 + Disciplina 1 + 3 Firmas a 2), 22 un Dominio (8 + 7 + 7), 44 un Ambito (2x22). Con 12 puntos en creacion cabe una Disciplina plegada y poco mas. Es la escalera larga de los puntos, como la escalera cuadrada lo es de las Llaves: **las Llaves suben hacia fuera** (x100 de alcance por peldano) y **los puntos hacia dentro** (el +4 se ensancha). El 3 es el unico numero ajustable del acordeon.
- Arcano cerrado (decision del autor): Don = Proyeccion, Alteracion, Adivinacion, Proteccion. Ritual = Alquimia, Invocacion, Encantamiento, Vinculos. Es la lista que ya usaba la app.
- 8.2 trae el catalogo de **200 Firmas** (5 por Disciplina, bilingue), ordenado por Ambito y Disciplina; con eso se cierra la pregunta de como agrupar el catalogo. Y cap. 8 trae **seis tablas de problemas** por genero (heridas graves en dos sabores, enfermedad, locura con aviso de mesa, lo que se pierde con los tres nombres de la barra Espiritual, fallos de equipo y mutaciones), que son ejemplos y no un sistema.
- Marcador de disposición (autor, 17 sep):"""
assert old in s
s = s.replace(old, new)
io.open(f, 'w', encoding='utf-8').write(s)
print('canon ok')

f = 'frag_editorial.html'
s = io.open(f, encoding='utf-8').read()
ROWS = """<tr><td class="num"><span class="flag ed">ED-38</span></td><td><strong>El acordeón.</strong> Regla del autor que se había quedado perdida en la conversación y que resuelve el agujero más grande que le quedaba a la progresión: con el Ancla cortando en +4, los puntos solo compraban anchura y no tenían meta. Ahora tres Firmas de Gran Maestro pliegan la Disciplina entera, tres Disciplinas el Dominio y los dos Dominios el Ámbito, a 8, 22 y 44 puntos. No sube el techo: lo ensancha. Y deja los dos monederos con escaleras largas distintas y complementarias —las Llaves suben hacia fuera, los puntos hacia dentro—, que es la clase de simetría que este sistema llevaba pidiendo desde el capítulo 2.</td><td><a href="#ch3-firmas">3.3</a></td></tr>
<tr><td>Las 200 Firmas y las seis tablas</td><td>El catálogo de Firmas vivía solo en la app mientras el manual prometía mil y no traía ninguna: ahora el 8.2 lleva las doscientas, cinco por Disciplina y bilingües, ordenadas por Ámbito, con lo que se cierra también la vieja pregunta de cómo agruparlas. Y las cuatro tablas que las recetas invocaban sin que existieran son ahora seis, escritas como el autor las pidió: ejemplos de problemas separados por género, no un sistema. Las heridas vienen en dos sabores (de aventura y sucia), la de locura lleva su aviso de mesa por delante, y la barra Espiritual trae los tres nombres que usa según el género: Corrupción, Empatía y la Bestia.</td><td><a href="#ch8-tablas">8.1</a></td></tr>
"""
anchor = '<tr><td>El menú de la pifia</td>'
assert anchor in s
s = s.replace(anchor, ROWS + anchor)

CIERRES = [
 ('<li>Las cuatro Disciplinas de Ritual y cómo organizar el catálogo de Firmas.</li>',
  '<li>Las cuatro Disciplinas de Ritual y cómo organizar el catálogo de Firmas. <strong>Cerrado</strong>: '
  'Alquimia, Invocación, Encantamiento y Vínculos, por decisión del autor; y las doscientas Firmas van '
  'ordenadas por Ámbito y Disciplina en <a href="#ch8-skills">8.2</a>.</li>'),
]
for a, b in CIERRES:
    if a in s:
        s = s.replace(a, b)
    else:
        print('  aviso: no estaba', a[:40])
io.open(f, 'w', encoding='utf-8').write(s)
print('cuaderno ok')
