# Monta la voz del autor sobre el vídeo con música, sin volver a codificar la imagen,
# y deja las pistas sueltas para editarlas a mano en Audacity.
#   python montar_voz.py ../../voz2.mp3 2.81
# El segundo número es el desfase: el segundo de la grabación que cae en el
# segundo 0 del vídeo (toma 1: 2,39; toma 2: 2,81). La voz no se recorta: el
# autor dice la presentación a propósito antes del primer subtítulo.
# La grabación viene de la interfaz en estéreo con el micro en la entrada 2, así
# que la voz está en el canal derecho.
import os, subprocess, sys
import imageio_ffmpeg

FF = imageio_ffmpeg.get_ffmpeg_exe()
AQUI = os.path.dirname(os.path.abspath(__file__))
MUDO = os.path.join(AQUI, 'nogum-app-innsmouth.mp4')
PISTA = os.path.join(AQUI, 'musica-trailer.wav')
LIMPIA = os.path.join(AQUI, 'voz-limpia.wav')
CON_VOZ = os.path.join(AQUI, 'nogum-app-innsmouth-voz.mp4')
PISTAS = os.path.join(AQUI, 'pistas-audacity')

CANAL = 1            # 0 izquierdo (entrada 1), 1 derecho (entrada 2)
DESFASE = 2.81       # segundo de la grabación que cae en el 0 del vídeo

# los efectos, con el golpe en el fotograma en que el objeto entra en la ficha:
# (archivo, segundo del vídeo donde empieza, desde dónde del archivo, cuánto dura, dB)
SFX = [
    ('camara.wav',   134.15, 0.0, 3.6, -10),  # el disparo (1,45 s del archivo) cae en 135,6
    ('revolver.wav', 138.28, 0.0, 3.6, -10),  # el primer amartillado (0,85 s) cae en 139,1
    ('cuaderno.wav', 147.95, 0.3, 2.6, -6),   # dos hojas que pasan, al salir el cuaderno
]

def ff(*a):
    subprocess.run([FF, '-y', '-loglevel', 'error', *a], check=True)

def dura(f):
    r = subprocess.run([FF, '-i', f], capture_output=True, text=True).stderr
    h, m, s = r.split('Duration: ')[1].split(',')[0].split(':')
    return int(h) * 3600 + int(m) * 60 + float(s)

voz = sys.argv[1] if len(sys.argv) > 1 else os.path.join(AQUI, '..', '..', 'voz2.mp3')
if len(sys.argv) > 2: DESFASE = float(sys.argv[2])
D = dura(MUDO)
# la voz en el reloj del vídeo, entera: solo se desplaza, y se rellena hasta el final
RELOJ = 'pan=mono|c0=c%d,atrim=start=%.2f,asetpts=PTS-STARTPTS,aresample=48000,apad,atrim=0:%.2f' % (CANAL, DESFASE, D)

# 1 · la voz limpia: graves de mesa fuera, un reductor de ruido suave y el volumen igualado
ff('-i', voz, '-af', RELOJ + ',highpass=f=80,afftdn=nr=10:nf=-50,loudnorm=I=-16:TP=-1.5:LRA=11',
   '-ar', '48000', '-c:a', 'pcm_s16le', LIMPIA)

# 2 · los efectos, cada uno en su sitio
entradas, cadenas, etiquetas = [], [], []
for k, (f, en, desde, dur, gan) in enumerate(SFX):
    entradas += ['-i', os.path.join(AQUI, 'sfx', f)]
    cadenas.append('[%d:a]aformat=sample_rates=48000:channel_layouts=stereo,atrim=start=%.2f:duration=%.2f,'
                   'asetpts=PTS-STARTPTS,afade=t=out:st=%.2f:d=0.4,volume=%ddB,adelay=%d:all=1[s%d]'
                   % (3 + k, desde, dur, dur - 0.4, gan, int(en * 1000), k))
    etiquetas.append('[s%d]' % k)

# 3 · la mezcla de referencia: la música baja cuando hablas, los efectos encima
ff('-i', MUDO, '-i', PISTA, '-i', LIMPIA, *entradas, '-filter_complex',
   '[2:a]asplit=2[v][vk];'
   '[1:a][vk]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=400[mb];' +
   ''.join(c + ';' for c in cadenas) +
   '[mb][v]%samix=inputs=%d:duration=first:normalize=0,volume=2dB,alimiter=limit=0.95[out]'
   % (''.join(etiquetas), 2 + len(SFX)),
   '-map', '0:v', '-map', '[out]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
   '-movflags', '+faststart', CON_VOZ)

# 4 · las pistas sueltas para Audacity: todas empiezan en el 0 del vídeo y duran
#     lo mismo, así que al importarlas juntas quedan alineadas
os.makedirs(PISTAS, exist_ok=True)
w = lambda n: os.path.join(PISTAS, n)
wav = ['-ar', '48000', '-c:a', 'pcm_s16le']
ff('-i', voz, '-af', RELOJ, *wav, w('1-voz-original.wav'))
ff('-i', LIMPIA, *wav, w('2-voz-limpia.wav'))
ff('-i', PISTA, '-af', 'apad,atrim=0:%.2f' % D, *wav, w('3-musica.wav'))
for k, (f, en, desde, dur, gan) in enumerate(SFX):
    ff('-i', os.path.join(AQUI, 'sfx', f), '-af',
       'aformat=sample_rates=48000:channel_layouts=stereo,atrim=start=%.2f:duration=%.2f,asetpts=PTS-STARTPTS,'
       'afade=t=out:st=%.2f:d=0.4,volume=%ddB,adelay=%d:all=1,apad=whole_dur=%.2f'
       % (desde, dur, dur - 0.4, gan, int(en * 1000), D), *wav, w('%d-efecto-%s.wav' % (4 + k, os.path.splitext(f)[0].lower())))
ff('-i', CON_VOZ, '-vn', '-af', 'apad=whole_dur=%.2f' % D, *wav, w('0-mezcla-de-referencia.wav'))
print('con voz:', CON_VOZ)
print('pistas:', PISTAS)
