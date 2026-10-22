# La App al día con el Juego completo v2 (22 oct)

Compilado con `python -I src/build_app3.py` → `src/out3/nogum_app.html`, `docs/app.html`, `NOGUM_app/NOGUM_app.html` (650 KB). Sin commit.

## Comprobación
- `node --check` sobre el script embebido de los tres ficheros: se parsea. Los dos blobs JSON (datos y canon) se cargan.
- Abierta en el navegador (servidor estático `localhost:8777`), sin un solo error de consola, recorriendo: Código con la regla 17 y experiencia negativa (`…-B10003-…-PN2-K3`, ida y vuelta idéntica), Código viejo de 16 bits (`B8001`, se lee igual y se reescribe igual), Baúl, ficha plantilla y ficha de personaje, Llaves (entera, Limitada y de un momento con la escalera llana: 7, 4 y 0 a +3), equipo desde el desplegable y desde el formulario 4, dados (por encima de +4 y por debajo), reparto (decorado), Preguntas sin IA, Historia, Sesiones, inglés y Acelerado. También la migración de una ficha guardada con el catálogo viejo. Al acabar, el localStorage del navegador quedó como estaba.

## 1. `extract_app_data.py` lee la v2
- **Bazar**: de `v2/fK1_bazar_a` + `fK2_bazar_b` + `fK3_bazar_c` (y sus `.en.html`). Tablas de **8 columnas**; cada objeto lleva `m` (Acceso), `p` (Puntos) y `k` (Llaves), en los dos idiomas, y se comprueba que las tres cifras coinciden entre castellano e inglés. Se saltan `bz-lectura`, `bz-fabrica`, `bz-casos`, `bz-precios`, `bz-resumen` y `bz-indice`. La categoría (arma, defensa, vehículo, artefacto, útil) se calcula sin «La cuenta:» de la nota, que nombra armaduras y escudos que el objeto no tiene. 372 objetos (antes 371: se añadió «Arma de fuego» en Piezas sueltas).
- **Baúl**: de `v2/fJ1_cap9a` (`ch9-baul` → `ch9-tablas`), **17 reglas**. La lista va en **orden de bit del Código**, no en el del manual: las 16 de siempre en su sitio y la escalera llana la 17 (bit 16). Así un Código viejo no cambia de significado. Se comprueban los nombres.
- **`baulLong` ya no se arrastra**: se regenera del texto v2 de cada módulo (ES/EN). La App no lo usa hoy.
- **Recetas y nivel máximo de los jugadores**: de `v2/fJ2_cap9b` (20; los techos se comprueban iguales en los dos idiomas). Han cambiado casi todos los Social a 1.
- La lista de **vocabulario retirado** que caza el extractor añade «Llave ancha/estrecha», «Wide Key», «DJ», «Malla Tonal», «2·x²», «como mucho».

## 2. El Código: 17 bits, compatible hacia atrás
- `B` sigue en cuatro cifras hex si la regla 17 está apagada (Código idéntico al de siempre); pasa a cinco solo si está encendida. Al leer se aceptan las dos. Una app vieja que lea uno nuevo ignora el bit 16.
- La experiencia de salida puede ser negativa (C·e4): viaja como `P` / `K` con `N` delante (`PN2` = dos puntos menos). Una app vieja lo lee como 0.
- `build_app3.py`: la aserción pasa a 17 y comprueba `var BAUL_BITS = 17;` en la App.
- La escalera llana (regla 17) entra en el grupo «Riesgo y poder» y en las recomendaciones del formulario 3. Encendida, el precio de las Llaves es 3n−2 en vez de n² (también en la Limitada y en el reescalado de la Parca).
- Equipo guardado: el Bazar v2 corrió una fila en Piezas sueltas; las fichas y los archivos de mesa viejos se migran solos (`bzv`).

## 3. La interfaz al canon (ES y EN)
- **Llaves en la ficha**: fuera «Estrecha / Ancha / Contra todo (el doble)». Ahora: **Entera** (toda la Disciplina, contra todo, n²), **Limitada** (contra una sola cosa o solo el daño, la mitad al alza, mínimo 1; aviso de que a un nivel cuesta igual y no se recomienda limitarla) y **Prestada o de un momento** (una escena, no se paga, se tacha). Una Llave vieja «ancha» se lee como de un momento.
- **Recordatorios** reescritos: tirada (pifia y crítico en el número que usas, «tira solo si fallar es interesante»); bonos que se acumulan a criterio de mesa, por encima de +4 se tira con +4, por debajo de −2 decide el Director; salida 12/14 + bote (5 Llaves o +1 Rejilla), 1·1·1·1·2 **recomendado**, experiencia que da más o menos; Rejilla (sin tirada, se narra la derrota), las dos lecturas, Rejilla vs Llave, nivel máximo de los jugadores; tres cerrojos, el daño no se paga, lo de un uso no se paga, Limitado si hay que reponer, mínimo 1; **una Llave por sesión y por cabeza**; iniciativa completa; defensa con pifia (+1, +2 con crítico); la Parca sin «nunca mata»; decorado sin ficha ni tirada; vida y muerte pactada (0.7).
- **14 puntos para todos** si algún jugador lleva Arcano (antes, solo el que lo tenía). La casilla «Tiene Arcano» decide quién toca el ámbito, no los puntos.
- **Sin Arcano no hay barra Espiritual** (6.5): la ficha ya no la dibuja.
- **Dados**: el «el DJ puede narrarlo sin tirar» de por encima de +4 cambia por «se tira con +4…»; nuevo aviso por debajo de −2; «Éxito parcial» → **Éxito con coste** (solo Pulp desenfrenado y Comedia negra); pifia en defensa según 6.2.
- **El reparto**: el **decorado** no tiene nivel (n−1, no se pregunta) ni tirada; desaparece «son hormigas o dioses»: lo que está muy por encima no es decorado.
- **Equipo**: precios de las columnas nuevas (`Acceso · puntos · Llaves` en la ficha, el buscador y la cuenta). La Parca reescala su precio con la Rejilla del portador como Llave Limitada al daño (9.3). **Acelerado**: el equipo solo cuesta dinero, sin puntos ni Llaves, y **tres objetos** (aviso si hay más), como dice su 2.9.
- «DJ» → Director en todo; «don»/dones no aparecía como aspecto (Don es el Dominio de Arcano y se queda); techos → «nivel máximo de los jugadores» en la ficha; Transformación, Sincronización, Daño ambiental, Vínculos, Menú de costes, Pacto y Director en oculto, al texto v2; «Baúl de reglas (8.1)» → 9.1; textos «16» → 17.
- Arreglos que salieron al probar: el botón «¿No sabes cuáles? Recomiéndame» llevaba a un formulario que ya no existe (ahora abre el del Baúl); la lectura de la IA de los formularios rompía con `q.a` indefinido (ahora dice la opción elegida); el aviso de presupuesto del equipo comparaba con el de la plantilla.

## 4. Enlaces y apartados
- La App no tenía enlaces a `juego.html`, solo números citados. Ahora los «(N.M)» de los recordatorios, las Llaves, el reparto, los dados y la barra de la mesa son **enlaces** a `juego.html#id` (local, web o artefacto, según el destino; en inglés con `?lang=en` salvo en claude.ai). Tabla `SECC` con 38 apartados; cada id comprobado en `src/v2/f*.html` (y presente ya en `docs/juego.html`). El 2.9 del Acelerado no se enlaza.
- Números puestos al día: 2.4 → 3.6 (niveles de la historia) y 3.1 (¿Rejilla o Llave?), 4.3 → 9.3 (precio según tu Rejilla), 8.1 → 9.1, cap. 8 → 9, cajones de Recursos 8.3 → 5.6, y los comentarios del código.

## 5. El asistente de reglas
- `build_app3.py` ya no le pasa CANON.md entero: le pasa la PALABRA DEL AUTOR (hasta «Jerarquía de autoridad»; lo de debajo es historia con capas viejas, y traía «Malla Tonal» y nombres con copyright) más el texto de la hoja de referencia v2 (`fL_referencia.html`). El prompt le dice que manda la palabra del autor, que «malla» es la Rejilla y que use el vocabulario vigente.

## Lo que no he podido resolver (dudas)
- **Escalera llana y Rejilla**: la regla del Baúl dice «subir n niveles con Llaves», así que en la App solo cambia el precio de las Llaves; la Rejilla sigue en 5·n². El autor escribió «Rejillas menos inaccesibles»: si quería también 5·(3n−2) para la Rejilla, es una línea (`gridCost`).
- **Escala de la partida**: la App sigue preguntando «de qué tamaño son las hazañas» (Rejilla 1–5 de la mesa). En el manual v2 no hay ese concepto con ese nombre (están los tres techos); la App lo presenta como tamaño de las amenazas, que no sube a los personajes. Se podría renombrar o quitar.
- **Precio del equipo con nivel para un portador que no es de nivel 1**: la Parca va exacta; los vehículos y la Sincronización se escalan en proporción, que es una aproximación.
- El Acelerado se ha alineado con `frag_acelerado.html` tal como está en el árbol de trabajo (equipo solo con dinero, tres objetos).
- Los enlaces al Juego funcionarán donde el `juego.html` publicado ya sea el v2 (`docs/` sí; `NOGUM_productos/NOGUM_juego.html` todavía no tiene los ids nuevos hasta que se monte).
