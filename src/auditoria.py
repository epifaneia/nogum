# -*- coding: utf-8 -*-
"""Que queda: banderas vivas, promesas sin cumplir y contradicciones a la vista."""
import io, os, re, glob
os.chdir(os.path.dirname(os.path.abspath(__file__)))

LIVE = ['frag_intro', 'frag_ch1a', 'frag_ch1b', 'frag_ch2', 'frag_ch3', 'frag_ch4', 'frag_ch5',
        'frag_ch67', 'frag_cap8', 'frag_bazar', 'frag_math', 'frag_acelerado', 'frag_glosario']
out = []

out.append('=' * 70 + '\n BANDERAS VIVAS (solo castellano)\n' + '=' * 70)
tot = 0
for n in LIVE:
    f = n + '.html'
    if not os.path.exists(f):
        continue
    s = io.open(f, encoding='utf-8').read()
    for m in re.finditer(r'<span class="flag (pending|proposal)">[^<]*</span>', s):
        a = max(0, m.start() - 230)
        ctx = re.sub(r'<[^>]+>', ' ', s[a:m.start()])
        ctx = re.sub(r'\s+', ' ', ctx).strip()[-180:]
        tot += 1
        out.append('[%s] %s :: ...%s' % (m.group(1)[:4].upper(), n.replace('frag_', ''), ctx))
out.append('TOTAL: %d' % tot)

out.append('\n' + '=' * 70 + '\n PROMESAS SIN CUMPLIR (por escribir / pendiente de / falta)\n' + '=' * 70)
PAT = re.compile(r'(está por escribir|por escribir|sin escribir|pendiente de|falta decidir|'
                 r'queda por|hay que decidir|aplazado|aún no|todavía no)', re.I)
for n in LIVE:
    f = n + '.html'
    if not os.path.exists(f):
        continue
    s = re.sub(r'<[^>]+>', ' ', io.open(f, encoding='utf-8').read())
    s = re.sub(r'\s+', ' ', s)
    for m in PAT.finditer(s):
        out.append('%-12s ...%s...' % (n.replace('frag_', ''), s[max(0, m.start() - 110):m.end() + 110].strip()))

out.append('\n' + '=' * 70 + '\n LO QUE EL CUADERNO DECLARA ABIERTO\n' + '=' * 70)
s = io.open('frag_editorial.html', encoding='utf-8').read()
i = s.index('id="ed-abiertas"')
seg = s[i:s.index('</ul>', i)]
for li in re.findall(r'<li>(.*?)</li>', seg, re.S):
    out.append(' - ' + re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', li)).strip())

io.open('auditoria.txt', 'w', encoding='utf-8').write('\n'.join(out))
print('escrito, lineas:', len(out))
