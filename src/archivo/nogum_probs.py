# Reconstrucción limpia del código de probabilidades de nogum_clean.md (combinatoria exacta, sin pandas)
import itertools

D = range(1, 11)
PAIRS = list(itertools.product(D, D))


def classify(rolls, base_fn, crit_fn, pifia_fn, mod, dif, pba=False, pba_thr=10):
    c = {"crit": 0, "pifia": 0, "limpio": 0, "consec": 0, "fallo": 0}
    for r in rolls:
        if crit_fn(r):
            c["crit"] += 1
        elif pifia_fn(r):
            c["pifia"] += 1
        else:
            t = base_fn(r) + mod
            if pba:
                if t >= pba_thr:
                    c["limpio"] += 1
                elif t >= dif:
                    c["consec"] += 1
                else:
                    c["fallo"] += 1
            else:
                if t >= dif:
                    c["limpio"] += 1
                else:
                    c["fallo"] += 1
    n = len(rolls)
    return {k: 100 * v / n for k, v in c.items()}


MODES = {
    # nombre: (tiradas, valor base, crítico, pifia, dif por defecto, pba)
    "Neutro / Comedia Negra (1d10)": ([(x,) for x in D], lambda r: r[0], lambda r: r[0] == 10, lambda r: r[0] == 1, 6, False),
    "Heroico Clásico (mejor de 2d10)": (PAIRS, max, lambda r: max(r) == 10, lambda r: r == (1, 1), 6, False),
    "Épico Desbordado (mejor de 2d10, PBA)": (PAIRS, max, lambda r: max(r) >= 9, lambda r: r == (1, 1), 6, True),
    "Existencial Gris (suma 2d10)": (PAIRS, sum, lambda r: sum(r) >= 19, lambda r: sum(r) <= 3, 13, False),
    "Terror Absoluto (peor de 2d10)": (PAIRS, min, lambda r: r == (10, 10), lambda r: min(r) == 1, 7, False),
    "Desesperanza Progresiva (peor de 2d10, PBA)": (PAIRS, min, lambda r: r == (10, 10), lambda r: min(r) <= 2, 6, True),
}

MODS = [-2, -1, 0, 1, 2, 3, 4]


def fmt(x):
    return f"{x:.0f}" if abs(x - round(x)) < 1e-9 else f"{x:.1f}"


def table(name, difs):
    rolls, base, crit, pif, _, pba = MODES[name]
    out = [f"\n#### {name}\n"]
    for dif in difs:
        out.append(f"\n**Dificultad {dif}**" + (" (umbral PBA de éxito limpio = 10)" if pba else "") + "\n")
        out.append("| Mod | Crítico | Pifia | Éxito limpio | Éxito c/consecuencia | Fallo | ÉXITO TOTAL | FRACASO TOTAL |")
        out.append("|---|---|---|---|---|---|---|---|")
        for m in MODS:
            p = classify(rolls, base, crit, pif, m, dif, pba)
            et = p["crit"] + p["limpio"] + p["consec"]
            out.append(f"| {m:+d} | {fmt(p['crit'])} | {fmt(p['pifia'])} | {fmt(p['limpio'])} | {fmt(p['consec'])} | {fmt(p['fallo'])} | {fmt(et)} | {fmt(100-et)} |")
    return "\n".join(out)


def dist():
    out = ["\n#### Distribuciones base (probabilidad % de cada valor)\n", "| Valor | 1d10 | Mejor de 2d10 | Peor de 2d10 |", "|---|---|---|---|"]
    for v in D:
        b = sum(1 for r in PAIRS if max(r) == v)
        w = sum(1 for r in PAIRS if min(r) == v)
        out.append(f"| {v} | 10 | {b} | {w} |")
    out.append("\n| Suma 2d10 | " + " | ".join(str(s) for s in range(2, 21)) + " |")
    out.append("|---|" + "---|" * 19)
    out.append("| % | " + " | ".join(str(sum(1 for r in PAIRS if sum(r) == s)) for s in range(2, 21)) + " |")
    return "\n".join(out)


if __name__ == "__main__":
    print(dist())
    print(table("Neutro / Comedia Negra (1d10)", [5, 6, 7, 8]))
    print(table("Heroico Clásico (mejor de 2d10)", [6, 7, 8]))
    print(table("Épico Desbordado (mejor de 2d10, PBA)", [6, 7]))
    print(table("Existencial Gris (suma 2d10)", [6, 11, 12, 13, 14]))
    print(table("Terror Absoluto (peor de 2d10)", [6, 7]))
    print(table("Desesperanza Progresiva (peor de 2d10, PBA)", [6, 7]))
