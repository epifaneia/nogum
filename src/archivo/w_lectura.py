# -*- coding: utf-8 -*-
"""La lectura del modelo, con progreso de verdad, streaming y boton de parar."""
import io, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
F = 'app4_body.html'
s = io.open(F, encoding='utf-8').read()
fal = []


def sub(a, b, n=1):
    global s
    if s.count(a) != n:
        fal.append('(%d!=%d) %s' % (s.count(a), n, a[:70])); return
    s = s.replace(a, b, n)


VIEJO_INI = 'function pideLectura(fid, btn) {'
VIEJO_FIN = '\n/* ======================= REPARTO ======================= */'
i = s.find(VIEJO_INI)
j = s.find(VIEJO_FIN)
if i < 0 or j <= i:
    print('no encuentro pideLectura (%d, %d)' % (i, j)); sys.exit(1)

NUEVO = r"""var iaEstado = {}, iaCtl = null;
var IAERR = {
  not_granted:['No has dado permiso para que la app me pregunte. Es el aviso que sale la primera vez.','You have not allowed the app to ask Claude. That is the prompt you get the first time.'],
  sampling_disabled:['Esta cuenta no tiene disponible la lectura.','This account does not have the reading available.'],
  not_declared:['Esta versión de la app no pide la capacidad de preguntar.','This version of the app does not declare the asking capability.'],
  capability_disabled:['La lectura no funciona en esta vista.','The reading does not work in this view.'],
  capability_removed:['La lectura no funciona en esta vista.','The reading does not work in this view.'],
  rate_limited:['Demasiadas preguntas de golpe, o se ha agotado tu cuota. Prueba dentro de un rato.','Too many questions at once, or your quota ran out. Try again in a while.'],
  session_expired:['Hay que volver a entrar en la cuenta.','You need to sign in again.'],
  refused:['No he querido contestar a eso. Cambia alguna respuesta y vuelve a pedirlo.','Claude declined to answer that. Change an answer and ask again.'],
  empty_completion:['No ha salido texto. Vuelve a pedirlo.','No text came out. Ask again.'],
  prompt_too_large:['Hay demasiadas respuestas para leerlas de una vez.','There are too many answers to read at once.']
};
function pideLectura(fid){
  if (!window.claude || !window.claude.use) {
    S.ia[fid] = t('Esta lectura solo funciona en la versión publicada de la app, que es la que puede preguntarme.','This reading only works in the published version of the app, which is the one that can ask Claude.');
    persist(); render(true); return;
  }
  var refresca = !!S.ia[fid];
  iaEstado[fid] = 'pensando';
  S.ia[fid] = '';
  iaCtl = new AbortController();
  var sig = iaCtl.signal;
  render(true);
  function pinta(txt){
    S.ia[fid] = txt;
    var box = $('iabox-' + fid);
    if (box) box.textContent = txt; else render(true);
  }
  window.claude.use('sample').then(function(sample){
    if (!sample) {
      iaEstado[fid] = '';
      S.ia[fid] = t('La lectura no está disponible en esta vista.','The reading is not available in this view.');
      persist(); render(true); return;
    }
    var pr = 'Eres el Director de NOGUM, un juego de rol universal. Un Director acaba de contestar un formulario de escalas de 1 a 5 sobre su mesa. '
      + 'Esto es lo que ha contestado:\n\n' + respuestasTexto(fid)
      + '\n\nY esto es lo que el formulario ha deducido:\n' + resultadoTexto(fid)
      + '\n\nEscribe entre 60 y 110 palabras, en ' + (S.lang === 'en' ? 'inglés' : 'castellano')
      + ', en segunda persona del plural («vuestra mesa»), sin listas ni títulos. '
      + 'Di en una frase qué clase de mesa es esta. Y después, lo importante: si hay dos respuestas que tiran en direcciones opuestas, dilo claramente, di qué sabor raro produce la mezcla y qué respuesta movería yo. '
      + 'Si no hay contradicción, dilo en media frase y no la inventes. No repitas los números ni expliques las reglas: habla de cómo se va a sentir jugar ahí.';
    return sample(pr, {
      modelTier:'default',
      signal:sig,
      cache: refresca ? {gcTime:600000, refresh:true} : {gcTime:600000},
      onText: function(up){ iaEstado[fid] = 'escribiendo'; pinta(up.text); }
    }).then(function(r){
      iaEstado[fid] = '';
      S.ia[fid] = r.text + (r.truncated ? '\n\n' + t('(se ha cortado: pídeme menos de una vez)','(cut short: ask for less at a time)') : '');
      persist(); render(true);
    });
  }).catch(function(e){
    iaEstado[fid] = '';
    var c = e && e.code;
    if (c === 'cancelled') S.ia[fid] = (e && e.text) || '';
    else S.ia[fid] = (IAERR[c] ? pick(IAERR[c]) : t('No se ha podido leer. Vuelve a intentarlo.','Could not read it. Try again.')) + (e && e.text ? '\n\n' + e.text : '');
    persist(); render(true);
  });
}
"""
s = s[:i] + NUEVO + s[j:]

CAJA_VIEJA = (
    "  h += '<div class=\"aiask\"><button type=\"button\" class=\"tool\" data-ia=\"' + fid + '\">' + "
    "esc(t('Léete mis respuestas y dime qué mesa es esta','Read my answers and tell me what table this is')) + '</button>' +\n"
    "    '<span class=\"note\">' + esc(t('Lee todo lo que has contestado y busca contradicciones. Tarda unos segundos.',"
    "'It reads everything you answered and looks for contradictions. Takes a few seconds.')) + '</span></div>';\n"
    "  if (S.ia && S.ia[fid]) h += '<div class=\"iabox\">' + esc(S.ia[fid]) + '</div>';\n"
    "  return h;")
CAJA_NUEVA = (
    "  var est = iaEstado[fid];\n"
    "  h += '<div class=\"aiask\">';\n"
    "  if (est) h += '<span class=\"iawait\">' + esc(est === 'pensando' ? t('Pensando…','Thinking…') : t('Escribiendo…','Writing…')) +\n"
    "    '</span><button type=\"button\" class=\"tool\" data-iastop=\"1\">' + esc(t('Parar','Stop')) + '</button>';\n"
    "  else h += '<button type=\"button\" class=\"tool\" data-ia=\"' + fid + '\">' + esc(S.ia[fid]\n"
    "    ? t('Volver a leerlo','Read it again')\n"
    "    : t('Léete mis respuestas y dime qué mesa es esta','Read my answers and tell me what table this is')) + '</button>';\n"
    "  h += '<span class=\"note\">' + esc(t('Lee las respuestas enteras y busca contradicciones. Lo escribo yo, tarda entre cinco segundos y un minuto, y lo paga tu cuenta.',"
    "'It reads all your answers and looks for contradictions. Claude writes it, it takes between five seconds and a minute, and it is billed to your account.')) + '</span></div>';\n"
    "  if (S.ia[fid] || est) h += '<div class=\"iabox\" id=\"iabox-' + fid + '\">' + esc(S.ia[fid] || '') + '</div>';\n"
    "  return h;")
sub(CAJA_VIEJA, CAJA_NUEVA)

sub("  v.querySelectorAll('[data-ia]').forEach(function(b){ b.addEventListener('click', function(){ pideLectura(b.getAttribute('data-ia'), b); }); });",
    "  v.querySelectorAll('[data-ia]').forEach(function(b){ b.addEventListener('click', function(){ pideLectura(b.getAttribute('data-ia')); }); });\n"
    "  v.querySelectorAll('[data-iastop]').forEach(function(b){ b.addEventListener('click', function(){ if (iaCtl) iaCtl.abort(); }); });")

sub(".iabox{margin-top:10px;",
    ".iawait{font:600 12px/1 var(--mono);text-transform:uppercase;letter-spacing:.05em;color:var(--red)}\n.iabox{margin-top:10px;min-height:1.6em;")

if fal:
    for x in fal:
        print('FALLO ' + x)
    sys.exit(1)
io.open(F, 'w', encoding='utf-8').write(s)
print('la lectura, con progreso, streaming y boton de parar')
