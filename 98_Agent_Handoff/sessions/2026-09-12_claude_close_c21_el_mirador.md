# CLOSE C21 — El mirador

**Fecha:** 2026-09-12. **Agente:** Claude Code. **Encargo:** ejecutar exclusivamente el lifecycle CLOSE de [[11_Books/Book_01_Seda_y_Polvora/Part_01_Dos_Mundos/21_El_Mirador]] después de VERIFY satisfactorio. Sin AUDIT, sin SURGERY, sin nuevo VERIFY, sin microedición, sin reabrir decisiones autorales.

## Antecedentes tomados como dados

- Diagnóstico editorial: [[98_Agent_Handoff/sessions/2026-09-09_codex_revision_editorial_cap_21]].
- Comprobación SURGERY (cero intervenciones nuevas, todo ya aplicado desde 2026-09-10): [[98_Agent_Handoff/sessions/2026-09-12_claude_surgery_c21_el_mirador]].
- VERIFY posterior: VERIFIED — correcciones objetivas, continuidad menor, sonrisa duplicada, bolera, penthouse, baile, beso/dormitorio y focalización resueltos; consentimiento, drift y mirador intactos; Dale/Ruth intacto; ningún bloqueador para CLOSE.
- Deuda documental conocida (sincronizar H11 con la prosa aprobada respecto al hablante del drift): al verificar contra [[06_Relationships/Hitos]] esta deuda específica **ya estaba resuelta** (nota "SINCRONIZADO CON LA PROSA (2026-09-10)" bajo H11 → "El drift"). La deuda documental real que persiste es otra, detectada al revisar H11 completo durante este CLOSE: la sección "El penthouse" de H11 sigue describiendo el beso ocurriendo en el sofá, con la botella de vino ya servida ("Adentro, con la botella de vino ya en el sofá... por fin se besan"), mientras la prosa vigente del capítulo sitúa el beso de pie, tras el baile, junto al espejo del recibidor (ajuste del 2026-09-09 al detonador del beso). Esta discrepancia ya estaba señalada como pendiente en el diagnóstico original de 2026-09-09 ("H11 todavía describe el beso en el sofá y conserva numeración antigua... esta desactualización no obliga a devolver el capítulo a la versión anterior"). **No bloquea CLOSE.** No se modificó H11 en este encargo.

## Gates

### A. Structure — GREEN
El capítulo cumple H11 (bolos, drift, mirador, penthouse). Progresión bolera → mirador → penthouse funciona: juego sin utilidad → confesión de Dale y Ruth → intimidad. Sin huecos estructurales internos.

### B. Continuity — GREEN
Continuidad interna intacta. Conexiones con C19/C20 compatibles: búnker del octavo hoyo cotejado con Cap. 19 (L225); apertura "Estás en otro lado" anclada en el casino; botella del penthouse inequívocamente la comprada esa noche. La deuda documental de H11 (beso en el sofá vs. beso de pie tras el baile) es una desactualización de la ficha de hitos, no una contradicción dentro del manuscrito — la prosa del capítulo es internamente consistente consigo misma.

### C. Voice / focalización — GREEN
Cole y Chiara reconocibles. La excepción de Cole hablando de Dale y Ruth está justificada por canon del autor explícito (Hitos.md, H11: "esto es la primera y única vez que Cole verbaliza en voz alta lo que Dale y Ruth le hicieron... se rompe una sola vez, aquí, con ella"). Focalización de la pasada del penthouse ya resuelta según VERIFY. Sin problema de voz que bloquee cierre.

### D. Editorial — GREEN
Las deudas del diagnóstico 2026-09-09 (secciones 1-3 + dos pendientes protegidos) están resueltas — confirmado por SURGERY (cero intervenciones nuevas necesarias) y por el header del capítulo, que documenta cada corrección aplicada el 2026-09-10. Sin cirugía pendiente conocida sobre la prosa del capítulo. M5/VERIFY no detectó problema global nuevo en C21 aparte de las deudas ya conocidas y resueltas.

### E. Dependencies — GREEN
Sin decisión autoral pendiente que impida considerar madura la prosa. La deuda documental de H11 (beso en el sofá) puede sincronizarse después en `Hitos.md` sin modificar el capítulo — es trabajo de ledger, no de manuscrito.

### F. Hygiene — GREEN
Metadata coherente: el header (comentario HTML de cabecera) documenta versión, ventana temporal y cada pasada editorial aplicada. Estado previo `borrador provisional` — equivalente heredado de BORRADOR, mismo criterio usado en el CLOSE de Cap. 10 (`CHAPTER_LIFECYCLE.md`, "Regla de equivalencia — estados heredados"). Grep sobre el archivo no encontró marcadores editoriales accidentales ni notas internas dentro de la prosa (el único bloque `<!--...-->` es el comentario de cabecera estándar del vault, no un residuo). No se requiere regenerar EPUB para certificar CLOSE.

## Deuda no bloqueante

- **H11 documental: SINCRONIZAR.** La sección "El penthouse" de [[06_Relationships/Hitos]] (H11) describe el beso en el sofá; la prosa vigente lo sitúa de pie, tras el baile, junto al espejo del recibidor. Sincronizar en un encargo futuro dedicado a `Hitos.md`; no se tocó en este CLOSE.

## Resultado

`READY_FOR_AUTHOR`

## Estado lifecycle

- **Anterior:** `borrador provisional` (equivalente a BORRADOR).
- **Nuevo:** `LISTO PARA AUTOR`.

## Integridad

- Prosa modificada: 0.
- Otros capítulos modificados: 0.
- Canon modificado: 0.
- H11 modificado: no.
- EPUB regenerado: no.

## Housekeeping de esta sesión

- `Estado:` del capítulo actualizado a `LISTO PARA AUTOR` (única línea tocada en el archivo del capítulo).
- Fila de Cap. 21 añadida en [[12_Craft_Policies/CHAPTER_STATUS]].
- `98_Agent_Handoff/CURRENT_BRIEF.md` actualizado con esta entrada.
- `PENDING.md`: retirada la entrada "SURGERY aplicada; pendiente VERIFY/CLOSE" (resuelta); conservada únicamente la deuda documental de sincronización de H11, marcada explícitamente como no bloqueante.
- Creado este archivo de sesión.

Sin commit ni push.
