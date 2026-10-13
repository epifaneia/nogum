# -*- coding: utf-8 -*-
"""Barrido de vocabulario retirado y de invariantes, sobre lo PUBLICADO.

Mira los cuatro productos tal como salen, no los fragmentos: lo que importa es
lo que lee el lector. El Cuaderno queda fuera porque es el diario de edicion y
ahi la historia es legitima. En la app se recorta el canon embebido por lo
mismo: es bitacora.
"""
import io, os, re, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))

PROD = [('La Apuesta', 'out3/art/tesis.html'),
        ('Juego', 'out3/art/juego.html'),
        ('Acelerado', 'out3/art/acelerado.html'),
        ('App', 'out3/nogum_app.html')]

MUERTOS = [
    (r'Bola de nieve', 'la tarjeta se llama Comedia negra (T134)'),
    # «se abre con maña» es castellano corriente y vale. Lo retirado es el
    # NOMBRE del escalon, que se escribiria asi:
    (r'la Maña\b|Maña\s*\(?[−-]1|[−-]1\s*\(?Maña', 'el escalon -1 se llama Torpe (T131)'),
    (r'[Mm]odo Agobio', 'el Acelerado ya no tiene Agobio (T146)'),
    (r'[Mm]odo Épico', 'ese modo se llama Optimista (T146)'),
    (r'Dread mode', 'Accelerated has no Dread mode (T146)'),
    (r'Cáscara|Núcleo\b', 'la vida es Letal/Tactico/Guerra (T133)'),
    (r'Regla del Margen', 'retirada (ED-1)'),
    (r'Cifras corregidas', 'seccion eliminada (T137)'),
    # Citar lo que decia el manual original es legitimo y va marcado (ED-B1).
    # Lo que no vale es que una regla NUESTRA reparta 3 o mas.
    (r'(?:Daño|Dmg|Damage)[ \t]*:?[ \t]*[3-9]\b(?![^.]{0,25}\[Inevitable\])', 'el dano maximo es +2; encima, la Parca (T131)'),
    (r'son cinco piezas|is five pieces', 'el pack es de cuatro (T135)'),
    (r'tres modos de tono|three tone modes', 'son cuatro (T146)'),
    (r'Tesis filosófica|Philosophical thesis', 'el producto es La Apuesta (T144)'),
    (r'bancos de música|music banks', 'la musica es solo arrastrar (T151)'),
]

INV = [
    ('Juego', r'\+4', 'la Firma a +4'),
    ('Juego', r'\bTorpe\b', 'el escalon Torpe'),
    ('Juego', r'La Parca', 'la Parca'),
    ('Juego', r'Letal', 'vida Letal'),
    ('Juego', r'Comedia negra', 'la tarjeta Comedia negra'),
    ('Acelerado', r'Optimista', 'modo Optimista'),
    ('Acelerado', r'\bTerror\b', 'modo Terror'),
    ('Acelerado', r'\bCaos\b', 'modo Caos'),
    ('La Apuesta', r'feliz accidente', 'el feliz accidente'),
]

fallos = []
textos, crudos = {}, {}
for nom, ruta in PROD:
    if not os.path.exists(ruta):
        fallos.append('FALTA %s' % ruta); continue
    s = io.open(ruta, encoding='utf-8').read()
    if nom == 'App':
        s = re.sub(r'<script type="application/json" id="canon">.*?</script>', '', s, flags=re.S)
    crudos[nom] = s
    # Los bloques se separan con salto de linea y lo de dentro con espacio. Sin
    # esto, el final de una celda se pega al principio de la siguiente y salen
    # coincidencias que no existen («...por su Daño» + «3. Te protege de algo?»).
    s = re.sub(r'</?(?:p|li|td|th|tr|div|h[1-6]|section|table|dt|dd|figcaption)\b[^>]*>', '\n', s)
    textos[nom] = re.sub(r'<[^>]+>', ' ', s)

L = '=' * 68
print(L); print(' 1 - VOCABULARIO RETIRADO'); print(L)
limpio = True
for pat, por in MUERTOS:
    for nom in textos:
        hits = list(re.finditer(pat, textos[nom]))
        if hits:
            limpio = False
            ctx = re.sub(r'\s+', ' ', textos[nom][max(0, hits[0].start() - 55):hits[0].start() + 65]).strip()
            print('  [%-10s] x%-3d %s' % (nom, len(hits), por))
            print('      ...%s...' % ctx)
            fallos.append('%s: %s' % (nom, por))
if limpio:
    print('  nada. Los cuatro productos estan limpios.')

print(); print(L); print(' 2 - INVARIANTES'); print(L)
for donde, pat, que in INV:
    n = len(re.findall(pat, textos.get(donde, '')))
    print('  %-4s [%-10s] %-28s x%d' % ('ok' if n else 'MAL', donde, que, n))
    if not n:
        fallos.append('%s: falta %s' % (donde, que))

print(); print(L); print(' 3 - ENLACES E IDENTIFICADORES'); print(L)
for nom in crudos:
    s = crudos[nom]
    # los productos llevan los dos idiomas en <template>: cada id sale dos veces
    # a proposito. Y paper.js construye anclas en JS, que no son anclas. Fuera.
    s = re.sub(r'<template id="src-en">.*?</template>', '', s, flags=re.S)
    s = re.sub(r'<script(?![^>]*application/json).*?</script>', '', s, flags=re.S)
    ids = re.findall(r'\sid="([^"]+)"', s)
    sid = set(ids)
    rotas = sorted({h for h in re.findall(r'href="#([^"]+)"', s) if h not in sid})
    art = len(re.findall(r'href="https://claude\.ai/artifact/', s))
    loc = len(re.findall(r'href="(?:\.\./)?NOGUM_[a-z]+\.html"', s))
    rep = sorted({i for i in ids if ids.count(i) > 1})
    print('  %-11s rotas:%-3d claude.ai:%-3d locales:%-3d ids repetidos:%d'
          % (nom, len(rotas), art, loc, len(rep)))
    if rotas: fallos.append('%s: anclas rotas %s' % (nom, rotas[:6]))
    if loc:   fallos.append('%s: %d enlaces locales en la version de artefacto' % (nom, loc))
    if rep:   fallos.append('%s: ids repetidos %s' % (nom, rep[:6]))

print(); print(L)
if fallos:
    print(' RESULTADO: %d problema(s)' % len(fallos))
    for x in fallos: print('  - ' + x)
else:
    print(' RESULTADO: limpio.')
print(L)
