import re,sys,os
S=sys.argv[1]
L=open('conversacioncompleta-docx.md',encoding='utf-8').read().split('\n')
junk={'copy_all','thumb_up','thumb_down','more_horiz','keep_pinGuardar en una notakeep_pin'}
date=re.compile(r'^(lunes|martes|miércoles|jueves|viernes|sábado|domingo), \d+ de \w+$')
out=[];turn=0;cur='(sin fecha)';expect=False
for l in L:
    s=l.strip()
    if s.startswith('keep_pin'):
        expect=True;continue
    if s in junk: continue
    if date.match(s): cur=s;out.append(f'\n########## FECHA: {s} ##########');continue
    if expect and s:
        turn+=1
        out.append(f'\n=== TURNO {turn} [{cur}] — la primera línea/párrafo siguiente es el MENSAJE DEL AUTOR; lo que sigue es la RESPUESTA DEL ASISTENTE ===')
        out.append('👤 AUTOR: '+l);expect=False;continue
    out.append(l.replace('more_horiz',''))
txt='\n'.join(out)
open(os.path.join(S,'conv_clean.md'),'w',encoding='utf-8').write(txt)
# split into ~65KB chunks at turn boundaries
parts=re.split(r'(?=\n=== TURNO )',txt)
chunks=[];buf=''
for p in parts:
    if len(buf.encode())+len(p.encode())>65000 and buf: chunks.append(buf);buf=''
    buf+=p
chunks.append(buf)
for i,c in enumerate(chunks,1):
    open(os.path.join(S,'chunks',f'c{i:02d}.md'),'w',encoding='utf-8').write(c)
    t=re.findall(r'=== TURNO (\d+) \[([^\]]+)\]',c)
    print(i,len(c.encode()),t[0] if t else '',t[-1] if t else '')
print('turns',turn)
