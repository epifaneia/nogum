# NOGUM v2 · Última revisión profunda

El autor, tras leerlo: «tiene una pinta brutal». Esta es la última pasada antes de que sustituya al libro viejo. Busca **fallos, repeticiones, asunciones y fallos estéticos**, y arregla lo que sea claro. Lo que no lo sea, apúntalo.

Antes de nada, lee: `src/CANON.md` desde la línea 1 hasta «Jerarquía de autoridad» (la palabra del autor, con todas sus aclaraciones y respuestas: es la única verdad), `src/v2/MAPA.md` §2–3 (voz y marcado) y `src/v2/CONCEPTOS.md` (los dos fallos de presentación). Lee tus ficheros **enteros, en orden de lectura**, como un lector que llega por primera vez.

## Qué buscar

1. **Contradicciones con el canon** o entre capítulos (cifras, nombres, reglas). Lo que el canon dice manda. Ojo con lo último que se ha aclarado: el éxito con coste solo existe en el Pulp desenfrenado y la Comedia negra (total 6 o 7); las masillas son decorado (sin ficha ni tirada); la Parca va Limitada al daño; una Llave por rasgo, sin cobrar dos veces el mismo concepto; las ventajas y lacras se compran y ocurren; la Llave de un momento no es crecer.
2. **Repeticiones**: un caso o una regla contada entera en dos sitios. Se queda en su casa y en el otro, una frase y enlace. También frases repetidas dentro de un mismo apartado.
3. **Asunciones**: un término usado antes de presentarse (CONCEPTOS.md, Fallo 1), o un fantasma de corrección (Fallo 2).
4. **Voz**: frases rotas o mal construidas (ejemplo real: «como el de el del sombrero y el látigo»; «el ejemplo contrario… es los sistemas de comedia negra»), condescendencia, absolutos en el texto de reglas («nunca», «siempre», «como mucho» —ojo: «casi siempre», «nunca» en una frase normal que no es regla, valen—), nombres con copyright.
5. **Erratas y estética del marcado**: tildes, concordancias, comillas «» sin cerrar, dobles espacios, tablas con filas o columnas que faltan o no cuadran (ejemplo real, ya arreglado: a la tabla de la escalera llana le faltaba la fila +3), recuadros vacíos, listas rotas, encabezados de tabla que no casan con sus celdas, números de apartado que no casan con su título, marcas `src` pegadas a la palabra.
6. **Coherencia de cifras en ejemplos**: cada tirada de ejemplo, cada cuenta de ficha y cada precio, recalculado.

## Reglas

- No cambies ninguna regla ni quites ejemplos únicos. «Que cada palabra cuente», sin apretar por apretar.
- Mantén los ids y los enlaces (`href="#…"` a ids que existan en `src/v2/f*.html`) y el HTML equilibrado. Comprueba con un script al acabar.
- Escribe `src/v2/final_<letra>.md` con cada cambio (fichero, sitio, tipo, antes → después) y las dudas para el autor. Informe final corto.
