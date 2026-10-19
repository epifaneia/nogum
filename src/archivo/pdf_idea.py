# -*- coding: utf-8 -*-
"""La Idea en PDF, compuesta a mano.

El texto sale de p_tesis_es.html, igual que en los otros tres productos: no
hay una copia del texto en ningun sitio. Lo que se decide a mano es DONDE
empieza cada pagina, y eso es la lista CORTES de abajo, escrita con las
palabras exactas del corte para que se pueda leer como las notas de un
cajista.

Una caja de altura fija con overflow:hidden se come en silencio lo que no
cabe. Por eso la composicion pasa por una puerta antes de imprimirse, medida
en el mismo Chrome que imprime y con las mismas fuentes:
  - nada se desborda de su caja, ni el texto ni las notas al margen
  - ningun titular se queda solo al pie de una pagina
  - un parrafo partido deja al menos dos lineas a cada lado del corte
  - el total de paginas es multiplo de 4, para imprimirlo como cuadernillo
Si la fuente cambia y una pagina deja de cuadrar, la puerta lo dice y no se
imprime nada.

    python pdf_idea.py --galera   mide cada bloque y sus lineas -> out3/pdf/galera.txt
    python pdf_idea.py            compone, comprueba e imprime
"""
import contextlib, html as H, io, json, os, re, subprocess, sys, datetime
from pathlib import Path

D = Path(__file__).resolve().parent
sys.path.insert(0, str(D))
with contextlib.redirect_stdout(io.StringIO()):     # assemble3 regenera las portadillas al cargarse
    from assemble3 import colofon, limpia_editorial, AUTOR, LICENCIA, NAV  # noqa: E402

FUENTE = D / 'p_tesis_es.html'
CSS = D / 'pdf' / 'idea.css'
FOTO = D / 'pdf' / 'portada.jpg'
OUT = D / 'out3' / 'pdf'
PDF_WEB = D.parent / 'docs' / 'la-idea.pdf'
PDF_LOCAL = D.parent / 'NOGUM_productos' / 'NOGUM_La_Idea.pdf'
WEB = 'https://epifaneia.dev/nogum/'
LINEAS = 46                                    # alto de la caja, en lineas de 15 pt
PRIMERA = 5                                    # el texto empieza en la pagina 5

FONTS = ('https://fonts.googleapis.com/css2?family=Ibarra+Real+Nova:ital,wght@0,400;0,600;0,700;1,400'
         '&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,700;1,8..60,400'
         '&family=JetBrains+Mono:wght@400;700&family=Big+Shoulders+Display:wght@800&display=block')

# ===================================================================== CORTES
# Donde empieza cada pagina de texto. Una cadena: la pagina abre con el
# bloque cuyo texto empieza asi. Una tupla (inicio, marca): la pagina abre
# DENTRO de ese parrafo, justo despues de la marca, que son las ultimas
# palabras que caben en la pagina anterior. Esto es lo que se toca a mano.
CORTES = [
    '1 · De qué va esto',                                           # p.5
    # p.6 · La 5 suelta cinco lineas para que la 6 llegue justo hasta la
    # entradilla. La 5 esta enfrente del indice: ahi un pie mas corto no se
    # compara con nada. En el pliego 6|7 si se compararia.
    ('Aquí está la incomodidad', 'te dan una ficha'),
    # p.7 · La entradilla abre pagina. La 6 acaba en «no hay ninguna razon
    # para girarlo solo una vez», y lo que lo remata esta al pasar la hoja.
    'No solo se puede adaptar el tono',
    # De la 7 a la 12 no hay composicion con todas las paginas a 46: el texto
    # no lo permite (309 composiciones validas, ninguna llena). Lo que si se
    # puede es que las dos paginas de cada pliego acaben a la misma altura,
    # que es lo que se ve: 6|7 a 46, 8|9 a 44, 10|11 a 45.
    'La vida: ¿cuánto aguanta un cuerpo?',                          # p.8, abre con el subtitulo
    ('Las probabilidades de las siete', 'y verificadas, y'),        # p.9
    'El primero es qué se hace con los dados',                      # p.10
    ('Pero un ancla crea un problema', 'el mundo compite'),         # p.11 (T158: «la Rejilla» corrio una palabra)
    ('Y a partir de ese momento el catálogo', 'hacen y no'),        # p.12, cierra la seccion 7
    # p.13 · El cierre abre pagina: es el final del libro y tiene que tener
    # su propia entrada. La 12 se queda corta, que es lo normal al acabar
    # una seccion.
    '8 · Cuatro piezas, una cosa',
    'Y por qué juntas son otra cosa',                               # p.14
]


# ================================================================ la fuente
def plano(h):
    return re.sub(r'\s+', ' ', H.unescape(re.sub(r'<[^>]+>', '', h))).strip()


def fuente():
    s = limpia_editorial(FUENTE.read_text(encoding='utf-8'))
    a = s.index('<section class="chapter cover"'); b = s.index('</section>', a)
    return s[a:b], s[b:]


def bloques():
    """El texto corrido, en orden: titulares de seccion, subtitulos y parrafos."""
    _, cuerpo = fuente()
    out = []
    for m in re.finditer(r'<(h2|h3)>(.*?)</\1>|<p( class="([^"]+)")?>(.*?)</p>', cuerpo, re.S):
        if m.group(1):
            out.append({'k': m.group(1), 'html': m.group(2).strip(), 'cl': ''})
        else:
            out.append({'k': 'p', 'html': m.group(5).strip(), 'cl': m.group(4) or ''})
    for i, b in enumerate(out):
        b['i'] = i; b['txt'] = plano(b['html'])
    # la unica referencia al manual: enlace vivo en el PDF y nota al margen en
    # papel. La nota va justo delante del enlace y sin «top»: asi cae a la
    # altura de la linea del enlace, no de la primera del parrafo.
    for b in out:
        if 'href="#ch1-maquinas"' in b['html']:
            nota = '<span class="nota"><b>Juego completo</b>§1.3 · La Sala de Máquinas</span>'
            b['html'] = b['html'].replace('<a href="#ch1-maquinas"',
                                          nota + '<a href="%sjuego.html#ch1-maquinas"' % WEB)
            b['nota'] = True
    return out


def busca(B, inicio):
    hits = [b for b in B if b['txt'].startswith(inicio)]
    if len(hits) != 1:
        raise SystemExit('CORTES: %d bloques empiezan por %r (tiene que ser uno)' % (len(hits), inicio))
    return hits[0]


# ============================================== partir un parrafo por dentro
def parte(html, marca):
    """Corta el HTML de un parrafo justo despues de la marca de texto.

    Cierra en la primera mitad las etiquetas que queden abiertas (una negrita
    a medias) y las reabre en la segunda, para que el corte no se note."""
    texto, mapa, pila, i = [], [], [], 0
    while i < len(html):
        c = html[i]
        if c == '<':
            j = html.index('>', i) + 1
            t = html[i:j]
            if t.startswith('</'):
                pila.pop()
            elif not t.endswith('/>'):
                pila.append((re.match(r'<(\w+)', t).group(1), t))
            i = j; continue
        if c == '&':
            j = html.index(';', i) + 1
            texto.append(H.unescape(html[i:j])); mapa.append((j, list(pila))); i = j; continue
        texto.append(c); mapa.append((i + 1, list(pila))); i += 1
    s = ''.join(texto)
    if s.count(marca) != 1:
        raise SystemExit('CORTES: la marca %r aparece %d veces en el parrafo %r'
                         % (marca, s.count(marca), s[:40]))
    fin, abiertas = mapa[s.index(marca) + len(marca) - 1]
    a = html[:fin] + ''.join('</%s>' % n for n, _ in reversed(abiertas))
    b = ''.join(t for _, t in abiertas) + html[fin:].lstrip()
    return a, b


# ============================================================== componer
def secciones(B):
    """num, titulo y lo que contiene cada seccion, para el indice."""
    S = []
    for b in B:
        if b['k'] == 'h2':
            n, t = b['txt'].split(' · ', 1)
            S.append({'i': b['i'], 'n': n, 't': t, 'h3': []})
        elif b['k'] == 'h3' and S:
            S[-1]['h3'].append(b['txt'])
    return S


def render(b, html=None, cl=''):
    html = b['html'] if html is None else html
    if b['k'] == 'h2':
        n, t = b['txt'].split(' · ', 1)
        return '<div class="h2"><span class="num">%s</span><h2>%s</h2></div>' % (n, H.escape(t))
    if b['k'] == 'h3':
        return '<h3>%s</h3>' % html
    cls = ' '.join(x for x in (b['cl'], cl, 'anotado' if 'class="nota"' in html else '') if x)
    return '<p%s>%s</p>' % (' class="%s"' % cls if cls else '', html)


def paginas_de_texto(B):
    """Aplica CORTES. Devuelve una lista de paginas, cada una con su HTML."""
    cortes = []
    for c in CORTES:
        ini, marca = (c, None) if isinstance(c, str) else c
        cortes.append((busca(B, ini)['i'], marca))
    if cortes[0] != (0, None):
        raise SystemExit('CORTES: la primera pagina tiene que empezar por el primer bloque')
    # un corte dentro del parrafo i va despues de un corte al principio de i;
    # dos cortes dentro del mismo parrafo dan la misma clave y no pasan
    claves = [(i, 1 if m else 0) for i, m in cortes]
    for (a, x), (b, y) in zip(claves, claves[1:]):
        if (b, y) <= (a, x):
            raise SystemExit('CORTES: fuera de orden o repetido en %r' % B[b]['txt'][:40])
    P = []
    for k, (i, marca) in enumerate(cortes):
        j, mj = cortes[k + 1] if k + 1 < len(cortes) else (len(B), None)
        trozos, sec = [], None
        for x in range(i, j + (1 if mj else 0)):
            b = B[x]
            if x == i and marca:                       # empieza dentro de un parrafo
                trozos.append(render(b, parte(b['html'], marca)[1], 'cont'))
            elif x == j and mj:                        # acaba dentro de un parrafo
                trozos.append(render(b, parte(b['html'], mj)[0], 'corta'))
            else:
                trozos.append(render(b))
        # la cornisa: la seccion en vigor al abrir la pagina
        for b in reversed(B[:i + 1]):
            if b['k'] == 'h2':
                sec = b['txt']; break
        P.append({'html': '\n'.join(trozos), 'sec': sec, 'h2': [B[x]['txt'] for x in range(i, j) if B[x]['k'] == 'h2'],
                  'abre': B[i]['k'] if not marca else 'cont'})
    return P


# ===================================================== las paginas de mueble
def cubierta(portada):
    lema = plano(portada['lede']).split('. ')[0] + '.'
    return ('<section class="page cubierta">'
            '<div class="arriba"><div class="marca"><i></i><i></i></div>'
            '<p class="kicker">%s</p><h1>NOGUM</h1></div>'
            '<img class="foto" src="%s" alt="">'
            '<div class="abajo"><p class="titulo">%s</p><p class="lema">%s</p>'
            '<p class="autor"><span>%s</span><span>%s</span></p></div></section>'
            % (portada['oficial'], FOTO.as_uri(), NAV['tesis'][0], lema, AUTOR, LICENCIA))


def creditos(traza):
    bl = []
    for m in re.finditer(r'<p( class="lede")?>(.*?)</p>', colofon('es'), re.S):
        cuerpo = m.group(2)
        t = re.match(r'<strong>([^<]+?)\.</strong>\s*(.*)', cuerpo, re.S)
        if m.group(1):
            bl.append(('Licencia', cuerpo))
        elif t:
            bl.append((t.group(1), t.group(2)))
    bl += [('Tipografía', 'Ibarra Real Nova, Source Serif 4, JetBrains Mono y Big Shoulders Display, '
                          'servidas por Google Fonts, cada una bajo su propia licencia.'),
           ('Cubierta', 'Imagen generada con inteligencia artificial. Queda fuera de la licencia '
                        'de esta obra.'),
           ('En la web', 'El juego completo, la versión rápida y la aplicación que lo configura, libres: '
                         '<a href="%s">epifaneia.dev/nogum</a>.' % WEB)]
    caja = ''.join('<div class="bloque"><b>%s</b><p>%s</p></div>' % b for b in bl)
    return ('<section class="page verso creditos"><div class="caja"><h2>Quién firma esto</h2>'
            '<p style="margin:0 0 6mm;font:italic 400 11pt/1.4 var(--ff-display)">NOGUM · %s. '
            'Edición en español, de %s.</p><div class="rejilla">%s</div>'
            '<p class="traza">%s</p></div></section>' % (NAV['tesis'][0], AUTOR, caja, traza))


def portadilla(portada):
    letras = portada['letras'].replace('·', '<span>·</span>')
    aparte = portada['aparte'].split(' Pulsa')[0]          # lo de pulsar es de pantalla
    bromas = ''.join('<li>%s</li>' % H.escape(x) for x in portada['bromas'])
    return ('<section class="page recto portadilla"><div class="caja">'
            '<p class="kicker">%s</p><p class="letras">%s</p><p class="oficial">%s</p>'
            '<p class="aparte">%s</p><ul class="bromas">%s</ul></div>'
            '<p class="entrada">%s</p></section>'
            % (portada['kicker'], letras, portada['oficial'], aparte, bromas, portada['lede']))


def indice(S, donde):
    li = ''.join('<li><span class="n">%s</span><span class="t">%s<small>%s</small></span>'
                 '<span class="p">%d</span></li>'
                 % (s['n'], H.escape(s['t']), H.escape(' · '.join(s['h3'])), donde[s['i']]) for s in S)
    return ('<section class="page verso indice"><div class="caja"><p class="kicker">%s</p>'
            '<h2>Todo lo que hay<br>aquí dentro</h2><ol>%s</ol></div></section>' % (NAV['tesis'][0], li))


def puertas(B):
    """Lo ultimo antes de la contracubierta: las otras tres piezas, con su
    enlace vivo. La seccion 8 ya dice a que responde cada una; de ahi sale."""
    P = [('El Acelerado', 'acelerado.html'), ('El Juego completo', 'juego.html'), ('La App', 'app.html')]
    li = ''
    for nombre, url in P:
        h = [b for b in B if b['k'] == 'h3' and b['txt'] == nombre][0]
        t = B[h['i'] + 1]['txt']
        # «Responde a ya: se puede empezar esta misma tarde...» -> la palabra
        # va grande, y lo que hay detras de los dos puntos va de descripcion
        m = re.search(r'Responde a (\w+)[^:.]*: ([^.]+\.)', t)
        q, detras = m.group(1), m.group(2)
        desc = t.split('. ')[0] + '. ' + detras[0].upper() + detras[1:]
        li += ('<li><span class="q"><small>Responde a</small>%s</span><span class="d"><b>%s</b>'
               '<span>%s</span><a href="%s%s">epifaneia.dev/nogum/%s</a></span></li>'
               % (q, nombre, H.escape(desc), WEB, url, url))
    return ('<section class="page recto puertas"><div class="caja"><p class="kicker">Por dónde seguir</p>'
            '<h2>Tres puertas</h2><ol>%s</ol></div><p class="pie">El código, las fuentes y el diario '
            'de diseño, con cada decisión y su porqué: <a href="https://github.com/epifaneia/nogum">'
            'github.com/epifaneia/nogum</a></p></section>' % li)


def contra(B):
    """La tesis entera, con las palabras del propio libro: el salto, las tres
    emociones que puede dar, y quien decide cual."""
    gancho = busca(B, 'Imagina un salto')['html']
    cuerpo = ''.join('<p>%s</p>' % busca(B, x)['html']
                     for x in ('Puede producir', 'Nada de eso lo decide el género'))
    cuatro = ' · '.join(b['txt'] for b in B if b['k'] == 'h3'
                        and b['txt'] in ('La Idea', 'El Juego completo', 'El Acelerado', 'La App'))
    return ('<section class="page verso contra"><div class="dentro"><div class="marca"><i></i><i></i></div>'
            '<p class="gancho">%s</p><div class="cuerpo">%s</div></div>'
            '<p class="cuatro">Una idea, cuatro piezas: %s</p>'
            '<div class="pie"><a class="url" href="%s">epifaneia.dev/nogum</a>'
            '<p class="lic">%s<br>%s</p></div></section>' % (gancho, cuerpo, cuatro, WEB, AUTOR, LICENCIA))


def de_la_portada(sec):
    g = lambda c: plano(re.search(r'<p class="%s"[^>]*>(.*?)</p>' % c, sec, re.S).group(1))
    return {'kicker': g('acro-kicker'), 'letras': g('acro-letters'), 'oficial': g('acro-official'),
            'bromas': H.unescape(re.search(r'data-jokes="([^"]+)"', sec).group(1)).split('|'),
            'aparte': plano(re.search(r'<aside class="meta"><p>(.*?)</p>', sec, re.S).group(1)),
            'lede': re.search(r'<p class="lede">(.*?)</p>', sec, re.S).group(1)}


# ================================================================== montar
MIDE = r'''<pre id="medidas" style="display:none">pendiente</pre><script>
document.fonts.ready.then(function(){
  var lh = 15 * 96 / 72, out = [];
  document.querySelectorAll('.page').forEach(function(pg, n){
    var o = {p: n + 1}, inn = pg.querySelector('.inner');
    if (inn) {
      var r0 = inn.getBoundingClientRect(), k = inn.children, last = k[k.length - 1];
      o.cap = inn.clientHeight / lh;
      o.usa = last ? (last.getBoundingClientRect().bottom - r0.top) / lh : 0;
      o.sale = inn.scrollHeight > inn.clientHeight + 1;
      o.ult = last ? (last.classList.contains('h2') ? 'h2' : last.tagName.toLowerCase()) : '';
      var c = inn.querySelector('p.cont'), t = inn.querySelector('p.corta');
      if (c) o.cont = Math.round(c.getBoundingClientRect().height / lh);
      if (t) o.corta = Math.round(t.getBoundingClientRect().height / lh);
      // la rejilla: todo parrafo de texto empieza en una linea entera
      o.fuera = [];
      inn.querySelectorAll('p:not(.lede):not(.signoff)').forEach(function(x){
        var y = (x.getBoundingClientRect().top - r0.top) / lh;
        if (Math.abs(y - Math.round(y)) > .05) o.fuera.push(x.textContent.slice(0, 30) + ' (' + y.toFixed(2) + ')');
      });
      pg.querySelectorAll('.nota').forEach(function(x){
        if (x.getBoundingClientRect().bottom > r0.bottom + 1) o.notasale = true; });
    }
    // lo del margen tiene que VERSE. Se sube por sus antecesores y, en cada
    // uno que recorte, se comprueba que cabe dentro de su caja. Sin
    // scrollIntoView(): una caja con overflow:hidden se puede desplazar por
    // codigo, y la comprobacion anterior desplazaba el texto hasta hacer
    // «visible» lo que estaba recortado.
    pg.querySelectorAll('.h2 .num, .nota').forEach(function(x){
      var r = x.getBoundingClientRect();
      for (var a = x.parentElement; a; a = a.parentElement) {
        var cs = getComputedStyle(a);
        if (cs.overflowX === 'visible' && cs.overflowY === 'visible') continue;
        var q = a.getBoundingClientRect();
        if (r.left < q.left - .5 || r.right > q.right + .5 || r.top < q.top - .5 || r.bottom > q.bottom + .5) {
          o.oculto = (o.oculto || '') + x.textContent.slice(0, 24) + '; '; break;
        }
      }
    });
    var pr = pg.getBoundingClientRect(), mb = pg.querySelectorAll('.caja, .dentro, .abajo, .arriba, .entrada, .pie, .foto, .cuatro');
    mb.forEach(function(x){
      var r = x.getBoundingClientRect();
      if (r.bottom > pr.bottom - 8 || r.top < pr.top + 8) o.mueble = (o.mueble || '') + x.className + ' se sale; ';
    });
    for (var a = 0; a < mb.length; a++) for (var b = a + 1; b < mb.length; b++) {
      var p = mb[a].getBoundingClientRect(), q = mb[b].getBoundingClientRect();
      if (p.left < q.right && q.left < p.right && p.top < q.bottom - 2 && q.top < p.bottom - 2)
        o.mueble = (o.mueble || '') + mb[a].className + ' pisa ' + mb[b].className + '; ';
    }
    out.push(o);
  });
  document.getElementById('medidas').textContent = JSON.stringify(out);
});
</script>'''

GALERA = r'''<pre id="medidas" style="display:none">pendiente</pre><script>
document.fonts.ready.then(function(){
  var lh = 15 * 96 / 72, inn = document.querySelector('.galera .inner'), k = inn.children, out = [];
  function lineas(p){
    var w = document.createTreeWalker(p, NodeFilter.SHOW_TEXT), r = document.createRange(), L = [], cur = '', top = null;
    while (w.nextNode()) {
      var t = w.currentNode;
      if (t.parentNode.closest && t.parentNode.closest('.nota')) continue;
      for (var i = 0; i < t.length; i++) {
        r.setStart(t, i); r.setEnd(t, i + 1);
        var q = r.getClientRects();
        if (q.length) { var y = q[0].top; if (top !== null && y > top + 4) { L.push(cur); cur = ''; } if (top === null || y > top + 4) top = y; }
        cur += t.data[i];
      }
    }
    L.push(cur); return L;
  }
  var y0 = inn.getBoundingClientRect().top;
  for (var i = 0; i < k.length; i++) {
    var a = k[i].getBoundingClientRect().top - y0;
    var b = i + 1 < k.length ? k[i + 1].getBoundingClientRect().top - y0 : inn.getBoundingClientRect().height;
    var o = {i: i, alto: (b - a) / lh};
    if (k[i].tagName === 'P') o.L = lineas(k[i]);
    out.push(o);
  }
  document.getElementById('medidas').textContent = JSON.stringify(out);
});
</script>'''


def documento(paginas, script):
    css = CSS.read_text(encoding='utf-8')
    return ('<!doctype html>\n<html lang="es"><head><meta charset="utf-8">'
            '<title>NOGUM · %s</title><link rel="stylesheet" href="%s"><style>%s</style></head>\n'
            '<body>\n%s\n%s</body></html>\n' % (NAV['tesis'][0], FONTS, css, '\n'.join(paginas), script))


def pagina_texto(n, pg):
    lado = 'recto' if n % 2 else 'verso'
    sec = pg['sec'] or ''
    return ('<section class="page %s texto"><div class="runhead"><span class="sub">NOGUM · %s</span>'
            '<span>%s</span></div><div class="inner">\n%s\n</div>'
            '<span class="folio-book">epifaneia.dev/nogum</span><span class="folio">%d</span></section>'
            % (lado, NAV['tesis'][0], H.escape(sec), pg['html'], n))


def chrome():
    for c in (os.environ.get('NOGUM_CHROME'),
              r'C:\Program Files\Google\Chrome\Application\chrome.exe',
              r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
              r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
              '/usr/bin/google-chrome', '/usr/bin/chromium'):
        if c and os.path.exists(c):
            return c
    raise SystemExit('No encuentro Chrome. Pon su ruta en NOGUM_CHROME.')


def mide(fichero):
    r = subprocess.run([chrome(), '--headless=new', '--disable-gpu', '--virtual-time-budget=20000',
                        '--dump-dom', fichero.as_uri()], capture_output=True, timeout=120)
    m = re.search(r'<pre id="medidas"[^>]*>(.*?)</pre>', r.stdout.decode('utf-8', 'replace'), re.S)
    if not m or m.group(1).strip() == 'pendiente':
        raise SystemExit('Chrome no ha devuelto medidas (¿sin red para las fuentes?)')
    return json.loads(H.unescape(m.group(1)))


def imprime(fichero, destino):
    destino.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([chrome(), '--headless=new', '--disable-gpu', '--virtual-time-budget=20000',
                    '--no-pdf-header-footer', '--print-to-pdf=' + str(destino), fichero.as_uri()],
                   capture_output=True, timeout=180)
    if not destino.exists():
        raise SystemExit('Chrome no ha escrito %s' % destino)


def traza():
    try:
        h = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'], capture_output=True, text=True,
                           cwd=D).stdout.strip()
    except Exception:
        h = '?'
    return 'Compuesto el %s · %s · desde %s' % (datetime.date.today().isoformat(), h, FUENTE.name)


# =================================================================== galera
def galera():
    B = bloques()
    OUT.mkdir(parents=True, exist_ok=True)
    f = OUT / 'galera.html'
    f.write_text(documento(['<section class="galera recto"><div class="inner">%s</div></section>'
                            % '\n'.join(render(b) for b in B)], GALERA), encoding='utf-8')
    M = mide(f)
    out, acum = [], 0.0
    for b, m in zip(B, M):
        acum += m['alto']
        out.append('%3d %-3s %5.1f  %6.1f   %s' % (b['i'], b['k'], m['alto'], acum, b['txt'][:64]))
        for n, l in enumerate(m.get('L', [])):
            sig = m['L'][n + 1] if n + 1 < len(m['L']) else ''
            guion = '-' if l and sig and l[-1].isalpha() and sig[0].isalpha() else ' '
            out.append('            %2d| %s%s' % (n + 1, l.strip()[-58:].rjust(58), guion))
    t = '\n'.join(out)
    (OUT / 'galera.txt').write_text(t, encoding='utf-8')
    print(t)
    print('\ncaja: %d lineas por pagina · total %.1f lineas = %.2f cajas llenas' % (LINEAS, acum, acum / LINEAS))


# ================================================================== compone
def compone():
    B = bloques()
    portada = de_la_portada(fuente()[0])
    T = paginas_de_texto(B)
    S = secciones(B)
    donde = {}
    for k, pg in enumerate(T):
        for b in B:
            if b['k'] == 'h2' and b['txt'] in pg['h2']:
                donde[b['i']] = PRIMERA + k
    paginas = [cubierta(portada), creditos(traza()), portadilla(portada), indice(S, donde)]
    paginas += [pagina_texto(PRIMERA + k, pg) for k, pg in enumerate(T)]
    paginas += [puertas(B), contra(B)]
    OUT.mkdir(parents=True, exist_ok=True)
    f = OUT / 'la-idea.html'
    f.write_text(documento(paginas, MIDE), encoding='utf-8')
    M = mide(f)

    # --------------------------------------------------------- la puerta
    fallos, avisos = [], []
    tipo = {1: 'cubierta', 2: 'créditos', 3: 'portadilla', 4: 'índice',
            len(paginas) - 1: 'puertas', len(paginas): 'contra'}
    if len(paginas) - 1 != PRIMERA + len(T) or (len(paginas) - 1) % 2 == 0:
        fallos.append('las puertas tienen que caer en una pagina impar, justo detras del texto')
    print('\n pág  tipo         usa/caja  llena  sección')
    for m in M:
        n = m['p']
        if m.get('mueble'):
            fallos.append('p.%d: el mueble se sale de la pagina (%s)' % (n, m['mueble'].strip()))
        if m.get('oculto'):
            fallos.append('p.%d: hay algo en el margen que no se ve: %s' % (n, m['oculto'].strip()))
        if 'cap' not in m:
            print(' %3d  %-11s' % (n, tipo.get(n, '?')))
            continue
        pg = T[n - PRIMERA]
        lleno = m['usa'] / m['cap']
        ultima = n - PRIMERA == len(T) - 1
        sig_abre = T[n - PRIMERA + 1]['abre'] if not ultima else None
        print(' %3d  %-11s %5.1f/%2.0f  %4.0f%%  %s' % (n, 'texto', m['usa'], m['cap'], lleno * 100, pg['sec']))
        if m['sale']:
            fallos.append('p.%d: el texto se DESBORDA (%.1f lineas en una caja de %.0f)' % (n, m['usa'], m['cap']))
        if m.get('notasale'):
            fallos.append('p.%d: una nota al margen se sale por abajo' % n)
        if m['ult'] in ('h2', 'h3'):
            fallos.append('p.%d: titular huerfano al pie de la pagina' % n)
        if m.get('corta', 9) < 2:
            fallos.append('p.%d: el parrafo partido deja %d linea al pie' % (n, m['corta']))
        if m.get('cont', 9) < 2:
            fallos.append('p.%d: el parrafo partido deja %d linea arriba (viuda)' % (n, m['cont']))
        for x in m.get('fuera', []):
            fallos.append('p.%d: fuera de la rejilla: %s' % (n, x))
        m['fin_seccion'] = ultima or sig_abre == 'h2'
    # Los pliegos. Un libro se lee de dos en dos paginas, y lo que se ve es si
    # las dos acaban a la misma altura. Una pagina de texto frente al indice o
    # frente a las puertas no se compara con nada; una que cierra seccion
    # puede quedarse corta.
    T_ = {m['p']: m for m in M if 'cap' in m}
    for iz in range(2, len(paginas) + 1, 2):
        a, b = T_.get(iz), T_.get(iz + 1)
        if a and b and not (a['fin_seccion'] or b['fin_seccion']) and abs(a['usa'] - b['usa']) >= 1:
            avisos.append('pliego %d|%d: acaban a %.1f y %.1f lineas' % (iz, iz + 1, a['usa'], b['usa']))
    if len(paginas) % 4:
        fallos.append('%d paginas: para un cuadernillo tienen que ser multiplo de 4' % len(paginas))
    for a in avisos:
        print('  aviso  ' + a)
    if fallos:
        print('\nNO SE IMPRIME:')
        for x in fallos:
            print('  ' + x)
        if '--forzar' not in sys.argv:
            raise SystemExit(1)
    imprime(f, PDF_WEB)
    PDF_LOCAL.parent.mkdir(parents=True, exist_ok=True)
    PDF_LOCAL.write_bytes(PDF_WEB.read_bytes())
    print('\n%d paginas · %s (%d KB)' % (len(paginas), PDF_WEB.relative_to(D.parent), PDF_WEB.stat().st_size // 1024))


if __name__ == '__main__':
    galera() if '--galera' in sys.argv else compone()
