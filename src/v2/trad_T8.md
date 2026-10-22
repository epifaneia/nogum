# Registro T8 · Traducción de `fK1_bazar_a.html` → `fK1_bazar_a.en.html`

Apartado 9.3 The Multiverse Bazaar, del principio hasta el final de «7. Gothic Horror». Abre `<section id="apx-bazar">` y no la cierra, igual que el castellano.

## Términos elegidos (no estaban en la tabla de TRADUCCION.md)

| Castellano | English | Nota |
|---|---|---|
| Columnas: Objeto · Daño · Esq · Abs · Acceso · Puntos · Llaves · Notas | Object · Damage · Dodge · Soak · Access · Points · Keys · Notes | Según el encargo |
| *La cuenta:* (en las notas) | *Tally:* | Cabecera de la tabla de casos: «La cuenta» → «Tally» |
| Etiqueta `Daño N` | `Damage N` (también `Mental Damage N`, `Social Damage N`) | El inglés viejo decía «Dmg»; la tabla de TRADUCCION.md manda «Damage» |
| Esq: Total / Parcial / Nula / Difícil (−2) / Fácil (+2) | Dodge: Full / Partial / None / Hard (−2) / Easy (+2) | Como el inglés viejo |
| Abs: Total / Máx N / Nula / Mente | Soak: Full / Max N / None / Mind | Como el inglés viejo |
| La Parca · Rejilla N / · cualquier nivel | The Reaper · Grid N / · any level | |
| Rejilla: Estándar / Nivel N / cualquier nivel / Llave espiritual | Grid: Standard / Level N / any level / Spirit Key | |
| Permiso (etiqueta), Permiso: Vuelo… | Permit, Permit: Flight / Radar / Travel / Fear / Movement | «permiso» → «permit» (tabla) |
| correa (de un poder) | strap | Como el inglés viejo («mandatory strap») |
| no descuenta | is no discount | |
| las piezas sueltas | the loose parts | Como `frag_bazar_b.en.html` |
| el instante robado | the stolen instant | Como `frag_bazar_b.en.html` |
| la lengua común | the common tongue | Como `frag_bazar_b.en.html` |
| Superfuerza, el Martillo Digno | Super Strength, the Worthy Hammer | Como `frag_bazar_b.en.html` |
| N2 / N3 («opera en N2») | L2 / L3 | Como el inglés viejo |
| barra (Mental) | bar | Tabla; el inglés viejo decía «track» |
| Artificio, Destreza, Alerta, Sigilo, Potencia, Armas, Atletismo | Artifice, Dexterity, Alertness, Stealth, Might, Weapons, Athletics | Como el inglés viejo |
| Comedia negra (tarjeta) | Black Comedy | Mayúsculas de la tabla de tonos |
| sable de luz (Lanza Vibratoria) | light sabre | Genérico, británico |

## Pasajes dudosos

- **Ordenador de pulsera (ordenador de muñeca)** → «Wrist computer». El inglés viejo decía «Wrist computer (wrist computer)», que repite lo mismo; quité el paréntesis. Si el índice necesita el nombre viejo exacto, se puede volver a poner.
- **El inhalador de combate** → «The combat inhaler». El castellano cambió el nombre (el inglés viejo decía «Jet (drug)», que es una marca de un videojuego). Nombre nuevo: el índice inglés viejo hay que corregirlo.
- **Garras Mantis** → se queda «Arm Blades», como el inglés viejo (evita el nombre con marca).
- **Jetpack (mochila cohete)** → «Jetpack», como el inglés viejo y su índice.
- «Siempre dentro de los límites de la etiqueta» → «All of this within the limits of the tag» (sin el absoluto, como pide el estilo).
- «En la mayoría de mesas no es equipo de personaje: es un argumento» → «At most tables it is not character equipment: it is a plot».
- Apóstrofos de los nombres de objeto rectos (`Thief's Dagger`) para que casen letra a letra con el índice inglés viejo; en el resto del texto, tipográficos (’).

## Comprobación de estructura (script)

Contra `fK1_bazar_a.html`: mismas etiquetas y en el mismo número, mismos 12 ids, mismos 110 href en el mismo orden, mismas clases en el mismo orden, mismas 249 marcas `src`, mismas 251 filas con el mismo número de celdas, HTML equilibrado (solo queda abierta `section`, igual que en castellano). De las 643 celdas `num`, todas iguales salvo las tres con palabras («0 o 1» → «0 or 1», «1 o 0» → «1 or 0», «1 por hechizo» → «1 per spell»). El conjunto de números del texto visible es idéntico: no ha cambiado ningún número.

## Nombres de objeto usados (para el índice)

205 de los 207 coinciden letra a letra con `frag_bazar_a.en.html` / `frag_bazar_b.en.html`; los dos nuevos son «Wrist computer» y «The combat inhaler».

### 1. The Dungeon and the Steppe

| Castellano | English |
|---|---|
| Daga de Ladrón | Thief's Dagger |
| Espada Corta | Short Sword |
| Espada Larga (Bastarda) | Longsword (Bastard Sword) |
| Mandoble a Dos Manos | Two-Handed Greatsword |
| Estoque de Duelista | Duellist's Rapier |
| Hacha de Batalla Enana | Dwarven Battleaxe |
| Lanza de Caballería | Cavalry Lance |
| Cimitarra | Scimitar |
| Látigo de Púas | Barbed Whip |
| El filo imposible (Corta-Dioses) | The impossible blade (Godslayer) |
| Arco Corto | Shortbow |
| Arco Largo Élfico | Elven Longbow |
| Ballesta Pesada | Heavy Crossbow |
| Honda | Sling |
| Hachas Arrojadizas | Throwing Axes |
| Proyectil Mágico | Magic Missile |
| Bola de Fuego | Fireball |
| Rayo Relámpago | Lightning Bolt |
| Toque Vampírico | Vampiric Touch |
| Aliento de Dragón | Dragon's Breath |
| Escudo de Torre | Tower Shield |
| Cota de Malla | Chainmail |
| Placas Completas | Full Plate |
| Capa de Desplazamiento | Cloak of Displacement |
| Anillo de Invisibilidad | Ring of Invisibility |
| Botas de Levitación | Boots of Levitation |
| Gema de Luz | Light Gem |
| Poción de Piel de Piedra | Stoneskin Potion |
| Pergamino de Vuelo | Scroll of Flight |
| Amuleto Anti-Detección | Anti-Detection Amulet |

### 2. The City of Neon

| Castellano | English |
|---|---|
| Pistola Ligera (9 mm) | Light Pistol (9 mm) |
| Pistola Pesada (.44 Magnum) | Heavy Pistol (.44 Magnum) |
| Subfusil (SMG) | Submachine Gun (SMG) |
| Escopeta (Cartucho) | Shotgun (Shells) |
| Rifle de Asalto | Assault Rifle |
| Rifle de Francotirador (Antimaterial) | Sniper Rifle (Anti-Materiel) |
| Lanzagranadas | Grenade Launcher |
| Cañón de Riel (Railgun) | Railgun |
| Pistola Inteligente (Smart) | Smart Pistol |
| Táser / Arma de Choque | Taser / Shock Weapon |
| Cuchillo de Combate | Combat Knife |
| Katana Monofilo | Monowire Katana |
| Martillo Cohete | Rocket Hammer |
| Garras Mantis | Arm Blades |
| Nanocable (Látigo) | Nanowire (Whip) |
| Chaleco Kevlar | Kevlar Vest |
| Blindaje Dérmico (implante) | Subdermal Armour (implant) |
| Implante de tiempo lento (Dilatador) | Slow-time implant (Time Dilator) |
| Camuflaje Termo-Óptico | Thermo-Optical Camouflage |
| Inhibidor de Dolor | Pain Inhibitor |
| Ciberojos | Cybereyes |
| Brazo Gorila | Gorilla Arm |
| Granada EMP | EMP Grenade |
| Hielo Negro (virus) | Black ICE (virus) |
| Exoesqueleto Militar | Military Exoskeleton |
| Inyector de Adrenalina | Adrenaline Injector |
| Dron de Combate | Combat Drone |
| Interfaz de Hacking | Hacking Interface |
| Piernas Reforzadas | Reinforced Legs |
| Siroco (droga de combate) | Sirocco (combat drug) |

### 3. Antediluvian Octopuses Pending

| Castellano | English |
|---|---|
| Bate de Béisbol | Baseball Bat |
| Hacha de Bombero | Fire Axe |
| Motosierra | Chainsaw |
| Escopeta de Caza | Hunting Shotgun |
| Revólver .38 | .38 Revolver |
| Bengala de Señales | Signal Flare |
| Cuchillo de Cocina | Kitchen Knife |
| Coche (atropello) | Car (running someone over) |
| Piedra / Ladrillo | Rock / Brick |
| Libro Maldito | Cursed Book |
| Símbolo Arcano (tiza) | Arcane Sigil (chalk) |
| Daga Ritual | Ritual Dagger |
| Cámara Fotográfica | Camera |
| Agua Bendita (o Ácido) | Holy Water (or Acid) |
| Amuleto de la Abuela | Grandma's Amulet |
| Grabadora | Tape Recorder |
| Sal | Salt |
| Ouija | Ouija Board |
| Muñeco Vudú | Voodoo Doll |
| Linterna | Torch |
| Botiquín | First-Aid Kit |
| Radio de Onda Corta | Shortwave Radio |
| Palanca | Crowbar |
| Mochila de Suministros | Supply Backpack |
| Cuerda | Rope |
| Mechero | Lighter |
| Mapa Local | Local Map |
| Alcohol | Booze |
| Anfetaminas | Amphetamines |

### 4. Opera of Stars

| Castellano | English |
|---|---|
| Pistola Bláster | Blaster Pistol |
| Rifle de Plasma | Plasma Rifle |
| Sable de Energía | Energy Sword |
| Cañón de Iones | Ion Cannon |
| Ballesta del gigante peludo (energética) | The Hairy Giant's Crossbow (energy) |
| Rifle Francotirador Láser | Laser Sniper Rifle |
| Granada Térmica | Thermal Grenade |
| Lanzarredes Electrificado | Electrified Net Launcher |
| Guantelete de Choque | Shock Gauntlet |
| Lanza Vibratoria | Vibro-Lance |
| Escudo Deflector Personal | Personal Deflector Shield |
| Armadura de Soldado de Asalto | Assault Trooper Armour |
| Traje de Vacío | Vacuum Suit |
| Jetpack (mochila cohete) | Jetpack |
| Generador de Camuflaje | Cloaking Generator |
| Botas Magnéticas | Magnetic Boots |
| Brazal Escudo | Shield Bracer |
| Casco con Visor Táctico | Helmet with Tactical Visor |
| Implante de Traducción | Translation Implant |
| Capa de la Orden / los Caídos | The Order / the Fallen Cloak |
| Empujón del Flujo | Flow Push |
| Rayo del Flujo | Flow Lightning |
| Truco Mental | Mind Trick |
| Salto del Flujo | Flow Leap |
| Lanzamiento de Sable | Sword Throw |
| Singularidad (Vórtice) | Singularity (Vortex) |
| Carga Psiónica | Psionic Charge |
| Estrangular | Throat Grip |
| Meditación de Batalla | Battle Meditation |
| Fantasma del Flujo | Flow Ghost |

### 5. Post-Apocalypse Pending

| Castellano | English |
|---|---|
| Bate con Clavos | Nail Bat |
| Rifle de Clavos | Nail Rifle |
| Ballesta de Resorte (de coche) | Leaf-Spring Crossbow (from a car) |
| Lanzallamas Casero | Homemade Flamethrower |
| Martillo Neumático | Pneumatic Hammer |
| Sierra Circular de Mano | Handheld Circular Saw |
| Cóctel Molotov | Molotov Cocktail |
| Tubo de Plomo | Lead Pipe |
| El «Gordo» (lanzabombas) | The “Fat Boy” (bomb launcher) |
| Interceptor V8 | V8 Interceptor |
| Buggy de Arena | Dune Buggy |
| Camión de Guerra | War Rig |
| Armadura de Neumáticos | Tyre Armour |
| Armadura de Chapas de Señal | Road-Sign Armour |
| Contador Geiger | Geiger Counter |
| Máscara de Gas | Gas Mask |
| Pastillas de Yodo | Iodine Tablets |
| Carne de Perro en Lata | Canned Dog Meat |
| Agua Purificada | Purified Water |
| Brazo Extra | Extra Arm |
| Piel de Escamas | Scaly Skin |
| Ojos Brillantes | Glowing Eyes |
| Glándulas de Adrenalina | Adrenal Glands |
| Servoarmadura Antigua | Ancient Power Armour |
| Ordenador de pulsera (ordenador de muñeca) | Wrist computer |
| Emisor de camuflaje | Camouflage emitter |
| El inhalador de combate | The combat inhaler |
| Mutante Mascota | Mutant Pet |

### 6. Martial Arts, Glows and Shouting

| Castellano | English |
|---|---|
| El Puño de los Cien Puños | Fist of a Hundred Fists |
| Patada Huracán | Hurricane Kick |
| Paso de la Sombra (Paso relámpago) | Shadow Step (Lightning step) |
| Golpe de una Pulgada | One-Inch Punch |
| Piel de Hierro | Iron Skin |
| Caminar por el Aire | Air Walk |
| Corte de Viento (katana) | Wind Cutter (katana) |
| Clon de Sombras | Shadow Clone |
| Puño Borracho | Drunken Fist |
| Los Ocho Puntos (Desbloqueo) | The Eight Points (Release) |
| Onda de energía a dos manos (rayo) | Two-Handed Energy Wave (beam) |
| Disco Destructor | Destroyer Disc |
| Bengala Solar (Destello cegador) | Solar Flare (Blinding flash) |
| Vuelo de Ki | Ki Flight |
| Escudo de Energía | Energy Shield |
| Sentir el Ki | Sense Ki |
| Teletransporte Instantáneo | Instant Teleport |
| Bomba de Energía (Bomba de energía prestada) | Energy Bomb (Borrowed-energy bomb) |
| Transformación (Super) | Transformation (Super) |
| Regeneración (unión definitiva) | Regeneration (final merge) |
| Nube de los limpios de corazón | Cloud of the Pure of Heart |
| Báculo Sagrado | Sacred Staff |
| Semilla del viejo de la montaña | The Mountain Hermit's Bean |
| El filo que nadie puede levantar | The Blade Nobody Can Lift |
| Pendientes de fusión | Fusion Earrings |
| Pergamino de Técnica Prohibida | Forbidden Technique Scroll |
| Abanico de las tres tormentas | Fan of the Three Storms |
| Radar de Reliquias | Relic Radar |
| Armadura del guerrero de otro planeta | The Armour of the Warrior from Another Planet |
| Agua Sagrada | Sacred Water |

### 7. Gothic Horror

| Castellano | English |
|---|---|
| Garras de la Bestia | Claws of the Beast |
| La Mirada (Dominación) | The Gaze (Dominate) |
| Celeridad (Velocidad) | Celerity (Speed) |
| Piel de Mármol | Marble Skin |
| Forma de Niebla | Mist Form |
| Presencia Majestuosa | Majestic Presence |
| Toque de Descomposición | Touch of Decay |
| Sangre Ácida | Acid Blood |
| Salto de Depredador | Predator's Leap |
| Invisibilidad Mental (Ofuscación) | Mental Invisibility (Obfuscate) |
| Estaca de Madera | Wooden Stake |
| Balas de Plata | Silver Bullets |
| Lanzallamas Pesado | Heavy Flamethrower |
| Espada Ancestral | Ancestral Sword |
| Escopeta con Aliento de Dragón | Dragon's Breath Shotgun |
| Ballesta de Mano | Hand Crossbow |
| Martillo de Guerra (almádena) | War Hammer (sledgehammer) |
| Látigo de Cadenas | Chain Whip |
| Granada de Fósforo | Phosphorus Grenade |
| Trampa para Osos | Bear Trap |
| Bolsa de Sangre Médica | Medical Blood Bag |
| Elixir de Vitae (sangre de anciano) | Vitae Elixir (elder's blood) |
| Amuleto Solar | Solar Amulet |
| Ropa de Diseño con Kevlar | Kevlar Designer Clothes |
| Teléfono Desechable | Burner Phone |
| Refugio Seguro (escritura) | Safe Haven (title deed) |
| Ghouls (criados) | Ghouls (servants) |
| Motocicleta Negra | Black Motorcycle |
| Cámara de Seguridad Hackeada | Hacked Security Camera |
| Ataúd Blindado | Armoured Coffin |

Total: 207 objetos.
