---
name: regenerar-y-subir
description: Cierre de tarea en este vault. Si la tarea cambió prosa de capítulos, regenera EPUB, PDF y audiolibro (incremental) del libro afectado y verifica; después hace commit y push a develop. Úsala al terminar cualquier tarea que haya cambiado archivos del vault, o cuando el autor diga «regenera», «sube», «cierra» o «súbelo a develop». No se usa a mitad de una tarea ni para cambios que el autor todavía no dio por terminados.
user-invocable: true
---

# Regenerar y subir

Protocolo de cierre (DECISIÓN DEL AUTOR, 2026-11-09): cuando cambia prosa, se regeneran audiolibro, EPUB y PDF; al terminar, todo se sube a `develop`. El autor ya autorizó de forma permanente el commit y el push a `develop` hechos con esta skill. No autoriza `main`, `--force`, reescribir historial ni subir otra rama.

## 0. Antes de empezar

1. Rama: `git branch --show-current` debe ser `develop`. Si no, detente y avisa (no se trabaja en otras ramas; ver memoria del proyecto).
2. `git status --short`: revisa que cada archivo cambiado sea de esta tarea. Si aparece trabajo ajeno (otra terminal, Codex, ChatGPT por Drive) que no conoces, **pregunta** antes de incluirlo; no lo descartes ni lo reviertas.
3. La tarea debe estar cerrada: handoff (`CURRENT_BRIEF`, `PENDING`, `log.md`, nota de sesión) ya actualizado según `CLAUDE.md`. Esta skill no escribe handoff: la regeneración rutinaria no se registra.

## 1. ¿Cambió prosa?

Prosa = cualquier `.md` dentro de `11_Books/<Libro>/Part_*/` (incluida su metadata en comentario HTML: el hash del audio sólo cuenta el texto hablado, así que un cambio de metadata no regenera audio, pero sí puede afectar EPUB/PDF si rompe un comentario).

```bash
{ git diff --name-only HEAD; git ls-files --others --exclude-standard; } | grep -E '^11_Books/Book_0[0-9]_[^/]+/Part_' | cut -d/ -f2 | sort -u
```

- Sin resultado → salta a §5 (sólo commit y push).
- `Book_01_Mascaras_De_Cristal` → §2.
- `Book_02_Sombras_De_Poder` → §3. Si el capítulo cambiado no está en `CHAPTERS` de `tools/build_sombras.py`, no entra a la copia de lectura: no hay que regenerar ese libro (dilo en el reporte).
- Otro libro sin herramientas → no se regenera; dilo en el reporte.

## 2. Libro I — *Máscaras de Cristal*

Desde la raíz del vault, en este orden:

```powershell
python -B .\tools\epub-build\build_epub.py
python -B .\tools\pdf-build\build_pdf.py
python -B .\tools\audiolibro\build_audiobook.py
```

- **EPUB y PDF** tardan segundos. Si el build se detiene por marcas editoriales (`BORRADOR`, `PENDIENTE`, `DISEÑO`, `POV:`…) fuera de comentario o por un comentario sin cerrar, es un error real del capítulo: corrígelo (cerrar el comentario, mover la marca a la metadata), sin borrar prosa, y vuelve a correr. Si la corrección no es obvia, detente y pregunta.
- **Audio**: incremental por hash; sólo regenera los capítulos cuyo texto hablado cambió (~4 min por capítulo; usa red, servicio de Microsoft). Lánzalo con `run_in_background` y espera la notificación; no hagas polling. Si falla la red, reintenta una vez; si vuelve a fallar, sigue con §4 y §5 con el audio PENDIENTE y dilo en el reporte (la bitácora lo deja marcado).
- Nunca `--forzar` ni cambiar voz o velocidad salvo orden del autor.

## 3. Libro II — *Sombras de Poder*

```powershell
python -B .\tools\build_sombras.py
python -B .\tools\audiolibro\build_audiobook.py --book Book_02_Sombras_De_Poder
```

Mismas reglas que §2.

## 4. Verificar

- Los comandos terminaron con código 0.
- Salidas actualizadas (fecha de hoy): `tools/epub-build/output/<Libro>.epub`, `output/pdf/<Libro>.pdf`.
- `python -B .\tools\audiolibro\build_audiobook.py --estado [--book …]` → 0 sin audio al día (o los que fallaron por red, nombrados).
- `git status --short`: además de la tarea, deben aparecer el EPUB, el PDF y `tools/audiolibro/bitacora/*`. Los MP3 no van a git (`output/audiolibro/` está en `.gitignore`; Drive los respalda).

## 5. Commit y push

1. Stage explícito de lo revisado en §0 más las salidas; nada de trabajo ajeno sin confirmar. `desktop.ini` y basura ya los excluye `.gitignore`.
2. Mensaje en español, como los anteriores del repo: primera línea con qué cambió («Parte II: … y regeneración de EPUB, PDF y audio»), cuerpo breve si hace falta, y al final la línea de coautoría que indique el sistema.
3. `git push origin develop`. Si lo rechaza por no fast-forward: `git fetch` y `git pull --ff-only`; si no es fast-forward (historias divergentes), **detente y avisa**. Nunca `--force`, nunca `rebase` sin permiso, nunca `main`.
4. Commits previos de la sesión que no se hayan subido se suben con este push (es lo esperado).

## 6. Reporte

Dos o tres líneas: hash del commit, qué se regeneró (o por qué no), capítulos con audio PENDIENTE si quedó alguno y confirmación del push. Nada de esto va a `log.md`, `CURRENT_BRIEF.md` ni a una nota de sesión, salvo que algo haya fallado y quede pendiente (entonces una línea en `PENDING.md`).
