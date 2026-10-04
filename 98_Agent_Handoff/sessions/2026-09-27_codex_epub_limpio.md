# EPUB actualizado y títulos de lectura

Solicitud expresa del autor: regenerar el EPUB, impedir filtraciones de metadata y quitar la numeración de capítulos; partes con romano y guion.

- Regenerado [[tools/epub-build/output/Seda_y_Polvora.epub]] con 44 capítulos y tres partes del Libro I, incluyendo las revisiones actuales.
- [[tools/epub-build/build_epub.py]] exporta títulos sin prefijo de capítulo y partes «I - Dos Mundos», «II - Con peores personas he tratado», «III - Ardizzone». Aplica también al índice.
- Conserva eliminación de YAML/comentarios y exclusión de planes internos. Añade bloqueo ante marcas editoriales residuales o comentarios incompletos. Los metadatos bibliográficos normales se conservan.
- Verificación: ZIP íntegro; XML de XHTML, NCX y OPF válido; 47 encabezados (44 capítulos y tres partes), todos presentes en navegación; sin marcas internas ni rutas de auditoría/handoff. Casos de regresión de prefijos, YAML tras comentario, cartas conservadas y bloqueo de metadata: correctos.
- No se modificaron capítulos ni estados editoriales. La exportación no aprueba los borradores. Pendientes de lectura del autor siguen vigentes.
