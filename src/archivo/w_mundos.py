# -*- coding: utf-8 -*-
"""La app lee los techos de los datos, y los veinte mundos vuelven a su receta."""
import io, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
F = 'app4_body.html'
s = io.open(F, encoding='utf-8').read()
fal = []


def sub(a, b, n=1):
    global s
    if s.count(a) != n:
        fal.append('(%d!=%d) %s' % (s.count(a), n, a[:70])); return
    s = s.replace(a, b, n)


# ---------------------------- 1. fuera la tabla a mano, dentro la de los datos
i = s.index('/* techos de Rejilla por receta (8.4): fis, men, soc, tec, arc; 0 = no existe */')
j = s.index('function arcOpen(){')
s = s[:i] + ('/* Los techos de Rejilla (8.4) vienen de los datos, leidos de la ficha impresa\n'
             '   de cada receta. Antes habia aqui una tabla copiada a mano y se quedo atras\n'
             '   al expulsar la receta 15: seis recetas llevaban los techos de la de al lado. */\n'
             'function techoReceta(r){ var x = DATA.techos && DATA.techos[r]; return (x && x.length === 5) ? x : null; }\n') + s[j:]
sub("if (M.known && M.world !== null) { var tc = TECHO[KNOWN[M.world].r]; return tc ? tc[4] > 0 : true; }",
    "if (M.known && M.world !== null) { var tc = techoReceta(KNOWN[M.world].r); return tc ? tc[4] > 0 : true; }")
sub("if (M.known && M.world !== null) { var tc = TECHO[KNOWN[M.world].r]; if (tc) return tc; }",
    "if (M.known && M.world !== null) { var tc = techoReceta(KNOWN[M.world].r); if (tc) return tc; }")

# -------------------------- 2. el mundo huerfano sale: su receta fue expulsada
VIEJO = ("  {r:14, n:['Instituto de día, caza de monstruos de noche','High school by day, monster hunting by night'], "
         "h:['Drama juvenil con estacas','Teen drama with stakes'], p:['alto','medio','carne',1,true,['gotico','terror'],[]]},\n")
sub(VIEJO, '')

# ------------------------------- 3. los seis desplazados vuelven a su sitio
for viejo, nuevo in ((15, 14), (16, 15), (17, 16), (18, 17), (19, 18)):
    sub('  {r:%d, n:[' % viejo, '  {r:%d, n:[' % nuevo)

# ---------------------- 4. y entra el mundo que faltaba: la receta 20 no tenia
ULT = ("  {r:18, n:['Una distopía de risa con un ordenador loco','A hilarious dystopia run by a mad computer'], "
       "h:['Todos son traidores, tú también','Everyone is a traitor, you too'], "
       "p:['neutro','alto','cascara',1,false,['neon','toon'],[7,8],'locura']}\n")
NUEVO = (ULT.rstrip('\n') + ',\n'
         "  {r:19, n:['Un mundo plano a lomos de una tortuga gigante','A flat world on the back of a giant turtle'], "
         "h:['Sátira fantástica y burocrática','Fantasy satire and bureaucracy'], "
         "p:['neutro','alto','carne',1,true,['fantasia','social'],[]]}\n")
sub(ULT, NUEVO)

# ------------------------------------------------------------- 5. las familias
sub("s:['Horror, vampiros, niños valientes y ladrones','Horror, vampires, brave kids and thieves'], k:[11,12,13,14,15]}",
    "s:['Horror, vampiros, niños valientes y ladrones','Horror, vampires, brave kids and thieves'], k:[11,12,13,14]}")
sub("s:['Superhéroes, anime, mechas y distopía','Superheroes, anime, mechas and dystopia'], k:[16,17,18,19]}",
    "s:['Superhéroes, anime, mechas, distopía y sátira','Superheroes, anime, mechas, dystopia and satire'], k:[15,16,17,18,19]}")

if 'TECHO[' in s:
    fal.append('queda alguna lectura de la tabla vieja TECHO[')
if fal:
    print('FALLOS:')
    for x in fal:
        print('  ' + x)
    sys.exit(1)
io.open(F, 'w', encoding='utf-8').write(s)
print('techos desde los datos y veinte mundos con su receta')
