# -*- coding: utf-8 -*-
"""Lo que falto en el Acelerado ingles: los dos pregenerados y las tarjetas viejas."""
import io, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
f = 'frag_acelerado.en.html'
s = io.open(f, encoding='utf-8').read()

R = [
 ("<p><strong>At the table:</strong> she shoots at +4 and dodges well, but with any gadget she's Null (−2): if an electronic door needs opening, let someone else do it.</p>",
  "<p><strong>Separate pot:</strong> 5 Keys — “Firearms against drones”, “Intimidation against runners” and three left unspent for session zero.</p>\n"
  "<p><strong>At the table:</strong> she shoots at +4 and dodges well, but with any gadget she's Null (−2): if an electronic door needs opening, let someone else do it.</p>"),
 ('<td>Erudition +1 → Occultism +2 → Cults and grimoires +3 · Erudition → Humanities +2 · Wits +1 → Investigation +2 → Archives and libraries +3</td><td class="num">7</td>',
  '<td>Erudition +1 → Occultism +2 → Cults and grimoires +3 · Erudition → Humanities +2 · Erudition → Sciences +2 · Wits +1 → Investigation +2 → Archives and libraries +3 · Wits → Alertness +2</td><td class="num">9</td>'),
 ('<td>Influence +1 → Empathy +2</td><td class="num">2</td>',
  '<td>Influence +1 → Empathy +2 · Influence → Deception +2 · Influence → Persuasion +2</td><td class="num">4</td>'),
 ("<p><strong>At the table:</strong> he knows more than anyone about what shouldn't exist,",
  "<p><strong>Separate pot:</strong> 5 Keys, which are his whole character — “Occultism against the Deep Ones”, “Investigation against the cult”, and three still to be discovered.</p>\n"
  "<p><strong>At the table:</strong> he knows more than anyone about what shouldn't exist,"),
 ('<td>Gift +1 → Projection +2 → Fire +4 · Gift → Protection +2</td><td class="num">5</td>',
  '<td>Gift +1 → Projection +2 → Fire +4 · Gift → Protection +2 · Ritual +1 → Summoning +2</td><td class="num">7</td>'),
 ('<td>Erudition +1 → Occultism +2</td><td class="num">2</td>',
  '<td>Erudition +1 → Occultism +2 · Erudition → Humanities +2</td><td class="num">3</td>'),
 ('<td>Influence +1</td><td class="num">1</td>',
  '<td>Influence +1 → Persuasion +2</td><td class="num">2</td>'),
 ('Level 2 in Arcane is an example choice; by default, characters start at level 1.',
  'Her level 2 in Arcane <strong>is her separate pot</strong>: she has spent there what the other two spend on Keys. By default, characters start at level 1 in everything.'),
 ('those from cards T1, T0 and T4 of the Complete Game',
  'those from the Epic, First Gear and Nightmare cards of the Complete Game'),
]
n = 0
for a, b in R:
    if a in s:
        s = s.replace(a, b, 1); n += 1
    else:
        print('  no encontrado:', a[:70])
io.open(f, 'w', encoding='utf-8').write(s)
print('EN acelerado, reemplazos:', n, 'de', len(R))
