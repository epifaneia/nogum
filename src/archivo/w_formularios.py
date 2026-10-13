# -*- coding: utf-8 -*-
"""Tres formularios en vez de uno: tono, contexto (recomienda) y equipo (para quien)."""
import io, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
F = 'app4_body.html'
s = io.open(F, encoding='utf-8').read()
fallos = []


def sub(a, b, n=1):
    global s
    c = s.count(a)
    if c != n:
        fallos.append('(%d!=%d) %s' % (c, n, a[:70]))
        return
    s = s.replace(a, b, n)


# ------------------------------------------------------------------ 1. CSS
CSS = """.fitem:hover{border-color:var(--red)}
/* hub de formularios */
.hub{display:grid;grid-template-columns:repeat(auto-fit,minmax(246px,1fr));gap:10px;margin:14px 0}
.hubcard{text-align:left;border:1.5px solid var(--rule);background:var(--paper);border-radius:14px;padding:14px 16px;display:flex;flex-direction:column;gap:6px;min-height:188px}
.hubcard:hover:not(:disabled){border-color:var(--red)}
.hubcard:disabled{opacity:.5;cursor:default}
.hubkick{font:600 10.5px/1 var(--mono);text-transform:uppercase;letter-spacing:.08em;color:var(--ink-3)}
.hubcard b{font:600 21px/1.15 var(--serif)}
.hubdesc{font-size:13.5px;line-height:1.4;color:var(--ink-2)}
.hubstate{font:11.5px/1.4 var(--mono);color:var(--blue)}
.hubgo{margin-top:auto;font:600 12px/1 var(--mono);text-transform:uppercase;letter-spacing:.05em;color:var(--red)}
.ftop{display:flex;align-items:center;gap:12px;margin:0 0 12px;flex-wrap:wrap}
.ftop .kick{font:600 11px/1 var(--mono);text-transform:uppercase;letter-spacing:.08em;color:var(--ink-3);margin:0}
.ftop .mini{flex:none}
/* contexto */
.recrow{border:1px solid var(--rule);border-radius:10px;padding:9px 11px;margin-bottom:7px}
.recrow .why{display:block;font:11.5px/1.45 var(--mono);color:var(--ink-3);margin-top:5px}
.recrow .tip{margin:5px 0 0;font-size:13px;line-height:1.4;color:var(--ink-2)}
.recrow .chip{font-size:14px;padding:5px 12px}
.chip.on{border-color:var(--red);background:var(--red);color:#fff}
.more{margin-top:14px;padding-top:12px;border-top:1px dashed var(--rule)}
/* equipo */
.eqwho{display:grid;gap:8px}
.eqwho button{text-align:left;border:1.5px solid var(--rule);background:var(--ground);border-radius:10px;padding:11px 14px;font-size:16px}
.eqwho button:hover{border-color:var(--red)}
.eqwho small{display:block;font:11.5px/1.4 var(--mono);color:var(--ink-3);margin-top:3px}
.fitem.on{border-color:var(--red);box-shadow:inset 0 0 0 1.5px var(--red)}
.cuenta{width:100%;border-collapse:collapse;font-size:13.5px;margin-top:6px}
.cuenta th{font:600 10.5px/1.4 var(--mono);text-transform:uppercase;letter-spacing:.05em;color:var(--ink-3);text-align:left;border-bottom:1px solid var(--rule);padding:5px 6px}
.cuenta td{border-bottom:1px solid var(--rule-2);padding:6px;vertical-align:top}
.cuenta td.num{text-align:right;font-family:var(--mono)}
.cuenta tr.tot td{border-bottom:none;font-weight:600}
.sem{font-family:var(--mono);font-size:11.5px}
.sem.ok{color:#1b8f45}.sem.mid{color:#b07800}.sem.bad{color:var(--red)}.sem.na{color:var(--ink-3)}
.eqtot{font:12.5px/1.6 var(--mono);color:var(--ink-2);margin:12px 0 0;padding-top:10px;border-top:1px dashed var(--rule)}
.eqtot b{color:var(--blue)}
.eqtot b.over{color:var(--red)}
.eqnote{font-size:13px;line-height:1.45;color:var(--ink-2);margin:10px 0 0}"""
sub('.fitem:hover{border-color:var(--red)}', CSS)

# ------------------------------------------------------- 2. secciones y paginas
sub("var SECTIONS = [['Universo','Universe'],['Edición','Edition'],['Tono','Tone'],['Peligro','Danger'],['Escala','Scale'],['Reglas extra','Extra rules'],['Resumen','Summary']];",
    "var SECTIONS = [['Universo','Universe'],['Edición','Edition'],['Tono','Tone'],['Peligro','Danger'],['Escala','Scale'],['Resumen','Summary']];")

i = s.index("].concat(BAUL_GROUPS.map(function(g, gi){")
j = s.index("})).concat([{sec:6, summary:true}]);") + len("})).concat([{sec:6, summary:true}]);")
s = s[:i] + "].concat([{sec:5, summary:true}]);" + s[j:]

# el resumen: la fila de reglas extra manda al formulario de contexto
sub("if (!isAcc()) rows.push([5, t('Reglas extra','Extra rules'), baul().length ? baul().map(function(k){ return pick(DATA.baul[k]); }).join(', ') : t('Ninguna','None'), t('Baúl de reglas (8.1)','Rules Chest (8.1)')]);",
    "if (!isAcc()) rows.push(['ctx', t('Reglas extra','Extra rules'), baul().length ? baul().map(function(k){ return pick(DATA.baul[k]); }).join(', ') : t('Ninguna','None'), t('Baúl de reglas (8.1) · formulario 2','Rules Chest (8.1) · form 2')]);")
sub("var h = '<div class=\"page\"><p class=\"kick\">' + esc(pick(SECTIONS[6])) + '</p>",
    "var h = '<div class=\"page\"><p class=\"kick\">' + esc(pick(SECTIONS[5])) + '</p>")

# ------------------------------------------------------------------ 3. estado
sub("S.tab = S.tab || 'form';",
    "S.tab = S.tab || 'form';\nif (S.form === undefined) S.form = null;\nS.ctx = S.ctx || {step:0, a:{}, applied:false, more:false};\nif (S.eq === undefined) S.eq = null;")

# ------------------------------------------------------- 4. los tres formularios
NUEVO = r"""
/* ======================= LOS TRES FORMULARIOS ======================= */
/* 1. El tono escribe la mesa. 2. El contexto recomienda las reglas extra.
   3. El equipo escribe en una ficha. Los dos primeros viajan en el Código;
   el tercero no: el equipo es de quien lleva la ficha. */

function hubCard(id, kick, title, desc, state, btn, on){
  return '<button type="button" class="hubcard"' + (on ? ' data-hub="' + id + '"' : ' disabled') + '>' +
    '<span class="hubkick">' + esc(kick) + '</span><b>' + esc(title) + '</b>' +
    '<span class="hubdesc">' + esc(desc) + '</span>' +
    '<span class="hubstate">' + esc(state) + '</span>' +
    '<span class="hubgo">' + esc(on ? btn : t('Todavía no','Not yet')) + '</span></button>';
}
function renderHub(){
  var hecho = M.known !== null, nch = S.chars.length;
  var h = '<div class="wiz"><p class="disclaimer">' + esc(t(
      'Tres formularios. Los dos primeros montan la mesa y viajan en el Código: valen para toda la partida y para todas las fichas. El tercero escribe en una ficha y es de quien la lleva: el equipo no viaja en el Código.',
      'Three forms. The first two set up the table and travel in the Code: they apply to the whole game and every sheet. The third writes on one sheet and belongs to whoever plays it: equipment does not travel in the Code.')) + '</p><div class="hub">';
  h += hubCard('tono', t('1 · La mesa','1 · The table'), t('El tono','Tone'),
    t('Universo, edición, tarjeta de tono, peligro y escala. Lo que decide cómo se tira.',
      'Universe, edition, tone card, danger and scale. What decides how you roll.'),
    hecho ? (worldName() + ' · ' + pick(card().n) + ' · ' + t('Rejilla ','Grid ') + grid()) : t('Sin hacer','Not done yet'),
    hecho ? t('Repasar','Review') : t('Empezar','Start'), true);
  h += hubCard('contexto', t('2 · La mesa','2 · The table'), t('El contexto','Context'),
    t('Siete preguntas sobre vuestra ficción y te recomiendo las reglas extra que la sostienen, con el por qué de cada una.',
      'Seven questions about your fiction and I recommend the extra rules that hold it up, each with its reason.'),
    !hecho ? t('Hace falta el tono primero','Needs the tone first')
           : isAcc() ? t('El Acelerado no usa el Baúl','Accelerated has no Chest')
           : (baul().length + ' ' + t('reglas activas de 16','rules on out of 16')),
    t('Abrir','Open'), hecho && !isAcc());
  h += hubCard('equipo', t('3 · La ficha','3 · The sheet'), t('El equipo','Equipment'),
    t('De compras. Se elige para quién, se busca por lo que hace el objeto, y el coste se descuenta de sus puntos y sus Llaves.',
      'Shopping. Pick who it is for, search by what the item does, and the cost comes off their points and Keys.'),
    !hecho ? t('Hace falta el tono primero','Needs the tone first')
           : !nch ? t('Hace falta una ficha hecha','Needs a finished sheet')
           : (nch + ' ' + t(nch === 1 ? 'ficha' : 'fichas', nch === 1 ? 'sheet' : 'sheets')),
    t('Abrir','Open'), hecho && nch > 0);
  h += '</div>';
  if (hecho && !nch) h += '<p class="hint">' + esc(t('El tercero se abre cuando haya una ficha: ve a la ficha plantilla y pulsa «Crear ficha».','The third one opens once there is a sheet: go to the template sheet and press “Create sheet”.')) + '</p>';
  return h + '</div>';
}

/* ---------------- 2. el contexto ---------------- */
/* cada respuesta trae las reglas del Baúl que la sostienen, y su propia frase
   es el por qué que se le ensena al Director */
var CTXQ = [
 {k:['Los planes','Plans'], q:['¿Cómo se juegan los planes en vuestra mesa?','How are plans played at your table?'], o:[
   ['Se preparan delante de todos, con el reloj corriendo','They are prepared in front of everyone, with the clock ticking',[0]],
   ['Se improvisan, y el pasado se cuenta después','They are improvised, and the past is told afterwards',[1,0]],
   ['No hay planes: esto va de reaccionar','There are no plans: this is about reacting',[]]]},
 {k:['El fallo','Failure'], q:['Cuando algo sale mal, ¿quién paga?','When something goes wrong, who pays?'], o:[
   ['La historia: el reloj de los malos avanza','The story: the villains’ clock advances',[0]],
   ['El plan: tiempo, recursos, posición o fuego amigo','The plan: time, resources, position or friendly fire',[15]],
   ['El cuerpo: se tira en una tabla y queda escrito','The body: you roll on a table and it stays written',[9]]]},
 {k:['Lo de dentro','What is inside'], q:['¿Qué llevan dentro los personajes que no es una herida?','What do the characters carry inside that is not a wound?'], o:[
   ['Una sed, un honor, una reputación: una barra propia','A thirst, an honour, a reputation: a track of its own',[13]],
   ['Gente a la que proteger','People to protect',[14]],
   ['Una muerte ya escrita','A death already written',[5]],
   ['Nada: lo que aprieta viene de fuera','Nothing: what squeezes comes from outside',[]]]},
 {k:['El cuerpo','The body'], q:['¿El cuerpo que tienen es el único?','Is the body they have the only one?'], o:[
   ['No: hay copias de seguridad','No: there are backups',[7]],
   ['No: se cambia de cuerpo como de abrigo','No: bodies change like coats',[6]],
   ['Sí, y por eso da miedo perderlo','Yes, and that is why losing it is frightening',[]]]},
 {k:['El precio','The price'], q:['¿Hay poder que se cobra solo?','Is there power that charges for itself?'], o:[
   ['Sí: el saber prohibido cobra en cordura','Yes: forbidden lore charges in sanity',[2,9]],
   ['Sí: alguien te lo presta y vuelve a cobrarlo','Yes: somebody lends it to you and comes back to collect',[2]],
   ['Sí, pero al revés: aquí lo sobrenatural funciona del revés','Yes, but inverted: here the supernatural works backwards',[4]],
   ['No: el poder es lo que te has ganado','No: power is what you have earned',[]]]},
 {k:['El subidón','The surge'], q:['¿Hay un momento en que un personaje se vuelve otra cosa?','Is there a moment when a character becomes something else?'], o:[
   ['Se transforma, y dura lo que dura la escena','They transform, and it lasts as long as the scene',[10]],
   ['Se mete en una máquina y hereda su escala','They climb into a machine and inherit its scale',[11]],
   ['No se transforma, pero cuando acierta, acierta muy fuerte','No transforming, but when they hit, they hit hard',[3]],
   ['Nada de eso','None of that',[]]]},
 {k:['El sitio','The place'], q:['¿El lugar mismo hace daño?','Does the place itself deal damage?'], o:[
   ['Sí: estar ahí cuesta salud en cada escena','Yes: being there costs health every scene',[12]],
   ['No: el peligro siempre tiene cara','No: danger always has a face',[]]]}
];
function ctxRec(){
  var rec = {}, ord = [];
  CTXQ.forEach(function(q, qi){
    var a = S.ctx.a[qi]; if (a === undefined || a === null) return;
    var op = q.o[a]; if (!op) return;
    op[2].forEach(function(k){ if (!(k in rec)) { rec[k] = t('lo pide tu respuesta: «','your answer asks for it: “') + pick([op[0], op[1]]) + '»'; ord.push(k); } });
  });
  if (M.known && M.world !== null) {
    (KNOWN[M.world].p[6] || []).forEach(function(k){
      if (!(k in rec)) { rec[k] = t('la trae la receta nº ','recipe no. ') + (KNOWN[M.world].r + 1) + t(' de emulación',' brings it along'); ord.push(k); }
    });
  }
  return {map:rec, ord:ord};
}
function ctxChip(k, why){
  var on = baul().indexOf(k) > -1;
  return '<div class="recrow"><button type="button" class="chip' + (on ? ' on' : '') + '" data-ctxk="' + k + '" aria-pressed="' + on + '">' + esc(pick(DATA.baul[k])) + '</button>' +
    '<span class="why">' + esc(why) + '</span><p class="tip">' + esc(pick(BAUL_TIP[k])) + '</p></div>';
}
function renderCtx(){
  var C = S.ctx;
  var h = '<div class="wiz"><div class="ftop"><button type="button" class="mini" data-ctx="exit">← ' + esc(t('Los formularios','The forms')) + '</button><p class="kick">' + esc(t('2 · El contexto · la mesa','2 · Context · the table')) + '</p></div>';
  if (C.step === -1) {
    var pr = (M.known && M.world !== null) ? (KNOWN[M.world].p[6] || []) : [];
    h += '<div class="page"><p class="kick">' + esc(t('Tu receta ya trae una respuesta','Your recipe already has an answer')) + '</p>' +
      '<p class="big">' + esc(worldName()) + '</p>' +
      '<p class="hint">' + esc(pr.length
        ? t('La receta nº ','Recipe no. ') + (KNOWN[M.world].r + 1) + t(' juega con estas reglas extra. Puedes quedarte con ellas y acabar aquí, o contestar siete preguntas sobre vuestra ficción para afinarlas.',' plays with these extra rules. You can keep them and finish here, or answer seven questions about your fiction to fine-tune them.')
        : t('Esta receta no pide ninguna regla extra: se juega con el núcleo. Si quieres añadir alguna, contesta las siete preguntas.','This recipe asks for no extra rules: it plays with the core. If you want to add some, answer the seven questions.')) + '</p>';
    if (pr.length) pr.forEach(function(k){ h += ctxChip(k, t('la trae la receta','the recipe brings it')); });
    h += '<div class="nav"><button type="button" class="btn" data-ctx="exit">' + esc(t('Me vale así','Good as it is')) + '</button>' +
      '<button type="button" class="btn go" data-ctx="go">' + esc(t('Afinar con preguntas','Fine-tune with questions')) + ' →</button></div></div></div>';
    return h;
  }
  if (C.step < CTXQ.length) {
    var q = CTXQ[C.step];
    h += '<div class="steps">' + CTXQ.map(function(x, i){ return '<span class="' + (i < C.step ? 'done' : i === C.step ? 'now' : '') + '">' + esc(pick(x.k)) + '</span>'; }).join('') + '</div>';
    h += '<div class="page"><p class="kick">' + esc(pick(q.k)) + ' · ' + (C.step + 1) + ' / ' + CTXQ.length + '</p>' +
      '<p class="big">' + esc(pick(q.q)) + '</p>' +
      '<p class="hint">' + esc(t('Ninguna respuesta es obligatoria y ninguna fija nada: al final verás lo recomendado y decides tú.','No answer is compulsory and none of them locks anything in: at the end you see the recommendation and you decide.')) + '</p><div class="choices">';
    q.o.forEach(function(op, oi){
      var on = C.a[C.step] === oi;
      h += '<button type="button" class="choice" data-ctxa="' + oi + '" aria-pressed="' + on + '"><span>' + esc(pick([op[0], op[1]])) +
        (op[2].length ? '<small>' + esc(t('activa: ','switches on: ') + op[2].map(function(k){ return pick(DATA.baul[k]); }).join(', ')) + '</small>' : '<small>' + esc(t('no añade ninguna regla','adds no rule')) + '</small>') +
        '</span><span class="mark"></span></button>';
    });
    h += '</div><div class="nav"><button type="button" class="btn" data-ctx="back"' + (C.step === 0 ? ' disabled' : '') + '>← ' + esc(u('back')) + '</button>' +
      '<button type="button" class="btn" data-ctx="skipall">' + esc(t('Ver la recomendación','See the recommendation')) + '</button>' +
      '<button type="button" class="btn go" data-ctx="next">' + esc(u('next')) + ' →</button></div></div></div>';
    return h;
  }
  /* la recomendacion */
  var r = ctxRec(), on = baul();
  h += '<div class="page"><p class="kick">' + esc(t('La recomendación','The recommendation')) + '</p>' +
    '<p class="big">' + esc(r.ord.length ? t('Esto es lo que pide vuestra ficción','This is what your fiction asks for') : t('Vuestra ficción no pide reglas extra','Your fiction asks for no extra rules')) + '</p>' +
    '<p class="hint">' + esc(r.ord.length
      ? t('Ya están activadas. Cada una lleva su por qué: si el por qué no te convence, quítala con un toque.','They are already switched on. Each one carries its reason: if the reason does not convince you, tap it off.')
      : t('Se juega con el núcleo, que es un juego completo. Abajo tienes las dieciséis por si quieres mirar.','You play with the core, which is a complete game. All sixteen are below if you want a look.')) + '</p>';
  r.ord.forEach(function(k){ h += ctxChip(k, r.map[k]); });
  h += '<div class="more"><button type="button" class="tool' + (C.more ? ' on' : '') + '" data-ctx="more">' +
    esc(C.more ? t('Esconder las demás','Hide the rest') : t('Ver las dieciséis','See all sixteen')) + '</button>';
  if (C.more) {
    h += '<p class="hint" style="margin-top:12px">' + esc(t('El Baúl entero (8.1). Nada queda escondido: lo recomendado es un punto de partida, no un límite.','The whole Chest (8.1). Nothing is hidden: the recommendation is a starting point, not a limit.')) + '</p>';
    BAUL_GROUPS.forEach(function(g){
      h += '<div class="rbgrp"><span class="rbgn">' + esc(pick(g.g)) + '</span><div class="chips">';
      g.k.forEach(function(k){ h += '<button type="button" class="chip' + (on.indexOf(k) > -1 ? ' on' : '') + '" data-ctxk="' + k + '" title="' + esc(pick(BAUL_TIP[k])) + '">' + esc(pick(DATA.baul[k])) + '</button>'; });
      h += '</div></div>';
    });
  }
  h += '</div><p class="techline">' + esc(t('Baúl de reglas (8.1): ','Rules Chest (8.1): ')) + '<b>' + baul().length + '</b> ' + esc(t('activadas de 16. Van dentro del Código de la mesa.','on out of 16. They travel inside the table Code.')) + '</p>' +
    '<div class="nav"><button type="button" class="btn" data-ctx="back">← ' + esc(t('Volver a las preguntas','Back to the questions')) + '</button>' +
    '<button type="button" class="btn" data-ctx="reset">' + esc(t('Empezar de nuevo','Start again')) + '</button>' +
    '<button type="button" class="btn go" data-ctx="exit">' + esc(t('Listo','Done')) + '</button></div></div></div>';
  return h;
}

/* ---------------- 3. el equipo ---------------- */
function resBonus(c){
  var b = ambHas(c, 2) ? 0 : -2;
  if (c.dom['2.1']) b = Math.max(b, 1);
  if (c.dis['2.1.3']) b = Math.max(b, 2);
  (c.fir || []).forEach(function(f){ if (f.key === '2.1.3') b = Math.max(b, f.lv); });
  return b;
}
function itemPtsOf(it){ var m = /(\d+)\s*(?:puntos?|points?)/.exec(pick(it.m) || ''); return m ? +m[1] : 0; }
function itemKeysOf(it){ var m = /(\d+)\s*(?:Llaves?|Keys?)/.exec(pick(it.m) || ''); return m ? +m[1] : 0; }
function accSem(c, it){
  var a = accOf(it);
  if (a === 9) return ['na', t('no se compra con dinero','not bought with money')];
  var r = resBonus(c);
  if (r >= a) return ['ok', t('a tu alcance','within reach')];
  if (a - r <= 1) return ['mid', t('con una tirada o un favor','with a roll or a favour')];
  return ['bad', t('fuera de tu alcance aquí','out of reach here')];
}
function eqRef(r){ return r.u + '|' + r.b + '|' + r.i; }
function eqItem(key){
  var p = String(key).split('|');
  var b = DATA.bazar.filter(function(x){ return x.id === p[0]; })[0];
  var it = b && b.blocks[+p[1]] && b.blocks[+p[1]].items[+p[2]];
  return it ? {u:p[0], b:+p[1], i:+p[2], it:it} : null;
}
function eqChar(){ return S.chars.filter(function(x){ return x.id === (S.eq && S.eq.who); })[0]; }
function renderEq(){
  var E = S.eq = S.eq || {who:null, step:0, fstep:0, cat:null, sel:[]};
  var h = '<div class="wiz"><div class="ftop"><button type="button" class="mini" data-eq="exit">← ' + esc(t('Los formularios','The forms')) + '</button><p class="kick">' + esc(t('3 · El equipo · la ficha','3 · Equipment · the sheet')) + '</p></div>';
  /* paso 0: para quien */
  if (!E.who || !eqChar()) {
    h += '<div class="page"><p class="kick">' + esc(t('Lo primero','First things first')) + '</p><p class="big">' + esc(t('¿Para quién es?','Who is it for?')) + '</p>' +
      '<p class="hint">' + esc(t('El equipo no es de la mesa, es de alguien: se paga con sus puntos, sus Llaves y su nivel en Recursos.','Equipment does not belong to the table, it belongs to someone: it is paid with their points, their Keys and their Resources level.')) + '</p><div class="eqwho">';
    S.chars.forEach(function(c, ci){
      var p = cost(c), k = keysUsed(c);
      h += '<button type="button" data-eqwho="' + c.id + '"><b>' + esc(c.name || (u('pc') + ' ' + (ci + 1))) + '</b>' +
        '<small>' + esc(c.concept || t('sin concepto','no concept')) + ' · ' + p + '/' + budget() + ' ' + esc(t('puntos','points')) +
        ' · ' + k + '/' + keysHave(c) + ' ' + esc(t('Llaves','Keys')) + ' · ' + esc(t('Recursos ','Resources ')) + bonusTxt(resBonus(c)) +
        ' · ' + (c.gear || []).length + ' ' + esc(t('objetos','items')) + '</small></button>';
    });
    return h + '</div></div></div>';
  }
  var c = eqChar();
  var who = c.name || (u('pc') + ' ' + (S.chars.indexOf(c) + 1));
  h += '<p class="hint">' + esc(t('De compras para ','Shopping for ') + who) + ' · <button type="button" class="mini" data-eq="who">' + esc(t('cambiar','change')) + '</button></p>';
  /* paso 2: la cuenta */
  if (E.step === 3) {
    var sp = 0, sk = 0, peor = 'ok';
    h += '<div class="page"><p class="kick">' + esc(t('La cuenta','The bill')) + '</p><p class="big">' + esc(t('Tres monedas, y solo dos se restan','Three coins, and only two get subtracted')) + '</p>' +
      '<table class="cuenta"><thead><tr><th>' + esc(t('Objeto','Item')) + '</th><th>' + esc(t('Acceso · lo paga el dinero','Access · money pays it')) + '</th><th class="num">' + esc(t('Puntos','Points')) + '</th><th class="num">' + esc(t('Llaves','Keys')) + '</th></tr></thead><tbody>';
    E.sel.forEach(function(key){
      var r = eqItem(key); if (!r) return;
      var sem = accSem(c, r.it), p = itemPtsOf(r.it), k = itemKeysOf(r.it);
      sp += p; sk += k;
      if (sem[0] === 'bad') peor = 'bad'; else if (sem[0] === 'mid' && peor !== 'bad') peor = 'mid';
      var a = accOf(r.it);
      h += '<tr><td><b>' + esc(pick(r.it.n)) + '</b><br><span class="note">' + esc(uniName(r.u)) + '</span></td>' +
        '<td><span class="sem ' + sem[0] + '">' + (a === 9 ? '—' : 'Acceso ' + a) + ' · ' + esc(sem[1]) + '</span></td>' +
        '<td class="num">' + (p || '—') + '</td><td class="num">' + (k || '—') + '</td></tr>';
    });
    h += '<tr class="tot"><td>' + esc(t('Total','Total')) + '</td><td><span class="sem ' + peor + '">' +
      esc(peor === 'ok' ? t('todo a tu alcance','all within reach') : peor === 'mid' ? t('algo hay que conseguirlo','something has to be obtained') : t('algo está fuera de tu alcance','something is out of reach')) +
      '</span></td><td class="num">' + sp + '</td><td class="num">' + sk + '</td></tr></tbody></table>';
    var pA = cost(c) + sp, kA = keysUsed(c) + sk;
    h += '<p class="eqtot">' + esc(t('Puntos de habilidad: ','Skill points: ')) + '<b class="' + (pA > budget() ? 'over' : '') + '">' + pA + ' / ' + budget() + '</b>' +
      ' · ' + esc(t('Llaves: ','Keys: ')) + '<b class="' + (kA > keysHave(c) ? 'over' : '') + '">' + kA + ' / ' + keysHave(c) + '</b><br>' +
      esc(t('El Acceso no se resta de nada: no es un monedero, es un umbral. Lo mide tu nivel en Recursos (ahora ','Access is not subtracted from anything: it is not a wallet, it is a threshold. Your Resources level measures it (now ')) + bonusTxt(resBonus(c)) + esc(t('), y quien decide si lo consigues es la mesa.','), and the table decides whether you get it.')) + '</p>';
    if (pA > budget() || kA > keysHave(c)) h += '<p class="eqnote">' + esc(t('Te pasas del presupuesto. Puedes añadirlo igual —la ficha lo marca en rojo y lo arregláis en la mesa—, o quitar algo.','You are over budget. You can add it anyway —the sheet flags it in red and you sort it out at the table— or drop something.')) + '</p>';
    h += '<div class="nav"><button type="button" class="btn" data-eq="list">← ' + esc(t('Volver a la lista','Back to the list')) + '</button>' +
      '<button type="button" class="btn" data-eq="more">' + esc(t('Buscar otra cosa','Look for something else')) + '</button>' +
      '<button type="button" class="btn go" data-eq="add">' + esc(t('Añadir a la ficha','Add to the sheet')) + ' →</button></div></div></div>';
    return h;
  }
  /* paso 1: el arbol de busqueda */
  if (!E.cat) {
    var q = FINDQ[E.fstep];
    h += '<div class="page"><p class="kick">' + esc(t('Qué estáis buscando','What you are looking for')) + '</p><p class="big">' + esc(pick(q.q)) + '</p>' +
      '<p class="hint">' + esc(t('No hace falta saber el nombre del objeto: basta con saber qué queréis que haga.','You do not need the item’s name: knowing what you want it to do is enough.')) + '</p><div class="choices">' +
      '<button type="button" class="choice" data-eqf="y"><span>' + esc(t('Sí','Yes')) + '</span><span class="mark"></span></button>' +
      '<button type="button" class="choice" data-eqf="n"><span>' + esc(t('No','No')) + '</span><span class="mark"></span></button></div>';
    if (!arcOpen()) h += '<p class="eqnote">' + esc(t('En este mundo no hay Arcano, así que la magia y los poderes no salen en la lista.','This world has no Arcane, so magic and powers do not appear in the list.')) + '</p>';
    h += '<div class="nav"><button type="button" class="btn" data-eq="fres"' + (E.fstep ? '' : ' disabled') + '>' + esc(t('Empezar de nuevo','Start again')) + '</button>' +
      (E.sel.length ? '<button type="button" class="btn go" data-eq="cuenta">' + esc(t('Ir a la cuenta','Go to the bill')) + ' (' + E.sel.length + ') →</button>' : '<span></span>') +
      '</div></div></div>';
    return h;
  }
  /* paso 2: la lista */
  var list = findItems(E.cat);
  h += '<div class="page"><p class="kick">' + esc(pick(CATN[E.cat])) + ' · ' + list.length + ' ' + esc(t('en tu mesa','on your table')) + '</p>' +
    '<p class="big">' + esc(t('Elige lo que quieras llevarte','Pick whatever you want to take')) + '</p>' +
    '<p class="hint">' + esc(t('Ordenados de lo más fácil de conseguir a lo más difícil. Puedes marcar varios.','Sorted from easiest to hardest to get hold of. You can tick several.')) + '</p><div class="flist">';
  list.forEach(function(r){
    var key = eqRef(r), on = E.sel.indexOf(key) > -1, sem = accSem(c, r.it);
    var p = itemPtsOf(r.it), k = itemKeysOf(r.it);
    h += '<button type="button" class="fitem' + (on ? ' on' : '') + '" data-eqadd="' + esc(key) + '" aria-pressed="' + on + '"><b>' + esc(pick(r.it.n)) + '</b>' +
      '<span>' + esc([pick(r.it.d), pick(r.it.e), pick(r.it.a)].filter(function(x){ return x && x !== '—'; }).join(' · ')) + '</span>' +
      '<em class="sem ' + sem[0] + '">' + esc(sem[1]) + (p ? ' · ' + p + ' ' + esc(t('puntos','pts')) : '') + (k ? ' · ' + k + ' ' + esc(t('Llaves','Keys')) : '') + '</em></button>';
  });
  h += '</div><div class="nav"><button type="button" class="btn" data-eq="fres">← ' + esc(t('Otra búsqueda','Another search')) + '</button>' +
    '<button type="button" class="btn go" data-eq="cuenta"' + (E.sel.length ? '' : ' disabled') + '>' + esc(t('Ir a la cuenta','Go to the bill')) + (E.sel.length ? ' (' + E.sel.length + ')' : '') + ' →</button></div></div></div>';
  return h;
}

function bindHub(){
  var v = $('view');
  v.querySelectorAll('[data-hub]').forEach(function(b){ b.addEventListener('click', function(){
    var k = b.getAttribute('data-hub');
    S.form = k;
    if (k === 'tono') { S.page = 0; S.fix = null; }
    if (k === 'contexto') { S.ctx = {step:(M.known && M.world !== null) ? -1 : 0, a:{}, applied:false, more:false}; }
    if (k === 'equipo') { S.eq = {who:S.chars.length === 1 ? S.chars[0].id : null, step:0, fstep:0, cat:null, sel:[]}; }
    persist(); render(); window.scrollTo(0,0);
  }); });
}
function bindCtx(){
  var v = $('view'), C = S.ctx;
  function recomienda(){
    if (C.applied) return;
    var r = ctxRec();
    r.ord.forEach(function(k){ if (baul().indexOf(k) < 0) toggleBaul(k); });
    C.applied = true;
  }
  v.querySelectorAll('[data-ctxa]').forEach(function(b){ b.addEventListener('click', function(){
    C.a[C.step] = +b.getAttribute('data-ctxa'); C.applied = false;
    persist(); render(true);
    setTimeout(function(){ if (S.form === 'contexto' && C.step < CTXQ.length) { C.step++; if (C.step >= CTXQ.length) recomienda(); persist(); render(); window.scrollTo(0,0); } }, 260);
  }); });
  v.querySelectorAll('[data-ctxk]').forEach(function(b){ b.addEventListener('click', function(){
    toggleBaul(+b.getAttribute('data-ctxk')); C.applied = true; persist(); render(true);
  }); });
  v.querySelectorAll('[data-ctx]').forEach(function(b){ b.addEventListener('click', function(){
    var k = b.getAttribute('data-ctx');
    if (k === 'exit') { S.form = null; }
    else if (k === 'go') { C.step = 0; }
    else if (k === 'next') { C.step++; if (C.step >= CTXQ.length) recomienda(); }
    else if (k === 'back') { C.step = C.step >= CTXQ.length ? CTXQ.length - 1 : Math.max(0, C.step - 1); }
    else if (k === 'skipall') { C.step = CTXQ.length; recomienda(); }
    else if (k === 'reset') { S.ctx = {step:0, a:{}, applied:false, more:false}; }
    else if (k === 'more') { C.more = !C.more; persist(); render(true); return; }
    persist(); render(); window.scrollTo(0,0);
  }); });
}
function bindEq(){
  var v = $('view'), E = S.eq;
  v.querySelectorAll('[data-eqwho]').forEach(function(b){ b.addEventListener('click', function(){
    E.who = b.getAttribute('data-eqwho'); E.step = 1; E.fstep = 0; E.cat = null; E.sel = [];
    persist(); render(); window.scrollTo(0,0);
  }); });
  v.querySelectorAll('[data-eqf]').forEach(function(b){ b.addEventListener('click', function(){
    var q = FINDQ[E.fstep], nx = q[b.getAttribute('data-eqf')];
    if (typeof nx === 'string') { E.cat = nx; E.step = 2; } else { E.fstep = nx; }
    persist(); render(); window.scrollTo(0,0);
  }); });
  v.querySelectorAll('[data-eqadd]').forEach(function(b){ b.addEventListener('click', function(){
    var key = b.getAttribute('data-eqadd'), i = E.sel.indexOf(key);
    if (i > -1) E.sel.splice(i, 1); else E.sel.push(key);
    persist(); render(true);
  }); });
  v.querySelectorAll('[data-eq]').forEach(function(b){ b.addEventListener('click', function(){
    var k = b.getAttribute('data-eq');
    if (k === 'exit') { S.form = null; }
    else if (k === 'who') { E.who = null; E.step = 0; }
    else if (k === 'fres') { E.fstep = 0; E.cat = null; E.step = 1; }
    else if (k === 'more') { E.fstep = 0; E.cat = null; E.step = 1; }
    else if (k === 'list') { E.step = 2; }
    else if (k === 'cuenta') { E.step = 3; }
    else if (k === 'add') {
      var c = eqChar();
      if (c) { E.sel.forEach(function(key){ var r = eqItem(key); if (r) c.gear.push({u:r.u, b:r.b, i:r.i}); }); S.tab = c.id; }
      S.form = null; S.eq = null;
    }
    persist(); render(); window.scrollTo(0,0);
  }); });
}

"""
sub('/* ======================= REMINDERS ======================= */', NUEVO + '/* ======================= REMINDERS ======================= */')

# ------------------------------------------------- 5. renderForm como repartidor
sub("""function renderForm(){
  var h = '<p class="disclaimer">' + esc(u('disclaimer')) + '</p><div class="wiz">';""",
    """function renderForm(){
  if (S.form === 'contexto') return renderCtx();
  if (S.form === 'equipo') return renderEq();
  if (S.form !== 'tono') return renderHub();
  var h = '<div class="ftop"><button type="button" class="mini" data-ctx="exit">← ' + esc(t('Los formularios','The forms')) + '</button><p class="kick">' + esc(t('1 · El tono · la mesa','1 · Tone · the table')) + '</p></div><p class="disclaimer">' + esc(u('disclaimer')) + '</p><div class="wiz">';""")

# bindForm reparte
sub("""function bindForm(){
  var v = $('view');""",
    """function bindForm(){
  if (S.form === 'contexto') return bindCtx();
  if (S.form === 'equipo') return bindEq();
  if (S.form !== 'tono') return bindHub();
  var v = $('view');""")

# el boton de salir del formulario de tono
sub("""  var x;
  if ((x = $('talkGo')))""",
    """  v.querySelectorAll('[data-ctx]').forEach(function(b){ b.addEventListener('click', function(){ if (b.getAttribute('data-ctx') === 'exit') { S.form = null; persist(); render(); window.scrollTo(0,0); } }); });
  var x;
  if ((x = $('talkGo')))""")

# data-fix: la fila de reglas extra abre el formulario 2
sub("""    var sec = +b.getAttribute('data-fix'); S.locked = false; S.fix = sec;""",
    """    var raw = b.getAttribute('data-fix');
    if (raw === 'ctx') { S.form = 'contexto'; S.ctx = {step:0, a:{}, applied:true, more:true}; persist(); render(); window.scrollTo(0,0); return; }
    var sec = +raw; S.locked = false; S.fix = sec; S.form = 'tono';""")

# ------------------------------------------- 6. la barra: recomiendame, y pestanas
sub("""  var h = '<div class="rbpanel"><p class="rbp-h">' + esc(t('Baúl de reglas (8.1)','Rules Chest (8.1)')) + '</p>';""",
    """  var h = '<div class="rbpanel"><p class="rbp-h">' + esc(t('Baúl de reglas (8.1)','Rules Chest (8.1)')) +
    '<button type="button" class="mini" data-rbb="ctxgo">' + esc(t('¿No sabes cuáles? Recomiéndame','Not sure which? Recommend me some')) + '</button></p>';""")
sub("""  else if (k === 'baulk') { toggleBaul(+b.getAttribute('data-k')); }""",
    """  else if (k === 'baulk') { toggleBaul(+b.getAttribute('data-k')); }
  else if (k === 'ctxgo') { S.tab = 'form'; S.form = 'contexto'; S.ctx = {step:(M.known && M.world !== null) ? -1 : 0, a:{}, applied:false, more:false}; rbOpen = null; rbMsg = ''; persist(); render(); window.scrollTo(0,0); return; }""")

# la pestana vuelve al hub
sub("""$('tabs').addEventListener('click', function(e){ var b = e.target.closest('[data-tab]'); if (b) { S.tab = b.getAttribute('data-tab'); persist(); render(); window.scrollTo(0,0); } });""",
    """$('tabs').addEventListener('click', function(e){ var b = e.target.closest('[data-tab]'); if (b) { var nt = b.getAttribute('data-tab'); if (nt === 'form' && S.tab !== 'form') S.form = null; S.tab = nt; persist(); render(); window.scrollTo(0,0); } });""")

# la barra de reglas, al mandar al formulario de universo propio
sub("""      if (M.tech === null || M.tech === undefined) { S.locked = false; S.fix = 0; S.tab = 'form';""",
    """      if (M.tech === null || M.tech === undefined) { S.locked = false; S.fix = 0; S.tab = 'form'; S.form = 'tono';""")

# ------------------------------------------------------------- 7. textos de la UI
sub("sub:['App del director','GM app'], form:['Formulario','Form'],",
    "sub:['App del director','GM app'], form:['Formularios','Forms'],")
sub("""  disclaimer:['La app aplica un tono y un set de reglas a la partida completa. Puedes repetir el formulario siempre que quieras cambiar de tono: para una sesión nueva, una escena nueva o incluso a mitad de escena. Las fichas se actualizan solas.','The app applies one tone and one rule set to the whole game. You can run the form again whenever you want to change tone: for a new session, a new scene or even mid-scene. Sheets update on their own.']""",
    """  disclaimer:['Este formulario aplica un tono y una escala a la partida completa. Puedes repetirlo siempre que quieras cambiar de tono: para una sesión nueva, una escena nueva o incluso a mitad de escena. Las fichas se actualizan solas, porque ninguna tirada pasa nunca de +4.','This form applies one tone and one scale to the whole game. You can run it again whenever you want to change tone: for a new session, a new scene or even mid-scene. Sheets update on their own, because no roll ever goes above +4.']""")

# el boton de la ficha plantilla lleva al equipo cuando ya hay ficha
sub("""if (cb) cb.addEventListener('click', function(){ var c = newChar(); S.chars.push(c); S.tab = c.id; persist(); render(); window.scrollTo(0,0); });""",
    """if (cb) cb.addEventListener('click', function(){ var c = newChar(); S.chars.push(c); S.tab = c.id; S.form = null; persist(); render(); window.scrollTo(0,0); });""")

if fallos:
    print('FALLOS:')
    for f in fallos:
        print('  ' + f)
    sys.exit(1)
io.open(F, 'w', encoding='utf-8').write(s)
print('app4_body.html: tres formularios escritos')
