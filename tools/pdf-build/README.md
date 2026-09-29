# Generador PDF

Genera un PDF de lectura del manuscrito de *Máscaras de Cristal* desde las fuentes Markdown del vault.

```powershell
python -B .\tools\pdf-build\build_pdf.py
```

## Requisitos

- Python 3.10 o posterior (biblioteca estándar únicamente).
- Pandoc en `PATH`.
- Typst CLI en `PATH` (motor predeterminado de Pandoc para PDF).

En Windows, Typst se puede instalar con:

```powershell
winget install --id Typst.Typst
```

El script reutiliza el recolector, la limpieza de metadata y las salvaguardas editoriales de `tools/epub-build/build_epub.py`. El PDF se genera en `output/pdf/Mascaras_De_Cristal.pdf`; el Markdown intermedio vive temporalmente en `tmp/pdfs/` y se elimina al terminar.

## Presentación

- Papel A5, márgenes de 18 mm arriba/abajo y 19 mm a los lados, cuerpo de 11 pt e interlineado 1.2.
- Índice de partes y capítulos, paginación arábiga y créditos.
- La portada tipográfica identifica el archivo como **Borrador de lectura**. Se mantiene así mientras la prosa siga pendiente de revisión del autor.
- No cambia el EPUB ni las fuentes del manuscrito.

Opciones útiles:

```powershell
python -B .\tools\pdf-build\build_pdf.py --paper letter
```

Para inspección visual de páginas, instala Poppler (incluye `pdftoppm` y `pdfinfo`). Si falta el motor, el script termina con un mensaje claro. Consulta la documentación oficial de [Pandoc](https://pandoc.org/MANUAL.html) y [Typst](https://typst.app/docs/).
