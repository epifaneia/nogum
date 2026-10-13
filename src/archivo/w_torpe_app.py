# -*- coding: utf-8 -*-
"""Torpe -1 y la Firma a +4 sin escalon intermedio, en la app."""
import io, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
F = 'app4_body.html'
s = io.open(F, encoding='utf-8').read()
fal = []


def sub(a, b, n=1):
    global s
    if s.count(a) != n:
        fal.append('(%d!=%d) %s' % (s.count(a), n, a[:72])); return
    s = s.replace(a, b, n)


# ---------------------------------------------------- 1. la Firma siempre es +4
sub("else if ((a = b.getAttribute('data-addf'))) c.fir.push({key:a, id:'', lv:3});",
    "else if ((a = b.getAttribute('data-addf'))) c.fir.push({key:a, id:'', lv:4});")
sub("else if ((a = b.getAttribute('data-flv'))) { var f = c.fir[+a], n = +b.getAttribute('data-n'); if (n === 3 && f.lv === 3) c.fir.splice(+a, 1); else f.lv = (n === 4 && f.lv === 4) ? 3 : n; }",
    "/* no hay +3: una Firma es +4 o no esta. Tocarla la quita. */\n"
    "  else if ((a = b.getAttribute('data-flv'))) { c.fir.splice(+a, 1); }")
sub("'<div class=\"srow fir\">' + dots(4, f.lv, [3,4], 'data-flv=\"' + fi + '\"')",
    "'<div class=\"srow fir\">' + dots(4, 4, [4], 'data-flv=\"' + fi + '\"')")
sub("c.fir.forEach(function(f){ p += f.lv === 4 ? 2 : 1; });",
    "c.fir.forEach(function(){ p += 2; });")
sub("'</select><button type=\"button\" class=\"plus noprint\" data-fdel=\"' + fi + '\" title=\"' + esc(t('Quitar','Remove')) + '\">×</button><span class=\"bonus\">+' + f.lv + '</span></div>'",
    "'</select><button type=\"button\" class=\"plus noprint\" data-fdel=\"' + fi + '\" title=\"' + esc(t('Quitar','Remove')) + '\">×</button><span class=\"bonus\">+4</span></div>'")
sub("if (f.key !== sk) return; best = Math.max(best, f.lv);",
    "if (f.key !== sk) return; best = Math.max(best, 4);")

# ------------------------------------------- 2. Torpe: la columna vacia resta 1
sub("""      var dk = ai + '.' + di, dOn = !blank && !!c.dom[dk];
      if (dOn) best = Math.max(best, 1);
      var fdom = FD.dom[dk];
      if (fdom) best = Math.max(best, 4);
      body += '<div class="dcol"><div class="srow dom' + (fdom ? ' folded' : '') + '">' + dots(1, dOn ? 1 : 0, blank ? [] : [1], 'data-dom="' + dk + '"') + '<span class="nm">' + esc(pick(d.n)) + (fdom ? ' <span class="fold">' + esc(t('plegado +4','folded +4')) + '</span>' : '') + '</span><span class="bonus">' + (dOn ? '+1' : '') + '</span></div>';""",
    """      var dk = ai + '.' + di, dOn = !blank && !!c.dom[dk];
      if (dOn) best = Math.max(best, 1);
      var fdom = FD.dom[dk];
      if (fdom) best = Math.max(best, 4);
      /* Torpe: hay algo en el ambito pero nada en esta columna. No es que no
         sepas: es que vas con el pie cambiado. */
      var torpe = !blank && !dOn && has;
      body += '<div class="dcol' + (torpe ? ' torpe' : '') + '"><div class="srow dom' + (fdom ? ' folded' : '') + '">' + dots(1, dOn ? 1 : 0, blank ? [] : [1], 'data-dom="' + dk + '"') + '<span class="nm">' + esc(pick(d.n)) + (fdom ? ' <span class="fold">' + esc(t('plegado +4','folded +4')) + '</span>' : '') + '</span><span class="bonus' + (torpe ? ' neg' : '') + '">' + (dOn ? '+1' : (torpe ? esc(t('Torpe −1','Clumsy −1')) : '')) + '</span></div>';""")
# y la disciplina sin dominio ensena el -1 en vez de nada
sub("""        body += '<div class="srow dis' + (fdis ? ' folded' : '') + '">' + dots(2, sOn ? 2 : (dOn ? 1 : 0), (!blank && dOn) ? [2] : [], 'data-dis="' + sk + '"') + '<span class="nm">' + esc(pick(s)) + (fdis ? ' <span class="fold">' + esc(t('plegada +4','folded +4')) + '</span>' : '') + '</span>' + (sOn ? '<button type="button" class="plus noprint" data-addf="' + sk + '" title="' + esc(t('Añadir firma','Add signature')) + '">+</button>' : '') + '<span class="bonus">' + (sOn ? '+2' : '') + '</span></div>';""",
    """        body += '<div class="srow dis' + (fdis ? ' folded' : '') + '">' + dots(2, sOn ? 2 : (dOn ? 1 : 0), (!blank && dOn) ? [2] : [], 'data-dis="' + sk + '"') + '<span class="nm">' + esc(pick(s)) + (fdis ? ' <span class="fold">' + esc(t('plegada +4','folded +4')) + '</span>' : '') + '</span>' + (sOn ? '<button type="button" class="plus noprint" data-addf="' + sk + '" title="' + esc(t('Añadir firma','Add signature')) + '">+</button>' : '') + '<span class="bonus' + ((!sOn && torpe) ? ' neg' : '') + '">' + (sOn ? '+2' : (torpe ? '−1' : '')) + '</span></div>';""")

# ------------------------------------- 3. el recordatorio de la hoja, al dia
sub("""<h3>' + esc(t('Tu bono','Your bonus')) + '</h3><table><tr><td>−2</td><td>' + esc(t('Ámbito vacío (Nulo)','Empty sphere (Null)')) + '</td></tr><tr><td>+0</td><td>' + esc(t('Algo en el ámbito','Something in the sphere')) + '</td></tr><tr><td>+1</td><td>' + esc(t('Habilidad amplia','Broad skill')) + '</td></tr><tr><td>+2</td><td>' + esc(t('Habilidad concreta','Specific skill')) + '</td></tr><tr><td>+3/+4</td><td>' + esc(t('Firma / Gran Maestro','Signature / Grand Master')) + '</td></tr></table>""",
    """<h3>' + esc(t('Tu bono','Your bonus')) + '</h3><table><tr><td>−2</td><td>' + esc(t('Ámbito vacío (Nulo)','Empty sphere (Null)')) + '</td></tr><tr><td>−1</td><td>' + esc(t('Columna vacía (Torpe)','Empty column (Clumsy)')) + '</td></tr><tr><td>+1</td><td>' + esc(t('Dominio: habilidad amplia','Domain: broad skill')) + '</td></tr><tr><td>+2</td><td>' + esc(t('Disciplina: habilidad concreta','Discipline: specific skill')) + '</td></tr><tr><td>+4</td><td>' + esc(t('Firma','Signature')) + '</td></tr></table>""")

# el acordeon ya no habla de Gran Maestro
s = s.replace('3 Firmas de Gran Maestro pliegan', '3 Firmas pliegan')
s = s.replace('3 Grand Master Signatures fold', '3 Signatures fold')

# ------------------------------------------------------------- 4. el aspecto
sub('.tag.parca{background:var(--ink);color:var(--paper);border-color:var(--ink)}',
    '.tag.parca{background:var(--ink);color:var(--paper);border-color:var(--ink)}\n'
    '.dcol.torpe .nm{opacity:.72}\n'
    '.srow .bonus.neg{color:var(--red);font-weight:600}')

if fal:
    print('FALLOS:')
    for x in fal:
        print('  ' + x)
    sys.exit(1)
io.open(F, 'w', encoding='utf-8').write(s)
print('app: Torpe -1 y la Firma a +4')
