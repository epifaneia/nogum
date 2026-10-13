# -*- coding: utf-8 -*-
"""Bloque 3: el Bazar aprende a decir que te cuesta.
Acceso en Recursos y coste en Llaves en la misma ficha tecnica, y se completan
las fichas a medias que dejo el borrador. ES y EN se parchean por posicion."""
import io, os, re, shutil, collections
os.chdir(os.path.dirname(os.path.abspath(__file__)))

ES, EN = 'frag_bazar.html', ('frag_bazar_a.en.html', 'frag_bazar_b.en.html')

# --- las 22 fichas a medias, por nombre espanol: (Esq, Abs)
FIX = {
    'Daga Ritual':                ('Total', 'Nula'),
    'Palanca':                    ('Total', 'Total'),
    'Carga Biótica':         ('Parcial', 'Nula'),
    'Interceptor V8':             ('Difícil (−2)', 'Máx 1'),
    'Bomba de Energía':      ('Nula', 'Nula'),
    'Báculo Sagrado':        ('Total', 'Total'),
    'Abanico Bancho':             ('Parcial', 'Total'),
    'Trampa para Osos':           ('Difícil (−2)', 'Máx 1'),
    'Amuleto Solar':              ('Nula', 'Nula'),
    'Coche Blindado':             ('Difícil (−2)', 'Máx 1'),
    'Armadura de Combate':        ('Parcial', 'Máx 1'),
    'Martillo Digno':             ('Total', 'Nula'),
    'Gema del Infinito':          ('Nula', 'Nula'),
    'Brazo Mecánico a Vapor': ('Total', 'Total'),
    'Baraja de Cartas Maldita':   ('Total', 'Nula'),
    'Reloj de Bolsillo Hipnótico': ('Nula', 'Voluntad'),
    'Tarta en la Cara':           ('Total', 'Nula'),
    'Escopeta Anudada':           ('Nula', 'Nula'),
    'Bomba Redonda Negra':        (None, 'Máx 1'),
    'Sierra de Suelo':            ('Difícil (−2)', 'Nula'),
    'Luz de Gas':                 ('Nula', 'Voluntad'),
    'Excomunión':            ('Nula', 'Nula'),
}
ESQ_EN = {'Total': 'Full', 'Parcial': 'Partial', 'Nula': 'None',
          'Difícil (−2)': 'Hard (−2)'}
ABS_EN = {'Total': 'Full', 'Nula': 'None', 'Máx 1': 'Max 1', 'Voluntad': 'Will'}

TAG = '<span class="tag">%s</span>'
BUMP2 = re.compile(r'implante|ciber|exoesqueleto|blindaje|militar|vehículo|nave|'
                   r'implant|cyber|exoskeleton|armour plating|military|vehicle|starship', re.I)
BUMP1 = re.compile(r'armadura|poción|artefacto|droga|mágic|ritual|reliquia|'
                   r'armour|potion|artefact|artifact|drug|magic|relic', re.I)


def acceso(dmg, esq, ab, eff, notes):
    """Nivel de Recursos que hace falta para tener esto. Derivado, no escrito a mano."""
    txt = dmg + ' ' + eff
    n = None
    m = re.search(r'Daño[^<]*?(\d)|Dmg[^<]*?(\d)', dmg)
    if m:
        n = int(m.group(1) or m.group(2))
    special = bool(re.search(r'Masivo|Absoluto|Infinito|Massive|Absolute|Infinite', txt))
    if special:
        a = 3
    elif n is None:
        a = 0
    elif n <= 1:
        a = 0
    elif n == 2:
        a = 1
    else:
        a = 2
    if re.search(r'(Esq|Dodge): *(Nula|None)', esq) or re.search(r'(Abs|Soak): *(Nula|None)', ab):
        a += 1
    blob = eff + ' ' + notes
    g = re.search(r'(?:Rejilla|Grid): *(?:Nivel|Level|Llave N|Key N) *(\d)', eff)
    if g and int(g.group(1)) >= 2:
        a = max(a, 3)
    elif n is None:
        if BUMP2.search(blob):
            a = max(a, 2)
        elif BUMP1.search(blob):
            a = max(a, 1)
    return max(0, min(3, a))


def llaves(eff):
    g = re.search(r'(?:Rejilla|Grid): *(?:Nivel|Level|Llave N|Key N) *(\d)', eff)
    if not g:
        return 0
    lv = int(g.group(1))
    return lv * lv if lv >= 2 else 0


def process(src, es, start_idx, fixlog):
    """Reescribe cada tabla de objetos; devuelve (texto, indice siguiente)."""
    idx = start_idx
    out, pos = [], 0
    for m in re.finditer(r'<tbody>(.*?)</tbody>', src, re.S):
        out.append(src[pos:m.start(1)])
        body, newrows, cur = m.group(1), [], 0
        for tr in re.finditer(r'<tr>.*?</tr>', body, re.S):
            newrows.append(body[cur:tr.start()])
            row = tr.group(0)
            tds = re.findall(r'<td[^>]*>(.*?)</td>', row, re.S)
            if len(tds) != 6:
                newrows.append(row)
                cur = tr.end()
                continue
            name = re.sub(r'<[^>]+>', '', tds[0]).strip()
            key = idx
            idx += 1
            dmg, esq, ab, eff, nt = tds[1], tds[2], tds[3], tds[4], tds[5]
            # 1. completar las fichas a medias
            fx = fixlog.get(key)
            if fx:
                e, a = fx
                if e and 'Esq:' not in esq and 'Dodge:' not in esq:
                    esq = TAG % (('Esq: ' if es else 'Dodge: ') + (e if es else ESQ_EN[e]))
                if a and 'Abs:' not in ab and 'Soak:' not in ab:
                    ab = TAG % (('Abs: ' if es else 'Soak: ') + (a if es else ABS_EN[a]))
            # 2. acceso y llaves, delante del efecto
            ac = acceso(dmg, esq, ab, eff, nt)
            lv = llaves(eff)
            tags = [TAG % (('Acceso ' if es else 'Access ') + str(ac))]
            if lv:
                tags.append(TAG % ('%d Llaves' % lv if es else '%d Keys' % lv))
            body_eff = eff if eff.strip() not in ('—', '-', '') else ''
            eff = ' '.join(tags) + ((' ' + body_eff) if body_eff else '')
            row = ('<tr><td>' + tds[0] + '</td><td>' + dmg + '</td><td>' + esq + '</td><td>'
                   + ab + '</td><td>' + eff + '</td><td>' + nt + '</td></tr>')
            newrows.append(row)
            cur = tr.end()
        newrows.append(body[cur:])
        out.append(''.join(newrows))
        pos = m.end(1)
    out.append(src[pos:])
    s = ''.join(out)
    if es:
        s = s.replace('<th>Rejilla / efecto</th>', '<th>Acceso / Rejilla</th>')
    else:
        s = s.replace('<th>Grid / Effect</th>', '<th>Access / Grid</th>')
    return s, idx


# --- localizar, en espanol, el indice global de cada ficha a medias
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
print('fichas a medias localizadas:', len(fixlog), 'de', len(FIX))

shutil.copyfile(ES, ES + '.bak_acc')
new, n = process(s, True, 0, fixlog)
io.open(ES, 'w', encoding='utf-8').write(new)
print('ES: objetos procesados', n)

i = 0
for f in EN:
    shutil.copyfile(f, f + '.bak_acc')
    t = io.open(f, encoding='utf-8').read()
    new, i = process(t, False, i, fixlog)
    io.open(f, 'w', encoding='utf-8').write(new)
print('EN: objetos procesados', i)

# --- control: reparto del acceso
c = collections.Counter(re.findall(r'<span class="tag">Acceso (\d)</span>', io.open(ES, encoding='utf-8').read()))
print('reparto de Acceso:', dict(sorted(c.items())))
print('objetos con coste en Llaves:', len(re.findall(r'<span class="tag">\d+ Llaves</span>',
                                                     io.open(ES, encoding='utf-8').read())))
