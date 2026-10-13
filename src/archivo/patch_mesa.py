# -*- coding: utf-8 -*-
"""La barra de reglas en la ficha, el Codigo de la mesa y la partida en archivo."""
import io, os, shutil
os.chdir(os.path.dirname(os.path.abspath(__file__)))
F = 'app4_body.html'
shutil.copyfile(F, F + '.bak_mesa')
s = io.open(F, encoding='utf-8').read()

CSS = r"""/* barra de reglas de la mesa */
.rulesbar{max-width:210mm;margin:0 auto 12px;border:1px solid var(--rule);border-radius:12px;background:var(--paper);box-shadow:var(--shadow);padding:9px 11px}
.rulesbar .rbrow{display:flex;flex-wrap:wrap;align-items:flex-end;gap:8px}
.rblab{align-self:center;font:600 10.5px/1.2 var(--mono);text-transform:uppercase;letter-spacing:.06em;color:var(--ink-3);margin-right:2px}
.rbf{display:flex;flex-direction:column;gap:3px;min-width:0}
.rbf>span{font:600 9.5px/1 var(--mono);text-transform:uppercase;letter-spacing:.05em;color:var(--ink-3)}
.rbf select{max-width:230px;font:14px/1.2 var(--serif);color:var(--ink);background:var(--ground);border:1px solid var(--rule);border-radius:7px;padding:5px 6px}
.rulesbar .tool.on{border-color:var(--red);background:var(--red-soft);color:var(--red)}
.rulesbar .spacer{flex:1 1 10px}
.rbpanel{border-top:1px solid var(--rule);margin-top:9px;padding-top:9px}
.rbp-h{font:600 10.5px/1 var(--mono);text-transform:uppercase;letter-spacing:.06em;color:var(--ink-3);margin:0 0 6px}
.rbp-t{font-size:13.5px;line-height:1.45;color:var(--ink-2);margin:0 0 9px;max-width:70ch}
.rbgrp{display:flex;gap:8px;align-items:baseline;margin-bottom:6px;flex-wrap:wrap}
.rbgn{flex:0 0 150px;font:600 11px/1.3 var(--mono);color:var(--ink-3)}
.rbgrp .chips{display:flex;flex-wrap:wrap;gap:5px;flex:1 1 300px}
.chip{border:1.5px solid var(--rule);background:var(--ground);border-radius:999px;padding:4px 10px;font-size:12.5px;line-height:1.2;text-align:left}
.chip.on{border-color:var(--red);background:var(--red-soft);color:var(--red);font-weight:600}
.rbcode{display:flex;gap:6px;flex-wrap:wrap;align-items:center;margin-bottom:7px}
.rbcode input{flex:1 1 260px;min-width:0;font:13px/1.3 var(--mono);color:var(--ink);background:var(--ground);border:1px solid var(--rule);border-radius:7px;padding:7px 8px}
.rbcode input[readonly]{font-weight:600;letter-spacing:.02em}
.rulesbar textarea{width:100%;box-sizing:border-box;min-height:70px;font:11.5px/1.4 var(--mono);color:var(--ink);background:var(--ground);border:1px solid var(--rule);border-radius:7px;padding:7px 8px;margin-bottom:7px}
label.tool.file{cursor:pointer;display:inline-flex;align-items:center}
.rbmsg{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin:8px 0 0;font-size:13.5px;background:var(--amber-soft);color:var(--amber);border-radius:8px;padding:7px 10px}
.rbmsg.bad{background:var(--red-soft);color:var(--red)}
@media (max-width:640px){.rbf select{max-width:100%}.rbgn{flex-basis:100%}}
"""

JS = r"""/* ======================= MESA: barra de reglas, Codigo y archivo ======================= */
var rbOpen = null, rbMsg = '', rbBad = false, rbUndo = null, DL = null;
if (window.claude && window.claude.use) window.claude.use('downloads').then(function(x){ DL = x || null; }, function(){ DL = null; });

var CARDCELL = {EPICA:['alto','bajo'], PULP:['alto','alto'], REAL:['neutro','bajo'], PRIM:['neutro','medio'], BOLA:['neutro','alto'], ANG:['bajo','bajo'], PES:['bajo','alto']};
var CARD3 = {EPICA:'EPI', PULP:'PUL', REAL:'REA', PRIM:'PRI', BOLA:'BOL', ANG:'ANG', PES:'PES', TRAG:'TRA'};
var C3 = {}; Object.keys(CARD3).forEach(function(k){ C3[CARD3[k]] = k; });
var CARDORD = ['EPICA','PULP','REAL','PRIM','BOLA','ANG','PES','TRAG'];
var ACCSET = {epico:['alto','medio'], neutro:['neutro','medio'], agobio:['bajo','medio']};
var UNIID = ['fantasia','steampunk','terror','postapo','neon','opera','gotico','supers','wuxia','social','toon'];
var ZOOMK = ['cascara','carne','nucleo'];

function setCard(k){
  S.scene = null;
  if (k === 'TRAG') { M.card = 'TRAG'; return; }
  M.card = null;
  var c = CARDCELL[k]; if (c) { M.opt = c[0]; M.caos = c[1]; M.hueco = 'prev'; }
}
function setAccMode(k){ S.scene = null; M.card = null; var c = ACCSET[k]; if (c) { M.opt = c[0]; M.caos = c[1]; } }
function baulGroupOf(k){ for (var i = 0; i < BAUL_GROUPS.length; i++) if (BAUL_GROUPS[i].k.indexOf(k) > -1) return i; return -1; }
function toggleBaul(k){
  var gi = baulGroupOf(k); if (gi < 0) return;
  var a = (M['b' + gi] || []).filter(function(x){ return x >= 0; }), i = a.indexOf(k);
  if (i > -1) a.splice(i, 1); else a.push(k);
  M['b' + gi] = a;
}
function baulMask(){ var m = 0; baul().forEach(function(k){ if (k >= 0 && k < 16) m |= (1 << k); }); return m; }
function setBaulMask(m){
  BAUL_GROUPS.forEach(function(g, gi){ M['b' + gi] = g.k.filter(function(k){ return (m >> k) & 1; }); });
}
function uniMask(){ var m = 0; universes().forEach(function(id){ var i = UNIID.indexOf(id); if (i > -1) m |= (1 << i); }); return m; }
function hx(n, w){ var s = (n >>> 0).toString(16).toUpperCase(); while (s.length < w) s = '0' + s; return s; }
function restoreM(json){
  var o = JSON.parse(json);
  Object.keys(M).forEach(function(k){ if (!(k in o)) delete M[k]; });
  Object.keys(o).forEach(function(k){ M[k] = o[k]; });
}

/* --- el Codigo --- */
function codeMake(){
  var p = ['N1', 'T' + CARD3[cardBase()], 'Z' + (ZOOMK.indexOf(M.zoom || 'carne') + 1 || 2), 'G' + grid(), 'S' + (estilo() ? 1 : 0), 'B' + hx(baulMask(), 4)];
  if (M.known && M.world !== null) p.push('W' + ('0' + M.world).slice(-2)); else p.push('U' + hx(uniMask(), 3));
  p.push('E' + (isAcc() ? 'A' : 'C'));
  return p.join('-');
}
function codeLink(){ return location.origin + location.pathname + '#c=' + codeMake(); }
function codeParse(str){
  var o = {}, tk = String(str || '').toUpperCase().replace(/[^A-Z0-9]+/g, ' ').trim().split(' ');
  if (!tk.length || tk[0] !== 'N1') return null;
  for (var i = 1; i < tk.length; i++) {
    var k = tk[i].charAt(0), v = tk[i].slice(1);
    if (k === 'T') { if (!C3[v]) return null; o.card = C3[v]; }
    else if (k === 'Z') o.zoom = ZOOMK[(+v) - 1] || 'carne';
    else if (k === 'G') o.grid = Math.max(1, Math.min(5, (+v) || 1));
    else if (k === 'S') o.estilo = v !== '0';
    else if (k === 'B') o.baul = parseInt(v, 16) || 0;
    else if (k === 'W') o.world = +v;
    else if (k === 'U') o.unis = parseInt(v, 16) || 0;
    else if (k === 'E') o.edition = (v === 'A') ? 'acelerado' : 'completo';
  }
  return o.card ? o : null;
}
function applyCode(str){
  var c = codeParse(str); if (!c) return false;
  rbUndo = JSON.stringify(M);
  M.edition = c.edition || 'completo';
  if (c.world !== undefined && KNOWN[c.world]) { M.known = true; M.world = c.world; M.unis = null; }
  else if (c.unis !== undefined) {
    var u = UNIID.filter(function(id, i){ return (c.unis >> i) & 1; });
    M.known = false; M.world = null; M.unis = u.length ? u : null;
  }
  setCard(c.card);
  M.zoom = c.zoom || 'carne';
  M.grid = c.grid || 1;
  M.estilo = c.estilo !== false;
  setBaulMask(c.baul || 0);
  S.scene = null; S.locked = true; S.fix = null;
  return true;
}

/* --- la partida en archivo --- */
function gameJson(){ return JSON.stringify({app:'NOGUM', v:1, saved:new Date().toISOString(), lang:S.lang, locked:S.locked, m:M, chars:S.chars, story:S.story, askMode:S.askMode}, null, 1); }
function gameName(){ var n = worldName().toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '').slice(0, 26); return 'nogum-' + (n || 'mesa') + '.json'; }
function exportGame(){
  var data = gameJson(), name = gameName();
  if (DL) { DL.save({filename:name, data:data}).then(function(){ rbMsg = t('Archivo guardado.','File saved.'); rbBad = false; render(true); }, function(){ var ta = $('rbJson'); if (ta) ta.value = data; rbMsg = t('El navegador no deja guardar: copia el texto de abajo y guardalo tu.','The browser will not save it: copy the text below and keep it yourself.'); rbBad = true; render(true); }); return t('Guardando...','Saving...');
  }
  try {
    var b = new Blob([data], {type:'application/json'}), a = document.createElement('a');
    a.href = URL.createObjectURL(b); a.download = name; document.body.appendChild(a); a.click();
    setTimeout(function(){ URL.revokeObjectURL(a.href); a.remove(); }, 2000);
    return t('Archivo guardado.','File saved.');
  } catch(e){}
  var ta2 = $('rbJson'); if (ta2) ta2.value = data;
  return t('El navegador no deja guardar: copia el texto de abajo y guardalo tu.','The browser will not save it: copy the text below and keep it yourself.');
}
function importGame(txt){
  var o = null;
  try { o = JSON.parse(txt); } catch(e){}
  if (!o || o.app !== 'NOGUM' || !o.m) { rbBad = true; return t('Eso no es una partida de NOGUM.','That is not a NOGUM game.'); }
  if (!confirm(t('La partida del archivo reemplaza esta mesa y todas sus fichas. ¿Seguir?','The game in the file replaces this table and all its sheets. Continue?'))) { rbBad = false; return ''; }
  rbUndo = null;
  restoreM(JSON.stringify(o.m));
  S.chars = Array.isArray(o.chars) ? o.chars : [];
  if (o.story) S.story = o.story;
  if (o.lang) S.lang = o.lang;
  if (o.askMode) S.askMode = o.askMode;
  S.locked = o.locked !== false; S.scene = null; S.fix = null; S.tab = 'tpl';
  rbBad = false;
  return t('Partida abierta: mesa, fichas e historia.','Game loaded: table, sheets and story.');
}

/* --- la barra --- */
function rbSel(f, cur, opts){
  return '<label class="rbf"><span>' + esc(opts.lab) + '</span><select data-rb="' + f + '">' + opts.list.map(function(o){
    return '<option value="' + esc(o[0]) + '"' + (String(o[0]) === String(cur) ? ' selected' : '') + '>' + esc(o[1]) + '</option>';
  }).join('') + '</select></label>';
}
function rulesBar(){
  if (M.known === null) return '';
  var h = '<div class="rulesbar noprint"><div class="rbrow"><span class="rblab">' + esc(t('La mesa','The table')) + '</span>';
  var wl = [[-1, t('Mundo propio','Your own world')]];
  KNOWN.forEach(function(k, i){ wl.push([i, pick(k.n)]); });
  h += rbSel('world', (M.known && M.world !== null) ? M.world : -1, {lab:t('Universo','Universe'), list:wl});
  h += rbSel('edition', edition(), {lab:t('Edición','Edition'), list:[['completo', t('NOGUM completo','Complete NOGUM')], ['acelerado', 'NOGUM Acelerado']]});
  if (isAcc()) {
    h += rbSel('acc', accBase(), {lab:t('Modo','Mode'), list:['epico','neutro','agobio'].map(function(k){ return [k, pick(ACC[k].n)]; })});
  } else {
    h += rbSel('card', cardBase(), {lab:t('Tarjeta','Card'), list:CARDORD.map(function(k){ return [k, pick(CARDS[k].n)]; })});
    h += rbSel('zoom', zoomK(), {lab:t('Vida fractal','Fractal Health'), list:ZOOMK.map(function(k){ return [k, pick(ZOOM[k].n)]; })});
  }
  h += rbSel('grid', grid(), {lab:t('Rejilla','Grid'), list:[1,2,3,4,5].map(function(i){ return [i, i + ' · ' + pick(GRIDN[i])]; })});
  h += '<button type="button" class="tool' + (estilo() ? ' on' : '') + '" data-rbb="estilo">' + esc(t('Estilo +2','Style +2')) + '</button>';
  if (!isAcc()) h += '<button type="button" class="tool' + (rbOpen === 'baul' ? ' on' : '') + '" data-rbb="baul">' + esc(t('Reglas extra','Extra rules')) + ' (' + baul().length + ')</button>';
  h += '<span class="spacer"></span><button type="button" class="tool' + (rbOpen === 'code' ? ' on' : '') + '" data-rbb="code">' + esc(t('Código','Code')) + '</button>';
  h += '<button type="button" class="tool' + (rbOpen === 'file' ? ' on' : '') + '" data-rbb="file">' + esc(t('Archivo','File')) + '</button></div>';
  if (rbOpen === 'baul') h += rbBaul();
  if (rbOpen === 'code') h += rbCode();
  if (rbOpen === 'file') h += rbFile();
  if (rbMsg) h += '<p class="rbmsg' + (rbBad ? ' bad' : '') + '">' + esc(rbMsg) + (rbUndo ? '<button type="button" class="mini" data-rbb="undo">' + esc(t('Deshacer','Undo')) + '</button>' : '') + '<button type="button" class="mini" data-rbb="hide">' + esc(t('Vale','OK')) + '</button></p>';
  return h + '</div>';
}
function rbBaul(){
  var on = baul();
  var h = '<div class="rbpanel"><p class="rbp-h">' + esc(t('Baúl de reglas (8.1)','Rules Chest (8.1)')) + '</p>';
  BAUL_GROUPS.forEach(function(g, gi){
    h += '<div class="rbgrp"><span class="rbgn">' + esc(pick(g.g)) + '</span><div class="chips">';
    g.k.forEach(function(k){ h += '<button type="button" class="chip' + (on.indexOf(k) > -1 ? ' on' : '') + '" data-rbb="baulk" data-k="' + k + '" title="' + esc(pick(BAUL_TIP[k])) + '">' + esc(pick(DATA.baul[k])) + '</button>'; });
    h += '</div></div>';
  });
  return h + '</div>';
}
function rbCode(){
  return '<div class="rbpanel"><p class="rbp-h">' + esc(t('El Código de la mesa','The table Code')) + '</p>' +
    '<p class="rbp-t">' + esc(t('Tu mesa en una línea: universo, edición, tarjeta, vida fractal, rejilla, Estilo y reglas extra. Pásalo y la otra mesa queda igual que la tuya. Al pegar un Código se cambia la mesa entera; las fichas se quedan donde están y pasan a jugar con las reglas nuevas.','Your table in one line: universe, edition, card, Fractal Health, grid, Style and extra rules. Pass it on and the other table ends up like yours. Pasting a Code replaces the whole table; the sheets stay where they are and start playing by the new rules.')) + '</p>' +
    '<div class="rbcode"><input type="text" id="rbCode" readonly value="' + esc(codeMake()) + '"><button type="button" class="tool" data-rbb="copy">' + esc(t('Copiar','Copy')) + '</button><button type="button" class="tool" data-rbb="copylink">' + esc(t('Copiar enlace','Copy link')) + '</button></div>' +
    '<div class="rbcode"><input type="text" id="rbCodeIn" placeholder="' + esc(t('Pega aquí el Código de otra mesa…','Paste another table’s Code here…')) + '"><button type="button" class="tool" data-rbb="apply">' + esc(t('Cambiar la mesa','Change the table')) + '</button></div></div>';
}
function rbFile(){
  return '<div class="rbpanel"><p class="rbp-h">' + esc(t('La partida en un archivo','The game in a file')) + '</p>' +
    '<p class="rbp-t">' + esc(t('El Código lleva la mesa; el archivo lleva la partida entera: mesa, fichas e historia. Guárdalo de vez en cuando, porque la app vive en este navegador y un borrado de datos se lo lleva todo. Al abrir un archivo se cambia todo, fichas incluidas.','The Code carries the table; the file carries the whole game: table, sheets and story. Save one now and then, because the app lives in this browser and clearing its data takes everything with it. Opening a file replaces everything, sheets included.')) + '</p>' +
    '<div class="rbcode"><button type="button" class="tool" data-rbb="export">' + esc(t('Guardar la partida','Save the game')) + '</button><label class="tool file">' + esc(t('Abrir un archivo…','Open a file…')) + '<input type="file" accept=".json,.txt,application/json" data-rbfile="1" hidden></label><button type="button" class="tool" data-rbb="importpaste">' + esc(t('Abrir el texto de abajo','Open the text below')) + '</button></div>' +
    '<textarea id="rbJson" placeholder="' + esc(t('Aquí aparece la partida si el navegador no deja guardar archivos; y aquí puedes pegarla para abrirla.','The game appears here if the browser will not save files; and you can paste one here to open it.')) + '"></textarea></div>';
}
function rbCopy(txt, id){
  var el = $(id);
  try { if (navigator.clipboard && navigator.clipboard.writeText) { navigator.clipboard.writeText(txt); return true; } } catch(e){}
  try { if (el) { el.value = txt; el.select(); return document.execCommand('copy'); } } catch(e){}
  return false;
}
document.addEventListener('click', function(e){
  var b = e.target.closest('.rulesbar [data-rbb]'); if (!b) return;
  var k = b.getAttribute('data-rbb');
  if (k === 'estilo') { M.estilo = !estilo(); rbMsg = ''; }
  else if (k === 'baul' || k === 'code' || k === 'file') { rbOpen = (rbOpen === k) ? null : k; rbMsg = ''; }
  else if (k === 'baulk') { toggleBaul(+b.getAttribute('data-k')); }
  else if (k === 'copy') { rbBad = !rbCopy(codeMake(), 'rbCode'); rbMsg = rbBad ? t('Cópialo a mano desde el recuadro.','Copy it by hand from the box.') : t('Código copiado.','Code copied.'); }
  else if (k === 'copylink') { rbBad = !rbCopy(codeLink(), 'rbCode'); rbMsg = rbBad ? t('Cópialo a mano desde el recuadro.','Copy it by hand from the box.') : t('Enlace copiado.','Link copied.'); }
  else if (k === 'apply') {
    var v = $('rbCodeIn') ? $('rbCodeIn').value : '';
    if (applyCode(v)) { rbBad = false; rbMsg = t('Mesa cambiada: ','Table changed: ') + pick(card().n) + ' · ' + worldName(); rbOpen = null; }
    else { rbBad = true; rbMsg = t('Ese Código no se entiende. Debe empezar por N1.','That Code cannot be read. It has to start with N1.'); }
  }
  else if (k === 'export') { rbMsg = exportGame(); }
  else if (k === 'importpaste') { rbMsg = importGame($('rbJson') ? $('rbJson').value : ''); if (rbMsg && !rbBad) rbOpen = null; }
  else if (k === 'undo') { if (rbUndo) { restoreM(rbUndo); rbUndo = null; S.scene = null; rbMsg = t('Se ha deshecho el cambio.','The change has been undone.'); rbBad = false; } }
  else if (k === 'hide') { rbMsg = ''; }
  else return;
  persist(); render(true);
});
document.addEventListener('change', function(e){
  var el = e.target.closest('.rulesbar [data-rb], .rulesbar [data-rbfile]'); if (!el) return;
  if (el.getAttribute('data-rbfile')) {
    var f = el.files && el.files[0]; if (!f) return;
    var r = new FileReader();
    r.onload = function(){ rbMsg = importGame(String(r.result)); if (rbMsg && !rbBad) rbOpen = null; persist(); render(); };
    r.onerror = function(){ rbBad = true; rbMsg = t('No se ha podido leer el archivo.','The file could not be read.'); render(true); };
    r.readAsText(f); return;
  }
  var f2 = el.getAttribute('data-rb'), v = el.value;
  rbMsg = '';
  if (f2 === 'world') {
    var i = +v;
    if (i < 0) {
      if (M.tech === null || M.tech === undefined) { S.locked = false; S.fix = 0; S.tab = 'form'; var vis = visible(); for (var j = 0; j < vis.length; j++) if (vis[j].sec === 0) { S.page = j; break; } persist(); render(); window.scrollTo(0,0); return; }
      M.known = false; M.world = null;
    } else { M.known = true; M.world = i; M.unis = null; rbUndo = null; rbMsg = t('Universo cambiado. Si además quieres su receta de tono entera, cámbiala con la tarjeta y el resto de la barra.','Universe changed. If you also want its whole tone recipe, set it with the card and the rest of the bar.'); }
  }
  else if (f2 === 'edition') M.edition = v;
  else if (f2 === 'card') setCard(v);
  else if (f2 === 'acc') setAccMode(v);
  else if (f2 === 'zoom') M.zoom = v;
  else if (f2 === 'grid') M.grid = +v;
  persist(); render(true);
});
(function(){
  var m = /[#&?]c=([A-Za-z0-9\-]+)/.exec(location.hash || '');
  if (!m) return;
  if (applyCode(m[1])) {
    S.tab = 'tpl'; rbOpen = null; rbBad = false;
    rbMsg = t('Mesa cargada desde el enlace: ','Table loaded from the link: ') + pick(card().n) + ' · ' + worldName();
    persist();
  }
  try { history.replaceState(null, '', location.pathname + location.search); } catch(e){}
})();

"""

# 1. CSS
assert s.count('</style>') == 1
s = s.replace('</style>', CSS + '</style>')

# 2. la seccion nueva, justo antes del render
A = '/* ======================= RENDER ======================= */'
assert s.count(A) == 1
s = s.replace(A, JS + A)

# 3. la tarjeta puede venir forzada (Tragedia) y el universo puede venir del Codigo
old = "function cardBase(){ var k = CELL[opt() + '|' + caos()];"
assert old in s
s = s.replace(old, "function cardBase(){ if (M.card && CARDS[M.card]) return M.card; var k = CELL[opt() + '|' + caos()];")

old = "  if (M.known && M.world !== null) return KNOWN[M.world].p[5];\n  var u = [];"
assert old in s
s = s.replace(old, "  if (M.known && M.world !== null) return KNOWN[M.world].p[5];\n  if (M.unis && M.unis.length) return M.unis;\n  var u = [];")

old = "  M.flavor = p[7] || 'coste';\n  M.hueco = 'prev';"
assert old in s
s = s.replace(old, "  M.flavor = p[7] || 'coste';\n  M.hueco = 'prev';\n  M.card = null; M.unis = null;")

# 4. el formulario manda sobre la barra: contestar al tono borra la tarjeta forzada
old = "      S.scene = null;\n      if (p.f === 'known')"
assert old in s
s = s.replace(old, "      S.scene = null;\n      if (p.f === 'opt' || p.f === 'caos' || p.f === 'hueco') M.card = null;\n      if (p.f === 'tech' || p.f === 'known') M.unis = null;\n      if (p.f === 'known')")

old = "      M[p.f] = arr; persist(); render(true);"
assert old in s
s = s.replace(old, "      M[p.f] = arr; if (p.f === 'sup' || p.f === 'xtra') M.unis = null; persist(); render(true);")

# 5. la barra, en la plantilla y en cada ficha
old = "  return toolbar() + a4(1, 3, p1) + a4(2, 3, p2) + a4(3, 3, p3) + '<div class=\"create noprint\">"
assert old in s
s = s.replace(old, "  return rulesBar() + toolbar() + a4(1, 3, p1) + a4(2, 3, p2) + a4(3, 3, p3) + '<div class=\"create noprint\">")

old = "  return '<div id=\"pcSheet\">' + toolbar("
assert old in s
s = s.replace(old, "  return rulesBar() + '<div id=\"pcSheet\">' + toolbar(")

# 6. estado: campos nuevos
old = "edition:null, opt:null, caos:null, flavor:null, hueco:null,"
assert old in s
s = s.replace(old, "edition:null, opt:null, caos:null, flavor:null, hueco:null, card:null, unis:null,")

io.open(F, 'w', encoding='utf-8').write(s)
print('app4_body.html parcheado:', len(s), 'bytes')
