# -*- coding: utf-8 -*-
"""La app ensena el acordeon: marca lo que se ha plegado."""
import io, os, shutil
os.chdir(os.path.dirname(os.path.abspath(__file__)))
F = 'app4_body.html'
shutil.copyfile(F, F + '.bak_acord')
s = io.open(F, encoding='utf-8').read()

FOLD = r"""var FOLDN = 3;   // tres Firmas pliegan la Disciplina; tres Disciplinas, el Dominio
function folds(c){
  var out = {dis:{}, dom:{}, amb:{}};
  if (!c) return out;
  AMB.forEach(function(a, ai){
    var domsOk = 0;
    a.doms.forEach(function(d, di){
      var disOk = 0;
      d.dis.forEach(function(x, si){
        var sk = ai + '.' + di + '.' + si, n = 0;
        c.fir.forEach(function(f){ if (f.key === sk && f.lv === 4) n++; });
        if (n >= FOLDN) { out.dis[sk] = true; disOk++; }
      });
      if (disOk >= FOLDN) { out.dom[ai + '.' + di] = true; domsOk++; }
    });
    if (domsOk >= a.doms.length) out.amb[ai] = true;
  });
  return out;
}
"""
anchor = 'function skillGrid(c){'
assert s.count(anchor) == 1
s = s.replace(anchor, FOLD + anchor)

old = "function skillGrid(c){\n  var blank = !c, h = '<div class=\"skillgrid\">';"
new = "function skillGrid(c){\n  var blank = !c, FD = folds(c), h = '<div class=\"skillgrid\">';"
assert old in s
s = s.replace(old, new)

# la Disciplina plegada se marca y cuenta como +4
old = """        if (sOn) best = Math.max(best, 2);
        body += '<div class="srow dis">' + dots(2, sOn ? 2 : (dOn ? 1 : 0), (!blank && dOn) ? [2] : [], 'data-dis="' + sk + '"') + '<span class="nm">' + esc(pick(s)) + '</span>'"""
new = """        if (sOn) best = Math.max(best, 2);
        var fdis = FD.dis[sk];
        if (fdis) best = Math.max(best, 4);
        body += '<div class="srow dis' + (fdis ? ' folded' : '') + '">' + dots(2, sOn ? 2 : (dOn ? 1 : 0), (!blank && dOn) ? [2] : [], 'data-dis="' + sk + '"') + '<span class="nm">' + esc(pick(s)) + (fdis ? ' <span class="fold">' + esc(t('plegada +4','folded +4')) + '</span>' : '') + '</span>'"""
assert old in s
s = s.replace(old, new)

# el Dominio plegado
old = """      body += '<div class="dcol"><div class="srow dom">' + dots(1, dOn ? 1 : 0, blank ? [] : [1], 'data-dom="' + dk + '"') + '<span class="nm">' + esc(pick(d.n)) + '</span>"""
new = """      var fdom = FD.dom[dk];
      if (fdom) best = Math.max(best, 4);
      body += '<div class="dcol"><div class="srow dom' + (fdom ? ' folded' : '') + '">' + dots(1, dOn ? 1 : 0, blank ? [] : [1], 'data-dom="' + dk + '"') + '<span class="nm">' + esc(pick(d.n)) + (fdom ? ' <span class="fold">' + esc(t('plegado +4','folded +4')) + '</span>' : '') + '</span>"""
assert old in s
s = s.replace(old, new)

# el Ambito plegado, en la cabecera de la tarjeta
old = """<span class="best">' + esc(t('Mejor ','Best ')) + bonusTxt(best) + '</span>"""
new = """<span class="best">' + esc(t('Mejor ','Best ')) + bonusTxt(best) + '</span>' + (FD.amb[ai] ? '<span class="fold big">' + esc(t('ÁMBITO PLEGADO','SPHERE FOLDED')) + '</span>' : '') + '"""
assert old in s
s = s.replace(old, new)

# recordatorio
old = "<li>' + esc(t('Cada nivel multiplica por cien tu alcance."
new = "<li>' + esc(t('El acordeón: 3 Firmas de Gran Maestro pliegan la Disciplina entera en +4, 3 Disciplinas el Dominio, y los 2 Dominios el Ámbito.','The accordion: 3 Grand Master Signatures fold the whole Discipline into +4, 3 Disciplines the Domain, and both Domains the Sphere.')) + '</li><li>' + esc(t('Cada nivel multiplica por cien tu alcance."
assert old in s
s = s.replace(old, new, 1)

CSS = """
.fold{font:600 9.5px/1 var(--mono);text-transform:uppercase;letter-spacing:.04em;color:var(--red);background:var(--red-soft);border-radius:999px;padding:2px 6px;margin-left:5px}
.fold.big{margin-left:auto}
.srow.folded .nm{font-weight:600}
"""
s = s.replace('</style>', CSS + '</style>', 1)
io.open(F, 'w', encoding='utf-8').write(s)
print('app con acordeon')
