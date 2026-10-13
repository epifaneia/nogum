import io, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
s = io.open('taller.html', encoding='utf-8').read()
i = s.index('</style>') + 8
full = ('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        + s[:i] + '\n</head>\n<body>\n' + s[i:] + '\n</body>\n</html>\n')
out = r'C:/Users/Daniel Martin/Desktop/NOGUM/NOGUM_taller/NOGUM_taller.html'
os.makedirs(os.path.dirname(out), exist_ok=True)
io.open(out, 'w', encoding='utf-8').write(full)
print('KB', len(full.encode()) // 1024)
