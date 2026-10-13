import sys
from html.parser import HTMLParser
VOID={'br','hr','img','input','meta','link','wbr','col','area','base','source','track','embed','param'}
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.stack=[]; s.err=[]; s.ids=[]; s.sig=[]
    def handle_starttag(s,t,a):
        d=dict(a)
        if 'id' in d: s.ids.append(d['id'])
        s.sig.append((t,tuple((k,v) for k,v in a if k in('id','class','href') or k.startswith('data-') and k!='data-jokes')))
        if t not in VOID: s.stack.append(t)
    def handle_endtag(s,t):
        if not s.stack or s.stack[-1]!=t: s.err.append(f'mismatch </{t}> stack={s.stack[-3:]}')
        else: s.stack.pop()
def run(f):
    p=P(); p.feed(open(f,encoding='utf-8').read()); p.close()
    if p.stack: p.err.append(f'unclosed {p.stack}')
    return p
ok=True
for n in sys.argv[1:]:
    a=run(n+'.html'); b=run(n+'.en.html')
    r=[]
    if b.err: r.append('tags: '+'; '.join(b.err))
    if a.ids!=b.ids: r.append('ids differ')
    if a.sig!=b.sig: r.append('structure/attrs differ')
    print(n+'.en.html', 'OK' if not r else r, f'({len(b.ids)} ids)')
    ok&=not r
sys.exit(0 if ok else 1)
