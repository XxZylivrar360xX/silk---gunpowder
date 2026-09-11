# 2026-09-11 — Claude Code — Ciclo de vida y cierre de capítulos

## Encargo

Formalizar cómo un capítulo pasa de BORRADOR a TERMINADO (y eventualmente CONGELADO). El sistema editorial general (`EDITORIAL_POLICY.md`, `DO_NOT_TOUCH.md`, `MICROEDICION.md`, skill `editorial-surgery`) ya existía de la sesión anterior — este encargo añade la pieza de ciclo de vida, no la rediseña.

## Rama y HEAD

`develop`, HEAD `fe002ba` al iniciar. Árbol con cambios previos sin commitear (trabajo editorial de la sesión anterior). No se hizo commit ni push en esta sesión.

## A. Archivos creados

- `12_Craft_Policies/CHAPTER_LIFECYCLE.md` — documento central: principio, 5 estados, gates A–F, READY_FOR_AUTHOR/BLOCKED, workflow CLOSE, bloqueante vs. no bloqueante, metadata, decisión de ledger, tabla de autoridad, no retroactividad.
- `12_Craft_Policies/CHAPTER_STATUS.md` — ledger compacto (capítulo/estado/última revisión/bloqueador), creado sin poblar.
- Esta nota de sesión.

## B. Archivos modificados

- `12_Craft_Policies/Redaccion_De_Capitulos.md` — sección "Después de escribir" enlazando a CHAPTER_LIFECYCLE.
- `12_Craft_Policies/editorial/MICROEDICION.md` — párrafo aclarando que CLOSE pertenece al lifecycle, no a los tres modos de microedición.
- `.claude/skills/editorial-surgery/SKILL.md` — reconoce CLOSE como cuarto modo (cuándo se activa, arranque, ejecutar el modo); nunca traduce READY_FOR_AUTHOR como TERMINADO.
- `12_Craft_Policies/README.md` — CHAPTER_LIFECYCLE en la lista de estructura; párrafo sobre el cuarto modo CLOSE.
- `INDEX.md` — enlaces a CHAPTER_LIFECYCLE y CHAPTER_STATUS.
- `98_Agent_Handoff/CURRENT_BRIEF.md` — nueva entrada de estado (ver abajo).
- `log.md` — nueva entrada.

## C. Máquina de estados

`BORRADOR → [REVISADO opcional] → LISTO PARA AUTOR → TERMINADO → CONGELADO`

REVISADO no es obligatorio: BORRADOR puede saltar directo a LISTO PARA AUTOR. TERMINADO exige aprobación explícita del autor, nunca inferida por silencio. CONGELADO es TERMINADO + unidad editorial cerrada (Parte/Libro), y solo se reabre por error objetivo, contradicción de continuidad, cambio de canon, cirugía estructural autorizada o pedido directo — nunca por gusto estilístico.

## D. Gates definitivos

A — Estructura · B — Continuidad · C — Voz y focalización · D — Editorial (no reabre auditoría completa; revisa reporte existente) · E — Dependencias (pendiente sobre el futuro no bloquea; pendiente sobre la versión actual sí) · F — Higiene.

## E. Cómo funciona CLOSE

Certificación de madurez, no una cuarta modalidad de microedición: identifica capítulo → lee estado → revisa reportes/pendientes → comprueba gates A–F → lectura final buscando bloqueadores (no mejoras) → emite READY_FOR_AUTHOR o BLOCKED. Un error mecánico objetivo puede corregirse si el alcance lo permite; una mejora editorial posible se registra como `CANDIDATO — NO BLOQUEANTE` sin tocarla; un bloqueador real detiene la promoción.

## F. Autoridad agente/autor

Ver tabla en CHAPTER_LIFECYCLE. Resumen: el agente puede mantener/marcar hasta LISTO PARA AUTOR (con gates); TERMINADO y CONGELADO son exclusivos del autor (CONGELADO solo vía workflow previamente autorizado); nadie reabre CONGELADO por gusto estilístico.

## G. Decisión sobre ledger central

Se creó `CHAPTER_STATUS.md` porque ni `00_Book_Map.md` ni `INDEX.md` llevan una tabla capítulo-por-capítulo escaneable (ambos son prosa narrativa de seguimiento). El ledger no duplica análisis: solo referencia. Se dejó **sin poblar** — poblarlo retroactivamente para C01–C29 es la auditoría de estados que este encargo explícitamente pospone.

## H. Integración con `editorial-surgery`

Se amplió la skill existente (no se creó una nueva). CLOSE se agregó como cuarto modo reconocible junto a AUDIT/SURGERY/VERIFY, con su propia carga de lectura (CHAPTER_LIFECYCLE) y su propia regla dura (nunca traducir READY_FOR_AUTHOR como TERMINADO). Evita proliferación de skills sin necesidad real.

## I. Qué se decidió NO automatizar

- No se recorrieron ni cambiaron estados de C01–C29.
- No se pobló el ledger con datos reales.
- No se tocó prosa narrativa alguna.
- No se regeneró el EPUB.
- No se hizo commit ni push.
- CLOSE no corrige por iniciativa propia salvo error mecánico objetivo dentro de alcance ya autorizado.

## J. Riesgos / contradicciones encontradas

Ninguna contradicción real con el sistema editorial existente. Punto de fricción potencial a vigilar: la convención actual de header de capítulo usa `Estado: borrador provisional.` (texto libre, minúsculas) en vez de los cinco valores formales (`BORRADOR`, etc.). CHAPTER_LIFECYCLE documenta los cinco valores oficiales pero **no normalizó** los headers existentes — eso es parte de la auditoría retroactiva pospuesta, no de este encargo.
