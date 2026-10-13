# -*- coding: utf-8 -*-
"""Inyecta las secciones de marcas y decisiones en taller.html. Idempotente."""
import io, os, re, json
os.chdir(os.path.dirname(os.path.abspath(__file__)))
R = lambda n: io.open(n, encoding='utf-8').read()
s = R('taller.html')

for a, b in [('<!--LISTAS-DATA-->', '<!--/LISTAS-DATA-->'), ('<!--LISTAS-SEC-->', '<!--/LISTAS-SEC-->'),
             ('/*LISTAS-JS*/', '/*/LISTAS-JS*/'), ('/*LISTAS-CSS*/', '/*/LISTAS-CSS*/'),
             ('<!--LISTAS-NAV-->', '<!--/LISTAS-NAV-->'), ('/*LISTAS-CALL*/', '/*/LISTAS-CALL*/'),
             ('/*LISTAS-ACTA*/', '/*/LISTAS-ACTA*/'), ('<!--LISTAS-COPY-->', '<!--/LISTAS-COPY-->')]:
    s = re.sub(re.escape(a) + '.*?' + re.escape(b), '', s, flags=re.S)


s = re.sub(r'/\*/SIETE-CALL\*/\s*renderActa\(\);', '/*/SIETE-CALL*/ renderActa();', s)

def rep(anchor, add, n=1):
    global s
    assert s.count(anchor) == n, (anchor[:60], s.count(anchor))
    s = s.replace(anchor, add, 1)


data = json.load(open('taller_listas.json', encoding='utf-8'))
js = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')

rep("<script>\n'use strict';",
    '<!--LISTAS-DATA--><script type="application/json" id="listasData">' + js + '</script><!--/LISTAS-DATA-->\n'
    "<script>\n'use strict';")

rep('<section id="acta">',
    '<!--LISTAS-SEC-->' + R('sec_listas.html').strip() + '<!--/LISTAS-SEC-->\n\n<section id="acta">')

rep('@media print{.top{display:none}',
    '/*LISTAS-CSS*/\n' + R('sec_listas.css').strip() + '\n/*/LISTAS-CSS*/\n@media print{.top{display:none}')

rep('/*/SIETE-CALL*/ renderActa();',
    '/*/SIETE-CALL*/\n/*LISTAS-JS*/\n' + R('sec_listas.js').strip() + '\n/*/LISTAS-JS*/\n'
    '/*LISTAS-CALL*/ renderMarcas(); renderRecetas(); renderPreg(); /*/LISTAS-CALL*/ renderActa();')

COPY = ('<!--LISTAS-COPY--><div class="actabar">'
        '<button type="button" class="mini" id="actaCopy">Copiar el acta</button>'
        '<span class="small" id="actaMsg"></span></div><!--/LISTAS-COPY-->')
rep('<textarea id="acta" readonly', COPY + '\n<textarea id="acta" readonly')

rep('<a href="#acta">Acta',
    '<!--LISTAS-NAV--><a href="#marcas">Marcas</a><a href="#banderas">Decisiones</a><!--/LISTAS-NAV-->'
    '<a href="#acta">Acta')

ACTA = (
    "/*LISTAS-ACTA*/\n"
    "  L.push('');\n"
    "  L.push('BARRIDO DE MARCAS');\n"
    "  var nm = 0, tm = 0;\n"
    "  LST.marcas.forEach(function(g){ g.items.forEach(function(it){ tm++;\n"
    "    if (S.marcas[it.id]) { L.push('  ' + it.n + ' -> ' + S.marcas[it.id]); nm++; }\n"
    "  }); });\n"
    "  L.push(nm ? '  (' + nm + ' de ' + tm + ')' : '  (sin elegir)');\n"
    "  L.push('');\n"
    "  L.push('DECISIONES PENDIENTES');\n"
    "  var nf = 0;\n"
    "  LST.preguntas.forEach(function(q){ if (S.preg[q.id]) { L.push('  ' + q.t + ': ' + S.preg[q.id]); nf++; } });\n"
    "  L.push(nf ? '  (' + nf + ' de ' + LST.preguntas.length + ')' : '  (sin contestar)');\n"
    "/*/LISTAS-ACTA*/\n"
)
rep("  $('acta').value = L.join('\\n');", ACTA + "  $('acta').value = L.join('\\n');")

io.open('taller.html', 'w', encoding='utf-8').write(s)
print('inyectado · KB', len(s.encode()) // 1024)
