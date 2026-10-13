# -*- coding: utf-8 -*-
"""Revision 2: enlaces, marcas, bilinguismo y codigo muerto."""
import io, os, re, sys, json
os.chdir(os.path.dirname(os.path.abspath(__file__)))
ERR = []


def err(t):
    ERR.append(t); print('  ERROR  ' + t)


SALIDAS = ['out3/nogum_tesis.html', 'out3/nogum_juego.html', 'out3/nogum_acelerado.html',
           'out3/nogum_cuaderno.html', 'out3/nogum_app.html']

print('=' * 72)
print(' 1. Enlaces internos que no llevan a ninguna parte')
print('=' * 72)
for f in SALIDAS:
    s = io.open(f, encoding='utf-8').read()
    ids = set(re.findall(r'\bid="([^"]+)"', s))
    anc = set(re.findall(r'href="#([^"]+)"', s))
    rotos = sorted(a for a in anc if a and a not in ids)
    # los enlaces entre manuales van a otro fichero, no son anclas de este
    # los href que viven dentro del script de la pagina no son anclas del documento
    rotos = [r for r in rotos if not r.startswith('http') and "' +" not in r]
    print('  %-28s %4d anclas, %4d destinos, rotos: %d' % (os.path.basename(f), len(anc), len(ids), len(rotos)))
    if rotos:
        err('%s: %s' % (os.path.basename(f), ', '.join(rotos[:10])))

print()
print('=' * 72)
print(' 2. Marcas registradas en lo publicable')
print('=' * 72)
try:
    from marcas_data import MARCAS
    nombres = []
    for grupo in (MARCAS.values() if isinstance(MARCAS, dict) else MARCAS):
        for e in (grupo if isinstance(grupo, list) else [grupo]):
            n = e[0] if isinstance(e, (list, tuple)) else e
            if isinstance(n, str) and len(n) > 3:
                nombres.append(n)
except Exception as e:
    nombres = []
    print('  (no he podido leer marcas_data: %s)' % e)
EXTRA = ['Dungeons', 'Vampire: The Masquerade', 'Shadowrun', 'Cthulhu', 'Warhammer', 'Star Wars',
         'Blades in the Dark', 'Cyberpunk 2020', 'Pathfinder', 'Fate Core', 'Mundodisco', 'Discworld',
         'Pratchett', 'Tolkien', 'Lovecraft', 'Eclipse Phase', 'Paranoia', 'Exalted', 'Rifts',
         'Mutants & Masterminds', 'Legend of the Five Rings', 'Stranger Things', 'Buffy']
busca = sorted(set([n for n in nombres if len(n) > 4] + EXTRA))
total = 0
for f in SALIDAS:
    s = io.open(f, encoding='utf-8').read()
    hits = [(n, s.count(n)) for n in busca if n in s]
    if hits:
        total += sum(h[1] for h in hits)
        err('%s: %s' % (os.path.basename(f), ', '.join('%s x%d' % h for h in hits[:8])))
print('  %d menciones de marca en los cinco productos' % total)

print()
print('=' * 72)
print(' 3. Castellano sin traducir dentro de la app')
print('=' * 72)
app = io.open('app4_body.html', encoding='utf-8').read()
js = app[app.index('<script>\n(function()'):]
# cadenas con acentos o signos espanoles fuera de un t(...) o de una tabla bilingue
sospech = []
for m in re.finditer(r"'([^'\\\n]{6,90})'", js):
    txt = m.group(1)
    if not re.search(r'[áéíóúñ¿¡üÁÉÍÓÚÑ«»]', txt):
        continue
    ini = max(0, m.start() - 70)
    ctx = js[ini:m.start()]
    # bien: t('es','en')  ·  ['es','en']  ·  esc(pick(...))
    if re.search(r"t\(\s*$", ctx) or re.search(r"\[\s*$", ctx) or re.search(r",\s*$", ctx):
        continue
    sospech.append(txt)
print('  cadenas en castellano sin pareja aparente: %d' % len(sospech))
for x in sospech[:12]:
    print('     ' + x[:84])
# el otro lado: t('x','x') con las dos iguales y acento (olvido de traducir)
ig = [a for a, b in re.findall(r"t\('([^']{4,70})','([^']{4,70})'\)", js) if a == b and re.search(r'[áéíóúñ¿¡]', a)]
print('  t() con los dos idiomas identicos y acentuados: %d' % len(ig))
for x in ig[:8]:
    print('     ' + x[:84])

print()
print('=' * 72)
print(' 4. Funciones declaradas y nunca usadas en la app')
print('=' * 72)
decl = re.findall(r'\nfunction ([A-Za-z_$][\w$]*)\s*\(', js)
muertas = []
for n in sorted(set(decl)):
    usos = len(re.findall(r'\b' + re.escape(n) + r'\b', js))
    if usos <= 1:
        muertas.append(n)
print('  funciones: %d   sin usar: %d' % (len(set(decl)), len(muertas)))
if muertas:
    print('     ' + ', '.join(muertas))
# variables de primer nivel sin usar
vdecl = re.findall(r'\nvar ([A-Z][A-Z0-9_]{2,})\s*=', js)
vm = [n for n in sorted(set(vdecl)) if len(re.findall(r'\b' + re.escape(n) + r'\b', js)) <= 1]
print('  tablas en mayusculas sin usar: %s' % (', '.join(vm) if vm else 'ninguna'))

print()
print('=' * 72)
print(' 5. Paridad entre fragmentos castellano e ingles')
print('=' * 72)
import glob
for es in sorted(glob.glob('frag_*.html')):
    if '.en.' in es or '.bak' in es:
        continue
    base = es[:-5]
    cands = [base + '.en.html'] + ([base.replace('_bazar', '_bazar_a') + '.en.html'] if 'bazar' in base else [])
    en = next((c for c in cands if os.path.exists(c)), None)
    if not en:
        if 'bazar' not in es and 'editorial' not in es and 'descartados' not in es and 'trazabilidad' not in es:
            print('  %-26s sin pareja inglesa' % es)
        continue
    a, b = io.open(es, encoding='utf-8').read(), io.open(en, encoding='utf-8').read()
    da = abs(len(a) - len(b)) * 100.0 / max(len(a), 1)
    marca = '  <-- muy distinto de tamano' if da > 35 else ''
    print('  %-26s es %6d  en %6d  dif %4.0f%%%s' % (es, len(a), len(b), da, marca))

print()
print('=' * 72)
print('ERRORES: %d' % len(ERR))
print('=' * 72)
