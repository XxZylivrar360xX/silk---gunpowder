# EPUB build

Generador local para los EPUB de la saga *Seda y Polvora*; por defecto, el Libro I, *Mascaras de Cristal*.

```powershell
python .\tools\epub-build\build_epub.py
```

Salida esperada:

- `tools/epub-build/output/Mascaras_De_Cristal.epub` (desde 2026-09-27; `Seda_y_Polvora.epub` es la salida anterior al cambio de título y se retira al regenerar)

Requiere `pandoc` disponible en PATH.

## Sombras de Poder — Libro II

Para regenerar EPUB y PDF juntos, desde la raíz del vault:

```powershell
python -B .\tools\build_sombras.py
```

El lanzador reutiliza ambos generadores con la portada de *Sombras de Poder*, autor Víctor Paz, colección *Seda y Pólvora*, posición 2 e identificador EPUB fijo y distinto del Libro I. Selecciona únicamente `Part_01_Nieve_Y_Ceniza/01_Hogar.md`: el título visible y el índice dicen **Hogar**, tomado del manuscrito. El PDF conserva la presentación de **Borrador de lectura**.

Salidas:

- `tools/epub-build/output/Sombras_De_Poder.epub`
- `output/pdf/Sombras_De_Poder.pdf`

Para generar sólo el EPUB: `python -B .\tools\build_sombras.py --format epub`. Para generar sólo el PDF: `--format pdf`; acepta `--paper letter` y `--year 2026`.

La lista `CHAPTERS` de `tools/build_sombras.py` controla la copia de lectura. Añadir ahí las rutas, relativas a `11_Books/Book_02_Sombras_De_Poder`, de los siguientes capítulos cuando el autor los incorpore. El orden sigue las carpetas y nombres de archivo. `Ya_Llego.md` queda fuera de esta selección: conserva notas internas y no forma parte de esta entrega.

Ambos generadores aceptan `--chapter` repetible para seleccionar archivos de `Part_*`; una ruta inexistente, ajena al libro o duplicada detiene la exportación. Sin esa opción, conservan la recolección habitual del libro completo. `--identifier` permite distinguir cada libro y debe mantenerse fijo entre regeneraciones. Para *Sombras de Poder*, usar el lanzador evita heredar los valores predeterminados del Libro I.

Notas:

- Cuando ya hay capitulos en `Part_*`, la nota editorial de `00_Front_Matter` se omite por defecto para que el EPUB lea como novela.
- Usa `--include-front-matter` si necesitas incluir esa nota de montaje.

- Los capítulos se exportan sólo con su título, sin «Capítulo» ni número, también en el índice. Las partes se exportan en dos líneas («Primera parte» en versalitas y el título en cursiva, con mayúscula sólo inicial), centradas en su página; los títulos legibles viven en `PART_TITLES` de `build_epub.py`. Sólo se incluyen partes con capítulos escritos del libro seleccionado.
- Se eliminan el frontmatter YAML y los comentarios HTML de los archivos fuente. Si quedan marcas editoriales (`BORRADOR`, `PENDIENTE`, `DISEÑO`, `POV:`, etc.) o comentarios sin cerrar, la exportación se detiene para revisarlos; no se borra prosa silenciosamente. Se conservan las citas narrativas, como cartas y mensajes, y los metadatos bibliográficos del EPUB (título, autor e idioma).
- Cualquier `.md` dentro de `Part_*` (o `00_Front_Matter`) que contenga la directiva literal `EPUB: EXCLUDE` en cualquier parte del archivo (típicamente en el comentario HTML inicial) se conserva en el vault pero no se incorpora al EPUB: no aporta contenido, no genera heading, no pasa a Pandoc. El build imprime `- excluded from EPUB: <ruta>` por cada archivo así excluido. Sirve para redirects/stubs (p. ej. capítulos fusionados que se conservan solo para no romper enlaces) y notas internas que deban permanecer junto al manuscrito sin exportarse.

Presentación de libro final (2026-09-27):

- Metadatos: «Máscaras de Cristal», «Víctor Paz», sin subtítulo, colección «Seda y Pólvora» (posición 1), `rights` y un identificador UUID **fijo** (`BOOK_IDENTIFIER`) para que los lectores conserven marcadores entre versiones. `--series`/`--series-position` fijan la colección de la saga.
- Página de créditos (© y aviso de ficción) generada por `build_credits_page`, fuera del índice. Índice titulado «Índice».
- Las comillas rectas `"…"` del manuscrito se exportan como latinas «…»; las anidadas se escriben “…” en la fuente.
- Tras Pandoc, `polish_epub` sustituye los `<title>` genéricos (`ch001.xhtml`) por el título del capítulo.
- CSS: sólo sangría (sin espacio entre párrafos), primer párrafo sin sangría y primera línea en versalitas, cortes de escena con ⁂, cartas en `blockquote` con margen lateral.
- Pendiente fuera del script: portada a ≥1600×2560 y validar con EPUBCheck / Kindle Previewer (no instalados en esta máquina).
