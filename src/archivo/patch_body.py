import io, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
s = io.open('app3_body.html', encoding='utf-8').read()
extra = io.open('app4_extra.js', encoding='utf-8').read()
css = io.open('app4_extra.css', encoding='utf-8').read()


def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:70], s.count(a))
    s = s.replace(a, b)


# data / tone
rep("function firmas(){ var o = []; for (var i = 1; i <= 5; i++) o.push({id:i, n:['Firma ' + i, 'Signature ' + i], tags:UNIVERSES.slice()}); return o; }\n", "")
rep("function cardKey(){ var k = CELL[opt() + '|' + caos()]; if (k === 'T3' && M.flavor === 'locura') k = 'T5'; return k; }",
    "function cardBase(){ var k = CELL[opt() + '|' + caos()]; if (k === 'T3' && M.flavor === 'locura') k = 'T5'; return k; }\n"
    "function sceneOn(){ return !!S.scene && S.tab !== 'form'; }\n"
    "function cardKey(){ return (sceneOn() && !isAcc() && CARDS[S.scene]) ? S.scene : cardBase(); }")
rep("function accK(){ if (opt()==='alto') return 'epico'; if (opt()==='bajo') return 'agobio'; return caos()==='alto' ? 'agobio' : 'neutro'; }",
    "function accBase(){ if (opt()==='alto') return 'epico'; if (opt()==='bajo') return 'agobio'; return caos()==='alto' ? 'agobio' : 'neutro'; }\n"
    "function accK(){ return (sceneOn() && isAcc() && ACC[S.scene]) ? S.scene : accBase(); }")
# changing the game tone in the form clears the scene override
rep("      if (p.set) p.set(val); else M[p.f] = val;",
    "      if (p.set) p.set(val); else M[p.f] = val;\n      S.scene = null;")

# markup: scene strip
rep('<main><div class="wrap" id="view"></div></main>',
    '<div id="scene" class="scene noprint" hidden></div>\n<main><div class="wrap" id="view"></div></main>')

# tabs
rep("  h += tabBtn('ask', u('ask'), 'right') + tabBtn('ses', u('ses'));\n  $('tabs').innerHTML = h; aiStatus();",
    "  h += tabBtn('dice', u('dice'), 'right') + tabBtn('story', u('story')) + tabBtn('ask', u('ask')) + tabBtn('ses', u('ses'));\n  $('tabs').innerHTML = h; aiStatus(); renderScene();")
rep("ask:['Preguntas','Questions'], ses:['Sesiones','Sessions'],",
    "ask:['Preguntas','Questions'], ses:['Sesiones','Sessions'], dice:['Dados','Dice'], story:['Historia','Story'],")

# form: talk mode + entry button
rep("  if (S.locked) return h + summaryPage(true) + '</div>';",
    "  if (S.locked) return h + summaryPage(true) + '</div>';\n  if (S.talk.on) return h + renderTalk() + '</div>';")
rep("""  h += '</div>' + (tl ? '<p class="techline">' + tl + '</p>' : '') + '</div>';""",
    """  h += '</div>' + (tl ? '<p class="techline">' + tl + '</p>' : '') + (p.f === 'known' ? '<div class="talkentry"><span>' + esc(t('¿Prefieres contarlo a tu manera?','Would you rather describe it your way?')) + '</span><button type="button" class="btn" id="talkGo">' + esc(t('Cuéntame tu universo','Tell me your universe')) + '</button></div>' : '') + '</div>';""")
rep("  if ((x = $('helpBtn')))",
    "  if ((x = $('talkGo'))) x.addEventListener('click', function(){ S.talk.on = true; persist(); render(); window.scrollTo(0,0); });\n  bindTalk();\n  if ((x = $('helpBtn')))")

# sheet head badge when the scene tone overrides
rep("""' · ' + esc(pick(card().n)) + '</div></div><div class="badges">' + (extra || '') + '</div></div>';""",
    """' · ' + esc(pick(card().n)) + (sceneOn() ? ' <span class="badge amber">' + esc(t('tono de escena','scene tone')) + '</span>' : '') + '</div></div><div class="badges">' + (extra || '') + '</div></div>';""")

# signatures on the sheet
rep("""'<select data-fsel="' + fi + '"><option value="">' + esc(t('Firma…','Signature…')) + '</option>' + firmas().filter(function(x){ return x.tags.some(function(tg){ return universes().indexOf(tg) > -1; }); }).map(function(x){ return '<option value="' + x.id + '"' + (f.id == x.id ? ' selected' : '') + '>' + esc(pick(x.n)) + '</option>'; }).join('') + '</select>""",
    """'<select data-fsel="' + fi + '"><option value="">' + esc(t('Firma…','Signature…')) + '</option>' + firmaList(sk).map(function(x, xi){ return '<option value="' + xi + '"' + (String(f.s) === String(xi) ? ' selected' : '') + ' title="' + esc(pick(x.d)) + '">' + esc(pick(x.n)) + '</option>'; }).join('') + '</select>""")
rep("""<span class="bonus">+' + f.lv + '</span></div>';""",
    """<span class="bonus">+' + f.lv + '</span></div>' + (firmaOf(f) ? '<div class="fdesc">' + esc(pick(firmaOf(f).d)) + '</div>' : '');""")
rep("c.fir[+s.getAttribute('data-fsel')].id = s.value; persist();",
    "c.fir[+s.getAttribute('data-fsel')].s = s.value; persist(); render(true);")

# chat bubble label
rep("kind === 'ai' ? 'NOGUM' : t('Canon (sin IA)','Canon (no AI)');",
    "kind === 'ai' ? 'NOGUM' : kind === 'lock' ? '🔒' : S.askMode === 'camp' ? t('Historia (sin IA)','Story (no AI)') : t('Canon (sin IA)','Canon (no AI)');")

# questions: two modes
rep("""function renderAsk(){ return '<div class="panel"><div class="formhead"><h2>' + esc(u('ask')) + '</h2></div><p class="note">' + esc(t('Dudas de reglas, respondidas según el canon de NOGUM y la mesa actual.','Rules questions, answered from the NOGUM canon and the current table.')) + '</p>""",
    """function renderAsk(){ var camp = S.askMode === 'camp'; return '<div class="panel"><div class="formhead"><h2>' + esc(u('ask')) + '</h2><div class="modesw" role="group"><button type="button" data-amode="rules" aria-pressed="' + !camp + '">' + esc(t('Reglas','Rules')) + '</button><button type="button" data-amode="camp" aria-pressed="' + camp + '">' + esc(t('Campaña','Campaign')) + '</button></div>' + (camp && S.story.pw && unlocked ? '<button type="button" class="tool" id="askLock">🔒 ' + esc(t('Bloquear secreto','Lock secret')) + '</button>' : '') + '</div><p class="note">' + esc(camp ? t('Preguntas sobre la campaña, respondidas con lo escrito en la pestaña Historia. Si la respuesta está en el Secreto de Máster, se pide la contraseña.','Campaign questions, answered from what is written in the Story tab. If the answer is in the GM secret, the password is required.') : t('Dudas de reglas, respondidas según el canon de NOGUM y la mesa actual.','Rules questions, answered from the NOGUM canon and the current table.')) + '</p>""")
rep("  var qv = $('askQ').value.trim(); if (!qv) return; $('askQ').value = ''; $('askNote').textContent = ''; chatMsg('me', qv);",
    "  var qv = $('askQ').value.trim(); if (!qv) return; $('askQ').value = ''; $('askNote').textContent = ''; chatMsg('me', qv);\n  if (S.askMode === 'camp') { campAsk(qv); return; }")
rep("$('clearBtn').addEventListener('click', function(){ turns = []; $('chat').innerHTML = ''; });",
    "$('clearBtn').addEventListener('click', function(){ if (S.askMode === 'camp') campReset(); else turns = []; $('chat').innerHTML = ''; }); "
    "v.querySelectorAll('[data-amode]').forEach(function(b){ b.addEventListener('click', function(){ S.askMode = b.getAttribute('data-amode'); pendingQ = null; persist(); render(); }); }); "
    "if ($('askLock')) $('askLock').addEventListener('click', function(){ unlocked = false; campReset(); render(); });")

# render: new tabs
rep("  else if (S.tab === 'ses') {",
    "  else if (S.tab === 'dice') { v.innerHTML = renderDice(); bindDice(); }\n  else if (S.tab === 'story') { v.innerHTML = renderStory(); bindStory(); }\n  else if (S.tab === 'ses') {")

# sessions: add the summary to the shared story
rep("""+ (a.next ? '<ul>' + a.next.map(function(x){ return '<li>' + esc(x) + '</li>'; }).join('') + '</ul>' : '');""",
    """+ (a.next ? '<ul>' + a.next.map(function(x){ return '<li>' + esc(x) + '</li>'; }).join('') + '</ul>' : '') + '<button type="button" class="tool" id="sesToStory">' + esc(t('Añadir el resumen a la Historia común','Add the summary to the Shared story')) + '</button>';
    $('sesToStory').addEventListener('click', function(){ var d = new Date().toLocaleDateString(S.lang); S.story.common = (S.story.common ? S.story.common.replace(/\\s+$/, '') + '\\n\\n' : '') + '[' + t('Sesión','Session') + ' ' + d + '] ' + a.summary; persist(); this.disabled = true; this.textContent = t('Añadido','Added'); });""")

# new block before RENDER
rep("/* ======================= RENDER ======================= */", extra + "/* ======================= RENDER ======================= */")
# CSS
rep("@media print{\n  .wiz,.nav,", css + "@media print{\n  .scene,.wiz,.nav,")

io.open('app4_body.html', 'w', encoding='utf-8').write(s)
b = io.open('build_app3.py', encoding='utf-8').read()
b = b.replace("R('app3_body.html')", "R('app4_body.html')")
if 'firmas.json' not in b:
    b = b.replace("js(json.load(open(os.path.join(D, 'app_data.json'), encoding='utf-8')))",
                  "js(dict(json.load(open(os.path.join(D, 'app_data.json'), encoding='utf-8')), firmas=json.load(open(os.path.join(D, 'firmas.json'), encoding='utf-8'))))")
    assert 'firmas.json' in b
io.open('build_app3.py', 'w', encoding='utf-8').write(b)
print('patched')
