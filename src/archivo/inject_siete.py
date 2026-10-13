# -*- coding: utf-8 -*-
"""Inyecta la sección «Las siete» (datos calculados por siete.py) en taller.html. Idempotente."""
import io, json, os, re

os.chdir(os.path.dirname(os.path.abspath(__file__)))
R = lambda n: io.open(n, encoding='utf-8').read()
s = R('taller.html')

# limpiar inyección previa
for a, b in [('<!--SIETE-DATA-->', '<!--/SIETE-DATA-->'), ('<!--SIETE-SEC-->', '<!--/SIETE-SEC-->'),
             ('/*SIETE-JS*/', '/*/SIETE-JS*/'), ('/*SIETE-CSS*/', '/*/SIETE-CSS*/'),
             ('<!--SIETE-NAV-->', '<!--/SIETE-NAV-->'), ('/*SIETE-CALL*/', '/*/SIETE-CALL*/')]:
    s = re.sub(re.escape(a) + '.*?' + re.escape(b), '', s, flags=re.S)


def rep(anchor, add, n=1):
    global s
    assert s.count(anchor) == n, (anchor[:60], s.count(anchor))
    s = s.replace(anchor, add)


data = json.load(open('siete.json', encoding='utf-8'))
js = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')

# 1. datos
rep('<script>\n\'use strict\';',
    '<!--SIETE-DATA--><script type="application/json" id="sieteData">' + js + '</script><!--/SIETE-DATA-->\n<script>\n\'use strict\';')
# 2. sección, antes del laboratorio
rep('<section id="lab">', '<!--SIETE-SEC-->' + R('sec_siete.html').strip() + '<!--/SIETE-SEC-->\n\n<section id="lab">')
# 3. css
rep('/* scene-free */\n' if '/* scene-free */' in s else '@media print{.top{display:none}',
    '/*SIETE-CSS*/\n' + R('sec_siete.css').strip() + '\n/*/SIETE-CSS*/\n@media print{.top{display:none}')
# 4. js (antes de la llamada final de render)
rep('renderDos(); renderMap(); renderLab(); renderProp(); renderTerms(); renderActa();',
    '/*SIETE-JS*/\n' + R('sec_siete.js').strip() + '\n/*/SIETE-JS*/\n'
    'renderDos(); renderMap(); renderLab(); renderProp(); renderTerms();'
    '/*SIETE-CALL*/ renderQuad(); renderSpectrum(); renderSieteCards(); renderVars(); /*/SIETE-CALL*/'
    ' renderActa();')
# 5. nav + estado de las variantes
rep('<a href="#lab">Laboratorio</a>', '<!--SIETE-NAV--><a href="#siete">Las siete</a><!--/SIETE-NAV--><a href="#lab">Laboratorio</a>')
if 'terms:{}, verdicts:{}' in s and 'vars:{}' not in s:
    s = s.replace('terms:{}, verdicts:{}', 'terms:{}, verdicts:{}, vars:{}')
if "L.push('NOMBRES ELEGIDOS');" in s and 'VARIANTES' not in s:
    s = s.replace("L.push('NOMBRES ELEGIDOS');",
                  "L.push('DECISIONES DE LAS SIETE');\n"
                  "  Object.keys(VARS7).forEach(function(k){ L.push('  ' + VARS7[k].t + ': ' + VARS7[k].q); });\n"
                  "  L.push('');\n  L.push('NOMBRES ELEGIDOS');")

io.open('taller.html', 'w', encoding='utf-8').write(s)
print('inyectado · KB', len(s.encode()) // 1024)
