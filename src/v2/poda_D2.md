# Poda D2 · `fE_cap4.html` (cap. 4, la Llave)

**Palabras (wc -w):** 5.274 → 4.299 (≈4.280 sin etiquetas). La Tabla 2 (4.8) sigue intacta: ella sola son unas 400. No se ha caído ninguna regla.

## Lo quitado (el caso → dónde se queda)

- **4.9 se queda en 4 aclaraciones (antes, 17).** Fuera las que repetían el cuerpo:
  - «¿La Llave me sube el bono?» → 4.1 («te sube de nivel, no de oficio»).
  - «Llave de Armas: ¿le doy sin tirar a cualquiera de mi nivel?» → 4.1, párrafo «En mesa» (le he pasado el «para eso la pagaste»).
  - «Armas contra los vampiros / licántropo» → 4.3 `ch4-limitada` (su casa). He subido allí el licántropo y «suelen ser prestadas: el agua bendita». «Es un consejo, no una regla» se dice una vez («un consejo de optimización»).
  - «¿Y el zarpazo del vampiro?» → 4.2 `ch4-arriba` (he añadido allí «o una Llave de un momento que te dé la ficción»).
  - «¿Una Llave de nivel superior deja al de abajo sin defensa?» → 4.2.
  - «Mi arma no se esquiva ni se absorbe: ¿una o dos?» → taller del Bazar (`bz-precios`).
  - «Embosco al vampiro antiguo…» → 4.2 («La Llave cubre lo que cubre»).
  - «Veinte mercenarios» y «Mi club de hackers, mi hermana, mi contacto» → metidos en la entrada «Llave de un momento» de 4.4 (de ahí: «son tu excusa y tu capacidad, no botones», el contacto de vacaciones, sin saltarse la progresión, «si mañana sois tres, la Llave no está»).
  - «Guardo una Llave en blanco…» → 0.4 (`ch0-novale`). En 4.4 se queda la regla, el repelente de tiburones y el caso del enemigo de la campaña, con su enlace a 0.4.
  - «Mi mundo no deja tener Mental 2. ¿Y con Llaves?» → 3.7 `ch3-techo-llaves` (allí ya está el laboratorio forense).
  - «Tengo un bazuca…» → **movido** al cuerpo de 4.5 (su casa), con un id nuevo: `ch4-bazuca`.
  - «La granada lleva Parca: ¿cuesta Llaves?» → recuadro de la granada en 4.2, con una línea («la que lanzas y se acaba no se paga», enlace a 5.4). El lanzagranadas de munición infinita se va al Bazar / 5.4 («lo que no se acaba es permanente»).
  - «Presencia Majestuosa: ¿no decía la Rejilla que el de abajo no tira?» → 4.4 `ch4-abiertas` (he añadido «no contradice a la Rejilla»).
- **4.2:** «Una Llave por rasgo» (Parca + Abs: Nula, Esq + Abs Nulas = 2) y «La pistola» se quedan en una frase y el enlace a `bz-precios`. La katana monofilo y las balas perforantes siguen como ejemplos del principio (palabra del autor, 22 oct).
- **4.3:** «La Llave es tan grande como diga la escena» estaba también en 4.4: se queda solo en 4.4 (casa de l5). He juntado en un párrafo el del alcance, el del bote y el de la Rejilla 5·n².
- **4.4:** «La Llave, de principio a fin» pasa de una lista de cinco puntos a un párrafo con lo único: no tiene techo (3.7), renunciar a un salto da Llaves (5.8) y cómo se va (5.7). Fuera los regalos del Director (su casa es 5.7). Fuera «este manual no le tiene miedo al combo barato… lo frena la mesa… sesión 0» (nace en 0.4).
- **4.5:** «Lo que lleva dentro» (Parca + Abs: Nula) se cae: ya lo dicen el recuadro de la Parca («ni absorción que valga») y el Bazar. «Lo de un solo uso no se paga» de aquí → al recuadro de la granada. El enlace del precio de la Parca va ahora a `bz-precios` en vez de a `ch5-armas`.
- **4.6:** fuera el dron (su casa es 5.4); la prueba se queda con «ver mejor es un bono». El párrafo «vago a propósito» queda en una frase con su enlace a 5.4.
- **4.7:** fuera la frase del pergamino de invisibilidad (ya lo dice su casilla en la Tabla 2).
- **4.1:** los tres ejemplos de la ficción, algo más cortos; ninguno se cae.

## Lo movido o lo nuevo

- **El bazuca** se cuenta en 4.5 (`ch4-bazuca`): cubre el daño, no el acierto; el misil teledirigido; la amiga hacker que le corta el guiado.
- **La invisibilidad** pasa a 4.6 (`ch4-invisibilidad`), como ejemplo del permiso y de la segunda prueba: capa, 1; a voluntad, 2; indetectable, Sigilo +2 contra todo, 4 Llaves. Para que 5.5 se quede en una línea y el taller del Bazar enlace aquí.
- **4.9 tiene un caso nuevo:** el hombre lobo, en una línea (la capacidad se paga; la de un momento, no), con enlace a `ch9-transformacion`, tal como dice PODA («como mucho un caso en 4.9»).

## Enlaces

Todos existen en `src/v2/f*.html` (comprobado por script). Ninguno a ids de h4 de cap. 5 que puedan caerse en su poda (`ch5-armas`, `ch5-dura`, `ch5-minimo`): solo los h3 de 5.x y `bz-precios`. HTML equilibrado (comprobado con un parser). No hay ids repetidos.

Ids nuevos que pueden usar los demás: `ch4-bazuca`, `ch4-invisibilidad`.

## Dudas

1. **Los de fuera que enlazan aquí:** la poda de cap. 5, la de 6.3 y la de la FAQ pueden enlazar al bazuca (`ch4-bazuca`), a la invisibilidad (`ch4-invisibilidad`) y a la granada (`ch4-granada`, sin cambios). Mejor apuntar ahí que solo a `ch4-parca` o `ch4-permisos`.
2. **El taller del Bazar** (`bz-fabrica`) todavía cuenta la invisibilidad entera. Se podría quedar en una frase con enlace a `ch4-invisibilidad` (es de K1 / quien pode el Bazar).
3. **El párrafo «Descartado» de 4.5** (T68, «Jerarquía de la inevitabilidad») es historia editorial, no está repetido. Lo he dejado, pero `assemble_v2.py` no borra las banderas: si no se quiere en el manual, se quita.
4. **El capítulo queda unas 300 palabras por encima del objetivo** (unas 3.900 sin la Tabla 2), sobre todo porque el bazuca y la invisibilidad han entrado en el cuerpo. Si hace falta acercarse a 4.000, lo siguiente que recortaría es la tabla «De dónde sale una Llave» (4.4) y la nota del Mundo Animado. Las dos son únicas, así que no las he tocado.
