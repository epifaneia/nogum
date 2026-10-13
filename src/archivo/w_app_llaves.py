# -*- coding: utf-8 -*-
"""La app aprende las Llaves: 12/14 puntos, bote aparte, techos de Rejilla y el x100."""
import io, os, shutil
os.chdir(os.path.dirname(os.path.abspath(__file__)))
F = 'app4_body.html'
shutil.copyfile(F, F + '.bak_llaves')
s = io.open(F, encoding='utf-8').read()

# ---------------------------------------------------------------- 1. datos nuevos
TECHO_JS = r"""/* techos de Rejilla por receta (8.4): fis, men, soc, tec, arc; 0 = no existe */
var TECHO = {
  0:[3,2,3,2,4], 1:[2,2,3,2,3], 2:[2,2,3,2,4], 3:[2,2,4,2,3], 4:[2,2,3,2,0],
  5:[2,1,2,1,2], 6:[3,2,4,3,4], 7:[2,1,4,2,0], 8:[3,3,3,4,0], 9:[2,1,2,2,2],
  10:[2,2,3,3,3], 11:[1,1,2,1,1], 12:[2,2,4,1,3], 13:[1,1,1,1,0], 14:[2,1,2,1,2],
  15:[2,1,3,2,2], 16:[5,5,4,5,5], 17:[5,2,2,2,5], 18:[4,1,2,3,0], 19:[1,1,2,2,2]
};
function arcOpen(){
  if (M.known && M.world !== null) { var tc = TECHO[KNOWN[M.world].r]; return tc ? tc[4] > 0 : true; }
  var sp = M.sup || [];
  return ['magia','monstruos','poderes','ki'].some(function(k){ return sp.indexOf(k) > -1; });
}
function techos(){
  if (M.known && M.world !== null) { var tc = TECHO[KNOWN[M.world].r]; if (tc) return tc; }
  return [5,5,5,5, arcOpen() ? 5 : 0];
}
function techo(ai){ var v = techos()[ai]; return v === undefined ? 5 : v; }
function budget(){ return arcOpen() ? 14 : 12; }
function keyCost(k){ var n = k.lv || 1; return n * n; }
function keysOwn(c){ var n = 0; (c.klist || []).forEach(function(k){ n += keyCost(k); }); return n; }
function keysGear(c){
  var n = 0;
  (c.gear || []).forEach(function(g){
    var b = DATA.bazar.filter(function(x){ return x.id === g.u; })[0];
    var it = b && b.blocks[g.b] && b.blocks[g.b].items[g.i];
    if (!it) return;
    var m = /(\d+)\s*(?:Llaves|Keys)/.exec(pick(it.m) || '');
    if (m) n += +m[1];
  });
  return n;
}
function keysHave(c){ return (c.pot === 'rejilla' ? 0 : 5) + (+c.kw || 0); }
function keysUsed(c){ return keysOwn(c) + keysGear(c); }

"""
anchor = 'function newChar(){'
assert s.count(anchor) == 1
s = s.replace(anchor, TECHO_JS + anchor)

# ---------------------------------------------------------------- 2. el x100
old = "var GRIDN = [null,['Una persona','One person'],['Una sala llena','A full room'],['Un edificio','A building'],['Una ciudad','A city'],['Un país','A country']];"
new = ("var GRIDN = [null,['Una persona · ×1','One person · ×1'],['Una sala llena · ×100','A full room · ×100'],"
       "['Un edificio · ×10.000','A building · ×10,000'],['Una ciudad · ×1.000.000','A city · ×1,000,000'],"
       "['Un país · ×100.000.000','A country · ×100,000,000']];")
assert old in s
s = s.replace(old, new)

# ---------------------------------------------------------------- 3. ficha nueva
old = "function newChar(){ var c = {id:'pc' + Date.now().toString(36), name:'', concept:'', grid:{}, dom:{}, dis:{}, fir:[], gear:[], stance:'violencia', dmg:{fis:0,men:0,esp:0}, keys:'', notes:''}; AMB.forEach(function(a){ c.grid[a.id] = grid(); }); return c; }"
new = ("function newChar(){ var c = {id:'pc' + Date.now().toString(36), name:'', concept:'', grid:{}, dom:{}, dis:{}, "
       "fir:[], gear:[], stance:'violencia', dmg:{fis:0,men:0,esp:0}, keys:'', notes:'', klist:[], pot:'llaves', potAmb:'', kw:0}; "
       "AMB.forEach(function(a, ai){ c.grid[a.id] = Math.min(grid(), techo(ai) || 1); }); return c; }")
assert old in s
s = s.replace(old, new)

# ---------------------------------------------------------------- 4. el contador de puntos
old = "  var extra = '<span class=\"pts' + (p > 10 ? ' over' : '') + '\">' + p + ' / 10</span>'"
new = "  var extra = '<span class=\"pts' + (p > budget() ? ' over' : '') + '\">' + p + ' / ' + budget() + '</span>'"
assert old in s
s = s.replace(old, new)
old = "    (p > 10 ? '<p class=\"lockmsg\">' + esc(t('Te has pasado de los 10 puntos.','You are over the 10 points.')) + '</p>' : '');"
new = "    (p > budget() ? '<p class=\"lockmsg\">' + esc(t('Te has pasado de los ','You are over the ') + budget() + t(' puntos.',' points.')) + '</p>' : '');"
assert old in s
s = s.replace(old, new)
old = "'<span class=\"badge\">' + esc(t('0 / 10 puntos','0 / 10 points')) + '</span>'"
new = "'<span class=\"badge\">' + esc('0 / ' + budget() + t(' puntos',' points')) + '</span>'"
assert old in s
s = s.replace(old, new)

# ---------------------------------------------------------------- 5. el techo en la rejilla de la ficha
old = """    var seg = '<span class="seg">';
    for (var g = 1; g <= 6; g++) seg += '<button type="button" class="' + (g <= lvl ? 'on' : '') + '"' + (blank ? ' disabled' : ' data-gridset="' + a.id + '" data-n="' + g + '"') + ' aria-label="' + g + '"></button>';
    seg += '</span>';"""
new = """    var cap = techo(ai), seg = '<span class="seg">';
    if (cap && lvl > cap) lvl = cap;
    for (var g = 1; g <= 6; g++) {
      var over = cap && g > cap;
      seg += '<button type="button" class="' + (g <= lvl ? 'on' : '') + (over ? ' cap' : '') + '"' + (blank || over ? ' disabled' : ' data-gridset="' + a.id + '" data-n="' + g + '"') + ' aria-label="' + g + '"></button>';
    }
    seg += '</span>';"""
assert old in s
s = s.replace(old, new)

old = """      '<div class="power"><span class="lab">' + esc(t('Rejilla','Grid')) + '</span>' + seg + '<span class="lab"><b>' + lvl + '</b> · ' + esc(lvl >= 6 ? t('Cósmico','Cosmic') : pick(GRIDN[lvl])) + '</span></div><div class="dcols">' + body + '</div></div>';"""
new = """      '<div class="power"><span class="lab">' + esc(t('Rejilla','Grid')) + '</span>' + seg + '<span class="lab"><b>' + lvl + '</b> · ' + esc(lvl >= 6 ? t('Cósmico','Cosmic') : pick(GRIDN[lvl])) + '</span>' + (cap && cap < 5 ? '<span class="techo">' + esc(t('techo ','ceiling ') + cap) + '</span>' : '') + '</div><div class="dcols">' + body + '</div></div>';"""
assert old in s
s = s.replace(old, new)

old = """    h += '<div class="acard' + (!blank && !has ? ' null' : '') + '">"""
new = """    h += '<div class="acard' + (!blank && !has ? ' null' : '') + (techo(ai) === 0 ? ' noexiste' : '') + '">"""
assert old in s
s = s.replace(old, new)

# ---------------------------------------------------------------- 6. el bloque de Llaves
KEYS_JS = r"""function keysBlock(c){
  var forms = [['dis', t('una Disciplina, para siempre','one Discipline, for ever')],
               ['amb', t('un Ámbito entero, una escena','a whole Sphere, one scene')]];
  var h = '<div class="sec">' + esc(t('Bote aparte y Llaves','Separate pot and Keys')) + '<span class="note">' +
    esc(t('+1 de Rejilla en un ámbito o 5 Llaves. No se cambia por puntos.','+1 Grid in one sphere or 5 Keys. It does not trade for points.')) + '</span></div>';
  if (!c) {
    h += '<div class="keys"><div class="potrow"><button type="button" class="potb" disabled>' + esc(t('+1 Rejilla','+1 Grid')) + '</button><button type="button" class="potb" disabled>' + esc(t('5 Llaves','5 Keys')) + '</button></div>';
    for (var i = 0; i < 5; i++) h += '<div class="krow blank"><span class="line"></span><span class="kf">' + esc(t('Disciplina / Ámbito','Discipline / Sphere')) + '</span><span class="kc">□</span></div>';
    return h + '</div>';
  }
  var used = keysUsed(c), have = keysHave(c), gear = keysGear(c);
  h += '<div class="keys"><div class="potrow">' +
    '<button type="button" class="potb" data-pot="rejilla" aria-pressed="' + (c.pot === 'rejilla') + '">' + esc(t('+1 Rejilla','+1 Grid')) + '</button>' +
    (c.pot === 'rejilla' ? '<select data-potamb>' + AMB.map(function(a, ai){ return techo(ai) ? '<option value="' + a.id + '"' + (c.potAmb === a.id ? ' selected' : '') + '>' + esc(pick(a.n)) + '</option>' : ''; }).join('') + '</select>' : '') +
    '<button type="button" class="potb" data-pot="llaves" aria-pressed="' + (c.pot !== 'rejilla') + '">' + esc(t('5 Llaves','5 Keys')) + '</button>' +
    '<span class="kcount' + (used > have ? ' over' : '') + '">' + used + ' / ' + have + ' ' + esc(t('Llaves','Keys')) + '</span>' +
    '<label class="kw noprint">' + esc(t('Ganadas','Earned')) + ' <input type="number" min="0" max="99" id="f-kw" value="' + (+c.kw || 0) + '"></label></div>';
  (c.klist || []).forEach(function(k, ki){
    h += '<div class="krow"><input type="text" data-ktxt="' + ki + '" placeholder="' + esc(t('contra qué…','against what…')) + '" value="' + esc(k.t || '') + '">' +
      '<select data-kform="' + ki + '">' + forms.map(function(f){ return '<option value="' + f[0] + '"' + (k.w === f[0] ? ' selected' : '') + '>' + esc(f[1]) + '</option>'; }).join('') + '</select>' +
      '<select data-klv="' + ki + '">' + [1,2,3,4,5].map(function(n){ return '<option value="' + n + '"' + (+k.lv === n ? ' selected' : '') + '>+' + n + '</option>'; }).join('') + '</select>' +
      '<span class="kc">' + keyCost(k) + '</span><button type="button" class="plus noprint" data-kdel="' + ki + '">×</button></div>';
  });
  h += '<div class="krow noprint"><button type="button" class="tool" data-kadd="1">' + esc(t('Añadir Llave','Add Key')) + '</button>' +
    (gear ? '<span class="note">' + esc(t('El equipo que rompe la Rejilla se lleva ','Grid-breaking equipment takes ') + gear + t(' Llaves.',' Keys.')) + '</span>' : '') + '</div>';
  return h + '</div>';
}
"""
anchor = 'function stanceBlock(c){'
assert s.count(anchor) == 1
s = s.replace(anchor, KEYS_JS + anchor)

# ---- se sustituye el campo de texto de Llaves en la ficha
old = """'<div class="fields" style="margin-top:12px"><div><label for="f-keys">' + esc(t('Llaves','Keys')) + '</label><textarea id="f-keys">' + esc(c.keys) + '</textarea></div><div><label for="f-notes">' + esc(t('Heridas y notas','Wounds and notes')) + '</label><textarea id="f-notes">' + esc(c.notes) + '</textarea></div></div>';"""
new = """keysBlock(c) + '<div class="fields" style="margin-top:12px"><div><label for="f-keys">' + esc(t('Notas de Llaves','Key notes')) + '</label><textarea id="f-keys">' + esc(c.keys) + '</textarea></div><div><label for="f-notes">' + esc(t('Heridas y notas','Wounds and notes')) + '</label><textarea id="f-notes">' + esc(c.notes) + '</textarea></div></div>';"""
assert old in s
s = s.replace(old, new)

# ---- y en la plantilla en blanco
old = """'<div class="fields"><div><div class="sec">' + esc(t('Llaves','Keys')) + '</div><div class="lines"><div class="line"></div><div class="line"></div></div></div><div><div class="sec">' + esc(t('Heridas y notas','Wounds and notes')) + '</div><div class="lines"><div class="line"></div><div class="line"></div></div></div></div>';"""
new = """keysBlock(null) + '<div class="fields"><div><div class="sec">' + esc(t('Notas','Notes')) + '</div><div class="lines"><div class="line"></div><div class="line"></div></div></div><div><div class="sec">' + esc(t('Heridas','Wounds')) + '</div><div class="lines"><div class="line"></div><div class="line"></div></div></div></div>';"""
assert old in s
s = s.replace(old, new)

# ---------------------------------------------------------------- 7. botones nuevos en onChar
old = "  else if ((a = b.getAttribute('data-gridset'))) c.grid[a] = +b.getAttribute('data-n');"
new = """  else if ((a = b.getAttribute('data-gridset'))) { var ai = AMB.map(function(x){ return x.id; }).indexOf(a), cap = techo(ai); var n = +b.getAttribute('data-n'); c.grid[a] = (cap && n > cap) ? cap : n; }
  else if ((a = b.getAttribute('data-pot'))) {
    if (a === 'rejilla') {
      c.pot = 'rejilla';
      if (!c.potAmb) { for (var pi = 0; pi < AMB.length; pi++) if (techo(pi)) { c.potAmb = AMB[pi].id; break; } }
      setPot(c);
    } else { if (c.potAmb) c.grid[c.potAmb] = Math.min(grid(), techo(AMB.map(function(x){ return x.id; }).indexOf(c.potAmb)) || 1); c.pot = 'llaves'; }
  }
  else if (b.getAttribute('data-kadd')) { c.klist = c.klist || []; c.klist.push({t:'', w:'dis', lv:1}); }
  else if ((a = b.getAttribute('data-kdel')) !== null && a !== undefined) { c.klist.splice(+a, 1); }"""
assert old in s
s = s.replace(old, new)

SETPOT = r"""function setPot(c){
  var ai = AMB.map(function(x){ return x.id; }).indexOf(c.potAmb);
  if (ai < 0) return;
  var cap = techo(ai) || 1;
  c.grid[c.potAmb] = Math.min(grid() + 1, cap);
}
"""
s = s.replace('function keysBlock(c){', SETPOT + 'function keysBlock(c){')

# ---------------------------------------------------------------- 8. enlaces de los campos nuevos
old = "    ['concept','keys','notes'].forEach(function(k){ $('f-' + k).addEventListener('input', function(){ c[k] = this.value; persist(); }); });"
new = """    ['concept','keys','notes'].forEach(function(k){ $('f-' + k).addEventListener('input', function(){ c[k] = this.value; persist(); }); });
    if ($('f-kw')) $('f-kw').addEventListener('input', function(){ c.kw = Math.max(0, +this.value || 0); persist(); render(true); });
    sh.querySelectorAll('[data-ktxt]').forEach(function(x){ x.addEventListener('input', function(){ c.klist[+x.getAttribute('data-ktxt')].t = x.value; persist(); }); });
    sh.querySelectorAll('[data-kform]').forEach(function(x){ x.addEventListener('change', function(){ c.klist[+x.getAttribute('data-kform')].w = x.value; persist(); render(true); }); });
    sh.querySelectorAll('[data-klv]').forEach(function(x){ x.addEventListener('change', function(){ c.klist[+x.getAttribute('data-klv')].lv = +x.value; persist(); render(true); }); });
    sh.querySelectorAll('[data-potamb]').forEach(function(x){ x.addEventListener('change', function(){ var old = c.potAmb; if (old) c.grid[old] = Math.min(grid(), techo(AMB.map(function(y){ return y.id; }).indexOf(old)) || 1); c.potAmb = x.value; setPot(c); persist(); render(true); }); });"""
assert old in s
s = s.replace(old, new)

# ---------------------------------------------------------------- 9. cabecera de equipo
old = "esc(t('Rejilla / efecto','Grid / effect'))"
new = "esc(t('Acceso / Rejilla','Access / Grid'))"
assert old in s
s = s.replace(old, new)

# ---------------------------------------------------------------- 10. estilos
CSS = """
.acard .techo{font:600 10px/1 var(--mono);color:var(--red);background:var(--red-soft);border-radius:999px;padding:3px 7px;margin-left:6px}
.acard.noexiste{opacity:.55}
.seg button.cap{background:repeating-linear-gradient(135deg,transparent,transparent 3px,var(--rule) 3px,var(--rule) 4px);cursor:not-allowed}
.keys{border:1px solid var(--rule);border-radius:10px;padding:8px 10px;margin-bottom:10px}
.potrow{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin-bottom:8px}
.potb{border:1.5px solid var(--rule);background:var(--ground);border-radius:999px;padding:4px 12px;font-size:13px}
.potb[aria-pressed="true"]{border-color:var(--red);background:var(--red-soft);color:var(--red);font-weight:600}
.potrow select{font:13px/1.2 var(--serif);border:1px solid var(--rule);border-radius:7px;padding:4px 6px;background:var(--ground);color:var(--ink)}
.kcount{margin-left:auto;font:600 12px/1 var(--mono);color:var(--ink-3)}
.kcount.over{color:var(--red)}
.kw{font:600 10px/1 var(--mono);text-transform:uppercase;color:var(--ink-3);display:flex;align-items:center;gap:5px}
.kw input{width:46px;font:13px var(--mono);border:1px solid var(--rule);border-radius:6px;padding:3px 5px;background:var(--ground);color:var(--ink)}
.krow{display:flex;gap:6px;align-items:center;margin-bottom:5px}
.krow input[type=text]{flex:1 1 140px;min-width:0;font:13px var(--serif);border:0;border-bottom:1px solid var(--rule);background:transparent;color:var(--ink);padding:3px 2px}
.krow select{font:12px var(--serif);border:1px solid var(--rule);border-radius:6px;padding:3px 4px;background:var(--ground);color:var(--ink);max-width:190px}
.krow .kc{font:600 13px var(--mono);color:var(--ink-2);min-width:18px;text-align:right}
.krow.blank{color:var(--ink-3)}
.krow.blank .line{flex:1;border-bottom:1px solid var(--rule)}
.krow.blank .kf{font:11px var(--mono);color:var(--ink-3)}
"""
s = s.replace('</style>', CSS + '</style>', 1)

io.open(F, 'w', encoding='utf-8').write(s)
print('app parcheada:', len(s), 'bytes')
