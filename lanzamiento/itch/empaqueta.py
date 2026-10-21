# Rehace los tres archivos de itch.io: el pack sin conexion (libros en HTML y
# la App) y los PDF por idioma. Antes: compilar (src/) y sacar los PDF con
# hacer_pdf.js en lanzamiento/itch/pdf. Se ejecuta desde la raiz del repositorio.
import zipfile, os
IT = 'lanzamiento/itch'
LEEME = """NOGUM · de Daniel Martín · CC BY-SA 4.0

Empieza por NOGUM_productos/NOGUM_idea.html (La Idea).
La App está en NOGUM_app/NOGUM_app.html. Todo se abre en el navegador, sin instalar nada.
Con conexión se ven las fuentes del libro; sin ella, las del sistema.
Los libros en PDF, para leer en pantalla o para imprimir, van aparte en esta misma página.
La versión siempre al día está en https://epifaneia.dev/nogum/

Start with NOGUM_productos/NOGUM_idea.html (The Idea).
The App is in NOGUM_app/NOGUM_app.html. Everything opens in your browser, nothing to install.
Online you get the book's fonts; offline, your system's.
The books as PDF, for reading on screen or for printing, are a separate download on this same page.
The always up-to-date version lives at https://epifaneia.dev/nogum/
"""
PDF_LEE = {'ES': """NOGUM · de Daniel Martín · CC BY-SA 4.0

Tres libros, cada uno en dos versiones:
- «pantalla»: el papel crema de la web y la portada con su imagen. Para leer en el ordenador o en una tableta.
- «papel»: hojas blancas y portada clara, para imprimir sin gastar media tinta.

Empieza por La Idea. Para jugar esta noche, el Acelerado.
La versión siempre al día, y la App, en https://epifaneia.dev/nogum/
""", 'EN': """NOGUM · by Daniel Martín · CC BY-SA 4.0

Three books, each in two versions:
- "screen": the site's cream paper and the cover with its image. For reading on a computer or a tablet.
- "paper": white pages and a light cover, to print without wasting half your ink.

Start with The Idea. To play tonight, the Accelerated.
The always up-to-date version, and the App, at https://epifaneia.dev/nogum/
"""}
with zipfile.ZipFile(IT + '/NOGUM-sin-conexion.zip', 'w', zipfile.ZIP_DEFLATED) as z:
    for f in ['NOGUM_idea.html', 'NOGUM_juego.html', 'NOGUM_acelerado.html']:
        z.write('NOGUM_productos/' + f, 'NOGUM/NOGUM_productos/' + f)
    for f in sorted(os.listdir('NOGUM_productos/img')):
        z.write('NOGUM_productos/img/' + f, 'NOGUM/NOGUM_productos/img/' + f)
    z.write('NOGUM_app/NOGUM_app.html', 'NOGUM/NOGUM_app/NOGUM_app.html')
    z.write('LICENSE', 'NOGUM/LICENSE.txt')
    z.writestr('NOGUM/LEEME - README.txt', LEEME)
for lang in ['ES', 'EN']:
    with zipfile.ZipFile(IT + '/NOGUM-PDF-' + lang + '.zip', 'w', zipfile.ZIP_DEFLATED) as z:
        for f in sorted(os.listdir(IT + '/pdf')):
            if '-' + lang + '-' in f: z.write(IT + '/pdf/' + f, 'NOGUM-PDF-' + lang + '/' + f)
        z.writestr('NOGUM-PDF-' + lang + '/' + ('LEEME' if lang == 'ES' else 'README') + '.txt', PDF_LEE[lang])
for f in ['NOGUM-sin-conexion.zip', 'NOGUM-PDF-ES.zip', 'NOGUM-PDF-EN.zip']:
    print(f, round(os.path.getsize(IT + '/' + f) / 1e6, 1), 'MB')
