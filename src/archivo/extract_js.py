import io, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
s = io.open('out3/nogum_app.html', encoding='utf-8').read()
js = s[s.rindex('<script>') + 8:s.rindex('</script>')]
io.open('chk.js', 'w', encoding='utf-8').write(js)
