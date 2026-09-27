# C06 — REDIRECT STUB formalizado / excluido del EPUB (2026-09-15/16, Claude Code)

Encargo del autor: formalizar que [[11_Books/Book_01_Seda_y_Polvora/Part_01_Dos_Mundos/06_Una_Amiga]] no es un capítulo narrativo y evitar que vuelva a entrar al EPUB, sin renumerar C07+ ni romper enlaces históricos.

## Contexto

C06 contiene únicamente una nota de redirección desde 2026-09-10 (BLOQUE 2 de PLAN_CIRUGIA_EDITORIAL_PARTE_I): el capítulo fue fusionado con el antiguo Cap. 5, cuya prosa vive en [[11_Books/Book_01_Seda_y_Polvora/Part_01_Dos_Mundos/05_La_Casa_No_Quiere_Ruido]] bajo el título «Una amiga». El archivo se conserva solo para no romper enlaces existentes mientras la renumeración global sigue pendiente.

`tools/epub-build/build_epub.py` recopilaba antes todos los `*.md` de cada carpeta `Part_*` sin distinguir capítulos narrativos de redirects/stubs, así que C06 aparecía en el EPUB como «Capítulo 6 — fusionado con el Capítulo 5».

## 1. Directiva en C06

Añadida al inicio del comentario HTML de [[11_Books/Book_01_Seda_y_Polvora/Part_01_Dos_Mundos/06_Una_Amiga]]:

```
EPUB: EXCLUDE
CLASIFICACION: REDIRECT STUB / NO ES CAPITULO NARRATIVO / NO LIFECYCLE / NO EPUB.
```

seguida de la nota de redirección original, sin modificarla. No se tocó el cuerpo visible del archivo (el heading "Capítulo 6 — fusionado con el Capítulo 5" y su párrafo permanecen igual, solo dejan de exportarse porque el archivo entero se excluye antes de llegar a Pandoc).

## 2. Builder — mecanismo genérico

En `tools/epub-build/build_epub.py`:

- Nueva constante `EPUB_EXCLUDE_MARKER = "EPUB: EXCLUDE"` y función `is_epub_excluded(raw_text)` que comprueba la presencia literal de esa cadena en el texto crudo del archivo (antes de despojar el comentario HTML, ya que la directiva vive ahí).
- `read_markdown` se dividió en `format_markdown(text)` (la transformación pura: quita frontmatter YAML, comentarios HTML, aplana wikilinks) y `read_markdown(path)` (lee el archivo y llama a `format_markdown`), para poder reutilizar la transformación sobre un texto ya leído una vez.
- `collect_folder` ahora lee cada archivo una sola vez como texto crudo, comprueba `is_epub_excluded`; si aplica, imprime `- excluded from EPUB: <ruta>` y no lo agrega a las secciones (no heading, no contenido, no Pandoc). El separador de carpeta (`# Parte ... {.part-title}`) solo se antepone si queda al menos un archivo no excluido.
- **Sin excepción hardcodeada de C06** — no hay ningún `if file_path.name == "06_Una_Amiga.md"` ni equivalente. Cualquier `.md` futuro con la misma directiva se excluirá igual, en cualquier carpeta `Part_*` o `00_Front_Matter`.

## 3. README

`tools/epub-build/README.md` documenta la directiva `EPUB: EXCLUDE`: qué hace, dónde se coloca, el mensaje de log que produce, y su propósito (redirects, stubs, notas internas que deben permanecer junto al manuscrito sin exportarse).

## 4. Clasificación editorial de C06

No se le asigna ningún estado de lifecycle (ni BORRADOR, ni LISTO PARA AUTOR, ni TERMINADO, ni CONGELADO) y no se añadió fila para C06 en [[12_Craft_Policies/CHAPTER_STATUS]]. En su lugar, se añadió una nota general mínima en la cabecera de ese archivo: los archivos `REDIRECT STUB` no participan del lifecycle de capítulos y quedan marcados `EPUB: EXCLUDE`, con C06 como ejemplo enlazado. No se infló más documentación de la necesaria.

## 5. Renumeración — NO ejecutada

No se movió C07→C06 ni ningún archivo posterior. No se cambiaron headings de capítulos posteriores ni referencias numéricas globales. Ese trabajo queda como operación transversal separada, según el propio plan de cirugía editorial referenciado en la nota de C06.

## 6. Regeneración y verificación del EPUB

Ejecutado `python tools/epub-build/build_epub.py`. Log relevante:

```
+ .../05_La_Casa_No_Quiere_Ruido.md
- excluded from EPUB: 11_Books\Book_01_Seda_y_Polvora\Part_01_Dos_Mundos\06_Una_Amiga.md
+ .../07_Ambos.md
...
EPUB ready: .../output/Seda_y_Polvora.epub
```

Build terminó sin error. Verificación adicional abriendo el EPUB como ZIP:

- 40 entradas totales; hoja de estilo (`EPUB/styles/stylesheet1.css`) y portada (`EPUB/text/cover.xhtml`) presentes.
- Ningún XHTML contiene el texto de redirección («Este capítulo fue absorbido…» / «fusionado con el Cap…»).
- Secuencia de capítulos de Parte I: … Capítulo 4 → **Capítulo 5 — Una amiga** → **Capítulo 7 — Ambos** … Capítulo 26. El salto de 5 a 7 es el hueco temporal aceptado, sin intento de ocultarlo ni renumerar solo en el EPUB.
- Capítulos 8–29 y ambas partes (I y II) presentes y en orden correcto.

## Housekeeping

- [[98_Agent_Handoff/CURRENT_BRIEF]]: nueva entrada.
- [[98_Agent_Handoff/PENDING.md]]: nueva entrada registrando la formalización y la renumeración global pendiente.
- [[12_Craft_Policies/CHAPTER_STATUS]]: nota general sobre archivos `REDIRECT STUB`, sin fila para C06.

## Resumen de salida

- Archivo conservado: sí. Capítulo narrativo: no. Participa en lifecycle: no. Exportable a EPUB: no.
- Directiva implementada: `EPUB: EXCLUDE`. Mecanismo genérico: sí. Excepción hardcodeada para C06: no.
- Build exitoso: sí. C05 presente: sí. Página de redirect C06 ausente: sí. C07+ presentes: sí. Portada/CSS preservados: sí.
- Renumeración global ejecutada: no. Hueco temporal 5→7 aceptado: sí.
- Prosa modificada: ninguna (solo el comentario interno de C06 y la línea de builder/README). Capítulos renumerados: ninguno. Estados lifecycle modificados: ninguno. Canon nuevo: no.
- Commit/push: no.
