# -*- coding: utf-8 -*-
"""Las 200 Firmas pasan de la app al manual (8.2), ordenadas por Ambito y Disciplina."""
import io, os, re, json
os.chdir(os.path.dirname(os.path.abspath(__file__)))

F = json.load(io.open('firmas.json', encoding='utf-8'))

# la piramide, leida del propio cuerpo de la app para no inventarse el orden
src = io.open('app4_body.html', encoding='utf-8').read()
blk = src[src.index('var AMB = ['):src.index('\nvar ', src.index('var AMB = [') + 10)]
AMB = []
for am in re.finditer(r"\{id:'(\w+)', n:\['([^']+)','([^']+)'\], doms:\[(.*?)\]\}\]\}", blk, re.S):
    pass
# mas simple: se saca a mano con expresiones sueltas
amb_names = re.findall(r"\{id:'(\w+)', n:\['([^']+)','([^']+)'\]", blk)
dom_names = re.findall(r"\{n:\['([^']+)','([^']+)'\], dis:", blk)
dis_names = re.findall(r"\['([^']+)','([^']+)'\]\]\}|\['([^']+)','([^']+)'\],", blk)
# las disciplinas, en orden, de cada bloque dis:[...]
dis_groups = []
for m in re.finditer(r"dis:\[(.*?)\]\}", blk, re.S):
    dis_groups.append(re.findall(r"\['([^']+)','([^']+)'\]", m.group(1)))
assert len(amb_names) == 5 and len(dom_names) == 10 and len(dis_groups) == 10, (len(amb_names), len(dom_names), len(dis_groups))

flat = []   # (ambES, ambEN, domES, domEN, disES, disEN)
for ai in range(5):
    for di in range(2):
        gi = ai * 2 + di
        for d in dis_groups[gi]:
            flat.append((amb_names[ai][1], amb_names[ai][2], dom_names[gi][0], dom_names[gi][1], d[0], d[1]))
assert len(flat) == 40, len(flat)

by_dis = {}
for e in F:
    by_dis[e['dis'][0].lower()] = e
missing = [f[4] for f in flat if f[4].lower() not in by_dis]
print('disciplinas sin firmas:', missing)


def build(es):
    L = 0 if es else 1
    h = ['<h4>%s</h4>\n' % (u'Las 200 Firmas' if es else 'The 200 Signatures')]
    h.append('<p>%s</p>\n' % (
        u'Cinco Firmas por Disciplina, para que nadie tenga que inventarse una desde cero en la sesión cero. '
        u'<strong>No es una lista cerrada:</strong> la Firma es tuya y puedes escribir la que quieras, siempre '
        u'que puedas explicar exactamente qué estás haciendo. Estas están aquí porque mirar cinco ejemplos de '
        u'tu rama es más rápido que mirar un folio en blanco, y porque enseñan el tamaño correcto: '
        u'<em>Armas de fuego</em>, no <em>francotirador</em>.'
        if es else
        u'Five Signatures per Discipline, so that nobody has to invent one from scratch in session zero. '
        u'<strong>It is not a closed list:</strong> the Signature is yours and you can write whatever you want, '
        u'as long as you can explain exactly what you are doing. These are here because looking at five examples '
        u'from your own branch is quicker than looking at a blank page, and because they teach the right size: '
        u'<em>Firearms</em>, not <em>sniper</em>.'))
    cur_amb = None
    for ambES, ambEN, domES, domEN, disES, disEN in flat:
        amb = ambES if es else ambEN
        if amb != cur_amb:
            if cur_amb is not None:
                h.append('</tbody></table></div>\n')
            cur_amb = amb
            h.append('<h4>%s</h4>\n' % amb)
            h.append('<div class="tw"><table class="t idx">\n<thead><tr><th>%s</th><th>%s</th><th>%s</th></tr></thead>\n<tbody>\n'
                     % ((u'Disciplina', u'Firma', u'Qué cubre') if es else ('Discipline', 'Signature', 'What it covers')))
        e = by_dis.get(disES.lower())
        if not e:
            continue
        items = e['items']
        for k, it in enumerate(items):
            h.append('<tr><td class="small">%s</td><td><strong>%s</strong></td><td class="small">%s</td></tr>\n'
                     % ((('<em>%s</em> · %s' % (domES if es else domEN, disES if es else disEN)) if k == 0 else ''),
                        it['n'][L], it['d'][L]))
    h.append('</tbody></table></div>\n')
    return ''.join(h)


for f, es in (('frag_cap8.html', True), ('frag_cap8.en.html', False)):
    s = io.open(f, encoding='utf-8').read()
    anchor = '<h3 id="ch8-recetas"'
    k = s.index(anchor)
    # se corta justo antes del cierre de seccion que precede a las recetas
    cut = s.rfind('</section>', 0, k)
    pos = cut if cut > 0 and cut > s.index('id="ch8-skills"') else k
    s = s[:pos] + build(es) + s[pos:]
    io.open(f, 'w', encoding='utf-8').write(s)
    print(' ', f, 'ok')
print('firmas totales:', sum(len(e['items']) for e in F))
