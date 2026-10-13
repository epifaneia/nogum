# -*- coding: utf-8 -*-
"""El barrido de marcas, en dos pasadas: titulos y referencias primero, luego el texto."""
import io, os, re, shutil, importlib.util, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location('mm', 'marcas_map.py')
mm = importlib.util.module_from_spec(spec); spec.loader.exec_module(mm)

ES_FILES = ['frag_bazar.html', 'frag_cap8.html', 'frag_ch1a.html', 'frag_ch1b.html', 'frag_ch2.html',
            'frag_ch3.html', 'frag_ch4.html', 'frag_ch5.html', 'frag_ch67.html', 'frag_math.html',
            'frag_glosario.html', 'frag_intro.html', 'frag_acelerado.html', 'p3_tesis_es.html']
EN_FILES = ['frag_bazar_a.en.html', 'frag_bazar_b.en.html', 'frag_cap8.en.html', 'frag_ch1a.en.html',
            'frag_ch1b.en.html', 'frag_ch2.en.html', 'frag_ch3.en.html', 'frag_ch4.en.html',
            'frag_ch5.en.html', 'frag_ch67.en.html', 'frag_math.en.html', 'frag_glosario.en.html',
            'frag_intro.en.html', 'frag_acelerado.en.html', 'p3_tesis_en.html']

modo = sys.argv[1] if len(sys.argv) > 1 else 'titulos'
cambios = 0

if modo == 'titulos':
    for f in ES_FILES + EN_FILES:
        if not os.path.exists(f):
            continue
        shutil.copyfile(f, f + '.bak_barrido')
        s = io.open(f, encoding='utf-8').read()
        o = s
        es = '.en.' not in f and 'tesis_en' not in f
        for a_es, b_es, a_en, b_en in mm.TITULOS:
            a, b = (a_es, b_es) if es else (a_en, b_en)
            if a in s:
                s = s.replace(a, b)
                cambios += 1
        for ref, b_es, b_en in mm.REFS:
            a = 'Ref: ' + ref
            if a in s:
                s = s.replace(a, 'Ref: ' + (b_es if es else b_en))
                cambios += 1
        if s != o:
            io.open(f, 'w', encoding='utf-8').write(s)
            print(' ', f)
    print('titulos y refs:', cambios)

elif modo == 'texto':
    PARES = sorted(mm.INLINE, key=lambda x: -len(x[0]))
    for f in ES_FILES + EN_FILES:
        if not os.path.exists(f):
            continue
        s = io.open(f, encoding='utf-8').read()
        o = s
        es = '.en.' not in f and 'tesis_en' not in f
        for a, b_es, b_en in PARES:
            b = b_es if es else b_en
            if a not in s:
                continue
            n = s.count(a)
            # al principio de frase o de celda, con mayuscula
            B = b[0].upper() + b[1:]
            s = re.sub(r'(<td>|<li>|<p>|<strong>|\. |: |» |“|«|\(|— )' + re.escape(a), lambda m: m.group(1) + B, s)
            s = s.replace(a, b)
            cambios += n
        if s != o:
            io.open(f, 'w', encoding='utf-8').write(s)
    print('menciones sustituidas:', cambios)
