# -*- coding: utf-8 -*-
"""Piezas sueltas: el catalogo generico de las cuatro categorias, con su precio
en las tres monedas. Se genera en los dos idiomas desde los mismos datos."""
import io, os, shutil
os.chdir(os.path.dirname(os.path.abspath(__file__)))

T = lambda x: '<span class="tag">%s</span>' % x
DASH = '—'


def cost(acc=None, pts=0, keys=0, grid=None, es=True):
    out = []
    if acc is not None:
        out.append(T(('Acceso ' if es else 'Access ') + str(acc)))
    if pts:
        out.append(T('%d punto%s' % (pts, 's' if pts > 1 else '') if es else '%d point%s' % (pts, 's' if pts > 1 else '')))
    if keys:
        out.append(T('%d Llaves' % keys if es else '%d Keys' % keys))
    if grid:
        out.append(T(('Rejilla: Nivel ' if es else 'Grid: Level ') + str(grid)))
    return ' '.join(out)


#  (nombre_es, nombre_en, dmg_es, dmg_en, esq_es, esq_en, abs_es, abs_en,
#   (acc, pts, keys, grid), nota_es, nota_en)
ARMAS = [
 ('Hoja corta', 'Short blade', 'Daño 1', 'Dmg 1', 'Esq: Total', 'Dodge: Full', 'Abs: Total', 'Soak: Full', (0, 0, 0, None),
  'El cuchillo, la daga, el punzón. Existe en todos los mundos y no cuesta nada tenerlo.',
  'The knife, the dagger, the shiv. It exists in every world and costs nothing to own.'),
 ('Hoja larga', 'Long blade', 'Daño 2', 'Dmg 2', 'Esq: Total', 'Dodge: Full', 'Abs: Total', 'Soak: Full', (1, 0, 0, None),
  'La espada, el machete, el hacha de mano.', 'The sword, the machete, the hand axe.'),
 ('Arma a dos manos', 'Two-handed weapon', 'Daño 3', 'Dmg 3', 'Esq: Fácil (+2)', 'Dodge: Easy (+2)', 'Abs: Máx 1', 'Soak: Max 1', (1, 0, 0, None),
  'Enorme y lenta: hace un destrozo, pero se ve venir.', 'Huge and slow: it does terrible damage, but you see it coming.'),
 ('Arma de maestro armero', 'Master-forged weapon', 'Daño 2', 'Dmg 2', 'Esq: Total', 'Dodge: Full', 'Abs: Total', 'Soak: Full', (2, 1, 0, None),
  'El punto compra <strong>+1 a dar</strong>, y es un suelo: no le hace nada a quien ya tiene Armas +1.',
  'The point buys <strong>+1 to hit</strong>, and it is a floor: it does nothing for someone who already has Weapons +1.'),
 ('Proyectil ligero', 'Light projectile', 'Daño 1', 'Dmg 1', 'Esq: Total', 'Dodge: Full', 'Abs: Total', 'Soak: Full', (1, 0, 0, None),
  'Arco corto, pistola pequeña, dardo.', 'Short bow, small pistol, dart.'),
 ('Proyectil pesado', 'Heavy projectile', 'Daño 2', 'Dmg 2', 'Esq: Difícil (−2)', 'Dodge: Hard (−2)', 'Abs: Máx 1', 'Soak: Max 1', (2, 0, 0, None),
  'Ballesta, rifle, arma larga: a distancia no hay dónde esconderse.', 'Crossbow, rifle, long gun: at range there is nowhere to hide.'),
 ('Arma de área', 'Area weapon', 'Daño 2', 'Dmg 2', 'Esq: Parcial', 'Dodge: Partial', 'Abs: Máx 1', 'Soak: Max 1', (2, 0, 0, None),
  'Fuego, metralla, aliento. Aunque esquives, te comes 1.', 'Fire, shrapnel, breath. Even if you dodge, you take 1.'),
 ('Arma inevitable', 'Inevitable weapon', 'Daño 3', 'Dmg 3', 'Esq: Nula', 'Dodge: None', 'Abs: Nula', 'Soak: None', (3, 0, 0, None),
  'El rifle supersónico, el rayo, la bala que ya te dio. No existe en todos los mundos, y donde existe lo cambia todo.',
  'The supersonic rifle, the beam, the bullet that already hit you. It does not exist in every world, and where it does it changes everything.'),
 ('Arma que abre la armadura', 'Armour-opener', 'Daño 2', 'Dmg 2', 'Esq: Total', 'Dodge: Full', 'Abs: Nula', 'Soak: None', (2, 0, 0, None),
  'Monofilo, perforante, ácido, maldita. Se esquiva bien; pararla, nunca.',
  'Monofilament, armour-piercing, acid, cursed. Easy to dodge; impossible to stop.'),
 ('Arma aturdidora', 'Stunning weapon', 'Daño 1 (aturde)', 'Dmg 1 (stun)', 'Esq: Total', 'Dodge: Full', 'Abs: Nula', 'Soak: None', (1, 0, 0, None),
  'Porra, táser, hechizo de sueño. Hace poco daño y mucha diferencia.',
  'Baton, taser, sleep spell. Little damage, a lot of difference.'),
 ('Arma de asedio', 'Siege weapon', 'Daño 3', 'Dmg 3', 'Esq: Nula', 'Dodge: None', 'Abs: Nula', 'Soak: None', (3, 0, 4, 2),
  'Cañón, ariete, bola de fuego de guerra: alcanza al nivel 2, así que cuesta 4 Llaves.',
  'Cannon, battering ram, war-grade fireball: it reaches level 2, so it costs 4 Keys.'),
 ('Arma silenciosa', 'Silent weapon', 'Daño 1', 'Dmg 1', 'Esq: Nula (por sorpresa)', 'Dodge: None (by surprise)', 'Abs: Total', 'Soak: Full', (2, 0, 0, None),
  'Solo es inevitable si nadie te ha visto llegar. Si te ven, se lee Esq: Total.',
  'Only inevitable if nobody saw you coming. If they do, read it as Dodge: Full.'),
]

DEFENSAS = [
 ('Ropa reforzada', 'Reinforced clothing', (0, 0, 0, None),
  'Absorbe 1 punto cuando el arma lo permite.', 'Soaks 1 point when the weapon allows it.'),
 ('Cota ligera', 'Light mail', (1, 1, 0, None),
  '<strong>+1 a defender.</strong> El punto es el entrenamiento de llevarla puesta.',
  '<strong>+1 to defend.</strong> The point is the training of wearing it.'),
 ('Placas completas', 'Full plate', (2, 2, 0, None),
  '<strong>+2 a defender</strong> y −2 a Sigilo. Lo segundo es gratis: es lo que la armadura <em>es</em>.',
  '<strong>+2 to defend</strong> and −2 to Stealth. The second is free: it is what the armour <em>is</em>.'),
 ('Escudo', 'Shield', (1, 1, 0, None),
  '<strong>+1 a defender</strong> y, una vez por escena, puedes reaccionar contra un arma de <span class="tag">Abs: Nula</span>.',
  '<strong>+1 to defend</strong> and, once per scene, you may react against a <span class="tag">Soak: None</span> weapon.'),
 ('Blindaje de combate', 'Combat armour', (3, 2, 0, None),
  '<strong>+2 a defender</strong> y absorbe 1 punto fijo. Material militar: Acceso 3.',
  '<strong>+2 to defend</strong> and soaks 1 fixed point. Military hardware: Access 3.'),
 ('Cobertura portátil', 'Portable cover', (1, 0, 0, None),
  'Mientras la usas, quien te dispara tira con <span class="tag">Esq: Difícil</span>… para él.',
  'While you use it, whoever shoots at you rolls at <span class="tag">Dodge: Hard</span>… for them.'),
 ('Campo de fuerza', 'Force field', (3, 0, 1, None),
  'Absorbe 2 puntos fijos y se agota al hacerlo. Para lo que nada para, y por eso es una Llave.',
  'Soaks 2 fixed points and burns out doing it. It stops what nothing stops, and that is why it is a Key.'),
 ('Amuleto de protección', 'Protective charm', (2, 0, 1, None),
  'Te deja reaccionar contra lo sobrenatural, que es lo que nadie puede hacer sin él.',
  'It lets you react against the supernatural, which is what nobody can do without it.'),
 ('Yelmo', 'Helm', (0, 0, 0, None),
  'Ignoras el primer aturdimiento de la escena.', 'You ignore the first stun of the scene.'),
 ('Piel endurecida', 'Hardened skin', (None, 1, 0, None),
  'Artefacto o poder: <strong>+1 a defender</strong> siempre, y no te lo pueden quitar. Si además nunca falla, es Potenciado: 2 puntos.',
  'Artefact or power: <strong>+1 to defend</strong> always, and it cannot be taken from you. If it also never fails, it is Enhanced: 2 points.'),
]

VEHICULOS = [
 ('Montura', 'Mount', (1, 0, 0, None),
  'Te mueve campo a través y no pelea por ti.', 'It carries you cross-country and does not fight for you.'),
 ('Vehículo de calle', 'Street vehicle', (1, 0, 0, None),
  'Mueve al grupo. Decorado, salvo que lo uses como arma.', 'It moves the group. Scenery, unless you use it as a weapon.'),
 ('Vehículo blindado', 'Armoured vehicle', (2, 0, 4, 2),
  'Atropella con <span class="tag">Daño 3</span> y opera en nivel 2: por eso cuesta Llaves.',
  'It runs people down at <span class="tag">Dmg 3</span> and operates at level 2: hence the Keys.'),
 ('Vehículo de combate', 'Combat vehicle', (3, 0, 4, 2),
  'Armas integradas <span class="tag">Daño 3</span> <span class="tag">Esq: Difícil</span>. Militar: Acceso 3.',
  'Integrated weapons <span class="tag">Dmg 3</span> <span class="tag">Dodge: Hard</span>. Military: Access 3.'),
 ('Aeronave ligera', 'Light aircraft', (2, 0, 1, None),
  'El permiso es volar. No opera por encima de tu nivel: solo te lleva donde no se puede ir.',
  'The permission is flight. It does not operate above your level: it just takes you where you cannot go.'),
 ('Nave de carga', 'Freighter', (3, 0, 9, 3),
  'Un hogar que cruza mundos y opera en nivel 3.', 'A home that crosses worlds and operates at level 3.'),
 ('Exoesqueleto', 'Exoskeleton', (3, 0, 9, 3),
  'Te conviertes en un tanque mientras lo llevas: Sincronización (<a href="#ch2-rejilla">2.4</a>).',
  'You become a tank while you wear it: Synchronisation (<a href="#ch2-rejilla">2.4</a>).'),
 ('Montura de guerra', 'War mount', (1, 0, 0, None),
  'Carga con <span class="tag">Daño 2</span> y se asusta como cualquiera.',
  'It charges at <span class="tag">Dmg 2</span> and spooks like anything else.'),
 ('Embarcación', 'Vessel', (2, 0, 4, 2),
  'Mueve a decenas de personas: eso ya es nivel 2.', 'It moves dozens of people: that is level 2 already.'),
 ('Vehículo de rescate', 'Rescue vehicle', (1, 0, 0, None),
  'Permiso: estabilizar a un herido grave en movimiento.', 'Permission: stabilising a badly wounded person on the move.'),
]

#  (nombre_es, nombre_en, que_da_es, que_da_en, cuenta_es, cuenta_en, ajuste_es, ajuste_en, precio_es, precio_en)
PODERES = [
 ('Ojo que atraviesa', 'Piercing eye', 'Ves a través de una pared', 'You see through a wall',
  'permiso: 1 Llave', 'permission: 1 Key', 'Completo', 'Complete', '1 Llave', '1 Key'),
 ('Alas', 'Wings', 'Vuelas', 'You fly',
  'permiso: 1 Llave', 'permission: 1 Key', 'Completo', 'Complete', '1 Llave', '1 Key'),
 ('Pulmón ajeno', 'Borrowed lung', 'Respiras donde no se puede', 'You breathe where you cannot',
  'permiso: 1 Llave', 'permission: 1 Key', 'Completo', 'Complete', '1 Llave', '1 Key'),
 ('Lengua común', 'Common tongue', 'Entiendes cualquier idioma', 'You understand any language',
  'permiso: 1 Llave', 'permission: 1 Key', 'Completo', 'Complete', '1 Llave', '1 Key'),
 ('Capa de invisibilidad', 'Cloak of invisibility', 'No te ven mientras la llevas puesta', 'You are unseen while wearing it',
  'permiso: 1 Llave', 'permission: 1 Key', 'Limitado', 'Limited', '1 Llave · Acceso 2', '1 Key · Access 2'),
 ('Invisibilidad a voluntad', 'Invisibility at will', 'Desapareces cuando quieres', 'You vanish whenever you want',
  'permiso: 1 Llave', 'permission: 1 Key', 'Potenciado', 'Enhanced', '2 Llaves', '2 Keys'),
 ('Velo absoluto', 'Absolute veil', 'Nada ni nadie puede detectarte', 'Nothing and nobody can detect you',
  'Rejilla 3 contra la detección: 9', 'Grid 3 against detection: 9', 'Completo', 'Complete', '9 Llaves', '9 Keys'),
 ('Mano que cura', 'Healing hand', 'Cierras heridas sin material', 'You close wounds with no equipment',
  'permiso: 1 Llave', 'permission: 1 Key', 'Completo', 'Complete', '1 Llave', '1 Key'),
 ('Carne que vuelve', 'Returning flesh', 'Recuperas un bloque por escena', 'You recover one block per scene',
  'permiso: 1 Llave', 'permission: 1 Key', 'Potenciado', 'Enhanced', '2 Llaves', '2 Keys'),
 ('Fuerza de sala', 'Room-strength', 'Te enfrentas a decenas a la vez', 'You take on dozens at once',
  'Rejilla 2 física: 4', 'Physical Grid 2: 4', 'Completo', 'Complete', '4 Llaves', '4 Keys'),
 ('Fuerza de edificio', 'Building-strength', 'Tiras abajo un edificio', 'You bring down a building',
  'Rejilla 3 física: 9', 'Physical Grid 3: 9', 'Completo', 'Complete', '9 Llaves', '9 Keys'),
 ('Descarga', 'Discharge', 'Haces daño sin arma: <span class="tag">Daño 2</span> <span class="tag">Esq: Parcial</span>',
  'You deal damage with no weapon: <span class="tag">Dmg 2</span> <span class="tag">Dodge: Partial</span>',
  'permiso: 1 Llave', 'permission: 1 Key', 'Completo', 'Complete', '1 Llave', '1 Key'),
 ('Oído de pensamientos', 'Mind-ear', 'Lees una mente', 'You read one mind',
  'permiso: 1 Llave', 'permission: 1 Key', 'Completo', 'Complete', '1 Llave', '1 Key'),
 ('Oído de multitud', 'Crowd-ear', 'Lees a una sala entera a la vez', 'You read a whole room at once',
  'Rejilla 2 mental: 4', 'Mental Grid 2: 4', 'Completo', 'Complete', '4 Llaves', '4 Keys'),
 ('Paso corto', 'Short step', 'Te teleportas a donde alcanza la vista', 'You teleport to wherever you can see',
  'permiso: 1 Llave', 'permission: 1 Key', 'Completo', 'Complete', '1 Llave', '1 Key'),
 ('Instante robado', 'Stolen instant', 'Una acción extra por escena', 'One extra action per scene',
  'permiso: 1 Llave', 'permission: 1 Key', 'Potenciado', 'Enhanced', '2 Llaves', '2 Keys'),
 ('Voz de máquina', 'Machine voice', 'Le hablas a una máquina y obedece', 'You speak to a machine and it obeys',
  'permiso: 1 Llave', 'permission: 1 Key', 'Completo', 'Complete', '1 Llave', '1 Key'),
 ('Mando de multitud', 'Crowd command', 'Una muchedumbre hace lo que dices', 'A crowd does what you say',
  'Rejilla 2 social: 4', 'Social Grid 2: 4', 'Completo', 'Complete', '4 Llaves', '4 Keys'),
 ('Piel contra el elemento', 'Elemental skin', 'El fuego, el frío o el vacío no te tocan', 'Fire, cold or vacuum do not touch you',
  'permiso: 1 Llave', 'permission: 1 Key', 'Completo', 'Complete', '1 Llave', '1 Key'),
 ('Ojo del mentiroso', 'Liar’s eye', 'Sabes cuándo te mienten', 'You know when you are being lied to',
  '<strong>esto no es un poder</strong>: es Empatía', '<strong>this is not a power</strong>: it is Empathy',
  '—', '—', '1 punto', '1 point'),
 ('Medio segundo', 'Half a second', 'Ves el instante siguiente: +2 a iniciativa y a esquivar',
  'You see the next instant: +2 to initiative and to dodging',
  '<strong>tampoco es un permiso</strong>: son dos bonos', '<strong>not a permission either</strong>: it is two bonuses',
  '—', '—', '2 puntos', '2 points'),
]

HEAD = ('<div class="tw"><table class="t">\n<thead><tr><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr></thead>\n<tbody>\n')
H_ES = HEAD % ('Objeto', 'Daño', 'Esq', 'Abs', 'Acceso / Rejilla', 'Notas')
H_EN = HEAD % ('Item', 'Dmg', 'Dodge', 'Soak', 'Access / Grid', 'Notes')


def row(name, dmg, esq, ab, c, note):
    f = lambda x: T(x) if x and x != DASH else DASH
    return ('<tr><td><strong>%s</strong></td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>\n'
            % (name, f(dmg), f(esq), f(ab), c or DASH, note))


def build(es):
    h = []
    h.append('<h3 id="bz-piezas">%s</h3>\n' % ('Piezas sueltas: el catálogo genérico' if es else 'Loose parts: the generic catalogue'))
    h.append('<p>%s</p>\n' % (
        'Lo de arriba son diez mundos con sus marcas y su sabor. Esto es lo contrario: <strong>las piezas desnudas</strong>, sin ambientación y con el precio hecho en las tres monedas. Sirven en cualquier universo, valen de plantilla para fabricar lo tuyo y son la respuesta rápida cuando alguien saca algo que no está en ninguna lista.'
        if es else
        'Above are ten worlds with their brands and their flavour. This is the opposite: <strong>the bare parts</strong>, with no setting and with the price already worked out in all three currencies. They work in any universe, they serve as templates for building your own, and they are the quick answer when somebody produces something that is on no list at all.'))

    h.append('<h4>%s</h4>\n' % ('Armas' if es else 'Weapons'))
    h.append(H_ES if es else H_EN)
    for it in ARMAS:
        n, ne, d, de, e, ee, a, ae, c, no, noe = it
        h.append(row(n if es else ne, d if es else de, e if es else ee, a if es else ae,
                     cost(c[0], c[1], c[2], c[3], es), no if es else noe))
    h.append('</tbody></table></div>\n')

    h.append('<h4>%s</h4>\n' % ('Defensas' if es else 'Defences'))
    h.append('<p class="small">%s</p>\n' % (
        'Una defensa no ataca, así que no lleva las tres etiquetas de combate: lleva lo que hace y lo que cuesta.'
        if es else
        'A defence does not attack, so it does not carry the three combat tags: it carries what it does and what it costs.'))
    h.append((HEAD % ('Objeto', 'Qué hace', 'Precio', 'Notas', '', '')).replace('<th></th><th></th>', '').replace(
        '<th>Qué hace</th><th>Precio</th><th>Notas</th>', '<th>Qué hace y qué cuesta</th><th>Notas</th>')
        if False else
        ('<div class="tw"><table class="t">\n<thead><tr><th>%s</th><th>%s</th><th>%s</th></tr></thead>\n<tbody>\n'
         % (('Objeto', 'Qué hace y qué cuesta', 'Notas') if es else ('Item', 'What it does and what it costs', 'Notes'))))
    for n, ne, c, no, noe in DEFENSAS:
        h.append('<tr><td><strong>%s</strong></td><td>%s</td><td>%s</td></tr>\n'
                 % (n if es else ne, cost(c[0], c[1], c[2], c[3], es) or DASH, no if es else noe))
    h.append('</tbody></table></div>\n')

    h.append('<h4>%s</h4>\n' % ('Vehículos' if es else 'Vehicles'))
    h.append('<div class="tw"><table class="t">\n<thead><tr><th>%s</th><th>%s</th><th>%s</th></tr></thead>\n<tbody>\n'
             % (('Vehículo', 'Qué hace y qué cuesta', 'Notas') if es else ('Vehicle', 'What it does and what it costs', 'Notes')))
    for n, ne, c, no, noe in VEHICULOS:
        h.append('<tr><td><strong>%s</strong></td><td>%s</td><td>%s</td></tr>\n'
                 % (n if es else ne, cost(c[0], c[1], c[2], c[3], es) or DASH, no if es else noe))
    h.append('</tbody></table></div>\n')

    h.append('<h4>%s</h4>\n' % ('Artefactos y poderes' if es else 'Artefacts and powers'))
    h.append('<p class="small">%s</p>\n' % (
        'Un artefacto es un poder con asas: se puede perder. Un poder innato es lo mismo sin asas, y cuesta igual. Las dos últimas filas están ahí a propósito: son las trampas más comunes.'
        if es else
        'An artefact is a power with handles: it can be lost. An innate power is the same thing without handles, and costs the same. The last two rows are there on purpose: they are the commonest traps.'))
    h.append('<div class="tw"><table class="t">\n<thead><tr><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th class="num">%s</th></tr></thead>\n<tbody>\n'
             % (('Poder', 'Qué da', 'La cuenta', 'Ajuste', 'Precio') if es else ('Power', 'What it gives', 'The sum', 'Adjustment', 'Price')))
    for p in PODERES:
        n, ne, g, ge, c, ce, aj, aje, pr, pre = p
        h.append('<tr><td><strong>%s</strong></td><td>%s</td><td>%s</td><td>%s</td><td class="num">%s</td></tr>\n'
                 % (n if es else ne, g if es else ge, c if es else ce, aj if es else aje, pr if es else pre))
    h.append('</tbody></table></div>\n')
    h.append('<p>%s</p>\n' % (
        'Con esto y el taller de arriba ya puedes poner precio a cualquier cosa. Si lo tuyo se parece a una de estas piezas, cuesta lo mismo; si es media pieza, redondea hacia arriba; y si no se parece a nada, desglósalo y ajústalo.'
        if es else
        'With this and the workshop above you can price anything. If yours resembles one of these parts, it costs the same; if it is half a part, round up; and if it resembles nothing at all, itemise it and adjust.'))
    return ''.join(h)


def put(f, txt, anchor):
    shutil.copyfile(f, f + '.bak_piezas')
    s = io.open(f, encoding='utf-8').read()
    k = s.index(anchor)
    s = s[:k] + txt + '\n' + s[k:]
    io.open(f, 'w', encoding='utf-8').write(s)
    print(' ', f, 'ok')


put('frag_bazar.html', build(True), '<h3 id="bz-resumen">')
put('frag_bazar_b.en.html', build(False), '<h3 id="bz-resumen">')
print('piezas:', len(ARMAS) + len(DEFENSAS) + len(VEHICULOS) + len(PODERES))
