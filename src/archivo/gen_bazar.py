# -*- coding: utf-8 -*-
"""Genera frag_bazar.html (apéndice 8.3 El Bazar del Multiverso)."""
import html, re, os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "frag_bazar.html")

FLAGS = {
    "B1": '<span class="flag ed">ED-B1</span>',
    "B2": '<span class="flag ed">ED-B2</span>',
    "B3": '<span class="flag ed">ED-B3</span>',
    "PROP": '<span class="flag proposal">Propuesta sin validar</span>',
}

def md(s):
    """Escapa y aplica mini-marcado: [[x]] -> tag, {B1} -> flag, {src:T68} -> src."""
    s = html.escape(s, quote=False)
    s = re.sub(r"\[\[(.+?)\]\]", lambda m: '<span class="tag">%s</span>' % m.group(1), s)
    s = re.sub(r"\{src:(.+?)\}", lambda m: '<span class="src">%s</span>' % m.group(1), s)
    s = re.sub(r"\{(B1|B2|B3|PROP)\}", lambda m: FLAGS[m.group(1)], s)
    return s

def tags(s):
    if not s:
        return "—"
    return " ".join('<span class="tag">%s</span>' % html.escape(t.strip(), quote=False) for t in s.split("|"))

def table(rows):
    out = ['<div class="tw"><table class="t">',
           "<thead><tr><th>Objeto</th><th>Daño</th><th>Esq</th><th>Abs</th><th>Malla / Efecto</th><th>Notas</th></tr></thead>",
           "<tbody>"]
    for r in rows:
        name, d, e, a, ef, notes = r
        out.append("<tr><td><strong>%s</strong></td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (
            md(name), tags(d), tags(e), tags(a), md(ef) if ef else "—", md(notes) if notes else "—"))
    out.append("</tbody></table></div>")
    return "\n".join(out)

T, P, N = "Esq: Total", "Esq: Parcial", "Esq: Nula"
AT, AN, M1, M2 = "Abs: Total", "Abs: Nula", "Abs: Máx 1", "Abs: Máx 2"
DIF, FAC = "Esq: Difícil (−2)", "Esq: Fácil (+2)"

SETTINGS = []

# ---------------------------------------------------------------- 1
SETTINGS.append(dict(
    id="bz-fantasia", title="1. Fantasía de la Vieja Escuela (D&amp;D / Conan)",
    lema="Donde el acero pesa y la magia rompe las reglas.", src="T68",
    status="Aprobada (T69)",
    blocks=[
        ("Armas de filo", [
            ("Daga de Ladrón", "Daño 1", T, AT, "[[Malla: Estándar]]", "+1 al ataque si atacas por la espalda (bonificador de situación; el total sigue dentro de [−2, +4])."),
            ("Espada Corta", "Daño 1", T, AT, "[[Malla: Estándar]]", "Fiable y rápida."),
            ("Espada Larga (Bastarda)", "Daño 2", T, M1, "", "Aunque pares con la armadura, te llevas al menos 1 punto de conmoción (la absorción solo quita 1)."),
            ("Mandoble a Dos Manos", "Daño 3", "Esq: Total (Lento)", M1, "", "La armadura evita que te corte, no que te rompa los huesos. «Total (Lento)» no está en la leyenda: se lee como Esq: Total; «Lento» es color narrativo (si el DJ quiere que pese en la mecánica, lo trata como Fácil +2)."),
            ("Estoque de Duelista", "Daño 1", T, "Abs: Nula en huecos", "", "Valor fuera de la leyenda. Por defecto, Abs: Total; si el atacante declara que busca los huecos (las axilas) y acierta con dificultad Difícil (−2), el golpe pasa a Abs: Nula. El original pedía «Dif 9», de la escala de TN descartada (ED-5)."),
            ("Hacha de Batalla Enana", "Daño 2", T, AT, "[[Efecto: rompe escudos]]", "El original dice que «elimina la defensa pasiva» (término antiguo): se lee como que el escudo del defensor deja de protegerle."),
            ("Lanza de Caballería", "Daño 3", DIF, M2, "", "Solo a la carga. Impacto brutal."),
            ("Cimitarra", "Daño 1", T, AT, "", "+1 a la «defensa pasiva» (parada): se lee como +1 a la tirada de esquiva o parada del portador."),
            ("Látigo de Púas", "Daño 1", T, AT, "[[Efecto: agarrar / derribar]]", "Puede agarrar o derribar en lugar de dañar."),
            ("La Vorpalina (Corta-Dioses)", "Daño: Infinito", T, AN, "[[Malla: Ignora todo]]", "Aprobada expresamente por el autor (T67): «que ignore la malla y sea la corta dioses». Si impacta y no se esquiva, el objetivo queda fuera de combate de un solo golpe, sea un dios, un dragón o una montaña. La decapitación es la narración; la muerte, solo si se pacta {B3}. No se puede tanquear."),
        ]),
        ("Armas a distancia", [
            ("Arco Corto", "Daño 1", T, AT, "", ""),
            ("Arco Largo Élfico", "Daño 2", P, M1, "", "La flecha atraviesa mallas ligeras."),
            ("Ballesta Pesada", "Daño 2", N, M1, "", "El virote es demasiado rápido para esquivarlo: solo te salva la armadura."),
            ("Honda", "Daño 1", T, AT, "", "Munición infinita (piedras)."),
            ("Hachas Arrojadizas", "Daño 1", T, AT, "", "Corto alcance."),
        ]),
        ("Magia y sobrenatural", [
            ("Proyectil Mágico", "Daño 1", N, AN, "", "Perseguidor y etéreo: solo lo paran los escudos mágicos."),
            ("Bola de Fuego", "Daño 3", "Esq: Parcial (área)", M1, "", "La armadura se calienta y quema igualmente. El original decía «si esquivas, te quitas la mitad»; en el canon, Parcial significa que siempre entra al menos 1 punto (ED-9)."),
            ("Rayo Relámpago", "Daño 2", N, "Abs: Nula (Metal)", "", "Valor fuera de la leyenda. Contra quien lleva armadura metálica, el rayo es inevitable (Esq: Nula, Abs: Nula). Sin metal («desnudo»), se puede esquivar: se lee como Esq: Total."),
            ("Toque Vampírico", "Daño 1", T, AN, "", "Atraviesa la armadura. Te curas tantas casillas como daño hagas."),
            ("Aliento de Dragón", "Daño 3", P, AN, "", "Funde la armadura. Tirarse al suelo es la esquiva parcial: el daño baja a 2."),
        ]),
        ("Protección y utilidad", [
            ("Escudo de Torre", "", "", "", "Permite intentar absorber ataques con [[Esq: Nula]] (como las flechas).", ""),
            ("Cota de Malla", "", "", "", "Absorbe hasta 1 punto de daño de armas de filo.", "El tope de la etiqueta Abs del arma atacante sigue mandando."),
            ("Placas Completas", "", "", "", "Absorben hasta 2 puntos de daño físico; −2 a esquivar.", ""),
            ("Capa de Desplazamiento", "", "", "", "Quien te ataca tira con Peor de 2d10 (se queda el dado bajo).", "Defensa mágica. Encaja tal cual en el motor canónico (lectura Peor)."),
            ("Anillo de Invisibilidad", "", "", "", "Eres indetectable; tu primer ataque es siempre sorpresa ([[Esq: Nula]]).", ""),
            ("Botas de Levitación", "", "", "", "Ignoras el terreno difícil y las caídas.", ""),
            ("Gema de Luz", "", "", "", "Ilumina como el día y ciega a las criaturas de la oscuridad.", ""),
            ("Poción de Piel de Piedra", "", "", "", "Tu absorción cuenta como [[Abs: Total]] contra los 3 primeros ataques físicos que recibas.", ""),
            ("Pergamino de Vuelo", "", "", "", "Movimiento en tres dimensiones durante una escena.", ""),
            ("Amuleto Anti-Detección", "", "", "", "Los magos no te detectan.", "El original dice «invisible a la Malla Mística»: se refiere al ámbito Arcano, no a la Rejilla."),
        ]),
    ],
))

# ---------------------------------------------------------------- 2
SETTINGS.append(dict(
    id="bz-neon", title="2. Distopía de Neón (Cyberpunk)",
    lema="Donde la velocidad mata y el blindaje es temporal.", src="T68",
    status="Aprobada (T69)",
    blocks=[
        ("Armas de fuego", [
            ("Pistola Ligera (9 mm)", "Daño 1", T, AT, "[[Malla: Estándar]]", ""),
            ("Pistola Pesada (.44 Magnum)", "Daño 2", T, M1, "", "Te rompe las costillas aunque lleves chaleco."),
            ("Subfusil (SMG)", "Daño 1", "Esq: Parcial (ráfaga)", AT, "", "Con tantas balas, esquivarlo todo es difícil: el original añade −2 a la esquiva (Parcial y Difícil a la vez)."),
            ("Escopeta (Cartucho)", "Daño 3", P, M1, "", "A quemarropa. Si esquivas, te comes la dispersión (1 punto), como marca la esquiva Parcial del canon."),
            ("Rifle de Asalto", "Daño 2", DIF, M1, "", "Alcance medio o largo."),
            ("Rifle de Francotirador (Antimaterial)", "Daño 3", N, AN, "", "Supersónico: si oyes el disparo, ya te ha dado. Atraviesa paredes y blindajes personales. Es el ejemplo canónico de arma inevitable (5.3)."),
            ("Lanzagranadas", "Daño 3", P, M2, "", "De área; la onda expansiva ignora las coberturas."),
            ("Cañón de Riel (Railgun)", "Daño 3", N, AN, "[[Malla: Llave N3]]", "Daña tanques y estructuras."),
            ("Pistola Inteligente (Smart)", "Daño 1", N, AT, "", "Balas teledirigidas: no se esquivan, solo se paran con blindaje."),
            ("Táser / Arma de Choque", "Daño 1 (aturdimiento)", T, "Abs: Nula (Metal)", "", "Valor fuera de la leyenda. Contra quien lleva armadura metálica o ciberimplantes, Abs: Nula y el daño se duplica; en los demás casos se lee como Abs: Total."),
        ]),
        ("Cuerpo a cuerpo (alta tecnología)", [
            ("Cuchillo de Combate", "Daño 1", T, AT, "", ""),
            ("Katana Monofilo", "Daño 2", T, AN, "", "Corta a nivel molecular: ignora el kevlar y las placas cerámicas."),
            ("Martillo Cohete", "Daño 3", FAC, M1, "", "Lento pero devastador."),
            ("Garras Mantis", "Daño 2", T, AT, "", "Ocultas: el primer ataque es sorpresa (ese golpe se lee como Esq: Nula)."),
            ("Nanocable (Látigo)", "Daño 2", DIF, AN, "", "Corta extremidades. Alcance medio."),
        ]),
        ("Tecnología y gadgets", [
            ("Chaleco Kevlar", "", "", "", "Absorbe 1 punto de daño balístico. Inútil contra el monofilo.", ""),
            ("Blindaje Dérmico (implante)", "", "", "", "Tu piel cuenta como armadura: absorbe siempre 1 punto.", ""),
            ("Sandevistan (Dilatador)", "", "", "", "Dos reacciones de esquiva por turno.", "El canon da una reacción por ataque (5.2): esto te deja reaccionar a dos ataques distintos en el mismo turno."),
            ("Camuflaje Termo-Óptico", "", "", "", "[[Esq: Total]] contra ataques a distancia mientras no te muevas.", ""),
            ("Inhibidor de Dolor", "", "", "", "Ignoras los penalizadores por heridas hasta quedar fuera de combate.", "El original decía «hasta que mueres» {B3}."),
            ("Ciberojos", "", "", "", "Anulan los penalizadores por oscuridad o humo.", ""),
            ("Brazo Gorila", "", "", "", "[[Malla: Nivel 2]] Manejas armas pesadas sin penalizador y abres puertas.", "El brazo tiene nivel propio (opera en N2); no es una Llave."),
            ("Granada EMP", "Daño 0 (humanos) / 3 (máquinas)", "Esq: Nula (máquinas)", "Abs: Nula (máquinas)", "", "Contra drones y cíborgs, el original decía «Daño 3 [Inevitable]»: se traduce como Esq: Nula y Abs: Nula {B1}. A los humanos no les hace daño."),
            ("Hielo Negro (virus)", "Daño Mental 2", N, AN, "", "Ataca directamente al cerebro del hacker."),
            ("Exoesqueleto Militar", "", "", "", "[[Malla: Nivel 3]] Te conviertes en un tanque.", "«Sube a Nivel 3»: es Sincronización (2.4); heredas el nivel del traje."),
            ("Inyector de Adrenalina", "", "", "", "Cura al instante 2 casillas de daño superficial.", ""),
            ("Dron de Combate", "", "", "", "Aliado que te da fuego de cobertura.", ""),
            ("Interfaz de Hacking", "", "", "", "Imprescindible para atacar en el plano digital.", ""),
            ("Piernas Reforzadas", "", "", "", "Caes hasta 20 m sin sufrir daño.", ""),
            ("Siroco (droga de combate)", "", "", "", "Mientras dura, tus tiradas de reflejos (esquiva, Atletismo) usan Mejor de 2d10 (Optimismo Alto). Al terminar, sufres Daño Mental 1.", "El original decía «+1 dado a Reflejos»: NOGUM no añade dados ni tiene atributos {B2}."),
        ]),
    ],
))

# ---------------------------------------------------------------- 3
SETTINGS.append(dict(
    id="bz-terror", title="3. Terror Actual (Lovecraft / Zombis)",
    lema="Donde las armas fallan y el miedo mata.", src="T68",
    status="Aprobada (T69)",
    merged="Cóctel Molotov → se conserva en Post-Apocalipsis (T69, versión más reciente).",
    blocks=[
        ("Armas improvisadas", [
            ("Bate de Béisbol", "Daño 1", T, AT, "", "Se rompe con una pifia."),
            ("Hacha de Bombero", "Daño 2", T, AT, "", "Pesada: requiere las dos manos."),
            ("Motosierra", "Daño 3", T, AN, "", "Ruidosa: atrae a más enemigos. Si fallas el ataque, tiras «Suerte» o te hieres a ti mismo. «Suerte» no es una habilidad del canon: el DJ elige la tirada (por ejemplo, Destreza)."),
            ("Escopeta de Caza", "Daño 3", P, AT, "", "Muy corto alcance. Alcanza a 2 objetivos si están juntos."),
            ("Revólver .38", "Daño 1", T, AT, "", "Fiable: no se encasquilla."),
            ("Bengala de Señales", "Daño 1 (fuego)", N, AN, "", "Se clava y quema. Aterroriza a las bestias."),
            ("Cuchillo de Cocina", "Daño 1", T, AT, "", "Muy frágil."),
            ("Coche (atropello)", "Daño 3", P, M1, "[[Malla: Nivel 2]]", "Nivel propio del vehículo (opera en N2)."),
            ("Piedra / Ladrillo", "Daño 1", T, AT, "", ""),
        ]),
        ("Artefactos y magia sucia", [
            ("Libro Maldito", "", "", "", "Permite lanzar hechizos a cambio de Daño Mental al usuario.", ""),
            ("Símbolo Arcano (tiza)", "", "", "", "Barrera que los monstruos de Nivel 1 no pueden cruzar.", "En el banco de ideas de T67 (formato sustituido) bloqueaba hasta Nivel 3."),
            ("Daga Ritual", "Daño 1", "", "", "[[Malla: Llave espiritual]]", "Permite herir a los fantasmas. Valor fuera de la leyenda: es una Llave narrativa contra entidades espirituales. Esq y Abs sin indicar (como cuchillo, el DJ puede darlas por Total)."),
            ("Cámara Fotográfica", "", "", "", "El flash aturde a las criaturas de sombra (pierden el turno).", ""),
            ("Agua Bendita (o Ácido)", "Daño 2", T, AN, "", "Solo afecta a demonios o alienígenas."),
            ("Amuleto de la Abuela", "", "", "", "Una vez por sesión, ignoras 1 punto de Daño Mental.", ""),
            ("Grabadora", "", "", "", "Detecta presencias invisibles (psicofonías).", ""),
            ("Sal", "", "", "", "Barrera contra espíritus.", ""),
            ("Ouija", "", "", "", "Sirve para comunicarse con el más allá, con el riesgo de invocar enemigos.", ""),
            ("Muñeco Vudú", "Daño 1", N, AN, "", "Requiere un enlace (pelo o sangre)."),
        ]),
        ("Equipo de supervivencia", [
            ("Linterna", "", "", "", "Anula los penalizadores por oscuridad. Las pilas se agotan (recurso).", ""),
            ("Botiquín", "", "", "", "Estabiliza a un herido grave; no cura al instante.", "El original dice «a un moribundo»."),
            ("Radio de Onda Corta", "", "", "", "Comunicación precaria.", ""),
            ("Palanca", "Daño 1", "", "", "Bonificador para forzar puertas.", "Como arma, Daño 1 (Esq y Abs sin indicar). La cuantía del bonificador no está fijada."),
            ("Mochila de Suministros", "", "", "", "Permite descansar en zonas inseguras.", ""),
            ("Cuerda", "", "", "", "Bonificador para escalar.", ""),
            ("Mechero", "", "", "", "Luz mínima y fuego.", ""),
            ("Mapa Local", "", "", "", "Te ahorra las tiradas de orientación.", ""),
            ("Alcohol", "", "", "", "Cura estrés (barra Mental), pero da un penalizador físico.", ""),
            ("Anfetaminas", "", "", "", "Ignoras el cansancio durante 1 escena; después, colapso.", ""),
        ]),
    ],
))

# ---------------------------------------------------------------- 4
SETTINGS.append(dict(
    id="bz-opera", title="4. Ópera Espacial (Star Wars / Mass Effect)",
    lema="Donde la tecnología es limpia, los láseres hacen «piu-piu» y la fe mueve naves.", src="T69",
    status="Aprobada (T70)",
    blocks=[
        ("Armas de energía", [
            ("Pistola Bláster", "Daño 2", T, M1, "", "Cauteriza la herida. Inútil contra escudos de energía. Variante {src:T107} «Rifle Bláster» con [[Esq: Parcial]], nunca validada: se conserva la de T69."),
            ("Rifle de Plasma", "Daño 3", P, M1, "", "Bola lenta pero devastadora: si impacta, funde blindajes ligeros. {src:T110} lo repite igual."),
            ("Sable de Luz / Energía", "Daño 3", T, AN, "", "Corta acero, carne y hueso; solo otro campo de energía lo para. Con una pifia te cortas un miembro (consecuencia grave). Igual en {src:T88}, {src:T107} y {src:T110}."),
            ("Cañón de Iones", "Daño 0 (físico) / 3 (escudos)", N, AN, "", "Fríe droides y desactiva escudos personales. No daña la carne. {src:T110} omite Esq y Abs."),
            ("Ballesta Wookiee (energética)", "Daño 3", DIF, M1, "", "Impacto cinético más explosión de energía. Te tira al suelo."),
            ("Rifle Francotirador Láser", "Daño 2", N, AT, "", "Va a la velocidad de la luz y no se esquiva, pero no penetra: lo para un espejo o el humo."),
            ("Granada Térmica", "Daño 3", P, AN, "", "Desintegra en un radio de 5 m. El texto añade «Daño Masivo»; manda la ficha (Daño 3)."),
            ("Lanzarredes Electrificado", "Daño 1 (aturdir)", T, AN, "[[Efecto: incapacita]]", "El objetivo pierde turnos."),
            ("Guantelete de Choque", "Daño 1", T, M1, "", "Cuerpo a cuerpo. Aturde."),
            ("Lanza Vibratoria", "Daño 2", T, M1, "", "Arma noble. Puede parar un sable de luz."),
        ]),
        ("Escudos y trajes", [
            ("Escudo Deflector Personal", "", "", "", "[[Abs: Total]] contra el primer ataque de energía de cada turno; [[Abs: Nula]] contra ataques físicos (cuchillos, puños).", "{src:T107} y {src:T110} lo repiten y añaden que un cuchillo lento lo atraviesa."),
            ("Armadura de Soldado de Asalto", "", "", "", "[[Abs: Total]] contra armas primitivas (flechas, balas); [[Abs: Nula]] contra blásteres.", ""),
            ("Traje de Vacío", "", "", "", "Sobrevives 1 hora en el espacio; te mueves en gravedad cero.", ""),
            ("Jetpack (mochila cohete)", "", "", "", "Movimiento vertical. [[Esq: Fácil (+2)]] mientras vuelas; si te dan, caes (Daño 3).", "El original escribe «[Esq: +2]»."),
            ("Generador de Camuflaje", "", "", "", "Invisibilidad total hasta que atacas. Batería de 3 turnos.", ""),
            ("Botas Magnéticas", "", "", "", "Caminas por el casco de la nave.", ""),
            ("Brazal Escudo", "", "", "", "+1 a la defensa en cuerpo a cuerpo.", "El original dice «Defensa Pasiva»: se lee como +1 a la tirada de esquiva o parada."),
            ("Casco con Visor Táctico", "", "", "", "Marca objetivos; ignoras la cobertura ligera.", ""),
            ("Implante de Traducción", "", "", "", "Entiendes cualquier idioma conocido.", ""),
            ("Capa de Jedi / Sith", "", "", "", "No da armadura; +1 a tiradas sociales o de intimidar.", ""),
        ]),
        ("Poderes (la Fuerza / biótica)", [
            ("Empujón de Fuerza", "Daño 1", DIF, AN, "[[Efecto: derriba y aleja]]", "Si el objetivo choca contra una pared, Daño 2."),
            ("Rayo de la Fuerza", "Daño 2", N, AN, "", "Tortura pura. Paraliza."),
            ("Truco Mental", "Daño Social 2", N, "Abs: Mente", "", "Solo contra masillas. Abs: Mente = se resiste con la barra o la competencia mentales; ignora la esquiva física."),
            ("Salto de Fuerza", "", "", "", "Salto vertical absurdo (20 m).", ""),
            ("Lanzamiento de Sable", "Daño 3", T, AN, "", "El sable va y vuelve. Es un objeto físico, así que se puede esquivar del todo."),
            ("Singularidad (Vórtice)", "", "", "", "Atrae a todos los enemigos a un punto y los deja flotando, indefensos.", ""),
            ("Carga Biótica", "Daño 2", "", "", "Te teletransportas hasta el enemigo e impactas; recuperas escudo.", "Esq y Abs sin indicar."),
            ("Estrangular", "Daño 1 / turno", N, AN, "", "Inevitable: el enemigo levita y se asfixia (daño continuo)."),
            ("Meditación de Batalla", "", "", "", "Durante la escena, todos los aliados hacen sus tiradas con Mejor de 2d10 (Optimismo Alto).", "El original daba «[+1 Dado]» {B2}."),
            ("Fantasma de la Fuerza", "", "", "", "[[Inmortalidad]] Si el personaje sale de la historia, sigue presente como guía narrativo.", "El original decía «si mueres» {B3}."),
        ]),
    ],
    blocknotes={"Poderes (la Fuerza / biótica)": "Se compran como equipo, pero se usan con el ámbito Arcano («El Flujo»; el original dice «Mente/Espíritu»). En T107 y T110 se repiten 111–112, y en T88 se resumen todos sin cambios."},
))

# ---------------------------------------------------------------- 5
SETTINGS.append(dict(
    id="bz-postapo", title="5. Post-Apocalipsis (Mad Max / Fallout)",
    lema="Donde todo está oxidado, sucio y duele mucho.", src="T69",
    status="Aprobada (T70)",
    merged="Escopeta de Dos Cañones (Recortada) → se conserva en Steampunk (T70); Sangre Ácida → se conserva en Horror Gótico (T70).",
    blocks=[
        ("Chatarra mortal", [
            ("Bate con Clavos", "Daño 2", T, M1, "", "Causa tétanos (consecuencia: Infección). Igual en {src:T107} y {src:T110}."),
            ("Rifle de Clavos", "Daño 1", T, AT, "", "Silencioso. Si es el golpe de gracia, clava al enemigo a la pared."),
            ("Ballesta de Resorte (de coche)", "Daño 3", DIF, M1, "", "Dispara varillas de acero. Recarga de 1 turno."),
            ("Lanzallamas Casero", "Daño 2", P, AN, "", "Área cónica. Con una pifia explotas tú (Daño 3). Igual en {src:T107} y {src:T110}."),
            ("Martillo Neumático", "Daño 3", FAC, AN, "", "Ignora las armaduras. Muy pesado: −2 a tu defensa (léase −2 a tus tiradas de esquiva)."),
            ("Sierra Circular de Mano", "Daño 3", T, M1, "", "Ruidosa. Intimidante (+1 a tiradas sociales)."),
            ("Cóctel Molotov", "Daño 2 (fuego)", P, AN, "", "Barato y eficaz. De área: el fuego persiste 1 turno. Duplicado: Terror Actual ({src:T68}) da la misma ficha y el detalle del fuego; se conserva esta versión (T69, la más reciente)."),
            ("Tubo de Plomo", "Daño 1", T, AT, "", ""),
            ("El «Gordo» (lanzabombas)", "Daño: Masivo", P, AN, "", "Mini-bomba nuclear: deja fuera de combate a todo lo que haya en la zona y deja radiación residual. El original decía «mata todo en la zona» {B3}. {src:T110} lo repite."),
        ]),
        ("Vehículos y supervivencia", [
            ("Interceptor V8", "Daño 3 (atropello)", "", "", "[[Malla: Nivel 2]] Blindaje ligero.", ""),
            ("Buggy de Arena", "", "", "", "[[Malla: Nivel 1]] Rápido y sin blindaje: ideal para huir.", ""),
            ("Camión de Guerra", "", "", "", "[[Malla: Nivel 3]] Fortaleza móvil, lenta.", ""),
            ("Armadura de Neumáticos", "", "", "", "[[Abs: Total]] contra golpes contundentes; inútil ([[Abs: Nula]]) contra el fuego.", "Igual en {src:T107} y {src:T110}."),
            ("Armadura de Chapas de Señal", "", "", "", "Absorbe como máximo 1 punto de balas ligeras. Ruidosa: fallo automático en Sigilo.", "El original escribe «[Abs: Máx 1] contra balas ligeras»."),
            ("Contador Geiger", "", "", "", "Pita cerca de las zonas de muerte invisible.", ""),
            ("Máscara de Gas", "", "", "", "Inmune a toxinas en el aire; −1 a Percepción.", "«Percepción» se lee como la disciplina Alerta."),
            ("Pastillas de Yodo", "", "", "", "Limpian 1 casilla de radiación.", ""),
            ("Carne de Perro en Lata", "", "", "", "Restaura 1 casilla de daño físico.", "{src:T107} añade: «Sabe a rayos»."),
            ("Agua Purificada", "", "", "", "«El oro azul». Restaura Mente y Cuerpo.", "Cantidad sin fijar."),
        ]),
        ("Mutaciones y artefactos", [
            ("Brazo Extra", "", "", "", "Sostienes un escudo y un arma a dos manos.", ""),
            ("Piel de Escamas", "", "", "", "Armadura natural: absorbe hasta 1 punto. −2 a tiradas sociales por el aspecto.", "El original escribe «[Abs: 1]» y «−2 Carisma» (NOGUM no tiene atributos)."),
            ("Ojos Brillantes", "", "", "", "Visión nocturna, pero te ven a kilómetros.", ""),
            ("Glándulas de Adrenalina", "", "", "", "En combate tiras con Mejor de 2d10 (Optimismo Alto); después, Daño Mental.", "El original daba «[Motor: Mejor de 2d10]» {B2}."),
            ("Servoarmadura Antigua", "", "", "", "[[Malla: Nivel 3]] Tanque humano. Requiere baterías de fusión.", ""),
            ("Pip-Boy (ordenador de muñeca)", "", "", "", "Mapa automático y diagnóstico de salud.", ""),
            ("Stealth Boy", "", "", "", "Invisibilidad durante 1 minuto. Efecto secundario: paranoia.", ""),
            ("Jet (droga)", "", "", "", "Acciones extra durante 1 turno. Adicción inmediata.", ""),
            ("Mutante Mascota", "", "", "", "PNJ de Nivel 2 que obedece órdenes sencillas.", ""),
        ]),
    ],
))

# ---------------------------------------------------------------- 6
SETTINGS.append(dict(
    id="bz-wuxia", title="6. Wuxia / Anime (Dragon Ball / Tigre y Dragón)",
    lema="Donde gritar te hace más fuerte y la gravedad es opcional.", src="T70",
    status="Aprobada (T70)",
    blocks=[
        ("Artes marciales (técnicas físicas)", [
            ("El Puño de la Estrella del Norte", "Daño 3", N, AN, "", "Puntos de presión: el enemigo queda fuera de combate al final del turno («ya estás muerto»). El original decía «muere» {B3}."),
            ("Patada Huracán", "Daño 1", P, AT, "[[Efecto: área]]", "Golpea a todos los enemigos adyacentes."),
            ("Paso de la Sombra (Shunpo)", "", "Esq: Total", "", "Teletransporte corto: esquiva total automática una vez por combate.", "El original lo etiqueta «[Defensa]». Igual en {src:T107} y {src:T110}."),
            ("Golpe de una Pulgada", "Daño 2", DIF, AN, "", "Rompe costillas a través de la armadura; empuja 5 m. Igual en {src:T107} y {src:T110}."),
            ("Piel de Hierro", "", "", "", "Tu piel cuenta como armadura de placas: absorbe hasta 2 puntos.", "El original la etiqueta «[Defensa Pasiva] [Abs: Máx 2]»."),
            ("Caminar por el Aire", "", "", "", "[[Permiso: Vuelo]] Saltas sobre el aire como si fuera sólido.", "Casi duplicado de «Caminar en el Aire» (Toon, {src:T78}, sin validar: no caes hasta que miras abajo). Se conserva esta versión, la aprobada."),
            ("Corte de Viento (katana)", "Daño 2", P, AT, "", "Ataque a distancia con la espada (onda de vacío)."),
            ("Clon de Sombras", "", "", "", "Creas una copia de ti; cada ataque tiene un 50 % de ir a parar a la copia.", ""),
            ("Puño Borracho", "", "", "", "Tus tiradas usan la tarjeta Gonzo (T5: 1d10; pifia con 1–2, crítico con 9–10), y quien intenta defenderse de ti lo hace con Difícil (−2).", "El original decía «[Motor: Caos Alto]. Tiras 1d10, pero la TN de defensa del enemigo sube +2» {B2}."),
            ("Los Ocho Puntos (Desbloqueo)", "", "", "", "Sufres Daño 1 cada turno, pero todas tus tiradas usan Mejor de 2d10 (Optimismo Alto).", "El original daba «[+1 Dado] a todo» {B2}."),
        ]),
        ("Técnicas de ki / energía", [
            ("Kame Hame Ha (rayo)", "Daño 3", DIF, M1, "", "1 turno de carga gritando. Destruye el terreno. Igual en {src:T107} y {src:T110}."),
            ("Disco Destructor", "Daño 3", T, AN, "", "Corta montañas. Lento pero imparable."),
            ("Bengala Solar (Taiyoken)", "", "", "", "[[Efecto: Ceguera]] Todos los enemigos pierden su siguiente turno.", ""),
            ("Vuelo de Ki", "", "", "", "Vuelo libre a gran velocidad.", ""),
            ("Escudo de Energía", "", "", "", "[[Abs: Total]] contra ataques de ki. Se rompe con daño físico.", ""),
            ("Sentir el Ki", "", "", "", "[[Permiso: Radar]] Detecta enemigos invisibles o tras las paredes.", ""),
            ("Teletransporte Instantáneo", "", "", "", "[[Permiso: Viaje]] A cualquier lugar donde haya una firma de energía conocida.", ""),
            ("Bomba de Energía (Genkidama)", "Daño: Absoluto", "", "", "[[Malla: Nivel 4]] 3 turnos de carga, indefenso. Borra el mapa.", "«(Nivel 4)» se lee como el nivel en el que opera la técnica."),
            ("Transformación (Super)", "", "", "", "Subes 1 nivel de Rejilla de forma temporal. Pelo rubio opcional.", "Igual en {src:T107} y {src:T110}."),
            ("Regeneración Namekiana", "", "", "", "Recuperas 1 bloque de vida si pierdes una extremidad.", ""),
        ]),
        ("Artefactos místicos", [
            ("Nube Kinton", "", "", "", "[[Malla: Nivel 2]] Vehículo volador. Solo para puros de corazón.", ""),
            ("Báculo Sagrado", "Daño 1", "", "", "Cambia de tamaño: alcance infinito.", "Esq y Abs sin indicar."),
            ("Semilla del Ermitaño", "", "", "", "[[Fractal: Reset Total]] Cura al instante toda la vida y la energía. Consumible.", "Igual en {src:T107} y {src:T110}."),
            ("Espada Z", "", "", "", "Pesadísima: entrenar con ella da experiencia extra.", "El capítulo de experiencia está aplazado."),
            ("Pendientes Pothala", "", "", "", "Fusión de dos PJ: suman sus competencias y suben 1 nivel de Rejilla.", "El original dice «stats». El bono total sigue limitado a [−2, +4]."),
            ("Pergamino de Técnica Prohibida", "", "", "", "Enseña una técnica de Nivel 4 a cambio de daño permanente.", "«Daño permanente» se lee como una consecuencia que solo cura otro arco (5.6)."),
            ("Abanico Bancho", "Daño 2 (área)", "", "", "Crea tornados.", "Esq y Abs sin indicar."),
            ("Radar del Dragón", "", "", "", "Localiza objetos de trama (Llaves).", ""),
            ("Armadura Saiyan", "", "", "", "Elástica: absorbe hasta 1 punto ([[Abs: Máx 1]]). No se rompe al transformarte.", ""),
            ("Agua Sagrada", "", "", "", "Convierte una habilidad de +2 en +4, pero beberla causa Daño 3.", ""),
        ]),
    ],
))

# ---------------------------------------------------------------- 7
SETTINGS.append(dict(
    id="bz-gotico", title="7. Horror Gótico (Vampiros / Hombres Lobo)",
    lema="Donde la sangre es moneda y la política es eterna.", src="T70",
    status="Aprobada (entregada en T70; el autor siguió adelante sin objeciones)",
    blocks=[
        ("Poderes de sangre (disciplinas)", [
            ("Garras de la Bestia", "Daño 2", T, AN, "", "Daño agravado: la armadura no para lo sobrenatural. Deja cicatriz permanente. «Agravado» no está en el canon: se lee como una consecuencia que no sigue los plazos normales de curación. Igual en {src:T107}."),
            ("La Mirada (Dominación)", "Daño Mental 2", N, "Abs: Mente", "", "Si entra daño, das una orden sencilla que hay que obedecer."),
            ("Celeridad (Velocidad)", "", "", "", "Una acción extra por turno: atacas dos veces o huyes automáticamente.", "El original daba «[Motor: Acción Extra]» {B2}."),
            ("Piel de Mármol", "", "", "", "Absorbe hasta 2 puntos ([[Abs: Máx 2]]). Las balas rebotan.", "El original la etiqueta «[Defensa Pasiva]»."),
            ("Forma de Niebla", "", "", "", "[[Inmunidad]] [[Abs: Total]] contra todo daño físico; solo te afectan el fuego, el sol o la magia.", "Igual en {src:T107}."),
            ("Presencia Majestuosa", "", "", "", "[[Permiso: Miedo]] Nadie de nivel inferior puede atacarte sin superar antes una tirada Mental.", ""),
            ("Toque de Descomposición", "Daño 1", T, AN, "", "Oxida y rompe al instante objetos y cerraduras."),
            ("Sangre Ácida", "", "", "", "Si te hieren cuerpo a cuerpo, el atacante recibe Daño 1 automático.", "Duplicado: aparece también en Post-Apocalipsis ({src:T69}, Mutaciones) con el mismo efecto. Se conserva esta versión (T70, la más reciente)."),
            ("Salto de Depredador", "", "", "", "[[Permiso: Movimiento]] Saltas 10 m y caes sin daño.", ""),
            ("Invisibilidad Mental (Ofuscación)", "", "", "", "La gente pasa por alto que estás ahí. Se rompe si interactúas.", ""),
        ]),
        ("Armas de cazadores y monstruos", [
            ("Estaca de Madera", "Daño 1", DIF, AT, "", "Con un crítico en el corazón, el vampiro queda paralizado al instante (incapacitado). Igual en {src:T107}."),
            ("Balas de Plata", "", "", "", "[[Llave: licántropos]] Contra hombres lobo, el daño pasa a [[Abs: Nula]] y cuenta como agravado.", "El original decía «convierten el Daño Sucio en Daño Agravado (X)»; «Sucio» era el antiguo Tipo A {B1}. Valor fuera de la leyenda: es una Llave narrativa contra una criatura, no un nivel."),
            ("Lanzallamas Pesado", "Daño 3 (fuego)", P, AN, "", "Obliga a los vampiros a una tirada contra el terror (Rötschreck)."),
            ("Espada Ancestral", "Daño 2", T, M1, "[[Malla: Nivel 3]]", "Puede decapitar: fuera de combate; la muerte, solo si se pacta {B3}. «Malla Nivel 3» se lee como el nivel propio del arma (opera en N3)."),
            ("Escopeta con Aliento de Dragón", "Daño 2 (fuego)", P, M1, "", "Munición incendiaria."),
            ("Ballesta de Mano", "Daño 1", T, AT, "", "Silenciosa."),
            ("Martillo de Guerra (almádena)", "Daño 3", FAC, M1, "", "Rompe huesos que se regeneran."),
            ("Látigo de Cadenas", "Daño 2", T, AT, "[[Efecto: agarrar]]", "Puede agarrar."),
            ("Granada de Fósforo", "Daño 3", P, AN, "", "Arde incluso bajo el agua o sin oxígeno."),
            ("Trampa para Osos", "Daño 2", "", "", "[[Efecto: Inmovilizar]] Velocidad 0.", "Esq y Abs sin indicar."),
        ]),
        ("Artefactos y recursos", [
            ("Bolsa de Sangre Médica", "", "", "", "[[Fractal: Reset Parcial]] Cura 3 casillas a un vampiro; a un humano no le hace nada.", ""),
            ("Elixir de Vitae (sangre de anciano)", "", "", "", "[[Malla: Nivel 3]] Tu nivel de Rejilla pasa a 3 durante una escena, pero quedas vinculado al donante (esclavitud).", ""),
            ("Amuleto Solar", "Daño 3 / turno (vampiros)", "", "", "Luz solar de verdad: daña a todos los vampiros del área.", "Esq y Abs sin indicar."),
            ("Ropa de Diseño con Kevlar", "", "", "", "Parece un traje de alta costura; absorbe hasta 1 punto ([[Abs: Máx 1]]).", "El original cita una marca de moda real."),
            ("Teléfono Desechable", "", "", "", "Indetectable.", ""),
            ("Refugio Seguro (escritura)", "", "", "", "Nadie entra sin invitación.", ""),
            ("Ghouls (criados)", "", "", "", "PNJ de Nivel 1, leales hasta el final.", ""),
            ("Motocicleta Negra", "", "", "", "[[Malla: Nivel 2]] Rápida y sigilosa.", ""),
            ("Cámara de Seguridad Hackeada", "", "", "", "[[Permiso: Información]]", ""),
            ("Ataúd Blindado", "", "", "", "Te permite descansar de día en zonas de guerra.", ""),
        ]),
    ],
))

# ---------------------------------------------------------------- 8
SETTINGS.append(dict(
    id="bz-supers", title="8. Superhéroes (Edad de Plata y cómic moderno)",
    lema="Donde la física es una sugerencia y los calzoncillos se llevan por fuera.", src="T70",
    status="Aprobada (entregada en T70; el autor siguió adelante sin objeciones)",
    blocks=[
        ("Superpoderes (como equipo)", [
            ("Visión Láser / Calorífica", "Daño 2", N, M1, "", "Alcance visual. {src:T107}: «Miras y explota»."),
            ("Superfuerza (Golpe)", "Daño 3", T, AN, "[[Malla: Llave N4]]", "Lanzas coches, rompes tanques. {src:T107} omitía Esq y Abs."),
            ("Vuelo Supersónico", "", "", "", "[[Permiso: Viaje]] Cruzas la ciudad en 1 turno.", ""),
            ("Piel Invulnerable", "", "", "", "[[Abs: Total]] contra el daño físico convencional (Nivel 1–2); solo te dañan las armas pesadas o la magia.", "Igual en {src:T107}."),
            ("Grito Sónico", "Daño 1", P, AN, "[[Efecto: cono, aturde]]", "Rompe cristales y tímpanos."),
            ("Telequinesis", "", "", "", "[[Permiso: Manipulación]] El daño depende de lo que lances.", ""),
            ("Telepatía", "Daño Mental 1", N, "Abs: Mente", "", "Lees los pensamientos superficiales sin tirar; sondear a fondo exige un ataque."),
            ("Intangibilidad (Fase)", "", "", "", "Atraviesas paredes. Inmune al daño físico, pero vulnerable al energético o al místico.", ""),
            ("Regeneración Rápida", "", "", "", "Curas automáticamente 1 casilla por turno.", ""),
            ("Control del Clima (Rayo)", "Daño 3", DIF, AN, "", ""),
        ]),
        ("Gadgets de justiciero", [
            ("Cinturón de Utilidades", "", "", "", "[[Permiso: Solución]] Una vez por sesión sacas justo el objeto que necesitas (espray antitiburones, ganzúa, antídoto).", "Igual en {src:T107}."),
            ("Batarang / Shuriken Explosivo", "Daño 2", T, M1, "", ""),
            ("Capa Planeadora", "", "", "", "Caes desde cualquier altura y planeas.", ""),
            ("Coche Blindado (Batmóvil)", "Daño 3 (armas integradas)", "", "", "[[Malla: Nivel 3]]", ""),
            ("Escudo de Vibranium / Energía", "", "", "", "[[Abs: Total]] e indestructible. Si gastas tu acción en defender, no te pasa nada.", ""),
            ("Visor de Detective", "", "", "", "Escanea huellas, latidos y estructura ósea.", ""),
            ("Pistola de Gancho", "", "", "", "Movimiento vertical rápido; también sirve para desarmar.", ""),
            ("Bombas de Humo Ninja", "", "", "", "Huida automática o ataque por sorpresa.", ""),
            ("Armadura de Combate (Iron)", "Daño 2 (rayos)", "", "", "[[Malla: Nivel 3]] Vuelo, superfuerza y rayos.", ""),
            ("Lazo de la Verdad", "", "", AN, "Si te atrapa (presa), no puedes mentir.", ""),
        ]),
        ("Objetos cósmicos", [
            ("Anillo de Poder", "", "", "", "[[Permiso: Creación]] Crea objetos de luz sólida que duran mientras te concentres.", ""),
            ("Cubo Cósmico (fragmento)", "", "", "", "Altera la realidad local: mientras actúa, las tiradas de la escena usan la tarjeta Gonzo (Caos Alto). Peligroso.", "El original daba «[Motor: Caos Alto]» {B2}."),
            ("Suero de Supersoldado", "", "", "", "Capacidades físicas al máximo humano (+4).", "NOGUM no tiene atributos: se lee como +4 en las tiradas físicas (el tope canónico)."),
            ("Cristal de Kriptonita", "", "", "", "[[Llave: debilidad]] Anula los poderes del héroe invulnerable y baja su nivel de Rejilla a 1.", "Es el ejemplo canónico de Llave (2.3)."),
            ("Casco Místico", "", "", "", "Inmune a la telepatía.", ""),
            ("Martillo Digno", "Daño 3", "", "", "[[Malla: Nivel 4]] Solo lo levanta quien el DJ decida. Vuelve a la mano.", "Esq y Abs sin indicar."),
            ("Gema del Infinito (una sola)", "Daño: Infinito", "", "", "Usarla te causa Daño 3.", "Esq y Abs sin indicar."),
            ("Capa de Levitación", "", "", "", "Tiene personalidad propia y te defiende sola.", ""),
            ("Reactor de Pecho", "", "", "", "Fuente de energía inagotable.", ""),
            ("Simbionte Alienígena", "", "", "", "Da poderes físicos, a cambio de Daño Mental constante (corrupción).", ""),
        ]),
    ],
))

# ---------------------------------------------------------------- 9
SETTINGS.append(dict(
    id="bz-steampunk", title="9. Steampunk / Weird West (Deadlands)",
    lema="Donde el vapor quema, los revólveres tienen 6 tiros y los fantasmas son reales.", src="T70",
    status="Aprobada (entregada en T70; el autor siguió adelante sin objeciones)",
    blocks=[
        ("Armas de pólvora y vapor", [
            ("Revólver «Pacificador» (.45)", "Daño 2", T, M1, "", "6 balas."),
            ("Rifle Winchester", "Daño 2", T, AT, "", "De palanca. Alcance largo."),
            ("Escopeta de Dos Cañones", "Daño 3", P, AT, "", "A quemarropa. Duplicado: Post-Apocalipsis ({src:T69}) la llama «(Recortada)», con la misma ficha y «si fallas el ataque por 1, se encasquilla». {src:T107} y {src:T110} la llaman «Escopeta Recortada» y cambian a «pifia = se encasquilla» (sin validar). Se conserva esta versión (T70, la más reciente aprobada)."),
            ("Gatling de Vapor (portátil)", "Daño 3", "Esq: Parcial (área)", M1, "", "Nube de plomo. Tarda 1 turno en girar el cañón. Igual en {src:T107}."),
            ("Rifle Tesla (Voltaico)", "Daño 2", N, "Abs: Nula (Metal)", "", "Arco eléctrico que salta entre objetivos metálicos. Valor fuera de la leyenda: contra objetivos con metal, Abs: Nula; sin metal, se lee como Abs: Total. Igual en {src:T107}."),
            ("Pistola de Clavos a Presión", "Daño 1", T, AT, "", "Silenciosa."),
            ("Cañón de Mano", "Daño 3", FAC, M1, "", "Un solo tiro. Puede romperte la muñeca."),
            ("Cuchillo Bowie", "Daño 1", T, AT, "", ""),
            ("Dinamita", "Daño 3", P, AN, "", "Mecha corta. Inestable."),
            ("Lanzallamas de Queroseno", "Daño 2", P, AN, "", "Mochila pesada."),
        ]),
        ("Inventos de ciencia extraña", [
            ("Brazo Mecánico a Vapor", "Daño 2", "", "", "[[Rejilla: Físico +1]] Requiere carbón.", "Mientras funciona, sube un nivel tu Rejilla en el ámbito Físico. Esq y Abs del golpe sin indicar."),
            ("Monóculo de Análisis", "", "", "", "Ves el flujo de la magia y a los fantasmas.", ""),
            ("Jetpack de Vapor", "", "", "", "Salto enorme; si fallas el aterrizaje, te quemas las piernas (Daño 1).", ""),
            ("Araña Mecánica Espía", "", "", "", "Control remoto por cable.", ""),
            ("Chaleco Voltaico", "", "", "", "Si te tocan cuerpo a cuerpo, descarga Daño 1.", ""),
            ("Botas de Resorte", "", "", "", "Saltas 3 m, con riesgo de caída.", ""),
            ("Inyector de Tónico", "", "", "", "Cura instantánea o dopaje: tu siguiente tirada usa Mejor de 2d10 (Optimismo Alto).", "El original daba «dopaje (+1 Dado)» {B2}."),
            ("Guantelete Magnético", "", "", "", "Atrae el arma del enemigo (desarme).", ""),
            ("Respirador de Carbón", "", "", "", "Inmune a los gases tóxicos.", ""),
            ("Sierra Mecánica de Combate", "Daño 3", T, M1, "", "Atraviesa puertas."),
        ]),
        ("Ocultismo y póker", [
            ("Baraja de Cartas Maldita", "Daño 1 (mágico)", "", "", "Lanzas una carta cortante.", "El original escribe «Daño Mágico 1». Esq y Abs sin indicar."),
            ("Roca Fantasma (combustible)", "", "", "", "Los inventos que la queman hacen sus tiradas con Mejor de 2d10 (Optimismo Alto), pero atrae a los demonios.", "El original daba «[Motor: +1 Dado]» {B2}."),
            ("Amuleto de Chamán", "", "", "", "[[Abs: Total]] contra ataques espirituales.", ""),
            ("Bala Bendita", "", "", "", "[[Llave: demonios]] Contra demonios, el daño pasa a [[Abs: Nula]] y cuenta como agravado.", "{src:T107}: «convierte el Daño Sucio en Agravado contra seres oscuros». «Sucio» era el antiguo Tipo A {B1}. Valor fuera de la leyenda: es una Llave narrativa contra una criatura."),
            ("Elixir de Aceite de Serpiente", "", "", "", "Cura o envenena (50 %).", ""),
            ("Mano del Hombre Muerto", "", "", "", "Si el personaje sale de la historia con ella en el bolsillo, vuelve como Resucitado (un zombi inteligente).", "El original decía «si mueres con ella» {B3}."),
            ("Lazo Espiritual", "", "", "", "Atrapa fantasmas.", ""),
            ("Tótem Animal", "", "", "", "Te da una habilidad animal a +2 de forma temporal.", ""),
            ("Reloj de Bolsillo Hipnótico", "Daño Mental 1", "", "", "[[Efecto: aturde]]", "Esq y Abs sin indicar."),
            ("Escopeta Exorcista", "", "", "", "Con inscripciones sagradas: repele a los demonios.", ""),
        ]),
    ],
))

# ---------------------------------------------------------------- 10
SETTINGS.append(dict(
    id="bz-toon", title="10. Comedia / Toon (Toon Force)",
    lema="Donde el daño aplasta pero no mata.", src="T78", proposal=True,
    status="Propuesta sin validar",
    merged="Caminar en el Aire → se conserva «Caminar por el Aire» en Wuxia / Anime (T70, aprobada).",
    intro="El autor no llegó a elegir entre Comedia/Toon y Espionaje Realista (T71). El asistente entregó Toon en T78 con 20 ítems (271–290) y dijo que eran «300 clavados», pero nunca llegaron los 10 que faltaban.",
    blocks=[
        ("Armas de tienda de bromas", [
            ("El Yunque (Caída)", "Daño 3", FAC, AN, "", "Te deja como un acordeón (consecuencia: Plano)."),
            ("Mazo Gigante de Madera", "Daño 2", T, AT, "", "Chichones instantáneos."),
            ("Dinamita con Mecha Larga", "Daño 3", P, AN, "", "Siempre explota justo cuando vas a mirar por qué no ha explotado."),
            ("Guante de Boxeo con Muelle", "Daño 1", "Esq: Sorpresa", M1, "", "Sale de cajas pequeñas y empuja 10 m. Valor fuera de la leyenda: si pilla al objetivo desprevenido, se lee como Esq: Nula; si ya lo conoce, como Esq: Total."),
            ("Tarta en la Cara", "Daño 0", "", "", "[[Efecto: Ceguera + Humillación]]", "Daña la dignidad (el original dice «Espíritu»). Con ED-11, la humillación iría a la barra Mental."),
            ("Escopeta Anudada", "Daño de retorno", "", "", "Si disparas, el tiro te da a ti.", "Valor fuera de la leyenda: el daño del arma se lo lleva quien dispara."),
            ("Bomba Redonda Negra", "Daño 3", P, "", "Te deja la cara negra y el pelo hacia atrás.", "Abs sin indicar."),
            ("Sierra de Suelo", "Daño: Caída", "", "", "Recortas un círculo alrededor del enemigo, que cae al vacío.", "Valor fuera de la leyenda: el daño es el de la caída (de 1 a 3 según la altura, 5.3)."),
            ("Cohete a la Espalda", "", "", "", "Vas muy rápido y sin controlar la dirección: las tiradas para dirigirlo usan la tarjeta Gonzo (Caos Alto).", "El original daba «[Motor: Caos Alto]» {B2}."),
            ("Túnel Pintado", "", "", "", "[[Efecto: Muro]] Tú pasas; tu perseguidor se estampa contra la pared.", ""),
        ]),
        ("Poderes toon", [
            ("Espacio en los Bolsillos", "", "", "", "Sacas cualquier objeto que tenga gracia en la escena.", ""),
            ("Disfraz Instantáneo", "", "", "", "Te disfrazas de mujer o de abuela en 1 segundo. Engaña a cualquiera de nivel de Rejilla inferior.", ""),
            ("Cuerpo de Goma", "", "", "", "[[Inmunidad: contundente]] Las balas rebotan y los golpes te estiran.", ""),
            ("Regeneración de Escena", "", "", "", "En la escena siguiente estás curado y limpio.", ""),
            ("Salir del Plano", "", "", "", "Te sales de la película y borras al enemigo con una goma.", ""),
            ("Inmortalidad Cómica", "", "", "", "[[Inmortalidad]] Nunca sales de la historia: si quedas fuera de combate, te salen alas y tocas el arpa un rato, y luego vuelves.", "El original decía «nunca mueres» {B3}."),
            ("Ojos Saltones", "", "", "", "Bonificador a Percepción al ver a una chica guapa.", "«Percepción» se lee como la disciplina Alerta."),
            ("Bajar la Cremallera", "", "", "", "Te quitas el «disfraz» de personaje y eres otro.", ""),
            ("Cartel de «Socorro»", "", "", "", "Acción gratuita para comunicarte con el público.", ""),
        ]),
    ],
))

SOCIAL = dict(
    id="bz-social", title="El Duelo Social (intriga cortesana)",
    lema="Donde la lengua corta más que la espada.", src="T78", proposal=True,
    status="Propuesta sin validar",
    blocks=[
        ("Arsenal social", [
            ("El Rumor Sutil", "Daño Social 1", T, AT, "", "Funciona como una daga: la buena reputación lo absorbe y la astucia lo desvía."),
            ("El Insulto Público", "Daño Social 2", P, M1, "", "Funciona como una espada larga: siempre entra algo de humillación, aunque tengas estatus."),
            ("El Chantaje (la Prueba)", "Daño Social 3", N, AN, "", "Un disparo de francotirador: tienen las fotos. Consecuencia grave: «Chantajeado». En {src:T72} el ejemplo era [[Daño Social 2]] [[Esq: Nula]] [[Abs: Reputación]]; se conserva la versión de T78, más reciente."),
            ("La Verdad Cósmica", "Daño Mental 3", N, AN, "", "Ataque mental inevitable. El original la llamaba «ataque mental de Tipo C» {B1}."),
            ("La Orden de Mando (Voz de Alfa)", "Daño Social 1", DIF, "Abs: Voluntad", "", "Ataca la autonomía. Abs: Voluntad = se resiste con la competencia mental."),
            ("Seducción Agresiva", "Daño Social 1", T, AN, "", "Ataca al deseo e ignora la armadura lógica."),
            ("Luz de Gas (Gaslighting)", "Daño Mental 1 / turno", "", "", "[[Fractal: Mente]]", "Daño continuo, turno a turno, que erosiona la cordura."),
            ("Excomunión / Destierro", "Daño: Masivo (Espiritual)", "", "", "Bomba nuclear social: el personaje sale de la historia en ese ámbito (socialmente, queda fuera de juego).", "El original decía «[Daño Masivo: Espíritu]… muerte del PJ en ese ámbito» {B3}."),
        ]),
    ],
)

# ------------------------------------------------------------------ render
def count(s):
    return sum(len(b[1]) for b in s["blocks"])

def render_setting(s, h3_extra=""):
    o = []
    flag = " " + FLAGS["PROP"] if s.get("proposal") else ""
    n = count(s)
    pend = ""
    if s["id"] != "bz-social" and n < 30:
        pend = ' <span class="flag pending">Pendiente</span>'
    o.append('<h3 id="%s">%s%s%s</h3>' % (s["id"], s["title"], flag, pend))
    o.append('<p><em>«%s»</em> <span class="src">%s</span></p>' % (html.escape(s["lema"], quote=False), s["src"]))
    if s.get("intro"):
        o.append("<p>%s</p>" % md(s["intro"]))
    if pend:
        o.append("<p>Esta ambientación tiene <strong>%d ítems</strong>: <strong>faltan %d</strong> para los 30.%s</p>" % (
            n, 30 - n, (" Ítems fusionados con otra ambientación: " + md(s["merged"])) if s.get("merged") else ""))
    for title, rows in s["blocks"]:
        o.append("<h4>%s</h4>" % html.escape(title, quote=False))
        bn = s.get("blocknotes", {}).get(title)
        if bn:
            o.append("<p>%s</p>" % md(bn))
        o.append(table(rows))
    return "\n".join(o)

parts = []
parts.append('<section class="chapter" id="apx-bazar">')
parts.append("<h2>8.3 El Bazar del Multiverso</h2>")
parts.append("""<p>Este apéndice es material de <strong>consulta</strong>, no de estudio. Es el <em>gear porn</em> de NOGUM: un escaparate de armas, armaduras, poderes y cachivaches de diez ambientaciones, más un arsenal social. Nadie tiene que memorizarlo. Ábrelo cuando necesites un arma para un PNJ, cuando un jugador pregunte «¿y esto qué hace?» o cuando quieras ver cómo suena tu género en números.</p>
<p>Las fichas técnicas son muletas didácticas: enseñan el tono mejor que la teoría. Que un Sable de Luz lleve <span class="tag">Abs: Nula</span> y un Rifle de Plasma <span class="tag">Abs: Máx 1</span> explica la ópera espacial más rápido que tres páginas de ensayo. Un arma no se define por su precio, sino por cómo dobla las reglas: ¿se puede esquivar?, ¿sirve de algo la armadura?, ¿alcanza a quien está por encima en la Rejilla?</p>
<aside class="meta"><p>Ojo, editor: casi todas las ambientaciones y muchos objetos llevan nombres de marcas y franquicias reales (D&amp;D, Conan, Cyberpunk, Star Wars, Mass Effect, Wookiee, Jedi/Sith, Mad Max, Fallout, Pip-Boy, Stealth Boy, Jet, Dragon Ball, Kame Hame Ha, Genkidama, Taiyoken, Nube Kinton, Semilla del Ermitaño, Saiyan, Namekiana, Pothala, Abanico Bancho, Espada Z, Shunpo, Estrella del Norte, Tigre y Dragón, Sandevistan, Rötschreck, Batmóvil, Batarang, Kriptonita, Vibranium, Iron, Deadlands, Roca Fantasma, Toon Force, la Vorpalina…). Antes de publicar hay que <strong>limar los números de serie</strong>: cambiarlos por eufemismos transparentes, como en El Camaleón. Aquí se conservan para que se reconozca la fuente.</p></aside>""")

parts.append('<h3 id="bz-lectura">Cómo leer la ficha técnica</h3>')
parts.append("""<p>Cada objeto describe con etiquetas explícitas qué hace con el daño, la esquiva, la absorción y la Rejilla. No hay «tipos» con nombre. Resumen del Capítulo 5 (5.3):</p>
<dl>
<dt><span class="tag">Daño 0–3</span></dt>
<dd>Puntos que tacha el golpe si entra limpio: 1 = leve («urgencias»), 2 = serio («UCI»), 3 = masivo («a comer con San Pedro»). Especiales: <span class="tag">Daño: Masivo</span>, <span class="tag">Daño: Absoluto</span>, <span class="tag">Daño: Infinito</span>, <span class="tag">Daño Mental N</span> y <span class="tag">Daño Social N</span> (con ED-11, el daño social va a la barra Mental salvo que la campaña cree una barra propia). Si el atacante saca un crítico, +1 al daño.</dd>
<dt><span class="tag">Esq</span></dt>
<dd>Lo que permite la reacción de esquivar. <strong>Total</strong>: la reducción puede dejar el daño en 0. <strong>Parcial</strong> (área, ráfagas, fuego): aunque mitigues, recibes al menos 1 punto. <strong>Nula</strong>: no se puede esquivar. <strong>Difícil (−2)</strong> y <strong>Fácil (+2)</strong> modifican la tirada de esquiva (ED-10).</dd>
<dt><span class="tag">Abs</span></dt>
<dd>Lo que permite la armadura. <strong>Total</strong>: puede anular todo el daño. <strong>Máx N</strong>: reduce como mucho N puntos. <strong>Nula</strong>: la armadura no sirve. Especiales: <strong>Mente</strong>, <strong>Voluntad</strong> y <strong>Reputación</strong>, que se resisten con la barra o la competencia mental o social.</dd>
<dt><span class="tag">Malla</span></dt>
<dd>Relación con la Rejilla de Potencia. <strong>Estándar</strong>: no afecta a niveles superiores; es el valor por defecto cuando la ficha no dice nada. <strong>Llave N</strong>: puede dañar hasta el nivel N. <strong>Nivel N</strong>: el objeto opera en ese nivel (vehículos, servoarmaduras; si lo pilotas, Sincronización). <strong>Ignora todo</strong>: solo la Vorpalina.</dd>
</dl>
<p>Recordatorio del procedimiento (5.2): el atacante tira contra la TN de la tarjeta activa. Si conecta, el defensor hace <strong>una</strong> reacción (esquivar o absorber, la vía que permita el arma): con éxito resta 1 y con crítico resta 2, siempre dentro de los límites de la etiqueta. En la columna «Malla / Efecto» van también las etiquetas de uso: <span class="tag">Permiso</span> (hace posible lo imposible), <span class="tag">Fractal</span> (cura o afecta a una barra), <span class="tag">Efecto</span>, <span class="tag">Inmunidad</span> y <span class="tag">Llave: criatura</span> (Llave narrativa contra un tipo de ser). Un «—» significa que el dato no aplica o que la fuente no lo da.</p>
<div class="rule"><p class="rule-title">Decisiones editoriales de este apéndice</p>
<ul>
<li><span class="flag ed">ED-B1</span> Las etiquetas descartadas en T68 (Tipo A/B/C, Sucio/Letal/Absoluto, [VELOZ], [LETAL], [ÁREA], [INEVITABLE]) se traducen al formato explícito: Tipo A → <span class="tag">Esq: Total</span> <span class="tag">Abs: Total</span>; Tipo B → <span class="tag">Abs: Máx 1</span>; Tipo C / «Inevitable» → <span class="tag">Esq: Nula</span> <span class="tag">Abs: Nula</span>. «Convertir el daño Sucio en Agravado» pasa a ser «el daño pasa a Abs: Nula».</li>
<li><span class="flag ed">ED-B2</span> «[+1 Dado]» no existe en el canon: NOGUM nunca añade dados. Se traduce como «la tirada usa Mejor de 2d10 (Optimismo Alto)» para la acción o el periodo que indique el objeto. Las demás etiquetas [Motor] se traducen igual: «Motor: Mejor de 2d10» es esa misma lectura; «Motor: Caos Alto» significa usar la tarjeta Gonzo (T5); «Motor: Acción Extra» se reescribe como efecto (una acción más por turno).</li>
<li><span class="flag ed">ED-B3</span> Ningún objeto mata por reglas (5.5). Donde la fuente decía «si mueres», «mata» o «muere», se lee «si el personaje sale de la historia» o «queda fuera de combate». La muerte solo ocurre si se pacta narrativamente.</li>
<li>Duplicados y variantes: se conserva la versión aprobada más reciente, y la otra se anota en «Notas». Los ítems fusionados solo cuentan una vez, así que algunas ambientaciones bajan de 30.</li>
<li>Los valores fuera de la leyenda ([Esq: Sorpresa], [Esq: Total (Lento)], [Abs: Nula (Metal)], [Abs: Nula en huecos], [Daño: Caída], [Daño de retorno], [Llave: criatura]…) se conservan tal cual, y la columna «Notas» explica cómo se interpretan.</li>
<li>No se incluye el banco de ideas del primer catálogo (T67), porque su formato de etiquetas quedó sustituido en T68.</li>
</ul></div>""")

total = 0
summary = []
for s in SETTINGS:
    parts.append(render_setting(s))
    n = count(s)
    total += n
    summary.append((s, n))

# social
parts.append(render_setting(SOCIAL))
parts.append("<p>Estas armas no entran en la cuenta de 300: el Duelo Social funciona como una ambientación extra. En la tabla, T78 escribía «[Daño N]» a secas; como es un arsenal social, se lee como <span class=\"tag\">Daño Social N</span> (o <span class=\"tag\">Daño Mental N</span> cuando el ataque es a la cordura). Los flecos de T72 pedían entre 10 y 20 armas sociales y aquí hay 8: <span class=\"flag pending\">Pendiente</span> faltan al menos 2.</p>")
nsoc = count(SOCIAL)

# summary table
parts.append('<h3 id="bz-resumen">Resumen del catálogo</h3>')
rows = ['<div class="tw"><table class="t">',
        "<thead><tr><th>Ambientación</th><th>Nº de ítems</th><th>Estado</th></tr></thead>", "<tbody>"]
for s, n in summary:
    st = html.escape(s["status"], quote=False)
    if s.get("proposal"):
        st = FLAGS["PROP"]
    if n < 30:
        st += ' <span class="flag pending">Pendiente</span> faltan %d' % (30 - n)
    if s.get("merged"):
        st += " (fusiones: " + md(s["merged"]) + ")"
    rows.append('<tr><td>%s</td><td class="num">%d</td><td>%s</td></tr>' % (s["title"], n, st))
rows.append('<tr><td>El Duelo Social (extra)</td><td class="num">%d</td><td>%s <span class="flag pending">Pendiente</span> faltan al menos 2 para las 10–20 que pedían los flecos de T72</td></tr>' % (nsoc, FLAGS["PROP"]))
rows.append('<tr><td><strong>Total</strong></td><td class="num"><strong>%d</strong></td><td>%d en las 10 ambientaciones + %d sociales. La conversación daba 290 + 8; se han fusionado %d duplicados (Cóctel Molotov, Escopeta de Dos Cañones, Sangre Ácida, Caminar en el Aire). Hasta 300 faltan %d.</td></tr>' % (total + nsoc, total, nsoc, 290 - total, 300 - total))
rows.append("</tbody></table></div>")
parts.append("\n".join(rows))
parts.append("</section>")

with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(parts) + "\n")

for s, n in summary:
    print(s["id"], n)
print("bz-social", nsoc)
print("TOTAL", total, "+", nsoc, "=", total + nsoc)
