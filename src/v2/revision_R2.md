# Revisión R2 · caps. 5–9, FAQ, glosario y apéndices

Ficheros revisados: `fF_cap5.html`, `fI_cap6_cap8.html`, `fG_cap7.html`, `fH_faq_glosario.html`, `fJ1_cap9a.html`, `fJ2_cap9b.html`, `fB_apendices.html` (y sus registros). He leído también `fA`, `fC`, `fD`, `fE`, `fK1` y `fK2` para comprobar la coherencia, sin editarlos.

## 0. Comprobaciones globales

- **HTML**: los siete ficheros quedan equilibrados (comprobado con un parser, 0 errores antes y después).
- **Enlaces**: todos los `href="#…"` de los siete ficheros existen en algún fragmento de `src/v2/`. No hay ids duplicados en todo `v2/`. No quedan ids de la numeración vieja (`ch4-malla`, `ch4-equipo`, `ch1-maquinas`…). Fuera de mis ficheros: **`fA_ideas_intro_0_1.html` enlaza a `#acelerado`, que no existe** (para el coordinador).
- **«Nunca matan»** (`fI`, antes cerca de la línea 86): ya estaba corregido por I («Te dejan fuera de combate; la muerte es otra cosa, y se pacta», con enlace a 0.7). No quedan más «nunca matan» ni «no mata» en mis ficheros.
- **Absolutos**: los «siempre/nunca» que quedan son descriptivos («el saco que siempre está lleno», «Acceso 1 siempre»), citas literales del autor («el ancla está para que nunca lo sea», a2; «siempre narrativo», texto del autor sobre combate) o efectos de ficción («nunca entendió los teléfonos»). No los he tocado.
- **Precio (cap. 5 como casa)**: comprobado que 6.3, 7.2, 9.1 (Transformación), 9.4, la FAQ, el glosario, el Apéndice A y el Bazar dicen lo mismo que 5.4–5.6: el daño no se paga; afectar al nivel siguiente (la Parca) es Llave, Limitada al daño (Parca 2 en un nivel 1 = 1 Llave; Parca 3 = 2); lo de un uso no se paga, lo que no se acaba es permanente, lo que hay que reponer es Limitado; mínimo 1; la pistola paga 1 Llave porque anula la esquiva a nivel 1; los blásters se esquivan por convenio del género; el hombre lobo Limitado, 3; el exoesqueleto 20 / 15.
- **Inés**: 7.2 y su expediente de 9.4 son la misma ficha y las cuentas cuadran (14 = 5 + 4 + 2 + 3 + 0; Firma 4 puntos en su rama; 5 Llaves en Entereza, Potencia, Atletismo, Pelea y Sigilo, completas, de un nivel; Rejilla 1·1·1·1·1; en la corte, Físico 2 y 0 Llaves).
- **Techos**: 7.2, 9.4, la FAQ y el glosario usan los tres nombres de 3.7 (nivel máximo inicial, del mundo, de los jugadores).

## 1. Lo que he cambiado

### `fG_cap7.html` (7.2)
1. **«No hay atributos» y el ejemplo de Historia y Gaya** (recuadro `ch7-atributos` y el párrafo de los cuatro niveles de «zoom»): fuera; viven en 2.2 (R1 ya los ha puesto en `fC`, `ch2-atributos`). En su lugar, una frase: «La ficha no tiene atributos: los campos amplios de la pirámide hacen ese papel, todo va directamente a los bonos, y para brillar hay que especializarse (2.2)», con enlace a `ch2-piramide`. El id `ch7-atributos` desaparece (nadie lo enlazaba). Motivo: MAPA §4, un solo sitio.
2. **[Lento]** (h4 `ch7-aspectos`): la regla («no sirve para tirar iniciativa; o entras con otra guardia, o vas el último») sale de aquí y se queda en 6.1, que es su casa. Aquí queda: se apunta en la ficha, no se compra, y enlace a 6.1.
3. **Paso 4 de «Los seis pasos»**: decía «La Rejilla de salida recomendada es 1 en todo (3.4), salvo que el bote vaya a un ámbito (paso 4)». Dos fallos: se remitía a sí mismo (el bote está en el paso 5) y chocaba con r5 (lo recomendado es 1·1·1·1·2). Ahora: «La Rejilla de salida es 1 en todo, la humana realista (3.4), y el bote puede poner un 2 donde el mundo lo permita: 1·1·1·1·2 es el punto de partida recomendado (5.2; paso 5)».
4. **Paso 1**: «los techos de Rejilla del mundo» → «los techos de Rejilla, el nivel máximo inicial y el de los jugadores (3.7)», para no confundirlo con el «nivel máximo del mundo» de 3.7, que no es el que pone la mesa para la ficha.

### `fI_cap6_cap8.html` (cap. 6)
5. **[Lento] unificado** (6.1, «Habilidades lentas»): decía «un aspecto negativo **comprado** en la ficha: en combate va **siempre** la última o…». Chocaba con 7.2 (los aspectos no se compran, ED-35) y con la decisión del autor (`frag_ch3.html`:109: «no sirve para tirar iniciativa; o entras con otra disposición, o vas el último»). Ahora: la etiqueta [Lento], que no se compra (enlace a 7.2), no sirve para tirar iniciativa, o entras con otra guardia o vas el último; y, de T87, si es tan lenta que no cabe en un conflicto, ni siquiera puede usarse en él. Ver pregunta 2.
6. **«Disposición» → «guardia»** en todo 6.1 (la pregunta del DJ, «El marcador de guardia», «cambiar de guardia», «la habilidad de la guardia elegida»). El canon (c4) dice «guardias», el recuadro ya se titulaba «Las tres guardias» y el glosario dice que «Disposición» era el nombre del borrador. Una idea, un nombre.
7. **La Parca en 6.3**: el párrafo repetía 4.5 (acontecimiento, «funciona como la Rejilla», fuera de combate sin absorción, la esquiva la dice su etiqueta). Queda en una frase y enlace: «Es la Parca, una Llave al daño con su nivel de Rejilla, y vive en 4.5. Aquí solo se ve cómo se escribe en la ficha técnica». «El daño máximo de un arma es 2» (c2) se queda en 6.3, que es su casa según el MAPA (ver nota para el coordinador, §3).

### `fF_cap5.html` (cap. 5)
8. **5.9, «Armas contra los vampiros»**: decía «¿Me vale contra el licántropo? **Sí**… así que es la completa». 4.9 (`fE`) y la FAQ dicen «**No**: es Limitada; por eso a un nivel no se compra así». La pregunta es de qué hace la Llave (casa: cap. 4), así que en 5.9 queda solo el precio, sin contradecir a nadie: «¿Me sale más barata “Armas contra los vampiros”, de un nivel? No. A un nivel, la Limitada cuesta lo mismo que la completa (mínimo 1), así que se compra Armas entera, que vale contra el licántropo y contra todo (4.3). La correa empieza a abaratar a partir del segundo nivel: dos en vez de cuatro». Ver pregunta 1.
9. **5.2, el bote**: «La anchura es barata, pero te la marca el universo con sus techos» → «pero la abre la historia, dentro de los techos de vuestro mundo (3.7)». Es la misma corrección que B hizo en el Apéndice A (r6, r8: la Rejilla la abre la historia; el techo es un límite, no quien la da).
10. **5.5, voz**: «Este es el error que vais a cometer, así que va en negrita» → «Este es el error más fácil de cometer…» (sin condescendencia).

### `fH_faq_glosario.html`
11. **FAQ «¿Qué ficha le hago a cada cosa?»**: «la ficha completa para quien importa» → «para el némesis» (7.3: se recomienda una sola, la del antagonista principal).
12. **Glosario, «Ficha completa»**: decía «para quien importa en la historia: los protagonistas y los PNJ que lo merecen. Es la recomendación del sistema». Ahora dice lo de 7.3: la llevan los protagonistas y, hecha por el Director, el némesis; se recomienda una sola en la mesa.
13. **Glosario, «Ficha rápida»**: «sus pocos números básicos» → «su nivel de Rejilla y un Ámbito entero a +2, y +0 fuera de él» (7.1, 7.4).
14. **Glosario**: el párrafo de entrada pasa a `class="lede"` (la epifanía del apartado: «una idea, un nombre»).

### `fJ2_cap9b.html` (9.4)
15. **ED-16** (aside de decisiones): «coherente con el caso A **del capítulo 3**» → «del caso A de 5.2», con enlace a `ch5-casos`. Numeración vieja.
16. **Receta 12**: «los manuales de la Llamada» → «los manuales de los pulpos antediluvianos» (el arquetipo que usa el resto del libro; «la Llamada» se acercaba demasiado al nombre del juego).
17. **Entrada de las recetas**: «El nivel máximo inicial lo pone la mesa (5.2)» → «El nivel máximo inicial es otro: con qué empieza una ficha nueva, por defecto el 2 del bote donde el universo lo permita (5.2)». Es la definición de 3.7.

### `fB_apendices.html` (Apéndice A, J)
18. **«Las dos escaleras»**: «La alternativa del manual es 3n−2» → «La regla opcional de la escalera llana (4.3) es 3n−2», con enlace a `ch4-llana`. E la conserva en 4.3 como regla opcional; aquí se dice lo mismo y se enlaza (resuelve la duda 1 de B).

### `fJ1_cap9a.html`
- Sin cambios. Revisado contra el canon (Transformación, daño ambiental, mutaciones, Vínculos, detective): coincide con el cap. 5.

## 2. Preguntas para el autor

1. **La Llave Limitada de un nivel, ya escrita.** Tu aclaración del 22 oct: «no tiene sentido separar cuando el precio es el mismo». 4.3 y 4.9 lo leen como «a un nivel no se compra así; si la escribiste “contra los vampiros”, es Limitada y no vale contra el licántropo» (la FAQ igual, y también «“Armas contra zombis”: ¿le doy sin tirar a un zombi de mi nivel? Sí… lo que la limita es lo que dice: solo zombis»). El 5.9 viejo lo leía al revés: «a un nivel no hay Limitada, así que es la completa». He dejado la lectura del cap. 4. ¿Cuál es la tuya?
2. **[Lento] demasiado lento.** En 6.1 he juntado tu decisión («no sirve para tirar iniciativa; o entras con otra guardia, o vas el último») con la frase de T87 «si es demasiado lenta, ni siquiera puede usarse en el tiempo de un conflicto». ¿Se queda la segunda, o basta con la primera?
3. **La Tragedia: ¿para toda la campaña?** 1.4 (`ch1-tragedia`) y el Apéndice B dicen «para toda la campaña y dicho en voz alta». Pero el módulo Destino (Wyrd) de 9.1 («Cuando el Wyrd se cumple, pasa a la receta Tragedia hasta el final de la escena») y la receta 6 la usan por personaje y por escena. ¿Es «para toda la campaña» o «declarada», a secas?
4. **Social 3–4 por fama en mundos humanos.** Receta 4 (samuráis, «una frase bien dicha mueve una provincia», Social 4) y receta 15 (ladrones, «el techo 3 es la ciudad entera a tus pies»). Tu criterio del ciberpunk («no existe el ser que impide tirar a cualquier humano para seducirlo…») y la FAQ («la fama, las deudas o los favores dan Llaves, no Rejilla») dirían Llaves. ¿Se bajan esos techos sociales o se quedan porque el género lo pide? (duda 3 de J2).
5. **La escalera llana 3n−2** (regla opcional en 4.3 y en el Apéndice A). El canon solo da n². ¿Se queda como opcional?
6. **El decorado, ¿«sin ficha»?** c7 dice «Decorado (sin ficha ni tirada)», y así lo dicen el glosario y la FAQ. 7.1 y 7.5 dicen «una línea: su nivel de Rejilla». No es contradicción de reglas (no tira en ningún caso), pero sí de palabras (duda 5 de G).
7. **La Parca, Limitada al daño.** 5.4–5.6 dicen que la Parca sola (hay que acertar) va Limitada: Parca 2 en un nivel 1, 1 Llave; Parca 3, 2. El Bazar (K1, K2) ya cuenta así. El texto viejo decía 4 por la Parca 3. ¿Confirmas la Limitada? (duda 1 de F).
8. **Anular la absorción, Llave.** El canon dice que la pistola paga Llave porque anula la esquiva a nivel 1. 5.6 y 5.9 aplican lo mismo a lo que a tu nivel anula la armadura (Abs: Nula, la katana monofilo), y lo que solo la dificulta va a puntos. ¿Te vale? (duda 2 de F).
9. **«Ignora todo»** (etiqueta [Rejilla] de 6.3, la espada vorpalina: «Corta dioses. Es una Llave de muchos niveles, y se paga como tal»). Con n² no tiene precio fijo. ¿Se queda así, abierta? (duda 3 de H).
10. **«Don» nombra dos cosas**: el aspecto (la gemela de la lacra) y el Dominio de Arcano. Choca con «una idea, un nombre» del glosario. ¿Se renombra uno? (duda 1 de H).
11. **Inés «casi humana» con cinco Llaves completas.** En Entereza, Potencia, Atletismo, Pelea y Sigilo actúa a nivel 2 contra cualquiera; el mortal le planta cara en lo demás. 7.2 y 9.4 lo dicen igual. ¿Vale así, o prefieres menos Llaves físicas? (dudas 1 de G y de J2).
12. **«La Fuerza» y «Soldados de Asalto»** en la receta 7 (nombre del Arcano y de las masillas). Son palabras comunes, pero juntas apuntan a una franquicia. ¿Se quedan?

## 3. Para el coordinador o R1 (fuera de mis ficheros)

- `fE_cap4.html` 4.5 repite entero el párrafo de c2 («El daño máximo de un arma es 2. Ese es el techo, y es a propósito…»), que según el MAPA vive en 6.3 (`ch6-armas`). En 6.3 se queda; en 4.5 bastaría una frase y un enlace a 6.3.
- `fA_ideas_intro_0_1.html`: enlace roto `#acelerado`.
- Las lacras se cuentan en tres sitios: 6.5 (dónde ocurren, la casa), 5.8 (una frase con enlace, que repite la definición) y 7.2 (una frase). Es aceptable; si se quiere apretar, 5.8 puede quedarse solo en «no se compran, ocurren (6.5)».
