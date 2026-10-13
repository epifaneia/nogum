# -*- coding: utf-8 -*-
"""Color por capitulo (escalas por familia) y el hueco de figura para diagramas."""
import io, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
fal = []


def sub(f, a, b, n=1):
    s = io.open(f, encoding='utf-8').read()
    if s.count(a) != n:
        fal.append('%s (%d!=%d) %s' % (f, s.count(a), n, a[:56])); return
    io.open(f, 'w', encoding='utf-8').write(s.replace(a, b, n))


# ------------------------------------------------- 1. la hoja sabe de que capitulo es
sub('paper.js',
    """  function newSheet(kind){
    var s = document.createElement('article');
    s.className = 'sheet' + (kind ? ' ' + kind : '');""",
    """  function newSheet(kind){
    var s = document.createElement('article');
    s.className = 'sheet' + (kind ? ' ' + kind : '');
    /* el color de capitulo viaja con la hoja: lo pinta el CSS, no el JS */
    if (runCap) s.setAttribute('data-cap', runCap);""")
sub('paper.js', '  var cur, body, placed, running, stack, clones;',
    '  var cur, body, placed, running, stack, clones, runCap = \'\';')
sub('paper.js', "    stack = []; clones = []; running = '';",
    "    stack = []; clones = []; running = ''; runCap = '';")
sub('paper.js', "          running = ''; newSheet('cover');",
    "          running = ''; runCap = ''; newSheet('cover');")
sub('paper.js',
    """          var h2 = q.sec.querySelector(':scope > h2');
          running = h2 ? cleanTitle(h2) : running;""",
    """          var h2 = q.sec.querySelector(':scope > h2');
          running = h2 ? cleanTitle(h2) : running;
          if (q.sec.id) { runCap = q.sec.id; if (cur) cur.setAttribute('data-cap', runCap); }""")

# ------------------------------------------------------------- 2. las escalas
CSS = """
/* ===== color por capitulo =========================================
   Cuatro familias, una escala cada una. No es decoracion: es para saber
   donde estas al pasar paginas. Se usa en hilos finos (el filete de la
   cabecera, la linea del titulo, el numero de pagina y el indice lateral),
   nunca en el texto ni en fondos: el manual sigue siendo tinta sobre papel.
   Y nunca lleva tono: un color de referencia no cuenta una historia. */
.sheet{--cap:var(--ink-3)}
/* el motor: azules */
.sheet[data-cap="intro"]{--cap:#4b6ea8}
.sheet[data-cap="ch1"],.sheet[data-cap="ch1-panel"],.sheet[data-cap="ch1-maquinas"]{--cap:#2a56a0}
.sheet[data-cap="ch2"]{--cap:#1f6f8b}
/* la ficha: verdes */
.sheet[data-cap="ch3"]{--cap:#2e7d6b}
/* la mesa: ambares y rojos */
.sheet[data-cap="ch4"]{--cap:#9a6b16}
.sheet[data-cap="ch5"]{--cap:#a8502a}
.sheet[data-cap="ch6"]{--cap:#8d3c3c}
.sheet[data-cap="ch7"]{--cap:#7a3f6d}
/* los apendices: grises y violetas apagados */
.sheet[data-cap="ch8"],.sheet[data-cap="ch8b"]{--cap:#5c5470}
.sheet[data-cap="apx-bazar"],.sheet[data-cap="apx-bazar-b"]{--cap:#4a6a52}
.sheet[data-cap="apx-mates"]{--cap:#555f6e}
.sheet[data-cap="apx-glosario"]{--cap:#6b6257}
/* el cuaderno de edicion */
.sheet[data-cap="audit-editorial"]{--cap:#2a56a0}
.sheet[data-cap="audit-descartados"]{--cap:#a8502a}
.sheet[data-cap="audit-traza"]{--cap:#5c5470}
.rh{border-bottom-color:color-mix(in srgb,var(--cap) 55%,var(--rule))}
.rh span:last-child{color:var(--cap)}
.sb h2{border-bottom-color:var(--cap)}
.pn{color:var(--cap)}
@media print{.rh,.sb h2,.pn{-webkit-print-color-adjust:exact;print-color-adjust:exact}}

/* ===== el hueco de figura =========================================
   Para DIAGRAMAS: el sistema dibujandose a si mismo. Nunca para escenas ni
   personajes. Toda imagen lleva tono, y este manual no arrastra ninguno: el
   tono lo pone la mesa, no la portada. Un esquema no cuenta una historia.
   El hueco reserva su sitio aunque el dibujo no exista todavia, para que el
   dia que llegue no haya que remaquetar el libro entero. */
.fig{margin:6mm 0;border:.3mm solid var(--rule);border-radius:1.2mm;overflow:hidden;background:var(--ground);break-inside:avoid;page-break-inside:avoid}
.fig > .fig-box{width:100%;aspect-ratio:16/9;display:flex;align-items:center;justify-content:center}
.fig.alta > .fig-box{aspect-ratio:4/3}
.fig.cuadrada > .fig-box{aspect-ratio:1/1}
.fig.tira > .fig-box{aspect-ratio:3/1}
.fig > .fig-box > *{max-width:100%;max-height:100%}
.fig > .fig-box:empty::after{content:attr(data-nota);font:11px/1.4 var(--mono);color:var(--ink-3);padding:4mm;text-align:center}
.fig figcaption,.fig > .fig-pie{margin:0;padding:2mm 3mm;font:9pt/1.35 var(--mono);color:var(--ink-2);border-top:.3mm solid var(--rule);background:var(--paper)}
.fig figcaption b,.fig > .fig-pie b{color:var(--cap)}
"""
s = io.open('paper.css', encoding='utf-8').read()
if '--cap:' not in s:
    io.open('paper.css', 'w', encoding='utf-8').write(s.rstrip() + '\n' + CSS)
    print('paper.css: escalas de capitulo y hueco de figura')
else:
    print('paper.css: ya estaba')

if fal:
    print('FALLOS:')
    for x in fal:
        print('  ' + x)
    sys.exit(1)
print('color por capitulo enchufado')
