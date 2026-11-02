# Encargo a Codex: renumeración del Libro I a 56 capítulos

Fecha: 2026-11-01. Encarga: Claude Code, a pedido del autor. Contrato de rol: [[98_Agent_Handoff/AGENT_ROLES]] (Codex). Al terminar, Claude verifica.

**DECISIÓN DEL AUTOR (2026-11-01):** la carretera del Libro I quedó aprobada y armada; se renumera **una sola vez**, de 60 a **56** capítulos. Salieron a `Escenas_Eliminadas/` los Caps. 14 (archivo 11), 16 (12b) y 23 (19). Se fusionaron el 6 (05b) en el 5 y el 28 (23) en el 29 (24). H13 *Grazie* (21b) entra como capítulo propio que cierra la Parte I. Contexto: [[98_Agent_Handoff/sessions/2026-11-01_claude_paso3_saldos_carretera]] y [[13_Auditorias/Book_01_Mascaras_De_Cristal/Carretera_Libro_I]].

Ruta base: `11_Books/Book_01_Mascaras_De_Cristal/`. **Los nombres de archivo no cambian**, sólo el número visible.

## Reglas

- No redactar ni editar prosa (texto fuera de los comentarios `<!-- -->`). Lo único que se toca dentro del cuerpo es la línea de encabezado `# Capítulo N — Título`.
- No tocar `Hitos.md`, `00_Biblia/`, `CLAUDE.md`, `AGENTS.md`, `CURRENT_BRIEF.md`, `PENDING.md`, `DECISIONS.md` ni `log.md` (Claude los actualiza tras verificar).
- **Histórico, no se renumera:** `98_Agent_Handoff/sessions/`, `archive/`, `ChatGPT/`, `encargos/`, `99_Reference/`, `97_Supersedido/`, `Escenas_Eliminadas/`, los dictámenes fechados de `13_Auditorias/` (salvo los dos documentos vivos que se listan abajo), fichas de `02_Characters/`, `03_Factions/`, `05_Locations/` y los ledgers de `12_Craft_Policies/revelations/`. Esos documentos siguen en «la numeración de su época» (convención del Book_Map).
- No regenerar EPUB, PDF ni audio. Sin commit ni push.
- **Ojo:** el 2026-10-22 ya hubo una «numeración de 56». Para no confundirlas, la nueva se nombra siempre **«numeración del 2026-11-01»** (o «de 56, 2026-11-01»), nunca sólo «de 56».

## Tabla de correspondencia (antes → ahora)

Los títulos se toman del encabezado de cada archivo, no de esta tabla.

| Ahora | Antes | Archivo | | Ahora | Antes | Archivo |
|---|---|---|---|---|---|---|
| 1 | 1 | 01 | | 29 | 33 | 25 |
| 2 | 2 | 02 | | 30 | 34 | 26 |
| 3 | 3 | 03 | | 31 | 35 | 27 |
| 4 | 4 | 04 | | 32 | 36 | 28 |
| 5 | 5 | 05a | | 33 | 37 | 29 |
| 6 | 7 | 05c | | 34 | 38 | 30 |
| 7 | 8 | 06 | | 35 | 39 | 31 |
| 8 | 9 | 07 | | 36 | 40 | 32 |
| 9 | 10 | 08 | | 37 | 41 | 33 |
| 10 | 11 | 08b | | 38 | 42 | 33b |
| 11 | 12 | 09 | | 39 | 43 | 34 |
| 12 | 13 | 10 | | 40 | 44 | 35 |
| 13 | 15 | 12 | | 41 | 45 | 36 |
| 14 | 17 | 13 | | 42 | 46 | 37 |
| 15 | 18 | 14 | | 43 | 47 | 38 |
| 16 | 19 | 15 | | 44 | 48 | 39 |
| 17 | 20 | 16 | | 45 | 49 | 40 |
| 18 | 21 | 17 | | 46 | 50 | 41 |
| 19 | 22 | 18 | | 47 | 51 | 42 |
| 20 | 24 | 20 | | 48 | 52 | 43 |
| 21 | 25 | 21 | | 49 | 53 | 44 |
| 22 | 25b (encabezado actual: «25») | 21b | | 50 | 54 | 45 |
| 23 | 26 | 22a | | 51 | 55 | 46 |
| 24 | 27 | 22b | | 52 | 56 | 47 |
| 25 | 29 | 24 | | 53 | 57 | 48 |
| 26 | 30 | 24b | | 54 | 58 | 49 |
| 27 | 31 | 24c | | 55 | 59 | 50 |
| 28 | 32 | 24d | | 56 | 60 | 50b |

Fuera del libro (sin número nuevo): antiguo 6 (05b, retirado), 14 (11), 16 (12b), 23 (19) y 28 (23).

**Partes:** I *Dos Mundos* = Caps. 1–22 (01–21b); II = 23–39 (22a–34); III *Ardizzone* = 40–56 (35–50b). Arco final sin Kal = 49–56 (44–50b). «—Ciao, bella.» es la última línea del 55 (archivo 50); el 56 es el desenlace. Primer punto de giro: Cap. 11 *La balanza*; primera respuesta: Cap. 14 *Auster*.

## Qué hacer

1. **Encabezados:** en los 51 archivos que cambian, `# Capítulo N — Título` pasa al número nuevo (antes de tocarlo, comprobar que el número viejo coincide con la tabla). En el comentario inicial, añadir arriba la línea `Renumerado 2026-11-01 (decisión del autor, carretera del Libro I): antes Cap. N.` Los archivos 01–05a no cambian.
2. **[[11_Books/Book_01_Mascaras_De_Cristal/00_Book_Map]]:** nota de numeración nueva al principio (resume la tabla y deja claro que los documentos fechados antes del 2026-11-01 usan la numeración de 60). Tabla principal regenerada **desde los encabezados**, 1–56 sin huecos. Las filas retiradas se mueven a una tabla aparte, «Fuera del libro», con su número de 60. Al día: partes, «Punto de salida» y las notas «hoy Caps.».
3. **[[12_Craft_Policies/CHAPTER_STATUS]]:** nota de numeración y columna de capítulo al día, con las retiradas aparte. **Los estados no se tocan.**
4. **Documentos vivos que citan números de capítulo.** Se pasan a la numeración nueva y se pone una nota de una línea arriba:
   - [[01_Timeline/02_Libro_01_Mascaras_De_Cristal]]
   - [[12_Craft_Policies/milestones/INDEX]]
   - [[13_Auditorias/Book_01_Mascaras_De_Cristal/Matriz_Temporal_Libro_I]]
   - [[INDEX]]
5. **Sólo una nota de equivalencia arriba, sin reescribir el cuerpo:**
   - [[11_Books/Book_01_Mascaras_De_Cristal/00_Plan_Arco_Final_Sin_Kal]] (sus 53–60 son hoy 49–56)
   - [[13_Auditorias/Book_01_Mascaras_De_Cristal/Carretera_Libro_I]]
   - [[01_Timeline/08_Matriz_Renombramiento_Capitulos_Libro_I]] (su nota de «56 caps.» se refiere a la numeración del 2026-10-22; aclararlo)
   - [[11_Books/Book_01_Mascaras_De_Cristal/00_Plan_Hilo_Tasador]]
   - [[11_Books/Book_01_Mascaras_De_Cristal/Part_01_Dos_Mundos/00_Plan_Rediseno_Parte_I]]
   - la guía de lectura [[98_Agent_Handoff/sessions/2026-10-31_claude_guia_lectura_caps34_60]]. Es una excepción al histórico porque el autor la está usando: una tabla 34–60 → 30–56 arriba.
6. **Audiolibro:** `python -B .\tools\audiolibro\build_audiobook.py --estado` (sin red). Anotar qué capítulos quedan pendientes por el cambio del número hablado.
7. **Comprobaciones:**
   - `rg "^# Capítulo" 11_Books/Book_01_Mascaras_De_Cristal/Part_0*` da 1–56 sin huecos ni repetidos.
   - Ningún enlace `[[...]]` roto por el cambio (no debería haber ninguno, porque los nombres de archivo no cambian).
   - `build_epub.py` sólo quita el número del encabezado, así que el EPUB no depende de él. No hace falta generarlo.

## Reporte

`98_Agent_Handoff/sessions/AAAA-MM-DD_codex_para_claude_renumeracion_56.md` (con la fecha real), con:

- los archivos tocados;
- la salida de las comprobaciones;
- una **lista de referencias numéricas que quedaron sin tocar** en documentos no históricos y que podrían confundir (con archivo y línea). Esas no se corrigen: las decide Claude.
