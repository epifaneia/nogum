# -*- coding: utf-8 -*-
"""Las imagenes de cada pieza, a los tamanos que usa la web.

Una por pieza en src/img/<pieza>.jpg (idea, juego, acelerado, app); la que
falte usa src/img/portada.jpg. Para cambiar una: dejar el original en
src/img/ con su nombre y ejecutar esto.

    docs/img/<pieza>.jpg       1280 px, la banda de la portadilla de cada libro
    docs/img/<pieza>-640.jpg    640 px, la tarjeta de la portada del sitio

Y los retratos de los expedientes (las fichas de ejemplo del capitulo 8): cada
original de src/img/expedientes/ sale a docs/img/exp/ a 600 px, en gris.

Y las laminas del interior: cada original de src/img/laminas/ sale a
docs/img/lam/ a 1400 px, en color.

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

# los expedientes: frente y perfil de cada ficha de ejemplo, en blanco y negro
EXP = os.path.join(ORIG, 'expedientes')
if os.path.isdir(EXP):
    os.makedirs(os.path.join(DEST, 'exp'), exist_ok=True)
    for f in sorted(os.listdir(EXP)):
        if not f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')): continue
        im = Image.open(os.path.join(EXP, f)).convert('L')
        lado = 600
        im = im.resize((lado, round(im.height * lado / im.width)), Image.LANCZOS)
        im.save(os.path.join(DEST, 'exp', os.path.splitext(f)[0] + '.jpg'), quality=80, optimize=True, progressive=True)
        print('exp', f)

# las laminas del interior de los libros, en color
LAM = os.path.join(ORIG, 'laminas')
if os.path.isdir(LAM):
    os.makedirs(os.path.join(DEST, 'lam'), exist_ok=True)
    for f in sorted(os.listdir(LAM)):
        if not f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')): continue
        im = Image.open(os.path.join(LAM, f)).convert('RGB')
        ancho = 1400
        if im.width > ancho: im = im.resize((ancho, round(im.height * ancho / im.width)), Image.LANCZOS)
        im.save(os.path.join(DEST, 'lam', os.path.splitext(f)[0] + '.jpg'), quality=80, optimize=True, progressive=True)
        print('lam', f)
