# -*- coding: utf-8 -*-
"""Las imagenes de cada pieza, a los tamanos que usa la web.

Una por pieza en src/img/<pieza>.jpg (idea, juego, acelerado, app). La que
falte usa src/img/portada.jpg, asi que hoy las cuatro son la misma. Para
cambiar una: dejar el original en src/img/ con su nombre y ejecutar esto.

    docs/img/<pieza>.jpg       1280 px, la banda de la portadilla de cada libro
    docs/img/<pieza>-640.jpg    640 px, la tarjeta de la portada del sitio

Necesita Pillow, pero solo para esto: la compilacion de los libros no lo usa.
"""
import os, sys
from PIL import Image

D = os.path.dirname(os.path.abspath(__file__))
ORIG = os.path.join(D, 'img')
DEST = os.path.join(D, '..', 'docs', 'img')
PIEZAS = ('idea', 'juego', 'acelerado', 'app')
TAMANOS = (('', 1280), ('-640', 640))

os.makedirs(DEST, exist_ok=True)
for p in PIEZAS:
    propia = os.path.join(ORIG, p + '.jpg')
    src = propia if os.path.exists(propia) else os.path.join(ORIG, 'portada.jpg')
    im = Image.open(src).convert('RGB')
    for suf, ancho in TAMANOS:
        alto = round(im.height * ancho / im.width)
        out = os.path.join(DEST, p + suf + '.jpg')
        im.resize((ancho, alto), Image.LANCZOS).save(out, quality=82, optimize=True, progressive=True)
    print('%-10s <- %s' % (p, os.path.basename(src)))
