# Vuelve a encajar una voz ya grabada sobre una grabación nueva de la App.
#   python reencajar_voz.py
# La voz se grabó sobre el vídeo de v1/: se corta en frases, por el silencio
# más cercano al principio de cada subtítulo, y cada frase se mueve lo que se
# haya movido su subtítulo en el vídeo nuevo. Los efectos, igual, y en el sitio
# en que los dejó el autor en su mezcla de Audacity.
# La música no baja cuando hablas: va a volumen constante, y una curva lenta
# compensa las subidas propias del tema. Al final, fundido desde la última frase.
# Deja las pistas en pistas-audacity-v2/ y una mezcla de prueba con el vídeo.
import os, subprocess, json
import numpy as np
import imageio_ffmpeg

FF = imageio_ffmpeg.get_ffmpeg_exe()
AQUI = os.path.dirname(os.path.abspath(__file__))
SR = 48000
PISTAS = os.path.join(AQUI, 'pistas-audacity')
SALIDA = os.path.join(AQUI, 'pistas-audacity-v2')
SRT_VIEJO = os.path.join(AQUI, 'v1', 'nogum-app-innsmouth.srt')
SRT_NUEVO = os.path.join(AQUI, 'nogum-app-innsmouth.srt')
VIDEO = os.path.join(AQUI, 'nogum-app-innsmouth.mp4')
MUSICA = os.path.join(AQUI, 'musica-trailer.wav')
PRUEBA = os.path.join(AQUI, 'nogum-app-innsmouth-voz-v2.mp4')
# las respiraciones bajan 10 dB; la voz hablada no se toca
PUERTA = 'agate=threshold=0.018:ratio=2:range=0.3:attack=10:release=250:detection=rms'
# (pista, subtítulo al que va atado, cuánto lo movió el autor en su mezcla)
EFECTOS = [('4-efecto-camara.wav', 22, 0.53), ('5-efecto-revolver.wav', 23, 0.66), ('6-efecto-cuaderno.wav', 25, 4.60)]


def carga(p, filtro=None, canales=1):
    a = [FF, '-v', 'error', '-i', p]
    if filtro: a += ['-af', filtro]
    a += ['-ac', str(canales), '-ar', str(SR), '-f', 'f32le', '-']
    x = np.frombuffer(subprocess.run(a, capture_output=True, check=True).stdout, np.float32)
    return x.reshape(-1, canales).copy()


def guarda(p, x):
    subprocess.run([FF, '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', str(x.shape[1]), '-i', '-',
                    '-c:a', 'pcm_s16le', p], input=np.ascontiguousarray(x, np.float32).tobytes(), check=True)


def srt(p):
    seg = lambda s: (lambda h, m, x: int(h) * 3600 + int(m) * 60 + float(x.replace(',', '.')))(*s.split(':'))
    return [seg(b.split('\n')[1].split(' --> ')[0]) for b in open(p, encoding='utf-8').read().strip().split('\n\n')]


def duracion(p):
    r = subprocess.run([FF, '-i', p], capture_output=True, text=True).stderr
    h, m, s = r.split('Duration: ')[1].split(',')[0].split(':')
    return int(h) * 3600 + int(m) * 60 + float(s)


def pega(destino, trozo, en):
    i = int(round(en * SR))
    if i < 0: trozo, i = trozo[-i:], 0
    j = min(len(destino), i + len(trozo))
    destino[i:j] += trozo[:j - i]


viejo, nuevo = srt(SRT_VIEJO), srt(SRT_NUEVO)
assert len(viejo) == len(nuevo), 'los dos vídeos no tienen los mismos subtítulos'
mueve = [n - v for v, n in zip(viejo, nuevo)]
D = duracion(VIDEO); N = int(D * SR)
os.makedirs(SALIDA, exist_ok=True)

# ---- la voz, frase a frase ----
voz = carga(os.path.join(PISTAS, '2-voz-limpia.wav'), PUERTA)[:, 0]
v = 0.1 * SR  # ventanas de 100 ms
energia = lambda a, b: np.sqrt((voz[a:b] ** 2).mean()) if b > a else 1
cortes = [0]
for t in viejo[1:]:
    ini, fin = int((t - 1.5) * SR), int((t + 0.3) * SR)
    ini = max(ini, cortes[-1] + int(v))
    mejor = min(range(ini, fin, int(v / 2)), key=lambda k: energia(k, k + int(v)))
    cortes.append(mejor + int(v / 2))
cortes.append(len(voz))
nueva_voz = np.zeros(N, np.float32)
for i in range(len(viejo)):
    pega(nueva_voz, voz[cortes[i]:cortes[i + 1]], cortes[i] / SR + mueve[i])
habla = np.where(np.abs(nueva_voz) > 0.1)[0]
fin_voz = habla[-1] / SR if len(habla) else D - 3
# después de la última frase solo queda el clic del ratón al parar la grabación
k = int((fin_voz + 0.4) * SR)
nueva_voz[k:k + SR // 20] *= np.linspace(1, 0, len(nueva_voz[k:k + SR // 20]))
nueva_voz[k + SR // 20:] = 0

# ---- los efectos ----
efectos = []
for f, sub, autor in EFECTOS:
    x = carga(os.path.join(PISTAS, f), canales=2)
    e = np.zeros((N, 2), np.float32)
    pega(e, x, autor + mueve[sub - 1])
    efectos.append((f, e))

# ---- la música, a volumen constante ----
mus = carga(MUSICA, canales=2)[:N]
if len(mus) < N: mus = np.vstack([mus, np.zeros((N - len(mus), 2), np.float32)])
mono = mus.mean(1); paso = SR // 4; ven = 2 * SR
tiempos = np.arange(0, N - ven, paso)
nivel = np.array([10 * np.log10((mono[k:k + ven] ** 2).mean() + 1e-12) for k in tiempos])
suave = lambda y, s: np.convolve(np.pad(y, (int(s * 4), int(s * 4)), 'edge'), np.ones(int(s * 4)) / int(s * 4), 'same')[int(s * 4):-int(s * 4)]
nivel = suave(nivel, 6)
objetivo = np.median(nivel[tiempos < 45 * SR])  # el nivel del arranque, que es el que suena bien
gan_db = suave(np.clip(objetivo - nivel, -9, 2), 4)
gan = 10 ** (np.interp(np.arange(N), tiempos + ven // 2, gan_db) / 20)
# fundido final, desde que acabas de hablar
f0 = int((fin_voz + 0.3) * SR)
if f0 < N:
    gan[f0:] *= 0.5 * (1 + np.cos(np.linspace(0, np.pi, N - f0)))
mus = mus * gan[:, None].astype(np.float32)

# ---- la mezcla ----
mezcla = mus + nueva_voz[:, None] + sum(e for _, e in efectos)
# a −14 LUFS, como la mezcla a mano, y sin pasar de −1 dB
tmp = os.path.join(SALIDA, '_tmp.wav'); guarda(tmp, mezcla)
r = subprocess.run([FF, '-i', tmp, '-af', 'loudnorm=print_format=json', '-f', 'null', '-'], capture_output=True, text=True).stderr
I = float(json.loads(r[r.rindex('{'):r.rindex('}') + 1])['input_i'])
g = 10 ** ((-14 - I) / 20)
os.remove(tmp)

guarda(os.path.join(SALIDA, '2-voz-reencajada.wav'), np.repeat((nueva_voz * g)[:, None], 2, 1))
guarda(os.path.join(SALIDA, '3-musica-constante.wav'), mus * g)
for f, e in efectos:
    guarda(os.path.join(SALIDA, f), e * g)
ref = os.path.join(SALIDA, '0-mezcla-de-referencia.wav')
subprocess.run([FF, '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-',
                '-af', 'alimiter=limit=0.89:level=false', '-c:a', 'pcm_s16le', ref],
               input=np.ascontiguousarray(mezcla * g, np.float32).tobytes(), check=True)
subprocess.run([FF, '-v', 'error', '-y', '-i', VIDEO, '-i', ref, '-map', '0:v', '-map', '1:a', '-c:v', 'copy',
                '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', PRUEBA], check=True)
print('vídeo %.1f s · última frase %.1f s · música %+.1f a %+.1f dB · volumen %+.1f dB'
      % (D, fin_voz, gan_db.min(), gan_db.max(), -14 - I))
print('frases movidas: %+.2f … %+.2f s' % (min(mueve), max(mueve)))
