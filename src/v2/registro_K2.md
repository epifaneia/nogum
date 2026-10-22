# Registro K2 · Bazar, segunda parte (`fK2_bazar_b.html`)

Fragmento sin `<section>` propio: continúa dentro de `apx-bazar` (la abre K1) y no la cierra (K3). Empieza en el h3 `bz-supers` y acaba en el párrafo final de `bz-piezas`. 165 filas de catálogo (164 viejas + 1 nueva), unos 72 KB.

El catálogo se ha copiado por script (Python, línea a línea) y se ha corregido entrada a entrada con una tabla de precios. Las tablas pasan de la columna vieja «Acceso / Rejilla» a tres columnas numéricas: **Acceso · Puntos · Llaves**. Las etiquetas que vivían en esa columna (`Rejilla: Nivel N`, `Permiso`, `Efecto`, `Fractal`, `Inmunidad`, `Llave: criatura`) y su texto pasan al principio de «Notas». Cabecera usada:

```html
<thead><tr><th>Objeto</th><th>Daño</th><th>Esq</th><th>Abs</th><th class="num">Acceso</th><th class="num">Puntos</th><th class="num">Llaves</th><th>Notas</th></tr></thead>
```

**Para el coordinador:** si K1 ha usado otra cabecera, hay que unificar (las tablas `t arsenal` tienen anchos fijos en `paper.css` para cinco columnas; con ocho conviene revisarlos).

## 1. De dónde sale cada parte

| Viejo (`frag_bazar.html`) | Nuevo |
|---|---|
| 481–482 (h3 y lema de Capas y mallas) | `bz-supers` |
| 483–497 Superpoderes (como equipo) | `bz-supers`, h4 igual |
| 498–512 Gadgets de justiciero | `bz-supers`, h4 igual |
| 513–527 Objetos cósmicos | `bz-supers`, h4 igual |
| 528–529 (h3 y lema del Oeste Extraño) | `bz-steampunk` |
| 530–544 Armas de pólvora y vapor | `bz-steampunk` |
| 545–559 Inventos de ciencia extraña | `bz-steampunk` |
| 560–574 Ocultismo y póker | `bz-steampunk` |
| 575–576 (h3 y lema del Mundo Animado) | `bz-toon` |
| 577–578 (notas de proceso T71/T78) | `bz-toon`, ahora en `<aside class="meta">`, con la cuenta corregida (30 ítems, completa) |
| 579–599 Armas de tienda de bromas | `bz-toon` |
| 600–618 Poderes toon | `bz-toon` |
| 619–641 Duelo Social: h3, lema, Arsenal social | `bz-social` |
| 642 (párrafo de cierre del Duelo Social) | `bz-social`, sin el «faltan al menos 2» (hay 16, dentro de las 10–20 pedidas) |
| 643–644 (h3 y entrada de Piezas sueltas) | `bz-piezas`, con enlace a 5.4 |
| 645–667 Armas | `bz-piezas` (+ una fila nueva, «Arma de fuego») |
| 668–683 Defensas | `bz-piezas` |
| 684–698 Vehículos | `bz-piezas` |
| 699–725 Artefactos y poderes | `bz-piezas` |
| 726 (párrafo final) | `bz-piezas`, remite a `bz-fabrica` y a 5.4 |
| 727 (línea en blanco) | — |

## 2. Lo que he tirado o cambiado, y por qué

- **Daño: Infinito** (Gema Primordial) → `La Parca · Rejilla 6` (lo cósmico es 6, C·22oct). **Daño: Masivo (Espiritual)** (Excomunión) → `La Parca · Rejilla 4` (la bomba nuclear de la Tabla 2). Patrón B del Bazar en REVISION: el daño de un arma llega a 2, más la Parca (c2).
- **Armas de fuego** (Revólver, Winchester, Escopeta de Dos Cañones) → `Esq: Nula` y 1 Llave (e8). La escopeta pierde su `Esq: Parcial` por la dispersión: el arma de fuego no se esquiva a nivel 1.
- **Piezas sueltas**: «pistola pequeña» sale de Proyectil ligero y «rifle, arma larga» de Proyectil pesado (ahora «ballesta, arco largo, jabalina»); para ellas se añade la fila **Arma de fuego** (Daño 2, Esq: Nula, Abs: Total, Acceso 1, 1 Llave), con la frase de los blásters (C·22oct). La cuenta de piezas sube de 58 a 59 (el resumen viejo decía 53; **K3**: contadlas de nuevo).
- **Arma de maestro armero**: fuera «y es un suelo: no le hace nada a quien ya tiene Armas +1» (bz:652, a2 y 22 oct: los bonos se acumulan, a criterio de mesa). Ahora: «se suma a lo que ya tengas» (enlace 2.5).
- **Suero del Soldado Perfecto**: fuera «capacidades físicas al máximo humano (+4)» y la nota «se lee como +4 en las tiradas físicas (el tope canónico)». La Tabla 1 aprobada pone al soldado del suero en N2 Físico: el suero da la Rejilla (5 Llaves si se compra; la abre la historia, r8).
- **Brazo Mecánico a Vapor**: subía la Rejilla Física sin Llaves (bz:549). Ahora 5 Llaves de Rejilla, Limitada por el carbón: 3.
- **La lista**: fuera «No te matan» (bz:663, l8: la muerte no se nombra en la Parca). Ahora «Quedas fuera de combate en lo social».
- **Inmortalidad Cómica**: «Nunca sales de la historia» → «No sales de la historia», y enlace a 0.7 (la muerte se pacta).
- **Sierra de Suelo**: el daño de caída «de 1 a 3» → «1 o 2, o la Parca si es alta de verdad» (c2).
- **Velo absoluto, Fuerza de sala, Fuerza de edificio, Oído de multitud, Mando de multitud**: las cuentas usaban 2·x² contra todo («idea 5», retirada). Ahora n² por Disciplina contra todo (l4, e2).
- **Capa de invisibilidad**: la etiqueta duplicada «1 Llave · Acceso 2» se queda en sus columnas.
- **Bombas de humo, dinamitas, bombas toon, Tarta, Inyector, Elixir de Aceite, Bala Bendita, Cohete a la Espalda, Túnel Pintado, La bomba de los mil soles**: de un solo uso, 0 (C·22oct), con la nota de cuánto costarían si nunca se acaban.
- Enlaces viejos reescritos: `#ch2-rejilla` (Sincronización, 2.4) → `#ch3-sincro` 3.8; «(2.3)» del Cristal → `#ch4-llave` 4.1; «(5.3)» de la caída → `#ch6-armas` 6.3. «Wuxia / Anime» → «Artes marciales» (el nombre del h3 6).
- Las marcas `src` viejas (T70, T78, T107, T124, T181) y los `flag ed` (ED-B1, B2, B3) se conservan. Lo nuevo lleva `C·e8`, `C·l4`, `C·l9`, `C·e2`, `C·e7`, `C·m3`, `C·l2` o `C·22oct`.

### La tabla de precios que he aplicado (para un portador de nivel 1)

Sigue `fF_cap5.html` (5.4 «La cuenta», 5.6 «Las armas»), que es el sitio del precio:

- Daño: gratis.
- Dificultar la defensa, en puntos: `Esq: Difícil (−2)` 2; `Esq: Parcial` 1; `Abs: Máx 1` (con Daño 2) 1. `Esq: Fácil` no descuenta.
- Anular una defensa a tu nivel, en Llaves: `Esq: Nula` 1; `Abs: Nula` 1 (5.6: «no la dificulta, la anula»). Condicional (por sorpresa, contra metal): Limitada, que a un nivel sigue siendo 1.
- La Parca: Limitada al daño, la mitad al alza: Parca 2 → 1, 3 → 2, 4 → 5, 5 → 8, 6 → 13. No cubre el acierto: si además no se esquiva, +1 Llave. Su `Abs: Nula` va dentro (no hay tirada de soportar). Su `Esq: Difícil`, puntos.
- Permiso permanente: 1 Llave, aunque el Acceso sea 0; Potenciado 2, Desatado 3.
- Llave de Disciplina: n² contra todo; Limitada (al daño, a un solo ser) la mitad al alza.
- Rejilla de un ámbito (Sincronización, el suero, el brazo): 5·n²; Limitada la mitad al alza.
- Vehículo con nivel: la Llave de su nivel, completa (n²), con su Parca dentro.
- Absorción fija y +1 a defender: 1 punto cada uno.
- De un solo uso: 0.
- Poderes (superpoderes, cósmicos, toon, arsenal social): Acceso «—».

## 3. Dudas para el autor

1. **La Parca con `Esq: Nula`**: la he cobrado como dos cosas (la Parca Limitada + 1 Llave porque no se esquiva), siguiendo 5.6 («la Parca sola cubre el daño, no el acierto»). El francotirador o el arma inevitable salen a 2 Llaves. ¿Vale, o una Parca que no se esquiva es una sola Llave?
2. **Las etiquetas de lo que tiene nivel** (Coche Blindado nivel 3, Gatling Parca 2, Control del Clima): he cobrado en puntos su `Esq: Difícil` y su `Abs: Máx 1`, porque contra quien está a su altura dificultan la defensa. Encarece la Gatling a 1 Llave y 3 puntos.
3. **Superfuerza y Martillo Digno (nivel 4)**: los he leído como Llave al daño, Limitada (5), más 1 por `Abs: Nula` = 6. Si la Superfuerza es Pelea completa contra todo, serían 9 (+1).
4. **`Abs: Nula` en lo cotidiano y cómico**: con 5.6, la Sartén, el táser (Arma aturdidora), la Baraja Maldita o la Seducción Agresiva pagan 1 Llave. Es coherente con la katana monofilo, pero se nota en el Mundo Animado.
5. **Pistola de Clavos a Presión y Cañón de Mano**: no las he hecho armas de fuego inesquivables. La de clavos no es de pólvora; el cañón de mano lleva `Esq: Fácil (+2)` (es el ejemplo de «Fácil» del cap. 6). ¿Se quedan así?
6. **Túnel Pintado y La Pintura de Túnel** son casi el mismo objeto. Los he separado por precio (el túnel ya pintado, de un uso, 0; la pintura, permanente, 1 Llave). ¿Se funde uno?
7. **Precios que son lectura mía donde la fuente no daba números**: Manto que Levita (1 Llave + 1 punto), Anillo de Voluntad (2, Potenciado), Salir del Plano (3, Desatado), Simbionte («1+»: lo que cuesten sus poderes), Reactor de Pecho (0: no hace nada en la ficha por sí solo), Excomunión en Parca 4 (por «bomba nuclear social»), Gema en Parca 6. Son neutros y a ojo de buen cubero (l9); mirad si alguno chirría.
8. **Pistola de Gancho y Araña Mecánica Espía**: los he dejado como útiles (solo Acceso), no como permisos.

## 4. Enlaces salientes

`bz-fabrica` (K1) · `ch0-muerte` · `ch2-bonos` · `ch3-ejemplos` · `ch3-sincro` · `ch3-subir` · `ch3-techos` · `ch4-ejemplos` · `ch4-escalera` · `ch4-llave` · `ch4-parca` · `ch4-tipos` · `ch5-ajuste` · `ch5-armas` · `ch5-cambio` · `ch5-cuenta` · `ch5-dura` · `ch5-sincro` · `ch6-armas` · `ch6-dano`. Todos comprobados en los fragmentos de A, C, D, E, F, I, salvo `bz-fabrica`, que es de K1.

## 5. Precios cambiados (para el índice de K3)

Formato: Acceso · puntos · Llaves. «Antes» es lo que decía la ficha vieja del catálogo (no el índice viejo). 112 filas, incluida la pieza nueva.

| Objeto | Antes | Ahora | Etiquetas cambiadas |
|---|---|---|---|
| Visión Láser / Calorífica | Acceso — · 0 pt · 0 Ll | Acceso — · 1 pt · 2 Ll | — |
| Superfuerza (Golpe) | Acceso — · 0 pt · 0 Ll | Acceso — · 0 pt · 6 Ll | — |
| Vuelo Supersónico | Acceso — · 0 pt · 0 Ll | Acceso — · 0 pt · 1 Ll | — |
| Piel Invulnerable | Acceso — · 0 pt · 0 Ll | Acceso — · 0 pt · 2 Ll | — |
| Grito Sónico | Acceso — · 0 pt · 0 Ll | Acceso — · 1 pt · 2 Ll | — |
| Telequinesis | Acceso — · 0 pt · 0 Ll | Acceso — · 0 pt · 1 Ll | — |
| Telepatía | Acceso — · 0 pt · 0 Ll | Acceso — · 0 pt · 2 Ll | — |
| Intangibilidad (Fase) | Acceso — · 0 pt · 0 Ll | Acceso — · 0 pt · 2 Ll | — |
| Regeneración Rápida | Acceso — · 0 pt · 0 Ll | Acceso — · 0 pt · 2 Ll | — |
| Control del Clima (Rayo) | Acceso — · 0 pt · 4 Ll | Acceso — · 2 pt · 2 Ll | — |
| Cinturón de Artilugios | Acceso 0 · 0 pt · 0 Ll | Acceso 0 · 0 pt · 1 Ll | — |
| Bumerán afilado / Shuriken Explosivo | Acceso 1 · 0 pt · 0 Ll | Acceso 1 · 1 pt · 0 Ll | — |
| Capa Planeadora | Acceso 0 · 0 pt · 0 Ll | Acceso 0 · 0 pt · 1 Ll | — |
| Coche Blindado (El coche blindado del justiciero) | Acceso 3 · 0 pt · 4 Ll | Acceso 3 · 3 pt · 4 Ll | — |
| Escudo de metal que se come los golpes / Energía | Acceso 0 · 0 pt · 0 Ll | Acceso 0 · 0 pt · 1 Ll | — |
| Visor de Detective | Acceso 0 · 0 pt · 0 Ll | Acceso 0 · 0 pt · 1 Ll | — |
| Armadura de Combate Motorizada | Acceso 3 · 0 pt · 20 Ll | Acceso 3 · 0 pt · 21 Ll | — |
| Cuerda de la Confesión | Acceso 0 · 0 pt · 0 Ll | Acceso 0 · 0 pt · 1 Ll | — |
| Anillo de Voluntad | Acceso — · 0 pt · 0 Ll | Acceso — · 0 pt · 2 Ll | — |
| Cubo de Poder Estelar (fragmento) | Acceso — · 0 pt · 0 Ll | Acceso — · 0 pt · 1 Ll | — |
| Suero del Soldado Perfecto | Acceso — · 0 pt · 0 Ll | Acceso — · 0 pt · 5 Ll | — |
| Cristal de la piedra de su propio mundo | Acceso — · 0 pt · 0 Ll | Acceso — · 0 pt · 8 Ll | — |
| Casco Místico | Acceso — · 0 pt · 0 Ll | Acceso — · 0 pt · 1 Ll | — |
| Martillo Digno | Acceso — · 0 pt · 0 Ll | Acceso — · 0 pt · 6 Ll | — |
| Gema Primordial (una sola) | Acceso — · 0 pt · 0 Ll | Acceso — · 0 pt · 14 Ll | Daño: Infinito → La Parca · Rejilla 6 |
| Manto que Levita | Acceso — · 0 pt · 0 Ll | Acceso — · 1 pt · 1 Ll | — |
| Simbionte Alienígena | Acceso — · 0 pt · 0 Ll | Acceso — · 0 pt · 1+ Ll | — |
| Revólver «Pacificador» (.45) | Acceso 1 · 0 pt · 0 Ll | Acceso 1 · 1 pt · 1 Ll | Esq: Total → Esq: Nula |
| Rifle Winchester | Acceso 1 · 0 pt · 0 Ll | Acceso 1 · 0 pt · 1 Ll | Esq: Total → Esq: Nula |
| Escopeta de Dos Cañones | Acceso 2 · 0 pt · 0 Ll | Acceso 2 · 0 pt · 1 Ll | Esq: Parcial → Esq: Nula |
| Gatling de Vapor (portátil) | Acceso 2 · 0 pt · 1 Ll | Acceso 2 · 3 pt · 1 Ll | — |
| Rifle Tesla (Voltaico) | Acceso 2 · 0 pt · 0 Ll | Acceso 2 · 0 pt · 2 Ll | — |
| Cañón de Mano | Acceso 2 · 0 pt · 0 Ll | Acceso 2 · 1 pt · 0 Ll | — |
| Dinamita | Acceso 2 · 0 pt · 1 Ll | Acceso 2 · 0 pt · 0 Ll | — |
| Lanzallamas de Queroseno | Acceso 1 · 0 pt · 0 Ll | Acceso 1 · 1 pt · 1 Ll | — |
| Brazo Mecánico a Vapor | Acceso 1 · 0 pt · 0 Ll | Acceso 1 · 0 pt · 3 Ll | — |
| Monóculo de Análisis | Acceso 0 · 0 pt · 0 Ll | Acceso 0 · 0 pt · 1 Ll | — |
| Jetpack de Vapor | Acceso 0 · 0 pt · 0 Ll | Acceso 0 · 0 pt · 1 Ll | — |
| Chaleco Voltaico | Acceso 0 · 0 pt · 0 Ll | Acceso 0 · 1 pt · 0 Ll | — |
| Botas de Resorte | Acceso 0 · 0 pt · 0 Ll | Acceso 0 · 0 pt · 1 Ll | — |
| Guantelete Magnético | Acceso 0 · 0 pt · 0 Ll | Acceso 0 · 0 pt · 1 Ll | — |
| Respirador de Carbón | Acceso 0 · 0 pt · 0 Ll | Acceso 0 · 0 pt · 1 Ll | — |
| Sierra Mecánica de Combate | Acceso 2 · 0 pt · 0 Ll | Acceso 2 · 1 pt · 0 Ll | — |
| Baraja de Cartas Maldita | Acceso 0 · 0 pt · 0 Ll | Acceso 0 · 0 pt · 1 Ll | — |
| Amuleto de Chamán | Acceso 1 · 0 pt · 0 Ll | Acceso 1 · 0 pt · 1 Ll | — |
| Mano del Hombre Muerto | Acceso 0 · 0 pt · 0 Ll | Acceso 0 · 0 pt · 1 Ll | — |
| Lazo Espiritual | Acceso 0 · 0 pt · 0 Ll | Acceso 0 · 0 pt · 1 Ll | — |
| Tótem Animal | Acceso 0 · 0 pt · 0 Ll | Acceso 0 · 1 pt · 0 Ll | — |
| Reloj de Bolsillo Hipnótico | Acceso 1 · 0 pt · 0 Ll | Acceso 1 · 0 pt · 1 Ll | — |
| Escopeta Exorcista | Acceso 0 · 0 pt · 0 Ll | Acceso 0 · 0 pt · 1 Ll | — |
| Dinamita con Mecha Larga | Acceso 2 · 0 pt · 1 Ll | Acceso 2 · 0 pt · 0 Ll | — |
| Guante de Boxeo con Muelle | Acceso 0 · 0 pt · 0 Ll | Acceso 0 · 0 pt · 1 Ll | — |
| Bomba Redonda Negra | Acceso 2 · 0 pt · 1 Ll | Acceso 2 · 0 pt · 0 Ll | — |
| Sierra de Suelo | Acceso 0 · 0 pt · 0 Ll | Acceso 0 · 2 pt · 2 Ll | — |
| El Yunque Oportuno | Acceso 0 · 0 pt · 1 Ll | Acceso 0 · 0 pt · 2 Ll | — |
| La Sartén | Acceso 0 · 0 pt · 0 Ll | Acceso 0 · 0 pt · 1 Ll | — |
| El Mazo de Feria | Acceso 0 · 0 pt · 0 Ll | Acceso 0 · 1 pt · 0 Ll | — |
| La Caja de Cerillas Infinita | Acceso 0 · 0 pt · 0 Ll | Acceso 0 · 1 pt · 2 Ll | — |
| El Imán Gigante | Acceso 1 · 0 pt · 0 Ll | Acceso 1 · 2 pt · 2 Ll | — |
| La Pintura de Túnel | Acceso 2 · 0 pt · 0 Ll | Acceso 2 · 0 pt · 1 Ll | — |
| Espacio en los Bolsillos | Acceso — · 0 pt · 0 Ll | Acceso — · 0 pt · 2 Ll | — |
| Disfraz Instantáneo | Acceso — · 0 pt · 0 Ll | Acceso — · 0 pt · 1 Ll | — |
| Cuerpo de Goma | Acceso — · 0 pt · 0 Ll | Acceso — · 0 pt · 1 Ll | — |
| Regeneración de Escena | Acceso — · 0 pt · 0 Ll | Acceso — · 0 pt · 1 Ll | — |
| Salir del Plano | Acceso — · 0 pt · 0 Ll | Acceso — · 0 pt · 3 Ll | — |
| Inmortalidad Cómica | Acceso — · 0 pt · 0 Ll | Acceso — · 0 pt · 1 Ll | — |
| Ojos Saltones | Acceso — · 0 pt · 0 Ll | Acceso — · 1 pt · 0 Ll | — |
| Bajar la Cremallera | Acceso — · 0 pt · 0 Ll | Acceso — · 0 pt · 1 Ll | — |
| Cartel de «Socorro» | Acceso — · 0 pt · 0 Ll | Acceso — · 0 pt · 1 Ll | — |
| El Agujero Portátil | Acceso — · 0 pt · 0 Ll | Acceso — · 0 pt · 1 Ll | — |
| La Caída Diferida | Acceso — · 0 pt · 0 Ll | Acceso — · 0 pt · 1 Ll | — |
| El Disfraz Fino | Acceso — · 0 pt · 0 Ll | Acceso — · 0 pt · 1 Ll | — |
| Los Patines Cohete | Acceso — · 0 pt · 0 Ll | Acceso — · 1 pt · 1 Ll | — |
| El Segundo de Más | Acceso — · 0 pt · 0 Ll | Acceso — · 0 pt · 2 Ll | — |
| El Insulto Público | Acceso — · 0 pt · 0 Ll | Acceso — · 2 pt · 0 Ll | — |
| El Chantaje (la Prueba) | Acceso — · 0 pt · 1 Ll | Acceso — · 0 pt · 2 Ll | — |
| La Verdad Cósmica | Acceso — · 0 pt · 4 Ll | Acceso — · 0 pt · 3 Ll | — |
| La Orden de Mando (Voz de Alfa) | Acceso — · 0 pt · 0 Ll | Acceso — · 2 pt · 0 Ll | — |
| Seducción Agresiva | Acceso — · 0 pt · 0 Ll | Acceso — · 0 pt · 1 Ll | — |
| Luz de Gas (Gaslighting) | Acceso — · 0 pt · 0 Ll | Acceso — · 1 pt · 1 Ll | — |
| Excomunión / Destierro | Acceso — · 0 pt · 0 Ll | Acceso — · 0 pt · 6 Ll | Daño: Masivo (Espiritual) → La Parca · Rejilla 4 |
| El Silencio Calculado | Acceso — · 0 pt · 0 Ll | Acceso — · 0 pt · 1 Ll | — |
| El Elogio Envenenado | Acceso — · 0 pt · 0 Ll | Acceso — · 2 pt · 0 Ll | — |
| La Filtración | Acceso — · 0 pt · 0 Ll | Acceso — · 0 pt · 2 Ll | — |
| El Ultimátum Público | Acceso — · 0 pt · 0 Ll | Acceso — · 1 pt · 0 Ll | — |
| La Deuda Recordada | Acceso — · 0 pt · 0 Ll | Acceso — · 2 pt · 1 Ll | — |
| La Confesión Ajena | Acceso — · 0 pt · 0 Ll | Acceso — · 0 pt · 1 Ll | — |
| Arma a dos manos | Acceso 1 · 0 pt · 0 Ll | Acceso 1 · 1 pt · 0 Ll | — |
| Proyectil pesado | Acceso 2 · 0 pt · 0 Ll | Acceso 2 · 3 pt · 0 Ll | — |
| Arma de fuego (nueva pieza) | — | Acceso 1 · 0 pt · 1 Ll | Daño 2 · Esq: Nula · Abs: Total |
| Arma de área | Acceso 2 · 0 pt · 0 Ll | Acceso 2 · 2 pt · 0 Ll | — |
| Arma inevitable | Acceso 3 · 0 pt · 1 Ll | Acceso 3 · 0 pt · 2 Ll | — |
| Arma que abre la armadura | Acceso 2 · 0 pt · 0 Ll | Acceso 2 · 0 pt · 1 Ll | — |
| Arma aturdidora | Acceso 1 · 0 pt · 0 Ll | Acceso 1 · 0 pt · 1 Ll | — |
| Arma de asedio | Acceso 3 · 0 pt · 1 Ll | Acceso 3 · 0 pt · 2 Ll | — |
| La bomba de los mil soles | Acceso 3 · 0 pt · 9 Ll | Acceso 3 · 0 pt · 0 Ll | — |
| La luna que no era una luna | Acceso — · 0 pt · 16 Ll | Acceso — · 0 pt · 9 Ll | — |
| La lanza que cae del cielo | Acceso 3 · 0 pt · 9 Ll | Acceso 3 · 0 pt · 6 Ll | — |
| La lista | Acceso 2 · 0 pt · 4 Ll | Acceso 2 · 0 pt · 3 Ll | — |
| Lo que viste de verdad | Acceso — · 0 pt · 4 Ll | Acceso — · 0 pt · 3 Ll | — |
| Arma silenciosa | Acceso 2 · 0 pt · 0 Ll | Acceso 2 · 0 pt · 1 Ll | — |
| Ropa reforzada | Acceso 0 · 0 pt · 0 Ll | Acceso 0 · 1 pt · 0 Ll | — |
| Blindaje de combate | Acceso 3 · 2 pt · 0 Ll | Acceso 3 · 3 pt · 0 Ll | — |
| Cobertura portátil | Acceso 1 · 0 pt · 0 Ll | Acceso 1 · 1 pt · 0 Ll | — |
| Yelmo | Acceso 0 · 0 pt · 0 Ll | Acceso 0 · 1 pt · 0 Ll | — |
| Vehículo de combate | Acceso 3 · 0 pt · 1 Ll | Acceso 3 · 2 pt · 1 Ll | — |
| Vehículo de rescate | Acceso 1 · 0 pt · 0 Ll | Acceso 1 · 0 pt · 1 Ll | — |
| Velo absoluto | Acceso — · 0 pt · 8 Ll | Acceso — · 0 pt · 4 Ll | — |
| Fuerza de sala | Acceso — · 0 pt · 5 Ll | Acceso — · 0 pt · 4 Ll | — |
| Fuerza de edificio | Acceso — · 0 pt · 20 Ll | Acceso — · 0 pt · 16 Ll | — |
| Descarga | Acceso 0 · 0 pt · 1 Ll | Acceso 0 · 1 pt · 1 Ll | — |
| Mando de multitud | Acceso — · 0 pt · 2 Ll | Acceso — · 0 pt · 1 Ll | — |
