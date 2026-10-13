# -*- coding: utf-8 -*-
"""Tercera pasada: el ingles, que se habia quedado atras.

El castellano llevaba el eufemismo y la traduccion inglesa habia vuelto a poner
la marca original: «Nube de los limpios de corazon» se habia traducido como
«Flying Nimbus», y «Semilla del viejo de la montana» como «Senzu Bean». El
criterio aqui es traducir **el eufemismo castellano**, no el termino de origen.
"""
import io, os, shutil, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))

FICHEROS = ['frag_bazar_a.en.html', 'frag_bazar_b.en.html', 'frag_cap8.en.html',
            'frag_ch1a.en.html', 'frag_ch1b.en.html', 'frag_ch2.en.html', 'frag_ch3.en.html',
            'frag_ch4.en.html', 'frag_ch5.en.html', 'frag_ch67.en.html', 'frag_math.en.html',
            'frag_glosario.en.html', 'frag_intro.en.html', 'frag_acelerado.en.html',
            'p_tesis_en.html', 'app4_body.html']

# (ingles de ahora, ingles nuevo, de donde venia, el castellano que traduce)
PARES = [
 # --- opera espacial
 ('The hairy giant Bowcaster (energy)', "The Hairy Giant's Crossbow (energy)", 'Lucasfilm',
  'Ballesta del gigante peludo'),
 ('Stormtrooper Armour', 'Assault Trooper Armour', 'Lucasfilm', 'Armadura de Soldado de Asalto'),
 ('Thermal Detonator', 'Thermal Grenade', 'Lucasfilm', 'Granada Termica'),
 ('Saber Throw', 'Sword Throw', 'coherencia con Energy Sword', 'Lanzamiento de Sable'),
 # --- artes marciales: el castellano ya estaba limpio y el ingles no
 ('Fist of the North Star', 'Fist of a Hundred Fists', 'manga', 'El Puno de los Cien Punos'),
 ('The Eight Gates (Release)', 'The Eight Points (Release)', 'manga', 'Los Ocho Puntos'),
 ('Energy Wavehameha (beam)', 'Two-Handed Energy Wave (beam)', 'manga', 'Onda de energia a dos manos'),
 ('Destructo Disc', 'Destroyer Disc', 'manga', 'Disco Destructor'),
 ('Instant Transmission', 'Instant Teleport', 'manga', 'Teletransporte Instantaneo'),
 ('Spirit Bomb (Borrowed-energy bomb)', 'Energy Bomb (Borrowed-energy bomb)', 'manga',
  'Bomba de Energia'),
 ('Namekian Regeneration', 'Regeneration (final merge)', 'manga', 'Regeneracion (union definitiva)'),
 ('Flying Nimbus', 'Cloud of the Pure of Heart', 'manga', 'Nube de los limpios de corazon'),
 ('Power Pole', 'Sacred Staff', 'manga', 'Baculo Sagrado'),
 ('Senzu Bean', "The Mountain Hermit's Bean", 'manga', 'Semilla del viejo de la montana'),
 ('Z Sword', 'The Blade Nobody Can Lift', 'manga', 'El filo que nadie puede levantar'),
 ('Potara Earrings', 'Fusion Earrings', 'manga', 'Pendientes de fusion'),
 ('Bansho Fan', 'Fan of the Three Storms', 'manga', 'Abanico de las tres tormentas'),
 ('The warrior from another planet Armour', "The Armour of the Warrior from Another Planet",
  'gramatica rota', 'Armadura del guerrero de otro planeta'),
]

# y un destrozo del castellano que aparecio al parear
ES_ROTO = [('Regeneración unión definitiva', 'Regeneración (unión definitiva)')]

seco = '--seco' in sys.argv
cuenta = {}
for f in FICHEROS:
    if not os.path.exists(f):
        continue
    s = io.open(f, encoding='utf-8').read()
    o = s
    for a, b, por, es in PARES:
        if a in s:
            cuenta[(a, b, por)] = cuenta.get((a, b, por), 0) + s.count(a)
            s = s.replace(a, b)
    if s != o and not seco:
        if not os.path.exists(f + '.bak_marcasen'):
            shutil.copyfile(f, f + '.bak_marcasen')
        io.open(f, 'w', encoding='utf-8').write(s)

for f in ('frag_bazar.html', 'frag_bazar_a.html', 'app4_body.html'):
    if not os.path.exists(f):
        continue
    s = io.open(f, encoding='utf-8').read()
    o = s
    for a, b in ES_ROTO:
        if a in s:
            cuenta[(a, b, 'gramatica rota')] = cuenta.get((a, b, 'gramatica rota'), 0) + s.count(a)
            s = s.replace(a, b)
    if s != o and not seco:
        io.open(f, 'w', encoding='utf-8').write(s)

print('%-38s -> %-36s %-18s x' % ('ANTES (ingles)', 'DESPUES', 'ORIGEN'))
print('-' * 102)
tot = 0
for (a, b, por), n in sorted(cuenta.items(), key=lambda x: x[0][2]):
    print('%-38s -> %-36s %-18s %d' % (a[:38], b[:36], por[:18], n))
    tot += n
print('-' * 102)
print('total: %d' % tot)
if seco:
    print('(ensayo)')
