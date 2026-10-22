# Revisión R1 · Introducción, Las seis ideas, caps. 0–4

Ficheros revisados (y los únicos que he editado): `fA_ideas_intro_0_1.html`, `fC_cap2.html`, `fD_cap3.html`, `fE_cap4.html`. Contraste con CANON.md 1–215, MAPA §4, PLAN, y lectura de coherencia contra `fF_cap5.html`, `fG_cap7.html`, `fI_cap6_cap8.html`, `fJ2_cap9b.html` y `fB_apendices.html`.

Comprobaciones mecánicas tras los cambios:
- **HTML**: los cuatro ficheros, equilibrados (parser sin errores ni etiquetas abiertas).
- **Enlaces**: todos los `href="#…"` de los cuatro existen en algún fragmento de `v2/`, salvo `#acelerado`, que `assemble_v2.py` reescribe al Acelerado actual (no está roto en el montaje). Los números de los enlaces coinciden con la numeración nueva; no queda ninguna referencia a la vieja. Ningún otro fragmento enlaza a un id de caps. 0–4 que no exista.
- **Ids**: ninguno repetido en todo `v2/` (el nuevo `ch2-atributos` no choca con `ch7-atributos`).
- **Canon**: no he encontrado nada en los cuatro que contradiga CANON 1–215. Las dos tablas aprobadas (3.3 y 4.8) están literales.

## 1. Lo que he cambiado

### fC_cap2.html (cap. 2)
1. **2.2, el porqué de la pirámide** (MAPA §4, encargo). Después del primer párrafo de `ch2-piramide` he puesto el ejemplo de Historia y la confederación de Gaya (`frag_ch3.html` 3–4) y el recuadro **«No hay atributos»** (`frag_ch3.html` 5–8), con id `ch2-atributos`. Uso la versión corregida de G: «no existen la Fuerza, los Reflejos ni la Inteligencia». La vieja decía también «Destreza», y en NOGUM Destreza es un Dominio. → **R2**: quitar la copia de 7.2 (`fG_cap7.html` 20–24: el recuadro `ch7-atributos` y el párrafo de Historia/Gaya) y dejar una frase con enlace a `ch2-piramide` (o `ch2-atributos`).
2. **2.5, la fórmula de la tirada** (un solo sitio). He quitado el recuadro `ch2-tirada`, que repetía la fórmula de `ch1-formula`. En su lugar va un párrafo (con el mismo id `ch2-tirada`, por si alguien lo enlaza) que nombra la fórmula, enlaza a 1.3 y dice qué entra en el bono total. Lo de «se tira de −2 a +4» ya estaba en `ch2-limites`, justo debajo.
3. **2.5, la TN.** «El número objetivo (TN) lo fija la tarjeta… 6… 11… y no se mueve» → «La TN la fija la tarjeta de tono y no se mueve (1.3)», con enlace a `ch1-tn`. Vive en 1.3, y aquí solo se cita.
4. **2.5, entrada.** «si se queda corta, el Director decide si hay tirada» → «si baja de −2, el Director decide si hay derecho a tirada». Es la Aclaración del 22 oct tal cual: «quedarse corta» era ambiguo.
5. **2.5, `ch2-limites`.** «el ancla está para que nunca lo sea» → «para que no lo sea». Es por la voz (sin absolutos) y por coherencia con 0.6, que ya decía «no».
6. **2.2, primera frase.** «la única forma de tener un bono en la ficha» → «un bono **de habilidad**». Los modificadores permanentes (prótesis, cicatrices, en el mismo capítulo) también están en la hoja.
7. **2.3, Arcano.** «magia, la Fuerza, psiónica» → «magia, el ki, psiónica». «La Fuerza», con mayúscula, es un nombre con copyright. El ki ya sale en 4.4.

### fA_ideas_intro_0_1.html (Introducción, ideas, caps. 0–1)
8. **0.6, aside T21–T22** («¿Tu Gran Maestro va a acertar casi siempre en la Épica?… Cambia seguridad por gloria»): **quitado**, porque estaba duplicado en 2.5 (`fC`, aside de `ch2-bonos`). Se queda allí porque su punto (subirse la dificultad para lucirse) es el margen por encima de +4, que vive en 2.5. Lo de 0.6 («si fallar no aporta nada, no tires») ya lo dice el cuerpo de 0.6. Ojo: hay una tercera versión en `fB_apendices.html` 760 («El principio del 99 %»), que no es mía.
9. **Cap. 0, entrada.** He quitado «Y las reglas trabajan para vosotros: se dejan de lado cuando estorban a lo que la historia pide». Era la tercera vez en media página: ya lo dicen la entrada del capítulo y el recuadro `ch0-norma`.
10. **Intro, «La trampa del tono».** «es **Los** sistemas de comedia negra» → «los» (minúscula, mitad de frase).

### fD_cap3.html (cap. 3)
11. **3.2, lectura narrativa.** «el arquero al que ningún guardia acierta nunca» → «al que los guardias no aciertan» (voz: sin absolutos).
12. **3.4, el rockero.** «Con cuatro —dos peldaños por encima, 4.3— saca a miles de fans» → «Con Llaves que le suben dos peldaños por encima (4.3)». He quitado la cifra. Su Llave es solo para sus fans, y eso huele a Limitada (la mitad). El canon dice que la Tabla 2 «no hace la cuenta del precio (algunas son Limitadas)», y el precio vive en el cap. 5. Ver la pregunta 4.

### fE_cap4.html (cap. 4)
13. **4.5, el daño máximo 2** (un solo sitio). El párrafo «El daño máximo de un arma es 2. Ese es el techo…» estaba casi literal en 6.3 (`fI_cap6_cap8.html` 114), que es la casa de c2. Lo he dejado en una frase con enlace a `ch6-armas`. Además he quitado la palabra «techo», que en este libro es de la Rejilla (3.7). El párrafo del «acontecimiento» se queda: es la Parca, y su casa es 4.5.
14. **4.5, cuántas Llaves cuesta la Parca** (coherencia con el cap. 5). Decía «Cuántas Llaves… una Parca 2 en manos de un nivel 1 le sube un nivel; una Parca 3, dos», y se podía leer «dos Llaves» o «dos niveles». El cap. 5 (`fF` 245) zanja el precio: la Parca sola cubre el daño, no el acierto, así que generalmente va Limitada (Parca 2 → 1 Llave, Parca 3 → 2). Ahora dice «Cuántos niveles…: le sube uno; una Parca 3, dos (4.3). Lo que cuesta eso —la Parca sola cubre el daño, no el acierto— está en 5.6», con enlace a `ch5-armas`.
15. **4.5, barras.** «(ED-11)», que estaba en texto plano, → `<span class="flag ed">ED-11</span>`, para que el montaje lo limpie.

### Sin cambios, comprobado
- **Las epifanías.** Cada capítulo y cada sección grande abre con su idea: cap. 0 (m1), cap. 1 (t1/t2), 1.4, cap. 2 (a1), cap. 3 (r1), 3.5, 3.6, 3.7, 3.8, cap. 4 (l1–l3), 4.5 y 4.7. No he reordenado nada.
- **Las cifras, contra el cap. 5.** 12/14 para todos, el bote (+1 de Rejilla o 5 Llaves), 1·1·1·1·2 recomendado y no máximo, una Llave por sesión y por cabeza, 5·n² / 8·n², n², la Limitada a un nivel que no se separa, mínimo 1, lo de un solo uso gratis, la pistola que paga Llave, los blásters esquivables, la Sincronización como Rejilla (5·n²), el bazuca Limitado al daño, el acordeón (8/22/44). Todo coincide con `fF`.
- **Los nombres.** Los tres techos de 3.7 («nivel máximo inicial / del mundo / de los jugadores») coinciden con las recetas (`fJ2`, «Nivel máximo de los jugadores»). «Rejilla» en todo; «Llave Limitada»; no quedan «la Vela», «Llave ancha» ni «Desenredando». «Malla» solo aparece en «cota de malla» y en el id `ch1-malla` del MAPA.
- **Los porcentajes de 2.5 («Lo que pesa cada bono»)**, recalculados: Primera marcha −2/−1/+1/+2/+4 = 30/40/60/70/90; Angustia −2/−1 = 9/16; Épica +4 = 99; Realista +4 = 85. Correctos.
- **Las referencias cruzadas** «receta 18» (robots gigantes, `fJ2` 181) y «los expedientes» (`exp-vampira-noches`) existen.

## 2. Para el coordinador y para R2 (no son preguntas al autor)

- **«No hay atributos» y Historia/Gaya** ya viven en 2.2. Falta quitarlos de 7.2 (`fG` 20–24) y enlazar.
- **La Parca, duplicada en 6.3.** `fI_cap6_cap8.html` 115 repite casi literal el párrafo del «acontecimiento» de 4.5. Basta una frase y el enlace, que ya lleva («Todo lo demás de la Parca está en 4.5»).
- **El aside del 99 %** sigue también en `fB_apendices.html` 760. Si se quiere un solo sitio, se queda en 2.5.
- **DJ / Director.** fC lo ha normalizado todo a «Director»; fA y fD mezclan «DJ» y «Director» (1.4, 3.5, 3.8). No lo he tocado: es una decisión de todo el libro, y conviene hacerla de una vez en el montaje.

## 3. Preguntas para el autor

1. **Por debajo de −2, «si la hay, con −2».** En 2.5 (`ch2-limites`, «Si el total queda por debajo de −2, el Director decide si hay derecho a tirada; si la hay, con −2») y en 2.6 («Mi ámbito está vacío (−2) y la tarea es difícil (−2)… Si la hay, tiras con −2»). Tu Aclaración dice solo que decide el narrador si hay tirada. El «con −2» viene del texto viejo y cuadra con el rango, pero no lo has dicho tú. ¿Se queda?
2. **Quien está arriba, cuando tú llevas Llave.** En 4.2 (`ch4-arriba`): «Desde ese momento quedáis a la par en lo que cubre la Llave: todo se tira con normalidad —el ataque, la defensa—, y el de arriba ya no acierta sin tirar: tira su ataque». El párrafo siguiente, y la aclaración del zarpazo en 4.9, dicen que para defenderte hace falta otra Llave, de la Disciplina con la que te defiendes. Juntos se leen así: con una Llave de Armas le das al vampiro, pero su zarpazo te sigue entrando sin tirada. ¿Es eso, o con tu Llave el vampiro ya tiene que tirar su ataque contra ti? (Es la duda 2 de D y la 7 de E.)
3. **El golpe de un ser de Rejilla superior.** En 3.1 (`ch3-salto`): «el golpe entra sin tirada, con el daño de su arma», y contra él «no hay tirada que te salve». El «anula lo que dice que anula» del 22 oct se ha aplicado solo a las Llaves y a las armas. ¿El puño del soldado del suero (Físico 2) contra un humano funciona como una Parca 2 (fuera de combate), o entra con su daño normal sin defensa? (Es la duda 1 de D.)
4. **¿La Llave de la estrella del rock es Limitada?** En 3.4 y en la Tabla 2 (N3 Social: «Saca a miles de fans… pero no impresiona a quien no sabe quién es»). Es solo para sus fans. Si es Limitada, a dos niveles cuesta 2 y no 4. He quitado la cifra de 3.4 hasta que lo digas.
5. **La escalera llana (3n−2), regla opcional** (`ch4-llana`, 4.3; y su tabla en el Apéndice, `fB` 800). No contradice n², pero es una segunda tarifa en el capítulo de la Llave. ¿Se queda en 4.3, se va al Baúl (9.1) o se borra?
6. **«Las Llaves que se rellenan cuando la partida ya empezó»** (tu Aclaración sobre el combo barato). fA (0.4) lo ha leído como la Llave en blanco que se escribe justo con lo que resuelve cada problema, y E (4.4) dice, con l7, que la Llave en blanco es legal y que solo la frena la mesa si se abusa. ¿Te referías a eso, o a otra cosa (por ejemplo, recargar Llaves a mitad de partida)?
7. **La tabla de bonos con siete filas** (2.1). El «+3 · El profesional con ayuda» es un nombre nuevo de C. ¿Vale? (Es la duda 1 de C.)
8. **La muerte pactada al revés** (0.7: «una noche de terror en la que los dados sí matan… también es un pacto»). Sale de tu «a menos que se haya pactado». ¿Se queda? (Es la duda 3 de A.)
9. **«Lo que pesa cada bono», Primera marcha +4: «solo fallas con el 1 natural, que es la pifia (90 %)»** (2.5). Es correcto con dado rojo y TN 6. Solo confirmo que quieres los porcentajes en el cuerpo del cap. 2 y no solo en el Apéndice B, porque el MAPA pide «no enturbiar la epifanía con matemáticas». Ya van detrás de la regla, en un h4 propio.

## 4. Informe corto

He revisado los cuatro ficheros contra el canon y el MAPA. No hay contradicciones con el canon. Los arreglos son de sitio único: la fórmula de la tirada, solo en 1.3; «No hay atributos» y Historia/Gaya, en 2.2; el aside del 99 %, solo en 2.5; el daño máximo 2, solo en 6.3. Los demás son de coherencia con el cap. 5 (el precio de la Parca, la cifra del rockero), de voz (dos absolutos, «la Fuerza») y uno de marcado. HTML equilibrado y enlaces completos. Quedan nueve preguntas para el autor, sobre todo la defensa contra quien está arriba (2 y 3) y si la Llave del rockero es Limitada (4).
