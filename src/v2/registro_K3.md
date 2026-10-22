# Registro K3 · Bazar, resumen e índice (`fK3_bazar_c.html`)

Fragmento sin `<section>` propio: sigue dentro de `apx-bazar` (la abre K1, la continúa K2) y **la cierra** con `</section>` al final. Unos 66 KB, 419 líneas: el resumen (14 filas) y el índice (372 filas en 5 tablas).

Además he tocado `fK1_bazar_a.html` para unificar sus precios con el capítulo 5 y con K2 (sección 3).

## 1. De dónde sale cada parte

| Viejo (`frag_bazar.html`) | Nuevo |
|---|---|
| 728–746 (`bz-resumen`, tabla) | `bz-resumen`, copiado por script y corregido a mano: recuentos rehechos (ver 4) |
| 747 (h3 `bz-indice`) | igual |
| 748 (párrafo de entrada del índice) | igual, más dos frases: cómo va ordenado y que los precios son los del catálogo, para un portador de nivel 1 (enlace a `bz-lectura`) |
| 749–1144 (las cinco tablas del índice) | **regeneradas por script** a partir de las filas de `fK1_bazar_a.html` (ya corregido) y `fK2_bazar_b.html`: nombre, «De dónde» (el h3 de la fila), «Qué hace» (celdas Daño y Esq) y «Precio» (columnas Acceso, Puntos, Llaves). Se conserva la categoría vieja de cada objeto, salvo los 24 Útiles que ahora cuestan puntos o Llaves (ver 2) |
| 1145 (`</section>`) | igual: cierra `apx-bazar` |

El índice viejo lo había generado `src/archivo/w_indice2.py` desde `app_data.json`, con un clasificador por palabras. El nuevo copia su formato y su orden: dentro de cada categoría, Acceso de menos a más (los poderes, sin Acceso, al final), y con el mismo Acceso, más Llaves primero. He añadido los puntos como segundo desempate y he quitado los acentos al ordenar por nombre (el viejo ponía «Báculo» detrás de «Bate»).

## 2. Lo que he tirado o cambiado, y por qué

- **Todos los precios del índice viejo** (260 de 371 filas cambian): eran los de antes del 22 oct. Ahora son los del catálogo, fila a fila (REVISION B·Bazar: «el índice no cobra Llaves que el catálogo sí»; e5, e8).
- **«Qué hace» de 20 filas**: las armas de fuego pasan a `Esq: Nula` (e8), y los daños `Masivo`, `Absoluto`, `Infinito` pasan a `La Parca · Rejilla N` (c2), como en el catálogo.
- **24 objetos pasan de Útiles a Artefactos y poderes**: la tabla de búsqueda de K1 dice «Útil: cuesta solo Acceso», y estos ahora pagan puntos o Llaves. Son Anillo de Invisibilidad, Botas de Levitación, Gema de Luz, Camuflaje Termo-Óptico, Ciberojos, Implante de tiempo lento, Inhibidor de Dolor, Piernas Reforzadas, Generador de Camuflaje, Implante de Traducción, Cinturón de Artilugios, Capa Planeadora, Cuerda de la Confesión, Visor de Detective, Manto que Levita, Cubo de Poder Estelar, Regeneración Rápida, Suero del Soldado Perfecto, Telequinesis, Vuelo Supersónico, Botas de Resorte, Guantelete Magnético, Respirador de Carbón y La Pintura de Túnel. Las cuentas quedan así: Armas 168, Defensas 36, Vehículos 19, Artefactos y poderes 124, Útiles 25.
- **Resumen**: los recuentos viejos no cuadraban. «294 = 286 + 8 sociales» y «Piezas sueltas 53» eran cifras de antes: las diez ambientaciones suman 297, el Duelo Social tiene 16 y las piezas sueltas 59 (58 viejas y el Arma de fuego nueva de K2). El total queda en 313 + 59 = 372, que son las filas del índice. Fuera la frase «La conversación daba 290 + 8… Hasta 300 faltan 14», que salía de las cifras equivocadas. Se quedan los cuatro duplicados fusionados.
- **Duelo Social**: fuera «Pendiente, faltan al menos 2», como en K2 (16 caben en las 10–20 pedidas).
- **«Wuxia / Anime»** → «6. Artes marciales, brillos y gritos» (es el nombre del h3).
- **«el precio hecho en las tres monedas»** → «con el precio hecho: Acceso, puntos y Llaves» (5.4). Las tres monedas, como teoría, se retiraron de F (C·e3: dos monederos y el Acceso).

## 3. La unificación de K1 con el capítulo 5

Regla que manda (`fF_cap5.html`, 5.4 paso 6 y 5.6 «Las armas»): la Parca de nivel N te pone *n* = N − 1 niveles por encima de un portador de nivel 1, y cubre el daño, no el acierto, así que va **Limitada al daño**: la mitad al alza de *n*², y a un nivel no se separa. Parca 2 → 1, 3 → 2, 4 → 5, 5 → 8, 6 → 13. K1 había cobrado (N − 1)², el precio completo.

Donde el capítulo 5 no lo dice, he seguido a K2:

- **Parca que además no se esquiva**: 1 Llave más («la Parca sola cubre el daño, no el acierto»). Su `Abs: Nula` va dentro.
- **La esquiva o la absorción de la Parca que dificulta la defensa** (`Esq: Difícil` 2 puntos, `Esq: Parcial` 1, `Abs: Máx 1` 1): se cobra en puntos, como en cualquier arma. K1 decía «su esquiva no se cobra aparte».
- **`Esq: Nula` y `Abs: Nula` a la vez** (sin Parca): dos defensas anuladas, **2 Llaves**, como La Filtración de K2. K1 cobraba 1 por las dos. Lo apoya 4.2: «le quita la que dice, y la otra se tira».
- **`Esq: Nula` en un ataque mental** que se resiste con la mente: se cobra (1 Llave), como Telepatía y el Reloj Hipnótico de K2. K1 decía «la Esq: Nula no anula nada».
- **Vehículo con nivel**: la Llave de su nivel completa, con su Parca dentro, y en puntos las etiquetas que dificultan la defensa (el Coche Blindado de K2).
- **Arma con «Rejilla: Nivel N»**: una Llave de Armas Limitada al daño, como el Martillo Digno de K2.
- **`Abs: Máx 1` con Daño 1**: no se cobra (la tabla de K2 lo cobra solo «con Daño 2»; su Guante de Boxeo no lo paga).

Lo que ya coincidía y no se ha tocado: permisos permanentes a 1 Llave aunque el Acceso sea 0, lo de un solo uso a 0, Sincronización a 5·*n*², Limitada condicional de un nivel a 1, permiso más anulación que pagan las dos cosas, Esq: Parcial 1 / Difícil 2 / Abs: Máx 1 1.

### Filas de K1 cambiadas (nombre → precio viejo → nuevo)

| Objeto | Antes | Ahora | Por qué |
|---|---|---|---|
| El filo imposible (Corta-Dioses) | Acceso 3 · 25 Llaves | Acceso 3 · **13 Llaves** | Parca hasta 6, Limitada; se esquiva. Alternativas de la nota: 1, 2, 5, 8 |
| Proyectil Mágico | Acceso 1 · 2 Llaves | Acceso 1 · **3 Llaves** | hechizo 1 + Esq Nula 1 + Abs Nula 1 |
| Rayo Relámpago | Acceso 2 · 2 Llaves | Acceso 2 · **3 Llaves** | hechizo 1 + dos anulaciones contra metal (Limitadas, 1 cada una) |
| Aliento de Dragón | Acceso 2 · 4 Llaves | Acceso 2 · **2 puntos · 2 Llaves** | Parca 3 Limitada; Esq Difícil |
| Rifle de Francotirador (Antimaterial) | Acceso 3 · 1 Llave | Acceso 3 · **2 Llaves** | dos anulaciones |
| Lanzagranadas | Acceso 2 · 1 Llave | Acceso 2 · **2 puntos · 1 Llave** | Parca 2; Esq Difícil |
| Cañón de Riel (Railgun) | Acceso 3 · 4 Llaves | Acceso 3 · **3 Llaves** | Parca 3 Limitada 2 + no se esquiva 1 |
| Hielo Negro (virus) | Acceso 2 · 1 Llave | Acceso 2 · **2 Llaves** | dos anulaciones |
| Bengala de Señales | Acceso 1 · 1 Llave | Acceso 1 · **2 Llaves** | dos anulaciones |
| Coche (atropello) | Acceso 3 · 1 Llave | Acceso 3 · **3 puntos · 1 Llave** | vehículo de nivel 2; Esq Difícil + Abs Máx 1 |
| Muñeco Vudú | Acceso 1 · 2 Llaves | Acceso 1 · **3 Llaves** | permiso 1 + dos anulaciones |
| Cañón de Iones | Acceso 1 · 1 Llave | Acceso 1 · **2 Llaves** | dos anulaciones Limitadas |
| Guantelete de Choque | Acceso 0 · 1 punto | **Acceso 0** | Abs Máx 1 con Daño 1 no se cobra |
| Rayo del Flujo | 2 Llaves | **3 Llaves** | permiso 1 + dos anulaciones |
| Truco Mental | 1 Llave | **2 Llaves** | permiso 1 + Esq Nula 1 |
| Estrangular | 2 Llaves | **3 Llaves** | permiso 1 + dos anulaciones |
| El «Gordo» (lanzabombas) | Acceso 3 · 4 Llaves | Acceso 3 · **1 punto · 2 Llaves** | Parca 3 Limitada; Esq Parcial |
| Interceptor V8 | Acceso 3 · 1 Llave | Acceso 3 · **3 puntos · 1 Llave** | vehículo de nivel 2; Esq Difícil + Abs Máx 1 |
| El Puño de los Cien Puños | 1 Llave | **2 Llaves** | Parca 2 + no se esquiva |
| Onda de energía a dos manos (rayo) | 4 Llaves | **3 puntos · 2 Llaves** | Parca 3 Limitada; Esq Difícil + Abs Máx 1 |
| Disco Destructor | 4 Llaves | **2 Llaves** | Parca 3 Limitada; se esquiva. No tenía nota «La cuenta»: añadida |
| Bomba de Energía | 5 Llaves | **6 Llaves** | Parca 4 Limitada 5 + no se esquiva 1 |
| La Mirada (Dominación) | 1 Llave | **2 Llaves** | permiso 1 + Esq Nula 1 |
| Espada Ancestral | Acceso 3 · 1 punto · 4 Llaves | Acceso 3 · **1 punto · 2 Llaves** | nivel 3 Limitado al daño; Abs Máx 1 |
| Amuleto Solar | Acceso 3 · 2 Llaves | Acceso 3 · **3 Llaves** | Parca 3 Limitada 2 + no se esquiva 1 |

En las 25 he reescrito también la nota «La cuenta», con enlace a 5.6 (`ch5-armas`) donde entra la Parca. Sin tocar, porque son de un solo uso (0): Granada Térmica, Granada de Fósforo, Granada EMP, Elixir de Vitae.

En el recuadro `bz-precios` de K1 he reescrito tres puntos: «Lo que anula» (las dos anulaciones pagan 2), «La Parca y la Rejilla» (la escalera Limitada 1, 2, 5, 8, 13; +1 si no se esquiva; esquiva y absorción difíciles en puntos; vehículo con nivel a precio completo) y «Lo que dificulta» (con Daño 1, `Abs: Máx 1` no se cobra).

**Para el coordinador:** la tabla 5 de `registro_K1.md` («Tabla para K3») tiene todavía los precios viejos de estas 25 filas. Mandan el fragmento y esta lista.

## 4. Índice contra catálogo

- **Están en el índice viejo y no en el catálogo:** ninguno. Las 371 filas viejas se encuentran por nombre y ambientación.
- **Están en el catálogo y no en el índice viejo:** uno, **Arma de fuego** (pieza suelta nueva de K2). Añadida a Armas.
- El índice nuevo tiene 372 filas, una por fila del catálogo (K1 207, K2 165), y sin duplicados. Lo comprueba el script.

## 5. Dudas para el autor

1. **`Esq: Nula` y `Abs: Nula` a la vez: ¿1 Llave o 2?** He puesto 2, como K2 y como dice 4.2 («le quita la que dice, y la otra se tira»). Pero l2 dice que una Llave de un nivel deja al de abajo sin tirada, y eso es leerlo como una sola Llave. Afecta a 9 filas de K1 (Proyectil Mágico, Rayo Relámpago, Francotirador Antimaterial, Hielo Negro, Bengala, Muñeco Vudú, Cañón de Iones, Rayo del Flujo, Estrangular) y a La Filtración de K2.
2. **Parca que no se esquiva: +1 Llave** (es la duda 1 de K2). Si una Parca inesquivable es una sola Llave, bajan 1 el Cañón de Riel, el Puño, la Bomba de Energía y el Amuleto Solar, y las de K2.
3. **La esquiva difícil de una Parca, en puntos** (es la duda 2 de K2). K1 decía que es lo que la Llave deja intentar, y que cobrarla haría más cara una Parca esquivable que una que no lo es. Con la regla actual, el Aliento de Dragón (2 puntos · 2 Llaves) cuesta casi lo mismo que el Cañón de Riel (3 Llaves).
4. **Dos correas en la misma Parca.** El Gordo (bombas que escasean), la Bomba de Energía (tres turnos de carga) y el Amuleto Solar (solo vampiros) ya van Limitados al daño. No he aplicado una segunda mitad: el Amuleto lleva una sola, y en las otras dos la nota remite al Ajuste (5.5).
5. **`Esq: Nula` en un ataque que se resiste con la mente** (Truco Mental, La Mirada): lo he cobrado como K2. K1 decía que ahí no anula nada.
6. **Espada Ancestral**: como el Martillo Digno de K2, una Llave de Armas Limitada al daño (2). Si «opera en nivel 3» quiere decir Armas completa contra todo, son 4.
7. **Guantelete de Choque**: a 0 por la regla de K2 (con Daño 1, `Abs: Máx 1` no hace nada salvo en el crítico). Así se queda en un arma de Acceso, como un cuchillo.
8. **Daga Ritual**: no la he tocado. Su `Abs: Nula` va dentro de la Llave contra espíritus, igual que las Balas de Plata (K1) y la Bala Bendita (K2). Si la `Abs: Nula` vale contra todos, serían 2.
9. **Los Útiles que pasan a Artefactos**: es una lectura mía de la tabla de búsqueda de K1. Si preferís que la categoría siga siendo «lo que es» y no «lo que cuesta», se pueden devolver.
10. **Coche Blindado (K2), 4 Llaves**: como vehículo paga su nivel 3 completo. Si se leyera como una Parca 3 Limitada, serían 2. Lo dejo como K2, que sigue a 5.6 («un vehículo normal no hereda nada… el cañón del tanque es una Llave»).

## 6. Enlaces salientes

En `fK3_bazar_c.html`: `ch5-cuenta` (F), `bz-lectura` (K1).
Añadidos en `fK1_bazar_a.html`: `ch5-armas` y `ch5-ajuste` (F). Existen los dos en `fF_cap5.html`.
