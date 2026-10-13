# -*- coding: utf-8 -*-
"""Segunda pasada del barrido de marcas.

La primera dejo lo gordo resuelto. Esto va a por lo que quedo:
  A. marcas y terminos registrados que siguen vivos
  B. destrozos gramaticales que dejo la primera pasada
  C. un typo del ingles que aparecio de paso

Criterio de los nombres: descriptivos y evocadores, en la linea de los que ya
funcionan en el Bazar («Martillo Digno», «Nube de los limpios de corazon»).
Se describe lo que el objeto HACE, no de donde viene.
"""
import io, os, re, shutil, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))

ES = ['app4_body.html', 'frag_bazar.html', 'frag_bazar_a.html', 'frag_cap8.html', 'frag_ch1a.html', 'frag_ch1b.html',
      'frag_ch2.html', 'frag_ch3.html', 'frag_ch4.html', 'frag_ch5.html', 'frag_ch67.html',
      'frag_math.html', 'frag_glosario.html', 'frag_intro.html', 'frag_acelerado.html',
      'p_tesis_es.html']
EN = ['app4_body.html', 'frag_bazar_a.en.html', 'frag_bazar_b.en.html', 'frag_cap8.en.html', 'frag_ch1a.en.html',
      'frag_ch1b.en.html', 'frag_ch2.en.html', 'frag_ch3.en.html', 'frag_ch4.en.html',
      'frag_ch5.en.html', 'frag_ch67.en.html', 'frag_math.en.html', 'frag_glosario.en.html',
      'frag_intro.en.html', 'frag_acelerado.en.html', 'p_tesis_en.html']

# (viejo_es, nuevo_es, viejo_en, nuevo_en, por que)
MARCAS = [
 # --- Opera espacial: «la Fuerza» es marca; el Flujo hace el mismo trabajo
 ('Empujón de Fuerza', 'Empujón del Flujo', 'Force Push', 'Flow Push', 'la Fuerza'),
 ('Rayo de la Fuerza', 'Rayo del Flujo', 'Force Lightning', 'Flow Lightning', 'la Fuerza'),
 ('Salto de Fuerza', 'Salto del Flujo', 'Force Jump', 'Flow Leap', 'la Fuerza'),
 # el ingles anadio «Force» donde el castellano no lo tiene
 ('Estrangular', 'Estrangular', 'Force Choke', 'Throat Grip', 'la Fuerza'),
 ('Fantasma de la Fuerza', 'Fantasma del Flujo', 'Force Ghost', 'Flow Ghost', 'la Fuerza'),
 ('Sable de Luz / Energía', 'Sable de Energía', 'Lightsaber / Energy Sword', 'Energy Sword', 'Lucasfilm'),
 ('Sable de Luz', 'Sable de Energía', 'Lightsaber', 'Energy Sword', 'Lucasfilm'),
 ('Carga Biótica', 'Carga Psiónica', 'Biotic Charge', 'Psionic Charge', 'termino de un videojuego'),
 # --- Superheroes
 ('Gema del Infinito (una sola)', 'Gema Primordial (una sola)',
  'Infinity Stone (just one)', 'Primordial Gem (just one)', 'Marvel'),
 ('Capa de Levitación', 'Manto que Levita', 'Cloak of Levitation', 'Levitating Mantle', 'Marvel'),
 ('Cubo Cósmico (fragmento)', 'Cubo de Poder Estelar (fragmento)',
  'Cosmic Cube (fragment)', 'Stellar Power Cube (fragment)', 'Marvel'),
 ('Suero de Supersoldado', 'Suero del Soldado Perfecto',
  'Super-Soldier Serum', 'Perfect Soldier Serum', 'Marvel'),
 ('Lazo de la Verdad', 'Cuerda de la Confesión', 'Lasso of Truth', 'Confession Rope', 'DC'),
 ('Cinturón de Utilidades', 'Cinturón de Artilugios', 'Utility Belt', 'Gadget Belt', 'DC'),
 ('Anillo de Poder', 'Anillo de Voluntad', 'Power Ring', 'Will Ring', 'DC'),
 ('Armadura de Combate (Iron)', 'Armadura de Combate Motorizada',
  'Combat Armour (Iron)', 'Powered Combat Armour', 'guino a Iron Man'),
 # --- Artes marciales
 ('Radar del Dragón', 'Radar de Reliquias', 'Dragon Radar', 'Relic Radar', 'Dragon Ball'),
 # --- prosa de los capitulos
 ('aprendiz jedi', 'aprendiz de la Orden', 'jedi apprentice', 'Order apprentice', 'Lucasfilm'),
 ('maestro jedi', 'maestro de la Orden', 'jedi master', 'Order master', 'Lucasfilm'),
 ('la protagonista de <em>Alien</em>', 'la última superviviente de la nave',
  'the protagonist of <em>Alien</em>', 'the last survivor on the ship', 'titulo de pelicula'),
 ('la kriptonita', 'la piedra de su propio mundo', 'kryptonite', 'the stone from his own world', 'DC'),
 ('Dungeons, dragons and loot', 'Dungeons, dragons and loot',
  'Dungeons, dragons and loot', 'Crypts, dragons and loot', 'demasiado cerca de D&D'),
]

# destrozos de la primera pasada: (patron, arreglo) en castellano
ROTOS = [
 ('Ballesta el gigante peludo', 'Ballesta del gigante peludo'),
 ('Pendientes pendientes de fusión', 'Pendientes de fusión'),
 ('Armadura el guerrero de otro planeta', 'Armadura del guerrero de otro planeta'),
]
ROTOS_EN = [
 ('Crossbow the hairy giant', 'Crossbow of the hairy giant'),
 ('Earrings earrings of fusion', 'Fusion Earrings'),
 ('Armour the warrior from another planet', 'Armour of the warrior from another planet'),
 ('What what you wrote on your sheet', 'What what you wrote on your sheet'),
]

seco = '--seco' in sys.argv
cambios = {}
for grupo, ficheros, idx in (('es', ES, 0), ('en', EN, 2)):
    for f in ficheros:
        if not os.path.exists(f):
            continue
        s = io.open(f, encoding='utf-8').read()
        o = s
        for fila in MARCAS:
            a, b = fila[idx], fila[idx + 1]
            if a == b or a not in s:
                continue
            n = s.count(a)
            s = s.replace(a, b)
            cambios.setdefault((a, b, fila[4]), 0)
            cambios[(a, b, fila[4])] += n
        for a, b in (ROTOS if grupo == 'es' else ROTOS_EN):
            if a == b or a not in s:
                continue
            n = s.count(a)
            s = s.replace(a, b)
            cambios.setdefault((a, b, 'roto'), 0)
            cambios[(a, b, 'roto')] += n
        if s != o and not seco:
            if not os.path.exists(f + '.bak_marcas2'):
                shutil.copyfile(f, f + '.bak_marcas2')
            io.open(f, 'w', encoding='utf-8').write(s)

print('%-34s -> %-34s  %-22s x' % ('ANTES', 'DESPUES', 'MOTIVO'))
print('-' * 100)
tot = 0
for (a, b, por), n in sorted(cambios.items(), key=lambda x: x[0][2]):
    print('%-34s -> %-34s  %-22s %d' % (a[:34], b[:34], por[:22], n))
    tot += n
print('-' * 100)
print('total de sustituciones: %d' % tot)
if seco:
    print('(ensayo: no se ha escrito nada)')
