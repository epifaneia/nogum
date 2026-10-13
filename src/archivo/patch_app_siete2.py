# -*- coding: utf-8 -*-
"""Huecos en la rejilla de escena, ayuda y prompt de la IA."""
import io, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
p = 'app4_body.html'
s = io.open(p, encoding='utf-8').read()


def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:70], s.count(a))
    s = s.replace(a, b)


rep("""          var k = CELL[r[0] + '|' + c[0]], ks = k === 'T3' ? ['T3','T5'] : [k];
          h += '<div class="tcellwrap">' + ks.map(function(x){ return '<button type="button" class="tcell' + (cardKey() === x ? ' on' : '') + '" data-scene="' + x + '"><b>' + esc(pick(CARDS[x].n)) + '</b><small>' + esc(pick(CARDS[x].roll)) + '</small></button>'; }).join('') + '</div>';""",
    """          var k = CELL[r[0] + '|' + c[0]];
          if (!k) { var alt = HOLE[r[0] + '|' + c[0]] || []; h += '<div class="tcellwrap">' + alt.map(function(x){ return '<button type="button" class="tcell hole' + (cardKey() === x ? ' on' : '') + '" data-scene="' + x + '"><b>' + esc(t('Hueco','Gap')) + '</b><small>' + esc(t('usa ','use ') + pick(CARDS[x].n)) + '</small></button>'; }).join('') + '</div>'; return; }
          h += '<div class="tcellwrap"><button type="button" class="tcell' + (cardKey() === k ? ' on' : '') + '" data-scene="' + k + '"><b>' + esc(pick(CARDS[k].n)) + '</b><small>' + esc(pick(CARDS[k].roll)) + '</small></button></div>';""")

i = s.index("  flavor:['Dos formas de caos")
j = s.index("\n", i)
s = s[:i] + ("  hueco:['Dos casillas del cuadrante no tienen tarjeta propia: las de universo con postura y dado plano. "
             "Con un dado sin curva no hay forma de inclinar el tono sin mover la dificultad, y eso este juego no lo hace. "
             "Elige a qué vecina te arrimas.','Two cells of the quadrant have no card of their own: the ones with a universe "
             "that has a stance and a flat die. With a curveless die there is no way to tilt the tone without moving the "
             "difficulty, and this game does not do that. Choose which neighbour to lean on.'],") + s[j:]

rep("['edition','opt','caos','flavor','zoom'].forEach(function(k){ en(k); });",
    "['edition','opt','caos','zoom'].forEach(function(k){ en(k); });\n  if (s.hueco === 'prev' || s.hueco === 'caos') M.hueco = s.hueco;")

old = "    '- flavor (only if opt is neutro and caos is alto): coste (things work, at a price) | locura (extremes rule: disasters and miracles).\\n' +"
new = "    '- hueco (only when opt is alto or bajo and caos is medio: that cell has no card): prev (the world behaves) | caos (the world makes noise).\\n' +"
rep(old, new)

s = s.replace("flavor:M.flavor,", "hueco:M.hueco,")
io.open(p, 'w', encoding='utf-8').write(s)
print('ok ·', len(s.encode()) // 1024, 'KB')
