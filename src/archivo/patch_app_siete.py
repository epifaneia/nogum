# -*- coding: utf-8 -*-
"""Lleva a la app el cuadrante de siete tarjetas, los dos huecos y el vocabulario nuevo."""
import io, os, re
os.chdir(os.path.dirname(os.path.abspath(__file__)))
s = io.open('app4_body.html', encoding='utf-8').read()


def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:70], s.count(a))
    s = s.replace(a, b)


# ---------- 1. tarjetas ----------
i = s.index('var CARDS = {')
j = s.index("var CELL = {")
CARDS = """var CARDS = {
  EPICA:{n:['Épica','Epic'], r:'mejor', tn:6, f:1, c:10, roll:['2d10, quédate el ALTO + bono','2d10, keep the HIGHER + bonus'], fum:['Leído 1 (doble 1)','A read 1 (double 1)'], cri:['Leído 10 (un 10 en cualquiera)','A read 10 (a 10 on either die)']},
  PULP:{n:['Pulp desenfrenado','Unleashed Pulp'], r:'mejor', tn:6, f:2, c:9, p:true, roll:['2d10, quédate el ALTO + bono','2d10, keep the HIGHER + bonus'], fum:['Leído 1–2','A read 1–2'], cri:['Leído 9–10','A read 9–10'], bands:['≤4 fallo · 5–6 éxito con coste · 7+ éxito','≤4 failure · 5–6 success at a cost · 7+ success'], partial:true},
  REAL:{n:['Realista','Realist'], r:'suma', tn:11, f:3, c:19, roll:['SUMA los 2d10 + bono','SUM the 2d10 + bonus'], fum:['Suma 2–3','Sum 2–3'], cri:['Suma 19–20','Sum 19–20']},
  PRIM:{n:['Primera marcha','First Gear'], r:'rojo', tn:6, f:1, c:10, roll:['Solo el dado rojo + bono','Red die only + bonus'], fum:['Leído 1','A read 1'], cri:['Leído 10','A read 10']},
  BOLA:{n:['Bola de nieve','Snowball'], r:'rojo', tn:6, f:2, c:9, p:true, roll:['Solo el dado rojo + bono','Red die only + bonus'], fum:['Leído 1–2','A read 1–2'], cri:['Leído 9–10','A read 9–10'], bands:['≤4 fallo · 5–6 éxito con coste · 7+ éxito','≤4 failure · 5–6 success at a cost · 7+ success'], partial:true},
  ANG:{n:['Angustia','Anguish'], r:'peor', tn:6, f:1, c:10, roll:['2d10, quédate el BAJO + bono','2d10, keep the LOWER + bonus'], fum:['Leído 1 (cualquier 1)','A read 1 (any 1)'], cri:['Leído 10 (doble 10)','A read 10 (double 10)']},
  PES:{n:['Pesadilla','Nightmare'], r:'peor', tn:6, f:2, c:9, p:true, roll:['2d10, quédate el BAJO + bono','2d10, keep the LOWER + bonus'], fum:['Leído 1–2','A read 1–2'], cri:['Leído 9–10','A read 9–10'], bands:['≤4 fallo · 5–6 éxito con coste · 7+ éxito','≤4 failure · 5–6 success at a cost · 7+ success'], partial:true},
  TRAG:{n:['Tragedia (receta)','Tragedy (recipe)'], r:'suma', tn:14, f:3, c:19, roll:['SUMA los 2d10 + bono','SUM the 2d10 + bonus'], fum:['Suma 2–3','Sum 2–3'], cri:['Suma 19–20','Sum 19–20']}
};
"""
s = s[:i] + CARDS + s[j:]

rep("var CELL = {'alto|bajo':'T1','alto|medio':'EPIC','alto|alto':'PULPD','neutro|bajo':'T2','neutro|medio':'T0','neutro|alto':'T3','bajo|bajo':'T6','bajo|medio':'T4','bajo|alto':'NIGHT'};",
    "var CELL = {'alto|bajo':'EPICA','alto|medio':null,'alto|alto':'PULP','neutro|bajo':'REAL','neutro|medio':'PRIM','neutro|alto':'BOLA','bajo|bajo':'ANG','bajo|medio':null,'bajo|alto':'PES'};\n"
    "var HOLE = {'alto|medio':['EPICA','PULP'], 'bajo|medio':['ANG','PES']};")

# modos de Acelerado: la banda pasa al reparto del manual completo
rep("bands:['≤5 fallo · 6–7 parcial · 8+ éxito','≤5 failure · 6–7 partial · 8+ success'], partial:true",
    "bands:['≤4 fallo · 5–6 éxito con coste · 7+ éxito','≤4 failure · 5–6 success at a cost · 7+ success'], partial:true")
rep("agobio:{n:['Modo Agobio','Dread mode'], roll:['El menor de los dos dados + bono','The lower of the two dice + bonus'], fum:['Un 1 en cualquiera','A 1 on either'], cri:['Doble 10','Double 10']",
    "agobio:{n:['Modo Agobio','Dread mode'], r:'peor', tn:6, f:1, c:10, p:true, roll:['El menor de los dos dados + bono','The lower of the two dice + bonus'], fum:['Leído 1 (cualquier 1)','A read 1 (any 1)'], cri:['Leído 10 (doble 10)','A read 10 (double 10)']")
rep("epico:{n:['Modo Épico','Epic mode'], roll:", "epico:{n:['Modo Épico','Epic mode'], r:'mejor', tn:6, f:1, c:10, roll:")
rep("neutro:{n:['Modo Neutro','Neutral mode'], roll:", "neutro:{n:['Modo Neutro','Neutral mode'], r:'rojo', tn:6, f:1, c:10, roll:")

# ---------- 2. huecos ----------
rep("function cardBase(){ var k = CELL[opt() + '|' + caos()]; if (k === 'T3' && M.flavor === 'locura') k = 'T5'; return k; }",
    "function isHole(){ return !isAcc() && CELL[opt() + '|' + caos()] === null; }\n"
    "function holeOpts(){ return HOLE[opt() + '|' + caos()] || null; }\n"
    "function cardBase(){ var k = CELL[opt() + '|' + caos()]; if (k) return k; var o = holeOpts(); return o ? o[M.hueco === 'caos' ? 1 : 0] : 'PRIM'; }")

# ---------- 3. página del hueco en vez de la del sabor ----------
old_flavor_start = "  {sec:2, f:'flavor', when:function(){ return !isAcc() && opt()==='neutro' && caos()==='alto'; }, ask:['¿Cómo se nota el caos?','How does the chaos show?'],"
k = s.index(old_flavor_start)
k2 = s.index("  {sec:3, f:'zoom'", k)
NEW = """  {sec:2, f:'hueco', when:function(){ return isHole(); }, ask:['Esa combinación no tiene tarjeta propia. ¿Cómo quieres que se note?','That combination has no card of its own. How do you want it to show?'],
    hint:['Con un dado plano no hay forma de inclinar el tono sin mover la dificultad, y la dificultad no se toca. Coge la vecina que más te suene.','With a flat die there is no way to tilt the tone without moving the difficulty, and the difficulty is never moved. Take whichever neighbour sounds closest.'],
    opts:[o('prev','Que el mundo se comporte','Let the world behave','La vecina ordenada','The ordered neighbour'), o('caos','Que el mundo haga ruido','Let the world make noise','La vecina caótica: éxito con coste y bandas anchas','The chaotic neighbour: success at a cost and wide bands')],
    tech:function(){ return M.hueco ? t('Tarjeta: ','Card: ') + '<b>' + esc(pick(card().n)) + '</b>' : ''; }},
"""
s = s[:k] + NEW + s[k2:]

# ---------- 4. dados: naturales sobre el valor leído ----------
i = s.index('var READ = {')
j = s.index('function curKey()')
s = s[:i] + s[j:]
rep("""function rollNow(){
  var k = curKey(), R = READ[k], C = card(), r = d10(), b = d10(), nat, fum, cri, use;
  if (R.m === 'red') { nat = r; fum = r <= R.fm; cri = r >= R.cm; use = 'r'; }
  else if (R.m === 'high') { nat = Math.max(r, b); fum = r === 1 && b === 1; cri = r === 10 || b === 10; use = r >= b ? 'r' : 'b'; }
  else if (R.m === 'low') { nat = Math.min(r, b); fum = r === 1 || b === 1; cri = r === 10 && b === 10; use = r <= b ? 'r' : 'b'; }
  else { nat = r + b; fum = nat <= 3; cri = nat >= 19; use = 'both'; }
  var B = diceBonus(), tot = nat + B.tot, tn = C.tn || 6, out;
  if (fum) out = 'fum'; else if (cri) out = 'cri';
  else if (C.partial) out = tot <= 5 ? 'fail' : tot <= 7 ? 'part' : 'ok';
  else out = tot >= tn ? 'ok' : 'fail';
  lastRoll = {m:R.m, r:r, b:b, use:use, nat:nat, bonus:B.tot, tot:tot, tn:tn, out:out, style:S.dice.style, mode:pick(C.n), who:B.c ? (B.c.name || u('pc')) : ''};""",
    """function rollNow(){
  var C = card(), r = d10(), b = d10(), nat, use, m = C.r || 'rojo';
  if (m === 'rojo') { nat = r; use = 'r'; }
  else if (m === 'mejor') { nat = Math.max(r, b); use = r >= b ? 'r' : 'b'; }
  else if (m === 'peor') { nat = Math.min(r, b); use = r <= b ? 'r' : 'b'; }
  else { nat = r + b; use = 'both'; }
  var fum = nat <= (C.f || 1), cri = nat >= (C.c || 10);
  var B = diceBonus(), tot = nat + B.tot, tn = C.tn || 6, out;
  if (fum) out = 'fum'; else if (cri) out = 'cri';
  else if (C.partial) out = tot <= 4 ? 'fail' : tot <= 6 ? 'part' : 'ok';
  else out = tot >= tn ? 'ok' : 'fail';
  lastRoll = {m:m === 'rojo' ? 'red' : m, r:r, b:b, use:use, nat:nat, bonus:B.tot, tot:tot, tn:tn, out:out, style:S.dice.style, mode:pick(C.n), who:B.c ? (B.c.name || u('pc')) : ''};""")
rep("function rollCard(c, bonus){\n  var r = [1 + Math.floor(Math.random()*10), 1 + Math.floor(Math.random()*10)];\n  if (c.read === 'rojo') r[1] = r[0];\n  return outcome(c, r, bonus);\n}",
    "", 0) if False else None

# ---------- 5. vocabulario ----------
rep("esc(t('Disposición','Stance'))", "esc(t('Guardia','Guard'))")
rep("<th>' + esc(t('Malla / efecto','Grid / effect')) + '</th>", "<th>' + esc(t('Rejilla / efecto','Grid / effect')) + '</th>")
s = s.replace("t('Iniciativa: declara disposición (Violencia, Treta, Especialidad)", "t('Iniciativa: declara tu guardia (Violencia, Treta, Especialidad)")
s = s.replace("Etiquetas: Daño 1–3 · Esq Total / Parcial (mín. 1) / Nula / Difícil −2 / Fácil +2 · Abs Total / Máx N / Nula.",
              "Etiquetas: Daño 1–3 · Esq Total / Parcial (mín. 1) / Nula / Difícil −2 / Fácil +2 · Abs Total / Máx N / Nula · Rejilla.")

# estado nuevo
rep("S.m = S.m || {known:null, family:null, world:null, era:null, tech:null, sup:[], xtra:[], edition:null, opt:null, caos:null, flavor:null, zoom:null, estilo:null, grid:null, b0:[], b1:[], b2:[], b3:[]};",
    "S.m = S.m || {known:null, family:null, world:null, era:null, tech:null, sup:[], xtra:[], edition:null, opt:null, caos:null, flavor:null, hueco:null, zoom:null, estilo:null, grid:null, b0:[], b1:[], b2:[], b3:[]};")
# el preset de un mundo conocido que caiga en un hueco coge la vecina ordenada
rep("  M.flavor = p[7] || 'coste';", "  M.flavor = p[7] || 'coste';\n  M.hueco = 'prev';")

io.open('app4_body.html', 'w', encoding='utf-8').write(s)
print('app parcheada ·', len(s.encode()) // 1024, 'KB')
