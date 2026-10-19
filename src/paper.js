(function(){
  'use strict';
  var CFG = JSON.parse(document.getElementById('cfg').textContent);
  var UI = {
    es:{contents:'Índice',search:'Buscar en el libro',ph:'Llave, Estilo, Vorpalina…',print:'Imprimir',theme:'Tema',menu:'Índice',typeset:'Maquetando páginas…',pages:'páginas',none:'Sin resultados para',meta:'Columna meta',page:'pág.'},
    en:{contents:'Contents',search:'Search the book',ph:'Key, Style, Vorpal…',print:'Print',theme:'Theme',menu:'Contents',typeset:'Typesetting pages…',pages:'pages',none:'No results for',meta:'Meta column',page:'p.'}
  };
  function $(id){ return document.getElementById(id); }
  function store(k,v){ try{ localStorage.setItem(k,v); }catch(e){} }
  function read(k){ try{ return localStorage.getItem(k); }catch(e){ return null; } }
  function esc(s){ return String(s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];}); }
  function norm(s){ return s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,''); }

  var book = $('book'), status = $('status');
  var KEY = 'nogum-' + CFG.product;
  var lang = (location.search.match(/lang=(es|en)/) || [])[1] || read('nogum-lang') || CFG.langs[0];
  if (CFG.langs.indexOf(lang) < 0) lang = CFG.langs[0];

  /* ---------- typesetter ---------- */
  var cur, body, placed, running, stack, clones, runCap = '';
  // contenedores que se pueden repartir entre hojas. div.t7s son las siete
  // tarjetas de tono: sin estar aqui iban como un solo bloque de dos paginas
  // y la hoja recortaba en silencio lo que no cabia (T163)
  var SPLIT = 'div.tw, table, ul, ol, dl, div.rule, div.example, div.cards, div.steps, div.step, div.recipe, blockquote, section, div.acro, div.legend, div.t7s';
  var HEAD = /^(H2|H3|H4)$/;
  function isHead(el){ return el.nodeType===1 && (HEAD.test(el.tagName) || (el.matches && el.matches('.rule-title,.example-title,.step-title,.recipe-title,.card-kicker'))); }

  function newSheet(kind){
    var s = document.createElement('article');
    s.className = 'sheet' + (kind ? ' ' + kind : '');
    /* el color de capitulo viaja con la hoja: lo pinta el CSS, no el JS */
    if (runCap) s.setAttribute('data-cap', runCap);
    s.innerHTML = '<header class="rh"><span></span><span></span></header><div class="sb"></div><footer class="pf"><span class="pn"></span></footer>';
    s.firstChild.firstChild.textContent = CFG.title[lang];
    s.firstChild.lastChild.textContent = running || '';
    book.appendChild(s);
    cur = s; body = s.querySelector('.sb'); placed = 0;
    return s;
  }
  function over(){ var l = body.lastElementChild; if (!l) return false; var top = body.getBoundingClientRect().top; return l.getBoundingClientRect().bottom - top > body.clientHeight - 4 || body.scrollHeight > body.clientHeight + 1; }
  function target(){ return clones.length ? clones[clones.length-1].t : body; }
  function shallow(node, cont){
    var c = node.cloneNode(false);
    if (cont) { c.removeAttribute('id'); c.classList.add('cont'); }
    var t = c;
    if (node.tagName === 'TABLE') {
      Array.prototype.forEach.call(node.children, function(ch){ if (ch.tagName !== 'TBODY') c.appendChild(ch.cloneNode(true)); });
      t = document.createElement('tbody'); c.appendChild(t);
    }
    return {c:c, t:t};
  }
  function units(node){
    if (node.tagName === 'TABLE') {
      var rows = [], out = [];
      Array.prototype.forEach.call(node.tBodies, function(tb){ rows = rows.concat(Array.prototype.slice.call(tb.rows)); });
      for (var i=0; i<rows.length; ) {
        var span = 1;
        Array.prototype.forEach.call(rows[i].cells, function(td){ span = Math.max(span, td.rowSpan || 1); });
        out.push(rows.slice(i, i+span)); i += span;
      }
      return out;
    }
    return Array.prototype.filter.call(node.childNodes, function(n){ return n.nodeType===1 || (n.nodeType===3 && n.nodeValue.trim()); }).map(function(n){ return [n]; });
  }
  function canSplit(node){ if (node.nodeType!==1 || !node.matches(SPLIT)) return false; var u = units(node); return u.length > 1 || (u.length === 1 && u[0].length === 1 && canSplit(u[0][0])); }
  function realCount(el){ return Array.prototype.filter.call(el.childNodes, function(n){ return (n.nodeType===1 && !isHead(n) && n.tagName!=='THEAD' && n.tagName!=='CAPTION' && n.tagName!=='COLGROUP' && !(n.tagName==='TBODY' && !n.rows.length)) || (n.nodeType===3 && n.nodeValue.trim()); }).length; }

  function breakPage(){
    // carry trailing headings of the innermost target to the next page
    var t = target(), carry = [];
    while (t.lastChild && t.lastChild.nodeType===1 && isHead(t.lastChild) && realCount(t) + t.querySelectorAll(':scope > h2,:scope > h3,:scope > h4').length > 1) { carry.unshift(t.lastChild); t.removeChild(t.lastChild); }
    var old = clones.slice();
    newSheet();
    var parent = body;
    clones = old.map(function(o, i){
      var s = shallow(stack[i], true);
      parent.appendChild(s.c); parent = s.t;
      return s;
    });
    carry.forEach(function(n){ target().appendChild(n); });
    // drop empty fragments left behind, keeping their anchors
    for (var i = old.length - 1; i >= 0; i--) {
      if (realCount(old[i].t) === 0 && !old[i].t.querySelector('[id]')) {
        if (old[i].c.id) { clones[i].c.id = old[i].c.id; }
        Array.prototype.slice.call(old[i].c.childNodes).forEach(function(n){ if (isHead(n) || n.nodeType===3) clones[i].t.insertBefore(n, clones[i].t.firstChild); });
        old[i].c.remove();
      } else break;
    }
  }
  function put(node){
    var t = target();
    t.appendChild(node);
    if (!over()) { if (!isHead(node)) placed++; return; }
    t.removeChild(node);
    if (canSplit(node) && (placed > 0 || true)) { split(node); return; }
    if (placed === 0) { t.appendChild(node); placed++; return; }
    breakPage();
    target().appendChild(node);
    if (over() && canSplit(node)) { target().removeChild(node); split(node); return; }
    placed++;
  }
  function split(node){
    var s = shallow(node, false);
    target().appendChild(s.c);
    if (over()) {
      target().removeChild(s.c);
      if (placed > 0) { breakPage(); }
      target().appendChild(s.c);
    }
    stack.push(node); clones.push(s);
    var us = units(node);
    us.forEach(function(group){
      var t = target();
      group.forEach(function(n){ t.appendChild(n); });
      if (!over()) { if (!(group.length===1 && isHead(group[0]))) placed++; return; }
      group.forEach(function(n){ t.removeChild(n); });
      if (group.length===1 && canSplit(group[0])) { split(group[0]); return; }
      if (placed > 0) { breakPage(); t = target(); }
      group.forEach(function(n){ t.appendChild(n); });
      if (over() && group.length===1 && canSplit(group[0])) { group.forEach(function(n){ t.removeChild(n); }); split(group[0]); return; }
      placed++;
    });
    stack.pop(); clones.pop();
  }

  function contentsBlock(entries){
    var h = document.createElement('div');
    var h2 = document.createElement('h2'); h2.textContent = UI[lang].contents; h2.id = 'contents';
    var ol = document.createElement('ol'); ol.className = 'toc-list';
    entries.forEach(function(e){
      var li = document.createElement('li'); li.className = 'l' + e.level;
      li.innerHTML = '<a href="#' + esc(e.id) + '"><span class="t"></span><span class="d"></span><span class="n" data-for="' + esc(e.id) + '">00</span></a>';
      li.querySelector('.t').textContent = e.title;
      ol.appendChild(li);
    });
    return [h2, ol];
  }
  function cleanTitle(el){
    var c = el.cloneNode(true);
    c.querySelectorAll('.flag,.src').forEach(function(x){ x.remove(); });
    return c.textContent.replace(/\s+/g,' ').trim();
  }

  function typeset(done){
    book.style.zoom = '';
    book.innerHTML = '';
    document.documentElement.lang = lang;
    status.textContent = UI[lang].typeset;
    var tpl = document.getElementById('src-' + lang);
    var frag = tpl.content.cloneNode(true);
    var sections = Array.prototype.slice.call(frag.children).filter(function(n){ return n.tagName==='SECTION'; });
    // prep: ids on h2, numbered lists, meta labels
    var entries = [];
    sections.forEach(function(sec){
      sec.querySelectorAll('ol').forEach(function(ol){ var st = parseInt(ol.getAttribute('start') || '1', 10); Array.prototype.forEach.call(ol.children, function(li, i){ if (li.tagName==='LI' && !li.hasAttribute('value')) li.value = st + i; }); });
      sec.querySelectorAll('aside.meta').forEach(function(a){ a.setAttribute('data-label', UI[lang].meta); });
      if (sec.classList.contains('cover')) return;
      var h2 = sec.querySelector(':scope > h2');
      if (h2) {
        if (!h2.id) { h2.id = sec.id || ('s-' + entries.length); sec.setAttribute('data-cap', sec.id || h2.id); sec.removeAttribute('id'); }
        entries.push({id:h2.id, title:cleanTitle(h2), level:2});
      }
      sec.querySelectorAll('h3[id]').forEach(function(h3){ entries.push({id:h3.id, title:cleanTitle(h3), level:3}); });
    });
    stack = []; clones = []; running = ''; runCap = '';
    var queue = [];
    sections.forEach(function(sec, idx){
      // la lamina (la hoja con la imagen) va antes de la portadilla: el indice
      // va detras de la portadilla, no detras de la lamina
      if (sec.classList.contains('cover')) { queue.push({cover:sec}); if (CFG.contents && !sec.classList.contains('lamina')) queue.push({contents:true}); return; }
      if (idx === 0 && CFG.contents) queue.push({contents:true});
      queue.push({sec:sec});
    });
    var i = 0, first = true;
    function step(){
      var t0 = performance.now();
      while (i < queue.length && performance.now() - t0 < 40) {
        var q = queue[i++];
        if (q.cover) {
          running = ''; runCap = ''; newSheet('cover');
          Array.prototype.slice.call(q.cover.childNodes).forEach(function(n){ body.appendChild(n); });
          if (q.cover.id) body.firstElementChild && (body.firstElementChild.id = body.firstElementChild.id || q.cover.id);
          first = false; cur = null;
        } else if (q.contents) {
          running = UI[lang].contents; newSheet();
          contentsBlock(entries).forEach(put);
          cur = null;
        } else {
          var h2 = q.sec.querySelector(':scope > h2');
          running = h2 ? cleanTitle(h2) : running;
          var capId = q.sec.getAttribute('data-cap') || q.sec.id;
          if (capId) { runCap = capId; if (cur) cur.setAttribute('data-cap', runCap); }
          if (!cur || CFG.chapterBreak || first) newSheet();
          else if (placed > 0) { /* continue on same sheet */ }
          Array.prototype.slice.call(q.sec.childNodes).forEach(function(n){
            if (n.nodeType===3 && !n.nodeValue.trim()) return;
            if (n.nodeType===1 && n.tagName==='H2' && placed > 0) {
              // keep a heading with at least some content: start a new sheet if little room is left
              if (body.clientHeight - body.scrollHeight < 120) { running = cleanTitle(n); breakPage(); }
            }
            if (n.nodeType===1 && n.tagName==='H2') { running = cleanTitle(n); cur.firstChild.lastChild.textContent = running; }
            put(n);
          });
          first = false;
        }
      }
      if (i < queue.length) { status.textContent = UI[lang].typeset + ' ' + book.children.length; setTimeout(step, 0); return; }
      finish(entries); if (done) done();
    }
    step();
  }

  /* ---------- after layout ---------- */
  var sheetInfo = [];
  function finish(entries){
    var sheets = Array.prototype.slice.call(book.querySelectorAll('.sheet'));
    sheets.forEach(function(s, k){ s.querySelector('.pn').textContent = String(k + 1); s.setAttribute('data-page', k + 1); });
    var pageOf = {};
    entries.forEach(function(e){ var el = document.getElementById(e.id); if (el) { var s = el.closest('.sheet'); pageOf[e.id] = s ? +s.getAttribute('data-page') : 0; } });
    book.querySelectorAll('.toc-list .n').forEach(function(n){ n.textContent = pageOf[n.getAttribute('data-for')] || '–'; });
    // side contents
    var ul = $('stoc'); ul.innerHTML = '';
    entries.forEach(function(e){
      var li = document.createElement('li'); li.className = 'l' + e.level;
      li.innerHTML = '<a href="#' + esc(e.id) + '"><span></span><span class="n">' + (pageOf[e.id] || '') + '</span></a>';
      li.querySelector('span').textContent = e.title;
      ul.appendChild(li);
    });
    sheetInfo = sheets.map(function(s){ return {page:+s.getAttribute('data-page'), text:s.querySelector('.sb').textContent.replace(/\s+/g,' ')}; });
    status.textContent = sheets.length + ' ' + UI[lang].pages + ' · A4';
    fit();
    labels();
    trackActive(entries, pageOf);
  }
  function fit(){
    book.style.zoom = '';
    var avail = document.querySelector('main').clientWidth - 32;
    var w = book.getBoundingClientRect().width || 794;
    var z = Math.min(1, avail / w);
    book.style.zoom = z < 1 ? String(z) : '';
  }
  var fitT; window.addEventListener('resize', function(){ clearTimeout(fitT); fitT = setTimeout(fit, 120); });

  var activeHandler;
  function trackActive(entries, pageOf){
    var links = Array.prototype.slice.call(document.querySelectorAll('#stoc a'));
    if (activeHandler) window.removeEventListener('scroll', activeHandler);
    var ticking = false;
    activeHandler = function(){
      if (ticking) return; ticking = true;
      requestAnimationFrame(function(){
        ticking = false;
        var best = null, bestY = -Infinity;
        entries.forEach(function(e, k){
          var el = document.getElementById(e.id); if (!el) return;
          var y = el.getBoundingClientRect().top;
          if (y < 140 && y > bestY) { bestY = y; best = k; }
        });
        links.forEach(function(a, k){ a.classList.toggle('active', k === best); });
        if (best !== null) {
          var a = links[best], side = $('side'), r = a.getBoundingClientRect(), sr = side.getBoundingClientRect();
          if (r.top < sr.top + 60 || r.bottom > sr.bottom - 20) side.scrollTop += r.top - sr.top - 120;
          store(KEY + '-at', entries[best].id);
        }
      });
    };
    window.addEventListener('scroll', activeHandler, {passive:true});
    activeHandler();
  }

  /* ---------- search ---------- */
  var q = $('q'), res = $('results'), stoc = $('stoc');
  q.addEventListener('input', function(){
    var term = q.value.trim();
    if (term.length < 2) { res.hidden = true; stoc.hidden = false; return; }
    var nt = norm(term), out = [];
    sheetInfo.forEach(function(s){
      var nx = norm(s.text), p = nx.indexOf(nt); if (p < 0) return;
      var from = Math.max(0, p - 45), snip = s.text.substr(from, term.length + 100), k = norm(snip).indexOf(nt);
      out.push('<li><a href="#" data-page="' + s.page + '"><span class="rv">' + UI[lang].page + ' ' + s.page + '</span><span class="rs">' + (from ? '…' : '') + esc(snip.slice(0,k)) + '<mark>' + esc(snip.substr(k, term.length)) + '</mark>' + esc(snip.slice(k + term.length)) + '…</span></a></li>');
    });
    res.innerHTML = out.length ? out.slice(0, 60).join('') : '<li><span class="rs">' + UI[lang].none + ' «' + esc(term) + '»</span></li>';
    res.hidden = false; stoc.hidden = true;
  });
  res.addEventListener('click', function(e){
    var a = e.target.closest('a[data-page]'); if (!a) return; e.preventDefault();
    var s = book.querySelector('.sheet[data-page="' + a.getAttribute('data-page') + '"]');
    if (s) s.scrollIntoView({block:'start'});
    closeMenu();
  });

  /* ---------- chrome ---------- */
  function labels(){
    var u = UI[lang];
    $('qLabel').textContent = u.search; q.placeholder = u.ph;
    $('printBtn').textContent = u.print; $('themeBtn').textContent = u.theme; $('menuBtn').textContent = u.menu;
    document.querySelectorAll('[data-i18n-es]').forEach(function(el){ el.textContent = el.getAttribute('data-i18n-' + lang); });
    document.querySelectorAll('.lang button').forEach(function(b){ b.setAttribute('aria-pressed', b.getAttribute('data-lang') === lang ? 'true' : 'false'); });
    document.title = CFG.title[lang];
  }
  function closeMenu(){ document.body.classList.remove('nav-open'); $('menuBtn').setAttribute('aria-expanded','false'); }
  document.addEventListener('click', function(e){
    var j = e.target.closest('.joke');
    if (j) { var list = j.getAttribute('data-jokes').split('|'); var i = (list.indexOf(j.textContent.replace(/^\(|\)$/g,'')) + 1) % list.length; j.textContent = '(' + list[i] + ')'; return; }
    var a = e.target.closest('#stoc a, .toc-list a');
    if (a) { e.preventDefault(); var el = document.getElementById(a.getAttribute('href').slice(1)); if (el) el.scrollIntoView({block:'start'}); closeMenu(); }
  });
  $('menuBtn').addEventListener('click', function(){ var o = document.body.classList.toggle('nav-open'); this.setAttribute('aria-expanded', o ? 'true' : 'false'); });
  $('printBtn').addEventListener('click', function(){ window.print(); });
  var root = document.documentElement, th = read('nogum-theme'); if (th) root.setAttribute('data-theme', th);
  $('themeBtn').addEventListener('click', function(){
    var c = root.getAttribute('data-theme') || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    var n = c === 'dark' ? 'light' : 'dark'; root.setAttribute('data-theme', n); store('nogum-theme', n);
  });
  document.querySelectorAll('.lang button').forEach(function(b){
    if (CFG.langs.indexOf(b.getAttribute('data-lang')) < 0) b.parentNode.hidden = true;
    b.addEventListener('click', function(){
      var l = b.getAttribute('data-lang'); if (l === lang) return;
      var at = read(KEY + '-at');
      lang = l; store('nogum-lang', l);
      typeset(function(){ var el = at && document.getElementById(at); if (el) el.scrollIntoView({block:'start'}); });
    });
  });
  window.addEventListener('beforeprint', function(){ book.dataset.z = book.style.zoom; book.style.zoom = ''; });
  window.addEventListener('afterprint', function(){ book.style.zoom = book.dataset.z || ''; });

  /* ---------- start ---------- */
  labels();
  var started = false;
  function start(){
    if (started) return; started = true;
    typeset(function(){
      var id = location.hash.slice(1) || read(KEY + '-at');
      var el = id && document.getElementById(id);
      if (el) el.scrollIntoView({block:'start'});
    });
  }
  if (document.fonts && document.fonts.ready) { document.fonts.ready.then(start); setTimeout(start, 2500); } else start();
})();
