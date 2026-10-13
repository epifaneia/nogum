# -*- coding: utf-8 -*-
"""El canon aprende la economia de la ficha: ED-27 a ED-35."""
import io, os, shutil
os.chdir(os.path.dirname(os.path.abspath(__file__)))
F = 'CANON.md'
shutil.copyfile(F, F + '.bak_llaves')
s = io.open(F, encoding='utf-8').read()

# --- 1. el presupuesto viejo deja de ser el vigente
old = '- Presupuesto recomendado: 10 puntos (ajustable: «juega con los números»).'
new = ('- Presupuesto: **12 puntos**, o **14** si el universo tiene Arcano (ED-31). La razon es la proporcion: '
       'sin magia hay 40 casillas (4 ambitos x 10) y con magia 50, asi que 12/40 y 14/50 dejan la misma escasez '
       '(~30 %). Los 10 puntos del borrador quedan SUPERADOS. Sigue siendo ajustable: «juega con los numeros».\n'
       '- **Bote aparte** (ED-31): ademas de los puntos, cada personaje recibe +1 nivel de Rejilla en un Ambito '
       '**o** 5 Llaves propias. No hay cambio entre los dos botes en ninguna direccion, para que no aparezca el '
       'heroe de Rejilla sin oficio. Economia: un nivel de Rejilla cubre 10 casillas por 5 monedas y una Llave '
       'cubre 1 por 1 — «la libertad se paga al doble».\n'
       '- Precio de las Firmas = ser Nulidad: cubrir los cuatro Ambitos cuesta 4 puntos y deja 8, que son '
       'exactamente dos Grandes Maestros. Lo que cuesta el agujero lo decide la TARJETA: 51 % lo saca adelante '
       'en Epica/Pulp, 36 % en Realista, 30 % en Primera marcha/Bola, 9 % en Angustia/Pesadilla.')
assert old in s
s = s.replace(old, new)

# --- 2. capitulo 2: x100, techo y Llave comprada
old = '- 2.5 Síntesis: Bono = ANCLA; Rejilla = VELA.'
new = """- **El x100 (ED-29)**: cada nivel de Rejilla multiplica por cien el ALCANCE (a cuanta gente llegas, que tamano de problema tocas): x1 persona, x100 sala, x10.000 edificio, x1.000.000 ciudad, x100.000.000 pais. Es alcance, no literalidad (un Fisico 2 no levanta cien veces mas peso). Un nivel de diferencia son dos ceros, y por eso no hay tirada. Regla opcional sin validar: x10 por nivel para campanas de callejon.
- **Techo de Rejilla por universo (ED-30)**: el nivel inicial lo pone la campana y el TECHO lo pone el genero. Cada una de las 20 recetas (8.4) trae su techo por ambito; en la app estan en la tabla TECHO. La Rejilla sube con la historia pero contra ese techo, y la Llave es la excepcion pactada («en cyberpunk no puedes tener un ingenio por cien, pero si el exploit que funciona contra esa IA»). Un techo de jugador no es un techo de mundo: los PNJ legendarios pueden estar por encima.
- **Que cubre una Llave (ED-27)**: una Disciplina para siempre, **o** un Ambito entero durante una ESCENA (si la Llave es muy concreta). Se elige la forma al comprarla. La Llave ancha se ata a una escena, no a un enemigo.
- **Llave propia y prestada (ED-28)**: propia = comprada (creacion o monedero), permanente, escrita con objetivo y nivel, pactada antes de empezar. Prestada = la da el DJ por trama o ingenio, dura una escena, no sube de nivel y NO se apunta. Traspaso: lo de un solo uso se declara; lo permanente se libera y el otro lo paga de su monedero. Regla de pulgar: «lo que se lleva en la mano se presta; lo que se lleva en la cabeza, no».
- **Escalera de Llaves (ED-32)**: subir n niveles contra la misma cosa cuesta n^2 Llaves (1, 4, 9, 16, 25). Alternativa opcional, la escalera llana 3n-2 (1, 4, 7, 10, 13), que coincide en los dos primeros peldanos. Con las 5 Llaves del bote, nadie empieza por encima de +2.
- 2.5 Síntesis: Bono = ANCLA; Rejilla = VELA."""
assert old in s
s = s.replace(old, new)

# --- 3. anadidos posteriores
old = '- Marcador de disposición (autor, 17 sep):'
new = """- **ED-33. Los dos monederos**: la experiencia son dos bolsas independientes, puntos de habilidad y Llaves, con ritmos distintos acordados en la sesion cero. Cinco velocidades (quietos / +1 por arco / +1 por sesion / +2 por sesion / +5 por arco) y una segunda pregunta (todos por igual, o por meritos, y el merito SUMA encima de una base). Ritmo por defecto de Llaves: 1 por sesion. El monedero de Llaves es el mando de potencia de la campana, porque los puntos saturan en +4 y las Llaves no saturan nunca: «si quieres que la campana escale, abre el grifo de las Llaves, no el de los puntos».
- **ED-34. Los tres cerrojos del equipo**: dinero (nivel de Recursos, escrito en la ficha tecnica como Acceso 0-3), permiso narrativo, y Llaves si el objeto rompe la Rejilla (cuesta el cuadrado del nivel al que llega: Llave N3 = 9 Llaves). Lo robado, prestado o conseguido en la ficcion funciona UNA ESCENA gratis; despues se paga o se deja. La Llave del equipo se puede perder; la Llave propia eres tu.
- **ED-35. La lacra es la cicatriz de un bloque lleno**: los dones y las lacras no se compran, ocurren. Cuando se llena un bloque de la barra Mental o Espiritual y el personaje se cura, el -2 se va y queda una lacra con nombre (sin numero, con consecuencias). Jugarla en contra propia es una de las siete cosas que se premian.
- Acceso del Bazar: los 294 objetos llevan Acceso derivado del dano y la rareza en una pasada (0 cotidiano, 1 arma seria, 2 militar, 3 lo que no deberia existir); el DJ puede mover cualquiera un escalon. Las tablas de poderes (Fuerza, ki, disciplinas, superpoderes, toon, arsenal social) NO llevan Acceso: describen lo que ya eres.
- Acelerado: se lo lleva todo (12/14 puntos, bote aparte, Llaves compradas, x100). Los pregenerados gastan 12 (Kira, sin magia) y 14 (Tomas, Ysolde).
- Marcador de disposición (autor, 17 sep):"""
assert old in s
s = s.replace(old, new)

io.open(F, 'w', encoding='utf-8').write(s)
print('canon actualizado:', len(s), 'bytes')
