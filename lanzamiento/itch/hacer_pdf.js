// Saca los PDF de los libros, en los dos modos del menu de imprimir.
// Necesita el servidor local en el puerto 8777 (raiz del repositorio) y
// puppeteer-core; PERFIL puede apuntar a un perfil de Chrome con los
// diccionarios de particion silabica (hyphen-data), si no, no parte palabras.
//   node hacer_pdf.js pdf [libros] [langs] [modos]
const puppeteer = require('puppeteer-core');
const path = require('path'), fs = require('fs');
const OUT = process.argv[2];
const LIBROS = (process.argv[3] || 'idea,acelerado,juego').split(',');
const LANGS = (process.argv[4] || 'es,en').split(',');
const MODOS = (process.argv[5] || 'pantalla,papel').split(',');
const NOMBRE = { idea: { es: 'La-Idea', en: 'The-Idea' }, acelerado: { es: 'Acelerado', en: 'Accelerated' }, juego: { es: 'Juego-completo', en: 'Complete-Game' } };
const MODO = { pantalla: { es: 'pantalla', en: 'screen' }, papel: { es: 'papel', en: 'paper' } };
(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const b = await puppeteer.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe', headless: 'new', userDataDir: process.env.PERFIL || undefined });
  for (const l of LIBROS) for (const lang of LANGS) {
    const p = await b.newPage(); await p.setCacheEnabled(false);
    await p.evaluateOnNewDocument(() => { try { localStorage.clear(); } catch (e) {} });
    await p.setViewport({ width: 1400, height: 1150 });
    await p.goto(`http://localhost:8777/docs/${WEB(l)}?lang=${lang}`, { waitUntil: 'networkidle0', timeout: 120000 });
    await p.waitForFunction(() => /p[áa]ginas|pages/i.test((document.getElementById('status') || {}).textContent || ''), { timeout: 240000 });
    await p.evaluate(() => document.fonts.ready);
    for (const m of MODOS) {
      await p.evaluate(m => document.documentElement.setAttribute('data-print', m), m);
      const f = path.join(OUT, `NOGUM-${NOMBRE[l][lang]}-${lang.toUpperCase()}-${MODO[m][lang]}.pdf`);
      await p.pdf({ path: f, preferCSSPageSize: true, printBackground: true, timeout: 600000 });
      console.log(f, Math.round(fs.statSync(f).size / 1024) + ' KB');
    }
    await p.close();
  }
  await b.close();
})();
function WEB(l) { return { idea: 'idea.html', acelerado: 'acelerado.html', juego: 'juego.html' }[l]; }
