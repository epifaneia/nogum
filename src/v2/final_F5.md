# Revisión final · F5 (FAQ y glosario, cap. 9, Bazar, apéndices, hoja de referencia)

Ficheros: `fH_faq_glosario.html`, `fJ1_cap9a.html`, `fJ2_cap9b.html`, `fB_apendices.html`, `fL_referencia.html`, `fK1/fK2/fK3_bazar_*.html` (en el Bazar: texto, notas y la coherencia del catálogo con el índice).

Comprobado con script al acabar: HTML equilibrado en cada fichero (el Bazar abre `<section>` en fK1 y la cierra en fK3, como siempre), ningún id repetido, ningún id quitado ni añadido, y ningún enlace roto. El único que no resuelve es `#acelerado`, que está en fA y lo reescribe el montaje.

## Comprobaciones hechas

- **FAQ → destino.** He leído el sitio al que apunta cada una de las 71 preguntas. Seis no se contestaban ahí y las he corregido (abajo). Las demás sí se contestan donde dicen.
- **Glosario ↔ capítulos.** Las 62 entradas comparadas con su capítulo. Cuatro decían algo distinto o se quedaban cortas (abajo). El orden alfabético y los enlaces están bien.
- **Bazar, catálogo ↔ índice.** Lo he cotejado con un script: 372 objetos en el catálogo y 372 filas en el índice. Coinciden el nombre, la ambientación, el «Qué hace» (Daño · Esq) y el precio (Acceso · puntos · Llaves) de todos. También coinciden los totales por categoría (168 · 36 · 19 · 124 · 25), los del resumen por ambientación (30, 30, 29, 30, 28, 30, 30, 30, 30, 30, 16 y 59) y el orden dentro de cada categoría.
- **Precios del Bazar.** He rehecho la cuenta de los 372 con la regla de 5.4–5.6 y el recuadro «De dónde salen los números». No hay ningún error aritmético. Tres precios aplican mal la regla, no la suma: no los he tocado y van en las dudas.
- **Apéndices.** He recalculado por enumeración exacta las siete tablas del Apéndice B y la de la Tragedia: todas cuadran. También cuadran todas las cifras de A.1–A.10 (medias, desviaciones, 3d6, 4dF, 2d6, ventaja en d20, coberturas 30/28 %, 5/8, 4+3+3, acordeón 8/22/44).
- **Ejemplos y fichas.** Las cuentas de Inés en los dos expedientes (14/14 puntos y 5/5 Llaves) cuadran, igual que los niveles máximos de cada receta frente a su texto y las escaleras n², 3n−2, Limitada, 5·n² y 8·n².

## Cambios

### fH_faq_glosario.html
| Sitio | Tipo | Antes → después |
|---|---|---|
| FAQ «Dos bonos de la misma fuente» | enlace que no contesta | 2.6 → **2.5** (`ch2-bonos`: «se acumula lo que se pueda, a criterio de mesa») |
| FAQ «¿Puede una ficha tener un +5?» | enlace | 2.6 → **2.1**, 2.6 (el rango −2…+4 está en 2.1) |
| FAQ «Con +4 en la Épica casi no fallo» | enlace | 2.6 → **2.5** (el «99 % en la Épica» está en `ch2-limites`) |
| FAQ «En ciberpunk, ¿por qué el genio informático no tiene Mental 2?» | enlace | 3.9 → **3.7** (`ch3-techo-llaves`) |
| FAQ «Soy nivel 2 y el enemigo es un humano de nivel 1 con ficha» | enlace incompleto | 3.1 → 3.1, **4.9** (donde está la pregunta literal) |
| FAQ «Este objeto del catálogo da un permiso y no pone Llaves» | enlace que no contesta | 5.9 → **los casos resueltos del Bazar** (`bz-casos`: «es una errata, no una regla») |
| Glosario · Llave | contradice 4.1 | «te deja afectar a **un** nivel de Rejilla por encima» → «te pone **uno o varios** niveles de Rejilla por encima del tuyo» |
| Glosario · Llave prestada | se quedaba corto (4.4: la prestada la da el Director) | «La que da la ficción» → «La que dan la ficción o el Director» |
| Glosario · TN | absoluto sin su excepción | «No se mueve (1.3).» → «… ; la Tragedia es la excepción declarada (1.4).» |
| Glosario · Ventaja | concordancia | «la ficción te **lo** debe» → «te **la** debe» |

### fJ1_cap9a.html (9.1–9.2)
| Sitio | Tipo | Antes → después |
|---|---|---|
| Tabla del baúl, fila «Menú de los 4 costes» | canon (el éxito con coste solo está en dos tarjetas) | «Todas las de éxito parcial» → «Las que juegan en el Pulp desenfrenado o la Comedia negra»; el 6.6 apunta a `ch6-costes` |
| «Menú de los 4 costes» (final de 9.1) | canon + término | «El éxito parcial… las recetas de caos alto lo dan por supuesto» → «El éxito con coste… Solo lo llevan el Pulp desenfrenado y la Comedia negra, y las recetas que juegan en ellas lo dan por supuesto» |
| Flashbacks | concordancia | «contra **el** TN», «por encima **del** TN» → «**la** TN», «**de la** TN»; el menú de la pifia apunta a `ch6-pifia` |
| Pacto del diablo | enlace | el menú de los 4 costes apunta a `ch6-costes` |
| Clones | cita mal copiada | «nadie muere por una mala tirada» → «ningún protagonista muere por una tirada» (0.7, literal) |
| El Director tira en oculto · Heridas graves · Locura · 200 Firmas | coherencia | «sesión cero / sesión zero» → «sesión 0» |
| Tablas de dados | repetición con contradicción | quitada la «tabla de estructura» de fallos de equipo (propuesta sin validar, 1–3/4–6/7–8/9/10). Era una segunda tabla de fallos de equipo, distinta de la de las Tablas de problemas. Su casa es esta última, y el punto de la lista ya enlaza a ella |
| Transformación | frase rota | «tiene **la misma** condición de fin» → «tiene **su** condición de fin» |
| Daño ambiental | precisión de regla (4.5) | «la tercera —seguir ahí te deja fuera de combate…» → «la tercera —a quien esté por debajo de ese nivel lo deja fuera de combate…» |
| Barras propias · Honor | contradice 6.4 (las barras se llenan) | «Llegar a 0 es la deshonra» → «Llenarla del todo es la deshonra» |
| Escalera llana | frase | «subir n niveles con **una Llave** cuesta n²» → «con **Llaves**» |
| Las barras con nombre propio | repetición (la regla y el ejemplo de la Humanidad viven en 6.5) | el recuadro «El nombre lo pone el género…», con su minitabla gótico/cyberpunk y el párrafo «sin Arcano no hay barra Espiritual», queda en un párrafo con enlace a 6.5. Se queda la tabla de nombres por género, que es la que solo está aquí |
| Mutaciones (tabla y nota) | contradice 4.6 (trepar y nadar son Atletismo, un bono) | «Un permiso nuevo (agarrar, trepar, nadar)» → «(trepar por una pared lisa, respirar bajo el agua)», y lo mismo en la nota |
| Las 40 Disciplinas | errata | «Juego de **M**anos» → «Juego de **m**anos» |
| Las 40 Disciplinas | repetición y fila de más | quitada la fila «Ritual · Según campaña…» (sobraba: la tabla tenía 41 filas y lo mismo lo dice el párrafo de debajo); quitados los espacios al final de las celdas de Ritual |
| Red de seguridad en cascada | repetición **y contradicción** con 2.2 | la cascada contada entera otra vez (bomba nuclear con Mecánica/Artificio, cuando 2.2 la hace con Seguridad/Operaciones), más un meta que lo admitía, se queda en un párrafo con la regla y enlace a 2.2 |
| Principios del catálogo | término inexistente | «Experto o Gran Maestro» → «Gran Maestro» |
| Firmas de ejemplo · Entereza | enlace roto en el sentido y nombre | «Aguantar dolor · Caso A de 5.2» → «Aguantar el dolor · Caso A de **7.2**» (`ch7-casos`) |
| Firmas de ejemplo · Mecánica/Explosivos nucleares | contradice 2.2 | fila quitada; «Explosivos» va en la fila de Seguridad, con la nota «es la del ejemplo de la cascada (2.2)» |
| «El catálogo está ordenado por Disciplina…» | repetición (lo dice «Las 200 Firmas» justo debajo) | párrafo fundido en el de «Las 200 Firmas» |
| 200 Firmas | palabras que no existen o calcos | Ganzuado → Ganzúa; Calmado de Ánimos → Calmar los Ánimos; «Bypassear paneles» → «Saltarse paneles»; Cómputo Análogo → Cómputo Analógico; «Bucleado de vídeo» → «Vídeo en bucle»; Rastreación → Rastreo; «o zafado de ataduras» → «, o zafarse de ataduras» |

### fJ2_cap9b.html (9.4)
| Sitio | Tipo | Antes → después |
|---|---|---|
| Las 19 recetas con «El fix:» | coherencia con su propia introducción («el lore y el arreglo») | «El fix:» → «El arreglo:» |
| Intro de los niveles máximos | repetición de 3.7 | sale la definición del nivel máximo inicial (es de 3.7 y aquí no se usa) y la frase de las Llaves queda en media línea |
| Receta 1 | término | «la **receta** de referencia del capítulo 1» → «la **tarjeta** del 1.4» |
| Receta 2 | contradice 6.4 y 0.7 | «Si la Corrupción se vacía, el personaje pasa a PNJ» → «Si la barra de Corrupción se llena del todo, el personaje pasa a manos del Director, si la mesa lo ha pactado (0.7)» |
| Receta 4 | igual + «sesión cero» | «el Honor a 0 retira la ficha» → «llenar la barra de Honor retira la ficha» |
| Receta 5 | repetición dentro de la frase | «Por el salto de nivel (3.1) y el Estilo (3.5), … la Regla del Estilo: … y el Estilo decide cómo» → «Por el salto de nivel (3.1), … la Regla del Estilo (3.5): …, y el Estilo decide cómo» |
| Receta 8 | repetición (el rockero vive en 3.4) | el caso entero (cuatro Llaves, completa, mundo conectado, sujeto a la mesa) → «el rockero que llena estadios lo hace con Llaves (3.4)» |
| Receta 11 | repetición dentro de la receta | «Los dragones corporativos son de nivel 4–5 en Social, pero son PNJ…» (ya dicho una línea antes) → «Los dragones son PNJ: su 4–5 es el nivel máximo del mundo…» |
| Receta 13 | frase que no se entendía | «Son dos barras distintas» (tras hablar de Llaves) → «La Sed y la Humanidad son dos barras distintas» |
| Receta 13, nivel máximo | repetición (tercera vez que dice que lo que separa al vampiro es tener Arcano) | quitada la frase repetida |
| Recetas 16 y 17 | «sesión cero» y «para súper ya consagrados» | «sesión 0»; «para empezar con héroes ya consagrados» |
| Receta 20 | fantasma de corrección («la suma es la herramienta del orden», sin contexto) | «Comedia negra (1.4): el dado rojo, y no la suma de los dos, que es la herramienta del orden y la que mataba el chiste» |
| Receta de crítica | enlace | el menú de los cuatro costes apunta a `ch6-costes` |
| Títulos paródicos | puntuación y concordancia con la receta 1 | «Clases, razas, y combos» → «Clases, razas y combos» |
| Piedra Rosetta · simuladores narrativos | cifra contraria al cuadrante | «Épica (…, Caos **Medio**)» → «Caos **Bajo**» |
| Piedra Rosetta · fila 2 | frase rota (el ejemplo real de REVISION-FINAL) y término | «Los sistemas de comedia negra · El «sí, pero…» y la comedia negra de problemas · 1d10 con éxito parcial» → «Los sistemas de movimientos (el nombre que usa A.3.2) · El «sí, pero…» y los problemas que trae cada éxito · dado rojo, con éxito con coste en 6–7» |
| Piedra Rosetta · pulp | término | «con éxito parcial» → «con éxito con coste» |
| Expediente de las primeras noches | frase que se muerde la cola | «lo que la sujeta no la sujeta» → «no la retiene» (como en 7.2) |

### fB_apendices.html
| Sitio | Tipo | Antes → después |
|---|---|---|
| A.5 | contradice 1.3 («cuatro lecturas») | «Hay seis lecturas:» → «Hay cuatro lecturas, y dos herramientas que se les ponen encima:» |
| A.6 | frase que se quedó vieja («Aquí se muestran cuatro perfiles», y no se muestra ninguno) | → «… siete filas por tarjeta, de la Nulidad (−2) al Gran Maestro (+4), con la moneda al aire (+0) en medio… Las gráficas de A.8 las dibujan, y el Apéndice B las escribe» |
| A.8 · Comedia negra | cifra mal dicha (a bono 0, el coste es el 40 % de lo que sale adelante) | «un quinto de lo que consigues viene con factura» → «una de cada cinco tiradas viene con factura» |
| A.10 · La escalera de las Llaves | **a la tabla le faltaba la fila +3** | añadida: +3 · 9 · ×10⁶ |
| Apéndice B · entrada | puntuación | «(A.8), dibujan» → «(A.8) dibujan» |

### fL_referencia.html (no se reestructura y sigue cabiendo en una cara: dos palabras de más)
| Sitio | Tipo | Antes → después |
|---|---|---|
| La Rejilla, segundo punto | pronombre ambiguo (tras «Lo cósmico», «La abre» parecía referirse a lo cósmico) | «La abre la historia» → «La Rejilla la abre la historia» |
| La cuenta | término (el Acceso es lo que pide el objeto, no tu nivel) | «Acceso: tu nivel en Recursos (0 cotidiano…)» → «Acceso: lo que tus Recursos te dejan tener (0 cotidiano…)» |

### Bazar (fK1, fK2, fK3): solo texto y notas, ningún precio tocado
| Sitio | Tipo | Antes → después |
|---|---|---|
| 13 notas con «Esq y Abs sin indicar» (Daga Ritual, Palanca, Carga Psiónica, Báculo Sagrado, Abanico, Trampa para Osos, Amuleto Solar, Martillo Digno, Gema Primordial, Brazo Mecánico, Baraja Maldita, Reloj Hipnótico, Bomba Redonda) | fantasma de la fuente que contradecía la fila (las columnas sí traen Esq y Abs) | frase quitada |
| Rifle de Plasma, Cañón de Iones, «Gordo», Superfuerza | notas de historia en el texto («T110 lo repite igual», «omite Esq y Abs», «omitía…») | quitadas; la marca `src` se queda |
| Granada Térmica | fantasma de corrección | quitado «El texto añade «Daño Masivo»; manda la ficha: es la Parca» |
| Escudo Deflector, Carne de Perro, Visión Láser | notas de historia | «T107 y T110 lo repiten y añaden que un cuchillo lento lo atraviesa» → «Un cuchillo lento lo atraviesa»; «T107 añade: «Sabe a rayos»» → «Sabe a rayos»; «T107: «Miras y explota»» → «Alcance visual: miras y explota» |
| Armadura de Soldado de Asalto | errata (en todo el libro es «blásters») | «blásteres» → «blásters» |
| Regeneración de Escena | enlace (la barra vuelve en 6.4) | (6.5) → (6.4) |
| Elixir de Vitae | enlace (lo de una escena no se paga: 5.4) | (4.8) → (5.4) |
| Marcas de las cabeceras del Mundo Animado y del Duelo Social (×3) | tilde | «peticion» → «petición» |
| Índice, entrada | regla de orden incompleta | añadido «lo que no lleva Acceso, los poderes, va al final» (es lo que hace la tabla) |

## Dudas para el autor

1. **Transformación (Super)**, Bazar 6: «temporal, Limitado: 3 Llaves». Según tu respuesta 7 y 5.9, acabar con la escena no la abarata si es a voluntad. Saldría completa, a 5 Llaves, salvo que tenga correas (desgaste, condiciones). No he tocado el precio.
2. **Escudo** (piezas sueltas · Defensas): «una vez por escena, puedes reaccionar contra un arma de Abs: Nula» cuesta 1 punto. Defenderte de lo que a tu nivel no se para es Llave, como el Escudo de Energía (Bazar 6) y la tabla de cajones. Saldría a 1 punto y 1 Llave (Limitada, mínimo 1).
3. **Medio segundo** (piezas sueltas): «+2 a iniciativa y a esquivar» son dos bonos de +2, así que por la cuenta saldrían 4 puntos, y el catálogo pone 2. O el texto dice +1 y +1, o el precio es 4 (en el catálogo y en el índice).
4. **Social 3–4 en los niveles máximos de las recetas** 1, 2, 3, 5, 7, 9, 11, 16 y 20. Solo se bajaron las de fama (4 y 15). ¿Alguno de esos también es fama? La receta 2 dice «Nadie es grande aquí. La magia es lo único que rompe el techo», y tiene Social 3 (más que nada salvo el Arcano 3).
5. **«Abs: Voluntad» / «Abs: Reputación»** (recetas 3 y 4, y el Bazar) solo se definen en la leyenda del Bazar («Especiales»), no en 6.3. Vale si es a propósito.
6. **Las 200 Firmas** (y muchos nombres del Bazar) van en mayúscula en cada palabra («Salto Imposible», «Daga de Ladrón»), a la inglesa. Las Firmas del capítulo 2 y de 7.2 van en minúscula («Esgrima antigua», «Aguantar el dolor»), y el Bazar mezcla las dos. Es un cambio de script si lo quieres. Además, varias Firmas cuelgan de una Disciplina que no es la suya según la lista cerrada:
   - Esquiva Refleja va en Atletismo, y la esquiva es Acrobacia.
   - Ganzúa / Cerrajería va en Juego de manos, y la cerrajería física es Mecánica.
   - Primeros Auxilios de Campo va en Supervivencia, y es Biotecnia.
   - Interrogatorio Técnico va en Investigación, e interrogar es Intimidación.
   - Lectura Corporal (las mentiras) va en Alerta, y es Empatía según 5.4.
   - Duplicación / Ilusión va en Proyección, y las ilusiones son Alteración.
7. **Títulos burdos**: «Hevochos con implantes. Y las reglas». ¿Errata o chiste que no pillo?
8. **A.3.2**: «En la mazmorra y la estepa el equivalente clásico es el crítico con 20 natural» no casa con el éxito parcial del que habla el párrafo. ¿Se quita, o va en A.3.1?
9. **Acordeón (A.10)**: la fila de la Disciplina plegada pone «—» en precio por casilla, y el texto dice «el precio por casilla no baja: 4, 4,4, 4,4». Con 8 puntos por una casilla el dibujo es otro. No lo he tocado.
10. **Expedientes de Inés**: sus «porqué» repiten casi literal 7.2 («Físico 2 no dice que sea más fuerte…», el cazador, el Príncipe). Los he dejado porque el expediente es una hoja suelta que se imprime aparte. Si prefieres, se quedan en una línea con enlace.
11. **Quitado de 9.1**: con la tabla de fallos de equipo repetida se ha ido su fila «Se daña: la próxima vez que falle, se rompe», que no está en la tabla buena. Si te gusta, cabe en esa tabla.
12. **«Llenar» o «vaciar» la barra**: el libro usa las dos (6.4 «al llenar el tercer bloque», 6.5 «al vaciarla», 4.5 «no vacía la barra»). Solo he cambiado donde ponía «a 0» (Honor, Corrupción), que choca con 6.4. ¿Se unifica?
13. **Escalera llana**: en tu última respuesta escribiste «n*3». He dejado 3n−2 (1, 4, 7, 10, 13), que es la tabla aprobada y la que crece más rápido sin encarecer el primer peldaño.

## Para el coordinador (fuera de mis ficheros)

- **fA, tarjeta del Pulp (1.4)**: «Con un personaje flojo, un tercio de lo que consigue viene con factura». A −2 son 32 de 51 (63 %). Lo correcto es «un tercio de las tiradas». En A.8 se dice bien.
- **fI, 6.6 · menú de los costes**: «(1.3: Pulp desenfrenado, Comedia negra y cualquier receta de caos alto)». Según el canon, solo esas dos tarjetas.
- **fC, 2.2**: «Solo se puede ser Maestro o Gran Maestro en cosas muy específicas». «Maestro» no es ningún escalón. Además, la Biotecnia de 2.3 aún lleva «cocina», que 9.2 quitó (ED-16).
- **fE 4.9, fF 5.9 y 9.1** cuentan los tres el hombre lobo. Su casa es 9.1.
- **Montaje**: hay marcas `src` con texto editorial que el lector verá como insignia: «Aprobado por el autor», «Borrador», «Decisión del autor», «Escrito a petición del autor (T124)». `limpia_editorial` solo quita los `flag`. Si no deben verse, hay que quitarlas en el montaje.
