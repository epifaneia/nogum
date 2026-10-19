# NOGUM

**Compilador de un manual bilingüe de 150 páginas, con validación automática de contenido, y la aplicación web que lo configura.**

El producto es un juego de rol universal. Lo interesante desde aquí es el problema: mantener **cuatro productos derivados de una misma fuente, en dos idiomas, con datos compartidos entre un libro y una aplicación**, sin que se desincronicen. Este repositorio es el pipeline que lo resuelve y las puertas de validación que lo vigilan.

🔗 **[Leerlo publicado](https://epifaneia.dev/nogum/)**

> **Por qué está aquí.** El principio de [Epifaneia](https://epifaneia.dev) es que *el modelo interpreta y el código determinista verifica*. Esto es ese principio llevado al extremo en un dominio donde la especificación era mía de arriba abajo: 150 páginas, dos idiomas, cuatro salidas y una aplicación que consume datos del propio libro.
>
> Las tres cosas que se demuestran son las mismas que se piden en un proceso regulado. **Trazabilidad:** cada regla lleva escrito de dónde sale, y el diario de diseño son 154 decisiones con su porqué. **Verificación automática:** las puertas paran la compilación cuando el contenido y los datos dejan de decir lo mismo. **Y restricción deliberada del modelo:** el configurador es determinista porque un árbol de veinte preguntas resuelve eso mejor que un modelo, y al asistente se le recorta el contexto para que nunca lea el diario de trabajo.
>
> El problema de fondo es el mismo que ataca [CTSM](https://github.com/epifaneia/ctsm) entre un requisito de cliente y un documento de proveedor: dos textos que debían decir lo mismo y dejaron de decirlo, sin que nadie se enterara. Aquí la diferencia es que el corpus es grande, vivo y bilingüe, y que las puertas llevan meses funcionando.

---

## El problema

Una misma fuente alimenta cuatro salidas que se contradicen con facilidad:

| Pieza | Qué es | Formato |
|---|---|---|
| La Idea | el argumento de diseño, 13 páginas | libro |
| Juego completo | el manual, ~150 páginas | libro |
| Acelerado | la versión corta, 16 páginas | libro |
| App | el configurador y las fichas | aplicación de un fichero |

Los tres libros se montan desde los mismos fragmentos. La aplicación consume **datos extraídos de esos fragmentos** (catálogo de equipo, reglas opcionales, recetas de mundo). Y todo existe en castellano y en inglés.

Las formas de romperlo son muchas y silenciosas: renombrar un concepto en el manual y no en los datos de la app; corregir una cifra en un idioma y no en el otro; expulsar un elemento de una lista y dejar seis referencias apuntando al de al lado.

## Cómo se resuelve

### Compilación

```
src/assemble3.py          los tres libros, dos idiomas, tres destinos
src/build_app3.py         la aplicación
src/extract_app_data.py   extrae datos del manual hacia la aplicación
src/make_covers.py        portadas
src/pdf_idea.py           La Idea en PDF, compuesta a mano
```

Tres destinos con enlaces distintos —carpeta local, artefactos, sitio público— resueltos en compilación, no a mano.

### Puertas de validación

Nada se publica sin pasar por aquí:

- **`src/w_revision.py`** — barre los productos compilados buscando vocabulario retirado, comprueba invariantes del sistema y revisa anclas rotas, identificadores duplicados y enlaces entre piezas.
- **`src/w_marcas_inv.py`** — inventario de marcas y nombres con derechos sobre lo publicado, con su contexto.
- **Aserciones en compilación** — que el número de recetas cuadre con el de tablas de techos; que el catálogo de reglas opcionales siga siendo de 16, porque el código de partida usa 16 bits; que los veinte mundos del atajo apunten a las veinte recetas una vez cada uno; que el documento JSON embebido en la aplicación siga siendo válido.
- **`src/pdf_idea.py`** — el PDF se pagina a mano (una lista de cortes con las palabras exactas de cada uno), y por eso pasa por su propia puerta, medida en el mismo Chrome que imprime: nada se desborda de su caja, todo párrafo empieza en la rejilla de 15 pt, ningún titular se queda al pie, un párrafo partido deja dos líneas a cada lado, las dos páginas de cada pliego acaban a la misma altura, lo del margen se ve de verdad y el total es múltiplo de 4 para imprimirlo como cuadernillo.
- **`src/curvas.py`** — el modelo de probabilidad del sistema, contrastado contra las tablas impresas del propio manual: 42 filas comparadas, 0 discrepancias. De ahí salen también las gráficas SVG del libro, generadas desde los datos y no dibujadas a mano.

Tres ejemplos de fallos que estas puertas encontraron y que ninguna lectura humana había visto: un catálogo que repartía un valor de daño retirado **solo en la versión inglesa**; texto que la aplicación arrastraba con vocabulario que el manual ya había cambiado; y dos rutas de salida que en Windows eran el mismo fichero, de modo que los enlaces publicados apuntaban a copias locales inexistentes.

## La aplicación

Un fichero HTML autónomo, sin dependencias ni servidor.

- **Configurador determinista**: monta la partida con preguntas sobre situaciones, no sobre reglas, y a partir de ahí acota el catálogo —que son cientos de elementos— a lo que ese mundo concreto usa.
- **Estado comprimido**: la configuración entera viaja en una cadena corta.
- **IndexedDB** para los ficheros de audio que el usuario aporta, con validación de que el fichero decodifica antes de guardarlo.
- **Modelo de lenguaje** para consultas de reglas, con el contexto curado: el documento de canon se corta por un marcador para que el asistente nunca lea el diario de trabajo.

Sobre esto último: el configurador es determinista **a propósito**. Un árbol de veinte preguntas resuelve mejor ese problema que un modelo, y el modelo se usa donde sí aporta.

## Estructura

```
docs/      el sitio publicado (GitHub Pages)
src/       fuentes, datos y pipeline
  frag_*.html      fragmentos del manual (es / en)
  pdf/             hoja de estilos e imagen de cubierta del PDF
  app4_body.html   la aplicación
  *.json           datos extraídos
  CANON.md         el diario de diseño: 154 decisiones con su porqué
  archivo/         scripts de un solo uso, por historial
LICENSE
```

## Compilar

```bash
cd src
python extract_app_data.py   # datos del manual -> aplicación
python assemble3.py          # los tres libros, tres destinos
python build_app3.py         # la aplicación
python pdf_idea.py           # La Idea en PDF (necesita Chrome y red para las fuentes)
python w_revision.py         # la puerta de validación
```

Sin dependencias: biblioteca estándar de Python 3. El PDF usa además Chrome o Edge en modo headless, que mide e imprime.

## Licencia

Contenido bajo [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Las mecánicas de juego no son objeto de derechos de autor: puedes escribir material compatible sin pedir permiso. El nombre NOGUM queda fuera de la licencia. Ver [LICENSE](LICENSE).
