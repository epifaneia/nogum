# -*- coding: utf-8 -*-
"""Añade al Cuaderno de Diseño las decisiones del taller de palancas."""
import io, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
s = io.open('frag_editorial.html', encoding='utf-8').read()
assert 'ED-18' not in s, 'ya aplicado'

ROWS = """<tr><td>El cuadrante de siete tarjetas</td><td>El panel de seis tarjetas más recetas queda sustituido por siete tarjetas repartidas en un cuadrante de nueve sitios, con <strong>dos huecos a la vista</strong>. Antes, dos pares de casillas eran mecánicamente idénticas (optimista previsible = optimista neutral; opresivo neutral = opresivo caótico) y el eje del caos no hacía nada en cuatro de las nueve. Ahora una palanca por columna y la fila elige la dirección.</td><td><a href="#ch1-panel">1.4</a>, <a href="#maq-cuadrante">1.3 I</a></td></tr>
<tr><td class="num"><span class="flag ed">ED-18</span></td><td><strong>Regla única de naturales.</strong> «Mira el número que vas a usar: si es 1, pifia; si es 10, crítico.» Reproduce exactamente las cifras anteriores (mejor de dos: 1&nbsp;% y 19&nbsp;%, que era «doble 1» y «cualquier 10»; peor de dos: 19&nbsp;% y 1&nbsp;%) y elimina los casos especiales. La suma conserva su línea: 2–3 y 19–20. El autor descartó la versión literal (2 y 20, al 1&nbsp;%) porque dejaba a la Realista sin un solo momento memorable por sesión.</td><td><a href="#ch1-panel">1.4</a></td></tr>
<tr><td class="num"><span class="flag ed">ED-19</span></td><td><strong>La dificultad no es palanca de tono.</strong> Un número por lectura (6 y 11) y se acabó: mover la TN por escena es justo la fricción que el juego promete quitar. El tono se construye con las otras cuatro palancas. Solo las recetas explícitas la tocan (Tragedia, suma vs TN 14).</td><td><a href="#maq-palancas">1.3 G</a></td></tr>
<tr><td class="num"><span class="flag ed">ED-20</span></td><td><strong>El centro del eje es la costumbre, no la objetividad.</strong> La columna central es el dado plano porque es lo que hace casi todo el hobby (d20, d100), no porque sea el punto medio estadístico: de hecho es la lectura más aleatoria de todas. Decisión explícita del autor: el eje mide la distancia respecto a lo que la mesa espera.</td><td><a href="#maq-palancas">1.3 G</a></td></tr>
<tr><td class="num"><span class="flag ed">ED-21</span></td><td><strong>El centro caótico lleva las dos herramientas.</strong> Ni el ruido ni la zona de roce inclinan el tono, así que en la única casilla sin dirección se aplican juntas: pifia 1–2, coste 5–6, crítico 9–10. Resultado: los cinco resultados al 20&nbsp;%, la única distribución uniforme del juego. Esto cierra la duda histórica de las dos tarjetas (Pulp/Drama y Gonzo) que compartían casilla.</td><td><a href="#tono-nc">1.4</a></td></tr>
<tr><td>La esquina opresiva se queda como está</td><td>La Pesadilla mantiene el ruido: 36&nbsp;% de pifias y techo del 64&nbsp;% para el gran maestro. El autor decide no suavizarla y avisar en el manual: lo opresivo tiene público, aunque sea minoritario, y el terror bien jugado se juega en una noche, no en una campaña de un año.</td><td><a href="#tono-pc">1.4</a></td></tr>
<tr><td class="num"><span class="flag ed">ED-15</span> (revisada)</td><td>Las bandas de Agobio en Acelerado pasan a ser la zona de roce del manual completo: fallo ≤4, coste 5–6, éxito 7+ sobre el dado menor. Deja de estar pendiente de confirmación. Consecuencia: un profesional (+2) sale adelante el 64&nbsp;% de las veces, y un 36&nbsp;% sin pagar nada.</td><td><a href="#ac-reglas">Acelerado</a></td></tr>
"""

anchor = '</tbody></table></div>\n\n<h3 id="ed-abiertas">'
assert s.count(anchor) == 1
s = s.replace(anchor, ROWS + anchor)
s = s.replace('href="#t0"', 'href="#tono-nn"').replace('href="#t4"', 'href="#tono-pp"')
io.open('frag_editorial.html', 'w', encoding='utf-8').write(s)
print('cuaderno actualizado')
