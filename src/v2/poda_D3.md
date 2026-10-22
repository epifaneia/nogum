# Poda · D3 (cap. 5, cap. 7, Bazar: lectura, precios y taller)

Copias de antes, por si hay que comparar: `scratchpad/fF_cap5.orig.html`, `fG_cap7.orig.html`, `fK1.orig.html`.

## Palabras (texto sin etiquetas)

| Fichero | Antes | Después |
|---|---|---|
| `fF_cap5.html` (cap. 5) | 11.036 | 4.479 |
| `fG_cap7.html` (cap. 7) | 3.201 | 3.063 (con los casos A y B ya dentro) |
| `fK1_bazar_a.html` (solo `bz-lectura`, `bz-precios`, `bz-fabrica`) | 10.776 el fichero | 11.199 el fichero (el taller recibe los casos de armas y las categorías). El catálogo (`bz-fantasia` en adelante) no se ha tocado: diff vacío |

## Cap. 5: qué se ha quitado y dónde se queda

- **5.1**: el recuadro de los tres pagos (`ch5-monedas`) se queda en una frase. Su tabla era la misma lista que los tres cerrojos de 5.6. El id `ch5-monedas` se conserva en esa frase.
- **5.2**:
  - Los casos A y B pasan a **7.2** (`ch7-casos`).
  - Fuera de 5.2: la justificación de 40/50 casillas, «la libertad cuesta un 60 %» con su desarrollo y el recuadro «Los dos peajes» con su tabla de porcentajes. Todo eso está en el Apéndice A.10 (`maq-economia`), así que en 5.2 queda una frase con enlace y el remate «el precio de las Firmas es ser una nulidad».
  - El aviso de que el equipo se come los puntos se queda en una frase.
  - «¿Y empezar en 3?» se queda en una línea dentro de la experiencia de salida.
- **5.3**: la tabla entera se queda. El texto se queda en dos párrafos (la proporción 5/8, y el aviso del nivel que no has visto).
- **5.4**: «Lo que se paga y lo que no» y «La cuenta, paso a paso» se funden en una sola lista de 9 pasos, una línea por regla:
  - Los bonos en puntos, con los precios de dificultar la defensa: Esq Parcial 1, Difícil 2, Abs Máx 1 1.
  - Los permisos, vagos a propósito, entre ÷2 y ×3, sin bajar de 1, con el total divisible.
  - Los niveles: n²; la Limitada, la mitad al alza; a un nivel cuesta igual, con enlace a 4.3, sin repetir el consejo. Lo de «Ignora todo» va a 6.3.
  - Lo que anula, y la Parca, en Llaves; una Llave por rasgo, con enlace a 5.6.
  - Todo un ámbito es Rejilla.
  - El Ajuste, y el mínimo de 1.
  - Un solo ejemplo: el dron, corto.
  - Fuera: la capa de invisibilidad como ejemplo del mínimo (vive en 4.6 y queda una línea en 5.5) y los hechizos como «caso más claro» (vive en 4.7; queda un enlace).
  - Se quedan las dos pruebas y «Cuánto dura».
  - Los ids `ch5-quese` y `ch5-pasos`: `ch5-quese` desaparece porque nadie lo enlazaba; `ch5-pasos`, `ch5-dura`, `ch5-minimo` y `ch5-permisos` siguen (`ch5-permisos` ahora en un `<li>`).
- **5.5**: queda un ejemplo, la invisibilidad en una línea, con enlace a 4.6.
  - Fuera: el ejemplo de volar Desatado y el de «el dron de 5.4».
  - Se quedan la tabla, el recuadro (solo paga lo no pagado, la pregunta de calibración, volver a etiquetar, más de ×3) y el «+3 Desatado el día uno» en dos frases.
- **5.6**:
  - Las tres cosas que da el equipo quedan en un párrafo, sin el bazuca ni la cabaña: el bazuca vive en 4.5 y en el taller.
  - **Las armas** quedan en cinco líneas de regla: daño gratis; dificultar en puntos; anular en Llaves, con la pistola y los blásters por convenio del género; la Parca Limitada al daño, con sus tres precios; una Llave por rasgo, con la Parca y Abs Nula.
  - Pasan al taller del Bazar: el lanzagranadas, la granada, el cañón de riel y el texto largo de «un arma brutal cuesta pocas Llaves».
  - La Sincronización y su precio quedan en una línea; la regla vive en 3.8.
  - «Las cuatro categorías» pasan al taller del Bazar (`bz-fabrica`), junto a «Cómo encontrar».
  - «Los poderes no llevan Acceso» se queda en una línea en los cerrojos. En el Bazar, otra línea con enlace.
  - Recursos: se quedan la tabla y el tirón, más cortos.
- **5.7**: un ejemplo, el C4 robado, que antes era una aclaración. El cañón de riel robado se va. Se quedan devolver, traspasar, mano y cabeza, y los regalos. El robot de la misión se queda aquí, que es su casa.
- **5.8**:
  - Fuera los dos párrafos de entrada, la lista de las «dos bolsas» (repetía 5.1) y la frase de los juegos que dan experiencia al fallar.
  - El acordeón se queda en una frase con enlace a 2.4. «Nadie se queda atrás», en un enlace a 3.6.
  - Se quedan las tablas, los premios, ventajas y lacras (con [Lento], la sesión 0 y «ocurren») y la tesis del autor.
- **5.9**: de 22 aclaraciones queda una, la Transformación (una línea y enlace a 9.1, la regla del «no vale como truco»). Las demás ya estaban en el cuerpo o en su casa:
  - Ya en el cuerpo: subir una Disciplina, el poder de tres cosas, menos de una Llave, la Rejilla que no quieres subir, empezar en 3, los 14 puntos, la Llave por cabeza, por qué un arma cuesta poco, la pistola y el hacha, el bláster, las dos Llaves por rasgo, la katana, el bazuca, la granada, el C4, el exoesqueleto y el robot.
  - En 4.3 o en el taller: el consejo de «Armas contra los vampiros» (4.3); la katana, el bazuca, la granada, el exoesqueleto y el robot (taller).
  - La errata del catálogo pasa al taller del Bazar.
  - Los ids `ch5-acl-puntos` y `ch5-acl-equipo` desaparecen; nadie los enlazaba.

## Cap. 7

- **7.2**: después de Inés, `h4#ch7-casos` «Dos fichas de salida», con los casos A y B: sus tablas y cuentas (14 + 5 Llaves, o 14 + Rejilla Social 2), y enlaces a 2.2, 4.1, 4.4 y 5.2, sin reexplicar.
  - El primer caso lleva `id="ch5-casos"` para no romper el enlace de `fJ2_cap9b.html:254` (ED-16).
- **Fuera de 7.2**:
  - La tabla «La cuenta, de un vistazo». Repetía la ficha de Inés y está en los expedientes.
  - El consejo de la Llave Limitada de un nivel en el paso 5 de Inés: ahora es media frase con enlace a 4.3.
  - En el paso 4 de los seis pasos, la repetición del bote.
  - En «Los aspectos» y [Lento], lo que ya dice 5.8: queda una frase con enlace.
- **7.1**: la casilla del decorado queda en una línea con enlace a 7.5.
- **7.6**: de 8 aclaraciones quedan 2: el decorado que te hace daño y cuándo una ficha rápida pasa a completa. Fuera:
  - Las Llaves de Inés sin objetivo (4.3).
  - Los 14 de Inés (5.2).
  - Arcano y los hechizos (4.7, y ya en Inés).
  - Las Llaves en blanco (4.4).
  - El +0 de la ficha rápida (7.4).
  - El nivel del decorado (7.5).

## Bazar (`fK1_bazar_a.html`)

- **`bz-fabrica`**:
  - Un párrafo de procedimiento, con enlace a 5.4, 5.5 y 5.6, en vez de la lista de 4 pasos que repetía 5.4.
  - Fuera la línea de la invisibilidad (casa 4.6 y 5.5).
  - Nuevo `h4#bz-casos` «Casos resueltos»: una tabla de 11 casos (columnas Puntos y Llaves): el hacha y la pistola, el bláster, la katana monofilo, la de «no se esquiva y no se absorbe» sin Parca, el bazuca, el francotirador (Parca + Esq Nula), el cañón de riel, la granada, el lanzagranadas (munición y carcaj), el exoesqueleto y el robot de la misión.
  - La errata del catálogo, en una frase.
  - La tabla de las cuatro categorías se une a «Cómo encontrar».
  - Los números cuadran con el catálogo: la pistola, 1 Llave; el bláster, 1 punto y 0 Llaves; la katana, 1 Llave; el lanzagranadas, 2 puntos y 1 Llave; el cañón de riel, 3 Llaves; el exoesqueleto, 20 Llaves.
- **`bz-precios`**: quitada la línea repetida «a un nivel la Limitada cuesta lo mismo», que ya estaba en la viñeta de la Parca.
- **`bz-lectura`**: el párrafo «Las tablas de poderes no llevan Acceso» se queda en una frase con enlace a 5.6. Lo del coche de la familia ya está en 5.6.

## Comprobaciones

- Ningún id duplicado en `src/v2/f*.html`. No hay enlaces colgando que salgan de mis cambios; el único colgando del conjunto es `#acelerado`, en `fA`, que no es mío.
- Se conservan todos los ids que otros enlazaban: `ch5`, `ch5-monederos`, `ch5-salida`, `ch5-casos` (ahora en 7.2), `ch5-cambio`, `ch5-cuenta`, `ch5-dura`, `ch5-ajuste`, `ch5-equipo`, `ch5-armas`, `ch5-sincro`, `ch5-devolver`, `ch5-progreso`, `ch5-dones`, y los `ch7-*`.
- Ids quitados, ninguno enlazado: `ch5-quese`, `ch5-categorias`, `ch5-bolsas`, `ch5-acl-puntos`, `ch5-acl-equipo`.
- El HTML de los tres ficheros está equilibrado. `fK1` deja abierta la `<section id="apx-bazar">` a propósito, como antes: la cierra `fK3`.

## Dudas

1. **`fJ2_cap9b.html:254`** enlaza `#ch5-casos` con la etiqueta «5.2». El id sigue vivo, ahora en 7.2. Quien lleve fJ2 debería cambiar la etiqueta a 7.2, o el enlace a `#ch7-casos`.
2. **Caso A**: lleva una Llave de Armas de un nivel y Firma en Pistolas. No he dicho nada de si su pistola paga además su Llave (no se esquiva a nivel 1), porque la Llave de Armas ya le pone un nivel por encima contra un humano y no sé si eso es «el mismo concepto». El canon no lo zanja.
3. **Granada «siempre llena»**: en el taller, «paga como el lanzagranadas» (Parca 2, 1 Llave; Esq Difícil, 2 puntos). Es cuenta derivada, no palabra del autor.
4. **5.9** queda con una sola aclaración. Si el coordinador quiere más, las candidatas son las que pasan a índice en la FAQ.
