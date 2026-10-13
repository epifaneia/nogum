# -*- coding: utf-8 -*-
"""Un enlace con Codigo pegado en la misma pestana no recarga la pagina: hay que escuchar el hashchange."""
import io, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
F = 'app4_body.html'
s = io.open(F, encoding='utf-8').read()

OLD = r"""(function(){
  var m = /[#&?]c=([A-Za-z0-9\-]+)/.exec(location.hash || '');
  if (!m) return;
  if (applyCode(m[1])) {
    S.tab = 'tpl'; rbOpen = null; rbBad = false;
    rbMsg = t('Mesa cargada desde el enlace: ','Table loaded from the link: ') + pick(card().n) + ' · ' + worldName();
    persist();
  }
  try { history.replaceState(null, '', location.pathname + location.search); } catch(e){}
})();"""

NEW = r"""function fromHash(live){
  var m = /[#&?]c=([A-Za-z0-9\-]+)/.exec(location.hash || '');
  if (!m) return false;
  var ok = applyCode(m[1]);
  if (ok) {
    S.tab = 'tpl'; rbOpen = null; rbBad = false;
    rbMsg = t('Mesa cargada desde el enlace: ','Table loaded from the link: ') + pick(card().n) + ' · ' + worldName();
    persist();
  }
  try { history.replaceState(null, '', location.pathname + location.search); } catch(e){}
  if (ok && live) { render(); window.scrollTo(0,0); }
  return ok;
}
window.addEventListener('hashchange', function(){ fromHash(true); });
fromHash(false);"""

assert s.count(OLD) == 1
s = s.replace(OLD, NEW)
io.open(F, 'w', encoding='utf-8').write(s)
print('hashchange anadido')
