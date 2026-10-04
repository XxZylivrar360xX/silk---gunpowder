# 2026-09-28 — Generador PDF de lectura

## Resultado

- Se añadió `tools/pdf-build/build_pdf.py`, reutilizando el recolector y los controles editoriales de `tools/epub-build/build_epub.py`.
- Se añadió [[tools/pdf-build/README]] con requisitos e instrucciones.
- Se generó `output/pdf/Mascaras_De_Cristal.pdf`: 44 capítulos, tres partes, A5, 589 páginas. Lleva portada tipográfica, créditos, índice, paginación y aviso «Borrador de lectura».
- No se modificó el manuscrito ni se regeneró el EPUB.

## Verificación

- Pandoc + Typst 0.15.1 compilaron el PDF; Poppler reporta 589 páginas y formato A5.
- Se renderizaron y revisaron portada, créditos, índice, divisores de parte, inicio de capítulo, página interior y cierre. La prosa aparece completa hasta «Ciao, bella.».
- Se instalaron Typst y Poppler por winget para generación y QA visual.

## Estado

Todo el Libro I sigue en BORRADOR y pendiente de revisión del autor. La salida es de lectura, no una edición final ni preparada para imprenta.
