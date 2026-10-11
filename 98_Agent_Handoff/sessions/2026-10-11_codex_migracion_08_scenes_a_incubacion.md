# 2026-10-11 — Codex — Migración de escenas a incubación

## Resultado

Por indicación del autor, se descontinuó `08_Scenes/` y sus cinco materiales narrativos quedaron bajo `07_Ideas/Incubacion_Escenas/`, ordenados por libro. Se conservaron los textos y estados editoriales; la copia de Stavanger mantiene un aviso que la identifica como histórica y no canónica.

- Libro II — *Sombras de Poder*: Stavanger (copia histórica; el capítulo vigente sigue en `11_Books/`).
- Libro III — *Voto de Ceniza*: llegada al hospital y nacimiento.
- Libro IV — *Cuentas de Sangre*: *Tornare a Casa* (borrador no canónico) y *Tres Hermanas* (material aprobado).

Se adaptó el README de incubación, se actualizó `07_Ideas/README.md`, `INDEX.md` y el README raíz. También se repararon las referencias activas en `07_Ideas/Escenas_Guia/` y en el handoff de `Libro_04_Incubadora`. Se retiraron las carpetas viejas vacías y su scaffolding.

## Verificación

- No quedaron referencias activas a `08_Scenes/` ni a `07_Ideas/Libro_02_Incubadora/` en Markdown operativo. Las menciones históricas en sesiones y archivos archivados se conservaron.
- Los cinco materiales están en sus nuevas rutas y las dos rutas antiguas ya no existen.
- `git diff --check` terminó sin errores; mostró sólo avisos de conversión LF/CRLF en dos archivos.

## Pendiente

Ninguno para esta migración. No se actualizaron `CURRENT_BRIEF.md`, `PENDING.md` ni `DECISIONS.md`, de acuerdo con el rol de Codex. `log.md` recibió una línea de enlace y el registro más antiguo se trasladó a `archive/2026-10_sesiones.md` para mantener el límite de 30 entradas.
