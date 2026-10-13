# -*- coding: utf-8 -*-
"""Exact analysis of the 3x3 tone grid: per-cell distributions, duplicates, session feel."""
import itertools, json, os
from fractions import Fraction as F

os.chdir(os.path.dirname(os.path.abspath(__file__)))
D = range(1, 11)
TWO = list(itertools.product(D, D))
ONE = [(x, x) for x in D]          # only the red die matters; blue ignored
BONUS = [-2, -1, 0, 1, 2, 3, 4]


def card(read, tn, fum, cri, bands=None, one=False):
    return dict(read=read, tn=tn, fum=fum, cri=cri, bands=bands, one=one)


red = lambda r: r[0]
hi = lambda r: max(r)
lo = lambda r: min(r)
sm = lambda r: r[0] + r[1]

# id -> (label, cell, mechanics)
CARDS = {
    'T1':    ('Héroe',            'alto|bajo',   card(hi, 6, lambda r: r == (1, 1), lambda r: max(r) == 10)),
    'EPIC':  ('Épica clásica',    'alto|medio',  card(hi, 6, lambda r: r == (1, 1), lambda r: max(r) == 10)),
    'PULPD': ('Pulp desatado',    'alto|alto',   card(hi, 6, lambda r: r == (1, 1), lambda r: max(r) == 10, bands='pulp')),
    'T2':    ('Realista',         'neutro|bajo', card(sm, 11, lambda r: sm(r) <= 3, lambda r: sm(r) >= 19)),
    'T0':    ('Estándar',         'neutro|medio', card(red, 6, lambda r: r[0] == 1, lambda r: r[0] == 10, one=True)),
    'T3':    ('Pulp / Drama',     'neutro|alto', card(red, 6, lambda r: r[0] == 1, lambda r: r[0] == 10, bands='pulp', one=True)),
    'T5':    ('Gonzo',            'neutro|alto', card(red, 6, lambda r: r[0] <= 2, lambda r: r[0] >= 9, one=True)),
    'T6':    ('Tragedia',         'bajo|bajo',   card(sm, 14, lambda r: sm(r) <= 3, lambda r: sm(r) >= 19)),
    'T4':    ('Terror',           'bajo|medio',  card(lo, 6, lambda r: min(r) == 1, lambda r: r == (10, 10))),
    'NIGHT': ('Pesadilla',        'bajo|alto',   card(lo, 6, lambda r: min(r) == 1, lambda r: r == (10, 10))),
    # proposals for a grid where both axes always do something
    'P-AB':  ('[prop] Gauss optimista',   'alto|bajo',  card(sm, 9, lambda r: sm(r) <= 3, lambda r: sm(r) >= 19)),
    'P-BA':  ('[prop] Pesadilla parcial', 'bajo|alto',  card(lo, 6, lambda r: min(r) == 1, lambda r: r == (10, 10), bands='pulp')),
    'P-BA2': ('[prop] Pesadilla gonzo',   'bajo|alto',  card(lo, 6, lambda r: min(r) <= 2, lambda r: max(r) == 10)),
    'P-AA':  ('[prop] Héroe gonzo',       'alto|alto',  card(hi, 6, lambda r: min(r) <= 2, lambda r: max(r) >= 9, bands='pulp')),
}


def outcome(c, roll, b):
    if c['fum'](roll):
        return 'pifia'
    if c['cri'](roll):
        return 'critico'
    tot = c['read'](roll) + b
    if c['bands'] == 'pulp':
        return 'fallo' if tot <= 5 else ('parcial' if tot <= 7 else 'exito')
    return 'exito' if tot >= c['tn'] else 'fallo'


def dist(cid, b):
    _, _, c = CARDS[cid]
    space = ONE if c['one'] else TWO
    n = len(space)
    out = {k: 0 for k in ('pifia', 'fallo', 'parcial', 'exito', 'critico')}
    for r in space:
        out[outcome(c, r, b)] += 1
    return {k: F(v, n) for k, v in out.items()}


def win(d):       # anything that is not a plain failure or fumble
    return d['exito'] + d['critico'] + d['parcial']


def clean(d):     # unqualified success
    return d['exito'] + d['critico']


data = {}
for cid, (name, cell, c) in CARDS.items():
    rows = {}
    for b in BONUS:
        d = dist(cid, b)
        rows[b] = {k: float(v) for k, v in d.items()}
        rows[b]['gana'] = float(win(d))
        rows[b]['limpio'] = float(clean(d))
    d0 = dist(cid, 0)
    data[cid] = dict(name=name, cell=cell, tn=c['tn'], partial=c['bands'] == 'pulp',
                     one=c['one'], rows=rows,
                     pifia=float(d0['pifia']), critico=float(d0['critico']),
                     span=float(win(dist(cid, 4)) - win(dist(cid, -2))))

# duplicates: identical outcome vectors across every bonus
sig = {cid: json.dumps([[round(data[cid]['rows'][b][k], 9) for k in ('pifia','fallo','parcial','exito','critico')] for b in BONUS]) for cid in CARDS}
dups = {}
for cid, s in sig.items():
    dups.setdefault(s, []).append(cid)
print('=== casillas mecánicamente idénticas ===')
for s, ids in dups.items():
    if len(ids) > 1:
        print('  ', ' == '.join('%s (%s)' % (i, CARDS[i][1]) for i in ids))

print('\n=== resumen (bono 0) ===')
print('%-7s %-22s %-12s %6s %6s %6s %6s %6s' % ('id', 'nombre', 'casilla', 'pifia', 'crit', 'gana', 'limpio', 'span'))
for cid in CARDS:
    d = data[cid]; r = d['rows'][0]
    print('%-7s %-22s %-12s %5.1f%% %5.1f%% %5.1f%% %5.1f%% %5.1f%%' % (
        cid, d['name'], d['cell'], 100*d['pifia'], 100*d['critico'], 100*r['gana'], 100*r['limpio'], 100*d['span']))

# session feel: 30 rolls per session at bonus +1
import math
print('\n=== sensación por sesión (30 tiradas, bono +1) ===')
for cid in CARDS:
    r = data[cid]['rows'][1]
    p, c = data[cid]['pifia'], data[cid]['critico']
    print('%-7s pifias %.1f  críticos %.1f  P(al menos 1 pifia) %4.0f%%  éxitos %.0f%%' % (
        cid, 30*p, 30*c, 100*(1-(1-p)**30), 100*r['gana']))

# how much the character sheet matters: P(win) at -2 vs +4
json.dump(data, open('grid_probs.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('\ngrid_probs.json escrito')
