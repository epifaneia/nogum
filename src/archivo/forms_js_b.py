# -*- coding: utf-8 -*-
"""El repartidor y el renderizador de pasos."""

BLOQUE_B = r"""/* ======================= EL REPARTIDOR Y LOS PASOS ======================= */
var FORMS = [
 {id:'tono', num:'1', cap:['La mesa','The table'], n:['El tono','Tone'],
  d:['Caos, optimismo y cuánto aguanta un cuerpo. Sale de situaciones, no de preguntas técnicas: a cada una le dices cuánto te suena.',
     'Chaos, optimism and how much a body can take. It comes out of situations, not technical questions: you say how much each one sounds like your table.']},
 {id:'uni', num:'2', cap:['La mesa','The table'], n:['El universo','The universe'],
  d:['Qué hay en vuestro mundo y de qué tamaño son las hazañas. Si tenéis un universo conocido en la cabeza, se acaba en dos toques.',
     'What is in your world and how big the deeds are. If you have a well-known universe in mind, it is over in two taps.']},
 {id:'baul', num:'3', cap:['La mesa','The table'], n:['El Baúl','The Chest'],
  d:['Las dieciséis reglas opcionales. Empieza delimitando: si no te gusta la chicha, desaparecen de un plumazo las que piden llevar números.',
     'The sixteen optional rules. It starts by setting boundaries: if you do not like crunch, the ones that make you track numbers vanish at a stroke.']},
 {id:'equipo', num:'4', cap:['La ficha','The sheet'], n:['El equipo','Equipment'],
  d:['De compras. Se elige para quién, se busca por lo que hace el objeto, y el coste se descuenta de sus puntos y sus Llaves.',
     'Shopping. Pick who it is for, search by what the item does, and the cost comes off their points and Keys.']}
];
function formEstado(id){
  var hecho = M.known !== null;
  if (id === 'tono') return hecho ? [pick(card().n) + ' · ' + pick(ZOOM[zoomK()].n) + (estilo() ? ' · Estilo' : ''), true]
                                  : [t('Sin contestar','Not answered yet'), true];
  if (id === 'uni') return hecho ? [worldName() + ' · ' + t('Rejilla ','Grid ') + grid(), true]
                                 : [t('Sin contestar','Not answered yet'), true];
  if (id === 'baul') return isAcc() ? [t('El Acelerado no usa el Baúl','Accelerated has no Chest'), false]
    : !hecho ? [t('Hace falta el universo','Needs the universe first'), false]
    : [baul().length + ' ' + t('de 16 activas','of 16 on'), true];
  return !hecho ? [t('Hace falta el universo','Needs the universe first'), false]
    : !S.chars.length ? [t('Hace falta una ficha hecha','Needs a finished sheet'), false]
    : [S.chars.length + ' ' + t(S.chars.length === 1 ? 'ficha' : 'fichas', S.chars.length === 1 ? 'sheet' : 'sheets'), true];
}
function renderHub(){
  var h = '<div class="wiz"><p class="disclaimer">' + esc(t(
      'Cuatro formularios y ninguno obligatorio. Los tres primeros montan la mesa y viajan en el Código: valen para la partida entera y para todas las fichas. El cuarto escribe en una ficha y no viaja, porque el equipo es de quien lo lleva.',
      'Four forms and none of them compulsory. The first three set up the table and travel in the Code: they apply to the whole game and every sheet. The fourth writes on one sheet and does not travel, because equipment belongs to whoever carries it.')) + '</p>';
  h += '<div class="hubedi"><span>' + esc(t('¿Cuánto juego queréis?','How much game do you want?')) + '</span>' +
    '<button type="button" class="tool' + (!isAcc() ? ' on' : '') + '" data-edi="completo">' + esc(t('NOGUM completo','Complete NOGUM')) + '</button>' +
    '<button type="button" class="tool' + (isAcc() ? ' on' : '') + '" data-edi="acelerado">NOGUM Acelerado</button>' +
    '<span class="note">' + esc(isAcc()
      ? t('Tres modos de tono, dificultad fija y nueve casillas de vida. Sin Baúl y sin vida a medida.','Three tone modes, fixed difficulty and nine health boxes. No Chest and no tailored health.')
      : t('Tarjetas de tono, letalidad a medida y las dieciséis reglas del Baúl.','Tone cards, tailored lethality and the sixteen rules of the Chest.')) + '</span></div>';
  h += '<div class="hub">';
  FORMS.forEach(function(f){
    var e = formEstado(f.id);
    h += '<button type="button" class="hubcard"' + (e[1] ? ' data-hub="' + f.id + '"' : ' disabled') + '>' +
      '<span class="hubkick">' + esc(f.num + ' · ' + pick(f.cap)) + '</span><b>' + esc(pick(f.n)) + '</b>' +
      '<span class="hubdesc">' + esc(pick(f.d)) + '</span>' +
      '<span class="hubstate">' + esc(e[0]) + '</span>' +
      '<span class="hubgo">' + esc(e[1] ? t('Abrir','Open') : t('Todavía no','Not yet')) + '</span></button>';
  });
  h += '</div>';
  if (M.known !== null) {
    h += '<div class="page" style="margin-top:14px"><p class="kick">' + esc(t('La mesa, ahora mismo','The table, right now')) + '</p><table class="summary">';
    resumenFilas().forEach(function(r){
      h += '<tr><td>' + esc(r[1]) + '</td><td>' + esc(r[2]) + '<span class="tech">' + esc(r[3]) + '</span></td>' +
        '<td class="chg">' + (r[0] ? '<button type="button" class="mini" data-hub="' + r[0] + '">' + esc(t('Cambiar','Change')) + '</button>' : '') + '</td></tr>';
    });
    h += '</table><div class="cta"><button type="button" class="btn red" data-gotpl="1">' + esc(t('Ficha plantilla','Template sheet')) + ' →</button></div></div>';
  } else {
    h += '<p class="hint">' + esc(t('Empieza por donde quieras. Con el universo ya se puede imprimir una ficha; el resto afina cómo se juega.','Start wherever you like. With the universe alone you can already print a sheet; the rest fine-tunes how it plays.')) + '</p>';
  }
  if (M.known !== null && !S.chars.length) h += '<p class="hint">' + esc(t('El cuarto se abre cuando haya una ficha: ve a la ficha plantilla y pulsa «Crear ficha».','The fourth one opens once there is a sheet: go to the template sheet and press “Create sheet”.')) + '</p>';
  return h + '</div>';
}
function resumenFilas(){
  var f = [];
  f.push(['uni', t('Universo','Universe'), worldName(), t('Objetos: ','Items: ') + universes().map(uniName).join(', ')]);
  f.push([null, t('Edición','Edition'), isAcc() ? t('A jugar ya','Play now') : t('Todas las herramientas','Every tool'), isAcc() ? 'NOGUM Acelerado' : t('NOGUM completo','Complete NOGUM')]);
  f.push(['tono', t('Tono','Tone'), {alto:t('El universo está de nuestra parte','The universe is on our side'), neutro:t('El universo es justo','The universe is fair'), bajo:t('El universo nos pone a prueba','The universe puts us to the test')}[opt()] + ' · ' + {bajo:t('mundo de reloj','clockwork world'), medio:t('mundo de película','film-like world'), alto:t('universo caótico','chaotic universe')}[caos()], pick(card().n)]);
  f.push(['tono', t('Peligro','Danger'), (isAcc() ? t('Vida fija','Fixed health') : pick(ZOOM[zoomK()].n)) + ' · ' + (estilo() ? t('con floritura','with flourish') : t('sin floritura','no flourish')), t('Vida fractal · Estilo ','Fractal Health · Style ') + (estilo() ? t('sí','on') : t('no','off'))]);
  f.push(['uni', t('Escala','Scale'), pick(GRIDN[grid()]), t('Rejilla nivel ','Grid level ') + grid()]);
  if (!isAcc()) f.push(['baul', t('Reglas extra','Extra rules'), baul().length ? baul().map(function(k){ return pick(DATA.baul[k]); }).join(', ') : t('Ninguna','None'), t('Baúl de reglas (8.1)','Rules Chest (8.1)')]);
  return f;
}

/* --------------------------- los pasos de cada formulario --------------------------- */
function pasosTono(){
  var p = [];
  S_TONO.forEach(function(sec){
    if (isAcc() && (sec.id === 'vida' || sec.id === 'estilo')) return;
    for (var i = 0; i < 3; i++) p.push({t:'q', s:sec, i:i});
    p.push({t:'res', s:sec});
  });
  p.push({t:'fin'});
  return p;
}
function pasosUni(){
  var p = [{t:'pick', k:'known'}];
  if (M.known === true) {
    p.push({t:'pick', k:'family'});
    if (M.family) p.push({t:'pick', k:'world'});
    if (M.world !== null && M.world !== undefined) p.push({t:'fin'});
    return p;
  }
  if (M.known !== false) return p;
  S_UNI.forEach(function(sec){
    if (sec.id === 'magia') p.push({t:'gate', g:'sobr', q:G_SOBR});
    if (sec.sup && !uniSobrOn()) return;
    for (var i = 0; i < 3; i++) p.push({t:'q', s:sec, i:i});
    p.push({t:'res', s:sec});
  });
  p.push({t:'one', g:'toon', q:Q_TOON});
  p.push({t:'fin'});
  return p;
}
function pasosBaul(){
  var p = [{t:'gate', g:'chicha', q:G_CHICHA}];
  if (!sc1('baul','chicha')) return p;
  if (!baulChicha()) {
    p.push({t:'gate', g:'insiste', q:G_INSIST});
    if (!sc1('baul','insiste')) return p;
    if (baulCero()) { p.push({t:'cero'}); return p; }
  }
  S_BAUL.forEach(function(sec, gi){
    for (var i = 0; i < 3; i++) p.push({t:'q', s:sec, i:i});
    p.push({t:'res', s:sec, gi:gi});
  });
  p.push({t:'fin'});
  return p;
}
function pasos(fid){ return fid === 'tono' ? pasosTono() : fid === 'uni' ? pasosUni() : pasosBaul(); }
function aplica(fid){ if (fid === 'tono') aplicaTono(); else if (fid === 'uni') aplicaUni(); else if (fid === 'baul') aplicaBaul(); }
function sectores(fid){ return fid === 'tono' ? S_TONO : fid === 'uni' ? S_UNI : S_BAUL; }

/* --------------------------- el renderizador --------------------------- */
function escala(q, cur){
  var h = '<p class="vign">' + esc(pick(q.v)) + '</p><div class="escala">';
  h += '<p class="polo">' + esc(pick(q.a)) + '</p><div class="pasos">';
  for (var n = 1; n <= 5; n++) h += '<button type="button" class="paso p' + n + (cur === n ? ' on' : '') +
    '" data-sc="' + n + '" aria-pressed="' + (cur === n) + '" aria-label="' + n + ' / 5"><i></i></button>';
  h += '</div><p class="polo b">' + esc(pick(q.b)) + '</p></div>';
  return h;
}
function tiraPasos(fid, ps, i){
  var sec = sectores(fid), vistos = [], aqui = -1;
  ps.forEach(function(p, pi){
    if (p.t === 'q' || p.t === 'res') {
      if (vistos[vistos.length - 1] !== p.s) vistos.push(p.s);
      if (pi <= i && vistos.length - 1 > aqui) aqui = vistos.length - 1;
    }
  });
  if (vistos.length < 2) return '';
  return '<div class="steps">' + vistos.map(function(s, k){
    return '<span class="' + (k < aqui ? 'done' : k === aqui ? 'now' : '') + '">' + esc(pick(s.k)) + '</span>';
  }).join('') + '</div>';
}
function renderPasos(fid){
  var F = FORMS.filter(function(x){ return x.id === fid; })[0];
  var ps = pasos(fid), i = S.st[fid] || 0;
  if (i >= ps.length) i = ps.length - 1;
  if (i < 0) i = 0;
  S.st[fid] = i;
  var p = ps[i];
  var h = '<div class="wiz"><div class="ftop"><button type="button" class="mini" data-fsal="1">← ' + esc(t('Los formularios','The forms')) + '</button>' +
    '<p class="kick">' + esc(F.num + ' · ' + pick(F.n) + ' · ' + pick(F.cap)) + '</p></div>';
  h += tiraPasos(fid, ps, i);
  h += '<div class="page">';
  if (p.t === 'q') {
    var tot = 0, pos = 0;
    ps.forEach(function(x){ if (x.t === 'q' && x.s === p.s) { tot++; if (x.i <= p.i) pos++; } });
    h += '<p class="kick">' + esc(pick(p.s.k)) + ' · ' + pos + ' / ' + tot + '</p>';
    h += escala(p.s.qs[p.i], ans(fid, p.s.id)[p.i] || 0);
  } else if (p.t === 'gate' || p.t === 'one') {
    h += '<p class="kick">' + esc(p.g === 'toon' ? t('La última','The last one') : t('Delimitando','Setting the boundaries')) + '</p>';
    h += escala(p.q, sc1(fid, p.g));
  } else if (p.t === 'res') {
    var r = p.gi !== undefined ? resBaul(p.gi) : fid === 'uni' ? resUni(p.s) : {t:RES_TONO[p.s.id][banda3(sc(fid, p.s.id))][0], d:RES_TONO[p.s.id][banda3(sc(fid, p.s.id))][1]};
    h += '<p class="kick">' + esc(pick(p.s.k)) + '</p><p class="big">' + esc(pick(r.t)) + '</p>' +
      '<p class="hint">' + esc(pick(r.d)) + '</p>' +
      '<p class="eqnote">' + esc(t('Si no es eso, vuelve atrás y mueve cualquiera de las tres. Se puede cambiar luego en la barra de la ficha.','If that is not it, go back and move any of the three. You can also change it later on the sheet bar.')) + '</p>';
  } else if (p.t === 'cero') {
    h += '<p class="kick">' + esc(t('Delimitado','Boundaries set')) + '</p><p class="big">' + esc(t('Cero reglas extra','No extra rules')) + '</p>' +
      '<p class="hint">' + esc(t('El núcleo de NOGUM es un juego completo: tono, Rejilla, vida fractal, equipo, Llaves y el menú de costes. El Baúl es lo que se añade cuando una partida concreta lo pide, y la vuestra no lo pide.','The core of NOGUM is a complete game: tone, Grid, Fractal Health, equipment, Keys and the menu of costs. The Chest is what you add when a particular game asks for it, and yours does not.')) + '</p>';
  } else if (p.t === 'pick') {
    h += renderPick(p.k);
  } else {
    h += renderFin(fid);
  }
  h += '</div>';
  var ult = i >= ps.length - 1;
  h += '<div class="nav"><button type="button" class="btn" data-fat="1"' + (i === 0 ? ' disabled' : '') + '>← ' + esc(u('back')) + '</button>' +
    (p.t === 'fin' ? '' : '<button type="button" class="btn" data-fsal="1">' + esc(t('Dejarlo aquí','Leave it here')) + '</button>') +
    (ult ? '<button type="button" class="btn go" data-fsal="1">' + esc(t('Listo','Done')) + '</button>'
         : '<button type="button" class="btn go" data-fsig="1"' + (pasoListo(fid, p) ? '' : ' disabled') + '>' + esc(u('next')) + ' →</button>') +
    '</div></div>';
  return h;
}
function pasoListo(fid, p){
  if (p.t === 'q') return !!ans(fid, p.s.id)[p.i];
  if (p.t === 'gate' || p.t === 'one') return !!sc1(fid, p.g);
  if (p.t === 'pick') return p.k === 'known' ? M.known !== null : p.k === 'family' ? !!M.family : (M.world !== null && M.world !== undefined);
  return true;
}
function renderPick(k){
  var h = '';
  if (k === 'known') {
    h += '<p class="kick">' + esc(t('El atajo','The shortcut')) + '</p><p class="big">' + esc(t('¿Tenéis un universo conocido en la cabeza?','Do you have a well-known universe in mind?')) + '</p>' +
      '<p class="hint">' + esc(t('Películas, novelas o juegos que todo el mundo reconoce. Si lo hay, la app aplica su receta de emulación entera y te ahorras veinte preguntas.','Films, novels or games everyone recognises. If there is one, the app applies its whole emulation recipe and saves you twenty questions.')) + '</p><div class="choices">' +
      '<button type="button" class="choice" data-pk="known|1" aria-pressed="' + (M.known === true) + '"><span>' + esc(t('Sí, uno conocido','Yes, a well-known one')) + '<small>' + esc(t('Elegimos entre veinte mundos','We pick from twenty worlds')) + '</small></span><span class="mark"></span></button>' +
      '<button type="button" class="choice" data-pk="known|0" aria-pressed="' + (M.known === false) + '"><span>' + esc(t('No, uno nuestro','No, one of our own')) + '<small>' + esc(t('Lo construimos con situaciones','We build it out of situations')) + '</small></span><span class="mark"></span></button></div>' +
      '<div class="talkentry"><span>' + esc(t('¿Prefieres contarlo a tu manera?','Would you rather describe it your way?')) + '</span><button type="button" class="btn" id="talkGo">' + esc(t('Cuéntame tu universo','Tell me your universe')) + '</button></div>';
  } else if (k === 'family') {
    h += '<p class="kick">' + esc(t('El atajo','The shortcut')) + '</p><p class="big">' + esc(t('¿Qué clase de historia?','What kind of story?')) + '</p><div class="choices">';
    FAMILIES.forEach(function(fm){
      h += '<button type="button" class="choice" data-pk="family|' + fm.id + '" aria-pressed="' + (M.family === fm.id) + '"><span>' + esc(pick(fm.n)) + '<small>' + esc(pick(fm.s)) + '</small></span><span class="mark"></span></button>';
    });
    h += '</div>';
  } else {
    var fm = FAMILIES.filter(function(x){ return x.id === M.family; })[0];
    h += '<p class="kick">' + esc(t('El atajo','The shortcut')) + '</p><p class="big">' + esc(t('¿Cuál de estos mundos?','Which of these worlds?')) + '</p><div class="choices">';
    (fm ? fm.k : []).forEach(function(ix){
      var kk = KNOWN[ix];
      h += '<button type="button" class="choice" data-pk="world|' + ix + '" aria-pressed="' + (M.world === ix) + '"><span>' + esc(pick(kk.n)) +
        '<small>' + esc(pick(kk.h) + ' · ' + DATA.recipes[kk.r][L()].replace(/^\d+\.\s*/, '')) + '</small></span><span class="mark"></span></button>';
    });
    h += '</div><p class="eqnote">' + esc(t('Elegir un mundo aplica su receta entera: tono, vida, escala, Estilo, reglas del Baúl y las secciones del Bazar que encajan. Todo se puede retocar después.','Picking a world applies its whole recipe: tone, health, scale, Style, Chest rules and the matching Bazaar sections. Everything can be tweaked afterwards.')) + '</p>';
  }
  return h;
}
function renderFin(fid){
  var h = '<p class="kick">' + esc(t('Hecho','Done')) + '</p><p class="big">' + esc(t('Esto es lo que has dicho','This is what you said')) + '</p><table class="summary">';
  if (fid === 'tono') {
    S_TONO.forEach(function(s){
      if (isAcc() && (s.id === 'vida' || s.id === 'estilo')) return;
      var r = RES_TONO[s.id][banda3(sc('tono', s.id))];
      h += '<tr><td>' + esc(pick(s.k)) + '</td><td>' + esc(pick(r[0])) + '<span class="tech">' + esc(pick(r[1])) + '</span></td></tr>';
    });
    h += '<tr><td>' + esc(t('La tarjeta','The card')) + '</td><td>' + esc(pick(card().n)) + '<span class="tech">' + esc(pick(card().roll)) + ' · TN ' + (card().tn || 6) + '</span></td></tr>';
  } else if (fid === 'uni') {
    h += '<tr><td>' + esc(t('Mundo','World')) + '</td><td>' + esc(worldName()) + '<span class="tech">' + esc(universes().map(uniName).join(', ')) + '</span></td></tr>';
    h += '<tr><td>' + esc(t('Escala','Scale')) + '</td><td>' + esc(pick(GRIDN[grid()])) + '<span class="tech">' + esc(t('Rejilla nivel ','Grid level ') + grid()) + '</span></td></tr>';
    h += '<tr><td>' + esc(t('Arcano','Arcane')) + '</td><td>' + esc(arcOpen() ? t('Sí: quinta barra y quinto ámbito','Yes: fifth track and fifth sphere') : t('No: cuatro ámbitos','No: four spheres')) + '<span class="tech">' + budget() + esc(t(' puntos de habilidad',' skill points')) + '</span></td></tr>';
  } else {
    var on = baul();
    h += '<tr><td>' + esc(t('Reglas activas','Rules on')) + '</td><td>' + esc(on.length ? on.map(function(k){ return pick(DATA.baul[k]); }).join(', ') : t('Ninguna','None')) + '<span class="tech">' + on.length + esc(t(' de 16',' of 16')) + '</span></td></tr>';
  }
  h += '</table><p class="eqnote">' + esc(t('Todo esto va dentro del Código de la mesa y se puede cambiar a mano en la barra que hay encima de cada ficha.','All of this goes inside the table Code and can be changed by hand on the bar above every sheet.')) + '</p>';
  h += '<div class="aiask"><button type="button" class="tool" data-ia="' + fid + '">' + esc(t('Léete mis respuestas y dime qué mesa es esta','Read my answers and tell me what table this is')) + '</button>' +
    '<span class="note">' + esc(t('Lee todo lo que has contestado y busca contradicciones. Tarda unos segundos.','It reads everything you answered and looks for contradictions. Takes a few seconds.')) + '</span></div>';
  if (S.ia && S.ia[fid]) h += '<div class="iabox">' + esc(S.ia[fid]) + '</div>';
  return h;
}
function bindPasos(fid){
  var v = $('view'), ps = pasos(fid), p = ps[S.st[fid] || 0];
  function avanza(){ S.st[fid] = Math.min((S.st[fid] || 0) + 1, pasos(fid).length - 1); persist(); render(); window.scrollTo(0, 0); }
  v.querySelectorAll('[data-sc]').forEach(function(b){ b.addEventListener('click', function(){
    var n = +b.getAttribute('data-sc');
    if (p.t === 'q') setAns(fid, p.s.id, p.i, n); else { S.q[fid] = S.q[fid] || {}; S.q[fid][p.g] = [n]; }
    aplica(fid); persist(); render(true);
    setTimeout(function(){ if (S.form === fid) avanza(); }, 300);
  }); });
  v.querySelectorAll('[data-pk]').forEach(function(b){ b.addEventListener('click', function(){
    var x = b.getAttribute('data-pk').split('|');
    if (x[0] === 'known') { M.known = x[1] === '1'; M.family = null; M.world = null; M.unis = null; if (!M.known) aplicaUni(); }
    else if (x[0] === 'family') { M.family = x[1]; M.world = null; }
    else { applyPreset(+x[1]); }
    persist(); render(true);
    setTimeout(function(){ if (S.form === fid) avanza(); }, 300);
  }); });
  v.querySelectorAll('[data-fsig]').forEach(function(b){ b.addEventListener('click', avanza); });
  v.querySelectorAll('[data-fat]').forEach(function(b){ b.addEventListener('click', function(){ S.st[fid] = Math.max(0, (S.st[fid] || 0) - 1); persist(); render(); window.scrollTo(0, 0); }); });
  v.querySelectorAll('[data-fsal]').forEach(function(b){ b.addEventListener('click', function(){ aplica(fid); S.form = null; persist(); render(); window.scrollTo(0, 0); }); });
  v.querySelectorAll('[data-ia]').forEach(function(b){ b.addEventListener('click', function(){ pideLectura(b.getAttribute('data-ia'), b); }); });
  bindTalk();
  var g = $('talkGo');
  if (g) g.addEventListener('click', function(){ S.talk.on = true; persist(); render(); window.scrollTo(0, 0); });
}

/* --------------------------- la lectura del modelo --------------------------- */
function respuestasTexto(fid){
  var out = [];
  sectores(fid).forEach(function(s){
    var a = ans(fid, s.id); if (!a.length) return;
    s.qs.forEach(function(q, i){
      if (!a[i]) return;
      out.push('- [' + s.k[0] + '] «' + q.v[0] + '» → ' + a[i] + '/5 (1 = «' + q.a[0] + '», 5 = «' + q.b[0] + '»)');
    });
  });
  if (fid === 'baul') {
    [['chicha', G_CHICHA], ['insiste', G_INSIST]].forEach(function(x){
      var n = sc1('baul', x[0]); if (n) out.push('- [delimitar] «' + x[1].v[0] + '» → ' + n + '/5');
    });
  }
  if (fid === 'uni') {
    var n = sc1('uni','sobr'); if (n) out.push('- [delimitar] «' + G_SOBR.v[0] + '» → ' + n + '/5');
    var tn = sc1('uni','toon'); if (tn) out.push('- [comedia] «' + Q_TOON.v[0] + '» → ' + tn + '/5');
  }
  return out.join('\n');
}
function resultadoTexto(fid){
  if (fid === 'tono') return 'Tarjeta: ' + card().n[0] + '. Optimismo: ' + opt() + '. Caos: ' + caos() + '. Vida fractal: ' + ZOOM[zoomK()].n[0] + '. Estilo: ' + (estilo() ? 'sí' : 'no') + '.';
  if (fid === 'uni') return 'Mundo: ' + worldName() + '. Secciones del Bazar: ' + universes().map(uniName).join(', ') + '. Rejilla inicial: ' + grid() + '. Arcano: ' + (arcOpen() ? 'sí' : 'no') + '.';
  return 'Reglas activas: ' + (baul().length ? baul().map(function(k){ return DATA.baul[k][0]; }).join(', ') : 'ninguna') + '.';
}
function pideLectura(fid, btn) {
  S.ia = S.ia || {};
  if (!window.claude || !window.claude.use) { S.ia[fid] = t('Esta lectura solo funciona en la versión publicada de la app.','This reading only works in the published version of the app.'); persist(); render(true); return; }
  btn.disabled = true;
  var antes = btn.textContent;
  btn.textContent = t('Leyendo…','Reading…');
  window.claude.use('sample').then(function(sample){
    if (!sample) { S.ia[fid] = t('La lectura no está disponible en esta vista.','The reading is not available in this view.'); persist(); render(true); return; }
    var pr = 'Eres el Director de NOGUM, un juego de rol universal. Un Director acaba de contestar un formulario de escalas de 1 a 5 sobre su mesa. '
      + 'Esto es lo que ha contestado:\n\n' + respuestasTexto(fid) + '\n\nY esto es lo que el formulario ha deducido:\n' + resultadoTexto(fid)
      + '\n\nEscribe entre 60 y 110 palabras, en ' + (S.lang === 'en' ? 'inglés' : 'castellano') + ', en segunda persona del plural («vuestra mesa»), sin listas ni títulos. '
      + 'Di en una frase qué clase de mesa es esta. Y después, lo importante: si hay dos respuestas que tiran en direcciones opuestas, dilo claramente y di qué sabor raro produce la mezcla y qué respuesta movería yo. '
      + 'Si no hay contradicción, dilo y no la inventes. No repitas los números ni expliques las reglas: habla de cómo se va a sentir jugar ahí.';
    return sample(pr, {modelTier:'default', cache:true}).then(function(r){
      S.ia[fid] = (r && r.text) ? r.text : t('No ha llegado respuesta.','No answer came back.');
      persist(); render(true);
    });
  }).catch(function(e){
    S.ia[fid] = t('No se ha podido leer: ','Could not read: ') + ((e && e.message) || (e && e.code) || '?');
    persist(); render(true);
  });
  setTimeout(function(){ if (btn) { btn.disabled = false; btn.textContent = antes; } }, 100);
}
"""
