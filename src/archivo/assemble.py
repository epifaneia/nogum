import re, html, os, sys
from html.parser import HTMLParser
D=os.path.dirname(os.path.abspath(__file__))
def R(n): return open(os.path.join(D,n),encoding='utf-8').read()

cap8=R('frag_cap8.html'); bazar=R('frag_bazar.html'); math=R('frag_math.html')
# split math into 1.3 and apendice D
m13, mD = math.split('<section class="chapter" id="apx-mates">',1)
mD='<section class="chapter" id="apx-mates">'+mD
# insert bazar (8.3) before 8.4 inside cap8
k=cap8.find('<h3 id="ch8-recetas"')
assert k>0
cap8=cap8[:k]+'</section>\n'+bazar+'\n<section class="chapter" id="ch8b">\n<h2>8.4 Simulación de manuales</h2>\n'+cap8[k:]
manual=''.join([R('frag_intro.html'),R('frag_ch1a.html'),m13,R('frag_ch1b.html'),R('frag_ch2.html'),R('frag_ch3.html'),R('frag_ch4.html'),R('frag_ch5.html'),R('frag_ch67.html'),cap8,mD])
acel=R('frag_acelerado.html')
audit=R('frag_editorial.html')+R('frag_descartados.html')+R('frag_trazabilidad.html')

def clean(t): return re.sub(r'<[^>]+>','',t).strip()
def toc_for(view,label,body):
    out=[f'<li class="g" data-view="{view}">{label}</li>']
    for m in re.finditer(r'<section class="chapter" id="([^"]+)">\s*<h2>(.*?)</h2>|<h3 id="([^"]+)"[^>]*>(.*?)</h3>',body,re.S):
        if m.group(1):
            t=clean(m.group(2)); t=re.sub(r'\s+',' ',t)
            out.append(f'<li><a class="h2" data-view="{view}" href="#{m.group(1)}">{html.escape(t)}</a></li>')
        else:
            t=clean(m.group(4)); t=re.sub(r'\s*(Propuesta sin validar|Pendiente|Descartado|ED-[\w-]+)\s*',' ',t).strip()
            out.append(f'<li><a class="h3" data-view="{view}" href="#{m.group(3)}">{html.escape(t)}</a></li>')
    return '\n'.join(out)
toc=toc_for('inicio','Inicio',R('frag_home.html'))+toc_for('manual','Manual',manual)+toc_for('acelerado','NOGUM Acelerado',acel)+toc_for('auditoria','Auditoría',audit)

allb=manual+acel+audit
counts={k:len(re.findall(r'class="flag %s"'%k,allb)) for k in ['proposal','pending','ed','drop']}
drop_rows=R('frag_descartados.html').split('dr-verificacion')[0].count('class="flag drop"')
home=R('frag_home.html')
for k,v in {'%%N_PENDING%%':counts['pending'],'%%N_PROPOSAL%%':counts['proposal'],'%%N_ED%%':counts['ed'],'%%N_DROP%%':drop_rows}.items():
    home=home.replace(k,str(v))
page=R('shell.html').replace('%%TOC%%',toc).replace('%%HOME%%',home).replace('%%MANUAL%%',manual).replace('%%ACELERADO%%',acel).replace('%%AUDIT%%',audit)

class V(HTMLParser):
    void={'br','hr','img','input','meta','link','col','wbr','source'}
    def __init__(s): super().__init__(); s.st=[]; s.err=[]; s.ids={}
    def handle_starttag(s,t,a):
        d=dict(a)
        if 'id' in d:
            s.ids[d['id']]=s.ids.get(d['id'],0)+1
        if t not in s.void: s.st.append((t,s.getpos()))
    def handle_endtag(s,t):
        if t in s.void: return
        if not s.st or s.st[-1][0]!=t:
            s.err.append((t,s.getpos(),s.st[-1] if s.st else None))
            # try recover
            for i in range(len(s.st)-1,-1,-1):
                if s.st[i][0]==t: del s.st[i:]; break
        else: s.st.pop()
v=V(); v.feed(page)
dups=[k for k,c in v.ids.items() if c>1]
hrefs=set(re.findall(r'href="#([^"]+)"',page))
missing=[h for h in hrefs if h not in v.ids and h not in ('inicio','manual','acelerado','auditoria')]
print('errors',v.err[:10],'unclosed',[x for x in v.st if x[0] not in('html','body','head')][:10])
print('dup ids',dups[:20]); print('missing anchors',missing)
print('counts',counts,'drop_rows',drop_rows,'bytes',len(page.encode()))
out=sys.argv[1] if len(sys.argv)>1 else os.path.join(D,'nogum_maestro.html')
open(out,'w',encoding='utf-8').write(page)
print('written',out)
