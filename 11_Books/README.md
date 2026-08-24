# 11_Books

Carpeta de montaje de libro y salida editorial para *Seda y Polvora*.

Cada libro debe tener su propia carpeta, un `00_Book_Map.md` y carpetas de partes en orden de lectura. La prosa final vive en esas partes, no en la biblia del vault.

## Libro activo

- `Book_01_Seda_y_Polvora/` - novela principal, en montaje inicial.

## Flujo EPUB

El generador esta en `tools/epub-build/build_epub.py`. Mientras no existan capitulos de prosa, el EPUB se arma con `00_Front_Matter/00_Nota_Editorial.md` como maqueta de lectura. Cuando ya hay capitulos en las partes, el script omite la nota editorial por defecto e incluye solo prosa, por orden de carpeta y nombre de archivo. Para incluir la nota de montaje manualmente, usar `--include-front-matter`.
