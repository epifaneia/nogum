# Registro K1 · Bazar, primera parte

Fragmento: `src/v2/fK1_bazar_a.html` (≈107 KB, 207 objetos en 22 tablas). Abre `<section class="chapter" id="apx-bazar">` con h2 «9.3 El Bazar del Multiverso» y **no la cierra** (sigue K2).

Cómo se hizo: la cabeza (entrada, `bz-lectura`, `bz-fabrica`) está escrita a mano; los catálogos 1–7 se copiaron por script (`frag_bazar.html` 147–480) y cada fila se corrigió desde una tabla de cambios por objeto. Las tablas pasan de 6 a 8 columnas: Objeto · Daño · Esq · Abs · **Acceso · Puntos · Llaves** · Notas. Lo que antes iba en «Acceso / Rejilla» (las etiquetas de Rejilla, Permiso, Efecto… y la descripción de los objetos que no atacan) va ahora al principio de Notas. Cada objeto con precio rehecho lleva al final de Notas «*La cuenta:* …» con su marca `C·…`.

## 1. De dónde sale cada parte

| Fuente (frag_bazar.html) | Destino |
|---|---|
| 1–2 (section, h2 8.3) | `apx-bazar`, h2 «9.3 El Bazar del Multiverso» |
| — (nuevo) | `p.lede` de la sección (C·e5) |
| 3–4 (entrada) | entrada, casi literal («Este apéndice» → «Es material…»; añadido «Y el precio sale justo de ahí») |
| 5 (aside de marcas) | igual |
| 6–19 (`bz-lectura`, la `dl`) | `bz-lectura`: Daño 0–2 (sin Daño 3 ni Masivo/Absoluto/Infinito), nueva entrada «La Parca · Rejilla N», Esq (con la pistola y los blásters), Abs, Rejilla (sin «Llave N» ni «Ignora todo»), Acceso · Puntos · Llaves |
| 18, 20, 40, 49–52, 104–105 (los precios viejos) | sustituidos por el recuadro nuevo `bz-precios` «De dónde salen los números de las columnas» (aplica 5.4 a las etiquetas, con enlaces) |
| 20 (tablas de poderes sin Acceso) | párrafo tras `bz-precios`, corregido: pagan puntos y Llaves; el regalo de la ficción no se paga (C·e6) |
| 22 (recordatorio del procedimiento) | igual, enlace a 6.2; «columna Notas» |
| 23–31 (aside ED-B1–B3 y demás) | igual; ED-B3 reescrito (enlace a 0.7, sin «ningún objeto mata»); **ED-B4 nuevo** (precios del 22 oct) |
| 32–34 (`bz-fabrica`, entrada del taller) | `bz-fabrica` corto: tabla de equivalencias + 4 pasos con enlaces a 5.4, 5.5, 5.6 |
| 35–44 (tres monedas) | → 5.4–5.6 (F). Aquí solo el paso 3 del taller |
| 46–54 (la cuenta) | → 5.4 (F). Aquí, los 4 pasos en una línea cada uno |
| 55–61 (las dos pruebas) | → 5.4 (F). Aquí, una frase con enlace; la 2.ª prueba corregida («Llave de nivel», no «nivel de Rejilla», bz:59) |
| 63–84 (el Ajuste, tramo gratis, «solo paga lo no pagado») | → 5.5 (F). Aquí solo un enlace en `bz-precios` |
| 86–97 (la invisibilidad, tres precios) | → 5.5 (F). Aquí, una frase con los tres precios, el tercero corregido a 4 Llaves |
| 99–108 (cuatro categorías) | → 5.6 (F). Las categorías siguen nombradas en la tabla de búsqueda |
| 110–127 (seis cajones, tirón de Recursos) | → 5.6 (F). Aquí, enlace a 5.6 |
| 129–133 (aviso: el equipo come de los puntos) | → F (5.2 / 5.6). No se repite aquí |
| 135–145 (cómo encontrar lo que buscas) | `bz-fabrica`, h4 «Cómo encontrar lo que buscas en el catálogo», igual; enlace a `bz-indice` |
| 147–198 (`bz-fantasia`) | igual, precios rehechos |
| 199–245 (`bz-neon`) | igual, precios rehechos |
| 246–292 (`bz-terror`) | igual, precios rehechos |
| 293–340 (`bz-opera`) | igual; párrafo de 326 reescrito (son poderes: punto en Arcano, puntos y Llaves, C·l10) |
| 341–386 (`bz-postapo`) | igual, precios rehechos |
| 387–433 (`bz-wuxia`) | igual, precios rehechos |
| 434–480 (`bz-gotico`) | igual, precios rehechos |

## 2. Lo que he tirado y por qué

- **Daño 3 («a comer con San Pedro»)** y los especiales **Masivo, Absoluto, Infinito** de la leyenda (bz:10): c2, el daño de un arma llega a 2 más la Parca; la broma nombraba la muerte (l8).
- **«Son gratis: describen lo que el objeto es»** (bz:49) y **«Llaves solo si rompe la Rejilla / por encima de tu nivel»** (bz:18, 20, 40, 104): e5, e8.
- **«x² contra un objetivo, 2·x² contra todo»** (bz:52): l4, el precio estaba invertido.
- **«El tramo gratis: una escena»** (bz:75–77) en su forma «por debajo de 1, gratis»: e7 (mínimo 1; lo de una escena o de un uso no se paga, pero no por ser barato).
- **«El Ancla corta en +4»** (bz:132): a1. El aviso entero se va con la teoría a F.
- **«Ningún objeto mata por reglas (5.5)»** (ED-B3): absoluto; queda «los objetos dejan fuera de combate; la muerte se pacta (0.7)».
- **«(«ya estás muerto»)»** del Puño de los Cien Puños y **«El original decía «mata todo en la zona»»** del Gordo, y **«la muerte, solo si se pacta»** del Corta-Dioses y la Espada Ancestral: l8 (en la Parca no se nombra la muerte; vive en 0.7).
- **«el total sigue dentro de [−2, +4]»** (Daga de Ladrón) y **«El bono total sigue limitado a [−2, +4]»** (Pendientes de fusión): a2 (se acumula; ver 2.5).
- **«Eres indetectable»** del Anillo: pasa a «invisible mientras lo llevas» (indetectable es Sigilo de nivel 3, 4 Llaves; el anillo es la capa).
- **«Se compran como equipo»** (poderes del Flujo, 326): l10.
- **«El capítulo de experiencia está aplazado»** (el filo que nadie levanta): ya existe 5.8.
- **«Permiso: Información»** de la Cámara Hackeada: pasa a «Efecto: información» (lo hace una tirada de Artificio; l9: si una habilidad lo hace, no es permiso).
- **Rejilla «2» del Cañón de Riel** (bz:212 ?): pasa a La Parca · Rejilla 3, que es lo que ya cobraba (4 Llaves) y lo que pide «daña tanques» (el tanque es N3, Tabla 2).
- **Esq: Parcial del Lanzagranadas** (bz:211 C): pasa a La Parca · Rejilla 2, Esq: Difícil, Abs: Nula, como las granadas (l2: «esquivar es difícil»).

## 3. Dudas para el autor

1. **Abs: Nula se cobra como Llave (1).** El canon dice «la pistola no dificulta: anula la esquiva, pagas Llave», y el 22 oct «anula lo que diga que anula… esquiva, bloqueo y daño». He leído que anular la absorción es lo mismo que anular la esquiva: 1 Llave (y las dos juntas, 1, porque es lo que hace una Llave de un nivel). Si prefieres que atravesar armadura sea solo «dificultar» (puntos), los objetos cuya Llave sale **solo** de Abs: Nula son: Estoque de Duelista, Táser, Katana Monofilo, Motosierra, Sable de Energía, Lanzarredes, Martillo Neumático, Garras de la Bestia (1 → 0, y pasarían a 1 punto), y la Llave de Abs: Nula de Nanocable, Lanzallamas Casero, Lanzallamas Pesado, Golpe de una Pulgada, Toque Vampírico, Empujón del Flujo, Carga Psiónica, Toque de Descomposición (−1 Llave cada uno).
2. **Cuántos puntos vale cada etiqueta.** He puesto Esq: Parcial 1, Esq: Difícil 2, Abs: Máx 1 1, Abs: Máx 2 0 (con daño 2 solo cuenta en crítico), Mejor de 2d10 ≈ +2. El canon dice «se paga por puntos» sin cifra.
3. **La esquiva de las armas de la Parca no se cobra aparte** (granada, coche, aliento): es lo que la Llave deja intentar. Si se cobrara, una Parca que deja esquivar a −2 costaría más que una que no deja, que es al revés.
4. **Hechizo que hace daño = permiso (1 Llave) + lo que anule.** Bola de Fuego 1 Llave + 2 puntos; Proyectil Mágico 2 Llaves. ¿Te vale, o el hechizo de daño solo paga lo que anula?
5. **El Corta-Dioses a 25 Llaves** («La Parca · cualquier nivel» = hasta el 6 desde el 1). Lo aprobaste como «ignora la malla»; no sé si quieres que tenga precio de equipo.
6. **Las herramientas que «dan bonificador»** (Palanca, Cuerda) las he tratado como dificultad de escena, sin puntos; la Linterna y el Mapa igual (sin cambio). Los Ciberojos, el Visor y los Ojos Brillantes sí pagan 1 punto (como la mira automática de e8). La frontera es mía.
7. **La mira automática de la Pistola Inteligente**: le he puesto +1 a dar, 1 punto, para que se distinga de la pistola normal (que ahora tampoco se esquiva).
8. **El Escudo de Torre** («permite absorber lo que no se esquiva»): con la regla vigente eso ya se puede; lo he tasado como el escudo de las piezas sueltas, 1 punto.
9. **Ajustes a ojo**: Celeridad 3 Llaves (Desatado), Clon de Sombras, Forma de Niebla, Teletransporte Instantáneo y Singularidad 2 (Potenciado), Meditación de Batalla 4 puntos, Bomba de Energía 5 (La Parca 4, Limitada por la carga), Transformación y Pendientes de fusión 3 (Rejilla de un ámbito, Limitada), Amuleto Solar 2 (solo vampiros).
10. **Consumibles**: Sal, Bengala de Señales, Granadas, Elixir de Vitae, pociones y drogas no se pagan. La Sal y la Bengala dependen de si es un puñado / una bengala (gratis) o un saco que no se acaba (1 Llave): he dejado la Sal gratis y la Bengala a 1 Llave (como pistola de bengalas), con la otra lectura en la nota.

### Para K2 y K3 (coherencia con las piezas sueltas y el índice)

- **Velo absoluto** (bz:710): «2 × 2² = 8» es el precio invertido; con l4, Sigilo dos niveles contra todo es 2² = **4**. Mi taller ya dice 4.
- **Fuerza de sala / de edificio** (bz:713–714): usan 2·x² por Disciplina; con l4 son 4 × 1 = 4 (sala) y 4 × 4 = 16 (edificio), por debajo del tope de la Rejilla (5 y 20).
- **Arma de maestro armero** (bz:652): «es un suelo» contradice a2.
- **Arma silenciosa** (bz:666, Esq: Nula por sorpresa) y **Arma que abre la armadura** (bz:657, Abs: Nula): con mi lectura, 1 Llave cada una (ver duda 1).
- **Escudo** de las piezas (bz:676): contra Abs: Nula una vez por escena; con mi lectura eso sería una Llave Limitada (1). Yo le he copiado el precio (1 punto) al Escudo de Torre.
- **Ropa reforzada** (bz:673): absorbe 1 sin puntos; aquí la Cota de Malla, el Kevlar y demás pagan 1 punto por absorber 1 (e5, y el índice viejo ya lo hacía).
- **La lista** (bz:663): «No te matan» (l8).
- En el índice, objetos de mis tablas que el índice viejo pone en una categoría y precio que ya no cuadran: los de la tabla de abajo.

## 4. Enlaces salientes

`ch0-muerte`, `ch2-bonos`, `ch3-sincro`, `ch3-techos`, `ch4-anula`, `ch4-escalera`, `ch4-tipos`, `ch4-parca`, `ch4-hechizos`, `ch4-ejemplos`, `ch5-cambio`, `ch5-cuenta`, `ch5-ajuste`, `ch5-equipo`, `ch5-devolver`, `ch5-progreso`, `ch6-golpes`, `ch6-armas`, `ch6-consecuencias`, y dentro del Bazar `bz-piezas` (K2) y `bz-indice` (K3). Ids propios nuevos: `bz-precios` (recuadro). Ids viejos conservados: `apx-bazar`, `bz-lectura`, `bz-fabrica`, `bz-fantasia`, `bz-neon`, `bz-terror`, `bz-opera`, `bz-postapo`, `bz-wuxia`, `bz-gotico`.

## 5. Tabla para K3: objetos con precio o etiquetas cambiadas

Formato del precio como en el índice viejo («Acceso N · N puntos · N Llaves»; «—» = sin coste ni Acceso). Los objetos que no salen aquí conservan su precio viejo (y siguen a 0 puntos, 0 Llaves salvo lo que ya tenían). La columna de etiquetas solo se rellena si cambió Daño o Esq (lo que el índice muestra en «Qué hace»).

| Objeto | De dónde | Precio viejo | **Precio nuevo** | Etiquetas nuevas (si cambian) |
|---|---|---|---|---|
| Daga de Ladrón | 1. La mazmorra y la estepa | Acceso 0 | **Acceso 0 · 1 punto** |  |
| Espada Larga (Bastarda) | 1. La mazmorra y la estepa | Acceso 1 | **Acceso 1 · 1 punto** |  |
| Mandoble a Dos Manos | 1. La mazmorra y la estepa | Acceso 2 | **Acceso 2 · 1 punto** |  |
| Estoque de Duelista | 1. La mazmorra y la estepa | Acceso 0 | **Acceso 0 · 1 Llave** |  |
| Hacha de Batalla Enana | 1. La mazmorra y la estepa | Acceso 1 | **Acceso 1 · 1 punto** |  |
| Lanza de Caballería | 1. La mazmorra y la estepa | Acceso 2 | **Acceso 2 · 1 punto** |  |
| Cimitarra | 1. La mazmorra y la estepa | Acceso 0 | **Acceso 0 · 1 punto** |  |
| El filo imposible (Corta-Dioses) | 1. La mazmorra y la estepa | Acceso 3 | **Acceso 3 · 25 Llaves** | La Parca · cualquier nivel · Esq: Total |
| Arco Largo Élfico | 1. La mazmorra y la estepa | Acceso 1 | **Acceso 1 · 2 puntos** |  |
| Ballesta Pesada | 1. La mazmorra y la estepa | Acceso 2 | **Acceso 2 · 1 punto · 1 Llave** |  |
| Proyectil Mágico | 1. La mazmorra y la estepa | Acceso 1 | **Acceso 1 · 2 Llaves** |  |
| Bola de Fuego | 1. La mazmorra y la estepa | Acceso 2 | **Acceso 2 · 2 puntos · 1 Llave** |  |
| Rayo Relámpago | 1. La mazmorra y la estepa | Acceso 2 | **Acceso 2 · 2 Llaves** |  |
| Toque Vampírico | 1. La mazmorra y la estepa | Acceso 0 | **Acceso 0 · 2 Llaves** |  |
| Escudo de Torre | 1. La mazmorra y la estepa | Acceso 0 | **Acceso 0 · 1 punto** |  |
| Cota de Malla | 1. La mazmorra y la estepa | Acceso 0 | **Acceso 0 · 1 punto** |  |
| Placas Completas | 1. La mazmorra y la estepa | Acceso 0 | **Acceso 0 · 2 puntos** |  |
| Capa de Desplazamiento | 1. La mazmorra y la estepa | Acceso 1 | **Acceso 1 · 2 puntos** |  |
| Anillo de Invisibilidad | 1. La mazmorra y la estepa | Acceso 0 | **Acceso 0 · 1 Llave** |  |
| Botas de Levitación | 1. La mazmorra y la estepa | Acceso 0 | **Acceso 0 · 1 Llave** |  |
| Gema de Luz | 1. La mazmorra y la estepa | Acceso 0 | **Acceso 0 · 1 Llave** |  |
| Amuleto Anti-Detección | 1. La mazmorra y la estepa | Acceso 0 | **Acceso 0 · 1 Llave** |  |
| Pistola Ligera (9 mm) | 2. La Ciudad de Neón | Acceso 0 | **Acceso 0 · 1 Llave** | Daño 1 · Esq: Nula |
| Pistola Pesada (.44 Magnum) | 2. La Ciudad de Neón | Acceso 1 | **Acceso 1 · 1 punto · 1 Llave** | Daño 2 · Esq: Nula |
| Subfusil (SMG) | 2. La Ciudad de Neón | Acceso 0 | **Acceso 0 · 1 Llave** | Daño 1 · Esq: Nula (ráfaga) |
| Escopeta (Cartucho) | 2. La Ciudad de Neón | Acceso 2 | **Acceso 2 · 1 punto · 1 Llave** | Daño 2 · Esq: Nula |
| Rifle de Asalto | 2. La Ciudad de Neón | Acceso 1 | **Acceso 1 · 1 punto · 1 Llave** | Daño 2 · Esq: Nula |
| Rifle de Francotirador (Antimaterial) | 2. La Ciudad de Neón | Acceso 3 | **Acceso 3 · 1 Llave** |  |
| Lanzagranadas | 2. La Ciudad de Neón | Acceso 2 | **Acceso 2 · 1 Llave** | La Parca · Rejilla 2 · Esq: Difícil (−2) |
| Cañón de Riel (Railgun) | 2. La Ciudad de Neón | Acceso 3 · 4 Llaves | **Acceso 3 · 4 Llaves** | La Parca · Rejilla 3 · Esq: Nula |
| Pistola Inteligente (Smart) | 2. La Ciudad de Neón | Acceso 1 | **Acceso 1 · 1 punto · 1 Llave** |  |
| Táser / Arma de Choque | 2. La Ciudad de Neón | Acceso 0 | **Acceso 0 · 1 Llave** |  |
| Katana Monofilo | 2. La Ciudad de Neón | Acceso 1 | **Acceso 1 · 1 Llave** |  |
| Martillo Cohete | 2. La Ciudad de Neón | Acceso 2 | **Acceso 2 · 1 punto** |  |
| Garras Mantis | 2. La Ciudad de Neón | Acceso 1 | **Acceso 1 · 1 Llave** |  |
| Nanocable (Látigo) | 2. La Ciudad de Neón | Acceso 1 | **Acceso 1 · 2 puntos · 1 Llave** |  |
| Chaleco Kevlar | 2. La Ciudad de Neón | Acceso 0 | **Acceso 0 · 1 punto** |  |
| Blindaje Dérmico (implante) | 2. La Ciudad de Neón | Acceso 1 | **Acceso 1 · 1 punto** |  |
| Implante de tiempo lento (Dilatador) | 2. La Ciudad de Neón | Acceso 0 | **Acceso 0 · 1 Llave** |  |
| Camuflaje Termo-Óptico | 2. La Ciudad de Neón | Acceso 0 | **Acceso 0 · 1 Llave** |  |
| Inhibidor de Dolor | 2. La Ciudad de Neón | Acceso 0 | **Acceso 0 · 2 puntos** |  |
| Ciberojos | 2. La Ciudad de Neón | Acceso 0 | **Acceso 0 · 1 punto** |  |
| Hielo Negro (virus) | 2. La Ciudad de Neón | Acceso 2 | **Acceso 2 · 1 Llave** |  |
| Piernas Reforzadas | 2. La Ciudad de Neón | Acceso 0 | **Acceso 0 · 1 Llave** |  |
| Motosierra | 3. Pulpos antediluvianos | Acceso 2 | **Acceso 2 · 1 Llave** |  |
| Escopeta de Caza | 3. Pulpos antediluvianos | Acceso 2 | **Acceso 2 · 1 Llave** | Daño 2 · Esq: Nula |
| Revólver .38 | 3. Pulpos antediluvianos | Acceso 0 | **Acceso 0 · 1 Llave** | Daño 1 · Esq: Nula |
| Bengala de Señales | 3. Pulpos antediluvianos | Acceso 1 | **Acceso 1 · 1 Llave** |  |
| Libro Maldito | 3. Pulpos antediluvianos | Acceso 0 | **Acceso 0 · 1 Llave por hechizo** |  |
| Símbolo Arcano (tiza) | 3. Pulpos antediluvianos | Acceso 0 | **Acceso 0 · 1 Llave** |  |
| Daga Ritual | 3. Pulpos antediluvianos | Acceso 0 | **Acceso 0 · 1 Llave** |  |
| Cámara Fotográfica | 3. Pulpos antediluvianos | Acceso 0 | **Acceso 0 · 1 Llave** |  |
| Amuleto de la Abuela | 3. Pulpos antediluvianos | Acceso 0 | **Acceso 0 · 1 punto** |  |
| Grabadora | 3. Pulpos antediluvianos | Acceso 0 | **Acceso 0 · 1 Llave** |  |
| Ouija | 3. Pulpos antediluvianos | Acceso 0 | **Acceso 0 · 1 Llave** |  |
| Muñeco Vudú | 3. Pulpos antediluvianos | Acceso 1 | **Acceso 1 · 2 Llaves** |  |
| Pistola Bláster | 4. Ópera de Estrellas | Acceso 1 | **Acceso 1 · 1 punto** |  |
| Rifle de Plasma | 4. Ópera de Estrellas | Acceso 2 | **Acceso 2 · 2 puntos** |  |
| Sable de Energía | 4. Ópera de Estrellas | Acceso 2 | **Acceso 2 · 1 Llave** |  |
| Cañón de Iones | 4. Ópera de Estrellas | Acceso 1 | **Acceso 1 · 1 Llave** |  |
| Ballesta del gigante peludo (energética) | 4. Ópera de Estrellas | Acceso 2 | **Acceso 2 · 3 puntos** |  |
| Rifle Francotirador Láser | 4. Ópera de Estrellas | Acceso 2 | **Acceso 2 · 1 Llave** |  |
| Granada Térmica | 4. Ópera de Estrellas | Acceso 2 · 1 Llave | **Acceso 2** |  |
| Lanzarredes Electrificado | 4. Ópera de Estrellas | Acceso 0 | **Acceso 0 · 1 Llave** |  |
| Guantelete de Choque | 4. Ópera de Estrellas | Acceso 0 | **Acceso 0 · 1 punto** |  |
| Lanza Vibratoria | 4. Ópera de Estrellas | Acceso 1 | **Acceso 1 · 1 punto** |  |
| Escudo Deflector Personal | 4. Ópera de Estrellas | Acceso 0 | **Acceso 0 · 1 punto** |  |
| Armadura de Soldado de Asalto | 4. Ópera de Estrellas | Acceso 0 | **Acceso 0 · 1 punto** |  |
| Jetpack (mochila cohete) | 4. Ópera de Estrellas | Acceso 0 | **Acceso 0 · 1 Llave** |  |
| Generador de Camuflaje | 4. Ópera de Estrellas | Acceso 0 | **Acceso 0 · 1 Llave** |  |
| Brazal Escudo | 4. Ópera de Estrellas | Acceso 0 | **Acceso 0 · 1 punto** |  |
| Casco con Visor Táctico | 4. Ópera de Estrellas | Acceso 0 | **Acceso 0 · 1 punto** |  |
| Implante de Traducción | 4. Ópera de Estrellas | Acceso 0 | **Acceso 0 · 1 Llave** |  |
| Capa de la Orden / los Caídos | 4. Ópera de Estrellas | Acceso 1 | **Acceso 1 · 1 punto** |  |
| Empujón del Flujo | 4. Ópera de Estrellas | — | **2 puntos · 2 Llaves** |  |
| Rayo del Flujo | 4. Ópera de Estrellas | — | **2 Llaves** |  |
| Truco Mental | 4. Ópera de Estrellas | — | **1 Llave** |  |
| Salto del Flujo | 4. Ópera de Estrellas | — | **1 Llave** |  |
| Lanzamiento de Sable | 4. Ópera de Estrellas | — | **1 Llave** |  |
| Singularidad (Vórtice) | 4. Ópera de Estrellas | — | **2 Llaves** |  |
| Carga Psiónica | 4. Ópera de Estrellas | — | **1 punto · 2 Llaves** |  |
| Estrangular | 4. Ópera de Estrellas | — | **2 Llaves** |  |
| Meditación de Batalla | 4. Ópera de Estrellas | — | **4 puntos** |  |
| Fantasma del Flujo | 4. Ópera de Estrellas | — | **1 Llave** |  |
| Bate con Clavos | 5. Post-Apocalipsis | Acceso 1 | **Acceso 1 · 1 punto** |  |
| Ballesta de Resorte (de coche) | 5. Post-Apocalipsis | Acceso 2 | **Acceso 2 · 3 puntos** |  |
| Lanzallamas Casero | 5. Post-Apocalipsis | Acceso 1 | **Acceso 1 · 1 punto · 1 Llave** |  |
| Martillo Neumático | 5. Post-Apocalipsis | Acceso 2 | **Acceso 2 · 1 Llave** |  |
| Sierra Circular de Mano | 5. Post-Apocalipsis | Acceso 2 | **Acceso 2 · 2 puntos** |  |
| El «Gordo» (lanzabombas) | 5. Post-Apocalipsis | Acceso 3 | **Acceso 3 · 4 Llaves** | La Parca · Rejilla 3 · Esq: Parcial |
| Armadura de Neumáticos | 5. Post-Apocalipsis | Acceso 0 | **Acceso 0 · 1 punto** |  |
| Armadura de Chapas de Señal | 5. Post-Apocalipsis | Acceso 0 | **Acceso 0 · 1 punto** |  |
| Brazo Extra | 5. Post-Apocalipsis | — | **1 Llave** |  |
| Piel de Escamas | 5. Post-Apocalipsis | — | **1 punto** |  |
| Ojos Brillantes | 5. Post-Apocalipsis | — | **1 punto** |  |
| Glándulas de Adrenalina | 5. Post-Apocalipsis | — | **1 punto** |  |
| Emisor de camuflaje | 5. Post-Apocalipsis | — | **1 Llave** |  |
| Mutante Mascota | 5. Post-Apocalipsis | — | **1 Llave** |  |
| El Puño de los Cien Puños | 6. Artes marciales, brillos y gritos | — | **1 Llave** | La Parca · Rejilla 2 · Esq: Nula |
| Patada Huracán | 6. Artes marciales, brillos y gritos | — | **1 punto** |  |
| Paso de la Sombra (Paso relámpago) | 6. Artes marciales, brillos y gritos | — | **1 Llave** |  |
| Golpe de una Pulgada | 6. Artes marciales, brillos y gritos | — | **2 puntos · 1 Llave** |  |
| Piel de Hierro | 6. Artes marciales, brillos y gritos | — | **2 puntos** |  |
| Caminar por el Aire | 6. Artes marciales, brillos y gritos | — | **1 Llave** |  |
| Corte de Viento (katana) | 6. Artes marciales, brillos y gritos | — | **1 punto · 1 Llave** |  |
| Clon de Sombras | 6. Artes marciales, brillos y gritos | — | **2 Llaves** |  |
| Puño Borracho | 6. Artes marciales, brillos y gritos | — | **2 puntos** |  |
| Los Ocho Puntos (Desbloqueo) | 6. Artes marciales, brillos y gritos | — | **2 puntos** |  |
| Bengala Solar (Destello cegador) | 6. Artes marciales, brillos y gritos | — | **1 Llave** |  |
| Vuelo de Ki | 6. Artes marciales, brillos y gritos | — | **1 Llave** |  |
| Escudo de Energía | 6. Artes marciales, brillos y gritos | — | **1 Llave** |  |
| Sentir el Ki | 6. Artes marciales, brillos y gritos | — | **1 Llave** |  |
| Teletransporte Instantáneo | 6. Artes marciales, brillos y gritos | — | **2 Llaves** |  |
| Bomba de Energía (Bomba de energía prestada) | 6. Artes marciales, brillos y gritos | — | **5 Llaves** | La Parca · Rejilla 4 · Esq: Nula |
| Transformación (Super) | 6. Artes marciales, brillos y gritos | — | **3 Llaves** |  |
| Regeneración (unión definitiva) | 6. Artes marciales, brillos y gritos | — | **1 Llave** |  |
| Báculo Sagrado | 6. Artes marciales, brillos y gritos | Acceso 0 | **Acceso 0 · 1 Llave** |  |
| Pendientes de fusión | 6. Artes marciales, brillos y gritos | Acceso 0 | **Acceso 0 · 3 Llaves** |  |
| Abanico de las tres tormentas | 6. Artes marciales, brillos y gritos | Acceso 1 | **Acceso 1 · 1 punto · 1 Llave** |  |
| Radar de Reliquias | 6. Artes marciales, brillos y gritos | Acceso 0 | **Acceso 0 · 1 Llave** |  |
| Armadura del guerrero de otro planeta | 6. Artes marciales, brillos y gritos | Acceso 0 | **Acceso 0 · 1 punto** |  |
| Garras de la Bestia | 7. Horror Gótico | — | **1 Llave** |  |
| La Mirada (Dominación) | 7. Horror Gótico | — | **1 Llave** |  |
| Celeridad (Velocidad) | 7. Horror Gótico | — | **3 Llaves** |  |
| Piel de Mármol | 7. Horror Gótico | — | **2 puntos** |  |
| Forma de Niebla | 7. Horror Gótico | — | **2 Llaves** |  |
| Presencia Majestuosa | 7. Horror Gótico | — | **1 Llave** |  |
| Toque de Descomposición | 7. Horror Gótico | — | **2 Llaves** |  |
| Sangre Ácida | 7. Horror Gótico | — | **1 Llave** |  |
| Salto de Depredador | 7. Horror Gótico | — | **1 Llave** |  |
| Invisibilidad Mental (Ofuscación) | 7. Horror Gótico | — | **1 Llave** |  |
| Estaca de Madera | 7. Horror Gótico | Acceso 0 | **Acceso 0 · 2 puntos · 1 Llave** |  |
| Balas de Plata | 7. Horror Gótico | Acceso 0 | **Acceso 0 · 1 Llave** |  |
| Lanzallamas Pesado | 7. Horror Gótico | Acceso 2 | **Acceso 2 · 1 punto · 1 Llave** |  |
| Espada Ancestral | 7. Horror Gótico | Acceso 3 · 4 Llaves | **Acceso 3 · 1 punto · 4 Llaves** |  |
| Escopeta con Aliento de Dragón | 7. Horror Gótico | Acceso 1 | **Acceso 1 · 1 punto · 1 Llave** | Daño 2 (fuego) · Esq: Nula |
| Martillo de Guerra (almádena) | 7. Horror Gótico | Acceso 2 | **Acceso 2 · 1 punto** |  |
| Granada de Fósforo | 7. Horror Gótico | Acceso 2 · 1 Llave | **Acceso 2** |  |
| Trampa para Osos | 7. Horror Gótico | Acceso 1 | **Acceso 1 · 3 puntos** |  |
| Elixir de Vitae (sangre de anciano) | 7. Horror Gótico | Acceso 3 · 4 Llaves | **Acceso 3** |  |
| Amuleto Solar | 7. Horror Gótico | Acceso 3 · 4 Llaves | **Acceso 3 · 2 Llaves** |  |
| Ropa de Diseño con Kevlar | 7. Horror Gótico | Acceso 0 | **Acceso 0 · 1 punto** |  |
