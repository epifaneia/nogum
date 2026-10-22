# Pone a cada PDF de imprime.mjs sus marcadores (el indice del libro:
# capitulos y, colgando de cada uno, sus apartados), los metadatos (titulo,
# autor, idioma, licencia) y que se abra con el panel de marcadores.
#   python -I src/pdf/marcadores.py <carpeta>
import json, os, sys
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, TextStringObject

D = sys.argv[1] if len(sys.argv) > 1 else 'pdf'
AUTOR = 'Daniel Martín'
LIC = 'CC BY-SA 4.0'
for f in sorted(os.listdir(D)):
    if not f.endswith('.json'):
        continue
    meta = json.load(open(os.path.join(D, f), encoding='utf-8'))
    pdf = os.path.join(D, f[:-5] + '.pdf')
    r = PdfReader(pdf)
    w = PdfWriter(clone_from=r)
    n = len(w.pages)
    assert n == meta['paginas'], '%s: el PDF tiene %d paginas y el libro %d' % (pdf, n, meta['paginas'])
    padre = None
    for e in meta['indice']:
        p = min(max(e['pagina'] - 1, 0), n - 1)
        if e['nivel'] == 2 or padre is None:
            padre = w.add_outline_item(e['titulo'], p)
        else:
            w.add_outline_item(e['titulo'], p, parent=padre)
    w.add_metadata({'/Title': meta['titulo'], '/Author': AUTOR,
                    '/Subject': 'Juego de rol' if meta['lang'] == 'es' else 'Roleplaying game',
                    '/Keywords': 'NOGUM, rol, RPG, ' + LIC, '/Creator': 'NOGUM · assemble3 + Chrome',
                    '/Copyright': '%s · %s' % (AUTOR, LIC)})
    w._root_object[NameObject('/Lang')] = TextStringObject(meta['lang'])
    w._root_object[NameObject('/PageMode')] = NameObject('/UseOutlines')
    with open(pdf, 'wb') as fh:
        w.write(fh)
    os.remove(os.path.join(D, f))
    print('%-45s %3d paginas  %3d marcadores' % (os.path.basename(pdf), n, len(meta['indice'])))
