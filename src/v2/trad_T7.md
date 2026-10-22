# trad_T7 · fB_apendices → fB_apendices.en.html

**Encargo:** Apéndice A · The Engine Room y Apéndice B · Full Tables.

## Método

- Base: `src/frag_math.en.html`, que va línea a línea con `src/frag_math.html` (castellano viejo). Alineé el castellano viejo con el v2 (difflib) y copié por script el inglés de cada línea idéntica, SVG incluidos. Solo se tradujeron a mano las ~75 líneas que cambian en el v2.
- Cambios del v2 que se aplicaron: numeración A.1–A.10 y A.3.1/A.3.2; «Apéndice D» → «Appendix B»; lede nuevo; A.6 reescrito (el Ancla, el exceso por encima de +4, el GM por debajo de −2); palanca 5 «Moving the TN» y la Tragedia como excepción declarada; dificultad como modificador (+2 easy, 0, −2 hard, −4 heroic); pie de las gráficas «the GM invents something» → «the story takes a turn on X% of rolls»; A.9 sin «inventar algo»; aside del 99 %; A.10: Arcano por mesa (nobody/someone plays Arcane, los 14 para todos), Rejilla que abre la historia dentro de los techos, escalera de Llaves solo n² con la llana enviada al Rules Chest (9.1), lectura tangible/narrativa, una Llave por sesión y por jugador; Apéndice B: intro y «The declared exception» con el consejo de no quedarse en los tonos oscuros; frase final de la Tragedia; `</section>` movido igual que en el castellano.

## Correcciones al inglés viejo (aunque el castellano no cambiara)

- «los sistemas de movimientos» se había quedado sin traducir → *the moves systems*.
- «Call of the antediluvian octopuses» → *the antediluvian octopuses* (el castellano no dice «La llamada»).
- «FATE» (nombre con copyright) → *The plus-and-minus dice system*, como el castellano v2.
- «Black comedy» → **Black Comedy** (tabla de términos), también dentro de los SVG.
- «higher/lower of two» → **best/worst of two** (tabla de términos), en texto, leyendas y tablas.
- Quitado un `<em>is</em>` que el castellano no tiene (para que cuadren las etiquetas).
- «a 1 never reaches the TN» → «does not reach» (el castellano no dice «nunca»).

## Términos elegidos (no están en la tabla)

| Castellano | English | Nota |
|---|---|---|
| casillas (de la pirámide) | slots | Del inglés viejo. *Boxes* se reserva para la vida fractal. |
| sale adelante | works out | Del inglés viejo. |
| la historia se tuerce | the story takes a turn | Pie de cada gráfica. |
| el sistema de los dados de más y menos | the plus-and-minus dice system | Arquetipo de FATE. |
| los sistemas de movimientos | the moves systems | Arquetipo de PbtA. |
| módulo del Destino (Baúl) | the Rules Chest’s Destiny module | `frag_cap8.en` dice «Destiny (Wyrd)». |
| excepción declarada | declared exception | |
| lectura tangible / narrativa | tangible / narrative reading | Tabla. |

## Dudosos

- «Se tiran siempre los dos», «siempre ocurre algo», «siempre hay otra Disciplina»: dejé *always* porque el castellano dice «siempre» y son hechos, no topes de reglas.
- «la mesa es adulta y decide» → «the table is made of adults, and it decides». Se puede suavizar si suena raro.

## Comprobación de estructura (script)

- 1026 líneas en los dos archivos; mismo número de etiquetas de cada tipo.
- ids (21), href (25), `span.src` (22), banderas `flag` (6) y atributos `class` (1423): idénticos y en el mismo orden.
- HTML equilibrado en los dos (HTMLParser: sin etiquetas abiertas ni cierres sueltos).
- 10 SVG, idénticos si se les quita el texto y el `aria-label`.
- Cifras por línea: iguales salvo la línea 666 («un 1 % arriba y otro abajo» → «1 % above and 1 % below»), lo esperado.
- Sin restos de castellano (búsqueda de acentos, «¿», ««», DJ, Director, etc.).
