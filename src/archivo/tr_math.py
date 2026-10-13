import re, io
SRC = 'frag_math.html'
DST = 'frag_math.en.html'
lines = io.open(SRC, encoding='utf-8').read().split('\n')

TBL = '<div class="tw"><table class="t"><thead><tr><th>Profile (bonus)</th><th>Fumble</th><th>Failure</th><th>Partial</th><th>Success</th><th>Critical</th><th>Total success</th></tr></thead><tbody>'

L = {
2: '<h2>1.3 The Engine Room (Statistical Analysis)</h2>',
3: '<aside class="meta"><p>Warning: this section is technical content. If probabilities bring you out in a rash, you can skip straight to 1.4 (Control Panel). The cards work just the same even if you do not know why. This is where you come to look at the engine with the bonnet up.</p></aside>',
4: '<p>Every figure in this section comes from an exact enumeration of the possible combinations: 10 with one die and 100 with two. They are neither rounded nor simulated. They follow the canonical rules: the fumble and the critical are read <strong>on the dice, without bonuses</strong>, and take priority over the total <span class="flag ed">ED-1</span>. Everything else is resolved with <em>reading + total bonus</em> against the TN of the active card.</p>',
5: '<h3 id="maq-equilibrio">A. The balance point: one die, neutral chaos</h3>',
6: '<p>What counts as “normal”? In real life, a flat distribution is madness: an expert surgeon who made a howling mistake one time in ten would be pure chaos. Even so, the hobby has spent decades rolling a single linear die (the d20 in D&amp;D, the d100 in Call of Cthulhu), and the table feels it as “normal”. NOGUM takes that habit as its starting point. <strong>A linear die is Neutral Chaos</strong> <span class="src">T14</span>. With 1d10, each face is worth 10%, and a Grand Master (+4) against TN 6 succeeds 90% of the time: they only fail on a natural 1. It is exciting, but not very professional.</p>',
7: '<h3 id="maq-orden">B. Tools of order: adding dice</h3>',
8: '<p>When you add dice together, the results pile up in the middle (the central limit theorem, the Gaussian bell curve). With 2d10 added, each extreme (2 or 20) comes up only 1% of the time, while the central value, 11, comes up 10%. Luck loses weight and competence gains it: that is <strong>order</strong> (Low Chaos).</p>',
9: '<ul><li><strong>GURPS</strong> rolls 3d6 (3–18, mean 10.5). A 10 or an 11 comes up 25% of the time, and a 3 or an 18 barely 0.93%. It is the classic example of a reliable world.</li><li><strong>FATE</strong> rolls 4dF (−4 to +4). The 0 comes up 23.46% of the time and the ±4 extremes only 2.47%: the sheet rules over the die.</li></ul>',
10: '<h3 id="maq-caos">C. Succumbing to chaos</h3>',
11: '<p>To raise Chaos there are two levers that leave the mean untouched:</p>',
12: '<dl><dt>C.1 Widening the natural ranges</dt><dd>More faces of the die become a fumble or a critical. With 1d10, going from “1 and 10” to “1–2 and 9–10” doubles the extremes: from 20% to 40% of rolls. It only makes sense because the fumble and the critical are natural: the bonus does not touch them. This is the Gonzo card (T5).</dd><dt>C.2 Partial success</dt><dd>A band of results becomes “yes, but…”. It is the heart of <em>Powered by the Apocalypse</em> games, which roll 2d6: on 6 or less you fail (41.67%), on 7–9 you get a success at a cost (41.67%) and on 10 or more, a full success (16.67%). This removes the dead end: something always happens. In D&amp;D the classic equivalent is the critical on a natural 20. This is the Pulp / Drama card (T3).</dd></dl>',
13: '<h3 id="maq-optimismo">D. The levers of optimism and terror</h3>',
14: '<p><strong>Optimism: keep the BEST of 2.</strong> This is advantage in D&amp;D 5th edition and the bonus dice in Call of Cthulhu 7th edition (which keep the better tens die). With 1d20, advantage raises the mean from 10.5 to 13.825 and cuts the fumble from 5% to 0.25%. In NOGUM, with 2d10, the mean rises from 5.5 to 7.15, the chance of either die being a 10 goes from 10% to 19%, and the double 1 stays at 1%.</p>',
15: '<p><strong>Terror: keep the WORST of 2.</strong> It is the exact mirror image. The mean drops to 3.85, any 1 ruins the roll (19%) and a miracle requires a double 10 (1%). Competence still counts, but panic can betray it.</p>',
16: '<h3 id="maq-dados">E. The NOGUM solution: two dice of different colours</h3>',
17: '<p>The whole system fits in <strong>two d10s of different colours, one red and one blue</strong>. You always roll both, and the active card says how to read them. There are six readings:</p>',
18: '<ol><li><strong>Red only</strong> (1d10): Neutral Chaos.</li><li><strong>The sum</strong> (2–20): order.</li><li><strong>The best</strong> of the two: optimism.</li><li><strong>The worst</strong> of the two: terror.</li><li><strong>Widened ranges</strong> on the red die: high chaos (C.1).</li><li><strong>Partial success bands</strong> on the total: high chaos (C.2).</li></ol>',
19: '<p>The table shows how each reading is distributed. The bar is relative to the most frequent value in its column.</p>',
53: '<p>Means: 1d10 (red) <strong>5.5</strong>, Best of 2d10 <strong>7.15</strong>, Worst of 2d10 <strong>3.85</strong>, Sum 2d10 <strong>11</strong>.</p>',
54: '<h3 id="maq-anclaje">F. The anchoring: from −2 to +4</h3>',
55: '<p>The total bonus (skill, difficulty, equipment and effects) <strong>always</strong> runs from −2 (Null) to +4 (Grand Master). It never leaves that range (see 4.1). That is why the tables in this book can be calculated in full: seven rows per card. Four reference profiles are shown here: Null (−2), Novice (+0), Professional (+2) and Grand Master (+4). Appendix D has all seven bonuses.</p>',
56: '<h3 id="maq-tarjetas">G. The seven configurations, one by one</h3>',
57: '<h4>T0 · Standard / Classic Adventure (Neutral Optimism / Medium Chaos) “Autopilot”</h4>',
58: '<p><em>Rule:</em> 1d10 (red) + bonus vs TN 6; fumble on natural 1; critical on natural 10.</p>',
65: '<p><strong>Why it fits:</strong> A single linear die: each face is worth 10%, and the bonus moves the needle ten points at a time. The Professional fails 3 times in 10 (counting the fumble) and even the Grand Master eats the natural 1. It is the volatility of an action film or of Game of Thrones: competence matters, but luck reigns. That is why it is the default tone: it is the hobby\'s habit. <span class="src">T130</span></p>',
66: '<h4>T1 · Hero (High Optimism / Low Chaos) “I\'m the best at what I do”</h4>',
67: '<p><em>Rule:</em> best of 2d10 + bonus vs TN 6; fumble on double 1; critical on any 10.</p>',
74: '<p><strong>Why it fits:</strong> The Grand Master almost never fails (99%): only the double 1 betrays them. And the Null still succeeds half the time (51%), because in this universe anyone can be a hero. The critical (19%) shows up almost one roll in five: the world wants you to shine. <span class="src">T130</span></p>',
75: '<h4>T2 · Realist (Neutral Optimism / Low Chaos) “Life is fair and predictable”</h4>',
76: '<p><em>Rule:</em> sum 2d10 + bonus vs TN 11; fumble on natural sum 2–3; critical on natural sum 19–20.</p>',
83: '<p><strong>Why it fits:</strong> The bell curve squashes the extremes (fumble and critical: 3% each) and leaves competence in charge: from 36% to 85% between the Null and the Grand Master. It is solid, fair and a little dull, so it rewards whoever plans ahead. The Master loses a bit compared with the single die, and that is the expert surgeon\'s “margin of human error”. <span class="src">T130</span></p>',
84: '<h4>T3 · Pulp / Drama (Neutral Optimism / High Chaos) “Yes, but it\'ll cost you”</h4>',
85: '<p><em>Rule:</em> 1d10 (red) + bonus; total ≤5 failure, 6–7 partial, ≥8 success; fumble on nat. 1; critical on nat. 10.</p>',
92: '<p><strong>Why it fits:</strong> A whole band of the die becomes success at a cost. For the Professional, 20% of rolls move the story forward with a bill attached. The engine churns out content non-stop: nobody gets stuck at a dead end, but few victories come out clean. <span class="src">T130</span></p>',
93: '<h4>T4 · Terror (Low Optimism / Medium Chaos) “I\'m scared of failing”</h4>',
94: '<p><em>Rule:</em> worst of 2d10 + bonus vs TN 6; fumble on any 1; critical on double 10.</p>',
101: '<p><strong>Why it fits:</strong> Competence barely saves you. The Grand Master reaches 81%, but the fumble (19%) is the same for everyone, and the Null is stuck at 9%. The tension does not come from “I don\'t know how to do this”, but from “I know how to do this, but panic may betray me”. The table grows cautious and avoids rolling. <span class="src">T130</span></p>',
102: '<h4>T5 · Gonzo (Maximum Chaos / Neutral Optimism) “Anything can happen!”</h4>',
103: '<p><em>Rule:</em> 1d10 (red) + bonus vs TN 6; fumble on nat. 1–2; critical on nat. 9–10.</p>',
110: '<p><strong>Why it fits:</strong> 40% of rolls end in an extreme whatever the bonus, which only matters in the 3–8 stretch. There is little distance between the Novice (50%) and the Grand Master (80%): Russian roulette rules. It suits comedy, dreams or wild magic, and in a serious campaign it would burn the table out. <span class="src">T130</span></p>',
111: '<h4>T6 · Tragedy (Low Optimism / Low Chaos) “There is no hope”</h4>',
112: '<p><em>Rule:</em> sum 2d10 + bonus vs TN 14; fumble on natural sum 2–3; critical on natural sum 19–20.</p>',
119: '<p><strong>Why it fits:</strong> It is suffocating realism. The same bell curve as the Realist, but with the bar moved up to 14: the Grand Master fails 36% of the time and the Null can only grit their teeth (15%). It is predictable, slow and oppressive: the maths of Chernobyl. <span class="src">T130</span></p>',
120: '<aside class="meta"><p>Did you notice that T1 and T4 are exact mirror images? In Hero, critical 19% and fumble 1%; in Terror, the other way round. The sheet does not change; what changes is the atmosphere. The same Professional goes from 91% to 49% without touching a single number on their sheet.</p></aside>',
121: '<h3 id="maq-malla">H. The nine modes of the Tonal Grid</h3>',
122: '<p>This is the reference for the Professional profile (+2) against the TN for each mode <span class="src">T130</span><span class="src">T131</span>. Six squares have a card. The other three (Classic Epic, Unleashed Pulp and Nightmare) are left for the GM to design, and they appear here with the reference recipe from the analysis of the nine modes.</p>',
123: '<div class="tw"><table class="t"><thead><tr><th>Optimism</th><th>Mode</th><th>Chaos</th><th>Card / recipe</th><th>TN</th><th>Fumble</th><th>Failure</th><th>Partial</th><th>Success</th><th>Critical</th><th>Total success</th></tr></thead><tbody>',
136: '<div class="rule"><p class="rule-title">The +4 illusion</p>',
137: '<p>When you go from one die (1–10) to the sum (2–20), the +4 seems to “weigh less”, because the scale is twice as long. It does not. With 1d10 against TN 6, the Grand Master needs a 2 or more: <strong>90%</strong>. With the sum against TN 11 they need a 7 or more: <strong>85%</strong> <span class="src">T29</span><span class="src">T30</span>. The bell curve concentrates results in the middle, so four points of bonus shift far more probability mass than their size suggests. Only five points are lost, and that is the grain of reality in Realist mode. The system changes the volatility, not your professional effectiveness.</p>',
138: '<p>Something similar happens with the Novice (+0): 50% with one die and 55% with the sum. The “50%” figure quoted for the sum was a wrong rounding <span class="flag ed">ED-M</span>.</p></div>',
139: '<aside class="meta"><p><strong>The 99% principle</strong>. In Hero mode, the Grand Master succeeds at a standard task 99% of the time <span class="src">T21</span><span class="src">T22</span>. That is not a bug: a Grand Master should have no trouble with the mundane. There is no “narrative inflation” here: the difficulty stays where it is. If the roll cannot turn out interesting, <strong>don\'t roll</strong>. And if the player wants to show off, let them raise the difficulty themselves with “one hand behind the back”, for instance by ricocheting the bullet off the wall. Trade safety for glory.</p></aside>',
142: '<h2>Appendix D · Full tables</h2>',
143: '<p>These are the exact probabilities (in %) for each total bonus from −2 to +4. <em>Total success</em> = partial + success + critical. Each row adds up to 100%. Rules: the fumble and the critical are natural and take priority; everything else is resolved with reading + bonus against the card\'s TN.</p>',
144: '<h3 id="apxd-t0">T0 · Standard / Classic Adventure</h3>',
145: '<p>1d10 (red) + bonus vs TN 6; fumble on natural 1; critical on natural 10.</p>',
155: '<h3 id="apxd-t1">T1 · Hero</h3>',
156: '<p>best of 2d10 + bonus vs TN 6; fumble on double 1; critical on any 10.</p>',
166: '<h3 id="apxd-t2">T2 · Realist</h3>',
167: '<p>sum 2d10 + bonus vs TN 11; fumble on natural sum 2–3; critical on natural sum 19–20.</p>',
177: '<h3 id="apxd-t3">T3 · Pulp / Drama</h3>',
178: '<p>1d10 (red) + bonus; total ≤5 failure, 6–7 partial, ≥8 success; fumble on nat. 1; critical on nat. 10.</p>',
188: '<h3 id="apxd-t4">T4 · Terror</h3>',
189: '<p>worst of 2d10 + bonus vs TN 6; fumble on any 1; critical on double 10.</p>',
199: '<h3 id="apxd-t5">T5 · Gonzo</h3>',
200: '<p>1d10 (red) + bonus vs TN 6; fumble on nat. 1–2; critical on nat. 9–10.</p>',
210: '<h3 id="apxd-t6">T6 · Tragedy</h3>',
211: '<p>sum 2d10 + bonus vs TN 14; fumble on natural sum 2–3; critical on natural sum 19–20.</p>',
221: '<h3 id="apxd-recetas">Reference recipes without a card</h3>',
222: '<p>These recipes come from the analysis of the nine modes <span class="src">T130</span><span class="src">T131</span>. The author has not settled their final design <span class="flag pending">Pending</span>.</p>',
223: '<h4>Classic Epic</h4>',
224: '<p>best of 2d10 + bonus vs TN 6; fumble on double 1; critical on any 10.</p>',
234: '<h4>Unleashed Pulp</h4>',
235: '<p>best of 2d10 + bonus; total ≤5 failure, 6–7 partial, ≥8 success; fumble on double 1; critical on any 10.</p>',
245: '<h4>Survival Thriller</h4>',
246: '<p>worst of 2d10 + bonus vs TN 6; total 4–5 = success at a cost; fumble on any 1; critical on double 10.</p>',
256: '<h4>Nightmare / Slasher</h4>',
257: '<p>worst of 2d10 + bonus vs TN 6; fumble on any 1; critical on double 10.</p>',
267: '<h3 id="apxd-medias">Means and distributions of the readings</h3>',
307: '<h3 id="apxd-corregidas">Corrected figures</h3>',
308: '<p><span class="flag ed">ED-M</span> During the design conversation, some figures were quoted that do not survive an exact recalculation. The editor has replaced them throughout the book with the values in this table. The last row is not an arithmetic error: it is a change of bands. It is included so that nobody is surprised when comparing.</p>',
309: '<div class="tw"><table class="t"><thead><tr><th>Quoted figure</th><th>Turn</th><th>Correct value</th></tr></thead><tbody>',
310: '<tr><td>P(rolling 11 on 2d10) “almost 20%”</td><td><span class="src">T15</span></td><td><strong>10%</strong> <span class="flag ed">ED-M</span></td></tr>',
311: '<tr><td>Realist +2 vs TN 11: 64%</td><td><span class="src">T20, T23</span></td><td><strong>72%</strong> (needs a natural sum ≥ 9) <span class="flag ed">ED-M</span></td></tr>',
312: '<tr><td>Sum vs 14, +4: 55%</td><td><span class="src">T20</span></td><td><strong>64%</strong> (needs ≥ 10) <span class="flag ed">ED-M</span></td></tr>',
313: '<tr><td>Sum vs 14, +2: 28%</td><td><span class="src">T20</span></td><td><strong>45%</strong> (needs ≥ 12) <span class="flag ed">ED-M</span></td></tr>',
314: '<tr><td>Sum vs 14, −2: 10%</td><td><span class="src">T20</span></td><td><strong>15%</strong> (needs ≥ 16) <span class="flag ed">ED-M</span></td></tr>',
315: '<tr><td>Tragedy (TN 13) +4: 64% and +2: 45%</td><td><span class="src">T23</span></td><td><strong>TN 13: 72% and 55%</strong> (with the canonical TN 14 (T30) you get 64% and 45%, so the quoted figures are valid for the current card) <span class="flag ed">ED-M</span></td></tr>',
316: '<tr><td>Tragedy −2: 10%</td><td><span class="src">T23</span></td><td><strong>15% (TN 14)</strong> (with TN 13 it would be 21%) <span class="flag ed">ED-M</span></td></tr>',
317: '<tr><td>Sum +0 vs TN 11: 50%</td><td><span class="src">T29</span></td><td><strong>55%</strong> (P(sum ≥ 11)) <span class="flag ed">ED-M</span></td></tr>',
318: '<tr><td>Grand Master critical on the sum (margin of 4): 36%</td><td><span class="src">T30</span></td><td><strong>45%</strong> (36% is P(≥ 13); the Margin Rule has been withdrawn (ED-1)) <span class="flag ed">ED-M</span></td></tr>',
319: '<tr><td>Power Fantasy critical (best of 2): 1%</td><td><span class="src">T130</span></td><td><strong>19%</strong> (corrected by the author in T131) <span class="flag ed">ED-M</span></td></tr>',
320: '<tr><td>Black Comedy +2: normal success 40%</td><td><span class="src">T130</span></td><td><strong>50%</strong> (rolls 4–8; normal failure (roll 3) is 10%) <span class="flag ed">ED-M</span></td></tr>',
321: '<tr><td>Purist Horror: fumble 10% (“1 on the good die”)</td><td><span class="src">T130</span></td><td><strong>19%</strong> (with worst of 2, the chosen die is a 1 if there is any 1) <span class="flag ed">ED-M</span></td></tr>',
322: '<tr><td>Thriller +2: dirty success ~20%, failure ~30%</td><td><span class="src">T130</span></td><td><strong>partial 32%, failure 0%, fumble 19%</strong> (clean success (with critical) 49%: that figure was indeed correct) <span class="flag ed">ED-M</span></td></tr>',
323: '<tr><td>Dissonance in horror: “from 80% to 30%”</td><td><span class="src">Draft 7.4</span></td><td><strong>91% → 49%</strong> (Professional +2 vs TN 6, best → worst of 2 (ED-14)) <span class="flag ed">ED-M</span></td></tr>',
324: '<tr><td>Pulp +2: failure 30%, cost 30%, clean 40%</td><td><span class="src">T23</span></td><td><strong>fumble 10, failure 20, partial 20, success 40, critical 10%</strong> (not a calculation error: T23 used bands 1–5 / 6–8 / 9+ and no natural fumble/critical; the canonical bands are used here)</td></tr>',
326: '<p>These figures from the conversation have been checked and are <strong>correct</strong>:</p><ul>',
327: '<li>Hero +4 / +2 / −2 (TN 6) <span class="src">T20</span></li>',
328: '<li>Terror +4 / +2 / −2 (TN 6) <span class="src">T20</span></li>',
329: '<li>Neutral 1d10 +4 / +2 / −2 <span class="src">T20</span></li>',
330: '<li>Realist +4 / −2 (TN 11) <span class="src">T20</span></li>',
331: '<li>Fumbles 10 / 1 / 19 / 3% <span class="src">T20</span></li>',
332: '<li>Tragedy (TN 14) +4 / +2: 64 / 45% <span class="src">T30</span></li>',
333: '<li>Unleashed Pulp +2: clean 75%, cost 16%, fumble 1% <span class="src">T130</span></li>',
334: '<li>Null 1d10: from 50% to 30% <span class="src">Draft 4.2</span></li>',
335: '<li>The +4 illusion: 90% versus 85% <span class="src">T30</span></li>',
336: '<li>Mean of the best of 2d10: 7.15; references for d20 with advantage (13.82 mean, 0.25% fumble), PbtA (41.7 / 41.7 / 16.7%) and 3d6 (≈ 25%) <span class="src">T13</span></li>',
}

TBL_ES = '<div class="tw"><table class="t"><thead><tr><th>Perfil (bono)</th><th>Pifia</th><th>Fallo</th><th>Parcial</th><th>Éxito</th><th>Crítico</th><th>Éxito total</th></tr></thead><tbody>'

# text-node mapping for remaining lines
TX = {
 'Valor': 'Value', '1d10 (barra)': '1d10 (bar)', 'Mejor (%)': 'Best (%)', 'Mejor (barra)': 'Best (bar)',
 'Peor (%)': 'Worst (%)', 'Peor (barra)': 'Worst (bar)', 'Suma 2d10 (%)': 'Sum 2d10 (%)',
 'Suma 2d10 (barra)': 'Sum 2d10 (bar)',
 'Nulidad (−2)': 'Null (−2)', 'Novato (+0)': 'Novice (+0)', 'Profesional (+2)': 'Professional (+2)',
 'Gran Maestro (+4)': 'Grand Master (+4)',
 'Alto': 'High', 'Bajo': 'Low', 'Medio': 'Medium', 'Neutro': 'Neutral',
 'Fantasía de Poder': 'Power Fantasy', 'Épica Clásica': 'Classic Epic', 'Pulp Desatado': 'Unleashed Pulp',
 'Realismo Gris': 'Grey Realism', 'Drama de Acción': 'Action Drama',
 'Comedia Negra / Extrañeza': 'Black Comedy / Weirdness', '(Caos Alto, otro sabor)': '(High Chaos, another flavour)',
 'Terror Purista': 'Purist Horror', 'Thriller de Supervivencia': 'Survival Thriller',
 '(Thriller, variante T130)': '(Thriller, T130 variant)', 'Pesadilla / Slasher': 'Nightmare / Slasher',
 'T1 Héroe': 'T1 Hero',
 'Receta: mejor de 2, crítico cualquier 10, pifia doble 1 (hoy idéntica a T1; la diferencia con Fantasía de Poder está abierta) ':
   'Recipe: best of 2, critical on any 10, fumble on double 1 (currently identical to T1; how it differs from Power Fantasy is still open) ',
 'Receta: mejor de 2 + parcial con total 6–7 ': 'Recipe: best of 2 + partial on a total of 6–7 ',
 'Receta: peor de 2 + total 4–5 = éxito con coste ': 'Recipe: worst of 2 + total 4–5 = success at a cost ',
 'Receta: peor de 2, pifia cualquier 1 (hoy idéntica a T4; el caos alto del eje bajo está por definir) ':
   'Recipe: worst of 2, fumble on any 1 (currently identical to T4; high chaos on the low axis is yet to be defined) ',
 'Pendiente': 'Pending',
 'T2 Realista': 'T2 Realist', 'T0 Estándar': 'T0 Standard', 'T5 Gonzo (rangos ampliados, C.1)': 'T5 Gonzo (widened ranges, C.1)',
 'T3 Pulp / Drama (éxito parcial, C.2)': 'T3 Pulp / Drama (partial success, C.2)', 'T6 Tragedia': 'T6 Tragedy',
 'T4 Terror': 'T4 Terror',
 'Lectura': 'Reading', 'Rango': 'Range', 'Media': 'Mean', '1d10 (rojo)': '1d10 (red)',
 'Mejor de 2d10': 'Best of 2d10', 'Peor de 2d10': 'Worst of 2d10', 'Suma 2d10': 'Sum 2d10',
 '5,5': '5.5', '7,15': '7.15', '3,85': '3.85',
 'Mejor ≤ valor (%)': 'Best ≤ value (%)', 'Peor ≤ valor (%)': 'Worst ≤ value (%)',
 'Suma': 'Sum', 'P(suma ≥ valor) (%)': 'P(sum ≥ value) (%)',
}

out = []
unknown = set()
for i, line in enumerate(lines, 1):
    if i in L:
        out.append(L[i]); continue
    if line == TBL_ES:
        out.append(TBL); continue
    def rep(m):
        t = m.group(0)
        if t in TX: return TX[t]
        if re.fullmatch(r'[\s0-9%+−\-–,.]*|1d10 \(%\)|TN|P \(%\)', t):
            return re.sub(r'(\d) %', r'\1%', t)
        unknown.add(t); return t
    parts = re.split(r'(<[^>]*>)', line)
    parts = [p if p.startswith('<') else (re.sub(r'.+', rep, p) if p else p) for p in parts]
    out.append(''.join(parts))
io.open(DST, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
print('unknown text nodes:', unknown)
