# -*- coding: utf-8 -*-
"""NOGUM - Sala de Máquinas: probabilidades exactas por enumeración.

Reglas según CANON.md §2 (ED-1: pifia y crítico NATURALES, con prioridad sobre el total).
Uso:  python nogum_math.py          -> imprime tablas y comprobaciones
      python nogum_math.py --html   -> además escribe frag_math.html
"""
import itertools
import os
import sys
from fractions import Fraction as F

D = range(1, 11)
ONE = [(x,) for x in D]                       # 10 combinaciones
TWO = list(itertools.product(D, D))           # 100 combinaciones
BONOS = [-2, -1, 0, 1, 2, 3, 4]
PERFILES = [(-2, "Nulidad"), (0, "Novato"), (2, "Profesional"), (4, "Gran Maestro")]
CATS = ["pifia", "fallo", "parcial", "exito", "critico"]

rojo = lambda r: r[0]
mejor = max
peor = min
suma = sum


def bandas_tn(tn):
    return lambda t: "exito" if t >= tn else "fallo"


def bandas_pulp(t):            # T3 / Pulp Desatado: <=5 fallo, 6-7 parcial, >=8 éxito
    return "fallo" if t <= 5 else ("parcial" if t <= 7 else "exito")


def bandas_thriller(t):        # TN 6; fallar por 1-2 (total 4-5) = éxito con coste
    return "exito" if t >= 6 else ("parcial" if t >= 4 else "fallo")


# id: (nombre, tirada, lectura, pifia(nat), crítico(nat), bandas(total), texto regla, tn)
CARDS = {
    "T0": ("Estándar / Aventura Clásica", ONE, rojo, lambda r: r[0] == 1, lambda r: r[0] == 10,
           bandas_tn(6), "1d10 (rojo) + bono vs TN 6; pifia 1 natural; crítico 10 natural", 6),
    "T1": ("Héroe", TWO, mejor, lambda r: r == (1, 1), lambda r: max(r) == 10,
           bandas_tn(6), "mejor de 2d10 + bono vs TN 6; pifia doble 1; crítico cualquier 10", 6),
    "T2": ("Realista", TWO, suma, lambda r: sum(r) <= 3, lambda r: sum(r) >= 19,
           bandas_tn(11), "suma 2d10 + bono vs TN 11; pifia suma natural 2–3; crítico suma natural 19–20", 11),
    "T3": ("Pulp / Drama", ONE, rojo, lambda r: r[0] == 1, lambda r: r[0] == 10,
           bandas_pulp, "1d10 (rojo) + bono; total ≤5 fallo, 6–7 parcial, ≥8 éxito; pifia 1 nat.; crítico 10 nat.", 6),
    "T4": ("Terror", TWO, peor, lambda r: min(r) == 1, lambda r: r == (10, 10),
           bandas_tn(6), "peor de 2d10 + bono vs TN 6; pifia cualquier 1; crítico doble 10", 6),
    "T5": ("Gonzo", ONE, rojo, lambda r: r[0] <= 2, lambda r: r[0] >= 9,
           bandas_tn(6), "1d10 (rojo) + bono vs TN 6; pifia 1–2 nat.; crítico 9–10 nat.", 6),
    "T6": ("Tragedia", TWO, suma, lambda r: sum(r) <= 3, lambda r: sum(r) >= 19,
           bandas_tn(14), "suma 2d10 + bono vs TN 14; pifia suma natural 2–3; crítico suma natural 19–20", 14),
}
RECETAS = {
    "EC": ("Épica Clásica", TWO, mejor, lambda r: r == (1, 1), lambda r: max(r) == 10,
           bandas_tn(6), "mejor de 2d10 + bono vs TN 6; pifia doble 1; crítico cualquier 10", 6),
    "PD": ("Pulp Desatado", TWO, mejor, lambda r: r == (1, 1), lambda r: max(r) == 10,
           bandas_pulp, "mejor de 2d10 + bono; total ≤5 fallo, 6–7 parcial, ≥8 éxito; pifia doble 1; crítico cualquier 10", 6),
    "TS": ("Thriller de Supervivencia", TWO, peor, lambda r: min(r) == 1, lambda r: r == (10, 10),
           bandas_thriller, "peor de 2d10 + bono vs TN 6; total 4–5 = éxito con coste; pifia cualquier 1; crítico doble 10", 6),
    "PS": ("Pesadilla / Slasher", TWO, peor, lambda r: min(r) == 1, lambda r: r == (10, 10),
           bandas_tn(6), "peor de 2d10 + bono vs TN 6; pifia cualquier 1; crítico doble 10", 6),
}
ALL = {**CARDS, **RECETAS}


def probs(key, bono):
    _, rolls, lect, pif, crit, band, _, _ = ALL[key]
    c = dict.fromkeys(CATS, 0)
    for r in rolls:
        if pif(r):
            c["pifia"] += 1
        elif crit(r):
            c["critico"] += 1
        else:
            c[band(lect(r) + bono)] += 1
    n = len(rolls)
    p = {k: F(100 * v, n) for k, v in c.items()}
    assert sum(p.values()) == 100, (key, bono, p)
    p["total"] = p["exito"] + p["parcial"] + p["critico"]
    return p


LECTURAS = [("1d10 (rojo)", ONE, rojo, range(1, 11)), ("Mejor de 2d10", TWO, mejor, range(1, 11)),
            ("Peor de 2d10", TWO, peor, range(1, 11)), ("Suma 2d10", TWO, suma, range(2, 21))]


def distribucion(rolls, lect, vals):
    n = len(rolls)
    d = {v: F(100 * sum(1 for r in rolls if lect(r) == v), n) for v in vals}
    assert sum(d.values()) == 100
    return d


def media(rolls, lect):
    return F(sum(lect(r) for r in rolls), len(rolls))


def fmt(x):
    x = F(x)
    return str(int(x)) if x.denominator == 1 else f"{float(x):.2f}".rstrip("0").replace(".", ",")


def sb(b):
    return f"+{b}" if b >= 0 else f"−{-b}"


# --- Referencias externas (para el texto) ---
def referencias():
    d20 = list(itertools.product(range(1, 21), repeat=2))
    ref = {}
    ref["d20_ventaja_media"] = F(sum(max(r) for r in d20), 400)
    ref["d20_desventaja_media"] = F(sum(min(r) for r in d20), 400)
    ref["d20_ventaja_pifia"] = F(100, 400)
    d6 = list(itertools.product(range(1, 7), repeat=2))
    ref["pbta_fallo"] = F(100 * sum(1 for r in d6 if sum(r) <= 6), 36)
    ref["pbta_parcial"] = F(100 * sum(1 for r in d6 if 7 <= sum(r) <= 9), 36)
    ref["pbta_exito"] = F(100 * sum(1 for r in d6 if sum(r) >= 10), 36)
    t3 = list(itertools.product(range(1, 7), repeat=3))
    ref["gurps_10_11"] = F(100 * sum(1 for r in t3 if sum(r) in (10, 11)), 216)
    ref["gurps_extremos"] = F(100 * sum(1 for r in t3 if sum(r) in (3, 18)), 216)
    fd = list(itertools.product((-1, 0, 1), repeat=4))
    ref["fate_0"] = F(100 * sum(1 for r in fd if sum(r) == 0), 81)
    ref["fate_4"] = F(100 * sum(1 for r in fd if abs(sum(r)) == 4), 81)
    ref["suma_11"] = distribucion(TWO, suma, range(2, 21))[11]
    return ref


# --- Verificación de cifras citadas en la conversación ---
def p_suma_ge(k):
    return F(100 * sum(1 for r in TWO if sum(r) >= k), 100)


def correcciones():
    """(cifra citada, turno, valor correcto, comentario, ¿errónea?)"""
    c = []
    c.append(("P(sacar 11 con 2d10) «casi un 20 %»", "T15", fmt(referencias()["suma_11"]) + " %", "", True))
    c.append(("Realista +2 vs TN 11: 64 %", "T20, T23", fmt(probs("T2", 2)["total"]) + " %", "necesita suma natural ≥ 9", True))
    c.append(("Suma vs 14, +4: 55 %", "T20", fmt(p_suma_ge(10)) + " %", "necesita ≥ 10", True))
    c.append(("Suma vs 14, +2: 28 %", "T20", fmt(p_suma_ge(12)) + " %", "necesita ≥ 12", True))
    c.append(("Suma vs 14, −2: 10 %", "T20", fmt(p_suma_ge(16)) + " %", "necesita ≥ 16", True))
    c.append(("Tragedia (TN 13) +4: 64 % y +2: 45 %", "T23", f"TN 13: {fmt(p_suma_ge(9))} % y {fmt(p_suma_ge(11))} %",
              f"con la TN 14 canónica (T30) salen {fmt(probs('T6', 4)['total'])} % y {fmt(probs('T6', 2)['total'])} %, así que las cifras citadas son válidas para la tarjeta vigente", True))
    c.append(("Tragedia −2: 10 %", "T23", f"{fmt(probs('T6', -2)['total'])} % (TN 14)", f"con TN 13 sería {fmt(p_suma_ge(15))} %", True))
    c.append(("Suma +0 vs TN 11: 50 %", "T29", fmt(probs("T2", 0)["total"]) + " %", "P(suma ≥ 11)", True))
    c.append(("Crítico del Gran Maestro en suma (margen de 4): 36 %", "T30", fmt(p_suma_ge(12)) + " %",
              "36 % es P(≥ 13); la Regla del Margen está retirada (ED-1)", True))
    c.append(("Crítico de Fantasía de Poder (mejor de 2): 1 %", "T130", fmt(probs("T1", 2)["critico"]) + " %", "corregido por el autor en T131", True))
    c.append(("Comedia Negra +2: éxito normal 40 %", "T130", fmt(probs("T5", 2)["exito"]) + " %",
              f"tiradas 4–8; el fallo normal (tirada 3) es {fmt(probs('T5', 2)['fallo'])} %", True))
    c.append(("Terror Purista: pifia 10 % («1 en el dado bueno»)", "T130", fmt(probs("T4", 2)["pifia"]) + " %",
              "en peor de 2, el dado elegido es 1 si hay cualquier 1", True))
    th = probs("TS", 2)
    c.append(("Thriller +2: éxito sucio ~20 %, fallo ~30 %", "T130",
              f"parcial {fmt(th['parcial'])} %, fallo {fmt(th['fallo'])} %, pifia {fmt(th['pifia'])} %",
              f"éxito limpio (con crítico) {fmt(th['exito'] + th['critico'])} %: ese dato sí era correcto", True))
    c.append(("Disonancia en el terror: «del 80 % al 30 %»", "Borrador 7.4",
              f"{fmt(probs('T1', 2)['total'])} % → {fmt(probs('T4', 2)['total'])} %", "Profesional +2 vs TN 6, mejor → peor de 2 (ED-14)", True))
    t3 = probs("T3", 2)
    c.append(("Pulp +2: fallo 30 %, coste 30 %, limpio 40 %", "T23",
              f"pifia {fmt(t3['pifia'])}, fallo {fmt(t3['fallo'])}, parcial {fmt(t3['parcial'])}, éxito {fmt(t3['exito'])}, crítico {fmt(t3['critico'])} %",
              "no es un error de cálculo: T23 usaba bandas 1–5 / 6–8 / 9+ y sin pifia/crítico naturales; aquí van las bandas canónicas", False))
    return c


VERIFICADAS = [
    ("Héroe +4 / +2 / −2 (TN 6)", "T20, T23", [("T1", 4, "total", 99), ("T1", 2, "total", 91), ("T1", -2, "total", 51)]),
    ("Terror +4 / +2 / −2 (TN 6)", "T20, T23", [("T4", 4, "total", 81), ("T4", 2, "total", 49), ("T4", -2, "total", 9)]),
    ("Neutro 1d10 +4 / +2 / −2", "T20", [("T0", 4, "total", 90), ("T0", 2, "total", 70), ("T0", -2, "total", 30)]),
    ("Realista +4 / −2 (TN 11)", "T20, T23", [("T2", 4, "total", 85), ("T2", -2, "total", 36)]),
    ("Pifias 10 / 1 / 19 / 3 %", "T20", [("T0", 0, "pifia", 10), ("T1", 0, "pifia", 1), ("T4", 0, "pifia", 19), ("T2", 0, "pifia", 3)]),
    ("Tragedia (TN 14) +4 / +2: 64 / 45 %", "T30", [("T6", 4, "total", 64), ("T6", 2, "total", 45)]),
    ("Pulp Desatado +2: limpio 75 %, coste 16 %, pifia 1 %", "T130", [("PD", 2, "parcial", 16), ("PD", 2, "pifia", 1)]),
    ("Nulidad 1d10: de 50 % a 30 %", "Borrador 4.2", [("T0", 0, "total", 50), ("T0", -2, "total", 30)]),
]


def verificar():
    for _, _, checks in VERIFICADAS:
        for k, b, cat, val in checks:
            assert probs(k, b)[cat] == val, (k, b, cat, probs(k, b)[cat], val)
    pd = probs("PD", 2)
    assert pd["exito"] + pd["critico"] == 75
    assert probs("T0", 4)["total"] == 90 and probs("T2", 4)["total"] == 85  # ilusión del +4
    assert media(TWO, mejor) == F(715, 100) and media(TWO, peor) == F(385, 100)


# ------------------------------------------------------------------ salida texto
def texto():
    out = []
    for k, (nom, *_rest) in ALL.items():
        regla = ALL[k][6]
        out.append(f"\n## {k} {nom} — {regla}")
        out.append("bono | pifia | fallo | parcial | éxito | crítico | ÉXITO TOTAL")
        for b in BONOS:
            p = probs(k, b)
            out.append(f"{sb(b):>4} | " + " | ".join(f"{fmt(p[c]):>5}" for c in CATS) + f" | {fmt(p['total']):>5}")
    out.append("\n## Medias y distribuciones")
    for nom, rolls, lect, vals in LECTURAS:
        d = distribucion(rolls, lect, vals)
        out.append(f"{nom}: media {fmt(media(rolls, lect))} | " + " ".join(f"{v}:{fmt(p)}" for v, p in d.items()))
    out.append("\n## Referencias")
    for k, v in referencias().items():
        out.append(f"{k}: {float(v):.3f}")
    out.append("\n## Cifras citadas en la conversación")
    for cit, turno, ok, com, err in correcciones():
        out.append(f"[{'ERR' if err else 'nota'}] {turno}: {cit} -> {ok} ({com})")
    return "\n".join(out)


# ------------------------------------------------------------------ salida HTML
def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def src(t):
    return f'<span class="src">{t}</span>'


PENDIENTE = '<span class="flag pending">Pendiente</span>'
EDM = '<span class="flag ed">ED-M</span>'


def tabla(head, rows, numcols):
    h = "".join(f"<th>{c}</th>" for c in head)
    body = []
    for row in rows:
        cells = []
        for i, c in enumerate(row):
            cls = ' class="num"' if i in numcols else ""
            cells.append(f"<td{cls}>{c}</td>")
        body.append("<tr>" + "".join(cells) + "</tr>")
    return ('<div class="tw"><table class="t"><thead><tr>' + h + "</tr></thead><tbody>\n"
            + "\n".join(body) + "\n</tbody></table></div>")


HEAD_P = ["Pifia", "Fallo", "Parcial", "Éxito", "Crítico", "Éxito total"]


def tabla_card(k, filas):
    rows = []
    for b, etiqueta in filas:
        p = probs(k, b)
        rows.append([etiqueta] + [fmt(p[c]) + " %" for c in CATS] + [f"<strong>{fmt(p['total'])} %</strong>"])
    return tabla(["Perfil (bono)"] + HEAD_P, rows, set(range(1, 7)))


def perfiles():
    return [(b, f"{n} ({sb(b)})") for b, n in PERFILES]


def todos():
    return [(b, sb(b)) for b in BONOS]


ENCAJE = {
    "T0": ("Optimismo Neutro / Caos Medio", "«Piloto automático»",
           "Un solo dado lineal: cada cara vale un 10 %, y el bono mueve la aguja de diez en diez. El Profesional falla "
           "{f2} de cada 10 veces (contando la pifia) y hasta el Gran Maestro se come el 1 natural. Es la volatilidad de "
           "una película de acción o de Juego de Tronos: la competencia importa, pero la suerte reina. Por eso es el tono "
           "por defecto: es la costumbre del hobby."),
    "T1": ("Optimismo Alto / Caos Bajo", "«Soy el mejor en lo que hago»",
           "El Gran Maestro casi no falla ({t4} %): solo le traiciona el doble 1. Y la Nulidad todavía acierta la mitad "
           "de las veces ({tm2} %), porque en este universo cualquiera puede ser un héroe. El crítico ({c} %) aparece casi "
           "una de cada cinco tiradas: el mundo quiere que brilles."),
    "T2": ("Optimismo Neutro / Caos Bajo", "«La vida es justa y predecible»",
           "La campana aplasta los extremos (pifia y crítico: {pf} % cada uno) y deja a la competencia al mando: de "
           "{tm2} % a {t4} % entre la Nulidad y el Gran Maestro. Es sólido, justo y algo aburrido, así que premia a quien "
           "planifica. El Maestro pierde un poco respecto al dado único, y ese es el «margen de error humano» del "
           "cirujano experto."),
    "T3": ("Optimismo Neutro / Caos Alto", "«Sí, pero te va a costar»",
           "Una franja entera del dado se convierte en éxito con coste. Para el Profesional, {p2} % de las tiradas "
           "avanzan la historia con una factura. El motor genera contenido sin parar: nadie se queda en punto muerto, "
           "pero pocas victorias salen limpias."),
    "T4": ("Optimismo Bajo / Caos Medio", "«Tengo miedo a fallar»",
           "La competencia apenas te salva. El Gran Maestro llega al {t4} %, pero la pifia ({pf} %) es igual para todos, y "
           "la Nulidad se queda en un {tm2} %. La tensión no viene de «no sé hacerlo», sino de «sé hacerlo, pero el "
           "pánico puede traicionarme». La mesa se vuelve precavida y evita tirar."),
    "T5": ("Caos Máximo / Optimismo Neutro", "«¡Cualquier cosa puede pasar!»",
           "El {ext} % de las tiradas acaba en un extremo sea cual sea el bono, que solo decide en el tramo 3–8. Entre "
           "el Novato ({t0} %) y el Gran Maestro ({t4} %) hay poca distancia: la ruleta rusa manda. Va bien para comedia, "
           "sueños o magia salvaje, y en una campaña seria quemaría a la mesa."),
    "T6": ("Optimismo Bajo / Caos Bajo", "«No hay esperanza»",
           "Es un realismo asfixiante. La misma campana del Realista, pero con la vara desplazada a 14: el Gran Maestro "
           "falla el {f4} % de las veces y la Nulidad solo aprieta los dientes ({tm2} %). Es predecible, lento y "
           "opresivo: la matemática de Chernobyl."),
}


def encaje(k):
    p = {b: probs(k, b) for b in BONOS}
    vals = dict(t4=fmt(p[4]["total"]), tm2=fmt(p[-2]["total"]), t0=fmt(p[0]["total"]),
                f2=fmt((100 - p[2]["total"]) / 10), f4=fmt(100 - p[4]["total"]),
                c=fmt(p[2]["critico"]), pf=fmt(p[2]["pifia"]), p2=fmt(p[2]["parcial"]),
                ext=fmt(p[2]["pifia"] + p[2]["critico"]))
    return ENCAJE[k][2].format(**vals)


def barras(nom_cols, dists, vals):
    head = ["Valor"]
    for n in nom_cols:
        head += [f"{n} (%)", f"{n} (barra)"]
    rows = []
    maxs = [max(d.values()) for d in dists]
    for v in vals:
        row = [str(v)]
        for d, m in zip(dists, maxs):
            w = round(100 * d[v] / m)
            row += [fmt(d[v]), f'<span class="bar" style="--w:{w}%"></span>']
        rows.append(row)
    numcols = {i for i in range(1, 1 + 2 * len(dists), 2)}
    return tabla(head, rows, numcols)


def html():
    r = referencias()
    P = lambda k, b: probs(k, b)
    L = []
    a = L.append
    # ================================================================ 1.3
    a('<section class="chapter" id="ch1-maquinas">')
    a("<h2>1.3 La Sala de Máquinas (Análisis Estadístico)</h2>")
    a('<aside class="meta"><p>Aviso: esta sección es contenido técnico. Si las probabilidades te dan urticaria, '
      "puedes saltar directamente al 1.4 (Panel de Control). Las tarjetas funcionan igual aunque no sepas por qué. "
      "Aquí se viene a mirar el motor con la tapa quitada.</p></aside>")
    a("<p>Todas las cifras de esta sección salen de una enumeración exacta de las combinaciones posibles: 10 con un "
      "dado y 100 con dos. No son redondeos ni simulaciones. Siguen las reglas canónicas: la pifia y el crítico se leen "
      "<strong>en los dados, sin bonos</strong> y tienen prioridad sobre el total "
      '<span class="flag ed">ED-1</span>. El resto se resuelve con <em>lectura + bono total</em> contra la TN de la '
      "tarjeta activa.</p>")

    a('<h3 id="maq-equilibrio">A. El punto de equilibrio: un dado, caos neutro</h3>')
    a("<p>¿Qué es lo «normal»? En la vida real, una distribución plana es una locura: un cirujano experto que "
      "cometiera un error garrafal una de cada diez veces sería caos puro. Aun así, el hobby lleva décadas tirando "
      "un único dado lineal (el d20 de D&amp;D, el d100 de La Llamada de Cthulhu), y la mesa lo siente como "
      "«lo normal». NOGUM toma esa costumbre como punto de partida. "
      f"<strong>Un dado lineal es el Caos Neutro</strong> {src('T14')}. Con 1d10, cada cara vale un 10 %, y un Gran "
      f"Maestro (+4) contra TN 6 acierta un {fmt(P('T0', 4)['total'])} %: solo falla con el 1 natural. Es emocionante, "
      "pero poco profesional.</p>")

    a('<h3 id="maq-orden">B. Herramientas de orden: sumar dados</h3>')
    a("<p>Al sumar dados, los resultados se amontonan en el centro (el teorema central del límite, la campana de "
      "Gauss). Con 2d10 sumados, cada extremo (2 o 20) sale solo un 1 % de las veces, y el valor central, 11, sale "
      f"un {fmt(r['suma_11'])} %. La suerte pierde peso y la competencia lo gana: eso es <strong>orden</strong> "
      "(Caos Bajo).</p>")
    a("<ul>"
      f"<li><strong>GURPS</strong> tira 3d6 (3–18, media 10,5). Un 10 o un 11 sale un {fmt(r['gurps_10_11'])} % de las "
      f"veces, y un 3 o un 18 apenas un {fmt(r['gurps_extremos'])} %. Es el ejemplo clásico de un mundo fiable.</li>"
      f"<li><strong>FATE</strong> tira 4dF (−4 a +4). El 0 sale un {fmt(r['fate_0'])} % de las veces y los extremos "
      f"±4 solo un {fmt(r['fate_4'])} %: la ficha manda sobre el dado.</li></ul>")

    a('<h3 id="maq-caos">C. Sucumbiendo al caos</h3>')
    a("<p>Para subir el Caos hay dos palancas que no tocan la media:</p>")
    a("<dl>"
      "<dt>C.1 Ampliar los rangos naturales</dt>"
      "<dd>Más caras del dado se convierten en pifia o crítico. Con 1d10, pasar de «1 y 10» a «1–2 y 9–10» dobla los "
      "extremos: del 20 % al 40 % de las tiradas. Solo tiene sentido porque la pifia y el crítico son naturales: el "
      "bono no los toca. Es la tarjeta Gonzo (T5).</dd>"
      "<dt>C.2 El éxito parcial</dt>"
      "<dd>Una franja de resultados pasa a ser «sí, pero…». Es el corazón de los juegos <em>Powered by the "
      f"Apocalypse</em>, que tiran 2d6: con 6 o menos se falla ({fmt(r['pbta_fallo'])} %), con 7–9 se tiene un éxito "
      f"con coste ({fmt(r['pbta_parcial'])} %) y con 10 o más, un éxito total ({fmt(r['pbta_exito'])} %). Así se "
      "elimina el punto muerto: siempre ocurre algo. En D&amp;D el equivalente clásico es el crítico con 20 natural. "
      "Es la tarjeta Pulp / Drama (T3).</dd></dl>")

    a('<h3 id="maq-optimismo">D. Las palancas del optimismo y del terror</h3>')
    mb, mp = media(TWO, mejor), media(TWO, peor)
    a("<p><strong>Optimismo: quedarse el MEJOR de 2.</strong> Es la ventaja de D&amp;D 5.ª edición y los dados de "
      "bonificación de La Llamada de Cthulhu 7.ª (que se quedan la mejor decena). Con 1d20, la ventaja sube la media "
      f"de 10,5 a {float(r['d20_ventaja_media']):.3f}".replace(".", ",") + " y reduce la pifia del 5 % al "
      f"{float(r['d20_ventaja_pifia']):.2f}".replace(".", ",") + " %. En NOGUM, con 2d10, la media sube de 5,5 a "
      f"{fmt(mb)}, la probabilidad de que algún dado sea 10 pasa del 10 % al 19 % y el doble 1 se queda en un 1 %.</p>")
    a("<p><strong>Terror: quedarse el PEOR de 2.</strong> Es el espejo exacto. La media baja a "
      f"{fmt(mp)}, cualquier 1 arruina la tirada (19 %) y el milagro exige un doble 10 (1 %). La competencia sigue "
      "contando, pero el pánico puede traicionarla.</p>")

    a('<h3 id="maq-dados">E. La solución NOGUM: dos dados de distinto color</h3>')
    a("<p>Todo el sistema cabe en <strong>dos d10 de distinto color, uno rojo y otro azul</strong>. Se tiran siempre "
      "los dos, y la tarjeta activa dice cómo se leen. Hay seis lecturas:</p>")
    a("<ol><li><strong>Solo el rojo</strong> (1d10): Caos Neutro.</li>"
      "<li><strong>La suma</strong> (2–20): orden.</li>"
      "<li><strong>El mejor</strong> de los dos: optimismo.</li>"
      "<li><strong>El peor</strong> de los dos: terror.</li>"
      "<li><strong>Rangos ampliados</strong> sobre el rojo: caos alto (C.1).</li>"
      "<li><strong>Bandas de éxito parcial</strong> sobre el total: caos alto (C.2).</li></ol>")
    a("<p>La tabla muestra cómo se reparte cada lectura. La barra es relativa al valor más frecuente de su "
      "columna.</p>")
    dists = [distribucion(rl, le, range(1, 11)) for _, rl, le, _ in LECTURAS[:3]]
    a(barras(["1d10", "Mejor", "Peor"], dists, range(1, 11)))
    a(barras(["Suma 2d10"], [distribucion(TWO, suma, range(2, 21))], range(2, 21)))
    a("<p>Medias: " + ", ".join(f"{n} <strong>{fmt(media(rl, le))}</strong>" for n, rl, le, _ in LECTURAS) + ".</p>")

    a('<h3 id="maq-anclaje">F. El anclaje: de −2 a +4</h3>')
    a("<p>El bono total (habilidad, dificultad, equipo y efectos) va <strong>siempre</strong> de −2 (Nulidad) a +4 "
      "(Gran Maestro). Nunca sale de ese rango (ver 4.1). Por eso las tablas de este libro se pueden calcular "
      "enteras: son siete filas por tarjeta. Aquí se muestran cuatro perfiles de referencia: Nulidad (−2), "
      "Novato (+0), Profesional (+2) y Gran Maestro (+4). El Apéndice D trae los siete bonos.</p>")

    a('<h3 id="maq-tarjetas">G. Las siete configuraciones, una a una</h3>')
    for k, (nom, *_x) in CARDS.items():
        coords, lema, _ = ENCAJE[k]
        a(f"<h4>{k} · {nom} ({coords}) {lema}</h4>")
        a(f"<p><em>Regla:</em> {esc(CARDS[k][6])}.</p>")
        a(tabla_card(k, perfiles()))
        a(f"<p><strong>Por qué encaja:</strong> {encaje(k)} {src('T130')}</p>")
    a('<aside class="meta"><p>¿Has visto que T1 y T4 son espejos exactos? En el Héroe, crítico 19 % y pifia 1 %; en '
      "el Terror, al revés. La ficha no cambia; lo que cambia es la atmósfera. El mismo Profesional pasa de un "
      f"{fmt(P('T1', 2)['total'])} % a un {fmt(P('T4', 2)['total'])} % sin tocar un solo número de su hoja.</p></aside>")

    a('<h3 id="maq-malla">H. Los nueve modos de la Malla Tonal</h3>')
    a("<p>Esta es la referencia del perfil Profesional (+2) contra la TN que corresponde a cada modo "
      f"{src('T130')}{src('T131')}. Seis casillas tienen tarjeta. Las otras tres (Épica Clásica, Pulp Desatado y "
      "Pesadilla) quedan para que el DJ las diseñe, y aquí aparecen con la receta de referencia del análisis de los "
      "nueve modos.</p>")
    filas = [
        ("Alto", "Fantasía de Poder", "Bajo", "T1 Héroe", "T1", ""),
        ("Alto", "Épica Clásica", "Medio", "Receta: mejor de 2, crítico cualquier 10, pifia doble 1", "EC",
         " (hoy idéntica a T1; la diferencia con Fantasía de Poder está abierta) " + PENDIENTE),
        ("Alto", "Pulp Desatado", "Alto", "Receta: mejor de 2 + parcial con total 6–7", "PD", " " + PENDIENTE),
        ("Neutro", "Realismo Gris", "Bajo", "T2 Realista", "T2", ""),
        ("Neutro", "Drama de Acción", "Medio", "T0 Estándar", "T0", ""),
        ("Neutro", "Comedia Negra / Extrañeza", "Alto", "T5 Gonzo (rangos ampliados, C.1)", "T5", ""),
        ("Neutro", "(Caos Alto, otro sabor)", "Alto", "T3 Pulp / Drama (éxito parcial, C.2)", "T3", ""),
        ("Bajo", "Terror Purista", "Bajo", "T6 Tragedia", "T6", ""),
        ("Bajo", "Thriller de Supervivencia", "Medio", "T4 Terror", "T4", ""),
        ("Bajo", "(Thriller, variante T130)", "Medio", "Receta: peor de 2 + total 4–5 = éxito con coste", "TS",
         " " + PENDIENTE),
        ("Bajo", "Pesadilla / Slasher", "Alto", "Receta: peor de 2, pifia cualquier 1", "PS",
         " (hoy idéntica a T4; el caos alto del eje bajo está por definir) " + PENDIENTE),
    ]
    rows = []
    for opt, modo, caos, cubre, k, nota in filas:
        p = P(k, 2)
        rows.append([opt, modo, caos, cubre + nota, str(ALL[k][7])] + [fmt(p[c]) + " %" for c in CATS]
                    + [f"<strong>{fmt(p['total'])} %</strong>"])
    a(tabla(["Optimismo", "Modo", "Caos", "Tarjeta / receta", "TN"] + HEAD_P, rows, set(range(4, 11))))

    a('<div class="rule"><p class="rule-title">La ilusión del +4</p>')
    a("<p>Al pasar de un dado (1–10) a la suma (2–20), parece que el +4 «pesa menos», porque la escala es el doble "
      f"de larga. No es así. Con 1d10 contra TN 6, el Gran Maestro necesita un 2 o más: <strong>{fmt(P('T0', 4)['total'])} %</strong>. "
      f"Con la suma contra TN 11 necesita un 7 o más: <strong>{fmt(P('T2', 4)['total'])} %</strong> {src('T29')}{src('T30')}. "
      "La campana concentra los resultados en el centro, así que cuatro puntos de bono mueven mucha más masa de "
      "probabilidad de lo que su tamaño sugiere. Solo se pierden cinco puntos, y ese es el grano de realidad del "
      "modo Realista. El sistema cambia la volatilidad, no tu eficacia profesional.</p>")
    a(f"<p>Con el Novato (+0) pasa algo parecido: {fmt(P('T0', 0)['total'])} % con un dado y "
      f"{fmt(P('T2', 0)['total'])} % con la suma. La cifra de «50 %» que se citó para la suma era un redondeo "
      f"erróneo {EDM}.</p></div>")
    a('<aside class="meta"><p><strong>El principio del 99 %</strong>. En el modo Héroe, el Gran Maestro acierta una '
      f"tarea estándar el {fmt(P('T1', 4)['total'])} % de las veces {src('T21')}{src('T22')}. Eso no es un bug: un Gran "
      "Maestro no debe tener problemas con lo mundano. Aquí no hay «inflación narrativa»: la dificultad se queda donde "
      "está. Si la tirada no puede salir interesante, <strong>no se tira</strong>. Y si el jugador quiere lucirse, "
      "que se suba él mismo la dificultad con la «mano a la espalda», por ejemplo rebotando la bala en la pared. "
      "Cambia seguridad por gloria.</p></aside>")
    a("</section>")

    # ================================================================ Apéndice D
    a('<section class="chapter" id="apx-mates">')
    a("<h2>Apéndice D · Tablas completas</h2>")
    a("<p>Estas son las probabilidades exactas (en %) para cada bono total de −2 a +4. "
      "<em>Éxito total</em> = parcial + éxito + crítico. Cada fila suma 100 %. Reglas: la pifia y el crítico son "
      "naturales y tienen prioridad; el resto se resuelve con lectura + bono contra la TN de la tarjeta.</p>")
    for k, (nom, *_x) in CARDS.items():
        a(f'<h3 id="apxd-{k.lower()}">{k} · {nom}</h3>')
        a(f"<p>{esc(CARDS[k][6])}.</p>")
        a(tabla_card(k, todos()))
    a('<h3 id="apxd-recetas">Recetas de referencia sin tarjeta</h3>')
    a("<p>Estas recetas proceden del análisis de los nueve modos " + src("T130") + src("T131") +
      ". El autor no ha cerrado su diseño final " + PENDIENTE + ".</p>")
    for k, (nom, *_x) in RECETAS.items():
        a(f"<h4>{nom}</h4>")
        a(f"<p>{esc(RECETAS[k][6])}.</p>")
        a(tabla_card(k, todos()))
    a('<h3 id="apxd-medias">Medias y distribuciones de las lecturas</h3>')
    a(tabla(["Lectura", "Rango", "Media"],
            [[n, f"{v[0]}–{v[-1]}", fmt(media(rl, le))] for n, rl, le, v in LECTURAS], {2}))
    d_all = [distribucion(rl, le, range(1, 11)) for _, rl, le, _ in LECTURAS[:3]]
    rows = [[str(v)] + [fmt(d[v]) for d in d_all]
            + [fmt(sum(d[x] for x in range(1, v + 1))) for d in d_all[1:]] for v in range(1, 11)]
    a(tabla(["Valor", "1d10 (%)", "Mejor (%)", "Peor (%)", "Mejor ≤ valor (%)", "Peor ≤ valor (%)"], rows, set(range(1, 6))))
    ds = distribucion(TWO, suma, range(2, 21))
    rows = [[str(v), fmt(ds[v]), fmt(sum(ds[x] for x in range(v, 21)))] for v in range(2, 21)]
    a(tabla(["Suma", "P (%)", "P(suma ≥ valor) (%)"], rows, {1, 2}))

    a('<h3 id="apxd-corregidas">Cifras corregidas</h3>')
    a(f"<p>{EDM} Durante la conversación de diseño se citaron algunas cifras que no resisten el recálculo exacto. "
      "El editor las ha sustituido en todo el libro por los valores de esta tabla. La última fila no es un error "
      "aritmético: es un cambio de bandas. Se incluye para que nadie se extrañe al comparar.</p>")
    rows = []
    for cit, turno, ok, com, err in correcciones():
        rows.append([esc(cit), src(turno), f"<strong>{esc(ok)}</strong>" + (f" ({esc(com)})" if com else "")
                     + (" " + EDM if err else "")])
    a(tabla(["Cifra citada", "Turno", "Valor correcto"], rows, set()))
    a("<p>Estas cifras de la conversación se han comprobado y son <strong>correctas</strong>:</p><ul>")
    for txt, turno, _ in VERIFICADAS:
        a(f"<li>{esc(txt)} {src(turno.split(',')[0])}</li>")
    a(f"<li>La ilusión del +4: {fmt(P('T0', 4)['total'])} % frente a {fmt(P('T2', 4)['total'])} % {src('T30')}</li>")
    a(f"<li>Media del mejor de 2d10: {fmt(media(TWO, mejor))}; referencias de d20 con ventaja "
      f"({float(r['d20_ventaja_media']):.2f}".replace(".", ",") + " de media, 0,25 % de pifia), PbtA "
      f"({float(r['pbta_fallo']):.1f} / {float(r['pbta_parcial']):.1f} / {float(r['pbta_exito']):.1f} %)".replace(".", ",")
      + f" y 3d6 (≈ {fmt(r['gurps_10_11'])} %) {src('T13')}</li>")
    a("</ul>")
    a("</section>")
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    verificar()
    print(texto())
    if "--html" in sys.argv:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "frag_math.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html())
        print("\nEscrito:", path)
