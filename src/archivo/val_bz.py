import re,sys
from html.parser import HTMLParser
VOID={'br','hr','img','input','meta','link','wbr','col','area','base','source','track','embed','param'}
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.st=[]; s.err=[]; s.ids=[]; s.tags=[]
    def handle_starttag(s,t,a):
        s.tags.append(t)
        for k,v in a:
            if k=='id': s.ids.append(v)
        if t not in VOID: s.st.append(t)
    def handle_endtag(s,t):
        if not s.st or s.st[-1]!=t: s.err.append((t,s.getpos(),s.st[-1:] ))
        else: s.st.pop()
def parse(f):
    p=P(); p.feed(open(f,encoding='utf-8').read()); p.close(); return p
a=parse('frag_bazar_a.html'); b=parse('frag_bazar_a.en.html')
print('balanced:', not b.err and not b.st, b.err[:3], b.st)
print('ids equal:', a.ids==b.ids, len(a.ids))
print('tag sequence equal:', a.tags==b.tags, len(a.tags), len(b.tags))
txt=open('frag_bazar_a.en.html',encoding='utf-8').read()
for w in [' de ',' la ',' que ','ción',' el ',' los ',' con ','«','»']:
    print(repr(w), txt.count(w))
