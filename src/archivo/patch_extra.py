import io
p='app4_extra.js'; s=io.open(p,encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:60],s.count(a)); s=s.replace(a,b)
rep("  if (!quiet && campTurns.length === 0 && false) return;\n","")
rep(" campTurns.pop(); campTurns.pop(); } })"," } })")
rep("function campAnswer(qv, moreInSecret, quiet){","function campAnswer(qv, moreInSecret){")
rep("campAnswer(qv, !!(r && r.in_secret), true);","campAnswer(qv, !!(r && r.in_secret));")
rep("if (locked) { pendingQ = null; lockBubble(); }","if (locked) { pendingQ = qv; lockBubble(); }")
rep("b.closest('.msg').remove(); campAnswer(q, false); }","b.closest('.msg').remove(); if (sample && !aiDenied) campAnswer(q, false); else chatMsg('loc', t('Secreto de Máster','GM secret') + ':\n' + S.story.secret.slice(0, 600)); }")
rep("lastRoll = {r:r, b:b, use:use,","lastRoll = {m:R.m, r:r, b:b, use:use,")
rep("(L2 && L2.use === 'r' && READ[curKey()].m === 'red' && w === 'b' ? ' off' : '')","(L2 && L2.m === 'red' && w === 'b' ? ' off' : '')")
rep("  } else if (s.known === false && M.known !== false)","  } else if (s.known === true && M.known !== true && typeof s.world !== 'number') { M.known = true; M.family = null; M.world = null; M.era = null; M.tech = null; }\n  else if (s.known === false && M.known !== false)")
io.open(p,'w',encoding='utf-8').write(s)
