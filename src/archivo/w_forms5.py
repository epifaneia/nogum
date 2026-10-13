# -*- coding: utf-8 -*-
"""Cinco opciones escritas o barra deslizante, y elegir ya no avanza solo."""
import io, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.getcwd())
from forms_js2 import BLOQUE_A

F = 'app4_body.html'
s = io.open(F, encoding='utf-8').read()
fal = []


def sub(a, b, n=1):
    global s
    if s.count(a) != n:
        fal.append('(%d!=%d) %s' % (s.count(a), n, a[:72])); return
    s = s.replace(a, b, n)


# ------------------------------------- 1. las tablas de preguntas, de nuevo
i = s.index("var SECTIONS = [['Universo','Universe']")
j = s.index("/* ======================= UI STRINGS ======================= */")
s = s[:i] + BLOQUE_A + "\n" + s[j:]

# ------------------------------------------------- 2. el renderizador nuevo
sub(r"""function escala(q, cur){
  var h = '<p class="vign">' + esc(pick(q.v)) + '</p><div class="escala">';
  h += '<p class="polo">' + esc(pick(q.a)) + '</p><div class="pasos">';
  for (var n = 1; n <= 5; n++) h += '<button type="button" class="paso p' + n + (cur === n ? ' on' : '') +
    '" data-sc="' + n + '" aria-pressed="' + (cur === n) + '" aria-label="' + n + ' / 5"><i></i></button>';
  h += '</div><p class="polo b">' + esc(pick(q.b)) + '</p></div>';
  return h;
}""",
r"""function escala(q, cur){
  var h = '<p class="vign">' + esc(pick(q.v)) + '</p>';
  if (q.ac) {
    /* de acuerdo o en desacuerdo: una barra que se desliza */
    h += '<div class="desliza"><div class="despolos"><span>' + esc(pick(ACN[0])) + '</span><span>' + esc(pick(ACN[4])) + '</span></div>' +
      '<input type="range" min="1" max="5" step="1" value="' + (cur || 3) + '" data-scr="1"' + (cur ? '' : ' class="sin"') +
      ' aria-label="' + esc(pick(q.v).slice(0, 80)) + '" aria-valuetext="' + esc(cur ? pick(ACN[cur - 1]) : t('sin contestar','not answered')) + '">' +
      '<p class="desval' + (cur ? '' : ' sin') + '">' + esc(cur ? pick(ACN[cur - 1])
        : t('Sin contestar: arrastra el tirador, o toca el punto de la barra que quieras.','Not answered: drag the handle, or tap wherever on the bar you mean.')) + '</p></div>';
    return h;
  }
  h += '<div class="choices">';
  q.o.forEach(function(op, n){
    h += '<button type="button" class="choice" data-sc="' + (n + 1) + '" aria-pressed="' + (cur === n + 1) + '"><span>' +
      esc(pick(op)) + '</span><span class="mark"></span></button>';
  });
  return h + '</div>';
}""")

# ---------------------------------------- 3. elegir ya no avanza: hay que pulsar
sub("""  v.querySelectorAll('[data-sc]').forEach(function(b){ b.addEventListener('click', function(){
    var n = +b.getAttribute('data-sc');
    if (p.t === 'q') setAns(fid, p.s.id, p.i, n); else { S.q[fid] = S.q[fid] || {}; S.q[fid][p.g] = [n]; }
    aplica(fid); persist(); render(true);
    setTimeout(function(){ if (S.form === fid) avanza(); }, 300);
  }); });""",
"""  function marca(n){
    if (p.t === 'q') setAns(fid, p.s.id, p.i, n); else { S.q[fid] = S.q[fid] || {}; S.q[fid][p.g] = [n]; }
    aplica(fid); persist(); render(true);
  }
  v.querySelectorAll('[data-sc]').forEach(function(b){ b.addEventListener('click', function(){ marca(+b.getAttribute('data-sc')); }); });
  v.querySelectorAll('[data-scr]').forEach(function(r){
    r.addEventListener('input', function(){ marca(Math.max(1, Math.min(5, +r.value || 3))); });
  });""")
sub("""  v.querySelectorAll('[data-pk]').forEach(function(b){ b.addEventListener('click', function(){
    var x = b.getAttribute('data-pk').split('|');
    if (x[0] === 'known') { M.known = x[1] === '1'; M.family = null; M.world = null; M.unis = null; if (!M.known) aplicaUni(); }
    else if (x[0] === 'family') { M.family = x[1]; M.world = null; }
    else { applyPreset(+x[1]); S.q.tono = {}; S.q.baul = {}; S.st.tono = 0; S.st.baul = 0; S.ia = {}; }
    persist(); render(true);
    setTimeout(function(){ if (S.form === fid) avanza(); }, 300);
  }); });""",
"""  v.querySelectorAll('[data-pk]').forEach(function(b){ b.addEventListener('click', function(){
    var x = b.getAttribute('data-pk').split('|');
    if (x[0] === 'known') { M.known = x[1] === '1'; M.family = null; M.world = null; M.unis = null; if (!M.known) aplicaUni(); }
    else if (x[0] === 'family') { M.family = x[1]; M.world = null; }
    else { applyPreset(+x[1]); S.q.tono = {}; S.q.baul = {}; S.st.tono = 0; S.st.baul = 0; S.ia = {}; }
    persist(); render(true);
  }); });""")

# el aviso de que hay que pulsar siguiente, una sola vez por formulario
sub("""    h += escala(p.s.qs[p.i], ans(fid, p.s.id)[p.i] || 0);""",
    """    h += escala(p.s.qs[p.i], ans(fid, p.s.id)[p.i] || 0);
    if (i === 0) h += '<p class="eqnote">' + esc(t('Elige, y cuando lo tengas pulsa «Siguiente». Nada se guarda hasta el final y puedes volver atrás.','Pick one, and press “Next” when you are happy. Nothing is final and you can always go back.')) + '</p>';""")

# ------------------------------------------------------- 4. el aspecto nuevo
VIEJO_CSS = """/* escalas de 1 a 5 */
.vign{font:600 clamp(19px,2.6vw,25px)/1.4 var(--serif);margin:0 0 22px;text-wrap:balance}
.escala{display:grid;gap:9px}
.polo{margin:0;font:13.5px/1.45 var(--mono);color:var(--ink-2);padding:9px 12px;border:1px solid var(--rule);border-radius:9px;background:var(--ground)}
.pasos{display:flex;gap:7px;align-items:center}
.paso{flex:1 1 0;display:flex;align-items:center;justify-content:center;height:54px;border:2px solid var(--rule);border-radius:10px;background:var(--paper)}
.paso i{display:block;border-radius:50%;background:var(--ink-3)}
.paso.p1 i,.paso.p5 i{width:20px;height:20px}
.paso.p2 i,.paso.p4 i{width:14px;height:14px}
.paso.p3 i{width:8px;height:8px}
.paso:hover{border-color:var(--ink-3)}
.paso.on{border-color:var(--red);background:var(--red)}
.paso.on i{background:#fff}"""
NUEVO_CSS = """/* la vineta y la barra de acuerdo */
.vign{font:600 clamp(19px,2.6vw,25px)/1.4 var(--serif);margin:0 0 22px;text-wrap:balance}
.desliza{border:1px solid var(--rule);border-radius:12px;padding:14px 16px 10px;background:var(--ground)}
.despolos{display:flex;justify-content:space-between;gap:12px;font:600 11.5px/1.3 var(--mono);text-transform:uppercase;letter-spacing:.04em;color:var(--ink-3);margin-bottom:10px}
.despolos span:last-child{text-align:right}
.desliza input[type=range]{-webkit-appearance:none;appearance:none;width:100%;height:30px;background:transparent;margin:0;display:block}
.desliza input[type=range]:focus{outline:2px solid var(--blue);outline-offset:3px}
.desliza input[type=range]::-webkit-slider-runnable-track{height:8px;border-radius:999px;background:linear-gradient(90deg,var(--rule),var(--ink-3),var(--rule))}
.desliza input[type=range]::-moz-range-track{height:8px;border-radius:999px;background:linear-gradient(90deg,var(--rule),var(--ink-3),var(--rule))}
.desliza input[type=range]::-webkit-slider-thumb{-webkit-appearance:none;appearance:none;width:28px;height:28px;margin-top:-10px;border-radius:50%;background:var(--red);border:3px solid var(--paper);box-shadow:0 1px 4px rgba(0,0,0,.35)}
.desliza input[type=range]::-moz-range-thumb{width:28px;height:28px;border-radius:50%;background:var(--red);border:3px solid var(--paper);box-shadow:0 1px 4px rgba(0,0,0,.35)}
.desliza input[type=range].sin::-webkit-slider-thumb{background:var(--ink-3)}
.desliza input[type=range].sin::-moz-range-thumb{background:var(--ink-3)}
.desval{margin:8px 0 0;text-align:center;font:600 17px/1.3 var(--serif);color:var(--ink)}
.desval.sin{font:12.5px/1.5 var(--mono);color:var(--ink-3);font-weight:400}"""
sub(VIEJO_CSS, NUEVO_CSS)

if fal:
    print('FALLOS:')
    for f in fal:
        print('  ' + f)
    sys.exit(1)
io.open(F, 'w', encoding='utf-8').write(s)
print('cinco opciones escritas, barra para el acuerdo, y elegir no avanza')
