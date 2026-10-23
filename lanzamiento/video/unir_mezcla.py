# Pega una mezcla hecha a mano (Audacity) al vídeo, sin volver a codificar la imagen.
#   python unir_mezcla.py pistas-audacity/mezcla-final.wav
import os, subprocess, sys
import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
AQUI = os.path.dirname(os.path.abspath(__file__))
mezcla = sys.argv[1] if len(sys.argv) > 1 else os.path.join(AQUI, 'pistas-audacity', 'mezcla-final.wav')
salida = os.path.join(AQUI, 'nogum-app-innsmouth-final.mp4')
subprocess.run([FF, '-y', '-loglevel', 'error', '-i', os.path.join(AQUI, 'nogum-app-innsmouth.mp4'), '-i', mezcla,
                '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-shortest',
                '-movflags', '+faststart', salida], check=True)
print('final:', salida)
