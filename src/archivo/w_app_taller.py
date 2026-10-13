# -*- coding: utf-8 -*-
"""La app aprende el taller: piezas genericas siempre disponibles, el equipo que
cuesta puntos, y el buscador de cuatro preguntas."""
import io, os, shutil
os.chdir(os.path.dirname(os.path.abspath(__file__)))
F = 'app4_body.html'
shutil.copyfile(F, F + '.bak_taller')
s = io.open(F, encoding='utf-8').read()

# 1. las piezas sueltas valen en cualquier mesa
old = "function universes(){\n"
assert s.count(old) == 1
s = s.replace(old, "function universes(){ var u = universesBase(); return u.indexOf('piezas') < 0 ? u.concat(['piezas']) : u; }\nfunction universesBase(){\n")

# 2. el equipo que te hace mejor se paga con puntos
OLDC = "function cost(c){ var p = 0;"
NEWC = """function gearNum(c, re){
  var n = 0;
  (c.gear || []).forEach(function(g){
    var b = DATA.bazar.filter(function(x){ return x.id === g.u; })[0];
    var it = b && b.blocks[g.b] && b.blocks[g.b].items[g.i];
    if (!it) return;
    var m = re.exec(pick(it.m) || '');
    if (m) n += +m[1];
  });
  return n;
}
function pointsGear(c){ return gearNum(c, /(\\d+)\\s*(?:puntos?|points?)/); }
function cost(c){ var p = pointsGear(c);"""
assert OLDC in s
s = s.replace(OLDC, NEWC)
old = """function keysGear(c){
  var n = 0;
  (c.gear || []).forEach(function(g){
    var b = DATA.bazar.filter(function(x){ return x.id === g.u; })[0];
    var it = b && b.blocks[g.b] && b.blocks[g.b].items[g.i];
    if (!it) return;
    var m = /(\\d+)\\s*(?:Llaves|Keys)/.exec(pick(it.m) || '');
    if (m) n += +m[1];
  });
  return n;
}"""
assert old in s
s = s.replace(old, "function keysGear(c){ return gearNum(c, /(\\d+)\\s*(?:Llaves|Keys)/); }")

# 3. el buscador de cuatro preguntas
FIND = r"""var CATN = {arma:['Armas','Weapons'], defensa:['Defensas','Defences'], vehiculo:['Vehículos','Vehicles'],
            artefacto:['Artefactos y poderes','Artefacts and powers'], util:['Útiles','Tools']};
var FINDQ = [
  {q:['¿Hace daño?','Does it do damage?'], y:1, n:2},
  {q:['¿Es un vehículo, o lo pilotas?','Is it a vehicle, or do you pilot it?'], y:'vehiculo', n:'arma'},
  {q:['¿Te protege de algo?','Does it protect you from something?'], y:'defensa', n:3},
  {q:['¿Te deja hacer algo que no podrías?','Does it let you do something you could not?'], y:'artefacto', n:'util'}
];
function accOf(it){ var m = /(?:Acceso|Access) (\d)/.exec(pick(it.m) || ''); return m ? +m[1] : 9; }
function findItems(cat){
  var out = [];
  DATA.bazar.forEach(function(bz){
    if (universes().indexOf(bz.id) < 0) return;
    bz.blocks.forEach(function(bl, bi){
      bl.items.forEach(function(it, ii){ if (it.c === cat) out.push({u:bz.id, b:bi, i:ii, it:it}); });
    });
  });
  out.sort(function(a, b){ return accOf(a.it) - accOf(b.it); });
  return out;
}
function finder(){
  var F = S.find = S.find || {open:false, step:0, cat:null};
  var h = '<div class="finder noprint"><button type="button" class="tool" data-fopen="1">'
        + esc(F.open ? t('Cerrar el buscador','Close the finder') : t('¿No sabes qué buscar?','Not sure what to look for?'))
        + '</button>';
  if (!F.open) return h + '</div>';
  if (!F.cat) {
    var q = FINDQ[F.step];
    h += '<div class="fq"><p>' + esc(pick(q.q)) + '</p><button type="button" class="tool strong" data-fans="y">'
      + esc(t('Sí','Yes')) + '</button><button type="button" class="tool" data-fans="n">' + esc(t('No','No'))
      + '</button>' + (F.step ? '<button type="button" class="mini" data-fres="1">' + esc(t('Empezar de nuevo','Start again')) + '</button>' : '') + '</div>';
  } else {
    var list = findItems(F.cat);
    h += '<div class="fq"><p><b>' + esc(pick(CATN[F.cat])) + '</b> · ' + list.length + ' '
      + esc(t('en tu mesa','on your table')) + '<button type="button" class="mini" data-fres="1">'
      + esc(t('Otra búsqueda','Another search')) + '</button></p><div class="flist">';
    list.forEach(function(r){
      h += '<button type="button" class="fitem" data-fadd="' + r.u + '|' + r.b + '|' + r.i + '"><b>'
        + esc(pick(r.it.n)) + '</b><span>' + esc([pick(r.it.d), pick(r.it.e)].filter(function(x){ return x && x !== '—'; }).join(' · ')) + '</span><em>'
        + esc(pick(r.it.m).replace(/\s+/g, ' ').slice(0, 42)) + '</em></button>';
    });
    h += '</div></div>';
  }
  return h + '</div>';
}
"""
anchor = 'function renderChar(c, idx){'
assert s.count(anchor) == 1
s = s.replace(anchor, FIND + anchor)

# 4. el buscador, en la ficha, al lado del selector de equipo
old = """'<div class="addrow noprint"><select id="gType">"""
new = """finder() + '<div class="addrow noprint"><select id="gType">"""
assert old in s
s = s.replace(old, new)

# 5. botones del buscador
old = "  else if (b.id === 'gAdd')"
new = """  else if (b.getAttribute('data-fopen')) { S.find = S.find || {}; S.find.open = !S.find.open; S.find.cat = null; S.find.step = 0; }
  else if ((a = b.getAttribute('data-fans'))) {
    var nx = FINDQ[S.find.step][a === 'y' ? 'y' : 'n'];
    if (typeof nx === 'number') S.find.step = nx; else S.find.cat = nx;
  }
  else if (b.getAttribute('data-fres')) { S.find.cat = null; S.find.step = 0; }
  else if ((a = b.getAttribute('data-fadd'))) { var pz = a.split('|'); c.gear.push({u:pz[0], b:+pz[1], i:+pz[2]}); }
  else if (b.id === 'gAdd')"""
assert old in s
s = s.replace(old, new)

# 6. estilos
CSS = """
.finder{margin:10px 0}
.fq{border:1px solid var(--rule);border-radius:10px;padding:10px;margin-top:8px}
.fq p{margin:0 0 8px;font-size:15px}
.fq .mini{margin-left:10px}
.flist{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:6px;max-height:320px;overflow:auto}
.fitem{text-align:left;border:1px solid var(--rule);background:var(--ground);border-radius:8px;padding:6px 8px;min-width:0}
.fitem b{display:block;font-size:13px}
.fitem span,.fitem em{display:block;font:11px/1.3 var(--mono);color:var(--ink-3);font-style:normal}
.fitem:hover{border-color:var(--red)}
"""
s = s.replace('</style>', CSS + '</style>', 1)
io.open(F, 'w', encoding='utf-8').write(s)
print('app con taller:', len(s))
