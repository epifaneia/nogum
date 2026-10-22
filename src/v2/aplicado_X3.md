# Aplicado X3 · Decisiones del 22 oct en cap. 9, Bazar y apéndices

Ficheros tocados: `fJ1_cap9a.html`, `fJ2_cap9b.html`, `fB_apendices.html`, `fK1_bazar_a.html`, `fK2_bazar_b.html`, `fK3_bazar_c.html`.
Comprobado por script: todos los `href="#…"` de estos seis ficheros apuntan a ids que existen en `src/v2/f*.html`; sin ids duplicados; etiquetas equilibradas (la `<section id="apx-bazar">` se abre en K1 y se cierra en K3, como antes).

## 4 · Combinaciones (Bazar)

- **Revisión de todas las filas con Parca** (K1 y K2, 40 filas con la etiqueta `La Parca`): ya seguían la regla. Ninguna cobraba la Llave extra por Abs: Nula, y todas las que no se esquivan pagan +1. Las he recalculado una a una (Parca N para un portador de nivel 1: N2 1, N3 2, N4 5, N5 8, N6 13; +1 si Esq: Nula; Esq Difícil 2, Parcial 1 y Abs Máx 1 en puntos) y cuadran todas.
- **Filas cuyo precio cambia** (son Llaves de nivel Limitadas al daño, o sea una Parca con otro nombre, y cobraban aparte la Abs: Nula):
  - **Superfuerza (Golpe)** (K2, 8. Capas y mallas): 6 → **5 Llaves**. Nota «La cuenta» reescrita: la Abs: Nula va dentro, como en la Parca.
  - **Martillo Digno** (K2, 8. Capas y mallas): 6 → **5 Llaves**. Igual.
  - Las dos están en el índice (`fK3`) con 5 Llaves. Su orden no cambia: siguen detrás de las de 6 y delante de las de 3.
- **Recuadro `bz-precios`** (K1):
  - «Lo que anula»: añadido «Una Llave por rasgo» y «En un arma sin Parca» delante de «las dos a la vez… 2».
  - «La Parca y la Rejilla»: «Su Abs: Nula va dentro» se amplía con la razón del autor (el daño masivo destroza también el escudo y no se cobra dos veces el mismo concepto). Añadido que vale igual para una Llave de nivel Limitada al daño (la Superfuerza, el Martillo Digno), y que no esquivarse es otro rasgo y paga +1.
- **Índice**: comparado fila a fila con K1+K2 por script. Hay 372 filas en los dos lados, todas encontradas, con el mismo precio. La única diferencia es de formato: el Libro Maldito pone «1 Llave por hechizo» en el índice y «1 por hechizo» en la columna Llaves del catálogo. No es un precio distinto.

## 5 · «A un nivel no se separa» como consejo (de paso, en el Bazar)

- En K1 (`bz-precios` y las notas del Lanzagranadas y del Puño de los Cien Puños), «a un nivel no se separa» pasa a «a un nivel cuesta lo mismo que la completa». Es la razón del coste, no una prohibición.
- En la Transformación (9.1), «ahí no merece la pena separarlas» pasa a «ahí, como consejo, no merece la pena separarlas».

## 6 · La escalera llana, al Baúl

- **9.1 (fJ1)**: módulo nuevo `<h4 id="ch9-llana">La escalera llana</h4>`, puesto antes de «Menú de los 4 costes».
  - Recuadro «Regla opcional · Crecer a plazos». Abre con las palabras del autor («Crecimiento más rápido, Rejillas menos inaccesibles») y sigue con el texto del recuadro `ch4-llana` de 4.3 (3n−2: 1, 4, 7, 10, 13).
  - Debajo, la tabla cuadrada / llana / alcance, traída del Apéndice A, y el párrafo «la divinidad se conquista en campaña / se compra a plazos», con enlace a `maq-economia` (A.10).
  - Fila nueva en la tabla del Baúl: «Escalera llana (3n−2) · Ninguna · Regla opcional del autor».
- **Apéndice A (fB)**: «Las dos escaleras» pasa a «La escalera de las Llaves».
  - La tabla se queda solo con n² y el alcance.
  - Sale la frase «Coinciden en 1 y en 4…». Entra una frase con enlace: «hay una regla opcional, la escalera llana (3n−2), y vive en el Baúl de reglas (9.1)» → `#ch9-llana`.
  - El enlace roto a `#ch4-llana` desaparece.
- **No aplicado / duda**: «Rejillas menos inaccesibles» sugiere que la escalera llana también vale para comprar Rejilla (5·n²). No he escrito cómo (sería inventar). Que lo diga el autor.

## 7 · Transformación (9.1)

- Añadido: «Es Limitada o no según sus condiciones» y «Que acabe con la escena no la abarata: si te transformas a voluntad y siempre que quieres, es la completa, y la condición de fin no vale como truco para pagar menos».
- Ya decía que se paga la capacidad y no la transformación de un momento que presta la trama.
- El h4 lleva ahora `id="ch9-transformacion"`. La receta 17 (fJ2) enlaza ahí.

## 8 · «Ignora todo» / Corta-Dioses (K1)

- Nota «La cuenta» del filo imposible: «cualquier nivel» es el techo de vuestro universo, el ser más poderoso del mundo, se pueda jugar o no (enlace a 3.7). Con techo 6, 13 Llaves; con techos más bajos, 1, 2, 5, 8.
- Añadido que el precio depende de contra quién se pueda usar: contra cualquiera, el de la tabla; contra unos pocos, lo dice el Ajuste (5.5). No pongo cifra para ese caso.
- En la leyenda, «Cualquier nivel: hasta el techo de vuestro universo».
- Precio sin cambios (Acceso 3 · 13 Llaves).

## 9 · El rockero (de paso, receta 8, fJ2)

- Añadida la cifra: cuatro Llaves, dos niveles por encima y completa, porque en un mundo conectado sus fans están en todas partes, «aunque eso queda sujeto a la mesa».

## 12 · Por debajo de −2 (de paso, Apéndice A, A.6)

- «quien narra decide si hay derecho a tirada» pasa a «el Director decide si hay tirada y, si la hay, se tira con −2».

## 13 · Tragedia: consejo, no regla

- **Wyrd (9.1)**: el h4 lleva `id="ch9-wyrd"`, y «receta Tragedia» enlaza a `ch1-tragedia` (1.4). Frase nueva: la Tragedia llega aquí en la dosis que recomendamos para los tonos más oscuros, poco tiempo, una escena; es un consejo, la mesa es adulta y decide.
- **Receta 6 (fJ2)**: «Tragedia cuando llega, hasta el final de esa escena» y la misma recomendación, con enlace a 1.4. Enlace al módulo (`#ch9-wyrd`).
- **Apéndice B (`apxd-recetas`)**:
  - «dicha en voz alta y para toda la campaña» pasa a «dicha en voz alta». Detrás va el consejo: se recomienda encarecidamente no quedarse mucho tiempo en los tonos más oscuros; una escena o un final, como en el Destino del Baúl (`#ch9-wyrd`), mejor que una campaña entera; la mesa es adulta y decide.
  - En la tarjeta de la Tragedia, «se dice para toda la campaña: moverla a mitad de partida…» pasa a «se dice en voz alta: moverla sin avisar…».
- **Fuera de mi lote**: 1.4 (`fA`, `ch1-tragedia`) todavía dice «para toda la campaña y dicho en voz alta». Lo tiene que igualar quien lleve fA.

## 14 · Social por fama → Llaves (recetas 4 y 15, fJ2)

- **Receta 4** (samuráis): techos 2·2·4·2·3 → **2·2·1·2·3**. Texto nuevo: la frase que mueve una provincia es fama, y la fama va con Llaves (Persuasión, Liderazgo, Intimidación), no con Rejilla, con el mismo criterio que el ciberpunk (enlace a `ch9-critica`), porque cualquier humano tiene derecho a tirar para resistirse (4.8).
- **Receta 15** (ladrones): techos 2·1·3·2·2 → **2·1·1·2·2**. La ciudad a tus pies es fama, y crece con Llaves (Contactos, Intimidación, Engaño).
- **Elección mía**: he bajado el Social a 1, como en la receta 8 y en la de crítica, porque la prueba del autor («no existe el ser que impide tirar a cualquier humano») deja en 1 el Social de un humano. Si el autor quiere 2 en la corte samurái, se cambia un número.
- **Duda, fuera del encargo**: otras recetas tienen techos sociales por encima de 1 que podrían caer en la misma prueba. Son la 5 (Soc 3), la 6 (Soc 2), la 12 (Soc 3) y la 13 (Soc 4, «el del príncipe»). No las he tocado.

## 21 · «Don» → «ventaja»

- No hay ningún «don» aspecto en mi lote. Todos los «Don» de 9.2, de las recetas y de los expedientes son el Dominio de Arcano y se quedan.
- «Anomalías y dones» (una de las opciones de categorías de Firmas, en 9.2) es el sentido genérico de la palabra, no el aspecto. Se queda.

## 25 · Apéndice A: A–J → A.1–A.10

- Los h3 `maq-equilibrio` … `maq-economia` se titulan ahora A.1 … A.10.
- Las herramientas C.1 y C.2 de «Sucumbiendo al caos» pasan a A.3.1 y A.3.2, en el `<dl>` y en la lista de A.5.
- Referencias corregidas:
  - Apéndice B: «apartado H» pasa a «Apéndice A (A.8)».
  - Fallos de equipo (9.1, fJ1): «herramienta C.1» pasa a «herramienta A.3.1».
  - Receta 10 (fJ2): «la herramienta C.1» pasa a «la herramienta A.3.1».
- En otros lotes, fA y fC ya usaban A.9 y A.6.

## Sin cambios

- 1, 2, 3, 10, 11, 15–20, 22–24: nada que tocar en mi lote. No queda ningún «DJ». No hay fila +3 con nombre. El decorado del Bazar es el objeto que regala la ficción, no la ficha de decorado.
