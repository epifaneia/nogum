# La App y las últimas decisiones (B, C, H, K, L) · 23 oct

Compilado con `python -I src/build_app3.py` → `src/out3/nogum_app.html`, `docs/app.html`, `NOGUM_app/NOGUM_app.html` (659 KB). Sin commit. Tocados: `app4_body.html`, `app_data.json` (regenerado) y `build_app3.py`. El extractor no ha hecho falta tocarlo.

## Comprobación
- `node --check` sobre el script de los tres ficheros: se parsea.
- En el navegador (`localhost:8777/docs/app.html`), sin errores de consola: Código viejo de mundo propio (`…-G3-…-U001-EC`, se lee como nivel máximo del mundo 3); Código viejo de un mundo conocido (supers, `G4`: sale 5, el nivel máximo de sus jugadores); Código nuevo con `J4`; formulario del universo entero (amenazas, jugadores, resumen); ficha con escalera llana y Físico 3; equipo viejo de Piezas sueltas; reparto con el mundo por debajo del grupo; inglés. Al acabar, el localStorage del navegador quedó como estaba.

## B · La Rejilla con la escalera llana
- `gridCost(n) = 5 · escalera(n)`: 5·n², o 5·(3n−2) con la regla 17 encendida (5, 20, 35, 50, 65). Lo siguen el coste de la ficha, el botón «+1 Rejilla» y lo pagado por Ámbito. En el Acelerado no hay Baúl, así que no cambia.
- Textos que lo dicen según la regla esté encendida o no: la nota del bote aparte (+3 cuesta 45 o 35) y el recordatorio «Grande en todo el Ámbito». La ayuda de la regla 17 y la de Transformación lo dicen también.
- Probado: Físico 3 con la escalera llana cuesta 20, y subir uno más 15.

## C · Fuera la escala de la partida
- **Nivel máximo del mundo** (3.7): lo más alto que existe en ese universo, el tamaño de las amenazas. Va de 1 a 6 (el 6, lo cósmico: «Un planeta · ×10.000.000.000») y nunca queda por debajo del nivel máximo de los jugadores. Se guarda en el mismo `M.grid` y viaja en la misma `G` del Código, así que **un Código viejo se lee sin romper**: su escala pasa a ser el nivel máximo del mundo. Una app vieja que lea un `G6` lo deja en 5.
- **Nivel máximo de los jugadores**: en un mundo conocido, el de la receta, Ámbito por Ámbito (ya estaba). En un mundo propio, una pregunta nueva en el formulario del universo y un desplegable en la barra (`M.pmax`, uno para los cinco Ámbitos, el Arcano solo si lo hay; «Sin techo» si no se contesta). Viaja como `J1`…`J5` solo si se ha dicho, así que los Códigos de siempre no cambian y una app vieja lo ignora.
- El formulario: el sector «Las hazañas» (lo más gordo que han hecho los protagonistas…) se cambia por **«Las amenazas»** (tres preguntas sobre lo más grande que existe; con todo al máximo, sale lo cósmico), y después entra «Los jugadores» («¿hasta dónde puede llegar uno de vuestros personajes?»).
- Los mundos conocidos: `p[3]` ya no es la escala (supers 4, anime 3). Ahora es el nivel máximo del mundo donde la receta lo nombra: 11 ciber-elfos 5 (dragones 4–5), 12 horror cósmico 6 (los dioses), 13 vampiros 5, 14 niños en bici 3 (el monstruo), 19 distopía 5 (el Ordenador). En las demás manda el nivel máximo de sus jugadores.
- Se dice en el resumen de la mesa, el final del formulario, el hub, la barra, los recordatorios, el panel del Código, la lectura de la IA, «Cuéntame tu universo» (campos `grid` 1–6 y `pmax`) y el contexto del asistente.
- **El reparto**: un PNJ no pasa del nivel máximo del mundo (salvo que los personajes ya lo hayan pasado). Si el tope lo pone eso, la App lo dice y propone subirlo en la barra.
- La nota del formulario de tono decía «aplica un tono y una escala»: ahora dice «un tono y una letalidad».
- `build_app3.py` comprueba que no vuelvan «Escala de la partida», «Game scale» ni el cerrojo viejo, y que `gridCost` siga a la escalera.

## H · El segundo cerrojo
- Los tres cerrojos del equipo: «el Acceso…, **que la historia lo permita** y el coste…» / «**the story allows it**». «Permiso narrativo» no quedaba en ningún otro sitio de la interfaz.

## K · «Ámbito»
- En castellano, con mayúscula en todos los textos de la interfaz donde es el término del juego (bono −1, Arcano, bote aparte, aviso de Rejilla alta, recordatorios, Transformación…). Ya no queda ningún «ámbito» en minúscula. En inglés sigue «sphere» en minúscula, como estaba (`TRADUCCION.md` dice «Sphere»; no se ha tocado).

## L · Nombres del Bazar
- `app_data.json` regenerado con `python -I src/extract_app_data.py`. **258 nombres** cambian, y solo de mayúsculas, solo en castellano («Hoja corta», «Fuerza de sala»); el inglés no cambia. Cambian también unas notas (Ámbito/Sphere, «La pintura de túnel») y `baulLong`. Mismas secciones, bloques, número de objetos y cifras (Acceso, puntos, Llaves).
- La App guarda el equipo **por índice** (`u`, `b`, `i`), no por nombre, y no se ha corrido nada: lo he comprobado posición por posición contra el JSON anterior. Una ficha con equipo de Piezas sueltas guardada antes se carga con los nombres nuevos. El buscador ya no distingue mayúsculas. `bzv` sigue en 2.

## Dudas
- **Nivel máximo del mundo en las recetas que no dan cifra**: vikingos («los dioses que te miran mal»), Mundodisco (el hechizo de los elfos), fantasía clásica… se quedan en el nivel máximo de sus jugadores. Si el autor quiere una cifra (5 o cósmico), es un número en `KNOWN`.
- **Un solo nivel máximo de los jugadores en un mundo propio**: el manual lo da por Ámbito; la App pregunta uno y vale para los cinco (el Arcano solo si hay magia). Afinarlo por Ámbito pediría cinco preguntas o cinco desplegables.
- **El nivel máximo del mundo no limita las Llaves en la ficha**: el manual dice que se puede subir hasta él; la App solo lo usa para informar y para el tope del reparto.
- Los archivos de mesa guardados antes avisan de que «las preguntas son de otra versión», porque el formulario del universo ha cambiado. La mesa y las fichas se abren igual.
