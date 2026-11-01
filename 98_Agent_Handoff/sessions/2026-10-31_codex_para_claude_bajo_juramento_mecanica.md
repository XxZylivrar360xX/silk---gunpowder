# 2026-10-31 — Codex para Claude — Bajo juramento: mecánica (Fase B)

Ejecución: 2026-11-01, autorizada por el autor después de concluir Claude la fusión. Nombre del reporte conservado según el encargo.

Fuentes: [[98_Agent_Handoff/encargos/ENCARGO_Codex_Bajo_Juramento_Mecanica]], [[98_Agent_Handoff/sessions/2026-10-31_codex_para_claude_inventario_bajo_juramento]], [[98_Agent_Handoff/sessions/2026-11-01_claude_fusion_bajo_juramento]]. Contrato: [[98_Agent_Handoff/AGENT_ROLES]] (Codex).

## Resultado

- Ejecutado git mv del archivo 23 desde Part_02 a Escenas_Eliminadas. Añadido al principio un comentario independiente con la leyenda exacta de fusión del 2026-10-31 y EPUB: EXCLUDE, siguiendo el formato del 19. Añadida su fila al README de escenas eliminadas.
- Connors y Rocco apuntan al 24. Confirmadas las carpetas, la manta de Russ y el intercambio de Rocco en la fusión. Nadir apunta al **24b**, porque Claude ya trasladó ahí la moto: excepción contextual identificada en A y respaldada por la decisión del autor. Alias conservados, incluso las etiquetas antiguas de capítulo, como exige B.2.
- Book_Map y CHAPTER_STATUS: fila 28 marcada «fusionado en el 29 (archivo 24), 2026-10-31; Escenas eliminadas»; enlaces de esa versión anterior dirigidos al archivo retirado. Nota de una línea en la fila 23 de la matriz de renombramiento. La fila 29 ya estaba en BORRADOR por Claude y se conservó; coincide con el primer Estado del encabezado fusionado. Sin renumerar.
- Corregido concesionario → lote en Garrett, Villani (sólo al mencionar el litigio anterior) y Almendra Towing (socio del terreno del taller). Las menciones restantes en fichas/facciones describen Villani Motors y se conservaron.

## Verificación

- Snapshot inicial de 813 archivos Markdown/JSON y hash de la prosa fuera de comentarios de 59 archivos de capítulos. Sin cambios de prosa en los capítulos restantes. El archivo 23 retirado, descontando únicamente el nuevo comentario y su salto de línea, coincide byte por byte con su original. Los archivos 24 y 24b no se editaron.
- Comparación de hashes: ningún archivo histórico previo ni Hitos, 00_Biblia, CURRENT_BRIEF, PENDING, DECISIONS, log o INDEX cambió durante esta ejecución. Se crea únicamente este nuevo reporte en sessions. Se conservaron modificaciones y renombrados previos ajenos al encargo.
- Revisados los diffs de esta ejecución y git diff --check, respetando CRLF: único aviso en Connors L10 por los dos espacios finales del salto Markdown ya presentes antes del cambio; se conservaron. Sin errores de whitespace nuevos. README y reporte nuevos comprobados por separado.
- Enlaces a 23: las referencias reales no históricas restantes apuntan a Escenas_Eliminadas y existen. Ningún enlace real quedó dirigido a Part_02/23; INDEX no contiene referencias a 23. El texto literal `[[...23_La_Letra_Pequena...]]` dentro del encargo es un ejemplo de patrón, no un destino real; se dejó intacto. No se repararon enlaces históricos.
- EPUB: inspección de tools/epub-build/build_epub.py, funciones collect_part_sections (líneas 140–153) y collect_folder (113–134): sólo enumera directorios cuyo nombre empieza por part_ y sus Markdown directos; además respeta EPUB: EXCLUDE. Escenas_Eliminadas queda fuera del recorrido. No se regeneraron EPUB ni PDF.

### Conteos de prosa

Se retiraron comentarios HTML y encabezados Markdown; se contaron palabras con la expresión Unicode \b\w+(?:[’'-]\w+)*\b. Es un conteo léxico reproducible, independiente del aproximado anotado por Claude.

| Archivo | Palabras |
|---|---:|
| [[11_Books/Book_01_Mascaras_De_Cristal/Part_02_Con_Peores_Personas_He_Tratado/24_Bajo_Juramento]] | 3744 |
| [[11_Books/Book_01_Mascaras_De_Cristal/Part_02_Con_Peores_Personas_He_Tratado/24b_Lo_Que_Cueste]] | 3016 |

### Audiolibro

Ejecutado python -B .\tools\audiolibro\build_audiobook.py --estado, salida 0, sin red ni generación de audio. Resultado: **51 de 56 al día; 5 pendientes**: 15 Roma Atrii, 24 Lo pequeño, 29 Bajo juramento, 30 Lo que cueste y 46 Cuatro letras. Los pendientes del 29 y 30 constan desde 2026-11-01 00:07 (sesión de Claude); se conservaron. El 23 ya no aparece como capítulo vigente en la tabla. Sus eventos antiguos permanecen en el historial generado.

## Archivos tocados

- [[11_Books/Book_01_Mascaras_De_Cristal/Escenas_Eliminadas/23_La_Letra_Pequena]]
- [[02_Characters/Edward_Connors]]
- [[02_Characters/Rocco]]
- [[02_Characters/Nadir_Amrani]]
- [[02_Characters/Garrett_Cross]]
- [[03_Factions/Villani_Motors]]
- [[03_Factions/Almendra_Towing]]
- [[11_Books/Book_01_Mascaras_De_Cristal/00_Book_Map]]
- [[12_Craft_Policies/CHAPTER_STATUS]]
- [[01_Timeline/08_Matriz_Renombramiento_Capitulos_Libro_I]]
- [[11_Books/Book_01_Mascaras_De_Cristal/Escenas_Eliminadas/README]]
- [[tools/audiolibro/bitacora/Mascaras_De_Cristal]]
- [[tools/audiolibro/bitacora/Mascaras_De_Cristal.json]]
- [[98_Agent_Handoff/sessions/2026-10-31_codex_para_claude_bajo_juramento_mecanica]]

El traslado figura en el índice de Git por git mv; no se añadieron al índice los demás cambios ni se alteró lo que ya estaba preparado antes de esta ejecución. Sin commit ni push.

## Pendientes y límites

Fase B completada. La lectura del autor y la renumeración única quedan fuera de este encargo. Se conservaron alias numéricos heredados, notas fechadas y descripciones previas: por ejemplo, la matriz aún describe el pleito con el término antiguo, y el resumen retirado del 23 conserva su versión. El README mantiene su nota fechada de regreso «sin ejecutar» anterior a la fusión; la fila nueva registra el destino actual. Los gates anteriores de CHAPTER_STATUS no certifican la fusión BORRADOR. Cualquier armonización editorial de esas notas corresponde a Claude, sin reescribir históricos.
