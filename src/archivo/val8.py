import re, sys
from html.parser import HTMLParser
VOID={'br','img','hr','meta','link','input','col','wbr'}
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.st=[]; s.err=[]; s.ids=[]; s.tags=[]
    def handle_starttag(s,t,a):
        s.tags.append(t)
        for k,v in a:
            if k=='id': s.ids.append(v)
        if t not in VOID: s.st.append(t)
    def handle_endtag(s,t):
        if not s.st or s.st[-1]!=t: s.err.append((t, s.getpos(), s.st[-3:]))
        else: s.st.pop()
def parse(f):
    p=P(); txt=open(f,encoding='utf-8').read(); p.feed(txt); p.close(); return p,txt
ps,_=parse('frag_cap8.html'); pe,te=parse('frag_cap8.en.html')
print('balanced:', not pe.err and not pe.st, pe.err[:5], pe.st)
print('ids identical:', ps.ids==pe.ids, pe.ids)
print('tag sequence identical:', ps.tags==pe.tags, len(ps.tags), len(pe.tags))
plain=re.sub(r'<[^>]+>',' ',te).lower()
for w in [' de ',' la ',' que ','ción']:
    print(repr(w), plain.count(w))
print('guillemets left:', te.count('«')+te.count('»'))
