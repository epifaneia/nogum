import sys
from html.parser import HTMLParser
VOID={'br','hr','img','input','meta','link','wbr','col','source','area','base','embed','param','track'}
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.stack=[]; s.err=[]; s.ids=[]; s.tags=[]
    def handle_starttag(s,t,a):
        d=dict(a)
        if 'id' in d: s.ids.append(d['id'])
        s.tags.append((t,tuple((k,v) for k,v in a if k not in ('aria-label',))))
        if t not in VOID: s.stack.append(t)
    def handle_endtag(s,t):
        if t in VOID: return
        if not s.stack or s.stack[-1]!=t: s.err.append(f"mismatch </{t}> stack={s.stack[-3:]}")
        else: s.stack.pop()
def parse(f):
    p=P(); p.feed(open(f,encoding='utf-8').read()); p.close(); return p
ok=True
for n in ['frag_ch3','frag_ch4','frag_ch5']:
    s=parse(n+'.html'); e=parse(n+'.en.html')
    bal=not e.err and not e.stack
    ids=s.ids==e.ids
    struct=s.tags==e.tags
    print(n, 'balanced' if bal else ('UNBALANCED',e.err,e.stack), 'ids_match' if ids else 'IDS_DIFFER', len(e.ids), 'tags+attrs_match' if struct else 'STRUCT_DIFFER')
    ok&=bal and ids and struct
print('ALL OK' if ok else 'FAIL')
