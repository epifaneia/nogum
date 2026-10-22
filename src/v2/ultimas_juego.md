# Últimas decisiones aplicadas al Juego completo (B, D, E, F, G, H, J, K, L, M)

Fuente: `DECISIONES-ultimas.md`. Cada cambio va en castellano y en su `.en.html`, con la misma estructura, salvo K y L, que solo tocan el castellano (en inglés ya es «Sphere» y los nombres se quedan en mayúscula de título). No se han tocado `src/frag_acelerado*`, `src/p_tesis_*` ni la App.

## B. La escalera llana abarata también la Rejilla (9.1, `fJ1`)
- En el recuadro de la regla, tras «1, 4, 7, 10, 13»: con ella baja también la Rejilla, para que siga siendo la compra más barata del Ámbito entero (5/8 de cubrirlo con Llaves): **5·(3n−2)**, es decir 5, 20, 35, 50, 65, en vez de 5·n².
- En la tabla, dos columnas nuevas: «Rejilla, cuadrada (5·n²)», 5 · 20 · 45 · 80 · 125, y «Rejilla, llana (5·(3n−2))», 5 · 20 · 35 · 50 · 65. En inglés, «Grid, square» y «Grid, flat».
- No se ha tocado la Transformación, que cita 5·n² para la regla por defecto.

## D. Firmas que estaban en otra Disciplina (catálogo de 9.2, `fJ1`)
Se han movido siete. Cada una va al final de su nueva Disciplina, y la fila inglesa se mueve igual:

| Firma | Estaba en | Pasa a | Por qué |
|---|---|---|---|
| Esquiva refleja | Atletismo | Acrobacia | Acrobacia cubre la esquiva activa (6.2) |
| Ganzúa / cerrajería física | Juego de manos | Seguridad | Seguridad cubre las cerraduras (y su ejemplo es «Abrir cerraduras») |
| Bloqueo y absorción | Pelea | Entereza | Se absorbe con Entereza (6.2) |
| Lectura corporal | Alerta | Empatía | Empatía es leer intenciones; ya estaba «Lectura de intenciones» |
| Primeros auxilios de campo | Supervivencia | Biotecnia | Biotecnia es curar de verdad, primeros auxilios incluidos |
| Duplicación ficticia / ilusión | Proyección | Alteración | Alteración cubre las ilusiones |
| Proyección astral / psíquica | Proyección | Adivinación | Es sentido sobrenatural (explorar o comunicarse), no lanzar energía |

- Ahora no todas las Disciplinas tienen cinco: Atletismo, Juego de manos, Pelea, Alerta y Supervivencia tienen 4; Proyección, 3; Acrobacia, Seguridad, Entereza, Empatía, Biotecnia, Alteración y Adivinación, 6. El total sigue siendo 200. La entradilla pasa de «Cinco Firmas por Disciplina» a «Unas cinco Firmas por Disciplina» («About five…»).
- Ninguna de las siete se cita fuera del catálogo: no había nada más que cambiar.
- Dudosas que se quedan como estaban: Desarme rápido (Juego de manos, podría ser Pelea), Interrogatorio técnico (Investigación; Intimidación también interroga, pero esta va por la lógica), Telequinesis fina (Alteración) y Control de cámaras (Seguridad o Sistemas). «Etiqueta cortesana» sigue en la fila «Sin asignar» de los ejemplos, con su nota «Encajaría en Persuasión».

## E. «Hackear una IA», de Mental a Técnico (tabla de 4.4, `fE`)
- Técnico: «Para que un humano de nivel 1 hackee una IA de nivel 3: una contraseña de administrador robada, un mes de preparación ininterrumpida o un portátil conectado al mainframe. También un laboratorio profesional, o los recursos de una megacorporación.»
- La fila Mental se quedaba vacía, y lleva un ejemplo nuevo: «Para que un detective de nivel 1 desmonte el plan de un genio criminal de nivel 3: el cuaderno donde lo dejó escrito, o el testigo que lo vio todo.»

## F. Fuera la fila +0 de Recursos (5.6, `fF`)
- Se borra la fila +0 («Un sueldo, o un grupo que te cubre»). El título pasa a «los cinco cajones de Recursos» («the five drawers»). Nadie más citaba los «seis cajones» ni «Recursos +0».

## G. Las tarjetas de 1.4 sin el porcentaje con bono 0 (`fA`)
- Las siete tarjetas pierden el par «Sale adelante (bono 0)» / «Works out (bonus 0)». Se quedan las bandas con sus porcentajes y el resto. La hoja de referencia ya no lo llevaba.

## H. «Que la historia lo permita» (el segundo cerrojo)
- 5.6, los tres cerrojos (`fF`): «**Que la historia lo permita**: que tenga sentido que esté en tus manos aquí y ahora.» / «**The story allows it**: …».
- Glosario, «Cerrojos del equipo» (`fH`): «el Acceso, que la historia lo permita y su coste…» / «Access, that the story allows it, and its cost…».
- Receta del ciberpunk sombrío, 9.4 (`fJ2`): «(Acceso, que la historia lo permita y su precio…)» / «(Access, that the story allows it, and its price…)».
- Daño ambiental, 9.1 (`fJ1`): la protección «funcionaba como permiso narrativo». No es una Llave, así que ahora dice «es lo que te salva: con ella, el daño se puede absorber o desaparece» / «is what saves you: with it…».
- Se quedan como están, porque ahí es la Llave: La Idea de 0 (`fA`, la piedra verde), Vínculos («La amistad es el permiso narrativo») y la receta de los niños en bici (`fJ2`).
- La FAQ, la hoja de referencia y el taller del Bazar no nombraban el cerrojo: no había nada que cambiar.

## J. El Baúl: coste de atención y cuándo estorba (9.1, `fJ1`)
- La tabla de módulos tiene dos columnas nuevas, «Coste de atención» y «Cuándo estorba» («Attention cost», «When it gets in the way»), antes de la columna editorial «Estado». Las 17 filas están rellenas con lo que dice cada módulo. Cuenta: 9 «Poco», 7 «Algo», 1 «Mucho» (las Fundas).
- La frase de antes de la tabla pasa a «Cada módulo dice qué hace, en qué recetas del 9.4 aparece, cuánta atención le pide a la mesa y cuándo estorba.»
- Las más interpretativas, por si el autor quiere retocarlas: Pacto del diablo (en la Épica estorba, porque solo añade el precio), Daño explosivo (con la Letal, una cadena de críticos acaba la pelea), Transformación (si la mesa apenas pelea) y Sincronización (un mecha de una sola escena).

## K. «Ámbito» con mayúscula (todo el castellano)
- Se han revisado las 94 apariciones de «ámbito/ámbitos» en minúscula: todas eran el término del juego («el Ámbito Arcano», «todo el Ámbito», «Ámbito a Ámbito», «en ese Ámbito», «5 Ámbitos», el título «3.4 Por Ámbitos», el caption de 4.4…), así que todas van con mayúscula. Ninguna era la palabra corriente. Por ficheros: fC 14, fD 27, fE 10, fF 10, fG 3, fI 3, fJ1 10 (contando la frase nueva de B), fJ2 7, fK1 5, fK2 3, fL 3. El glosario y los apéndices ya lo tenían.
- El inglés no se ha tocado: aún tiene unas 90 «sphere» en minúscula frente a 58 «Sphere». Si se quiere el mismo criterio que en castellano, eso va aparte.

## L. Mayúscula solo en la primera palabra (castellano)
- Se ha hecho por script: el `sc.py` y el `apply.py` del scratchpad de esta sesión. Las tablas de las 200 Firmas (9.2) y todos los objetos del Bazar (`fK1`, `fK2`) se pasan a mayúscula solo inicial, y el índice de `fK3` y las menciones en otros capítulos se cambian con la misma tabla (539 formas). Ejemplos: «Daga de ladrón», «Espada larga (bastarda)», «Hurto sutil (pickpocket)», «Ganzúa / cerrajería física». También va en minúscula lo que va detrás de una barra o entre paréntesis.
- Excepciones, revisadas a mano (se quedan con mayúscula):
  - Siglas: CCTVs, EMP, EOD, IAs, SMG, V8, VIP, VTOL.
  - Nombres propios y marcas: Magnum, Kevlar, Molotov, Geiger, Winchester, Tesla, Bowie, «Ciencias de la Tierra» (el planeta).
  - Nombres de algo concreto: el Corta-Dioses, el «Gordo», el «Pacificador», el «Socorro» del cartel, la Orden y los Caídos (la capa), y el Flujo (los cuatro poderes de la Ópera de Estrellas, como «el Flujo» del Arcano).
  - Los nombres de las ambientaciones (La Ciudad de Neón, El Oeste Extraño…) no se tocan.
- Correcciones a mano después del script: «Mantenimiento del orden» (aquí no es la Orden), «La orden de mando (voz de alfa)» y «Ciber-diagnóstico».
- Menciones fuera del catálogo que se han cambiado: «Presencia majestuosa» (4.4 en `fE` y FAQ en `fH`), «Sable de energía» y «Rifle de plasma» (nota de `fK1`), «Martillo digno», «La pintura de túnel», «Escopeta de dos cañones», «Sangre ácida», «Caminar por el aire» y «Caminar en el aire» (notas de fusión en `fK1`, `fK2` y `fK3`).
- Los ejemplos de Firmas en prosa (2.4, 7.2, los expedientes del 9.4) y la tabla de ejemplos de 9.2 ya iban en mayúscula inicial: no había nada que cambiar.
- Ahora hay dos objetos que se llaman igual, «Placas completas»: el de la mazmorra y el de las piezas sueltas. Antes los separaba la mayúscula. Son dos objetos distintos y el índice los distingue por «De dónde».
- **Comprobación del índice**: cada una de las 372 filas del índice existe tal cual en el catálogo y en la ambientación que dice su columna «De dónde» (se comprueba el par nombre + sección). Todos los objetos del catálogo están en el índice.

## M. Datos y ejemplos
- La Angustia, en la tarjeta de 1.4 (`fA`) y en el Apéndice B (`fB`): «Con la Pesadilla, que es la misma lectura, son las dos tarjetas donde más pesa la ficha, del 9 % al 81 %…».
- La Realista y el +4 (2.5, «Lo que pesa cada bono», `fC`): «el +4 pesa casi lo mismo» pasa a «el 85 %: cinco puntos menos que con un dado, aunque la escala sea el doble de larga, porque la campana concentra los resultados en el centro y cuatro puntos de bono mueven mucha probabilidad». Son las cifras del Apéndice B: 85 % con la suma frente a 90 % con un dado.
- El parkour, en 2.4 (`fC`): «que vale para cruzar la ciudad por los tejados, no para caminar por la cuerda floja del circo». Las dos cosas son Acrobacia, que es lo que ilustra la Firma. En 9.2 (`fJ1`): «Vale para cruzar la ciudad a la carrera y por los tejados; en la cuerda floja del circo sigues tirando con el +2 de Acrobacia».
- «Pura Erudición… leer una calle» (2.2, `fC`) pasa a «te toca seguir un rastro por el monte». Leer la calle es Actualidad, que también es Erudición; el rastro es Supervivencia, el otro Dominio (Ingenio).

## Comprobaciones (por script)
- HTML equilibrado en cada fragmento. `fK1` abre la `section` del Bazar y `fK3` la cierra, como antes.
- El castellano y el inglés tienen el mismo número de etiquetas de cada tipo, los mismos ids y los mismos href, fichero a fichero. Los href del glosario van en otro orden porque el glosario está ordenado alfabéticamente en cada idioma; ya era así.
- No hay ids repetidos. El único enlace sin destino es `#acelerado`, que lo resuelve el montaje.
- La hoja de referencia (`fL`) solo cambia en tres «Ámbito»: no crece.
