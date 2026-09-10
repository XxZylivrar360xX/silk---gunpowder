# 11_Books

Carpeta de montaje de libro y salida editorial para *Seda y Polvora*.

Cada libro debe tener su propia carpeta, un `00_Book_Map.md` y carpetas de partes en orden de lectura. La prosa final vive en esas partes, no en la biblia del vault.

## Libros de la trilogía

- `Book_01_Seda_y_Polvora/` - Libro I, novela activa en montaje. Absorbe la vieja Parte II ("La Construcción"); termina en H1 + reveal del embarazo + coda de Halbrook. Roadmap: [[01_Timeline/02_Cadena_De_Eventos_Libro_I]].
- `Book_02_Voto_De_Ceniza/` - Libro II. Solo `00_Book_Map.md` (esqueleto derivado de [[00_Biblia/00_Trilogy_Structure]]). Sin prosa; prosa bloqueada hasta cerrar el Libro I.
- `Book_03_Interregno/` - Libro III. Solo `00_Book_Map.md` (esqueleto). Sin prosa; prosa bloqueada hasta cerrar los Libros I y II.

Cada libro tiene su propio `00_Book_Map.md`; las carpetas de partes de los Libros II y III se crean cuando el autor apruebe su desglose.

## Flujo EPUB

El generador esta en `tools/epub-build/build_epub.py`. Mientras no existan capitulos de prosa, el EPUB se arma con `00_Front_Matter/00_Nota_Editorial.md` como maqueta de lectura. Cuando ya hay capitulos en las partes, el script omite la nota editorial por defecto e incluye solo prosa, por orden de carpeta y nombre de archivo. Para incluir la nota de montaje manualmente, usar `--include-front-matter`.
