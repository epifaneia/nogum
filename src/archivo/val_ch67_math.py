import re, io, sys
from html.parser import HTMLParser
VOID = {'br','hr','img','input','meta','link','wbr','source','col','area','base','embed','param','track'}
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.st=[]; s.err=[]; s.ids=[]; s.w=[]; s.text=[]
    def handle_starttag(s,t,a):
        d=dict(a)
        if 'id' in d: s.ids.append(d['id'])
        if 'style' in d: s.w.append(d['style'])
        if t not in VOID: s.st.append(t)
    def handle_endtag(s,t):
        if t in VOID: return
        if not s.st or s.st[-1]!=t: s.err.append((t, s.getpos(), s.st[-3:]))
        else: s.st.pop()
    def handle_data(s,d): s.text.append(d)
def parse(f):
    p=P(); p.feed(io.open(f,encoding='utf-8').read()); p.close(); return p
SP = [r'\bde\b', r'\bla\b', r'\bque\b', r'ción', r'\bel\b', r'\blos\b', r'\blas\b', r'\bdel\b', r'\bcon\b', r'\bpara\b', r'\buna?\b', r'\bes\b', r'\bpor\b', r'\by\b', r'[áéíóúñ¿¡«»]', r'\d %']
for base in sys.argv[1:]:
    s, e = parse(base+'.html'), parse(base+'.en.html')
    txt = ' '.join(e.text)
    hits = {pat: re.findall(r'.{0,25}'+pat+r'.{0,25}', txt) for pat in SP}
    hits = {k:v for k,v in hits.items() if v}
    print(base, '| balanced:', not e.err and not e.st, e.err[:3], e.st,
          '| ids equal:', s.ids==e.ids, len(s.ids),
          '| styles equal:', s.w==e.w, len(s.w),
          '| spanish hits:', hits)
