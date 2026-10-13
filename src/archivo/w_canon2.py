# -*- coding: utf-8 -*-
"""Canon y Cuaderno: las tres monedas (ED-36) y el Ajuste (ED-37)."""
import io, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# ---- CANON
f = 'CANON.md'
s = io.open(f, encoding='utf-8').read()
old = '- Marcador de disposición (autor, 17 sep):'
new = """- **ED-36. Tres monedas, tres cosas distintas** (el taller del Bazar, 8.3). Un objeto puede pedir hasta tres pagos y cada uno sale de su sitio: **Recursos** paga TENERLO (y con el las etiquetas: Dano, Esq, Abs, alcance), **puntos de habilidad** pagan que te haga MEJOR (cualquier bono a una tirada: +1 defender, +1 dar; 1 punto por +1, igual que la piramide), y **Llaves** pagan que te deje hacer lo IMPOSIBLE (permisos a 1 Llave, niveles de Rejilla a N^2). La cota de malla no tiene nada de extraordinario en su mundo: Recursos + puntos, cero Llaves. Los bonos de equipo son SUELO y no suma (cascada, se usa el escalon mas alto), el punto compra el papel y no la pieza concreta, y el equipo come de los 12/14 puntos: en partidas de poderes se sube el presupuesto, con el aviso de que mas puntos = menos especializacion.
  - Dos pruebas: si una habilidad ya lo hace, no es poder, es bono (sentir mentiras = Empatia). Si te hace ganar a cosas de un nivel por encima, no es permiso, es Rejilla.
  - Cuatro categorias: arma, defensa, vehiculo, artefacto (+ util para lo demas, que solo cuesta Acceso).
  - Cajones de Recursos: −2 nada · +0 Acceso 0 · +1 Acceso 1 · +2 Acceso 2 · +3 Acceso 2-3 · +4 Acceso 3. Un escalon por encima una vez por arco, pagando con una complicacion (el tiron de Recursos).
- **ED-37. El Ajuste**: lo que la cuenta no sabe decir. Limitado (÷2) · Completo (×1) · Potenciado (×2) · Desatado (×3), sobre puntos y Llaves, nunca sobre el Acceso. Redondeo hacia arriba y minimo 1. NO es un dial de cuatro potencias del mismo poder: es el corrector de lo que el desglose no ha pagado, y **solo paga lo que la cuenta no ha pagado ya**. Calibracion: cuantas escenas resuelve esto que no hayas pagado. Se pacta al comprarlo, se escribe al lado del poder y se puede volver a etiquetar si el juego demuestra que estaba mal tasado. Si algo pide mas de ×3, es un nivel de Rejilla no visto, o es decorado. Ejemplo canonico: capa de invisibilidad (1 Llave, Limitado) · invisibilidad a voluntad (2, Potenciado) · indetectable (Rejilla 3 = 9, Completo), donde se ve que la etiqueta se retira en cuanto la cuenta sabe describir el poder.
- Bazar: 347 objetos (294 de ambientacion + 53 piezas genericas de las cuatro categorias con precio hecho), cada uno etiquetado con su categoria, e indice cruzado al final del apendice. En el Acelerado el equipo solo cuesta Recursos.
- Marcador de disposición (autor, 17 sep):"""
assert old in s
s = s.replace(old, new)
io.open(f, 'w', encoding='utf-8').write(s)
print('canon ok')

# ---- CUADERNO
f = 'frag_editorial.html'
s = io.open(f, encoding='utf-8').read()
ROWS = """<tr><td class="num"><span class="flag ed">ED-36</span></td><td><strong>Tres monedas, tres cosas distintas.</strong> Recursos paga tenerlo, los puntos pagan que te haga mejor y las Llaves pagan que te deje hacer lo imposible. La decisión del autor que lo ordena todo: el bono de la cota de malla se paga con <em>puntos</em>, no con Llaves, porque en su mundo una cota no tiene nada de extraordinario y lo que te da es exactamente lo que te habría dado entrenar. Con eso el Bazar entero se vuelve usable: casi todo cuesta solo dinero, y solo pagas de un monedero cuando el objeto te mejora o rompe el techo.</td><td><a href="#bz-fabrica">8.3</a></td></tr>
<tr><td class="num"><span class="flag ed">ED-37</span></td><td><strong>El Ajuste.</strong> Limitado, Completo, Potenciado y Desatado no son cuatro potencias del mismo poder: son el corrector de lo que el desglose no sabe decir, y multiplican ÷2, ×1, ×2 y ×3 sobre puntos y Llaves. Con dos salvaguardas que el autor pidió implícitamente al describirlo como subjetivo: <strong>solo paga lo que la cuenta no ha pagado ya</strong>, y se puede volver a etiquetar si el juego demuestra que estaba mal tasado. El ejemplo de la invisibilidad —capa, a voluntad, indetectable— enseña la propiedad bonita: la etiqueta se retira sola en cuanto la cuenta sabe describir el poder.</td><td><a href="#bz-fabrica">8.3</a></td></tr>
<tr><td>El taller y las piezas sueltas</td><td>Las reglas de fabricación van <strong>delante</strong> del catálogo, que pasa a ser una tabla de equivalencias: miras lo que cuesta algo parecido y extrapolas. Detrás van 53 piezas genéricas sin ambientación —12 armas, 10 defensas, 10 vehículos y 21 artefactos y poderes— con el precio hecho en las tres monedas, y un índice cruzado que ordena los 347 objetos por categoría y por Acceso. Las dos últimas filas de la tabla de poderes son trampas a propósito: «saber si te mienten» es Empatía y «ver el instante siguiente» son dos bonos; ninguna de las dos es un poder.</td><td><a href="#bz-piezas">8.3</a></td></tr>
"""
anchor = '<tr><td>El menú de la pifia</td>'
assert anchor in s
s = s.replace(anchor, ROWS + anchor)
io.open(f, 'w', encoding='utf-8').write(s)
print('cuaderno ok')
