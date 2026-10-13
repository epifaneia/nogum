# -*- coding: utf-8 -*-
"""Segunda pasada del Bazar: el Acceso no se pone donde no se compra con dinero,
y la inevitabilidad solo encarece cuando de verdad no se puede esquivar."""
import io, os, re, shutil, collections
os.chdir(os.path.dirname(os.path.abspath(__file__)))

ES, EN = 'frag_bazar.html', ('frag_bazar_a.en.html', 'frag_bazar_b.en.html')
for f in (ES,) + EN:
    shutil.copyfile(f + '.bak_acc', f)          # volvemos al original

exec(open('w_bazar.py', encoding='utf-8').read().split('# --- las 22')[0])  # nada util, solo imports

FIX = {
    'Daga Ritual': ('Total', 'Nula'), 'Palanca': ('Total', 'Total'),
    'Carga Biótica': ('Parcial', 'Nula'), 'Interceptor V8': ('Difícil (−2)', 'Máx 1'),
    'Bomba de Energía': ('Nula', 'Nula'), 'Báculo Sagrado': ('Total', 'Total'),
    'Abanico Bancho': ('Parcial', 'Total'), 'Trampa para Osos': ('Difícil (−2)', 'Máx 1'),
    'Amuleto Solar': ('Nula', 'Nula'), 'Coche Blindado': ('Difícil (−2)', 'Máx 1'),
    'Armadura de Combate': ('Parcial', 'Máx 1'), 'Martillo Digno': ('Total', 'Nula'),
    'Gema del Infinito': ('Nula', 'Nula'), 'Brazo Mecánico a Vapor': ('Total', 'Total'),
    'Baraja de Cartas Maldita': ('Total', 'Nula'),
    'Reloj de Bolsillo Hipnótico': ('Nula', 'Voluntad'),
    'Tarta en la Cara': ('Total', 'Nula'), 'Escopeta Anudada': ('Nula', 'Nula'),
    'Bomba Redonda Negra': (None, 'Máx 1'), 'Sierra de Suelo': ('Difícil (−2)', 'Nula'),
    'Luz de Gas': ('Nula', 'Voluntad'), 'Excomunión': ('Nula', 'Nula'),
}
ESQ_EN = {'Total': 'Full', 'Parcial': 'Partial', 'Nula': 'None', 'Difícil (−2)': 'Hard (−2)'}
ABS_EN = {'Total': 'Full', 'Nula': 'None', 'Máx 1': 'Max 1', 'Voluntad': 'Will'}
TAG = '<span class="tag">%s</span>'

# tablas que no se compran: son lo que ya eres
SKIP = re.compile(r'Poderes|Mutaciones|Artes marciales|Técnicas de ki|Superpoderes|'
                  r'Arsenal social|Objetos cósmicos|'
                  r'Powers|Mutations|Martial arts|Ki techniques|Superpowers|Social arsenal|Cosmic', re.I)
BUMP2 = re.compile(r'implante|ciber|exoesqueleto|blindaje|militar|vehículo|nave|kevlar|'
                   r'implant|cyber|exoskeleton|military|vehicle|starship', re.I)
BUMP1 = re.compile(r'armadura|poción|artefacto|droga|mágic|ritual|reliquia|'
                   r'armour|potion|artefact|artifact|drug|magic|relic', re.I)


def acceso(dmg, esq, ab, eff, notes):
    txt = dmg + ' ' + eff
    m = re.search(r'Daño[^<]*?(\d)|Dmg[^<]*?(\d)', dmg)
    n = int(m.group(1) or m.group(2)) if m else None
    if re.search(r'Masivo|Absoluto|Infinito|Massive|Absolute|Infinite', txt):
        a = 3
    elif n is None:
        a = 0
    elif n <= 1:
        a = 0
    elif n == 2:
        a = 1
    else:
        a = 2
    if re.search(r'(Esq|Dodge): *(Nula|None)', esq):
        a += 1
    g = re.search(r'(?:Rejilla|Grid): *(?:Nivel|Level|Llave N|Key N) *(\d)', eff)
    if g and int(g.group(1)) >= 2:
        a = max(a, 3)
    elif n is None:
        blob = eff + ' ' + notes
        if BUMP2.search(blob):
            a = max(a, 2)
        elif BUMP1.search(blob):
            a = max(a, 1)
    return max(0, min(3, a))


def llaves(eff):
    g = re.search(r'(?:Rejilla|Grid): *(?:Nivel|Level|Llave N|Key N) *(\d)', eff)
    lv = int(g.group(1)) if g else 0
    return lv * lv if lv >= 2 else 0


def process(src, es, idx, fixlog):
    out, pos, head = [], 0, ''
    for m in re.finditer(r'<h4[^>]*>(.*?)</h4>|<tbody>(.*?)</tbody>', src, re.S):
        if m.group(1) is not None:
            head = re.sub(r'<[^>]+>', '', m.group(1))
            continue
        skip = bool(SKIP.search(head))
        out.append(src[pos:m.start(2)])
        body, newrows, cur = m.group(2), [], 0
        for tr in re.finditer(r'<tr>.*?</tr>', body, re.S):
            newrows.append(body[cur:tr.start()])
            row = tr.group(0)
            tds = re.findall(r'<td[^>]*>(.*?)</td>', row, re.S)
            if len(tds) != 6:
                newrows.append(row); cur = tr.end(); continue
            key = idx; idx += 1
            dmg, esq, ab, eff, nt = tds[1], tds[2], tds[3], tds[4], tds[5]
            fx = fixlog.get(key)
            if fx:
                e, a = fx
                if e and 'Esq:' not in esq and 'Dodge:' not in esq:
                    esq = TAG % (('Esq: ' + e) if es else ('Dodge: ' + ESQ_EN[e]))
                if a and 'Abs:' not in ab and 'Soak:' not in ab:
                    ab = TAG % (('Abs: ' + a) if es else ('Soak: ' + ABS_EN[a]))
            if not skip:
                tags = [TAG % (('Acceso ' if es else 'Access ') + str(acceso(dmg, esq, ab, eff, nt)))]
                lv = llaves(eff)
                if lv:
                    tags.append(TAG % ('%d Llaves' % lv if es else '%d Keys' % lv))
                body_eff = '' if eff.strip() in ('—', '-', '') else eff
                eff = ' '.join(tags) + ((' ' + body_eff) if body_eff else '')
            newrows.append('<tr><td>' + tds[0] + '</td><td>' + dmg + '</td><td>' + esq
                           + '</td><td>' + ab + '</td><td>' + eff + '</td><td>' + nt + '</td></tr>')
            cur = tr.end()
        newrows.append(body[cur:])
        out.append(''.join(newrows))
        pos = m.end(2)
    out.append(src[pos:])
    s = ''.join(out)
    s = s.replace('<th>Rejilla / efecto</th>', '<th>Acceso / Rejilla</th>') if es else \
        s.replace('<th>Grid / Effect</th>', '<th>Access / Grid</th>')
    return s, idx


s = io.open(ES, encoding='utf-8').read()
fixlog, idx = {}, 0
for m in re.finditer(r'<tbody>(.*?)</tbody>', s, re.S):
    for tr in re.finditer(r'<tr>.*?</tr>', m.group(1), re.S):
        tds = re.findall(r'<td[^>]*>(.*?)</td>', tr.group(0), re.S)
        if len(tds) != 6:
            continue
        name = re.sub(r'<[^>]+>', '', tds[0]).strip()
        for k, v in FIX.items():
            if name.startswith(k):
                fixlog[idx] = v
        idx += 1
print('fichas a medias:', len(fixlog))

new, n = process(s, True, 0, fixlog)
io.open(ES, 'w', encoding='utf-8').write(new)
i = 0
for f in EN:
    t = io.open(f, encoding='utf-8').read()
    new, i = process(t, False, i, fixlog)
    io.open(f, 'w', encoding='utf-8').write(new)
print('objetos:', n, '/', i)
txt = io.open(ES, encoding='utf-8').read()
print('reparto de Acceso:', dict(sorted(collections.Counter(re.findall(r'tag">Acceso (\d)<', txt)).items())))
print('con coste en Llaves:', collections.Counter(re.findall(r'tag">(\d+) Llaves<', txt)))
print('sin Acceso (poderes):', 294 - sum(collections.Counter(re.findall(r'tag">Acceso (\d)<', txt)).values()))
