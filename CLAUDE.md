# CLAUDE.md

Guia corta para Claude Code en este vault. Mantener breve: este archivo se carga al inicio y no debe convertirse en bitacora.

## Responder Barato

Los tokens son recurso del usuario. Por defecto:

- Responde en espanol de Mexico, con "tu", sin voseo.
- Respuesta corta: 1-3 frases para tareas simples; mas detalle solo si cambia una decision.
- No repitas salidas largas de comandos ni resumas dos veces lo mismo.
- No leas archivos enormes "por si acaso": usa `rg`, indices, brief y lectura por demanda.
- `log.md` es historico largo; no lo leas completo salvo peticion explicita.
- Si el trabajo fue largo, el detalle va al vault o al handoff, no al chat.

## Arranque De Sesion

1. Lee `98_Agent_Handoff/START_HERE.md`.
2. Lee `98_Agent_Handoff/CURRENT_BRIEF.md`.
3. Revisa `98_Agent_Handoff/PENDING.md` si vas a proponer siguiente trabajo.
4. Usa `INDEX.md` para navegar.
5. Lee solo los archivos directamente relacionados con la tarea.

## Que Es Esto

*Seda y Polvora* es una novela original de crimen y romance en vault de Obsidian. No hay build, tests ni dependencias: todo es Markdown, canon, continuidad y estructura narrativa.

No es adaptacion. Giulia Rossetti y Kyle Rass fueron solo semilla de inspiracion: nacionalidad y arquitectura de personalidad. Nombres, biografia, ciudad, familia, negocios y trama son originales. Si algo empieza a parecer copia de la fuente, hay que alejarlo.

## Reglas Intocables

- **CANON DEL AUTOR:** no reinterpretar, no sustituir, no "mejorar" lineas de dialogo canon.
- **DISENO:** inferencia del agente; se puede discutir.
- **PENDIENTE:** falta decision del autor; no rellenar por conveniencia.
- Cole y Chiara no se separan, pero el lector debe creer que pueden romperse.
- La relacion es maquinaria del ascenso, no subtrama.
- El toma territorio; ella toma relato.
- La violencia debe cambiar una relacion o estructura; si no, sobra.
- La ciudad se escribe como lugar concreto, no decorado generico.

## Rutas Clave

- `INDEX.md`: mapa maestro del vault.
- `98_Agent_Handoff/`: relevo compacto entre agentes.
- `00_Biblia/`: vision, temas, principios y reglas del mundo.
- `01_Timeline/00_Estructura_del_Ascenso.md`: fases del ascenso.
- `01_Timeline/01_Primer_Borrador_Beats.md`: 90 beats macro.
- `06_Relationships/Cole_y_Chiara.md`: arquitectura de la relacion.
- `06_Relationships/Hitos.md`: hitos obligatorios del autor.
- `06_Relationships/Momentos_de_Fractura.md`: conflictos que casi lo rompen todo.
- `99_Reference/`: referencia externa no canon; no copiar.

## Escritura Y Edicion

- Contenido del vault en espanol.
- Rutas nuevas sin tildes ni enes.
- Enlaces Obsidian: `[[Carpeta/Archivo]]`, sin `.md`.
- Al crear archivo relevante, enlazar en `INDEX.md`.
- Al cerrar cambio sustantivo, actualizar `98_Agent_Handoff/CURRENT_BRIEF.md`; si cambia canon o continuidad, tambien `log.md`.
- No hacer commit ni push salvo que el usuario lo pida.

## Lectura Bajo Demanda

- Para escena: leer personajes presentes, lugar, fase y hito relacionado.
- Para personaje: leer ficha, relacion directa y auditoria si afecta reparto.
- Para trama: leer estructura del ascenso, primer borrador de beats y mapa de conflicto.
- Para relevo rapido: leer solo `START_HERE`, `CURRENT_BRIEF` y `PENDING`.
