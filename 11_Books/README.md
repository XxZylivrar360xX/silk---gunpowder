# 11_Books

Carpeta de montaje de libro y salida editorial para *Seda y Polvora*.

Cada libro debe tener su propia carpeta, un `00_Book_Map.md` y carpetas de partes en orden de lectura. La prosa final vive en esas partes, no en la biblia del vault.

## Libros del arco principal

> **SUPERSESIÓN (2026-09-22):** la saga deja de tratarse como trilogía estricta. Se inserta
> *Sombras de Poder* como Libro II, entre *Máscaras de Cristal* y *Voto de Ceniza* — ver
> [[00_Biblia/00_Trilogy_Structure]]. Todo el material del antiguo esquema de seis Partes
> internas de *Máscaras de Cristal* (Nieve y Ceniza, Exilio, Torna a Casa) se movió a
> `Book_02_Sombras_De_Poder/`. *Voto de Ceniza* y *Cuentas de Sangre* se renumeraron a Libro
> III y Libro IV.

- `Book_01_Mascaras_De_Cristal/` - Libro I, novela activa en montaje. Termina en el **Cap. 50b** (*La tierra bajo sus botas*; "Ciao, bella" es la última línea del 50), no en H1 (~~Cap. 44~~, superado 2026-10-01). Roadmap: [[01_Timeline/02_Libro_01_Mascaras_De_Cristal]].
- `Book_02_Sombras_De_Poder/` - Libro II — Sombras de Poder *(working title)*, nuevo. Absorbe las antiguas Partes IV-VI del Libro I, ahora sus propias Partes I-III (Nieve y Ceniza, Exilio, Torna a Casa). Contiene H1, el embarazo, el incendio, Villa Candelaria, Stavanger, Bonnie/Mei-Lin (F2) ~~y la llegada de Halbrook~~ (pasó al 50b del Libro I). Primer capítulo en BORRADOR: [[11_Books/Book_02_Sombras_De_Poder/Part_01_Nieve_Y_Ceniza/01_Hogar|Hogar]]. Roadmap: [[01_Timeline/03_Libro_02_Sombras_De_Poder]].
- `Book_03_Voto_De_Ceniza/` - Libro III (era Libro II). Solo `00_Book_Map.md` (esqueleto derivado de [[00_Biblia/00_Trilogy_Structure]]). Sin prosa; prosa bloqueada hasta cerrar los Libros I y II.
- `Book_04_Cuentas_De_Sangre/` - Libro IV — Cuentas de Sangre (era Libro III). Solo `00_Book_Map.md` (esqueleto). Sin prosa; prosa bloqueada hasta cerrar los Libros I-III.

Cada libro tiene su propio `00_Book_Map.md`; las carpetas de partes de los Libros III y IV se crean cuando el autor apruebe su desglose.

## Libros del ciclo de Elenna (trilogía, 2026-10-03)

- `Book_05_Juramento_De_Hierro/` - Libro V — Juramento de Hierro (era Libro IV). Solo `00_Book_Map.md` (esqueleto derivado de [[07_Ideas/Libro_04_Incubadora/07_Arquitectura_y_Temas]]). Sin prosa; el diseño vive en la incubadora ([[07_Ideas/Libro_04_Incubadora/README]]) — esa carpeta conserva su nombre histórico "Libro_04" pese a la renumeración operativa.
- `Book_06_Hijos_Del_Silencio/` - Libro VI — Hijos del Silencio (nuevo, 2026-10-03). Solo `00_Book_Map.md` (esqueleto). Caza y arresto de Ethan / Dylan Marsh. Sin prosa ni portada.
- `Book_07_Camino_A_Casa/` - Libro VII — Camino a Casa (era Libro V, luego VI). Solo `00_Book_Map.md` (esqueleto). Resolución final del caso Vera; cierra la saga. Sin prosa; prosa bloqueada hasta cerrar los Libros V y VI.

Títulos y portadas de *Juramento de Hierro* y *Camino a Casa* son CANON DEL AUTOR (2026-09-16); el título *Hijos del Silencio* es CANON DEL AUTOR (2026-10-03). La arquitectura de capítulos/partes sigue en incubadora y no está aprobada.

## Flujo EPUB

El generador esta en `tools/epub-build/build_epub.py`. Mientras no existan capitulos de prosa, el EPUB se arma con `00_Front_Matter/00_Nota_Editorial.md` como maqueta de lectura. Cuando ya hay capitulos en las partes, el script omite la nota editorial por defecto e incluye solo prosa, por orden de carpeta y nombre de archivo. Para incluir la nota de montaje manualmente, usar `--include-front-matter`.

Para *Sombras de Poder*, ejecutar `python -B .\tools\build_sombras.py` desde la raíz del vault: regenera EPUB y PDF con la selección explícita de capítulos del Libro II, inicialmente sólo **Hogar**. Configuración y salidas en [[tools/epub-build/README]] y [[tools/pdf-build/README]].
