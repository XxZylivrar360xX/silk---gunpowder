# Encargo a Codex: mecánica de la fusión *Bajo juramento*

Fecha: 2026-10-31. Encarga: Claude Code, a pedido del autor. Contexto (leer sólo §Arco legal de Hoover): [[98_Agent_Handoff/sessions/2026-10-31_claude_carretera_libro_i]]. Contrato de rol: [[98_Agent_Handoff/AGENT_ROLES]] (Codex).

**DECISIÓN DEL AUTOR (2026-10-31):** los archivos `23_La_Letra_Pequena.md` (Cap. 28 *Nada caro*) y `24_Bajo_Juramento.md` (Cap. 29) se fusionan en uno solo, *Bajo juramento*, que se escribe en `24_Bajo_Juramento.md`. El 23 sale a `Escenas_Eliminadas/`. **No se renumera** (la renumeración se hará una sola vez, cuando la carretera quede armada). Hoover es socio **del lote** (Lote Almendra), no de un concesionario.

Ruta base: `11_Books/Book_01_Mascaras_De_Cristal/`.

## Reglas para todo el encargo

- No redactar ni editar prosa de capítulos (texto fuera de los comentarios `<!-- -->`).
- No tocar `Hitos.md`, `00_Biblia/`, `CURRENT_BRIEF.md`, `PENDING.md`, `DECISIONS.md` ni `log.md`.
- **Histórico, no tocar:** `98_Agent_Handoff/sessions/`, `98_Agent_Handoff/archive/`, `98_Agent_Handoff/ChatGPT/`, `99_Reference/`, `97_Supersedido/`, `13_Auditorias/` (dictámenes con fecha), `output/`, `.git/`.
- Sin commit ni push.

---

## Fase A: inventario (sólo lectura; se puede hacer ya, en paralelo con Claude)

Buscar con `rg` en todo el vault, excepto `.git/` y `output/`:

1. Enlaces y rutas: `23_La_Letra_Pequena`, `24_Bajo_Juramento`.
2. Títulos: `Nada caro`, `Bajo juramento`.
3. Números, sólo en archivos que también mencionen Hoover, Rivers, Krane o Villani: `Cap. 28`, `Cap. 29`, `Caps. 28–29`, `Caps. 23–24`, `Cap. 23`, `Cap. 24`.
4. Términos: `Hoover` junto a `concesionario` (en la misma línea o en la siguiente), y `Kawasaki`.

Entregar una tabla con estas columnas: archivo · línea · coincidencia · categoría (prosa / encabezado de capítulo / mapa o estado / ficha / política / Libro II / histórico) · acción propuesta (cambiar ruta / anotar fusión / cambiar «concesionario» por «lote» / dejar).

Reporte: `98_Agent_Handoff/sessions/2026-10-31_codex_para_claude_inventario_bajo_juramento.md`. **En esta fase no se edita nada.**

---

## Fase B: ejecución mecánica (SÓLO cuando el autor avise que Claude terminó la fusión)

1. **Mover:** `git mv` de `Part_02_Con_Peores_Personas_He_Tratado/23_La_Letra_Pequena.md` a `Escenas_Eliminadas/23_La_Letra_Pequena.md`. Copiar el formato de encabezado de `Escenas_Eliminadas/19_Tierra_Buena.md`: línea `ESCENA ELIMINADA (2026-10-31, DECISIÓN DEL AUTOR): fusionado en el Cap. 29 *Bajo juramento* (archivo 24).` y `EPUB: EXCLUDE`, dentro del comentario inicial. Añadir su fila a la tabla de `Escenas_Eliminadas/README.md`, con el mismo formato que las demás.
2. **Enlaces:** en archivos no históricos, reescribir `[[...23_La_Letra_Pequena...]]`:
   - en mapas, estados, timeline, fichas, políticas y Libro II → `[[11_Books/Book_01_Mascaras_De_Cristal/Part_02_Con_Peores_Personas_He_Tratado/24_Bajo_Juramento]]` (conservar el alias `|...` si lo hay);
   - si el enlace habla de la versión vieja en concreto → la ruta de `Escenas_Eliminadas/`.
3. **Mapas y estado, sin renumerar:**
   - En `00_Book_Map.md` y `12_Craft_Policies/CHAPTER_STATUS.md`, la fila del Cap. 28 (archivo 23) queda marcada como `fusionado en el 29 (archivo 24), 2026-10-31; Escenas eliminadas`. La fila del 29 se queda con el estado que Claude haya dejado en el encabezado del 24.
   - En `01_Timeline/08_Matriz_Renombramiento_Capitulos_Libro_I.md`, una nota de una línea en la fila del 23.
4. **Lote:** en fichas y facciones (`02_Characters/`, `03_Factions/`), donde se diga que Hoover es socio o dueño «del concesionario», poner «del lote». No tocar «concesionario» cuando se refiera a Villani.
5. **Verificación:**
   - `python -B .\tools\audiolibro\build_audiobook.py --estado` (sin red; sólo marca pendientes).
   - Confirmar que `build_epub.py` sigue sin recorrer `Escenas_Eliminadas/`. No regenerar EPUB ni PDF.
   - Buscar enlaces rotos a `23_La_Letra_Pequena` en archivos no históricos e `INDEX.md`.
   - Contar las palabras de prosa (sin comentarios) de `24_Bajo_Juramento.md` y `24b_Lo_Que_Cueste.md`.
6. **Reporte:** `98_Agent_Handoff/sessions/2026-10-31_codex_para_claude_bajo_juramento_mecanica.md`, con archivos tocados, conteos, el resultado de `--estado` y lo que quedó sin resolver.
