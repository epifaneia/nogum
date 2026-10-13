# -*- coding: utf-8 -*-
"""Lleva al canon el modelo de siete tarjetas (decisiones del autor, 18-IX-2026)."""
import io, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
s = io.open('CANON.md', encoding='utf-8').read()
assert 'ED-18' not in s, 'ya aplicado'

BLOCK = """
## 2bis. EL CUADRANTE DE SIETE TARJETAS (modelo vigente)
Sustituye al panel de 6 tarjetas + recetas. Decidido por el autor tras el taller de palancas.
- **Las cinco palancas** y su vector (centro / dispersión / espectáculo):
  1. Lectura mejor o peor de 2d10: mueve el centro (media 7,15 o 3,85 frente a 5,5) Y concentra (DT 2,35 vs 2,87 del dado plano). Es DIAGONAL: cuenta como dos palancas. Por eso vive en las esquinas de la columna previsible.
  2. Suma 2d10: no mueve el centro, concentra al máximo (DT 2,03 equivalente), apaga el espectáculo (extremos 3 %).
  3. Ruido (rangos naturales ampliados): no mueve el centro ni la dispersión; multiplica el espectáculo. Se aplica AL VALOR LEÍDO: rojo 20/20, mejor 4/36, peor 36/4. Se inclina solo según el tono.
  4. Zona de roce (éxito con coste): la TN y el punto justo por debajo (5–6 con TN 6; 10–11 con TN 11). Ocupa ~20 % en las cuatro lecturas. Si un coste vale medio éxito, no mueve el centro. Caos puro.
  5. TN: única palanca de optimismo puro, PERO NO se usa para construir el cuadrante (ED-19). Un número por lectura: 6 (dado, mejor, peor) y 11 (suma).
- **Palancas descartadas y por qué**: dados explosivos (rompen el anclaje [−2,+4]); mejor de 3 (mismo vector, más dados); mover el anclaje (obliga a rehacer fichas; la tesis es cambiar de reglas sin tocar la ficha); que el jugador elija la lectura tras ver los dados (el tono lo ponen mesa y DJ antes de tirar; si nadie dice nada vale el de la campaña); qué hace una pifia (no es palanca: es decisión del narrador; la complicación pequeña vive en la zona de roce).
- **Arquitectura**: una palanca por columna, la fila elige la dirección. Fila = de qué lado está el universo. Columna = cuánto se le nota.
- **Las siete tarjetas** (cifras exactas con bono 0: pifia / fallo / coste / éxito / crítico → sale bien):
  - Héroe (optimista·previsible): mejor de 2d10, TN 6. 1/24/0/56/19 → 75 %. Del nulo al maestro: 51 → 99 %.
  - Leyenda (optimista·caótico): mejor de 2d10 + zona de roce + ruido. 4/12/20/28/36 → 84 %. 64 → 96 %.
  - Realista (neutral·previsible): suma 2d10, TN 11, naturales 2–3 / 19–20. 3/42/0/52/3 → 55 %. 36 → 85 %.
  - Estándar (neutral·neutral): dado rojo, TN 6. 10/40/0/40/10 → 50 %. 30 → 90 %.
  - Gonzo (neutral·caótico): dado rojo + zona de roce + ruido. 20/20/20/20/20 → 60 %. 40 → 80 %. Única distribución uniforme del juego (ED-21).
  - Terror (opresivo·previsible): peor de 2d10, TN 6. 19/56/0/24/1 → 25 %. 9 → 81 % (es donde más pesa la ficha).
  - Pesadilla (opresivo·caótico): peor de 2d10 + zona de roce + ruido. 36/28/20/12/4 → 36 %. 16 → 64 %. Aviso de uso en el manual: pensada para sesiones sueltas, no para campaña.
- **Dos huecos reales**: optimista·neutral y opresivo·neutral. Con dado plano no hay forma de inclinar el tono sin mover la TN, y la TN no se mueve. Se dibujan a la vista y se invita a rellenarlos. Los géneros de 1.2 que caen ahí (Épica clásica, Thriller de supervivencia) usan la tarjeta vecina.
- **Lectura del cuadrante como espectro**: los ejes no son binarios; la partida cae en un punto y, cerca de un borde, se toma prestada solo una parte de la tarjeta vecina (p. ej. la banda sin el ruido).
- **Propiedades medidas**: contando un coste como medio éxito, la columna caótica tiene el mismo centro que la previsible (74/50/26 vs 75/55/25 con bono 0). Con bono −2 ambas columnas empatan; con +4 el orden premia al experto (81 % en la fila opresiva) y el ruido lo frena (64 %): el caos iguala. Con bono −2, en las dos esquinas caóticas desaparece el éxito normal (o milagro o coste). Con +4 se cierra la zona de roce.
- **Recetas que sí mueven la TN** (deben decirlo en voz alta y valen para toda la campaña): Tragedia = suma 2d10 vs TN 14 (3/69/0/25/3 → 28 % con bono 0; 15 → 64 %).
- **ED-18 (regla única de naturales)**: «mira el número que vas a usar: si es 1, pifia; si es 10, crítico». Reproduce exactamente los valores anteriores (mejor de 2: 1 % y 19 % = doble 1 / cualquier 10; peor de 2: 19 % y 1 %; rojo: 10 % y 10 %) y elimina los casos especiales. La suma conserva su línea propia: 2–3 y 19–20 (3 %), decidido frente a la alternativa literal 2 y 20 (1 %), que dejaba a la Realista sin momentos memorables.
- **ED-19 (la TN no es palanca de tono)**: un número por lectura (6 y 11). Mover la TN por escena es la fricción que el juego promete quitar. El ruido y la zona de roce hacen el trabajo.
- **ED-20 (el centro es la costumbre, no la objetividad)**: la columna central es el dado plano porque es lo que hace el hobby (d20, d100), no porque sea el punto medio estadístico; de hecho es la lectura más aleatoria. El eje mide distancia respecto a la expectativa de la mesa. Decisión explícita del autor.
- **ED-21 (el centro caótico lleva las dos herramientas)**: como ni el ruido ni la zona de roce inclinan el tono, en la casilla sin dirección se aplican juntos: pifia 1–2, coste 5–6, crítico 9–10 → cinco resultados al 20 %.
- **ED-15 (revisada)**: las bandas de Agobio en Acelerado pasan a ser la zona de roce del manual completo (fallo ≤4, coste 5–6, éxito 7+) sobre el dado menor. Confirmado por el autor. Consecuencia: profesional (+2) sale adelante 64 % (36 % limpio).
- **Tarjetas retiradas**: T0–T6 y las recetas Épica Clásica / Pulp Desatado / Pesadilla del panel anterior quedan superadas por las siete. Su rastro se conserva en el Cuaderno de Diseño.
"""

anchor = '\n## 3. Capítulo 2 — El Ancla (Rejilla de Potencia)'
assert s.count(anchor) == 1
s = s.replace(anchor, '\n' + BLOCK.strip() + '\n' + anchor)
io.open('CANON.md', 'w', encoding='utf-8').write(s)
print('canon actualizado ·', len(s.encode()) // 1024, 'KB')
