# EPUB build

Generador local para los EPUB de la saga *Seda y Polvora*; por defecto, el Libro I, *Mascaras de Cristal*.

```powershell
python .\tools\epub-build\build_epub.py
```

Salida esperada:

- `tools/epub-build/output/Mascaras_De_Cristal.epub` (desde 2026-09-27; `Seda_y_Polvora.epub` es la salida anterior al cambio de título y se retira al regenerar)

Requiere `pandoc` disponible en PATH.

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
