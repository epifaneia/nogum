# -*- coding: utf-8 -*-
"""Saca del transcripto los ultimos turnos de usuario y el texto mio que los precede."""
import io, json, sys, os
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
    role = m.get('role')
    c = m.get('content')
    txt = ''
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

n = int(sys.argv[1]) if len(sys.argv) > 1 else 10
us = [i for i, r in enumerate(rows) if r[0] == 'user']
start = us[-n] if len(us) >= n else 0
out = []
for role, txt in rows[max(0, start - 1):]:
    out.append('\n' + ('=' * 70) + '\n[' + role.upper() + ']\n' + txt)
io.open('dig.txt', 'w', encoding='utf-8').write('\n'.join(out))
print('turnos:', len(rows), 'escritos desde', start, 'tam', os.path.getsize('dig.txt'))
