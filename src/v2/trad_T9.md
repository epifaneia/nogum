# trad_T9 · Bazar, segundo y tercer tramo

Archivos: `fK2_bazar_b.en.html` (secciones 8–10, Duelo Social, Piezas sueltas; dentro de `apx-bazar`, sin abrir ni cerrar sección) y `fK3_bazar_c.en.html` (resumen e índice; cierra la `</section>`).

## Reaprovechado
- Nombres de objetos y textos descriptivos: de `src/frag_bazar_b.en.html` (y `frag_bazar_a.en.html` para los objetos 1–5 en el índice). Las notas de precio («La cuenta: …», C·e8, C·l9, C·22oct…) son nuevas y se han traducido.
- Cabecera de las tablas del catálogo: Object · Damage · Dodge · Soak · Access · Points · Keys · Notes. Índice: Object · From · What it does · Price.
- «La cuenta:» → «Tally:»; «la cuenta» en el texto → «the tally»; «Ajuste:» → «Adjustment:».

## Términos elegidos (no estaban en la tabla)
| Castellano | English |
|---|---|
| Daño N (etiqueta) | Damage N (no «Dmg»: igual que los demás `.en` de v2) · Daño Mental/Social → Mental/Social Damage · Daño de retorno → Backfire Damage · Daño: Caída → Damage: Fall |
| Esq: Nula/Total/Parcial/Difícil/Fácil/Sorpresa | Dodge: None/Full/Partial/Hard/Easy/Surprise |
| Abs: Nula/Total/Máx 1/Voluntad/Mente/Reputación | Soak: None/Full/Max 1/Will/Mind/Reputation |
| Limitada al daño | Limited to damage |
| Parca N (en las notas) | Reaper N |
| la mitad al alza | half rounded up |
| de un solo uso: no se paga | single use: it is not paid for |
| que no se esquive, otra | being undodgeable, another |
| valor fuera de la leyenda | off-legend value |
| un útil: solo Acceso | a tool: Access only |
| Útiles (categoría del índice) | Tools |
| Pelea / Armas / Entereza / Potencia / Engaño / Sigilo / Liderazgo / Empatía / Alerta | Brawling / Weapons / Fortitude / Might / Deception / Stealth / Leadership / Empathy / Alertness (de `GLOSSARY_EN.md`) |
| Resucitado (Mano del Hombre Muerto) | Risen (el viejo decía «Harrowed», término de un juego con marca) |

## Nombres cambiados respecto al inglés viejo
- **Mineral fantasma (combustible)** → *Ghost Ore (fuel)*. El viejo decía «Ghost Rock», que es nombre de marca; el castellano v2 ya lo había cambiado.
- **Cristal de la piedra de su propio mundo** → *Crystal of the Stone from His Own World* (el viejo, «The stone from his own world Crystal», estaba roto).
- Índice, objetos de `fK1` cuyo inglés viejo ya no casaba con el castellano v2 (los demás nombres de `fK1`, tal cual en `frag_bazar_a/b.en.html`):
  - **El inhalador de combate** → *The combat inhaler* (el viejo: «Jet (drug)», nombre de marca).
  - **Ordenador de pulsera (ordenador de muñeca)** → *Wrist computer* (como en `fK1_bazar_a.en.html`).
- Apóstrofos rectos en los nombres (Thief's Dagger, Shaman's Amulet, Dead Man's Hand), como `fK1.en`.

## Pasajes dudosos / pequeñas decisiones
- `<span class="src">Escrito a petición del autor (T124)</span>`: se deja en castellano, como manda el encargo; `assemble_v2.py` reduce esas marcas a su código (T124).
- `<span class="flag ed">Nota de trabajo</span>` → «Working note»; el texto del `flag pending` del resumen se ha traducido (es prosa, no código).
- La Filtración: el castellano dice «se vuelve público Lo que dijiste…» (falta el punto); en inglés lleva punto: «becomes public. What you said…».
- «sesión 0» → «session zero» (la única fila donde un número pasa a palabra).
- Ojos Saltones conserva «a pretty girl» como el castellano.

## Comprobación de estructura (script)
- Mismo número de etiquetas de cada tipo, mismos `id`, `href`, `class`, mismas marcas `src` y banderas `flag`, en ambos archivos.
- HTML equilibrado; `fK3.en` cierra `</section>` igual que el castellano.
- Filas: fK2 178/178; fK3 392/392. Celdas numéricas idénticas (495 y 386). Ningún número cambiado (salvo «sesión 0» → «session zero»).
- Índice: 372 filas, todas con el nombre exacto de su fila del catálogo inglés (fK2: los de `fK2_bazar_b.en.html`; fK1: los de `frag_bazar_a/b.en.html` más los dos cambios de arriba). Sin restos de castellano en el índice.

## Alineado con fK1
Hecho, fila a fila, con `fK1_bazar_a.en.html` ya terminado: las filas `<strong>` de fK1.en (de la 20.ª en adelante; las 19 primeras son ejemplos de la ficha técnica) contra fK1 en castellano, y de ahí al índice. Las 372 filas del índice nombran exactamente una fila del catálogo inglés (fK1.en + fK2.en). Si fK1.en vuelve a cambiar algún nombre, hay que repetir la comparación.
