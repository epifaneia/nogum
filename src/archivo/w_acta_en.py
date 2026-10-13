# -*- coding: utf-8 -*-
"""La segunda tanda del acta, en ingles, y el catalogo de Firmas cerrado en los dos."""
import io, os, re
os.chdir(os.path.dirname(os.path.abspath(__file__)))

EN = [
 ('To do so they pay a cost: <strong>mark off 1 box of their Mental track</strong> (the stress of having foreseen everything) or <strong>spend an equipment resource</strong>. If the flashback calls for a risky action, it is rolled like any other. <span class="flag proposal">Unvalidated proposal</span>',
  '<strong>The flashback is not paid for: it is rolled.</strong></p>'
  '<ul><li>Roll whatever skill the plan calls for against the active card’s TN.</li>'
  '<li><strong>Success:</strong> the flashback happened, and you have what you went for.</li>'
  '<li><strong>Every point above the TN</strong> buys one more detail inside it: something you left ready, an exit, somebody placed where you needed them.</li>'
  '<li><strong>Failure:</strong> the plan existed, but it went crooked and you find out now.</li>'
  '<li><strong>Fumble:</strong> the past gives you away; the fumble menu (5.2) decides how.</li></ul>'
  '<p>That way the flashback stops being a currency and becomes a scene with risk, which is what the table wanted it for. <span class="src">Author’s decision</span>'),
 ('the transformation carries a noted <strong>end condition</strong>: when the scene ends, when a health block is filled, or by spending one box of the Spiritual track per turn. <span class="flag proposal">Unvalidated proposal</span>',
  'the transformation always has the same <strong>end condition</strong>: <strong>it ends when the scene ends</strong>. No variants, no counters, no spending boxes per turn: what the genre wants is for it to last exactly as long as the fight. <span class="src">Author’s decision</span>'),
 ('for example, radiation <span class="tag">Dmg 1</span> <span class="tag">Dodge: None</span> <span class="tag">Soak: None</span>. Proper protection (suit, shelter, antidote) works as narrative permission: with it, the damage can be soaked or disappears. <span class="flag proposal">Unvalidated proposal</span>',
  'and <strong>the damage rises the longer you stay</strong>: <span class="tag">Dmg 1</span> the first scene, <span class="tag">Dmg 2</span> the second, <span class="tag">Dmg 3</span> the third, always <span class="tag">Dodge: None</span> <span class="tag">Soak: None</span>. The counter resets the moment you get out. Proper protection (suit, shelter, antidote) works as narrative permission: with it, the damage can be soaked or disappears. <span class="src">Author’s decision</span>'),
 ('<li><strong>As a shield.</strong> It can divert Mental damage onto a bond, which suffers in the fiction (an argument, an abandonment, a wound). Personal life is sacrificed to save the mind.</li>',
  '<li><strong>As a shield.</strong> It can divert damage onto a bond, which suffers in the fiction: an argument, an abandonment, a wound. Personal life is sacrificed to save the rest.</li>'
  '</ul><p><strong>Which bar a bond can shield is decided by the universe.</strong> By default, the Mental one. In the gothic, the Spiritual one as well: holding on to somebody who loves you is exactly what holds the Beast back, which is why bonds are half a character sheet there. <span class="src">Author’s decision</span></p><ul style="display:none">'),
 ('The <strong>Mental</strong> track can be called Empathy and take a hit with each implant: cyberpsychosis is a madness, not a possession, and this world has no Arcane sphere, so it has no Spiritual bar <span class="flag proposal">Unvalidated proposal</span>.',
  'The <strong>Mental</strong> track is called <strong>Humanity</strong> here and takes a hit with each implant: cyberpsychosis is a madness, not a possession, and this world has no Arcane sphere, so it has no Spiritual bar. It is deliberately the same word the gothic uses (ED-39): <em>the same word, the same loss, and yet a different bar</em>, because there a Beast lives inside and here nobody does.'),
 ('In canon: Generation is the Grid level (for example, fledgling 1, prince 3, methuselah 5 <span class="flag proposal">Unvalidated proposal</span>).',
  'In canon: no ladder of Generations. <strong>Every vampire is Grid 2 at the supernatural</strong>, and by default at Physical too, which is not excessive: a human without a Key <strong>loses automatically</strong>, and that is exactly what the genre means. The steps are still one at a time, and one step is ×100. If you want to tell a fledgling from a methuselah, do not raise the Grid: <strong>give them Keys</strong> —Fortitude, Stealth, Intimidation—, which is finer and does not break the scale.'),
 ('here it is played as the thing that actually gives you a scene: the craving <span class="flag proposal">Unvalidated proposal</span>.',
  'here it is played as the thing that actually gives you a scene: the craving.'),
 ('In this recipe the Spiritual track is called <strong>Identity</strong>: if it empties, the character forgets who they are and becomes an NPC. <span class="flag proposal">Unvalidated proposal</span>',
  'Here the Mental track is called <strong>Identity</strong> (ED-39: there is no Arcane, so there is no Spiritual bar). <strong>Emptying it never retires the sheet.</strong> What waits on the other side is therapy —mind-dancing, reconstruction, time— and you come back as <em>a very different character</em>, which is far better table material than a gap. Severe cases are not played as protagonists unless expressly agreed, and losing the sheet only happens in short games where that ending was agreed from the start. <span class="src">Author’s decision</span>'),
 ('Sherlock’s “metanarrative power” (the Game Master feeding him clues) is a Signature, an aspect or a Key. <span class="flag pending">Pending</span>',
  'the detective’s “metanarrative power” —the Director feeding them clues— <strong>is a Key</strong>: one clue per scene, bought and paid for like any other. That way it stops being a favour from the Director and becomes something the player chose to have. <span class="src">Author’s decision</span>'),
 ('<strong>Blood</strong> (renamed Mental track): the vampire’s stress; spent to activate powers. <em>Recipe 13.</em>',
  '<strong>Thirst</strong> (renamed Mental track): the vampire’s craving, played as withdrawal. <em>Recipe 13.</em>'),
 ('<strong>Corruption</strong> (renamed Spiritual track) in grimdark; <strong>Empathy</strong> and <strong>Identity</strong> (renamed Mental track) in cyberpunk and digital minds,',
  '<strong>Corruption</strong> (renamed Spiritual track) in grimdark; <strong>Humanity</strong> and <strong>Identity</strong> (renamed Mental track) in cyberpunk and digital minds,'),
 ('the specific uses of each track (what fills it, what empties it) are not validated. <span class="flag proposal">Unvalidated proposal</span>',
  'the specific uses of each track are settled in <a href="#ch8-tablas">the problem tables</a> and in ED-39.'),
]
f = 'frag_cap8.en.html'
s = io.open(f, encoding='utf-8').read()
for a, b in EN:
    n = s.count(a)
    print('%d  %s' % (n, a[:56]))
    s = s.replace(a, b)
io.open(f, 'w', encoding='utf-8').write(s)

# --- las banderas aprobadas que quedaban en ingles
FLAG = re.compile(r'\s*<span class="flag (?:pending|proposal)">[^<]*</span>')
OK = '<span class="src">Approved by the author</span>'
for f, marcas in (('frag_cap8.en.html',
                   ['Whoever fills their clock first wins', 'the heroes have packed sandwiches',
                    'The player may turn the bargain down', "the weapon's and the defender's tags",
                    '1 per minor rune, 2 per major rune', 'Spiritual Dmg 1</span> to the caster',
                    'the configuration that comes closest']),
                  ('frag_acelerado.en.html',
                   ['not the wording of the others', "The rest are this rulebook's own",
                    'Each also uses their separate pot'])):
    s = io.open(f, encoding='utf-8').read()
    for marca in marcas:
        i = s.find(marca)
        if i < 0:
            print('  NO:', f, marca[:40]); continue
        m = FLAG.search(s, i)
        if not m or m.start() - (i + len(marca)) > 130:
            print('  sin bandera:', marca[:40]); continue
        s = s[:m.start()] + ' ' + OK + s[m.end():]
    io.open(f, 'w', encoding='utf-8').write(s)

# --- el catalogo de Firmas, cerrado en los dos idiomas
CAT = [
 ('frag_cap8.html',
  'El autor quiere un catálogo masivo, de unas <strong>1.000 Firmas</strong> (5 categorías × 5 Firmas × 40 Disciplinas), organizado en categorías que <strong>se solapen lo menos posible</strong> y dejen claro al jugador dónde mirar. <span class="flag pending">Pendiente</span>',
  'El catálogo está <strong>hecho y ordenado por Disciplina</strong>: doscientas Firmas, cinco por cada una, aquí mismo. Esa es la categorización, y es la que se usa en mesa: miras tu rama y eliges. El autor hablaba de llegar a unas mil (cinco categorías por Disciplina); con las doscientas escritas, ampliarlo es sumar filas y no rediseñar nada. <span class="src">Cerrado</span>'),
 ('frag_cap8.en.html',
  'organized into categories that overlap as little as possible and make it clear to the player where to look. <span class="flag pending">Pending</span>',
  'The catalogue is <strong>written and ordered by Discipline</strong>: two hundred Signatures, five per Discipline, right here. That is the categorisation, and it is the one used at the table: you look at your branch and pick. The author spoke of reaching a thousand (five categories per Discipline); with two hundred written, expanding it means adding rows, not redesigning anything. <span class="src">Closed</span>'),
]
for f, a, b in CAT:
    s = io.open(f, encoding='utf-8').read()
    print('catalogo %s: %d' % (f, s.count(a)))
    io.open(f, 'w', encoding='utf-8').write(s.replace(a, b))
