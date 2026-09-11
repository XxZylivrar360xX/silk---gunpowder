# Ciclo de vida del capítulo

Cómo un capítulo pasa de prosa usable a capítulo cerrado. Es agnóstico al agente: sirve igual para Claude, Codex o el autor leyendo solo.

Este documento no diagnostica ni interviene prosa — eso lo hacen [[12_Craft_Policies/editorial/EDITORIAL_POLICY]] y [[12_Craft_Policies/editorial/MICROEDICION]]. Este documento responde una pregunta distinta: **¿en qué estado está el capítulo, y qué falta para que avance?**

---

## Principio central

> **Los agentes certifican condiciones. El autor declara terminado.**

> **No encontrar más problemas no da autoridad para cerrar el capítulo.**

Un agente puede confirmar que ya no existe una razón objetiva conocida para seguir editando. Solo el autor puede decidir que el capítulo está cerrado.

---

## Estados oficiales

### BORRADOR

Existe prosa usable. Puede seguir recibiendo ajustes estructurales autorizados, continuidad, redacción, microedición o decisiones del autor.

BORRADOR no significa "malo". Significa: **todavía está abierto.**

### REVISADO

Estado opcional/intermedio. Significa: pasó una revisión sustantiva concreta, pero todavía existen gates o decisiones pendientes.

No es estación obligatoria. Un capítulo puede pasar de BORRADOR → LISTO PARA AUTOR directamente si cumple los gates sin necesitar REVISADO.

### LISTO PARA AUTOR

Todos los bloqueadores técnicos conocidos están cerrados. El agente considera que ya no existe una razón objetiva conocida para seguir editando antes de la lectura final del autor.

LISTO PARA AUTOR ≠ TERMINADO. El agente solo certifica: "puedes decidir si esto se cierra".

### TERMINADO

Solo puede asignarse tras aprobación explícita del autor. Ningún agente puede promover unilateralmente un capítulo a TERMINADO.

Ejemplos válidos de autorización: "aprobado", "queda terminado", "cerramos este capítulo", o equivalente inequívoco. No inferir aprobación por silencio.

### CONGELADO

Capítulo TERMINADO que pertenece a una unidad editorial ya cerrada (Parte, Libro, u otro bloque expresamente congelado por el autor).

No se reabre por mejora estilística oportunista. Solo por: error objetivo, contradicción de continuidad descubierta después, cambio explícito de canon, cirugía estructural expresamente autorizada, o solicitud directa del autor. Que exista una frase potencialmente "mejor" no es razón suficiente.

---

## Gates para LISTO PARA AUTOR

Matriz simple. No convierte el capítulo en checklist gigante — la evidencia detallada vive en session reports, no en el capítulo.

### Gate A — Estructura

Confirmar: el capítulo cumple una función identificable; cambia poder, relación o ambos cuando corresponde; deja consecuencia; ocupa la posición correcta en el arco; no existe cirugía estructural abierta conocida.

Si existe problema estructural: **BLOCKED**. No intentar solucionarlo mediante microedición.

### Gate B — Continuidad

Confirmar, según aplique: cronología, canon, conocimiento de personajes, orden de revelaciones, relaciones, objetos recurrentes, seeds, callbacks, consecuencias previas.

No exige releer todo el vault. Usar los ledgers e índices correspondientes ([[12_Craft_Policies/revelations/Book_01_Seda_y_Polvora]], [[12_Craft_Policies/milestones/INDEX]], `06_Relationships/Hitos.md`).

### Gate C — Voz y focalización

Confirmar que no existe un bloqueador conocido en POV, voz del narrador cercano, diálogo, sistema perceptivo, homogeneización de personajes.

No exige eliminar toda irregularidad estilística.

### Gate D — Editorial

Confirmar que no quedan problemas editoriales significativos conocidos, aplicando [[12_Craft_Policies/editorial/EDITORIAL_POLICY]].

Este gate **no significa iniciar una nueva auditoría completa**. Si el capítulo ya pasó la revisión editorial prevista, revisar el reporte existente.

### Gate E — Dependencias

Confirmar: decisiones pendientes relevantes registradas; ninguna dependencia futura conocida rota; ninguna semilla crítica sin ledger cuando debía registrarse; ningún callback importante perdido por una edición.

Un pendiente documentado que deliberadamente pertenece al futuro **no** bloquea. Un pendiente sobre la propia versión actual del capítulo **sí** puede bloquear.

### Gate F — Higiene

Confirmar: sin residuos de prompt; sin placeholders accidentales; sin notas internas filtradas al cuerpo; sin contradicción entre header y estado real; metadata operativa coherente.

---

## Resultado del check

### READY_FOR_AUTHOR

Todos los gates aplicables están verdes. Puede promoverse a `Estado: LISTO PARA AUTOR`. La promoción puede hacerla el agente si el encargo autorizó explícitamente la comprobación/cierre técnico. Nunca a TERMINADO.

### BLOCKED

Existe al menos un bloqueador real. Debe reportarse: gate, bloqueo, evidencia mínima, acción requerida. No iniciar automáticamente la acción correctiva salvo que el encargo también la autorice.

---

## Workflow CLOSE

CLOSE no es una cuarta modalidad de microedición (esas son AUDIT/SURGERY/VERIFY, ver [[12_Craft_Policies/editorial/MICROEDICION]] sección A). Es una certificación de madurez del capítulo.

Su pregunta es: **¿está este capítulo en condiciones de ser presentado al autor como terminado?**

### CLOSE debe

1. Identificar el capítulo.
2. Leer su estado actual.
3. Revisar reportes existentes pertinentes (session files, reportes editoriales).
4. Revisar pendientes conocidos.
5. Comprobar los gates A–F.
6. Hacer una lectura final orientada a detectar **bloqueadores**, no oportunidades de mejora.
7. Emitir READY_FOR_AUTHOR o BLOCKED.

### CLOSE no debe

- Hacer una nueva microedición general.
- Buscar tics por iniciativa propia.
- Reescribir frases porque "podrían quedar mejor".
- Abrir cirugía estructural.
- Modificar canon.
- Regenerar EPUB.

---

## Descubrimiento durante CLOSE

Si CLOSE encuentra algo, clasificarlo antes de actuar:

### Error mecánico objetivo

Ejemplo: typo, residuo de prompt, placeholder accidental. Puede reportarse. Solo corregirse si el alcance del encargo permite correcciones mecánicas.

### Posible mejora editorial

No corregir automáticamente. Registrar como `CANDIDATO — NO BLOQUEANTE` si realmente no impide cerrar.

### Bloqueador

Emitir `BLOCKED` y detener la promoción.

---

## Bloqueante vs. no bloqueante

No todo hallazgo impide cerrar.

**Bloqueante:** contradicción de canon; motivación rota; escena necesaria ausente; revelación anticipada; POV roto de forma sustantiva; pendiente autoral que define el contenido actual; placeholder; callback crítico destruido.

**No bloqueante:** alternativa estilística equivalente; frase que podría comprimirse pero funciona; pequeña repetición no problemática; preferencia estética; optimización opcional.

> **Un capítulo no necesita ser imposible de mejorar para estar terminado.**

---

## Metadata

Sin matrices YAML ni docenas de flags. La fuente visible principal sigue siendo la línea `Estado:` ya existente en el header HTML del capítulo (ver convención vigente, p. ej. `Estado: borrador provisional.` en capítulos ya escritos), con uno de estos cinco valores:

- `Estado: BORRADOR`
- `Estado: REVISADO`
- `Estado: LISTO PARA AUTOR`
- `Estado: TERMINADO`
- `Estado: CONGELADO`

La evidencia de gates vive en el session report, en `98_Agent_Handoff/CURRENT_BRIEF.md`, y en el ledger de cierre si se usa (ver abajo). No se duplica el análisis dentro del propio capítulo.

---

## Ledger central — decisión

Se creó [[12_Craft_Policies/CHAPTER_STATUS.md]] como ledger compacto porque ni `00_Book_Map.md` ni `INDEX.md` llevan hoy una tabla capítulo-por-capítulo de estado editorial (ambos son prosa narrativa de seguimiento, no una tabla escaneable). El ledger no duplica análisis — solo referencia dónde vive.

**No se pobló retroactivamente.** Este encargo crea el sistema; no audita C01–C29. Un encargo separado de auditoría de estados / cierre de Parte I decidirá cómo poblarlo.

---

## Integración con `Redaccion_De_Capitulos.md`

Al final del flujo de redacción: capítulo usable → `Estado: BORRADOR` → ver este documento para cómo avanza de ahí.

## Integración con `MICROEDICION.md`

AUDIT diagnostica. SURGERY interviene. VERIFY comprueba una cirugía. **CLOSE certifica madurez del capítulo** — pertenece al lifecycle, no a la microedición.

## Integración con la skill `editorial-surgery`

La skill reconoce cuando el usuario pide cerrar, aprobar técnicamente o comprobar si un capítulo está listo; en ese caso carga este documento y ejecuta el workflow CLOSE en vez de (o antes de) AUDIT/SURGERY/VERIFY. Nunca traduce READY_FOR_AUTHOR como TERMINADO.

---

## Autoridad

| Acción | Agente | Autor |
|---|---:|---:|
| Mantener BORRADOR | Sí | Sí |
| Marcar REVISADO | Sí | Sí |
| Marcar LISTO PARA AUTOR | Sí, con gates | Sí |
| Marcar TERMINADO | **No** | **Sí** |
| Marcar CONGELADO | Solo por workflow previamente autorizado | **Sí** |
| Reabrir CONGELADO por gusto estilístico | No | No |
| Reabrir por canon/error/orden expresa | Reportar | Sí |

---

## No retroactividad automática

Este documento crea el sistema de estados y el workflow CLOSE. **No se aplica todavía** a los capítulos ya escritos (C01–C29): ninguno cambia de estado como consecuencia de este encargo. La auditoría de estados / cierre de Parte I es trabajo futuro, separado y explícito.
