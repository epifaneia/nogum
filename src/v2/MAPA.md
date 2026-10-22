# NOGUM v2 · Mapa de la reestructura (para los agentes)

Estás reescribiendo un trozo del **Juego completo** de NOGUM (castellano) con una estructura nueva. El libro viejo NO se toca: todo lo nuevo se escribe en `C:\Users\Daniel Martin\Desktop\NOGUM\src\v2\`. Después se monta en un HTML local para compararlo con el viejo.

## 0. Lo que tienes que leer antes de nada

1. `src/CANON.md`, **líneas 1–215**: la PALABRA DEL AUTOR. Es la única verdad. Lo marcado «Sí» está confirmado; en lo marcado «No» manda solo el texto del autor. Las «Aclaraciones del 22 oct» (desde la línea 138) también son palabra del autor, e incluyen las dos tablas de ejemplos de la Rejilla ya aprobadas. Nada de CANON.md por debajo de la línea 215 vale como verdad (es historia, con capas viejas y erróneas).
2. `REVISION-canon-2026-10-21.md` (raíz): el barrido de contradicciones del libro viejo, con fichero:línea. **Toda corrección que afecte a tus fuentes hay que aplicarla.** Ojo: algunas «dudas» de ese informe ya las ha contestado el autor en las Aclaraciones; manda la Aclaración.
3. `PLAN-reestructura.md` (raíz): el principio y el índice.
4. Este fichero entero, y tu sección de reparto.
5. Tus fuentes viejas, enteras (rutas en `src/`).

## 1. El principio (palabras del autor)

«De lo más general, epifanías, descripciones genéricas cuanto antes, y los detalles que sientan que salen de manera natural de aplicar los principios generales. El manual entero debe estar escrito así.»

- Cada capítulo abre con su idea en una o dos frases claras (la epifanía), luego la descripción general, luego los detalles como consecuencia.
- **Cada concepto tiene un solo sitio** (ver §4). Si tu capítulo necesita un concepto que vive en otro, lo nombras en una frase y enlazas (`<a href="#id">N.M</a>`). No lo vuelves a explicar.
- **No dejes nada fuera.** «Cuanto más mejor»: reaprovecha todo el texto viejo que puedas (ejemplos, asides, tablas, bromas, figuras), corregido. Solo se cae lo que contradice al canon o lo que ahora vive en otro capítulo (y entonces se enlaza). Todo lo que tires lo apuntas en tu registro (§6).
- **No inventes reglas.** Si el canon no zanja un caso y el texto viejo es compatible, se queda. Si no es compatible y no sabes, no lo resuelvas tú: déjalo como está lo más neutro posible y apúntalo como duda en el registro.

## 2. La voz (preferencias del autor)

- Frases cortas y llanas. Nunca condescendiente ni sermoneador («¿te parece justo que…?», nunca «¿entiendes que…?»). No enturbiar la epifanía con matemáticas: los números van detrás, o en el apéndice.
- **Manual universal: nada de absolutos.** Evita «nunca», «siempre», «como mucho», «en ningún caso», «fuera de la Rejilla». Usa «generalmente», «en la mayoría de mesas», «no se recomienda». La muerte y el nivel cósmico son «casi siempre», no «nunca». Tampoco hay que repetir las excepciones en cada párrafo.
- **Nada de nombres con copyright ni personas reales**: arquetipos («el trepamuros», «el alien de mallas y calzoncillos», «el consultor de Baker Street»). Los mitos y el folclore (Orfeo) valen.
- Texto principal serio; la columna lateral `<aside class="meta">` es la voz informal (bromas, referencias). Consérvalas.
- El nombre es **Rejilla** (en inglés Grid). Si el autor escribe «malla», es la Rejilla. «Llave ancha», «Llave pequeña», «la Vela» y el «Desenredando» desaparecen.

## 3. Marcado

Copia las convenciones de los `frag_*.html` viejos. Lo esencial:

```html
<section class="chapter" id="ch3">
<h2>Capítulo 3 · Lo que eres (la Rejilla)</h2>
<p class="lede">…</p>
<h3 id="ch3-nivel">3.1 Qué significa un nivel</h3>
<h4 id="ch3-…">…</h4>
<div class="rule" id="…"><p class="rule-title">…</p>…</div>   <!-- recuadro de regla -->
<aside class="meta"><p>…</p></aside>                          <!-- columna informal -->
<div class="tw"><table class="t"><thead>…</thead><tbody>…</tbody></table></div>
<span class="src">T183</span>                                  <!-- marca de origen -->
</section>
```

- Los números de los títulos los colorea el montaje solo: escribe `Capítulo 3 · …` y `3.1 …` en texto plano.
- **Marcas de origen**: conserva las `<span class="src">T…</span>` del texto que reaproveches. Lo que salga del canon nuevo lleva `<span class="src">C·l2</span>` (el id del concepto) o `<span class="src">C·22oct</span>` (las Aclaraciones). Las banderas `flag ed / drop / pending / proposal` de los viejos se pueden conservar o quitar (el montaje las borra del manual).
- **Ids**: usa exactamente los ids de §4 para los h2/h3 que te tocan. Los h4 y recuadros, con el prefijo de tu capítulo (`ch3-…`). No repitas ids que existan en otro capítulo.
- **Enlaces internos**: `href="#id"` con los ids de §4. Reescribe todas las referencias viejas («ver 2.3», `href="#ch2-llave"`, «(3.5)») a la numeración y los ids nuevos.
- Al final de cada capítulo de reglas (2 a 7), un `<h3 id="chN-aclaraciones">N.x Aclaraciones</h3>` con las zonas que ha costado delimitar, como casos cortos (`<p><strong>¿Pregunta?</strong> Respuesta.</p>`). **Regla: una aclaración solo aplica un principio del capítulo; si un caso necesita una regla nueva, la regla va en el cuerpo.**

## 4. El índice nuevo, con ids (para enlazar)

| Sitio | id | Qué vive aquí (canon) |
|---|---|---|
| Portada / Cómo leer | `portada`, `como-leer` | (lo monta el coordinador) |
| Introducción | `intro` (h3 `intro-tiendas`, `intro-nogum`, `intro-manual`) | la tesis |
| Las seis ideas | `ideas` | las ideas madre, una por capítulo 0–5 |
| Capítulo 0 · La mesa manda | `ch0` | m1, m2, m3, m4 |
| 0.1 Las líneas rojas | `ch0-lineas` | m2 |
| 0.2 Qué vamos a sentir | `ch0-sentir` | |
| 0.3 Quién propone | `ch0-quien` | |
| 0.4 «Esto no vale» | `ch0-novale` | m1 (combo barato = abuso de reglas, se pacta en la 0) |
| 0.5 Volver a la sesión 0 | `ch0-volver` | |
| 0.6 Tira solo si fallar es interesante | `ch0-tirar` | m4 (y a2: nunca por ser numéricamente trivial) |
| 0.7 La muerte se pacta | `ch0-muerte` | m3 (el único sitio donde se habla de la muerte) |
| 0.8 Y de ahí salen los números | `ch0-numeros` | |
| Capítulo 1 · El tono | `ch1` | t1–t6 |
| 1.1 Los dos ejes | `ch1-ejes` | |
| 1.2 El cuadrante | `ch1-malla` | t2 |
| 1.3 La tirada | `ch1-tirada` | t1, t3, t4, t5 (descripción general: dos d10, TN 6/11, dificultad como modificador, pifias y críticos en el número que usas, éxito con coste) + presentación de la Sala de Máquinas con enlace a `apx-maquinas` |
| 1.4 Las tarjetas de tono | sección `ch1-panel` (h3 `ch1-panel-cuadrante`) | las siete tarjetas |
| 1.5 El tono se mueve | `ch1-mueve` | t6 (lo general; el cómo, en el cap. 8) |
| Capítulo 2 · Lo que sabes (el Ancla) | `ch2` | a1–a4 |
| 2.1 El Ancla: de −2 a +4 | `ch2-ancla` | a1 |
| 2.2 La pirámide | `ch2-piramide` (h4 `ch2-nulidad`) | a3, a4 |
| 2.3 La lista cerrada | `ch2-lista` | |
| 2.4 Las Firmas | `ch2-firmas` | Firma +4 |
| 2.5 Los bonos se acumulan | `ch2-bonos` | a2, t3 (dificultad), modificadores, por encima de +4 / por debajo de −2, «acumular lo que se pueda, a criterio de mesa» |
| 2.6 Aclaraciones | `ch2-aclaraciones` | |
| Capítulo 3 · Lo que eres (la Rejilla) | `ch3` | r1–r9 |
| 3.1 Qué significa un nivel | `ch3-nivel` | r1, r7 (¿Rejilla o Llave? con sus dos caras) |
| 3.2 Las dos lecturas | `ch3-lecturas` | r2, r3 (narrativa; tangible ×100, «dos ceros», tabla de escenarios) |
| 3.3 La Rejilla en ejemplos | `ch3-ejemplos` | **Tabla 1 aprobada** (CANON.md, Aclaraciones) |
| 3.4 Por ámbitos | `ch3-ambitos` | r4, «los unos abundan», ser no es saber, el zoom |
| 3.5 El Estilo | `ch3-estilo` | a6 (cuando ya no se puede fallar) |
| 3.6 Quién la sube | `ch3-subir` | r8 |
| 3.7 Los techos | `ch3-techos` | r6 (nivel máximo inicial / del mundo / de los jugadores; no se aplica a las Llaves); lo cósmico (22 oct) |
| 3.8 Sincronización | `ch3-sincro` | r9 |
| 3.9 Aclaraciones | `ch3-aclaraciones` | |
| Capítulo 4 · A quién afectas (la Llave) | `ch4` | r10, l1–l10 |
| 4.1 Qué es una Llave | `ch4-llave` | l1, l2, l3 (toda una Disciplina, contra cualquier objetivo; te pone n niveles por encima) |
| 4.2 Anula lo que dice que anula | `ch4-anula` | l2 (la granada), r10 (con permiso, bono completo; no se protege dos veces), 22 oct (Esquiva, Absorción, Daño) |
| 4.3 Subir más de un nivel | `ch4-escalera` | l4 (n²; Limitada; a un nivel no se separa) |
| 4.4 Propia, prestada, de un momento | `ch4-tipos` | l5, l6, l7 (en blanco; el abuso lo frena la mesa); Presencia Majestuosa como ejemplo de lo abiertas que son |
| 4.5 La Parca | `ch4-parca` | l8 + 22 oct (es una Llave; fuera de combate sin derecho a tirada; sin hablar de muerte) |
| 4.6 Los permisos | `ch4-permisos` | l9 |
| 4.7 Los hechizos | `ch4-hechizos` | l10 |
| 4.8 Llaves en ejemplos | `ch4-ejemplos` | **Tabla 2 aprobada** |
| 4.9 Aclaraciones | `ch4-aclaraciones` | |
| Capítulo 5 · Lo que cuesta (la cuenta) | `ch5` | a5, e1–e8 |
| 5.1 Dos monederos | `ch5-monederos` | e3 (una Llave por sesión y por cabeza) |
| 5.2 Con qué se empieza | `ch5-salida` | a5 (12/14 + 5 Llaves o un nivel; los 14, para todos si alguien juega Arcano), e1 (bote aparte), r5 (1·1·1·1·2 recomendado), e4 (experiencia de salida, también negativa) |
| 5.3 La unidad de cambio | `ch5-cambio` | e2 (5·n² / 8·n²) |
| 5.4 La cuenta | `ch5-cuenta` | e7, e8, l9: bono → puntos; lo que es de Llave → Llaves; el daño no se paga; afectar al nivel siguiente (la Parca) es Llave; lo de un uso o una escena no se paga; mínimo 1; lo que no se gasta nunca es permanente; Limitado si hay que reponer |
| 5.5 El Ajuste | `ch5-ajuste` | ÷2 · ×1 · ×2 · ×3, vago a propósito |
| 5.6 El equipo | `ch5-equipo` | e5 (Acceso, permiso narrativo, coste en los dos monederos), e8 (la pistola paga Llave; blásters esquivables por convenio del género), Recursos y Acceso |
| 5.7 Devolver, prestar, regalar | `ch5-devolver` | e6 |
| 5.8 Progresión | `ch5-progreso` | e3, dones y lacras |
| 5.9 Aclaraciones | `ch5-aclaraciones` | |
| Capítulo 6 · El peligro | `ch6` | c1–c6 |
| 6.1 Iniciativa | `ch6-iniciativa` | c4 |
| 6.2 La secuencia de ataque | `ch6-golpes` (recuadro `ch6-monstruo`) | c1 |
| 6.3 Arsenal: la ficha técnica | `ch6-armas` | c2, c3 (las etiquetas aplican «anula lo que dice»; la Parca vive en 4.5) |
| 6.4 La vida fractal | `ch6-vida` | c5 |
| 6.5 Sistemas de daño | `ch6-dano` | c6 |
| 6.6 Catálogo de consecuencias | `ch6-consecuencias` | |
| 6.7 Aclaraciones | `ch6-aclaraciones` | |
| Capítulo 7 · Las fichas | `ch7` | c7 + creación de personajes |
| 7.1 Cuatro fichas | `ch7-tipos` | de la más principal a la más desechable |
| 7.2 La ficha del protagonista, paso a paso | `ch7-protagonista` | aplica los caps. 2–5; aspectos; ejemplo resuelto con Inés |
| 7.3 Fichas completas | `ch7-completa` | |
| 7.4 Fichas rápidas | `ch7-rapida` | +0 fuera de su ámbito, «Rejilla 1–5»: se quedan (22 oct) |
| 7.5 Fichas de decorado | `ch7-decorado` | |
| 7.6 Aclaraciones | `ch7-aclaraciones` | |
| Capítulo 8 · La consola de mezclas | `ch8` | consejos de tono |
| 8.1–8.4 | `ch8-diagnostico`, `ch8-defecto`, `ch8-velocidades`, `ch8-disonancia` | |
| Preguntas frecuentes | `apx-faq` | |
| Capítulo 9 · La caja de herramientas | `ch9` | |
| 9.1 Baúl de reglas | `ch9-baul` | |
| Tablas de problemas | `ch9-tablas` | |
| 9.2 Listado de competencias | `ch9-skills` | |
| 9.3 El Bazar del Multiverso | sección `apx-bazar` (h3 `bz-…` como los viejos) | |
| 9.4 Simulación de manuales | sección `ch9b` (h3 `ch9-recetas`, `ch9-fichas`) | recetas, Piedra Rosetta, expedientes |
| Glosario | `apx-glosario` | |
| Apéndice A · La Sala de Máquinas | `apx-maquinas` (h3 `maq-…` como los viejos) | |
| Apéndice B · Tablas completas | `apx-mates` (h3 `apxd-…` como los viejos) | |

## 5. El reparto (qué fuente va a dónde y quién lo escribe)

Fuentes en `src/`. Los números son líneas del fichero viejo.

**A · Ideas, Introducción, cap. 0, cap. 1** → `v2/fA_ideas_intro_0_1.html`
- `frag_intro.html` entero → Introducción (corrige intro:29).
- Nueva sección `ideas` «Las seis ideas», justo después de la Introducción: una idea por capítulo 0–5 (la mesa manda / el tono es la física / el Ancla: lo que sabes / la Rejilla: lo que eres / la Llave: a quién afectas / una sola cuenta), cada una en 2–4 frases, con su enlace. Sustituye al recuadro «Siete ideas» (`frag_ch2.html` 5–19) y a los dos párrafos de entrada del cap. 2 viejo (1–4): reaprovecha lo que valga.
- `frag_ch0.html` entero → cap. 0 (0.1–0.5, 0.8). Escribe 0.6 y 0.7 nuevos desde el canon (m3, m4, a2), reaprovechando los pilares de la Introducción y las frases sobre la muerte que haya en `frag_ch5.html` (124–132) y `frag_acelerado.html` (277–283): cópialas aquí, no las borres de allí (lo hará quien tenga ese capítulo).
- `frag_ch1a.html` entero → 1.1, 1.2.
- 1.3 La tirada: nueva, general y corta, con lo esencial de `frag_math.html` E (16–121, solo lo que el jugador necesita, sin estadística) y F (122–123), y de «Cómo se lee cualquier tarjeta» (`frag_ch1b.html` ~1–12). Acaba presentando la Sala de Máquinas en un párrafo con enlace a `apx-maquinas`.
- `frag_ch1b.html` entero → sección `ch1-panel` (1.4). Corrige ch1b:9 y 21. La Tragedia (ch1b:82) se queda como **excepción declarada** (22 oct).
- 1.5 El tono se mueve: corto, desde el canon t6, enlazando al cap. 8 para el cómo.

**B · Apéndices de matemáticas** → `v2/fB_apendices.html`
- `frag_math.html` 1–825 (sección `ch1-maquinas`) → sección `apx-maquinas`, «Apéndice A · La Sala de Máquinas». Se mueve casi entero. Corrige math:123, 131, 137, 782, 798, 802–807, 820, 823 (la Llave por sesión es por cabeza).
- `frag_math.html` 826–1021 (`apx-mates`) → «Apéndice B · Tablas completas». La Tragedia, excepción declarada.
- Copia los bloques grandes por script (Python leyendo líneas) y corrige después con Edit: hay SVG y tablas que no se deben reescribir a mano.

**C · Capítulo 2 · Lo que sabes** → `v2/fC_cap2.html`
- `frag_ch2.html` 20–33 (2.1 viejo) → 2.1. Corrige ch2:30 («el +4 es tu ancla» → el ancla es el rango de todas las fichas).
- `frag_ch3.html` 10–44 (pirámide y Nulidad) → 2.2; 45–69 (lista cerrada) → 2.3; 70–101 (Firmas) → 2.4.
- `frag_ch4.html` 1–43 y 79–86 (la tirada, dificultad, habilidad, modificadores) → 2.5. Corrige ch4:8, 25, 26 (no se narra el éxito: se tira con +4), 27 (fuera la regla de «no hay combos»: se acumula lo que se pueda, a criterio de mesa, con el ancla en +4), 41 («casi infalible»).
- `frag_ch2.html` 242–247 (2.5 viejo, «la Vela») → **se retira** («nunca me gustó»); si hay algo útil del Ancla, a 2.1.

**D · Capítulo 3 · Lo que eres** → `v2/fD_cap3.html`
- `frag_ch2.html` 34–99 (2.2 viejo) → 3.1 y 3.2. Reescribe 3.1 con la voz del autor en r1 (el porqué: cuando el combate contra cierto nivel ya no interesa, se resume con un nivel de distancia, más probablemente subiendo a los jugadores que bajando al enemigo; el débil pierde el permiso de intentarlo, salvo que la narrativa le dé una Llave) y r7 (dos caras). Tabla de escenarios (54–63) y «dos ceros» (72–80) → 3.2, con r3 (la narrativa puede tener su escala; la tangible: el ×100 es la mejor elección y no se recomienda cambiarlo, con el ejemplo del boxeador y la turba de cien adolescentes / diez: «el quizás estorba»). Nivel 6: lo cósmico es nivel planetas, casi siempre injugable, no un absoluto. La pistola sale de la fila N1 de la tabla de escenarios (paga Llave) y la granada queda como Llave de N2.
- La tabla de ejemplos vieja (89–97) → sustituida por la **Tabla 1** aprobada (3.3), con la nota «con un poco de imaginación, todo puede ser un personaje», y un enlace a la Tabla 2 (4.8).
- `frag_ch2.html` 186–241 (2.4 viejo): zoom, «¿Rejilla o Llave?» (→ 3.1), ejemplo del hacker, «Ser no es saber», «Los unos abundan» (se quedan, 22 oct) → 3.4; «Sincronización» → 3.8; «Subir de nivel», «La Rejilla cambia el universo» → 3.6; «El techo del mundo» → 3.7 (con los tres techos); «¿Qué nivel tienen al empezar?» y «El bote puede darte un 2» → **no**: son del cap. 5 (los escribe F); aquí solo una frase y enlace a 5.2.
- `frag_ch4.html` 87–130 (4.5 viejo, Rejilla y Estilo), la parte de Estilo de `frag_ch3.html` 102–111, y la de `frag_ch67.html` 15–17 → 3.5 El Estilo (la de las fichas de decorado se queda también en 7.5, en una frase con enlace).
- `frag_cap8.html` entrada «Sincronización» del Baúl → 3.8 (fúndela con la del cap. 2 viejo).
- `frag_ch2.html` 248–323 (2.6 viejo, «Desenredando»): sus apartados «Qué es un nivel de Rejilla» y «La Rejilla» → 3.9 Aclaraciones.

**E · Capítulo 4 · A quién afectas** → `v2/fE_cap4.html`
- `frag_ch2.html` 100–145 (2.3 viejo, tabla «subir contra la misma cosa» incluida, corregida: n² es el precio completo, contra todo) → 4.1–4.3. `frag_ch2.html` 159–185 («La Llave de principio a fin», «Llave propia y Llave prestada») → 4.4. «Prestar y traspasar» → **no**: es de 5.7 (F).
- `frag_ch5.html` 122–132 («La Parca: lo que no es un arma») y lo de la Parca en `frag_ch4.html` 44–78 → 4.5 (sin hablar de la muerte; en el cap. 6 queda un enlace).
- `frag_ch3.html` 102–111, la parte de magia → 4.7 Los hechizos (l10: el punto en Arcano es requisito; el hechizo es un permiso, se paga con Llaves).
- Permisos (l9): de `frag_ch3.html` 179–195 (la cuenta de los permisos) solo lo que define qué es un permiso → 4.6; el precio lo explica 5.4 (enlaza).
- **Tabla 2** aprobada → 4.8.
- `frag_ch2.html` 248–323 («Desenredando»): apartado «La Llave» y la parte de la Parca de «El equipo y la Parca» → 4.9 Aclaraciones. Presencia Majestuosa como ejemplo.

**F · Capítulo 5 · Lo que cuesta** → `v2/fF_cap5.html`
- `frag_ch2.html` 146–158 (unidad de cambio; la tabla de 8 Disciplinas = 8·n² es la buena) → 5.3; la «Idea 5» de 311 (2·x²) se cae.
- `frag_ch2.html` 225–235 parte de la salida («¿Qué nivel tienen los personajes al empezar?», «El bote puede darte un 2») → 5.2.
- `frag_ch3.html` 112–178 (economía de la escasez, Caso A con Llaves completas, no estrechas) → 5.2; 179–195 (Ajuste) → 5.4 y 5.5; 196–275 (progresión, dones y lacras) → 5.8.
- `frag_ch4.html` 44–78 (equipo, tres cerrojos, sin la Parca) → 5.6 y 5.4.
- `frag_ch2.html` 159–185 «Prestar y traspasar» → 5.7.
- `frag_bazar.html` 1–146 (`bz-lectura`, `bz-fabrica`: la cuenta, el Ajuste, tres monedas, cuatro categorías, los seis cajones de Recursos) → la teoría del precio pasa a 5.4–5.6. En el Bazar se queda solo cómo leer la ficha técnica del catálogo y un taller corto que remite a 5.4 (eso lo escribe K1).
- `frag_ch2.html` 248–323 («Desenredando»): «Puntos, Llaves y limitaciones» y la parte de equipo de «El equipo y la Parca» → 5.9 Aclaraciones.

**G · Capítulo 7 · Las fichas** → `v2/fG_cap7.html`
- `frag_ch67.html` 1–32 (cap. 6 viejo) → 7.1, 7.3, 7.4, 7.5 (reordenado: protagonista, completa, rápida, decorado). Corrige ch67:10.
- `frag_ch3.html` 1–9 (entrada del cap. 3 viejo) y la parte de aspectos de 102–111 → 7.2.
- 7.2 La ficha del protagonista, paso a paso: un procedimiento corto que aplica, en orden, los caps. 2–5 (con enlaces, sin reexplicar), y un **ejemplo resuelto construyendo a Inés desde cero**, a partir de su expediente (`frag_cap8.html` 934–1008). El expediente sigue en 9.4; aquí se cuenta cómo se hizo.

**H · Preguntas frecuentes y Glosario** → `v2/fH_faq_glosario.html`
- Sección `apx-faq` «Preguntas frecuentes»: las dudas transversales que más ha costado delimitar (las de `frag_ch2.html` 248–323, las Aclaraciones del 22 oct en CANON.md, y las del informe REVISION). Respuesta corta y enlace al sitio que la explica. No repite los capítulos: remite.
- `frag_glosario.html` → `apx-glosario`, con todas las definiciones según el canon y enlaces a los ids nuevos. Quita la nota de «malla es errata» o déjala en una frase sin tono de corrección.

**I · Capítulo 6 · El peligro y Capítulo 8 · La consola** → `v2/fI_cap6_cap8.html`
- `frag_ch5.html` entero → cap. 6, salvo la Parca (122–132, ahora en 4.5: deja una frase y enlace) y la muerte (va a 0.7: deja enlace). Corrige ch5:29 (anula lo que dice que anula), 85, 100, 108, 119, 126.
- `frag_ch67.html` 33–115 (cap. 7 viejo) → cap. 8. Corrige ch67:52.

**J1 · Capítulo 9, primera parte** → `v2/fJ1_cap9a.html`
- `frag_cap8.html` 1–677 (entrada del cap., Baúl, Tablas de problemas, Listado de competencias) → `ch9`, 9.1, Tablas, 9.2. La entrada «Sincronización» del Baúl se va a 3.8: deja una línea y enlace. Corrige cap8:3, 66, 138 (Transformación: n² contra todo), 149, 318.

**J2 · Capítulo 9, segunda parte** → `v2/fJ2_cap9b.html`
- `frag_cap8.html` 678–1008 (menú degustación, recetas, crítica, títulos, Piedra Rosetta, expedientes) → sección `ch9b` «9.4 Simulación de manuales». Corrige cap8:763, 801 (el catedrático: Llaves, no Social 2), 811, 819, 896 (Social a 4 → Llaves, 22 oct), 926, 959–968 (las Llaves de Inés y de la vampira, Disciplinas completas). Los techos de las recetas, con los nombres nuevos (3.7).

**K1 · Bazar, primera parte** → `v2/fK1_bazar_a.html`
- `frag_bazar.html` 1–480: entrada, `bz-lectura` (solo cómo leer la ficha técnica), `bz-fabrica` (corto, remite a 5.4–5.6), y los catálogos 1–7 (fantasía a gótico).
**K2 · Bazar, segunda parte** → `v2/fK2_bazar_b.html`
- `frag_bazar.html` 481–727: catálogos 8–10, Duelo Social, piezas sueltas.
**K3 · Bazar, resumen e índice** (va después de K1 y K2) → `v2/fK3_bazar_c.html`
- `frag_bazar.html` 728–1146: resumen e índice, alineados con los precios que hayan quedado en K1 y K2.

Para K1–K3 (los patrones de REVISION, «B · El Bazar»): Daño máximo 2 + la Parca (fuera Daño 3 y Masivo/Absoluto/Infinito: son Parca con su nivel); dificultar esquiva o absorción, +2 al dar, mira automática → **puntos**; Esq Nula o la Parca o un nivel de Rejilla → **Llave**; las pistolas y armas de fuego normales son inesquivables a nivel 1 → Llave; los blásters de ópera espacial, esquivables por convenio del género; los permisos permanentes cuestan al menos 1 Llave aunque el Acceso sea 0; lo de un solo uso no se paga (granadas, elixires: si es de un uso, gratis; si nunca se acaba, permanente; si hay que reponer, Limitado). Presencia Majestuosa se queda. Las fichas del catálogo llevan **Acceso · Puntos · Llaves** como columnas de coste donde haga falta.

## 6. Tu registro

Además de tu fragmento, escribe `v2/registro_<letra>.md` con:
1. **De dónde sale cada parte**: cada rango viejo que has usado (fichero:líneas) → dónde ha ido (id nuevo). Tiene que cubrir **todas** tus líneas asignadas.
2. **Lo que has tirado y por qué** (id del canon).
3. **Dudas para el autor**: casos que el canon no zanja y que has dejado neutros.
4. **Enlaces salientes**: los ids de otros capítulos a los que enlazas (para comprobar que existen).

Tu informe final: un párrafo con lo hecho, el tamaño del fragmento y las dudas. No edites nada fuera de `src/v2/`.
