# -*- coding: utf-8 -*-
"""Cuatro formularios modulares de escalas. Sustituye el asistente viejo."""
import io, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.getcwd())
from forms_js import BLOQUE_A
from forms_js_b import BLOQUE_B

F = 'app4_body.html'
s = io.open(F, encoding='utf-8').read()
fallos = []


def corta(ini, fin, nuevo, inc_fin=False):
    """Sustituye lo que hay entre dos anclas."""
    global s
    if s.count(ini) != 1 or s.count(fin) != 1:
        fallos.append('anclas: %r=%d  %r=%d' % (ini[:40], s.count(ini), fin[:40], s.count(fin)))
        return
    a = s.index(ini)
    b = s.index(fin) + (len(fin) if inc_fin else 0)
    if b <= a:
        fallos.append('orden invertido: %r' % ini[:40]); return
    s = s[:a] + nuevo + s[b:]


def sub(a, b, n=1):
    global s
    if s.count(a) != n:
        fallos.append('(%d!=%d) %s' % (s.count(a), n, a[:64])); return
    s = s.replace(a, b, n)


# ------------------------------------------------------------------- 1. CSS
CSS = """.eqnote{font-size:13px;line-height:1.45;color:var(--ink-2);margin:10px 0 0}
/* escalas de 1 a 5 */
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
.paso.on i{background:#fff}
/* el repartidor */
.hubedi{display:flex;align-items:center;gap:8px;flex-wrap:wrap;border:1px solid var(--rule);border-radius:10px;padding:9px 12px;margin:12px 0}
.hubedi>span:first-child{font:600 11px/1 var(--mono);text-transform:uppercase;letter-spacing:.06em;color:var(--ink-3)}
.hubedi .note{font:11.5px/1.4 var(--mono);color:var(--ink-3);flex:1 1 200px}
.hubedi .tool.on{border-color:var(--red);background:var(--red);color:#fff}
.summary .chg{width:1%;white-space:nowrap}
/* la lectura del modelo */
.aiask{margin-top:16px;padding-top:12px;border-top:1px dashed var(--rule);display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.aiask .note{font:11.5px/1.4 var(--mono);color:var(--ink-3);flex:1 1 220px}
.iabox{margin-top:10px;border-left:3px solid var(--red);padding:6px 0 6px 12px;font-size:15.5px;line-height:1.55;white-space:pre-wrap}"""
sub('.eqnote{font-size:13px;line-height:1.45;color:var(--ink-2);margin:10px 0 0}', CSS)

# ------------------------------------------------- 2. tablas y motor de escalas
corta("var SECTIONS = [['Universo','Universe']",
      "/* ======================= UI STRINGS ======================= */",
      BLOQUE_A + "\n")

# ---------------------------------------- 3. el repartidor y el renderizador
DISPATCH = r"""
/* ======================= REPARTO ======================= */
function esPaso(f){ return f === 'tono' || f === 'uni' || f === 'baul'; }
function renderForm(){
  if (S.form === 'equipo') return renderEq();
  if (esPaso(S.form)) {
    if (S.talk.on) return '<div class="wiz"><div class="ftop"><button type="button" class="mini" data-fsal="1">← ' +
      esc(t('Los formularios','The forms')) + '</button></div>' + renderTalk() + '</div>';
    return renderPasos(S.form);
  }
  return renderHub();
}
function bindForm(){
  if (S.form === 'equipo') return bindEq();
  if (esPaso(S.form)) return bindPasos(S.form);
  return bindHub();
}
function bindHub(){
  var v = $('view');
  v.querySelectorAll('[data-hub]').forEach(function(b){ b.addEventListener('click', function(){
    var k = b.getAttribute('data-hub');
    S.form = k;
    if (k === 'equipo') S.eq = {who:null, step:0, fstep:0, cat:null, sel:[]};
    persist(); render(); window.scrollTo(0, 0);
  }); });
  v.querySelectorAll('[data-edi]').forEach(function(b){ b.addEventListener('click', function(){
    M.edition = b.getAttribute('data-edi'); S.scene = null; persist(); render(true);
  }); });
  v.querySelectorAll('[data-gotpl]').forEach(function(b){ b.addEventListener('click', function(){
    S.tab = 'tpl'; S.form = null; persist(); render(); window.scrollTo(0, 0);
  }); });
}

"""
corta("/* ======================= FORM ======================= */",
      "/* ======================= LOS TRES FORMULARIOS ======================= */",
      BLOQUE_B + DISPATCH)

# ------------------------------------- 4. fuera el hub y el contexto viejos
corta("function hubCard(id, kick, title, desc, state, btn, on){",
      "/* ---------------- 3. el equipo ---------------- */",
      "/* ---------------- 4. el equipo ---------------- */\n")
corta("function bindHub(){\n  var v = $('view');\n  v.querySelectorAll('[data-hub]').forEach(function(b){ b.addEventListener('click', function(){\n    var k = b.getAttribute('data-hub');\n    S.form = k;\n    if (k === 'tono')",
      "function bindEq(){", "")

# ----------------------------------------------------------- 5. estado nuevo
sub("S.ctx = S.ctx || {step:0, a:{}, applied:false, more:false};",
    "S.q = S.q || {};\nS.st = S.st || {};\nS.ia = S.ia || {};")

# --------------------------------------------- 6. referencias que quedaban
sub("if ((x = $('talkSum'))) x.addEventListener('click', function(){ S.talk.on = false; S.fix = null; S.page = visible().length - 1; persist(); render(); window.scrollTo(0,0); });",
    "if ((x = $('talkSum'))) x.addEventListener('click', function(){ S.talk.on = false; S.fix = null; S.form = 'uni'; S.st.uni = pasosUni().length - 1; persist(); render(); window.scrollTo(0,0); });")
sub("      if (M.tech === null || M.tech === undefined) { S.locked = false; S.fix = 0; S.tab = 'form'; S.form = 'tono'; var vis = visible(); for (var j = 0; j < vis.length; j++) if (vis[j].sec === 0) { S.page = j; break; } persist(); render(); window.scrollTo(0,0); return; }",
    "      if (M.tech === null || M.tech === undefined) { S.tab = 'form'; S.form = 'uni'; S.st.uni = 0; persist(); render(); window.scrollTo(0,0); return; }")
sub("if (M.known === null) { S.locked = false; S.page = 0; }",
    "if (M.known === null) { S.form = null; }")

# el archivo de partida se lleva tambien las respuestas
sub("function gameJson(){ return JSON.stringify({app:'NOGUM', v:1, saved:new Date().toISOString(), lang:S.lang, locked:S.locked, m:M, chars:S.chars, s",
    "function gameJson(){ return JSON.stringify({app:'NOGUM', v:1, saved:new Date().toISOString(), lang:S.lang, locked:S.locked, q:S.q, m:M, chars:S.chars, s")
sub("  S.locked = o.locked !== false; S.scene = null; S.fix = null; S.tab = 'tpl';",
    "  if (o.q && typeof o.q === 'object') S.q = o.q;\n  S.locked = o.locked !== false; S.scene = null; S.fix = null; S.tab = 'tpl'; S.form = null; S.st = {}; S.ia = {};")

if fallos:
    print('FALLOS:')
    for f in fallos:
        print('  ' + f)
    sys.exit(1)
io.open(F, 'w', encoding='utf-8').write(s)
print('cuatro formularios escritos, %d KB' % (len(s) // 1024))
