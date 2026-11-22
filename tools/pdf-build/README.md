# Generador PDF

Genera un PDF de lectura desde las fuentes Markdown del vault; por defecto, *Máscaras de Cristal*.

```powershell
python -B .\tools\pdf-build\build_pdf.py
```

## Interior de imprenta (tapa blanda 6 × 9)

```powershell
python -B .\tools\pdf-build\build_imprenta.py
```

Genera `output/pdf/Mascaras_De_Cristal_Imprenta_6x9.pdf`, el interior para KDP (2026-11-22, a pedido del autor). Es distinto del PDF de lectura en A5:

- página de 6 × 9 in con márgenes en espejo: 0.875 in de medianil, 0.625 in al exterior y 0.85 in arriba y abajo (KDP pide al menos 0.75 in de medianil hasta 700 páginas);
- Libertinus Serif a 11 pt, justificada, con división silábica en español, sangría de primera línea y control de viudas y huérfanas (fuente libre OFL, se puede incrustar para venta);
- preliminares en orden: portadilla, verso en blanco, portada y créditos; sin cubierta, que va en archivo aparte;
- partes y capítulos en página impar, con caída; las cabeceras llevan el título del libro en la página par y el del capítulo en la impar; folio arriba al exterior, y al pie en las aperturas;
- separador de escena con tres asteriscos pegado al párrafo siguiente; las cartas van en bloque sangrado;
- índice al final.

Al terminar imprime el número de páginas y el lomo estimado (papel blanco y crema) para `tools/portada/componer_tapa.py`. `--muestra 1-12,689` exporta esas páginas a PNG para revisarlas sin abrir el PDF. Las medidas viven en la plantilla Typst dentro del script.

## Sombras de Poder

El lanzador del Libro II regenera EPUB y PDF con la misma selección de capítulos:

```powershell
python -B .\tools\build_sombras.py
```

Para regenerar sólo el PDF:

```powershell
python -B .\tools\build_sombras.py --format pdf
```

La selección inicial incluye únicamente **Hogar**, en la Parte I — Territorio ajeno. La salida es `output/pdf/Sombras_De_Poder.pdf`. Para incorporar capítulos posteriores, actualizar `CHAPTERS` en `tools/build_sombras.py`; instrucciones y metadatos en [[tools/epub-build/README]].

El generador PDF también acepta `--chapter` repetible (rutas relativas a `--book`), `--series`, `--series-position` y `--identifier`. El lanzador ya fija estos valores para el Libro II. `--paper letter` cambia el tamaño del PDF sin alterar el EPUB.

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
- La primera página es la portada ilustrada (`--cover`, ruta relativa al vault; por defecto la v1 de *Máscaras de Cristal*; `--cover ""` la omite). El lanzador del Libro II pasa la suya.
- La portada tipográfica identifica el archivo como **Borrador de lectura**. Se mantiene así mientras la prosa siga pendiente de revisión del autor.
- No cambia el EPUB ni las fuentes del manuscrito.

Opciones útiles:

```powershell
python -B .\tools\pdf-build\build_pdf.py --paper letter
```

Para inspección visual de páginas, instala Poppler (incluye `pdftoppm` y `pdfinfo`). Si falta el motor, el script termina con un mensaje claro. Consulta la documentación oficial de [Pandoc](https://pandoc.org/MANUAL.html) y [Typst](https://typst.app/docs/).
