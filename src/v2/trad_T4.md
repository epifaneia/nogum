# trad_T4 · Capítulos 6, 7 y 8

Salida:
- `src/v2/fI_cap6_cap8.en.html` (secciones `ch6` y `ch8`, como el original)
- `src/v2/fG_cap7.en.html`

Reaprovechado: `frag_ch5.en.html` (peligro, viejo cap. 5), `frag_ch67.en.html` (fichas y consola, viejos 6 y 7), `frag_ch3.en.html` (casos A y B, nombres de habilidades), `frag_ch4.en.html` (resultados del Estilo) y el expediente de Inés de `frag_cap8.en.html` (concepto, Firma «Being invited in», Thirst/Humanity, «She has not grown»). Lo reaprovechado se corrigió donde el castellano v2 cambia: la pifia del defensor (ahora +1 al daño), la esquiva solo si el ataque conecta, la penalización de barras que se suma, las Llaves de Inés sin objetivo, cuatro fichas en lugar de tres, etc. Se quitaron los pasajes viejos que v2 ya no tiene (doble pifia, fórmula de daño, ED-17, ED-12, «Unvalidated proposal» de la tabla de la consola).

## Ejemplo 6.7 (nuevo)

Las tiradas dicen lo mismo, cifra a cifra: Realista, 2d10 sumados, TN 11, pifia 2–3, crítico 19–20. Inés, Estilo: «6 and 5, eleven, plus two, 13» → éxito, «you look magnificent» (el nombre del resultado de éxito del Estilo en `frag_ch4.en.html`). Tomás: «8 and 4, twelve, plus two, 14». El Margrave: «4 and 3, seven». Daño completo: una casilla.

## Términos elegidos (no estaban en la tabla)

| Castellano | English | Nota |
|---|---|---|
| Esq/Abs: Total · Parcial · Difícil · Fácil · Nula · Máx N | Full · Partial · Hard · Easy · None · Max N | del inglés viejo |
| Daño X, Daño Mental N (etiqueta) | Damage X, Mental Damage N | la tabla de términos dice Damage; el viejo usaba «Dmg» |
| ficha técnica | spec sheet | del inglés viejo |
| salto de poder | power gap | del inglés viejo |
| se narra la derrota | the defeat is narrated | |
| a la par | level / on a par | |
| Cuerpo / Mente / Espíritu (de qué barra cuelga) | Body / Mind / Spirit | del inglés viejo |
| Herida moderada / grave | Moderate wound / Severe wound | el viejo mezclaba «Grave» y «Severe»; unificado en Severe |
| Sed / Humanidad (barras de Inés) | Thirst / Humanity | del expediente viejo |
| el Margrave | the Margrave | |
| urgencias | A&E | británico |
| un coche a ciento veinte | a car at seventy | en millas, como el viejo |
| Especialidad (guardia) | Speciality | la tabla de términos manda sobre el viejo «Specialty» |
| la lectura narrativa de la Rejilla | the narrative reading of the Grid | |
| cartulina | index card | |
| Descartado (bandera `flag drop`) | Dropped | es texto visible, no código; así lo hacía el inglés viejo. Las banderas ED-n se quedan |

## Pasajes dudosos

- 6.1, «Y como el rol es improvisación fluida, no se frena el juego eligiendo la acción de antemano. La intención, sí.» → «…the game is not held up by choosing the action in advance. The intention is chosen.» El «sí» en inglés suelto no se entiende.
- 7.2, paso 3: «la Firma +4, que es la compra de dos» → «the Signature +4, which costs two» (cuesta dos puntos: 1 + 1 + 2 = 4).
- 6.8, «¿me libro siempre?» → «do I always get away with it?» Es la pregunta del lector, no texto de reglas; por eso deja el «always».
- Las marcas `<span class="src">` van en castellano, sin traducir («Decisión del autor», «Texto del autor sobre combate», «Borrador, T35»…), como manda el encargo. El inglés viejo sí las había traducido.

## Comprobación de estructura (script)

Para los dos pares es/en: mismo número de etiquetas de cada tipo, mismas clases (también `tag`, `tag parca`, `flag ed`, `flag drop`, `src`), mismos rowspan/colspan, mismos ids en el mismo orden, mismos href en el mismo orden, mismo texto en todas las `src`, y HTML equilibrado. Todo bien en los dos. Un barrido de restos («Director», «Esq», «Rejilla», «Dmg», «Specialty», «track», «», palabras castellanas sueltas) fuera de las `src` no encuentra nada.
