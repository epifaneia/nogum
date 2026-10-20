# Monta el vídeo de la App a partir de la grabación de grabar.js.
#   python montar.py            -> vídeo mudo + vídeo con música + pista de música
#   python montar.py voz.m4a    -> además, la versión con voz: la música baja sola cuando hablas
# Necesita imageio-ffmpeg (pip install imageio-ffmpeg) y la grabación en la carpeta temporal.
import os, subprocess, sys, tempfile, shutil
import imageio_ffmpeg

FF = imageio_ffmpeg.get_ffmpeg_exe()
AQUI = os.path.dirname(os.path.abspath(__file__))
TMP = os.path.join(tempfile.gettempdir(), 'nogum-video')
MUSICA = os.path.join(AQUI, 'Cjbeards - Shattered Glass.mp3')
MUDO = os.path.join(AQUI, 'nogum-app-innsmouth.mp4')
CON_MUSICA = os.path.join(AQUI, 'nogum-app-innsmouth-musica.mp4')
PISTA = os.path.join(AQUI, 'musica-trailer.wav')
CON_VOZ = os.path.join(AQUI, 'nogum-app-innsmouth-voz.mp4')

def ff(*a):
    subprocess.run([FF, '-y', '-loglevel', 'error', *a], check=True)

def dura(f):
    r = subprocess.run([FF, '-i', f], capture_output=True, text=True).stderr
    h, m, s = r.split('Duration: ')[1].split(',')[0].split(':')
    return int(h) * 3600 + int(m) * 60 + float(s)

# 1 · el vídeo, a 1920×1080 y 30 fps
ff('-f', 'concat', '-safe', '0', '-i', os.path.join(TMP, 'lista.txt'),
   '-vf', 'fps=30,scale=1920:1080:flags=lanczos:in_range=pc:out_range=tv,setsar=1,format=yuv420p',
   '-color_range', 'tv', '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709',
   '-c:v', 'libx264', '-preset', 'slow', '-crf', '18', '-movflags', '+faststart', MUDO)
shutil.copy(os.path.join(TMP, 'subtitulos.srt'), os.path.join(AQUI, 'nogum-app-innsmouth.srt'))
D = dura(MUDO)

# 2 · la música, estirada hasta D: se repite un trozo de la parte tranquila
#     (hacia el minuto 2:10) con un fundido de 3 s, para que el final natural
#     de la pista caiga sobre la tirada y el cartel
M = dura(MUSICA)
corte = 148.0
S = round(corte + M - 3 - D, 2)
if S >= corte:  # el vídeo es más corto que la pista: sin repetición
    filtro = '[0:a]atrim=0:%.2f,asetpts=PTS-STARTPTS' % D
else:
    filtro = ('[0:a]atrim=0:%.2f,asetpts=PTS-STARTPTS[a];[0:a]atrim=start=%.2f,asetpts=PTS-STARTPTS[b];'
              '[a][b]acrossfade=d=3:c1=tri:c2=tri' % (corte, S))
filtro += ',volume=-7.5dB,afade=t=in:st=0:d=2,afade=t=out:st=%.2f:d=3,atrim=0:%.2f[m]' % (D - 3, D)
ff('-i', MUSICA, '-filter_complex', filtro, '-map', '[m]', '-ar', '48000', '-c:a', 'pcm_s16le', PISTA)
ff('-i', MUDO, '-i', PISTA, '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
   '-shortest', '-movflags', '+faststart', CON_MUSICA)
print('vídeo %.1f s · repetición desde %.2f s' % (D, S))

# 3 · con voz: la música se aparta sola cuando hablas (sidechain)
if len(sys.argv) > 1:
    voz = sys.argv[1]
    ff('-i', MUDO, '-i', PISTA, '-i', voz, '-filter_complex',
       '[2:a]aresample=48000,loudnorm=I=-16:TP=-1.5:LRA=11,asplit=2[v][vk];'
       '[1:a][vk]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=400[mb];'
       '[mb][v]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.95[out]',
       '-map', '0:v', '-map', '[out]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
       '-movflags', '+faststart', CON_VOZ)
    print('con voz:', CON_VOZ)
