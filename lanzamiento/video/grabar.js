// Graba el vídeo de demostración de la App: una partida de NOGUM Acelerado en
// Innsmouth, de la portada a la primera tirada. Cursor y subtítulos van
// inyectados en la página, así que salen en la captura tal cual.
//   node grabar.js        -> graba (frames + tiempos + subtítulos .srt)
//   node grabar.js seco   -> solo hace fotos de control, sin grabar
// Necesita puppeteer-core, Chrome y la web servida en http://localhost:8777
// (python -m http.server 8777 desde la raíz del repo). Después, con ffmpeg:
//   ffmpeg -f concat -safe 0 -i <tmp>/nogum-video/lista.txt -vf "fps=30,scale=1920:1080:flags=lanczos:in_range=pc:out_range=tv,setsar=1,format=yuv420p" -c:v libx264 -preset slow -crf 18 -movflags +faststart nogum-app-innsmouth.mp4
const puppeteer = require('puppeteer-core'); const path = require('path'); const fs = require('fs');
const SECO = process.argv[2] === 'seco';
// los fotogramas van a la carpeta temporal: son miles y no se versionan
const OUT = path.join(require('os').tmpdir(), 'nogum-video'); const FR = path.join(OUT, 'frames');
fs.rmSync(OUT, { recursive: true, force: true }); fs.mkdirSync(FR, { recursive: true });
const ESPERA = ms => new Promise(r => setTimeout(r, ms));

const LORE = fs.readFileSync(path.join(__dirname, 'innsmouth.txt'), 'utf8').split('\n=====\n');

process.on('unhandledRejection', async e => { console.error(e.message); try { await global.pg.screenshot({ path: path.join(OUT, 'FALLO.png') }); } catch (x) {} process.exit(1); });
(async () => {
  const b = await puppeteer.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe', headless: 'new', defaultViewport: null, args: ['--hide-scrollbars', '--force-color-profile=srgb', '--force-device-scale-factor=1.5', '--window-size=1296,815'] });
  const p = (await b.pages())[0] || await b.newPage(); global.pg = p;
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  // la mesa arranca vacía; solo la historia de la campaña viene escrita de casa
  await p.goto('http://localhost:8777/docs/app.html?lang=es', { waitUntil: 'networkidle0' });
  await p.evaluate((lore, secreto) => {
    localStorage.clear(); localStorage.setItem('nogum-lang', 'es'); localStorage.setItem('nogum-theme-app', '"light"');
    localStorage.setItem('nogum-app3', JSON.stringify({ lang: 'es', story: { pc: ['', '', '', '', ''], common: lore, secret: secreto, pw: null } }));
  }, LORE[0].trim(), LORE[1].trim());
  await p.goto('http://localhost:8777/docs/app.html', { waitUntil: 'networkidle0' });
  await p.evaluate(() => document.fonts.ready);
  const caja = await p.evaluate(() => [innerWidth, innerHeight, devicePixelRatio]);
  if (caja[0] !== 1280 || caja[1] < 720 || caja[2] !== 1.5) throw new Error('la ventana mide ' + caja);

  // ---- el escenario: cursor y subtítulos ----
  const escena = () => {
    if (document.getElementById('vcur')) return;
    const st = document.createElement('style');
    st.textContent = `
      #vcur{position:fixed;left:0;top:0;z-index:2147483647;pointer-events:none;width:30px;height:30px;
        transform:translate(var(--x,640px),var(--y,800px));transition:transform var(--d,700ms) cubic-bezier(.45,.05,.25,1)}
      #vcur svg{display:block;filter:drop-shadow(0 2px 3px rgba(0,0,0,.35))}
      #vcur i{position:absolute;left:-14px;top:-14px;width:28px;height:28px;border-radius:50%;background:rgba(184,50,58,.45);transform:scale(0);opacity:0}
      #vcur.pulsa i{animation:vpulsa .45s ease-out}
      @keyframes vpulsa{0%{transform:scale(.2);opacity:1}100%{transform:scale(1.6);opacity:0}}
      #vsub{position:fixed;left:50%;bottom:18px;transform:translateX(-50%);z-index:2147483646;pointer-events:none;
        max-width:1040px;width:max-content;box-sizing:border-box;padding:10px 22px 11px;border-radius:10px;
        background:rgba(20,17,14,.86);color:#f5efe3;font:500 22px/1.35 "Source Serif 4",Georgia,serif;text-align:center;
        opacity:0;transition:opacity .35s}
      #vsub.on{opacity:1}
      #vsub b{color:#f07378;font-weight:600}
      #vtit{position:fixed;inset:0;z-index:2147483645;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;
        background:#1c1814;color:#ede6d9;opacity:0;transition:opacity .8s;pointer-events:none}
      #vtit.on{opacity:1}
      #vtit h1{margin:0;font:700 120px/1 "Big Shoulders Display",Impact,sans-serif;letter-spacing:.02em}
      #vtit p{margin:0;font:400 28px/1.3 "Source Serif 4",Georgia,serif;color:#cbbfa9}
      #vtit small{font:500 18px/1 "JetBrains Mono",Consolas,monospace;color:#f07378;letter-spacing:.08em;margin-top:18px}`;
    document.head.appendChild(st);
    const c = document.createElement('div'); c.id = 'vcur';
    c.innerHTML = '<i></i><svg width="26" height="30" viewBox="0 0 26 30"><path d="M2 2 L2 24 L8 18.5 L12.5 28 L16.5 26.2 L12 17 L20 17 Z" fill="#fff" stroke="#14110e" stroke-width="2" stroke-linejoin="round"/></svg>';
    document.body.appendChild(c);
    const s = document.createElement('div'); s.id = 'vsub'; document.body.appendChild(s);
    const tt = document.createElement('div'); tt.id = 'vtit'; document.body.appendChild(tt);
  };
  await p.evaluate(escena);
  // la app repinta el cuerpo de la vista, pero el cursor cuelga de body: si
  // algo lo borra, se vuelve a poner
  const asegura = () => p.evaluate(escena).then(() => p.evaluate(() => document.querySelectorAll('input,textarea').forEach(e => { e.spellcheck = false; })));

  // ---- la grabación ----
  const cdp = await p.createCDPSession(); const tiempos = []; let nf = 0, t0 = null;
  if (!SECO) {
    cdp.on('Page.screencastFrame', async ({ data, metadata, sessionId }) => {
      const f = path.join(FR, 'f' + String(++nf).padStart(5, '0') + '.jpg');
      fs.writeFileSync(f, Buffer.from(data, 'base64'));
      tiempos.push([f, metadata.timestamp]); if (t0 === null) t0 = metadata.timestamp;
      cdp.send('Page.screencastFrameAck', { sessionId }).catch(() => {});
    });
    await cdp.send('Page.startScreencast', { format: 'jpeg', quality: 94, maxWidth: 1920, maxHeight: 1080, everyNthFrame: 1 });
  }
  const inicio = Date.now() / 1000;
  const subs = []; let subHasta = 0, subAbierto = null;
  const ahora = () => Date.now() / 1000 - inicio;

  // un subtítulo se queda al menos lo que tarda en leerse
  async function sub(txt, minimo) {
    const falta = subHasta - Date.now(); if (falta > 0) await ESPERA(falta);
    await asegura();
    if (subAbierto) { subAbierto.fin = ahora(); }
    await p.evaluate(h => { const s = document.getElementById('vsub'); s.classList.remove('on'); }, txt);
    await ESPERA(260);
    await p.evaluate(h => { const s = document.getElementById('vsub'); s.innerHTML = h; s.classList.add('on'); }, txt);
    const limpio = txt.replace(/<[^>]+>/g, '');
    subAbierto = { ini: ahora(), fin: null, txt: limpio }; subs.push(subAbierto);
    subHasta = Date.now() + (minimo || Math.max(2600, limpio.length * 62));
  }
  async function finSub() {
    const falta = subHasta - Date.now(); if (falta > 0) await ESPERA(falta);
    await p.evaluate(() => document.getElementById('vsub').classList.remove('on'));
    if (subAbierto) { subAbierto.fin = ahora(); subAbierto = null; }
  }
  let fotos = 0;
  const foto = async tag => { if (SECO) await p.screenshot({ path: path.join(OUT, String(++fotos).padStart(2, '0') + '-' + tag + '.png') }); };

  // mueve el cursor al centro de un elemento (desplazando la página si hace falta)
  async function apunta(sel, dur) {
    await asegura();
    await p.waitForSelector(sel, { visible: true, timeout: 8000 });
    const fuera = await p.evaluate(s => {
      const r = document.querySelector(s).getBoundingClientRect();
      return r.top < 70 || r.bottom > innerHeight - 150;
    }, sel);
    if (fuera) {
      await p.evaluate(s => {
        const el = document.querySelector(s), r = el.getBoundingClientRect();
        scrollBy({ top: r.top - innerHeight * 0.38, behavior: 'smooth' });
      }, sel);
      await quieto();
    }
    const pos = await p.evaluate(s => { const r = document.querySelector(s).getBoundingClientRect(); return { x: r.left + Math.min(r.width / 2, 160), y: r.top + r.height / 2 }; }, sel);
    await p.evaluate((x, y, d) => { const c = document.getElementById('vcur'); c.style.setProperty('--d', d + 'ms'); c.style.setProperty('--x', x + 'px'); c.style.setProperty('--y', y + 'px'); }, pos.x, pos.y, dur || 650);
    await ESPERA((dur || 650) + 120);
    return pos;
  }
  async function pulsa(sel, dur, despues) {
    if (sel.endsWith('@ultimo')) {
      sel = await p.evaluate(s => { const t = [...document.querySelectorAll(s)].filter(e => e.getBoundingClientRect().width > 0).pop(); document.querySelectorAll('[data-vult]').forEach(e => e.removeAttribute('data-vult')); t.setAttribute('data-vult', '1'); return '[data-vult]'; }, sel.slice(0, -7));
    }
    const pos = await apunta(sel, dur);
    await p.evaluate(() => { const c = document.getElementById('vcur'); c.classList.remove('pulsa'); void c.offsetWidth; c.classList.add('pulsa'); });
    await p.mouse.click(pos.x, pos.y);
    await ESPERA(despues === undefined ? 650 : despues);
    await asegura();
  }
  async function escribe(sel, txt, retardo) {
    await pulsa(sel, 600, 250);
    await p.keyboard.type(txt, { delay: retardo || 55 });
    await ESPERA(350);
  }
  // arrastra el tirador de una barra hasta un valor (1..5)
  async function desliza(valor) {
    const sel = '[data-scr]';
    const r = await p.evaluate(s => { const e = document.querySelector(s), r = e.getBoundingClientRect(); return { l: r.left, w: r.width, y: r.top + r.height / 2, v: +e.value }; }, sel);
    const px = v => r.l + 10 + (r.w - 20) * (v - 1) / 4;
    await apunta(sel, 600);
    await p.evaluate((x, y) => { const c = document.getElementById('vcur'); c.style.setProperty('--d', '400ms'); c.style.setProperty('--x', x + 'px'); c.style.setProperty('--y', y + 'px'); }, px(r.v), r.y);
    await ESPERA(500);
    await p.mouse.move(px(r.v), r.y); await p.mouse.down();
    const pasos = 18;
    for (let i = 1; i <= pasos; i++) {
      const x = px(r.v) + (px(valor) - px(r.v)) * i / pasos;
      await p.mouse.move(x, r.y);
      await p.evaluate((x, y) => { const c = document.getElementById('vcur'); c.style.setProperty('--d', '0ms'); c.style.setProperty('--x', x + 'px'); c.style.setProperty('--y', y + 'px'); }, x, r.y);
      await ESPERA(28);
    }
    await p.mouse.up(); await ESPERA(500); await asegura();
    // tras soltar, la app repinta: el cursor vuelve a donde estaba
    await p.evaluate((x, y) => { const c = document.getElementById('vcur'); c.style.setProperty('--d', '0ms'); c.style.setProperty('--x', x + 'px'); c.style.setProperty('--y', y + 'px'); }, px(valor), r.y);
  }
  // espera a que la página deje de desplazarse
  async function quieto() {
    let y = -1;
    for (let i = 0; i < 60; i++) { await ESPERA(110); const n = await p.evaluate(() => scrollY); if (n === y) break; y = n; }
  }
  async function baja(px, ms) { await p.evaluate(y => scrollBy({ top: y, behavior: 'smooth' }), px); await quieto(); await ESPERA(ms ? Math.max(0, ms - 600) : 300); }
  async function arriba() { await p.evaluate(() => scrollTo({ top: 0, behavior: 'smooth' })); await quieto(); }
  async function titulo(h1, sub, small, ms) {
    await p.evaluate((a, b, c) => { document.getElementById('vcur').style.opacity = 0; const t = document.getElementById('vtit'); t.innerHTML = '<h1>' + a + '</h1><p>' + b + '</p>' + (c ? '<small>' + c + '</small>' : ''); t.classList.add('on'); }, h1, sub, small);
    await ESPERA(ms);
  }
  const quitaTitulo = async () => { await p.evaluate(() => { document.getElementById('vtit').classList.remove('on'); document.getElementById('vcur').style.opacity = 1; }); await ESPERA(900); };

  // =================== el guion ===================
  await titulo('NOGUM', 'La App del Director', 'UNA PARTIDA EN TRES MINUTOS', 2600);
  await quitaTitulo();
  await sub('Esta es la App de NOGUM. Vamos a montar una partida de <b>terror cósmico</b>, de principio a fin.');
  await apunta('[data-edi=acelerado]', 1100);
  await foto('bienvenida');
  await sub('Elegimos <b>NOGUM Acelerado</b>: lo esencial, para jugar esta misma tarde.');
  await pulsa('[data-edi=acelerado]');

  // -- el universo --
  await sub('Primero, el universo. ¿Tenéis uno conocido en la cabeza?');
  await pulsa('[data-hub=uni]', 900, 900);
  await pulsa('[data-pk="known|1"]');
  await pulsa('[data-fsig]', 700, 800);
  await sub('Es un mundo actual, con misterio…');
  await pulsa('[data-pk="family|mo"]', 800);
  await pulsa('[data-fsig]', 700, 800);
  await foto('mundos');
  await sub('…y de los que dan miedo: <b>dioses primigenios, libros prohibidos y locura</b>.');
  await pulsa('[data-pk="world|11"]', 900, 900);
  await pulsa('[data-fsig]', 700, 900);
  await sub('Dos toques, y la mesa ya sabe qué cabe en su mundo y de qué tamaño son las hazañas.');
  await baja(260, 1400); await foto('universo-fin');
  await pulsa('[data-fsal]@ultimo', 800, 900);

  // -- el tono --
  await sub('Ahora, el tono. No hay preguntas técnicas: hay <b>situaciones</b>, y tú dices qué esperas.');
  await pulsa('[data-hub=tono]', 900, 900);
  await foto('tono-1');
  await sub('Un buen escalador, sin prisa y con buen material. ¿Qué espera la mesa? Que la pared le cobre algo.');
  await pulsa('[data-sc="2"]', 900, 900);
  await pulsa('[data-fsig]', 700, 900);
  await sub('Un ruido al fondo del pasillo para distraer al guardia. Mira… sin creérselo del todo.');
  await pulsa('[data-sc="2"]', 900, 900);
  await pulsa('[data-fsig]', 700, 900);
  await sub('¿La suerte está de vuestro lado? En Innsmouth, <b>no</b>.');
  await desliza(1);
  await ESPERA(600);
  await pulsa('[data-fsig]', 700, 900);
  await foto('optimismo');
  await sub('El universo os pone a prueba. En el Acelerado eso es <b>Terror</b>: el mismo dado, pero solo tres casillas de vida.');
  await pulsa('[data-fsig]', 900, 900);
  await sub('El caos. Tres sesiones preparando un golpe… y sale otra cosa. Hay que improvisar.');
  await pulsa('[data-sc="4"]', 900, 900);
  await pulsa('[data-fsig]', 700, 900);
  await sub('Una pelea de taberna sin nada en juego… y alguien saca un cuchillo.');
  await pulsa('[data-sc="4"]', 900, 900);
  await pulsa('[data-fsig]', 700, 900);
  await sub('Vuestro mundo no es un reloj: los planes se tuercen por donde nadie miraba.');
  await desliza(4);
  await ESPERA(500);
  await pulsa('[data-fsig]', 700, 900);
  await pulsa('[data-fsig]', 800, 900);
  await foto('tono-fin');
  await sub('Resultado: <b>Modo Terror</b>. Antes de tirar un solo dado, la mesa ya sabe cómo se va a sentir con ellos en la mano.');
  await ESPERA(1500);
  await pulsa('[data-fsal]@ultimo', 900, 1000);
  await sub('Así queda la mesa. Todo esto cabe en un Código corto que se comparte con los jugadores.');
  await baja(560, 1600); await ESPERA(1200); await foto('mesa');

  // -- el personaje --
  await sub('Ahora, un investigador. De la ficha plantilla sale una ficha nueva.');
  await pulsa('[data-gotpl]', 900, 1100);
  await baja(380, 1200);
  await pulsa('#createBtn', 900, 1100);
  await escribe('#f-name', 'Frank Delaney');
  await sub('<b>Frank Delaney</b>, detective privado. Boston, 1927.');
  await escribe('#f-concept', 'Detective privado de Boston');
  await apunta('#f-concept', 200);
  await sub('Catorce puntos. Sabe investigar, mirar dos veces y leer lo que no debería…');
  for (const s of ['[data-dom="1.1"]', '[data-dis="1.1.0"]', '[data-dis="1.1.1"]', '[data-dom="1.0"]', '[data-dis="1.0.2"]']) await pulsa('#pcSheet ' + s, 450, 380);
  await sub('…moverse sin ruido, sacarle la verdad a un testigo y, si no queda otra, apretar el gatillo.');
  for (const s of ['[data-dom="0.0"]', '[data-dis="0.0.2"]', '[data-dom="2.0"]', '[data-dis="2.0.2"]', '[data-dom="0.1"]', '[data-dis="0.1.3"]']) await pulsa('#pcSheet ' + s, 450, 380);
  await ESPERA(800); await foto('ficha');

  // -- el equipo --
  await sub('El equipo es de quien lo lleva. Se busca por nombre, o por lo que hace.');
  await arriba();
  await pulsa('[data-tab=form]', 800, 900);
  await pulsa('[data-hub=equipo]', 900, 900);
  await pulsa('[data-eqwho]', 800, 900);
  await escribe('#eqq', 'cámara', 90);
  await ESPERA(500);
  await sub('Una cámara, para lo que nadie creería sin pruebas…');
  await pulsa('#eqres [data-eqadd]', 800, 700);
  await foto('camara');
  await p.evaluate(() => { const i = document.getElementById('eqq'); i.select(); });
  await p.keyboard.press('Backspace'); await ESPERA(200);
  await p.keyboard.type('revólver', { delay: 90 }); await ESPERA(600);
  await sub('…y un revólver pequeño. Por si las pruebas vienen a buscarle a él.');
  await pulsa('#eqres [data-eqadd]', 800, 800);
  await pulsa('[data-eq=cuenta]', 800, 1000);
  await foto('cuenta');
  await sub('La cuenta: lo que cuesta en puntos, en Llaves, y si está a su alcance.');
  await ESPERA(1200);
  await pulsa('[data-eq=add]', 900, 1100);
  await sub('Lo que no está en la lista se apunta a mano: <b>un cuaderno de tapas negras</b>.');
  await escribe('#f-notes', 'Cuaderno de tapas negras, siempre en el bolsillo del abrigo.', 42);
  await ESPERA(600); await foto('notas');

  // -- la historia --
  await sub('En <b>Historia</b> vive la memoria de la campaña. Primero, de dónde viene Frank.');
  await arriba();
  await pulsa('[data-tab=story]', 800, 1000);
  await escribe('#st-pc0', 'Expolicía de Boston. Lo echaron por hacer demasiadas preguntas sobre un caso que nadie quería resolver. Ahora le pagan por hacerlas.', 32);
  await sub('Y la campaña, que ya estaba escrita: <b>La sombra sobre Innsmouth</b>.');
  // la campaña arriba del todo, y se lee un trozo bajando por dentro
  await p.evaluate(() => { const r = document.getElementById('st-common').closest('.panel').getBoundingClientRect(); scrollBy({ top: r.top - 150, behavior: 'smooth' }); });
  await quieto();
  await apunta('#st-common', 900);
  await ESPERA(1800); await foto('historia');
  for (let i = 1; i <= 3; i++) {
    await p.evaluate(k => { const ta = document.getElementById('st-common'); ta.scrollTo({ top: (ta.scrollHeight - ta.clientHeight) * k / 3, behavior: 'smooth' }); }, i);
    await ESPERA(1500);
  }
  await foto('historia-2');
  await sub('La pestaña Preguntas contesta a partir de lo que hay aquí. Y el secreto del Máster, con candado si hace falta.');
  await baja(420, 1500);
  await ESPERA(1800);

  // -- la primera tirada --
  await sub('Y a jugar. Frank entra en el hotel Gilman House y escucha a través de la pared.');
  await arriba();
  await pulsa('[data-tab=dice]', 800, 1000);
  await pulsa('#dPc', 700, 300);
  await p.evaluate(() => { const s = document.getElementById('dPc'); s.selectedIndex = 1; s.dispatchEvent(new Event('change', { bubbles: true })); });
  await ESPERA(900); await asegura();
  await pulsa('#dSk', 700, 300);
  await p.evaluate(() => { const s = document.getElementById('dSk'); const o = [...s.options].findIndex(o => /Alerta/.test(o.textContent)); s.selectedIndex = o > 0 ? o : 1; s.dispatchEvent(new Event('change', { bubbles: true })); });
  await ESPERA(900); await asegura();
  await sub('Modo Terror: solo cuenta el dado rojo.');
  await pulsa('#dRoll', 900, 900);
  await arriba(); await ESPERA(600);
  await foto('dados');
  await ESPERA(1800);
  await finSub();
  await titulo('NOGUM', 'Un juego de rol universal. Libre, en español y en inglés.', 'EPIFANEIA.DEV/NOGUM', 4200);

  if (!SECO) await cdp.send('Page.stopScreencast');
  if (subAbierto) subAbierto.fin = ahora();
  await ESPERA(300);
  // ---- lo que necesita ffmpeg: cada fotograma y cuánto dura ----
  if (!SECO) {
    const lista = tiempos.map(([f, t], i) => "file '" + f.split(path.sep).join('/') + "'\nduration " + ((i + 1 < tiempos.length ? tiempos[i + 1][1] : t + 2) - t).toFixed(4)).join('\n') + "\nfile '" + tiempos[tiempos.length - 1][0].split(path.sep).join('/') + "'\n";
    fs.writeFileSync(path.join(OUT, 'lista.txt'), lista);
    // los subtítulos, contados desde el primer fotograma
    const desfase = t0 - inicio;
    const hms = s => { s = Math.max(0, s); const h = Math.floor(s / 3600), m = Math.floor(s % 3600 / 60), x = (s % 60).toFixed(3).padStart(6, '0').replace('.', ','); return String(h).padStart(2, '0') + ':' + String(m).padStart(2, '0') + ':' + x; };
    fs.writeFileSync(path.join(OUT, 'subtitulos.srt'), subs.map((s, i) => (i + 1) + '\n' + hms(s.ini - desfase) + ' --> ' + hms(s.fin - desfase) + '\n' + s.txt + '\n').join('\n'));
    console.log('fotogramas', nf, 'duración', (tiempos[tiempos.length - 1][1] - t0).toFixed(1), 's');
  }
  console.log('errores JS', errs.length ? errs : 'ninguno');
  await b.close();
})();
