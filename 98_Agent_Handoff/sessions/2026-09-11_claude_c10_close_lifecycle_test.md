# C10 — CLOSE (2026-09-11, Claude Code) — primera prueba del lifecycle

Encargo: ejecutar el workflow CLOSE de [[12_Craft_Policies/CHAPTER_LIFECYCLE]] sobre [[11_Books/Book_01_Seda_y_Polvora/Part_01_El_Encuentro_Y_La_Nada/10_El_Corral]], como primera prueba del sistema. Sin AUDIT, sin SURGERY, sin mejoras opcionales, sin tocar prosa.

## Gates

| Gate | Resultado | Razón mínima |
|---|---|---|
| A — Estructura | GREEN | Función identificable (H12, ejecuta beats 1-8 de H5 fusionados); posición confirmada en [[11_Books/Book_01_Seda_y_Polvora/00_Book_Map]]; sin cirugía estructural abierta conocida (M1/M1.5/M2 cerrados); dentro del perímetro de Libro I según [[00_Biblia/00_Trilogy_Structure]] (no menciona Riley/Halbrook/embarazo). |
| B — Continuidad | GREEN | Cotejado línea por línea contra [[06_Relationships/Hitos]] H12: ataque, llamada, bolso/reloj, Beatrice Varek, craniotomía/tres días, tregua con Dario, coartada con las dos grietas, vigilancia, sedán gris, túnel/bahía de carga, parador, restricción de no nombrar al atacante ni a Il Consorzio — todo coincide. Referencia a Corrado (línea 20) coincide palabra por palabra con la versión pública fijada en [[12_Craft_Policies/revelations/SAGA_LEVEL]] ("nunca se devolvió un cuerpo", "paga esa cuenta sola"). Encontrada nota obsoleta en `Hitos.md` (ver candidatos). |
| C — Voz y focalización | GREEN | POV dual (Chiara → Cole) es función deliberada del capítulo (fusiona H12 + apertura de H5), no defecto. El propio reporte de M2 verificó explícitamente que Cole conserva interioridad además de competencia observable y que Chiara conserva agencia perceptiva pese a estar herida. |
| D — Editorial | GREEN | M1, M1.5 y M2 (2026-09-11) ya aplicados y cerrados; el reporte de M2 concluye "no se detectó ninguna zona adicional con el mismo criterio". Único hallazgo pendiente es el HIGH del pilot editorial V1.1 (ver candidatos), no tratado por no bloquear. |
| E — Dependencias | GREEN | El pendiente "secuelas del golpe en Caps. 11-14" pertenece deliberadamente a esos capítulos, no a este (y Cap. 11 ya está resuelto según `PENDING.md`). No hay pendiente autoral sobre la propia versión actual de C10. |
| F — Higiene | GREEN | Sin residuos de prompt ni placeholders en el cuerpo; comentario de header es historial editorial válido según convención del vault. Línea `Estado:` evaluada aparte (ver abajo). Metadata operativa coherente. |

## Resultado final

**READY_FOR_AUTHOR.** Promovido a `Estado: LISTO PARA AUTOR` en el header del capítulo, con autorización explícita del encargo para el cierre técnico. No se marcó TERMINADO.

## Estado heredado — "borrador provisional"

El header usaba `Estado: borrador provisional.` (convención heredada, previa al lifecycle formal). Evaluado como **equivalente seguro a `BORRADOR`**: `CHAPTER_LIFECYCLE.md` cita textualmente esa misma frase como ejemplo de la convención vigente en capítulos ya escritos al introducir los cinco valores formales; "provisional" refuerza, no contradice, la definición de BORRADOR ("todavía está abierto"); y no hay lectura alternativa razonable (no es REVISADO ni ningún estado más avanzado). No se dejó que esta diferencia puramente nominal bloqueara el cierre.

**Hueco de política detectado — CERRADO (2026-09-11, mismo día, encargo del autor):** `CHAPTER_LIFECYCLE.md` no declaraba la equivalencia de forma explícita — sólo usaba la frase como ilustración de la convención antigua. Se añadió una "Regla de equivalencia — estados heredados" en la sección Metadata de `CHAPTER_LIFECYCLE.md`: cualquier formulación heredada que exprese que el capítulo sigue abierto (p. ej. "borrador provisional") equivale automáticamente a `BORRADOR` y no bloquea un CLOSE por sí sola; una formulación heredada ambigua que no exprese claramente "sigue abierto" debe reportarse y preguntarse, no asumirse. Ya no hace falta repetir este análisis capítulo por capítulo al auditar C01-C29.

## Candidatos — NO BLOQUEANTE

1. **Cluster de diálogo largo de Héctor (pilot editorial V1.1, único HIGH del capítulo).** [[tools/editorial/reports/PILOT_01_10_V1_1/10_El_Corral.editorial|Reporte]]: `LONG_DIALOGUE_CLUSTER` sobre el monólogo de confesión de Héctor junto a la cama. Nunca fue triado formalmente (el pilot completo sigue "pendiente de calibración" según `PENDING.md`, sección "Piloto Stack Editorial V1"). Cae directamente en la categoría de falso positivo que el propio pilot marcó como prioritaria a calibrar ("diálogo largo deliberado"); el monólogo es claramente intencional (confesión de un personaje que casi nunca habla así). No bloquea, pero sigue sin cierre formal — decisión del autor o de una calibración futura del stack V1, no de este CLOSE.
2. **Nota obsoleta en `Hitos.md` (H12, sección "Pendientes").** Dice: *"el Capítulo 10 dice 'dos o tres días de observación'"* — desactualizada. La prosa actual (y la nota "Gravedad médica (2026-08-29)" más arriba en el mismo archivo) ya establece craniotomía descompresiva y tres días de evolución. Es un residuo de housekeeping en el ledger, no en el capítulo; vale la pena limpiarlo en un futuro paso de mantenimiento de `Hitos.md`, fuera del alcance de este CLOSE (no se tocó `Hitos.md`).
3. **Pendiente de `PENDING.md` sobre Corrado/Ettore ("formulaciones de los capítulos 2 y 10").** Para C10 específicamente, el texto ya coincide con el canon vigente de `SAGA_LEVEL.md` — no se encontró contradicción. Queda pendiente sólo la mitad del Cap. 2 (fuera de alcance de este CLOSE) y, opcionalmente, que un encargo futuro marque explícitamente resuelta la mitad de C10 en ese pendiente.

## Archivos modificados

- `11_Books/Book_01_Seda_y_Polvora/Part_01_El_Encuentro_Y_La_Nada/10_El_Corral.md` — sólo la línea `Estado:` (→ `LISTO PARA AUTOR`). Sin cambios de prosa.
- `12_Craft_Policies/CHAPTER_STATUS.md` — primera fila poblada (Cap. 10).
- `98_Agent_Handoff/CURRENT_BRIEF.md` — entrada de handoff mínima.
- `98_Agent_Handoff/sessions/2026-09-11_claude_c10_close_lifecycle_test.md` — este archivo (nuevo).

Sin AUDIT, sin SURGERY, sin cambios de canon, sin regeneración de EPUB, sin commit.
