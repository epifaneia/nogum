// Imprime los tres libros a PDF con Chrome sin ventana, como lo haria el
// boton «Imprimir» del propio libro, y guarda al lado el indice (titulo,
// nivel y pagina de cada apartado) para ponerle marcadores despues.
//   node src/pdf/imprime.mjs <carpeta-salida>
// Necesita el servidor estatico en localhost:8777 sirviendo la raiz del repo.
import { spawn } from 'node:child_process';
import { writeFileSync, mkdirSync, mkdtempSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const BASE = 'http://localhost:8777/NOGUM_productos/';
const OUT = process.argv[2] || 'pdf';
const PORT = 9333;
mkdirSync(OUT, { recursive: true });

const LIBROS = [
  { f: 'NOGUM_juego.html', es: 'NOGUM · Juego completo', en: 'NOGUM · Complete Game' },
  { f: 'NOGUM_acelerado.html', es: 'NOGUM · Acelerado', en: 'NOGUM · Accelerated' },
  { f: 'NOGUM_idea.html', es: 'NOGUM · La Idea', en: 'NOGUM · The Idea' },
];
// «pantalla»: el crema y la portada con su imagen (para leer en PDF);
// «papel»: hojas blancas y portada clara (para imprimir en casa).
const MODOS = [{ m: 'pantalla', es: '', en: '' }, { m: 'papel', es: ' (papel)', en: ' (paper)' }];

const sleep = ms => new Promise(r => setTimeout(r, ms));
const chrome = spawn(CHROME, ['--headless=new', `--remote-debugging-port=${PORT}`,
  `--user-data-dir=${mkdtempSync(join(tmpdir(), 'nogum-pdf-'))}`, '--no-first-run',
  '--no-default-browser-check', '--hide-scrollbars', 'about:blank'], { stdio: 'ignore' });

async function pagina() {
  for (let i = 0; i < 50; i++) {
    try {
      const l = await (await fetch(`http://127.0.0.1:${PORT}/json/list`)).json();
      const p = l.find(t => t.type === 'page');
      if (p) return p.webSocketDebuggerUrl;
    } catch (e) { /* todavia arrancando */ }
    await sleep(200);
  }
  throw new Error('Chrome no responde');
}

const ws = new WebSocket(await pagina());
await new Promise(r => ws.addEventListener('open', r, { once: true }));
let id = 0; const esperas = new Map();
ws.addEventListener('message', ev => {
  const m = JSON.parse(ev.data);
  if (m.id && esperas.has(m.id)) { const { ok, ko } = esperas.get(m.id); esperas.delete(m.id); m.error ? ko(new Error(m.error.message)) : ok(m.result); }
});
const cdp = (method, params = {}) => new Promise((ok, ko) => { const n = ++id; esperas.set(n, { ok, ko }); ws.send(JSON.stringify({ id: n, method, params })); });
const js = async expr => (await cdp('Runtime.evaluate', { expression: expr, returnByValue: true, awaitPromise: true })).result.value;

await cdp('Page.enable');
await cdp('Emulation.setDeviceMetricsOverride', { width: 1400, height: 1000, deviceScaleFactor: 1, mobile: false });

for (const libro of LIBROS) for (const lang of ['es', 'en']) {
  await cdp('Page.navigate', { url: `${BASE}${libro.f}?lang=${lang}&pdf=${Date.now()}` });
  // espera a que el maquetador termine: «N páginas · A4» / «N pages · A4»
  let estado = '';
  for (let i = 0; i < 300; i++) {
    await sleep(500);
    estado = await js(`(document.getElementById('status')||{}).textContent||''`) || '';
    if (/·\s*A4/.test(estado)) break;
  }
  if (!/·\s*A4/.test(estado)) throw new Error(`${libro.f} ${lang}: no termina de maquetar (${estado})`);
  await sleep(800);
  const indice = await js(`[...document.querySelectorAll('#stoc > li')].map(li => ({
      nivel: li.className === 'l3' ? 3 : 2,
      titulo: li.querySelector('a span').textContent.trim(),
      pagina: +(li.querySelector('.n').textContent || 0) }))`);
  const paginas = await js(`document.querySelectorAll('#book .sheet').length`);
  for (const modo of MODOS) {
    await js(`document.documentElement.setAttribute('data-print', '${modo.m}'); true`);
    await sleep(300);
    const { data } = await cdp('Page.printToPDF', { printBackground: true, preferCSSPageSize: true,
      displayHeaderFooter: false, marginTop: 0, marginBottom: 0, marginLeft: 0, marginRight: 0 });
    const nombre = `${libro[lang]}${modo[lang]}`;
    writeFileSync(join(OUT, `${nombre}.pdf`), Buffer.from(data, 'base64'));
    writeFileSync(join(OUT, `${nombre}.json`), JSON.stringify({ titulo: libro[lang], lang, modo: modo.m, paginas, indice }, null, 1));
    console.log(`${nombre}.pdf · ${paginas} páginas · ${indice.length} apartados`);
  }
  await js(`document.documentElement.removeAttribute('data-print'); true`);
}
ws.close(); chrome.kill();
