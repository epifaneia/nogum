# -*- coding: utf-8 -*-
"""«Dalo por bueno»: las banderas que el acta aprueba, retiradas una a una."""
import io, os, re
os.chdir(os.path.dirname(os.path.abspath(__file__)))

OK_ES = '<span class="src">Aprobado por el autor</span>'
OK_EN = '<span class="src">Approved by the author</span>'

# (fichero, marca que precede a la bandera, sustituto)
TRABAJO = [
 ('frag_cap8.html', 'Gana quien complete antes su reloj', OK_ES),
 ('frag_cap8.html', 'los héroes llevan bocadillos', OK_ES),
 ('frag_cap8.html', 'El jugador puede rechazar el pacto', OK_ES),
 ('frag_cap8.html', 'las etiquetas del arma y del defensor', OK_ES),
 ('frag_cap8.html', 'más cerca estás de quedar fuera de juego', OK_ES),
 ('frag_cap8.html', 'al servicio del destino', OK_ES),
 ('frag_cap8.html', '2 por runa mayor', OK_ES),
 ('frag_cap8.html', 'Daño Espiritual 1</span> al lanzador', OK_ES),
 ('frag_cap8.html', 'la configuración que más se le parece', OK_ES),
 ('frag_acelerado.html', 'no la redacción de las demás', OK_ES),
 ('frag_acelerado.html', 'Las demás son propias de este manual', OK_ES),
 ('frag_acelerado.html', 'Cada uno usa además su bote aparte', OK_ES),
 ('frag_cap8.en.html', 'Whoever completes their clock first wins', OK_EN),
 ('frag_cap8.en.html', 'the heroes have sandwiches', OK_EN),
 ('frag_cap8.en.html', 'The player may refuse the bargain', OK_EN),
 ('frag_cap8.en.html', 'the attacker’s and defender’s tags', OK_EN),
 ('frag_cap8.en.html', 'the closer you are to being out of the game', OK_EN),
 ('frag_cap8.en.html', 'in the service of destiny', OK_EN),
 ('frag_cap8.en.html', '2 for a major one', OK_EN),
 ('frag_cap8.en.html', 'Spiritual Dmg 1</span> to the caster', OK_EN),
 ('frag_cap8.en.html', 'the configuration that comes closest', OK_EN),
 ('frag_acelerado.en.html', 'not the wording of the rest', OK_EN),
 ('frag_acelerado.en.html', 'The rest are this rulebook’s own', OK_EN),
 ('frag_acelerado.en.html', 'Each also uses their separate pot', OK_EN),
]

FLAG = re.compile(r'\s*<span class="flag (?:pending|proposal)">[^<]*</span>')
hechos, fallos = 0, []
porfile = {}
for f, marca, rep in TRABAJO:
    porfile.setdefault(f, []).append((marca, rep))

for f, items in porfile.items():
    if not os.path.exists(f):
        fallos.append(f + ' (no existe)'); continue
    s = io.open(f, encoding='utf-8').read()
    for marca, rep in items:
        i = s.find(marca)
        if i < 0:
            fallos.append('%s :: %s' % (f, marca[:40])); continue
        m = FLAG.search(s, i)
        if not m or m.start() - (i + len(marca)) > 120:
            fallos.append('%s :: sin bandera cerca de %s' % (f, marca[:40])); continue
        s = s[:m.start()] + ' ' + rep + s[m.end():]
        hechos += 1
    io.open(f, 'w', encoding='utf-8').write(s)

print('banderas retiradas:', hechos)
for x in fallos:
    print('  NO:', x)

# el catalogo de Firmas ya existe: se cierra la pregunta de como agruparlo
CAT = [
 ('frag_cap8.html',
  ('El autor quiere un catálogo masivo, de unas <strong>1.000 Firmas</strong> (5 categorías × 5 Firmas × 40 Disciplinas), organizado en categorías que se solapen lo menos posible y dejen claro al jugador dónde mirar.',
   'El catálogo está <strong>hecho y ordenado por Disciplina</strong>: doscientas Firmas, cinco por cada una, aquí mismo. Esa es la categorización, y es la que se usa en mesa: miras tu rama y eliges. El autor hablaba de llegar a unas mil (cinco categorías por Disciplina); con las doscientas escritas, ampliar es sumar filas, no rediseñar nada.')),
]
for f, (a, b) in CAT:
    s = io.open(f, encoding='utf-8').read()
    print('catalogo:', s.count(a))
    s = s.replace(a, b)
    io.open(f, 'w', encoding='utf-8').write(s)
