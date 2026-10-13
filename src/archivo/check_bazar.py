import sys
from html.parser import HTMLParser
VOID={"br","hr","img","meta","link","input","wbr"}
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.stack=[]; s.err=[]; s.h3=None; s.counts={}; s.intbody=False; s.ids=[]
    def handle_starttag(s,t,a):
        if t in VOID: return
        s.stack.append((t,s.getpos()))
        d=dict(a)
        if t=="h3": s.h3=d.get("id"); s.ids.append(s.h3)
        if t=="tbody": s.intbody=True
        if t=="tr" and s.intbody: s.counts[s.h3]=s.counts.get(s.h3,0)+1
        if "style" in d: s.err.append(("style attr",s.getpos()))
    def handle_endtag(s,t):
        if t in VOID: return
        if not s.stack or s.stack[-1][0]!=t:
            s.err.append(("mismatch </%s>"%t,s.getpos(),s.stack[-1] if s.stack else None)); return
        s.stack.pop()
        if t=="tbody": s.intbody=False
p=P(); p.feed(open("frag_bazar.html",encoding="utf-8").read()); p.close()
print("errores:",p.err or "ninguno"); print("sin cerrar:",p.stack or "nada")
print("ids duplicados:", len(p.ids)!=len(set(p.ids)))
tot=0
for k,v in p.counts.items():
    if k in ("bz-resumen","bz-lectura"): continue
    print(k,v); tot+=v
print("TOTAL filas catálogo:",tot)
