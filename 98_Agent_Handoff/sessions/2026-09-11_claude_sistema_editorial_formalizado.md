# Sistema editorial formalizado (2026-09-11, Claude Code)

Encargo del autor: convertir el proceso editorial validado en M0–M4 (ver [[98_Agent_Handoff/sessions/2026-09-11_claude_c10_microedicion_m2]], [[98_Agent_Handoff/sessions/2026-09-11_codex_microedicion_m3_fundacion_de_voz]], [[98_Agent_Handoff/sessions/2026-09-11_codex_microedicion_m4_intuicion_presagio_percepcion]]) en un sistema permanente, reutilizable y agnóstico al agente. No se tocó prosa; no se inició microedición nueva.

## A. Archivos creados

- `12_Craft_Policies/editorial/MICROEDICION.md` — procedimiento operativo: modos AUDIT/SURGERY/VERIFY, lectura antes de editar, catálogo de categorías de candidatos (corte y protección), árbol de decisión de 7 pasos, protecciones deliberadas, autocrítica obligatoria, regla de no-segunda-pasada.
- `.claude/skills/editorial-surgery/SKILL.md` — skill de Claude Code. Confirmada la convención real del harness (`.claude/skills/<nombre>/SKILL.md` con frontmatter `name`/`description`/`user-invocable`) contra un ejemplo instalado del sistema antes de crearla.
- `98_Agent_Handoff/sessions/2026-09-11_claude_sistema_editorial_formalizado.md` — este archivo.

## B. Archivos modificados

- `12_Craft_Policies/editorial/EDITORIAL_POLICY.md` — se conservó íntegra la política existente (una alerta no es error, estructura≠edición, no uniformidad matemática, orden de prioridad, DO_NOT_TOUCH manda) y se añadieron 11 secciones (A–K) con los aprendizajes de M0–M4.
- `12_Craft_Policies/README.md` — sección nueva "Craft vs. editorial" (qué responde cada capa y por qué `Redaccion_De_Capitulos.md` no absorbe el método editorial) y "Editorial: modos y skill" (mapa de AUDIT/SURGERY/VERIFY y qué carga la skill).
- `CLAUDE.md` (raíz del vault) — una línea añadida en "Escritura Y Edicion": remite a la skill `editorial-surgery` y a `12_Craft_Policies/editorial/` para auditoría, microedición o verificación. Nada más.
- `INDEX.md` — entradas para `MICROEDICION.md` y la skill.
- `98_Agent_Handoff/CURRENT_BRIEF.md` — entrada de estado al inicio.

## C. Qué archivo tiene qué responsabilidad

| Archivo | Responsabilidad |
|---|---|
| `EDITORIAL_POLICY.md` | Filosofía y principios de juicio: cómo decidir si algo debe tocarse. |
| `DO_NOT_TOUCH.md` | Fronteras absolutas de canon/arquitectura que ninguna pasada editorial cruza. |
| `MICROEDICION.md` | Procedimiento: modos, clasificación, árbol de decisión, formato de reporte. |
| `.claude/skills/editorial-surgery/SKILL.md` | Activación y orden de carga para que Claude Code ejecute el sistema sin prompt largo. |
| `Redaccion_De_Capitulos.md` | Cómo generar prosa nueva — no se toca; sigue siendo craft, no edición. |

## D. Por qué `Redaccion_De_Capitulos.md` no absorbe el método editorial

Escribir y editar tienen objetivos opuestos: generar material nuevo bajo reglas de voz/POV/staging vs. juzgar material ya generado sin destruirlo. Mezclarlos convertiría la guía de escritura en manual de corte y viceversa — un redactor leyendo esa política terminaría auto-censurando prosa nueva con criterios de intervención posterior, y un editor terminaría inventando reglas de escritura que no le corresponden. Se mantienen como capas separadas con precedencia ya declarada en `README.md`.

## E. Skill: cuándo se activa, modos, qué carga, qué no puede hacer

- **Se activa** para: auditoría editorial, microedición, cirugía de prosa, revisión de redundancia/sobreexplicación, verificación postoperatoria, análisis transversal de tics.
- **No se activa** para: redacción inicial, brainstorming, canon, diseño estructural, merge de capítulos, continuidad macro, EPUB, diálogo puro.
- **Modos:** AUDIT (no toca prosa), SURGERY (toca solo el ámbito autorizado), VERIFY (evalúa una cirugía ya hecha).
- **Qué carga, en orden:** `EDITORIAL_POLICY.md` → `DO_NOT_TOUCH.md` → `MICROEDICION.md` → solo después, fichas de voz/ledger/hitos/capítulos específicos del encargo.
- **Qué no puede hacer:** fusionar capítulos, mover escenas, cambiar orden, crear beats, resolver motivaciones, reestructurar arcos. Si detecta un problema de ese tipo, reporta y detiene la intervención en esa zona — no lo resuelve.

## F. Deducciones de M0–M4 promovidas a política permanente

- El molde "algo en el fondo del estómago... nunca se equivocaba" (M4) → sección G, intuición vs. presagio cierto.
- "Cole hizo lo que sabía hacer... convertirse en alguien capaz" y la garantía de acierto de Mabel (M2/M4) → sección C, acción antes que certificación.
- El diagnóstico atribuido retroactivamente al cuerpo en C16 (M4) → sección F, cuerpo no equivale a conocimiento.
- La clasificación FIRMA/FUNCIONAL/REPETITIVO de los 49 casos de "como si" en C01 (M3) → sección A del policy y categorías REPETICIÓN LEXICAL/SINTÁCTICA/FUNCIONAL de MICROEDICION.
- "Chiara no creyó en nada natural" evaluada y finalmente cortada, pero documentada como duda legítima (M3) → sección B (valor no informativo) y la categoría DUDOSA — CONSERVAR.
- El intercambio "before/after + categoría + razón + qué ya hacía la escena + qué conserva" usado consistentemente en M2/M3/M4 → formato obligatorio de SURGERY en MICROEDICION sección A.
- El patrón de preguntas de cierre de M2 ("¿perdió información psicológica?", "¿conserva agencia perceptiva?") → preguntas fijas de VERIFY en MICROEDICION sección A.
- La sección de autocrítica de M3/M4 (cambio que más dudas genera, cambio más agresivo, caso protegido a último momento, riesgo de esterilización) → MICROEDICION sección F, ahora obligatoria.
- "Detenerse al entregar este reporte" (cierre explícito de M3 y M4) → MICROEDICION sección G.

## G. Decisiones descartadas

- Cuotas de tics o reducción por porcentaje/palabra — explícitamente prohibido (EDITORIAL_POLICY sección J), como pedía el encargo.
- Políticas específicas por palabra o construcción ("prohibido *como si*", "prohibido *demasiado*") — rechazado; M3 demostró que la función depende del contexto, no de la palabra.
- Meter toda la lógica editorial en `CLAUDE.md` — rechazado; solo una línea de referencia, el método vive en `12_Craft_Policies/editorial/`.
- Duplicar canon, fichas o citas concretas del manuscrito dentro de la skill — rechazado; la skill apunta a las políticas y al vault, no repite contenido.
- Reescribir `DO_NOT_TOUCH.md` desde cero — rechazado; ya cubre correctamente canon, diálogo, beats, cronología, revelaciones, consecuencias, objetos recurrentes, progresión Cole/Chiara y rareza de voz deliberada (vía "convertir rarezas de voz en español neutro genérico"). Se revisó explícitamente contra los aprendizajes de M0–M4 y no apareció ninguna frontera nueva que perteneciera ahí en vez de a `MICROEDICION.md`.

## H. Riesgos

- **Duplicación potencial:** `EDITORIAL_POLICY.md` sección A (repetición) y `MICROEDICION.md` sección C (categorías de repetición) se solapan a propósito — una es principio, la otra es taxonomía operativa. Si una cambia, revisar la otra.
- **Ruta de la skill sin verificar en producción:** se confirmó el formato de `SKILL.md` contra un ejemplo instalado del propio harness, pero esta es la primera skill de proyecto en este vault; no se probó invocación real en esta sesión.
- **`tools/editorial/README.md`** (auditor determinista) no se tocó y sigue hablando de `audit_only`; sigue siendo insumo válido para el modo AUDIT pero no fue actualizado para mencionar el nuevo `MICROEDICION.md`. No se detectó contradicción, solo falta de referencia cruzada — no se consideró necesaria para este encargo.
- **`PILOT_01_10.md`** dice que "hasta esa calibración no se autoriza Fase 2 ni una skill de Claude". Verificado en `log.md` (2026-08-30): la calibración V1.1 corrió, pero quedó explícitamente "pendiente revisión de ChatGPT + autor antes de Fase 2" — no hay entrada posterior que confirme el cierre de esa revisión. Se interpretó que esa condición se refiere a automatizar el auditor determinista (`tools/editorial/`) como corrector, no a una skill de método manual como `editorial-surgery` — las microediciones M0–M4 que motivan este encargo ya se ejecutaron manualmente sin pasar por Fase 2. Si el autor entendía que la condición cubría también esta skill, hay que tratarla como borrador hasta que confirme el cierre de la revisión V1.1.

## Estado

Sistema editorial formalizado. Sin commit ni push. Ninguna prosa, ficha, hito, timeline o EPUB tocados. No se inició microedición nueva. Detenido tras este reporte.
