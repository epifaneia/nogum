# -*- coding: utf-8 -*-
"""Dos arreglos: la fuga de las banderas a los datos, y el atajo sin respuestas."""
import io, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
fal = []


def arregla(fichero, pares):
    s = io.open(fichero, encoding='utf-8').read()
    for a, b in pares:
        if s.count(a) != 1:
            fal.append('%s (%d) %s' % (fichero, s.count(a), a[:60])); continue
        s = s.replace(a, b, 1)
    io.open(fichero, 'w', encoding='utf-8').write(s)


# 1. las banderas y las notas de procedencia no son parte del nombre de nada
arregla('extract_app_data.py', [(
    "def txt(s): return H.unescape(re.sub(r'\\s+', ' ', re.sub(r'<[^>]+>', ' ', s))).strip()",
    "# las banderas y las notas de procedencia no forman parte del nombre de nada\n"
    "FUERA = re.compile(r'<span class=\"(?:flag[^\"]*|src)\">.*?</span>', re.S)\n"
    "def txt(s): return H.unescape(re.sub(r'\\s+', ' ', re.sub(r'<[^>]+>', ' ', FUERA.sub(' ', s)))).strip()")])

# 2. cuando se usa el atajo no hay escalas que leer: se le dice la receta
arregla('app4_body.html', [(
    """function respuestasTexto(fid){
  var out = [];""",
    """function respuestasTexto(fid){
  var out = [];
  if (fid === 'uni' && M.known && M.world !== null) {
    return '- No ha contestado escalas: ha usado el atajo y ha elegido el universo conocido «' + KNOWN[M.world].n[0] +
      '», que aplica la receta de emulación nº ' + (KNOWN[M.world].r + 1) + ' («' + DATA.recipes[KNOWN[M.world].r][0] + '») entera.';
  }"""), (
    """  return out.join('\\n');
}""",
    """  return out.length ? out.join('\\n') : '- Todavía no ha contestado ninguna pregunta de este formulario.';
}""")])

if fal:
    for x in fal:
        print('FALLO ' + x)
    sys.exit(1)
print('arreglados: la fuga de banderas y el atajo sin escalas')
