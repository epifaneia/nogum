# -*- coding: utf-8 -*-
"""Los recordatorios de la ficha cuentan las Llaves, el x100 y el techo."""
import io, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
F = 'app4_body.html'
s = io.open(F, encoding='utf-8').read()

OLD = """<li>' + esc(t('Por debajo: imposible, salvo con una Llave (arma, debilidad, ayuda…). Con Llave tiras normal.','Below: impossible, unless you have a Key (weapon, weakness, help…). With a Key you roll as normal.')) + '</li></ul></div>';"""
NEW = """<li>' + esc(t('Por debajo: imposible, salvo con una Llave (arma, debilidad, ayuda…). Con Llave tiras normal.','Below: impossible, unless you have a Key (weapon, weakness, help…). With a Key you roll as normal.')) + '</li><li>' + esc(t('Cada nivel multiplica por cien tu alcance. Un nivel de diferencia son dos ceros: por eso no hay tirada.','Each level multiplies your reach by a hundred. One level of difference is two zeros: that is why there is no roll.')) + '</li><li>' + esc(t('Una Llave es una Disciplina para siempre, o un Ámbito entero durante una escena. Subir más contra lo mismo: 1, 4, 9 Llaves.','A Key is one Discipline for ever, or a whole Sphere for one scene. Climbing further against the same thing: 1, 4, 9 Keys.')) + '</li><li>' + esc(t('El techo lo pone el universo; la Llave es la excepción pactada.','The ceiling is set by the universe; the Key is the agreed exception.')) + '</li></ul></div>';
  h += '<div class="rbox"><h3>' + esc(t('Equipo y Llaves','Equipment and Keys')) + '</h3><ul><li>' + esc(t('Tres cerrojos: el dinero (tu nivel en Recursos, el Acceso del objeto), el permiso narrativo y las Llaves si rompe la Rejilla.','Three locks: money (your Resources level, the item’s Access), narrative permission, and Keys if it breaks the Grid.')) + '</li><li>' + esc(t('Lo robado o prestado funciona una escena entera gratis; después, se paga o se deja.','Looted or borrowed gear works free for a whole scene; after that you pay for it or leave it.')) + '</li><li>' + esc(t('Monedero por defecto: 1 Llave por sesión. Es el mando de potencia de la campaña.','Default wallet: 1 Key per session. It is the campaign’s power dial.')) + '</li></ul></div>';"""
assert OLD in s
s = s.replace(OLD, NEW)
io.open(F, 'w', encoding='utf-8').write(s)
print('recordatorios al dia')
