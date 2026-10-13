# -*- coding: utf-8 -*-
"""Buscador de palabra clave en el formulario de equipo, antes del arbol."""
import io, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
F = 'app4_body.html'
s = io.open(F, encoding='utf-8').read()
fal = []


def sub(a, b, n=1):
    global s
    if s.count(a) != n:
        fal.append('(%d!=%d) %s' % (s.count(a), n, a[:72])); return
    s = s.replace(a, b, n)


# ---------------------------------------------------- 1. el motor de busqueda
sub("function eqChar(){ return S.chars.filter(function(x){ return x.id === (S.eq && S.eq.who); })[0]; }",
    r"""function eqChar(){ return S.chars.filter(function(x){ return x.id === (S.eq && S.eq.who); })[0]; }
/* acentos fuera y todo en minusculas, que nadie escribe «Katana» con mayuscula */
function norm(x){ return String(x == null ? '' : x).normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase(); }
function eqBusca(q){
  var pal = norm(q).split(/\s+/).filter(function(x){ return x.length > 1; });
  if (!pal.length) return [];
  var out = [];
  DATA.bazar.forEach(function(bz){
    if (universes().indexOf(bz.id) < 0) return;
    var un = norm(uniName(bz.id));
    bz.blocks.forEach(function(bl, bi){
      var bn = norm(pick(bl.n));
      bl.items.forEach(function(it, ii){
        var nom = norm(pick(it.n));
        var todo = nom + ' ' + norm(pick(it.x)) + ' ' + norm(pick(it.d)) + ' ' + norm(pick(it.e)) +
          ' ' + norm(pick(it.a)) + ' ' + norm(pick(it.m)) + ' ' + bn + ' ' + un;
        for (var k = 0; k < pal.length; k++) if (todo.indexOf(pal[k]) < 0) return;
        var enNombre = 1;
        for (var j = 0; j < pal.length; j++) if (nom.indexOf(pal[j]) < 0) { enNombre = 0; break; }
        out.push({u:bz.id, b:bi, i:ii, it:it, nm:enNombre ? 0 : 1});
      });
    });
  });
  out.sort(function(a, b){ return (a.nm - b.nm) || (accOf(a.it) - accOf(b.it)); });
  return out;
}
function eqFicha(c, r){
  var key = eqRef(r), on = S.eq.sel.indexOf(key) > -1, sem = accSem(c, r.it);
  var p = itemPtsOf(r.it), k = itemKeysOf(r.it);
  return '<button type="button" class="fitem' + (on ? ' on' : '') + '" data-eqadd="' + esc(key) + '" aria-pressed="' + on + '"><b>' + esc(pick(r.it.n)) + '</b>' +
    '<span>' + esc([pick(r.it.d), pick(r.it.e), pick(r.it.a)].filter(function(x){ return x && x !== '—'; }).join(' · ')) + '</span>' +
    '<em class="sem ' + sem[0] + '">' + esc(sem[1]) + (p ? ' · ' + p + ' ' + esc(t(p === 1 ? 'punto' : 'puntos', 'pt' + (p === 1 ? '' : 's'))) : '') +
    (k ? ' · ' + k + ' ' + esc(t(k === 1 ? 'Llave' : 'Llaves', 'Key' + (k === 1 ? '' : 's'))) : '') + '</em></button>';
}
function eqResHTML(c){
  var E = S.eq, q = E.busca || '';
  if (norm(q).replace(/\s+/g, '').length < 2) {
    return '<p class="eqvacio">' + esc(t('Escribe una palabra: el nombre si lo sabes, o lo que haga el objeto («veneno», «cuerda», «escudo», «implante»).',
      'Type a word: the name if you know it, or what the item does (“poison”, “rope”, “shield”, “implant”).')) + '</p>';
  }
  var res = eqBusca(q);
  if (!res.length) {
    return '<p class="eqvacio">' + esc(t('Nada con esa palabra en el equipo de tu mesa. Prueba con otra, o búscalo por lo que hace.',
      'Nothing by that word in your table’s gear. Try another one, or search by what it does.')) + '</p>';
  }
  var corte = res.slice(0, 60);
  return '<p class="eqcuantos">' + esc(res.length + ' ' + t(res.length === 1 ? 'objeto' : 'objetos', res.length === 1 ? 'item' : 'items') +
    (res.length > 60 ? t(' · se enseñan los 60 primeros', ' · showing the first 60') : '')) + '</p><div class="flist">' +
    corte.map(function(r){ return eqFicha(c, r); }).join('') + '</div>';
}""")

# ------------------------------------------------- 2. la pagina del buscador
sub("""  /* paso 1: el arbol de busqueda */
  if (!E.cat) {""",
    """  /* el buscador de palabra clave: lo primero, porque si sale a la primera se acabo */
  if (E.modo !== 'arbol' && E.modo !== 'lista') {
    h += '<div class="page"><p class="kick">' + esc(t('De compras','Shopping')) + '</p><p class="big">' +
      esc(t('¿Qué buscáis?','What are you looking for?')) + '</p>' +
      '<div class="eqbuscar"><input type="search" id="eqq" autocomplete="off" spellcheck="false" placeholder="' +
      esc(t('katana, cuerda, veneno, implante…','katana, rope, poison, implant…')) + '" value="' + esc(E.busca || '') + '"></div>' +
      '<div id="eqres">' + eqResHTML(c) + '</div>' +
      '<p class="eqnote">' + esc(t('Se busca en el nombre y en lo que hace cada objeto, solo dentro del equipo que tu mesa tiene abierto.',
        'It searches names and what each item does, only within the gear your table has open.')) + '</p>' +
      '<div class="nav" id="eqnav"><button type="button" class="btn" data-eq="arbol">' +
      esc(t('No sé cómo se llama · búscalo por lo que hace','I do not know its name · search by what it does')) + ' →</button>' +
      '<button type="button" class="btn go" data-eq="cuenta"' + (E.sel.length ? '' : ' disabled') + '>' +
      esc(t('Ir a la cuenta','Go to the bill')) + (E.sel.length ? ' (' + E.sel.length + ')' : '') + ' →</button></div></div></div>';
    return h;
  }
  /* y si no, el arbol de cuatro preguntas */
  if (!E.cat) {""")

# el aviso del arbol deja de parecer una opcion
sub("""    h += '<div class="page"><p class="kick">' + esc(t('Qué estáis buscando','What you are looking for')) + '</p><p class="big">' + esc(pick(q.q)) + '</p>' +
      '<p class="hint">' + esc(t('No hace falta saber el nombre del objeto: basta con saber qué queréis que haga.','You do not need the item’s name: knowing what you want it to do is enough.')) + '</p><div class="choices">' +
      '<button type="button" class="choice" data-eqf="y"><span>' + esc(t('Sí','Yes')) + '</span><span class="mark"></span></button>' +
      '<button type="button" class="choice" data-eqf="n"><span>' + esc(t('No','No')) + '</span><span class="mark"></span></button></div>';
    if (!arcOpen()) h += '<p class="eqnote">' + esc(t('En este mundo no hay Arcano, así que la magia y los poderes no salen en la lista.','This world has no Arcane, so magic and powers do not appear in the list.')) + '</p>';
    h += '<div class="nav"><button type="button" class="btn" data-eq="fres"' + (E.fstep ? '' : ' disabled') + '>' + esc(t('Empezar de nuevo','Start again')) + '</button>' +""",
    """    h += '<div class="page"><p class="kick">' + esc(t('Por lo que hace','By what it does')) + ' · ' + (E.fstep + 1) + ' / 4</p><p class="big">' + esc(pick(q.q)) + '</p><div class="choices">' +
      '<button type="button" class="choice" data-eqf="y"><span>' + esc(t('Sí','Yes')) + '</span><span class="mark"></span></button>' +
      '<button type="button" class="choice" data-eqf="n"><span>' + esc(t('No','No')) + '</span><span class="mark"></span></button></div>';
    if (!arcOpen()) h += '<p class="eqnote">' + esc(t('En este mundo no hay Arcano, así que la magia y los poderes no salen en la lista.','This world has no Arcane, so magic and powers do not appear in the list.')) + '</p>';
    h += '<div class="nav"><button type="button" class="btn" data-eq="busca">← ' + esc(t('Buscar por palabra','Search by word')) + '</button>' +""")

# la lista reutiliza la ficha, para no tener dos sitios donde pintarla
sub("""  list.forEach(function(r){
    var key = eqRef(r), on = E.sel.indexOf(key) > -1, sem = accSem(c, r.it);
    var p = itemPtsOf(r.it), k = itemKeysOf(r.it);
    h += '<button type="button" class="fitem' + (on ? ' on' : '') + '" data-eqadd="' + esc(key) + '" aria-pressed="' + on + '"><b>' + esc(pick(r.it.n)) + '</b>' +
      '<span>' + esc([pick(r.it.d), pick(r.it.e), pick(r.it.a)].filter(function(x){ return x && x !== '—'; }).join(' · ')) + '</span>' +
      '<em class="sem ' + sem[0] + '">' + esc(sem[1]) + (p ? ' · ' + p + ' ' + esc(t(p === 1 ? 'punto' : 'puntos', 'pt' + (p === 1 ? '' : 's'))) : '') + (k ? ' · ' + k + ' ' + esc(t(k === 1 ? 'Llave' : 'Llaves', 'Key' + (k === 1 ? '' : 's'))) : '') + '</em></button>';
  });""",
    """  list.forEach(function(r){ h += eqFicha(c, r); });""")

# ------------------------------------------------------- 3. los enganches
sub("""  v.querySelectorAll('[data-eqwho]').forEach(function(b){ b.addEventListener('click', function(){
    E.who = b.getAttribute('data-eqwho'); E.step = 1; E.fstep = 0; E.cat = null; E.sel = [];
    persist(); render(); window.scrollTo(0,0);
  }); });""",
    """  v.querySelectorAll('[data-eqwho]').forEach(function(b){ b.addEventListener('click', function(){
    E.who = b.getAttribute('data-eqwho'); E.modo = 'busca'; E.busca = ''; E.fstep = 0; E.cat = null; E.sel = [];
    persist(); render(); window.scrollTo(0, 0);
  }); });
  /* el buscador se repinta solo por dentro, para no perder el foco al escribir */
  var inp = $('eqq');
  if (inp) {
    function repinta(){
      var box = $('eqres'); if (box) box.innerHTML = eqResHTML(eqChar());
      var nav = $('eqnav'); if (nav) {
        var go = nav.querySelector('[data-eq="cuenta"]');
        if (go) { go.disabled = !E.sel.length; go.textContent = t('Ir a la cuenta','Go to the bill') + (E.sel.length ? ' (' + E.sel.length + ')' : '') + ' →'; }
      }
    }
    inp.addEventListener('input', function(){ E.busca = inp.value; persist(); repinta(); });
    var box0 = $('eqres');
    if (box0) box0.addEventListener('click', function(ev){
      var b = ev.target.closest('[data-eqadd]'); if (!b) return;
      var key = b.getAttribute('data-eqadd'), i = E.sel.indexOf(key);
      if (i > -1) E.sel.splice(i, 1); else E.sel.push(key);
      persist(); repinta();
    });
    if (window.matchMedia && window.matchMedia('(min-width:768px)').matches) { try { inp.focus(); } catch(e){} }
  }""")
sub("""    if (k === 'exit') { S.form = null; }
    else if (k === 'who') { E.who = null; E.step = 0; }
    else if (k === 'fres') { E.fstep = 0; E.cat = null; E.step = 1; }
    else if (k === 'more') { E.fstep = 0; E.cat = null; E.step = 1; }
    else if (k === 'list') { E.step = 2; }
    else if (k === 'cuenta') { E.step = 3; }""",
    """    if (k === 'exit') { S.form = null; }
    else if (k === 'who') { E.who = null; E.modo = 'busca'; }
    else if (k === 'busca') { E.modo = 'busca'; E.cat = null; E.fstep = 0; }
    else if (k === 'arbol' || k === 'fres') { E.modo = 'arbol'; E.cat = null; E.fstep = 0; }
    else if (k === 'more') { E.modo = 'busca'; E.cat = null; E.fstep = 0; }
    else if (k === 'list') { E.modo = E.cat ? 'lista' : 'busca'; }
    else if (k === 'cuenta') { E.modo = 'cuenta'; }""")
sub("""    if (typeof nx === 'string') { E.cat = nx; E.step = 2; } else { E.fstep = nx; }""",
    """    if (typeof nx === 'string') { E.cat = nx; E.modo = 'lista'; } else { E.fstep = nx; }""")
sub("""  if (E.step === 3) {""", """  if (E.modo === 'cuenta') {""")
sub("""      if (c) { E.sel.forEach(function(key){ var r = eqItem(key); if (r) c.gear.push({u:r.u, b:r.b, i:r.i}); }); S.tab = c.id; }""",
    """      if (c) { E.sel.forEach(function(key){ var r = eqItem(key); if (r) c.gear.push({u:r.u, b:r.b, i:r.i}); }); S.tab = c.id; }""")
sub("""  var E = S.eq = S.eq || {who:null, step:0, fstep:0, cat:null, sel:[]};
  var h = '<div class="wiz"><div class="ftop">""",
    """  var E = S.eq = S.eq || {who:null, modo:'busca', busca:'', fstep:0, cat:null, sel:[]};
  if (!E.modo) { E.modo = 'busca'; E.busca = E.busca || ''; }
  var h = '<div class="wiz"><div class="ftop">""")
sub("""    if (k === 'equipo') S.eq = {who:null, step:0, fstep:0, cat:null, sel:[]};""",
    """    if (k === 'equipo') S.eq = {who:null, modo:'busca', busca:'', fstep:0, cat:null, sel:[]};""")

# -------------------------------------------------------------- 4. el aspecto
sub(".eqnote{font-size:13px;line-height:1.45;color:var(--ink-2);margin:10px 0 0}",
    """.eqnote{font-size:13px;line-height:1.45;color:var(--ink-2);margin:10px 0 0}
.eqbuscar{margin:0 0 12px}
.eqbuscar input{width:100%;box-sizing:border-box;font:18px/1.3 var(--serif);padding:13px 16px;border:2px solid var(--rule);border-radius:12px;background:var(--paper);color:var(--ink)}
.eqbuscar input:focus{outline:none;border-color:var(--red)}
.eqbuscar input::placeholder{color:var(--ink-3)}
.eqvacio{margin:0;padding:18px 4px;font-size:14.5px;line-height:1.5;color:var(--ink-3);text-align:center}
.eqcuantos{margin:0 0 8px;font:11.5px/1.4 var(--mono);text-transform:uppercase;letter-spacing:.05em;color:var(--ink-3)}""")

if fal:
    print('FALLOS:')
    for f in fal:
        print('  ' + f)
    sys.exit(1)
io.open(F, 'w', encoding='utf-8').write(s)
print('buscador de palabra clave puesto')
