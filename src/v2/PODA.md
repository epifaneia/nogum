# NOGUM v2 · La poda (quitar repetición)

Crítica de lectura que el autor hace suya: «hay mucha repetición». El núcleo (introducción a glosario, sin el cap. 9 ni los apéndices) ha pasado de ~27.000 palabras a ~55.000, y buena parte es el mismo caso contado varias veces. Objetivo: **~38.000 palabras en el núcleo**, sin perder ninguna regla ni ningún ejemplo único.

Sigue valiendo todo `MAPA.md` (voz, marcado, ids, sin absolutos, no inventar reglas) y `DECISIONES-22oct.md`. El canon (CANON.md 1–~290) manda.

## La regla

**Cada caso, cada regla y cada remate se cuenta una vez, en su casa.** En los demás sitios, como mucho una frase y un enlace (`<a href="#id">N.M</a>`). Si un párrafo solo repite lo que ya está en su casa, se borra. Si tiene algo único, ese algo se queda (o se mueve a su casa si te toca ese fichero).

Remates que suenan a disculpa a la décima: «es un consejo, no una regla», «se pacta en la sesión 0», «lo frena la mesa», «la mesa es adulta». Se dicen **donde nacen** (sesión 0 y la mesa: cap. 0; cada consejo: en su sitio, una vez) y en los demás, nada o un enlace.

## Dónde vive cada caso (su casa)

| Caso | Casa | Ahora aparece también en |
|---|---|---|
| «Armas contra los vampiros» / Llave Limitada de un nivel (consejo de optimización) | 4.3 `ch4-escalera` | 4.9, 5.4, 5.9 (×3), 7.6, FAQ (×2) |
| El rockero / la estrella del rock | 3.4 `ch3-ambitos` (con su cifra, sujeta a la mesa); la casilla de la Tabla 2 (4.8) se queda tal cual, es tabla aprobada | 3.2, 3.3 (texto fuera de la tabla), 3.9, FAQ |
| Exoesqueleto / sincronización y su precio | 3.8 `ch3-sincro` (la regla); su precio, una línea en 5.6 | 5.6 (×2), 5.9, FAQ (×2) |
| El robot de la misión / regalos del Director | 5.7 `ch5-devolver` | 5.6, FAQ |
| El bazuca (Llave Limitada al daño) | 4.5 `ch4-parca` | 4.4, 4.9 (×2), 5.6 (×2), 5.9 (×2), 6.3, FAQ (×3) |
| El hombre lobo / la Transformación | 9.1 `ch9-transformacion` (ya escrita); como mucho un caso en 4.9 | 3.3, 5.9 (×2), 6.3, FAQ (×3) |
| La granada (anula lo que dice que anula) | 4.2 `ch4-anula`; «lo de un solo uso no se paga», una línea en 5.4 | 3.2, 3.4, 3.9, 4.5, 4.9 (×4), 5.4, 5.6, 5.9 (×4), 6.2, 6.3 (×7), 6.6, 6.7 (×5), FAQ (×7) |
| La pistola, el bláster, la katana monofilo, «una Llave por rasgo», Parca + Abs: Nula, munición infinita y demás casos de armas | **El taller del Bazar** (`bz-fabrica` / `bz-precios`, en `fK1_bazar_a.html`). El principio vive en 4.2 (anula lo que dice) y las etiquetas en 6.3; en 5.4, una línea por regla, sin casos | 4.2, 5.4, 5.6 (×7), 5.9 (×3), 6.3, 6.7, FAQ |
| Los casos A y B (fichas de salida) | **7.2**, junto a Inés (son fichas de ejemplo, no precios) | 5.2 |
| El dron (ejemplo de la cuenta) | 5.4, una vez y corto | 4.6, 4.8, 5.1, 5.5 |
| La invisibilidad (ejemplo de permiso y Ajuste) | 4.6 `ch4-permisos` (el permiso); 5.5, una línea para el Ajuste | 4.7, 5.4, 0.8, 8.4 |
| El cañón de riel | Bazar | 5.1, 5.6 (×2), 5.7, FAQ |
| La muerte | 0.7 | — |
| La sesión 0 / la mesa manda / el combo barato | cap. 0 (0.4 el combo y la Llave en blanco) | por todas partes |

## Capítulo 5: en los huesos

El capítulo 5 tiene 11.000 palabras y el libro presume de que la cuenta cabe en una servilleta. Que lo demuestre: **la cuenta entera en unas dos páginas** (5.4: los pasos, una línea por regla; 5.5: el Ajuste, corto). Los casos de armas se van al taller del Bazar; los casos A y B, a 7.2. 5.1–5.3 y 5.6–5.8 se quedan con su regla y un ejemplo cada uno, no tres. 5.9 Aclaraciones: solo lo que delimita y no está ya en el cuerpo. **Objetivo: ≤ 4.500 palabras.**

## Preguntas frecuentes: un índice

`apx-faq` pasa a ser **un índice de preguntas de una línea, cada una con su enlace** al sitio que la contesta (la aclaración o el apartado), agrupadas como ahora. Sin repetir la respuesta. Si una respuesta de la FAQ no está en ningún otro sitio, se deja con una frase de respuesta como mucho. Objetivo: ~1.000 palabras.

## Lo nuevo

- **Un ejemplo de juego** al final del cap. 6, antes de las aclaraciones: «6.7 Una escena, de principio a fin» (`ch6-ejemplo`; las aclaraciones pasan a 6.8 con su mismo id `ch6-aclaraciones`). Media página: una escena contada con sus tiradas (tarjeta de tono, dados, TN, resultado), en la que aparezcan **un salto de Rejilla** (el de abajo no tiene tirada; el de arriba tira Estilo para ver cómo, o se narra) **y una Llave** (alguien de abajo que sí puede tocar al de arriba porque tiene la Llave que cubre eso). Enlaces a las reglas que se usan.
- **3.1**: una línea con lo que sí puede hacer quien está debajo sin Llave: huir, buscar la Llave, cambiar de plan.
- **2.1**: la fila «+3 · —» sale de la tabla; debajo, una frase: el +3 no sale de la ficha; si los bonos llegan a +3 al aplicarse, no se dice cómo.

## Tu registro

Al acabar, escribe `src/v2/poda_<letra>.md`: palabras antes y después de cada fichero, qué has quitado (caso → dónde se queda), qué has movido, y dudas. Comprueba que todos tus enlaces existen en `src/v2/f*.html` y que el HTML está equilibrado.
