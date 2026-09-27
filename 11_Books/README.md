# 11_Books

Carpeta de montaje de libro y salida editorial para *Seda y Polvora*.

Cada libro debe tener su propia carpeta, un `00_Book_Map.md` y carpetas de partes en orden de lectura. La prosa final vive en esas partes, no en la biblia del vault.

## Libros del arco principal

> **SUPERSESIÓN (2026-09-22):** la saga deja de tratarse como trilogía estricta. Se inserta
> *Sombras de Poder* como Libro II, entre *Seda y Pólvora* y *Voto de Ceniza* — ver
> [[00_Biblia/00_Trilogy_Structure]]. Todo el material del antiguo esquema de seis Partes
> internas de *Seda y Pólvora* (Nieve y Ceniza, Exilio, Torna a Casa) se movió a
> `Book_02_Sombras_De_Poder/`. *Voto de Ceniza* y *Cuentas de Sangre* se renumeraron a Libro
> III y Libro IV.

- `Book_01_Seda_y_Polvora/` - Libro I, novela activa en montaje. Termina en el **Cap. 44** ("Ciao, bella", cierre de la Parte III — Ardizzone), no en H1. Roadmap: [[01_Timeline/02_Libro_01_Seda_y_Polvora]].
- `Book_02_Sombras_De_Poder/` - Libro II — Sombras de Poder *(working title)*, nuevo. Absorbe las antiguas Partes IV-VI del Libro I, ahora sus propias Partes I-III (Nieve y Ceniza, Exilio, Torna a Casa). Contiene H1, el embarazo, el incendio, Villa Candelaria, Stavanger, Riley/Mei-Lin (F2) y la llegada de Halbrook. Sin prosa; abre en el Cap. 45, todavía sin escribir. Roadmap: [[01_Timeline/03_Libro_02_Sombras_De_Poder]].
- `Book_03_Voto_De_Ceniza/` - Libro III (era Libro II). Solo `00_Book_Map.md` (esqueleto derivado de [[00_Biblia/00_Trilogy_Structure]]). Sin prosa; prosa bloqueada hasta cerrar los Libros I y II.
- `Book_04_Cuentas_De_Sangre/` - Libro IV — Cuentas de Sangre (era Libro III). Solo `00_Book_Map.md` (esqueleto). Sin prosa; prosa bloqueada hasta cerrar los Libros I-III.

Cada libro tiene su propio `00_Book_Map.md`; las carpetas de partes de los Libros III y IV se crean cuando el autor apruebe su desglose.

## Libros de la duología post-saga-principal

- `Book_05_Juramento_De_Hierro/` - Libro V — Juramento de Hierro (era Libro IV). Solo `00_Book_Map.md` (esqueleto derivado de [[07_Ideas/Libro_04_Incubadora/07_Arquitectura_y_Temas]]). Sin prosa; el diseño vive en la incubadora ([[07_Ideas/Libro_04_Incubadora/README]]) — esa carpeta conserva su nombre histórico "Libro_04" pese a la renumeración operativa.
- `Book_06_Camino_A_Casa/` - Libro VI — Camino a Casa (era Libro V). Solo `00_Book_Map.md` (esqueleto). Sin prosa; prosa bloqueada hasta cerrar Juramento de Hierro.

Título y portada de ambos son CANON DEL AUTOR (2026-09-16); la arquitectura de capítulos/partes sigue en incubadora y no está aprobada. Su renumeración a V/VI es puramente posicional — no cambia contenido, título ni portada.

## Flujo EPUB

El generador esta en `tools/epub-build/build_epub.py`. Mientras no existan capitulos de prosa, el EPUB se arma con `00_Front_Matter/00_Nota_Editorial.md` como maqueta de lectura. Cuando ya hay capitulos en las partes, el script omite la nota editorial por defecto e incluye solo prosa, por orden de carpeta y nombre de archivo. Para incluir la nota de montaje manualmente, usar `--include-front-matter`.
