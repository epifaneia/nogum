# trad_T5 · Traducción de fH, fL y fJ2

Salida:
- `src/v2/fH_faq_glosario.en.html` (apx-faq + apx-glosario)
- `src/v2/fL_referencia.en.html` (hoja de referencia)
- `src/v2/fJ2_cap9b.en.html` (9.4: recetas, crítica, títulos, Piedra Rosetta, expedientes)

## Reaprovechado

- **fJ2**: base `src/frag_cap8.en.html` (recetas 1–20, crítica, títulos, Rosetta, ED-R*, expedientes de Inés). Se corrigió en todo lo que el castellano v2 ha cambiado: los techos de cada receta («Nivel máximo de los jugadores», con las cifras nuevas y los párrafos C·22oct sobre fama = Llaves), la línea «En NOGUM» (antes «In canon»), las referencias numeradas que ahora son enlaces (3.1, 3.5, 4.7…), la receta 6 (Tragedia en dosis), la 12 (dioses de nivel 6, no decorado), la 13 (la Generación, el 2 físico que sale del bote), la 14 (Llaves de Disciplinas enteras + Vínculos), la 18 (dos fichas), la 20 (texto nuevo del canon), la crítica (2·1·1·2, no 2·1·4·2), la Rosetta (Caos Bajo, «sistemas de movimientos»), ED-R1/ED-R2 y las Llaves de Inés en las primeras noches (ya sin objetivo: «Fortitude +1 level», etc.).
- **fH glosario**: `frag_glosario.en.html` es una versión mucho más vieja y distinta; solo sirvió de referencia de tono. Traducido de nuevo entero.
- **fH FAQ y fL**: no había inglés previo. Traducidos de cero.

## Glosario: orden y headwords

Las 62 entradas están en orden alfabético inglés (comprobado por script, sin distinguir mayúsculas e ignorando «[» y apóstrofos), con los mismos ids `gl-…`. Comprobado por script que cada id conserva sus mismos `href` y sus mismas `src`. Headwords elegidos:

| id | Headword |
|---|---|
| gl-baul | Rules Chest (va en la R) |
| gl-bazar | Multiverse Bazaar (en la M) |
| gl-cerrojos | Locks (on equipment) |
| gl-llave-prestada | Borrowed Key (or momentary Key) |
| gl-tarjeta | Tone card (en la T) |
| gl-regalo | GM’s gift |
| gl-rejilla-tag | [Grid] (tag), justo detrás de Grid |
| gl-etiquetas | Tags (Damage, Dodge, Soak) |
| gl-monedero | Purse |
| gl-fuera | Out of the fight |

- `gl-rejilla`: la nota castellana «En inglés, <em>Grid</em>» se ha invertido: «In Spanish, <em>Rejilla</em>». Dudoso pero lógico; se puede quitar.
- La nota meta final (malla/cota) se ha adaptado: «If you ever come across a plain “mesh”, it is the Grid by its homely old name. Unless it belongs to a mail shirt.» (*mesh* era el nombre viejo en inglés y sirve también para la malla de una cota).

## Términos nuevos que tuve que elegir (no están en TRADUCCION.md)

- Nivel máximo de los jugadores (etiqueta de cada receta) → **Player maximum**; abreviaturas de ámbitos **Phy · Men · Soc · Tec · Arc**.
- saltos pactados → **agreed jumps** (el inglés viejo decía *pacted jumps*; lo cambié para casar con «la muerte se pacta» → *death is agreed*).
- salto de nivel → **level gap** (el viejo decía *power gap*).
- Regla del Estilo / Regla de Masillas → **Style Rule / Mook Rule** (como el viejo).
- Sano / Herido / Crítico / Fuera de combate → **Healthy / Wounded / Critical / Out of the fight** (como el viejo).
- Valores de etiqueta: Total / Parcial / Difícil / Fácil / Nula / Máx N → **Full / Partial / Hard / Easy / None / Max N** (como el viejo). La etiqueta de daño, **Damage N** (no *Dmg*, según TRADUCCION.md): `Spiritual Damage 1`, `Social Damage N`, `Mental Damage 2`.
- «Esto no vale» → **“That doesn’t count”** (el del capítulo 0 viejo).
- En NOGUM (línea de canon de cada receta) → **In NOGUM**.
- el taller / los casos resueltos del Bazar → **the Bazaar’s workshop / the Bazaar’s solved cases**.
- Hoja de referencia, columnas: Lees → **You read**; Con coste → **At a cost**; Se paga → **Paid with**; cap. → **ch.**
- Los simuladores narrativos / los sistemas de movimientos (Rosetta) → **The narrative simulators / The moves-based systems**.
- Pilotaje (ED-R3) → **Piloting**.

## Marcas `src`

Se dejan sin traducir, como pide el encargo, incluidas «Aprobado por el autor» y «Decisión del autor» (el inglés viejo las había traducido). Si el maquetador las muestra en la edición inglesa, habría que decidir si se traducen.

## Pasajes dudosos

- Receta 1: «aquí, que es fiable y a voluntad, entero» lo leo como el Ajuste Completo → «here, since it is reliable and at will, Complete». Si «entero» quería decir otra cosa (el precio sin rebaja de Limitado), el sentido es el mismo.
- Receta 13: «lo que de verdad da juego en mesa: el mono» → «the thing that actually gives you play at the table: the craving». *Craving* repite la palabra de antes en vez de *withdrawal*; me pareció más claro.
- Receta 5: «hace arriar banderas» → «makes ships strike their colours».
- FAQ: «¿Una Llave va contra un objetivo?» → «Is a Key aimed at one target?».

## Hoja de referencia: una cara de A4

Renderizada en Chrome headless con `paper.css` + `v2.css` (como el test de la hoja castellana): castellano **934 px** de 973 disponibles; inglés **933 px** tras recortar cuatro frases (sin perder contenido: «if so», «the Arcane point», «Highest first»…). Cabe y no es más larga que la castellana.

## Comprobación de estructura (script)

| Fichero | etiquetas | ids | href | clases | src | flags | equilibrado |
|---|---|---|---|---|---|---|---|
| fH | iguales | mismos 69 (el orden del glosario cambia a propósito) | mismos 162 (multiconjunto; por entrada, iguales) | iguales | iguales por entrada | iguales | sí |
| fL | iguales | iguales | iguales, mismo orden (32) | iguales | iguales | iguales | sí |
| fJ2 | iguales | iguales, mismo orden (12) | iguales, mismo orden (70) | iguales | iguales | iguales | sí |

Mismas tablas con el mismo número de filas y columnas (el recuento de `tr`/`td`/`th` es idéntico). Números de apartado y de receta, iguales.
