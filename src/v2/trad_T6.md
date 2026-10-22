# trad_T6 · Capítulo 9a (Baúl, tablas de problemas, listado de competencias, 200 Firmas)

`src/v2/fJ1_cap9a.html` → `src/v2/fJ1_cap9a.en.html`

## Cómo se ha hecho

- Se extraen los bloques hoja (p, li, td, th, h2–h4) de `frag_cap8.html` y `frag_cap8.en.html`: son paralelos (1615 y 1615, mismas etiquetas en el mismo orden), así que castellano viejo → inglés viejo queda emparejado por posición.
- De los 1308 bloques de v2: **951** idénticos al castellano viejo, que se copian del inglés viejo por script; **257** solo números o vacíos; **~100** nuevos o cambiados, traducidos a mano (casi todos son el bloque viejo con las remisiones nuevas `<a href>` o con frases añadidas o quitadas).
- Al inglés reutilizado se le aplican estas correcciones de términos: Game Master / Director → **GM**; track → **bar**; `Dmg` → **Damage** en las etiquetas (la tabla de TRADUCCION.md manda sobre GLOSSARY_EN); Tone Cards → tone cards; apóstrofo recto → ’.

## Correcciones al inglés viejo (no eran solo de términos)

- Tabla de módulos: el inglés viejo tenía desfasadas cuatro celdas de estado (Relojes «Aprobado», Flashbacks «Se tiran: ver abajo», Tablas «Escritas en “Tablas de problemas”», Daño ambiental «Aprobado: el daño sube…»). Ahora están traducidas desde el castellano v2.
- Fundas: el inglés viejo decía `Spiritual Dmg 1` y el castellano dice Daño Mental 1. Corregido: **Mental Damage 1**.
- Varias `span.src` del inglés viejo traían códigos de más (T116, T127, T133). Se han restaurado las del castellano.
- «House» (copyright) → **the grumpy doctor with the cane** (el castellano v2 ya dice «el médico cascarrabias del bastón»). «El profesor de química enfermo» → **the sick chemistry teacher**.
- El h4 «Heridas graves» decía *Severe wounds* y el resto del capítulo *Grievous wounds*. Lo he igualado a **Grievous wounds**.

## Términos que he tenido que elegir

| Castellano | English |
|---|---|
| Regla opcional · Crecer a plazos | Optional rule · Growing in instalments |
| Cuadrada (n²) / Llana (3n−2), columnas | Square (n²) / Flat (3n−2) |
| Subir (cabecera) | Rise |
| Alcance en la lectura tangible | Reach in the tangible reading |
| barra propia | custom bar |
| Rejilla mística inversa | Inverse mystic Grid |
| permiso (suelto, mutaciones, hechizos) | permit (permiso narrativo sigue siendo narrative permission) |
| la divinidad se compra a plazos | godhood is bought in instalments |
| expedientes de ejemplo | sample case files |
| Las que juegan en el Pulp desenfrenado o la Comedia negra | Those played on Unleashed Pulp or Black Comedy |

## Lo que se queda sin traducir, a propósito

- Lo que va dentro de `<span class="src">` («Aprobado por el autor», «Decisión del autor», «Borrador», T…, C·22oct) va igual que en castellano, como pide el encargo. Al montar el libro, `assemble_v2.py` borra las marcas con texto.
- El comentario `<!-- Notas de trabajo… -->` (la categorización de las Firmas por eras) se queda en castellano: no es texto visible y no va al manual.

## Pasajes dudosos

- Transformación: «a voluntad es la Llave completa» → *at will it is the complete Key*. Lo he dejado en minúscula, como el castellano (que escribe «Limitada» con mayúscula y «completa» sin ella). Si el inglés quiere el nombre del Ajuste, sería *Complete*.
- Firma «Ganzúa / Cerrajería Física» → *Lockpicking*, del inglés viejo, que coincide con «Abrir cerraduras» → *Lockpicking* en la tabla de ejemplos. Si molesta la repetición: *Picks / Mechanical Locks*.
- Pilotaje → *Driving* (inglés viejo). Cubre también los vehículos marítimos; *Piloting* sería más exacto, pero lo he mantenido para no chocar con los capítulos 2 y 7.
- Uso **GM** en todo el capítulo, sin desarrollar «Game Master», porque no es la primera aparición en el libro.

## Comprobación de estructura (script)

- Mismo número de cada etiqueta, de apertura y de cierre (sin contar el comentario).
- Secuencia de etiquetas idéntica.
- ids: 7, iguales. href: 61, iguales y en el mismo orden. Atributos `class`: 692, iguales.
- `span.src`: 57, idénticas. Banderas `flag`: 26 (6 `flag ed`), iguales. Comentarios: 3, iguales.
- 18 tablas con las mismas filas y celdas. HTML equilibrado.
- No queda texto en castellano fuera de `src` y del comentario.
