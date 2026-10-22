# trad_T1 · Portada, «Cómo leer», introducción, seis ideas, caps. 0–1

Archivos: `p_juego_v2.en.html`, `fA_ideas_intro_0_1.en.html`.

## Fuentes reaprovechadas
- Portada: cabecera de `p3_juego.en.html` tal cual (Complete Game, English edition · System rulebook, acrónimo oficial en castellano con `lang="es"`, chistes en inglés). Traducidos de nuevo «How to read this manual», la leyenda (solo T68 / C·l2, como el v2) y el mapa de 9 filas.
- Introducción: `frag_intro.en.html`, corregida donde el v2 cambia (pilares 1 y 5 reescritos; enlaces a 0.6/0.7/2.5/0.4).
- Cap. 0: `frag_ch0.en.html` para 0.1–0.5; nuevos 0.4 (segundo párrafo), 0.6, 0.7, 0.8 y la entrada.
- Cap. 1: `frag_ch1a.en.html` (1.1, 1.2), `frag_ch1b.en.html` (tarjetas, avisos, cuadrante), `frag_math.en.html` (vocabulario del motor: readings, bands, lever, works out). Nuevos 1.3 entero y 1.5.
- Las seis ideas: traducción nueva.

## Términos elegidos (no estaban en la tabla)
| Castellano | English | Nota |
|---|---|---|
| se pacta / pactar (la muerte) | is agreed / agreed | 0.7 «Death is agreed»; el viejo usaba a veces «pacted» |
| fuera de combate | out of the fight | como el inglés viejo de cap. 5 |
| masillas | mooks | tabla (fichas) |
| Pelea (habilidad) | Brawling | como `frag_ch2/ch3.en` |
| techos de la Rejilla | the Grid ceilings | en 0.8; los tres techos van descritos en llano, como en el castellano |
| sale adelante | works out | como el viejo |
| la costumbre (columna) | the habit | como el viejo |
| Ni ordena ni hace ruido | Neither orders nor makes a fuss | el viejo decía «nor charges», que era otro texto |
| porcentaje de éxito (Ancla) | chance of success | |
| la vara (TN) | the bar | |
| el bote | the pot | coherente con «separate pot» |
| afectar (Llave) | touch | para casar con «Who You Can Touch» |

## Arquetipos
- «The Boys» del inglés viejo (nombre con copyright) → «the series about rotten superheroes, the one where the poster-boy paladins are worse than the villains», como dice el v2.
- «el mercenario bocazas» (el viejo lo dejaba en castellano) → «the motor-mouthed mercenary».
- «Call of the antediluvian octopuses» → «the antediluvian octopuses» (el v2 quita el título).
- «1984, Chernobyl» del viejo → «the dystopia of the all-seeing eye, the nuclear disaster told minute by minute» (el v2).
- «blaster pistol» → «laser pistol» (el castellano dice «pistola láser»).
- Siguen siendo arquetipos: the adventurer with the hat and the whip, the consultant from Baker Street, the alien in tights and trunks, the spy with a number, the criminals who save the galaxy, the killer who walks into dreams, the empire’s battle moon, a green stone. *Alice in Wonderland* se queda (dominio público, igual que en el castellano).

## Pasajes dudosos
- 0.7 «Lo que sí hace el tamaño es ponérselo difícil a la mesa» → «What size does do is make things hard for the table». Leo que un arma enorme hace difícil argumentar que el protagonista sobrevive; la traducción deja la misma ambigüedad que el original.
- Idea 5 «compran lo que te deja tocar lo que está por encima» → «buy what lets you touch what sits above you». Literal y algo forzado, como el castellano.
- La Pulp «un tercio de las tiradas viene con factura» (el viejo decía «of what they get»): sigo el v2.
- Absolutos: dejo los que vienen del castellano («No protagonist dies from a roll», «never using their position»): son el pacto, no reglas añadidas. No he metido ninguno nuevo.

## Comprobación de estructura (script, html.parser)
| | etiquetas | ids | href | clases | `src`/`flag` | equilibrado |
|---|---|---|---|---|---|---|
| p_juego_v2.en.html | iguales | 3 = 3 | 10 = 10 | iguales | 2 = 2 | sí |
| fA_ideas_intro_0_1.en.html | iguales | 40 = 40 | 70 = 70 | iguales | 62 = 62 | sí |

Única diferencia de atributo: la portada inglesa lleva `lang="es"` en `acro-official` (el acrónimo oficial en castellano), donde la castellana lleva `lang="en"`. Es lo que se pidió. No quedan apóstrofos rectos ni caracteres castellanos fuera de ese acrónimo.
