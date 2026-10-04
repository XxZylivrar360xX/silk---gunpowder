# 2026-09-28 — Regeneración EPUB de *Máscaras de Cristal*

## Resultado

- Se regeneró `tools/epub-build/output/Mascaras_De_Cristal.epub` por solicitud explícita del autor.
- El exportador reunió los 44 capítulos de las tres partes y excluyó dos notas internas marcadas `EPUB: EXCLUDE`.
- La portada del EPUB coincide byte por byte con `99_Reference/book_covers/Mascaras_de_Cristal_VICTOR_PAZ.png`.
- No se modificaron capítulos ni el estado BORRADOR del manuscrito.

## Verificación

- El EPUB abre como archivo ZIP válido (`testzip()` no reportó errores); tamaño: 1,907,295 bytes.
- Se actualizó INDEX, CURRENT_BRIEF y PENDING; el enlace de la versión anterior se retiró del INDEX.
- EPUBCheck no está instalado en este entorno; queda como revisión pendiente.
