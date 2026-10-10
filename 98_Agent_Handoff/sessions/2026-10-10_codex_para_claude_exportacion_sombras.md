# Codex → Claude — exportación de Sombras de Poder

**Fecha:** 2026-10-10

## Encargo y resultado

Preparado `tools/build_sombras.py` para regenerar EPUB y PDF del Libro II. Ejecución desde la raíz: `python -B .\tools\build_sombras.py`. Opciones: `--format epub`, `--format pdf`, `--paper letter`, `--year`.

La lista `CHAPTERS` selecciona únicamente [[11_Books/Book_02_Sombras_De_Poder/Part_01_Nieve_Y_Ceniza/01_Hogar|Hogar]]. Usa la fuente vigente renombrada por el autor; no cambia prosa ni estado BORRADOR. Los futuros capítulos se añaden expresamente a la lista. `Ya_Llego.md` queda fuera de esta copia de lectura.

## Cambios de proceso

- Los generadores EPUB/PDF aceptan `--chapter` repetible y un identificador bibliográfico explícito; PDF también recibe colección y posición. El uso predeterminado del Libro I se conserva.
- Libro II: portada `Sombras_De_Poder_VICTOR_PAZ.png`, Víctor Paz, colección *Seda y Pólvora*, posición 2, UUID fijo `urn:uuid:2bbb6f80-be4e-478a-8ff2-4a7348319358`.
- Documentación en [[tools/epub-build/README]], [[tools/pdf-build/README]] y [[11_Books/README]]; navegación en [[INDEX]].
- Se añadió esta entrada a [[log]] y se trasladaron las dos más antiguas al índice mensual para mantener 30 recientes. Sin cambios en CURRENT_BRIEF, PENDING ni DECISIONS, conforme al rol de Codex.

## Salidas y comprobación

- `tools/epub-build/output/Sombras_De_Poder.epub`: generado; ZIP/XML, portada, título, UUID, posición de saga y secciones Créditos / Nieve y ceniza / Hogar comprobados.
- `output/pdf/Sombras_De_Poder.pdf`: generado en A5, 32 páginas; índice hacia la parte (p. 4) y Hogar (p. 5), cierre de Fabrizio. Revisión visual de las 32 páginas renderizadas y detalle de índice, inicio y final.
- Selección explícita comprobada; rechaza rutas ajenas/inexistentes, duplicados y selección vacía. Los comentarios y marcas editoriales no pasan a la lectura.
- El manuscrito recolectado del Libro I mantiene exactamente el hash previo a la modificación. Sus salidas existentes no se regeneraron.

## Pendientes

Agregar a `CHAPTERS` los siguientes capítulos cuando el autor los incorpore a la copia de lectura. La exportación no aprueba el borrador. Sin commit ni push en este encargo.
