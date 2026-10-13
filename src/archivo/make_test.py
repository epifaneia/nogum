import io
src = r'C:/Users/Daniel Martin/Desktop/NOGUM/NOGUM_app/NOGUM_app.html'
s = io.open(src, encoding='utf-8').read()
mock = r'''<script>
window.__prompts = [];
(function(){
  function sample(input, opts){
    window.__prompts.push(input);
    var txt = JSON.stringify(input);
    var ans = txt.indexOf('unlocked') > -1 ? 'Lo guarda el capitán Brisa (Secreto de Máster).' : 'Según la Historia común, el grupo está en Valdoria.';
    if (opts && opts.onText) opts.onText({text: ans, delta: ans});
    return Promise.resolve({text: ans, truncated: false});
  }
  sample.json = function(input){
    window.__prompts.push(input);
    if (input.indexOf('index of a roleplaying campaign journal') > -1) {
      return Promise.resolve(input.split('PUBLIC SECTIONS')[0].indexOf('grimorio') > -1 ? {in_public:false, in_secret:true} : {in_public:true, in_secret:false});
    }
    if (input.indexOf('set up a table for the NOGUM') > -1) {
      if (input.indexOf('piratas') > -1 && input.indexOf('Sí, rápido') < 0)
        return Promise.resolve({set:{known:false, era:'pasado', tech:'vapor', sup:['magia'], opt:'alto', caos:'alto', zoom:'carne', estilo:true, baul:[0]}, reply:'Piratas con magia vudú, optimista y caótico.', question:'¿Queréis empezar ya con pocas reglas o con todas las herramientas?'});
      return Promise.resolve({set:{edition:'completo', grid:2}, reply:'Todas las herramientas, a escala de sala.', question:''});
    }
    return Promise.resolve({});
  };
  window.claude = {use: function(n){ return Promise.resolve(n === 'sample' ? sample : null); }};
})();
</script>
'''
s = s.replace('<script type="application/json" id="data">', mock + '<script type="application/json" id="data">', 1)
io.open(r'C:/Users/Daniel Martin/Desktop/NOGUM/NOGUM_app/test_mock.html', 'w', encoding='utf-8').write(s)
print('ok')
