# -*- coding: utf-8 -*-
"""Arreglos de la revision: enlace roto, bitacora fuera del asistente, codigo muerto."""
import io, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
fal = []


def sub(f, a, b, n=1):
    s = io.open(f, encoding='utf-8').read()
    if s.count(a) != n:
        fal.append('%s (%d!=%d) %s' % (f, s.count(a), n, a[:60])); return
    io.open(f, 'w', encoding='utf-8').write(s.replace(a, b, n))


# ------------------------------------------------- 1. el enlace que no existia
# «ch1-cuadrante» me lo invente: el ancla de los dos ejes es ch1-ejes
sub('frag_editorial.html', '<td><a href="#ch1-cuadrante">1.1</a></td>', '<td><a href="#ch1-ejes">1.1</a></td>')

# ------------------------------- 2. la bitacora no es canon para el asistente
c = io.open('CANON.md', encoding='utf-8').read()
MARCA = '<!-- BITACORA: de aqui para abajo es el diario de trabajo, no reglas. -->\n'
if MARCA not in c:
    anc = '## 11. Añadidos posteriores'
    if c.count(anc) != 1:
        fal.append('CANON.md: no encuentro la seccion 11 (%d)' % c.count(anc))
    else:
        c = c.replace(anc, MARCA + '\n' + anc, 1)
        io.open('CANON.md', 'w', encoding='utf-8').write(c)
        print('CANON.md: marcada la frontera de la bitacora')

sub('app4_body.html',
    "var CANON = JSON.parse(document.getElementById('canon').textContent);",
    "var CANON_TODO = JSON.parse(document.getElementById('canon').textContent);\n"
    "/* El asistente de reglas solo lee el canon, no el diario de trabajo: si no,\n"
    "   a quien pregunta por el acordeon le puede contestar con un arreglo de un\n"
    "   script. El diario sigue entero en el fichero, detras de la marca. */\n"
    "var CANON = CANON_TODO.split('<!-- BITACORA')[0];")

# ------------------------------------------------------- 3. codigo que sobra
s = io.open('app4_body.html', encoding='utf-8').read()
for linea in ("var UNIVERSES = DATA.bazar.map(function(b){ return b.id; });\n",
              "function isHole(){ return !isAcc() && CELL[opt() + '|' + caos()] === null; }\n"):
    if s.count(linea) == 1:
        s = s.replace(linea, '')
        print('fuera: %s' % linea.strip()[:52])
    else:
        fal.append('no encuentro para borrar: %s' % linea.strip()[:52])
io.open('app4_body.html', 'w', encoding='utf-8').write(s)

if fal:
    print('FALLOS:')
    for x in fal:
        print('  ' + x)
    sys.exit(1)
print('arreglos de la revision aplicados')
