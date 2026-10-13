# -*- coding: utf-8 -*-
"""App: las siete tarjetas definitivas y el motor de dados con bandas + coste sobre el total."""
import io, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
p = 'app4_body.html'
s = io.open(p, encoding='utf-8').read()


def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:70], s.count(a))
    s = s.replace(a, b)


i = s.index('var CARDS = {')
j = s.index('var CELL = {')
CARDS = """var CARDS = {
  EPICA:{n:['Épica','Epic'], r:'mejor', tn:6, bp:'normal', bc:'normal', roll:['2d10, quédate el ALTO + bono','2d10, keep the HIGHER + bonus'], fum:['Leído 1 (doble 1) · 1 %','A read 1 (double 1) · 1%'], cri:['Leído 10 (un 10 en cualquiera) · 19 %','A read 10 (a 10 on either) · 19%']},
  PULP:{n:['Pulp desenfrenado','Unleashed Pulp'], r:'mejor', tn:6, bp:'ancha', bc:'normal', coste:true, partial:true, roll:['2d10, quédate el ALTO + bono','2d10, keep the HIGHER + bonus'], fum:['Leído 1–2 · 4 %','A read 1–2 · 4%'], cri:['Leído 10 · 19 %','A read 10 · 19%'], bands:['Si aciertas justo (total 6 o 7), sale con coste','If you just make it (total 6 or 7), it comes at a cost']},
  REAL:{n:['Realista','Realist'], r:'suma', tn:11, bp:'normal', bc:'normal', roll:['SUMA los 2d10 + bono','SUM the 2d10 + bonus'], fum:['Suma 2–3 · 3 %','Sum 2–3 · 3%'], cri:['Suma 19–20 · 3 %','Sum 19–20 · 3%']},
  PRIM:{n:['Primera marcha','First Gear'], r:'rojo', tn:6, bp:'normal', bc:'normal', roll:['Solo el dado rojo + bono','Red die only + bonus'], fum:['Leído 1 · 10 %','A read 1 · 10%'], cri:['Leído 10 · 10 %','A read 10 · 10%']},
  BOLA:{n:['Bola de nieve','Snowball'], r:'rojo', tn:6, bp:'ancha', bc:'ancha', coste:true, partial:true, roll:['Solo el dado rojo + bono','Red die only + bonus'], fum:['Leído 1–2 · 20 %','A read 1–2 · 20%'], cri:['Leído 9–10 · 20 %','A read 9–10 · 20%'], bands:['Si aciertas justo (total 6 o 7), sale con coste','If you just make it (total 6 or 7), it comes at a cost']},
  ANG:{n:['Angustia','Anguish'], r:'peor', tn:6, bp:'estrecha', bc:'estrecha', roll:['2d10, quédate el BAJO + bono','2d10, keep the LOWER + bonus'], fum:['Doble 1 · 1 %','Double 1 · 1%'], cri:['Doble 10 · 1 %','Double 10 · 1%']},
  PES:{n:['Pesadilla','Nightmare'], r:'peor', tn:6, bp:'normal', bc:'normal', roll:['2d10, quédate el BAJO + bono','2d10, keep the LOWER + bonus'], fum:['Leído 1 (cualquier 1) · 19 %','A read 1 (any 1) · 19%'], cri:['Leído 10 (doble 10) · 1 %','A read 10 (double 10) · 1%']},
  TRAG:{n:['Tragedia (receta)','Tragedy (recipe)'], r:'suma', tn:14, bp:'normal', bc:'normal', roll:['SUMA los 2d10 + bono','SUM the 2d10 + bonus'], fum:['Suma 2–3 · 3 %','Sum 2–3 · 3%'], cri:['Suma 19–20 · 3 %','Sum 19–20 · 3%']}
};
"""
s = s[:i] + CARDS + s[j:]

# Acelerado: el Agobio lleva el coste con la misma regla
rep("agobio:{n:['Modo Agobio','Dread mode'], r:'peor', tn:6, f:1, c:10, p:true, roll:['El menor de los dos dados + bono','The lower of the two dice + bonus'], fum:['Leído 1 (cualquier 1)','A read 1 (any 1)'], cri:['Leído 10 (doble 10)','A read 10 (double 10)'], bands:['≤4 fallo · 5–6 éxito con coste · 7+ éxito','≤4 failure · 5–6 success at a cost · 7+ success'], partial:true}",
    "agobio:{n:['Modo Agobio','Dread mode'], r:'peor', tn:6, bp:'normal', bc:'normal', coste:true, partial:true, roll:['El menor de los dos dados + bono','The lower of the two dice + bonus'], fum:['Leído 1 (cualquier 1)','A read 1 (any 1)'], cri:['Leído 10 (doble 10)','A read 10 (double 10)'], bands:['Si aciertas justo (total 6 o 7), sale con coste','If you just make it (total 6 or 7), it comes at a cost']}")
rep("epico:{n:['Modo Épico','Epic mode'], r:'mejor', tn:6, f:1, c:10, roll:", "epico:{n:['Modo Épico','Epic mode'], r:'mejor', tn:6, bp:'normal', bc:'normal', roll:")
rep("neutro:{n:['Modo Neutro','Neutral mode'], r:'rojo', tn:6, f:1, c:10, roll:", "neutro:{n:['Modo Neutro','Neutral mode'], r:'rojo', tn:6, bp:'normal', bc:'normal', roll:")

rep("var CELL = {'alto|bajo':'EPICA','alto|medio':null,'alto|alto':'PULP','neutro|bajo':'REAL','neutro|medio':'PRIM','neutro|alto':'BOLA','bajo|bajo':'ANG','bajo|medio':null,'bajo|alto':'PES'};",
    "var CELL = {'alto|bajo':'EPICA','alto|medio':null,'alto|alto':'PULP','neutro|bajo':'REAL','neutro|medio':'PRIM','neutro|alto':'BOLA','bajo|bajo':'ANG','bajo|medio':null,'bajo|alto':'PES'};")

# ---------- motor de dados ----------
rep("""function rollNow(){
  var C = card(), r = d10(), b = d10(), nat, use, m = C.r || 'rojo';
  if (m === 'rojo') { nat = r; use = 'r'; }
  else if (m === 'mejor') { nat = Math.max(r, b); use = r >= b ? 'r' : 'b'; }
  else if (m === 'peor') { nat = Math.min(r, b); use = r <= b ? 'r' : 'b'; }
  else { nat = r + b; use = 'both'; }
  var fum = nat <= (C.f || 1), cri = nat >= (C.c || 10);
  var B = diceBonus(), tot = nat + B.tot, tn = C.tn || 6, out;
  if (fum) out = 'fum'; else if (cri) out = 'cri';
  else if (C.partial) out = tot <= 4 ? 'fail' : tot <= 6 ? 'part' : 'ok';
  else out = tot >= tn ? 'ok' : 'fail';""",
    """function banda(C, side, r, nat){
  var w = side ? (C.bc || 'normal') : (C.bp || 'normal');
  if (C.r === 'suma') return side ? nat >= 19 : nat <= 3;
  if (w === 'estrecha') return side ? (r[0] === 10 && r[1] === 10) : (r[0] === 1 && r[1] === 1);
  if (w === 'normal') return side ? nat >= 10 : nat <= 1;
  return side ? nat >= 9 : nat <= 2;
}
function rollNow(){
  var C = card(), r = d10(), b = d10(), nat, use, m = C.r || 'rojo';
  if (m === 'rojo') { nat = r; use = 'r'; }
  else if (m === 'mejor') { nat = Math.max(r, b); use = r >= b ? 'r' : 'b'; }
  else if (m === 'peor') { nat = Math.min(r, b); use = r <= b ? 'r' : 'b'; }
  else { nat = r + b; use = 'both'; }
  var fum = banda(C, 0, [r, b], nat), cri = banda(C, 1, [r, b], nat);
  var B = diceBonus(), tot = nat + B.tot, tn = C.tn || 6, out;
  if (fum) out = 'fum'; else if (cri) out = 'cri';
  else if (C.coste && tot >= tn && tot <= tn + 1) out = 'part';
  else out = tot >= tn ? 'ok' : 'fail';""")

# recordatorio de la ficha: el coste se explica aparte
rep("(c.bands ? '<dt>' + esc(t('Resultado','Result')) + '</dt><dd>' + esc(pick(c.bands)) + '</dd>' : '')",
    "(c.bands ? '<dt>' + esc(t('Éxito con coste','Success at a cost')) + '</dt><dd>' + esc(pick(c.bands)) + '</dd>' : '')")

io.open(p, 'w', encoding='utf-8').write(s)
print('app parcheada ·', len(s.encode()) // 1024, 'KB')
