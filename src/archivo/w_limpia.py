# -*- coding: utf-8 -*-
"""El aparato editorial sale de los manuales. Se queda en el Cuaderno, que es
donde tiene sentido: ahi es el contenido, aqui era ruido."""
import io, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
F = 'assemble3.py'
s = io.open(F, encoding='utf-8').read()
if 'def limpia_editorial' in s:
    print('ya estaba'); sys.exit(0)

FUNC = '''def limpia_editorial(body):
    """Fuera las notas de edicion de los manuales.

    Dos formas distintas de aparecer, y se tratan distinto:
      - un bloque que EMPIEZA por la bandera es una nota entera -> se borra el bloque
      - una bandera al final de una frase util es solo una marca -> se borra la marca
    Lo de «aprobado / propuesta del asistente / pendiente» tampoco va al manual:
    el lector no tiene por que saber que estaba en duda. Todo queda en el
    Cuaderno, que es el sitio de eso."""
    CL = r'flag (?:ed|drop|pending|proposal)'
    # 1. bloques que son la nota entera
    for tag in ('p', 'li', 'aside', 'td'):
        body = re.sub(r'<' + tag + r'[^>]*>\\s*<span class="' + CL + r'"[^>]*>.*?</' + tag + '>', '', body, flags=re.S)
    # 2. marcas sueltas dentro de texto que si vale
    body = re.sub(r'\\s*<span class="' + CL + r'"[^>]*>.*?</span>', '', body, flags=re.S)
    # 3. parentesis y comas que quedan colgando
    body = re.sub(r'\\(\\s*\\)', '', body)
    body = re.sub(r'\\s+([.,;:])', r'\\1', body)
    return body

'''
a = 'def fix_cross(body, me, mode):'
assert s.count(a) == 1
s = s.replace(a, FUNC + a, 1)
b = "        b = con_pack(fix_cross(c['src'][l], me, mode), me, mode, l)"
assert s.count(b) == 1
s = s.replace(b, "        b = fix_cross(c['src'][l], me, mode)\n"
                 "        if me != 'cuaderno': b = limpia_editorial(b)\n"
                 "        b = con_pack(b, me, mode, l)", 1)
io.open(F, 'w', encoding='utf-8').write(s)
print('assemble3: el aparato editorial sale de los manuales')
