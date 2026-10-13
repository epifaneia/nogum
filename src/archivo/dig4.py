# -*- coding: utf-8 -*-
"""Imprime turnos por indice: dig4.py 188 193"""
import io, json, sys
P = r'C:\Users\Daniel Martin\.claude\projects\C--Users-Daniel-Martin-Desktop-NOGUM\fbb7f4ff-e94d-49c7-a22f-513a4a60b7b6.jsonl'
rows = []
for line in io.open(P, encoding='utf-8'):
    line = line.strip()
    if not line:
        continue
    try:
        o = json.loads(line)
    except Exception:
        continue
    m = o.get('message')
    if not isinstance(m, dict):
        continue
    role = m.get('role'); c = m.get('content'); txt = ''
    if isinstance(c, str):
        txt = c
    elif isinstance(c, list):
        for p in c:
            if isinstance(p, dict) and p.get('type') == 'text':
                txt += p.get('text', '')
    if not txt.strip():
        continue
    if role == 'user' and ('<system-reminder>' in txt or 'tool_result' in txt):
        continue
    rows.append((role, txt.strip()))
a, b = int(sys.argv[1]), int(sys.argv[2])
out = []
for i in range(a, min(b, len(rows))):
    out.append('\n' + '=' * 70 + '\n### TURNO %d [%s]\n' % (i, rows[i][0].upper()) + rows[i][1])
io.open('dig4.txt', 'w', encoding='utf-8').write('\n'.join(out))
print('escrito', len('\n'.join(out)))
