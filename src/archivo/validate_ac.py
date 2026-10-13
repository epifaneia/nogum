import re,sys
from html.parser import HTMLParser
VOID={'br','img','hr','meta','input','link','col','source','wbr'}
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.st=[]; s.err=[]; s.ids=[]; s.tags=[]; s.text=[]
    def handle_starttag(s,t,a):
        s.tags.append(t)
        for k,v in a:
            if k=='id': s.ids.append(v)
        if t not in VOID: s.st.append(t)
    def handle_endtag(s,t):
        if not s.st or s.st[-1]!=t: s.err.append((t,s.getpos(),s.st[-3:]))
        else: s.st.pop()
    def handle_data(s,d): s.text.append(d)
def run(f):
    p=P(); p.feed(open(f,encoding='utf-8').read()); p.close(); return p
a=run('frag_acelerado.html'); b=run('frag_acelerado.en.html')
print('balanced:', not b.err and not b.st, b.err[:5], b.st)
print('ids identical:', a.ids==b.ids, len(b.ids))
print('tag sequence identical:', a.tags==b.tags)
txt=' '.join(b.text)
for w in [' de ',' la ',' que ','ción']:
    print(repr(w), len(re.findall(re.escape(w),txt,re.I)))
