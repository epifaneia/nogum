# -*- coding: utf-8 -*-
"""El Acelerado en ingles: Epic -> Optimistic, Dread -> Chaos, y Terror nuevo."""
import io, os, re, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
F = 'frag_acelerado.en.html'
s = io.open(F, encoding='utf-8').read()
fal = []


def rep(a, b, q):
    global s
    if s.count(a) != 1:
        fal.append('%s (%d)' % (q, s.count(a)))
        return
    s = s.replace(a, b, 1)


def blo(ini, fin, b, q):
    """Sustituye desde ini hasta fin (ambos literales), fin incluido."""
    global s
    i = s.find(ini)
    j = s.find(fin, i)
    if i < 0 or j < 0:
        fal.append(q)
        return
    s = s[:i] + b + s[j + len(fin):]


rep('<tr><td><strong>A lot</strong></td><td>Epic</td><td>Epic</td><td>Epic</td></tr>',
    '<tr><td><strong>A lot</strong></td><td>Optimistic</td><td>Optimistic</td><td>Optimistic</td></tr>', 'cruce mucho')

blo('<p>Optimism is what picks the mode.', '</p>',
    '<p>Optimism picks the mode and chaos decides one box. There are four, and each changes one thing and one thing only:</p>\n'
    '<ul>\n'
    '<li><strong>Optimistic</strong> changes <em>the die</em>: you roll two and keep the higher.</li>\n'
    '<li><strong>Neutral</strong> changes nothing. It is the reference.</li>\n'
    '<li><strong>Chaos</strong> changes <em>what the result is made of</em>: same die, wider bands and successes that charge a toll.</li>\n'
    '<li><strong>Terror</strong> changes <em>what you can take</em>: the same die as Neutral, but three health boxes instead of nine.</li>\n'
    '</ul>\n'
    '<p>Look hard at the third one, because it is the strangest and the most important thing in this book: <strong>Chaos and Neutral bring exactly the same number of rolls home</strong>, 50&nbsp;% with the sheet at zero and 70&nbsp;% with the sheet at +2. Chaos does not make you fail more. It changes what happens to you is made of: where Neutral deals clean successes and clean failures, Chaos deals fumbles, criticals and wins that come with an invoice.</p>\n'
    '<p>And the fourth is the other way to hurt. <strong>In Terror the world is not crueller: you are more fragile.</strong> You roll as in Neutral and you hit just as often. What changes is that a knife kills you. The Complete Game calls that <em>fractal health</em> and leaves it in your hands; here it comes preset, so you can watch it work without having to decide anything.</p>',
    'parrafo del cruce')

blo('<p><strong>ED-A1.</strong> The author set the three modes', '</p>',
    '<p><strong>ED-A1.</strong> The author set the four modes, their readings, and that the 3 health boxes are anchored to Terror rather than being a switch. The crossing table is an editorial decision: high optimism = Optimistic with any chaos; normal optimism + a lot of chaos = Chaos; low optimism = Terror with any chaos.</p>',
    'ED-A1')

blo('<aside class="meta"><p>Missing a tone?', '</aside>',
    '<aside class="meta"><p>Missing a tone? A world that is Swiss clockwork and cruel at the same time? A game of Russian roulette where a 9 is already a miracle? Dark <em>and</em> chaotic at once? These four cover roughly everything and are enough to start with. And they are not a separate invention: all four exist in the Complete Game —Optimistic is Epic, Neutral is First Gear, Chaos is Black comedy and Terror is First Gear with the short health track—. By the time they feel small, you already know four of the seven cards. <span class="src">T135</span></p></aside>',
    'aside tonos')

rep('<tr><td><strong>Epic</strong></td><td>The <strong>higher</strong> of the two</td><td>Double 1</td><td>A 10 on either</td><td>Total 6 or more: success</td></tr>',
    '<tr><td><strong>Optimistic</strong></td><td>The <strong>higher</strong> of the two</td><td>Double 1</td><td>A 10 on either</td><td>Total 6 or more: success</td></tr>', 'tabla optimista')

blo('<tr><td><strong>Dread</strong></td><td>The <strong>lower</strong> of the two</td>', '</tr>',
    '<tr><td><strong>Chaos</strong></td><td><strong>Red die only</strong> (the blue one does not count)</td><td>A 1 <strong>or 2</strong> on the red</td><td>A 9 <strong>or 10</strong> on the red</td><td>Total 5 or less: failure · 6 or 7: <strong>partial success</strong> · 8 or more: success <span class="flag ed">ED-15</span></td></tr>\n'
    '<tr><td><strong>Terror</strong></td><td><strong>Red die only</strong> (the blue one does not count)</td><td>A 1 on the red</td><td>A 10 on the red</td><td>Total 6 or more: success · <strong>and only 3 health boxes</strong> (2.6)</td></tr>',
    'tabla caos y terror')

rep('<p><strong>Partial success (Dread only).</strong>', '<p><strong>Partial success (Chaos only).</strong>', 'parcial')

blo('<p><strong>ED-15.</strong> The author said', '</p>',
    '<p><strong>ED-15.</strong> The Chaos mode bands are exactly those of the Black comedy card in the Complete Game: red die, fumble on 1 or 2, critical on 9 or 10, and success at a cost taking the TN and the point above it (total 6 or 7). It never turns a failure into a success; it only charges a toll on what had already worked out. Consequence: in Chaos a professional (+2) works it out 70&nbsp;% of the time —the same as in Neutral— but three out of every seven of those times paying a price. All four readings come from the Complete Game: Epic, First Gear, Black comedy, and First Gear with the short health track.</p>',
    'ED-15')

blo('<aside class="meta"><p>Same character (+2), same task:', '</aside>',
    '<aside class="meta"><p>Same character (+2), same task. In <strong>Optimistic</strong> they pull it off 91&nbsp;% of the time. In <strong>Neutral</strong>, 70&nbsp;%. '
    'In <strong>Chaos</strong>, also 70&nbsp;% —you read that right, the same number— but three out of every seven of those times paying a price, and with twice the fumbles and twice the criticals. '
    'In <strong>Terror</strong>, 70&nbsp;% again: what changes is that two hits now put them out. '
    'You have not touched the sheet once: you have changed the atmosphere three times in three different ways.</p></aside>',
    'aside porcentajes')

rep('<p>Every character has <strong>9 health boxes</strong>, in three blocks of three. Each point of damage crosses off one box.</p>',
    '<p>Every character has <strong>9 health boxes</strong>, in three blocks of three. Each point of damage crosses off one box.</p>\n'
    '<div class="rule"><p class="rule-title">Except in Terror</p>\n'
    '<p>In <strong>Terror</strong> mode there are not nine: there are <strong>3 boxes</strong>, a single block. Fill it and you are out of the fight. '
    'With the damage in this book that means <strong>two serious hits take you off the scene</strong>, and the grenade in the weapons table is not a threat: it is the ending.</p>\n'
    '<p>It is not a switch you have to remember to turn on. It comes with the mode, and it is the one piece of this book that lets you look in on what the Complete Game calls <strong>fractal health</strong>: there, lethality is a dial and you turn it, with three, nine or twenty-seven boxes.</p></div>',
    'vida terror')

rep('<p><strong>In Dread</strong>, a partial success in combat', '<p><strong>In Chaos</strong>, a partial success in combat', 'combate')
rep('<li><strong>Failure</strong> (and, in Dread, partial success):', '<li><strong>Failure</strong> (and, in Chaos, partial success):', 'estilo')
rep('<tr><td>We start in Epic mode</td>', '<tr><td>We start in Optimistic mode</td>', 'arranque epico')
rep('<tr><td>We start in Dread mode</td>', '<tr><td>We start in Terror mode</td>', 'arranque terror')
rep('if you start in Epic, you play in Epic all afternoon', 'if you start in Optimistic, you play in Optimistic all afternoon', 'limites')
rep('<tr><td>Game mode</td><td>Epic / Neutral / Dread.</td></tr>',
    '<tr><td>Game mode</td><td>Optimistic / Neutral / Chaos / Terror.</td></tr>', 'referencia')
rep('His game is finding Keys. In Dread', 'His game is finding Keys. In Terror', 'pnj')
blo('<li><strong>ED-A1.</strong> Selector crossing table:', '</li>',
    '<li><strong>ED-A1.</strong> Selector crossing table: high optimism → Optimistic; low optimism → Terror; normal optimism → Neutral, except with “a lot” of chaos, which goes to Chaos.</li>',
    'ED-A1 lista')
blo('<li><strong>ED-15.</strong> Dread bands', '</li>',
    '<li><strong>ED-15.</strong> Success at a cost in Chaos mode, on the red die: total 6 or 7, with wide fumble and critical bands (1–2 / 9–10). It is the Black comedy card from the Complete Game, unchanged. In combat and in Style, the partial is read as success at a cost or as “you win, but messily”. <span class="src">T146</span></li>',
    'ED-15 lista')

io.open(F, 'w', encoding='utf-8').write(s)
if fal:
    print('FALLOS:')
    for m in fal:
        print('  ' + m)
    sys.exit(1)
print('ingles: cuatro modos')
