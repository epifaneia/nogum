import json, os
D = os.path.dirname(os.path.abspath(__file__))
R = lambda n: open(os.path.join(D, n), encoding='utf-8').read()
css = R('paper.css'); tokens = css[:css.index('*{box-sizing')]
def js(o): return json.dumps(o, ensure_ascii=False).replace('</', '<' + chr(92) + '/')
page = R('app2_body.html').replace('%%TOKENS%%', tokens).replace('%%DATA%%', js(json.load(open(os.path.join(D, 'app_data.json'), encoding='utf-8')))).replace('%%CANON%%', js(R('CANON.md')))
os.makedirs(os.path.join(D, 'out3'), exist_ok=True)
open(os.path.join(D, 'out3', 'nogum_app.html'), 'w', encoding='utf-8').write(page)
i = page.index('</style>') + 8
full = ('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        + page[:i] + '\n</head>\n<body>\n' + page[i:] + '</body>\n</html>\n')
open(r'C:/Users/Daniel Martin/Desktop/NOGUM/NOGUM_app/NOGUM_app.html', 'w', encoding='utf-8').write(full)
print('KB', len(page.encode()) // 1024)
