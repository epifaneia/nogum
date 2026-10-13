import re
from html.parser import HTMLParser
VOID={'br','img','hr','meta','link','input','wbr'}
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.st=[]; s.err=[]; s.ids=[]; s.tags=[]
    def handle_starttag(s,t,a):
        s.tags.append(t)
        for k,v in a:
            if k=='id': s.ids.append(v)
        if t not in VOID: s.st.append(t)
    def handle_endtag(s,t):
        if not s.st or s.st[-1]!=t: s.err.append(t)
        else: s.st.pop()
def run(f):
    p=P(); p.feed(open(f,encoding='utf-8').read()); return p
a=run('frag_bazar_b.html'); b=run('frag_bazar_b.en.html')
print('balanced:', not b.err and not b.st, b.err, b.st)
print('ids equal:', a.ids==b.ids, len(b.ids))
print('tag sequence equal:', a.tags==b.tags)
txt=re.sub(r'<[^>]+>',' ',open('frag_bazar_b.en.html',encoding='utf-8').read())
for w in [' de ',' la ',' que ','ción',' el ',' los ',' con ',' y ','«','»']:
    if w in txt: print('found',repr(w),txt.count(w))
