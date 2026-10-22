# Revisión final · F2 (cap. 2 `fC_cap2.html` y cap. 3 `fD_cap3.html`)

## Comprobaciones de cifras

- **Porcentajes por bono contra el Apéndice B**: todos cuadran. Primera marcha: −2 30 %, −1 40 %, +1 60 %, +2 70 %, +4 90 % (fallo solo con la pifia del 1). Angustia: −2 9 %, −1 16 %. Épica +4: 99 % (1 % de pifia). Realista +4: 85 %, y el 15 % que falta sale de 12 de fallo más 3 de pifia.
- **Pirámide**: Dominio 1 / Disciplina 1 / Firma 2, acumulado 1-2-4, y un punto por cada +1. Ejemplos: 4, 6 y 8 puntos, bien. Recuentos: 10 Dominios, 40 Disciplinas y 200 Firmas (5 × 40), bien.
- **Acordeón**: 8 / 22 / 44, igual que A.10 (8 + 7 + 7 = 22; 2 × 22 = 44). «Más de media ficha» (8 de 12) y «una Disciplina plegada y poco más» con 12 puntos, bien.
- **Tabla 1 contra CANON.md**: comparada casilla a casilla con un script: idéntica (5 filas × 5 columnas).
- **Cap. 3**: la tabla de dos ceros (×1 … ×10¹⁰), el rockero (4 Llaves = 2², nivel 3) y el hacker (Llave de nivel 3) cuadran. La receta 18 sí es la de los robots gigantes.
- **Enlaces**: todos los `href="#…"` llevan a ids que existen. HTML equilibrado (comprobado con un parser) y comillas «» emparejadas.

## Cambios

### fC_cap2.html
| Sitio | Tipo | Antes → Después |
|---|---|---|
| Lede | Repetición («todas las fichas» dos veces en el mismo párrafo) | «Ese rango, el mismo para todas las fichas, es el Ancla.» → «Ese rango es el Ancla.» |
| 2.2, tabla de la pirámide, fila Ámbitos | Concordancia | «−2 si está vacía» → «−2 si está vacío» |
| 2.2, tabla, fila Firma | Absoluto falso (también hay ventajas, equipo…) | «la única compra de dos puntos del sistema» → «… de la pirámide» |
| 2.2, tras la tabla | Término sin presentar («Maestro» no es ningún perfil; el +2 es el Profesional) | «Solo se puede ser Maestro o Gran Maestro en cosas muy específicas» → «Solo se llega a Gran Maestro en cosas muy específicas» |
| 2.3, aside | Frase rota (el «que significa» no tenía a qué referirse) | «a los narrativos de aspectos (que significa «destino» en inglés)» → «a cierto juego narrativo de aspectos, cuyo nombre significa «destino» en inglés» |
| 2.3, tabla de la lista, casilla de Vínculos | Estética (dentro de la casilla de una Disciplina había una nota sobre toda la tabla) | «(9.2). Es la lista que usa la app.» y sus marcas `src` salen de la casilla y pasan a un `p.small` bajo la tabla: «Es la lista que usa la app; con las Firmas de cada Disciplina, en 9.2.» |
| 2.4, tabla del acordeón | Cifra (44 puntos a punto por sesión) | «Cuarenta sesiones» → «Cuarenta y cuatro sesiones» |
| 2.5, Lo que pesa cada bono (+2) | Concordancia (la TN es femenina en todo el libro) | «un TN 6 en un TN 4 virtual» → «una TN 6 en una TN 4 virtual» |
| 2.5, aside y Lo que pesa cada bono | Marcado (10 porcentajes con espacio normal; el resto del libro usa `&nbsp;`) | «99 %» → «99&nbsp;%», etc. |
| 2.5, Modificadores temporales | Absoluto en texto de reglas | «Define siempre la condición» → «Define la condición» |
| 2.6, el rifle (+1) | Cuenta errónea: la dificultad va de dos en dos, así que el punto que sobra no paga una tarea difícil | «Tiras con +4, así que gasta el punto que sobra en ponerte la tarea más difícil: el disparo a la mano…» → «En una tarea normal tiras con +4 igual; pero si te pones una difícil (−2) —el disparo a la mano en vez de al cuerpo, o desde más lejos—, el rifle te deja en +3 en vez de +2» |
| 2.6, la ficha rápida | Enlace repetido (7.4 dos veces en el mismo párrafo) | Se quita el segundo |

### fD_cap3.html
| Sitio | Tipo | Antes → Después |
|---|---|---|
| 3.1, ¿Rejilla o Llave? | Ambigüedad («cambiar de Rejilla» se lee como cambiar de sistema) | «es hora de cambiar de Rejilla» → «es hora de subirle un nivel de Rejilla» |
| 3.2 | Repetición (decide / se decide) | «El tono decide cuál se lee, y se decide en la sesión 0» → «… y se pacta en la sesión 0» |
| 3.2, tabla de escenarios, nivel 5 | Escala (lo «global» es un planeta, nivel 6) y absoluto | «el control mental global» → «el control mental de todo un país»; «Solo para finales de campaña» → «Casi siempre, para finales de campaña» |
| 3.2, recuadro Un nivel son dos ceros | Repetición: el «No recomendamos» del ×10 ya está dicho, con el ejemplo del boxeador, dos párrafos más arriba | «No recomendamos una versión en ×10. … la respuesta no es encoger la escala: es dejar…» → «Encoger la escala no arregla nada. … la respuesta es dejar…» (el argumento de la pirámide se queda) |
| 3.4, Ser no es saber | Contradicción con «ser no es saber» y con 3.9 (tener un 2 sin un punto): «competente» habla de habilidad; además, todo el mundo «tiene un nivel» | «Para tener un nivel en un ámbito hay que ser competente en todo el ámbito» → «Para pasar del 1 en un ámbito hay que ser grande en todo el ámbito» |
| 3.5, regla del Estilo, paso 3 | Término mal usado: el éxito con coste no es una banda (las bandas son pifia y crítico) | «esa banda se lee aquí como éxito a secas» → «ese resultado se lee aquí como éxito a secas» |
| 3.5, Advertencia de tono | Contradicción con el canon (las masillas son decorado, sin tirada) y concordancia («el último masilla») | «y hasta el último masilla tira dados» → «y hasta el último soldado enemigo tira dados: ahí no hay decorado» |
| 3.7 | Absoluto falso (los techos se ordenan entre sí) | «No tienen nada que ver entre sí.» → «No tienen por qué coincidir.» |
| 3.7, h4 `ch3-techo-llaves` | Absoluto en el título; el cuerpo dice «mejor no» | «Las Llaves no tienen techo» → «A las Llaves, mejor sin techo» (el id no cambia) |
| 3.7, cuerpo del h4 | Repetición literal del lede del 3.7 | «Los techos hablan de ámbitos enteros. A las Llaves es mejor no ponerles techo: siempre pueden…» → «Los techos hablan de ámbitos enteros; las Llaves, no. Siempre pueden…» |

## Dudas para el autor

1. **Sincronización (3.8)**: el lede dice, como el canon (r9), que se «hereda su ficha y su nivel», pero el párrafo siguiente dice «en otros juegos, un mecha tiene otra ficha; aquí basta con mover tu posición en la Rejilla… con la misma ficha» (y la receta 18 dice lo mismo). ¿Se hereda la ficha del mecha o se conserva la propia y solo cambian el nivel y el zoom de la vida? No lo he tocado.
2. **«Ámbito» o «ámbito»**: en el cap. 2 alterna la mayúscula («los cinco Ámbitos», «un Ámbito plegado») y la minúscula («el ámbito Técnico»); el cap. 3 va casi siempre en minúscula. Pasa en todo el libro (también en los apéndices y en el glosario), así que hay que decidirlo de una vez para todos.
3. **2.4, Parkour**: «Acrobacia → Parkour (que solo vale para moverse por la ciudad, no para nadar)». Nadar es de Atletismo, no de Acrobacia, así que el contraste no ilustra lo que se pierde al especializarse. ¿Otro ejemplo (por ejemplo, «no para caer de un caballo»)?
4. **2.2, Torpe**: «Eres pura Erudición… y te toca leer una calle». La Erudición tiene Actualidad («saber de la calle»), así que puede leerse como de la misma columna. Si se quiere decir Alerta o Investigación (Ingenio), quizá «leer una escena» o «ver la emboscada» sea más claro.
5. **2.5, el +4 en la Realista**: «la campana concentra los resultados en el centro, el +4 pesa casi lo mismo». ¿Casi lo mismo que en la Primera marcha? Los números no lo dicen así (+40 puntos allí, +30 aquí). Lo he dejado.
6. **2.5**: el «se acumula lo que se pueda… lo que pase de +4 se tira con +4» aparece en la apertura y otra vez en el recuadro de límites. Lo he dejado como idea y luego regla; si sobra, se puede recortar la apertura.
