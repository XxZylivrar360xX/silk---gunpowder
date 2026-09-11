---
name: editorial-surgery
description: Ejecuta auditoría editorial, microedición o verificación postoperatoria de prosa ya escrita en este vault (redundancia, sobreexplicación, glosa, tics, presagio garantizado, verificación de una cirugía previa). No se activa para redacción inicial, brainstorming, canon, diseño estructural, merge de capítulos, continuidad macro, generación de EPUB o diálogo exclusivamente.
user-invocable: true
---

# Cirugía editorial

Método para juzgar y, cuando el encargo lo autoriza, intervenir prosa ya escrita en `10_Chapters/` o `11_Books/`. Esta skill contiene **método**, no verdad del proyecto: no duplica canon, fichas de personaje, hitos, secretos ni timeline. Esos siguen viviendo en el vault y se leen aparte, bajo demanda.

## Cuándo se activa

Sí: auditoría editorial, microedición, cirugía de prosa, revisión de redundancia o sobreexplicación, verificación postoperatoria, análisis transversal de tics o patrones de estilo, o una petición de **cerrar, aprobar técnicamente o comprobar si un capítulo está listo** (workflow CLOSE).

No: redacción inicial de capítulo, brainstorming de trama, canon, diseño estructural (fusionar capítulos, mover escenas, cambiar orden, crear beats, resolver motivaciones, reestructurar arcos), continuidad macro, generación de EPUB, o una tarea que es solo diálogo/canon sin componente de edición de prosa existente.

Si en medio de una tarea de esta skill aparece un problema estructural (motivación rota, continuidad rota, un arco que necesita reordenarse), **repórtalo y detén la intervención editorial en esa zona**. La cirugía estructural es otro rol; no se resuelve aquí.

## Arranque

1. **Identifica el modo:** AUDIT, SURGERY, VERIFY o **CLOSE**. Si el encargo no lo dice explícitamente, pregúntalo antes de leer nada más — el modo determina si vas a tocar prosa. Un pedido de "¿está listo este capítulo?", "cierra el capítulo X" o "aprueba técnicamente X" es CLOSE, no AUDIT.
2. **Identifica el ámbito autorizado:** qué capítulos, qué patrón, qué rango de líneas. No lo des por hecho; si es ambiguo, pregunta.
3. **Lee, en este orden:**
   - [[12_Craft_Policies/editorial/EDITORIAL_POLICY]] — qué se busca y qué principios rigen la decisión.
   - [[12_Craft_Policies/editorial/DO_NOT_TOUCH]] — qué está fuera de alcance sin importar el hallazgo.
   - [[12_Craft_Policies/editorial/MICROEDICION]] — el procedimiento: modos, clasificación de candidatos, árbol de decisión, protecciones deliberadas, autocrítica.
   - Si el modo es **CLOSE**: además [[12_Craft_Policies/CHAPTER_LIFECYCLE]] — estados oficiales, gates A–F y el workflow CLOSE. Ejecútalo tal como está definido ahí. **Nunca traduzcas READY_FOR_AUTHOR como TERMINADO** — solo el autor declara TERMINADO.
4. **Solo después**, carga lo específico de la tarea y nada más:
   - la(s) ficha(s) de `12_Craft_Policies/voice/` de los personajes cuya voz está en juego;
   - la sección relevante del ledger de revelaciones (`12_Craft_Policies/revelations/`) si el pasaje toca secretos o información retenida;
   - el/los hito(s) de `06_Relationships/Hitos.md` si el pasaje ejecuta uno;
   - los capítulos exactos autorizados — completos si el encargo compara apariciones a lo largo de ellos (ver MICROEDICION sección B, lectura antes de editar).
5. **No leas de más.** No abras `log.md` completo, `CURRENT_BRIEF.md` entero más allá de lo necesario para orientarte, ni capítulos fuera del ámbito autorizado. Sigue las políticas de ahorro de contexto de `CLAUDE.md` del vault.

## Ejecutar el modo

Sigue la definición operativa de cada modo en [[12_Craft_Policies/editorial/MICROEDICION|MICROEDICION]] sección A. En resumen:

- **AUDIT** no toca prosa. Entrega mapa de hallazgos, candidatos clasificados (MICROEDICION sección C), casos protegidos y riesgos.
- **SURGERY** toca prosa solo dentro del ámbito autorizado, y solo tras pasar cada candidato por el árbol de decisión (MICROEDICION sección D). Cada intervención se documenta con before/after, categoría, razón, qué ya hacía la escena y qué conserva la versión nueva.
- **VERIFY** no reabre una ronda general; evalúa una cirugía ya hecha contra las preguntas fijas de MICROEDICION sección C (VERIFY).
- **CLOSE** no toca prosa salvo error mecánico objetivo dentro de alcance. Comprueba los gates A–F de [[12_Craft_Policies/CHAPTER_LIFECYCLE]] y emite READY_FOR_AUTHOR o BLOCKED. No es una pasada de mejora: busca bloqueadores, no oportunidades.

## Al cerrar

- Si la tarea fue AUDIT o SURGERY con más de una intervención, incluye la autocrítica obligatoria (MICROEDICION sección F).
- Documenta protecciones deliberadas cuando el alcance lo amerite (MICROEDICION sección E) — no solo lo cortado.
- Detente. No inicies una segunda pasada porque el archivo sigue abierto (MICROEDICION sección G); una nueva ronda necesita nueva autorización del autor.
- Actualiza `98_Agent_Handoff/CURRENT_BRIEF.md` y, si cambió el estado editorial de un capítulo, `log.md` — según el protocolo normal del vault, no algo específico de esta skill.
- No regeneres el EPUB como parte de esta skill.

## Qué no hacer nunca desde aquí

- No fabriques correcciones para justificar una pasada (EDITORIAL_POLICY sección I): una auditoría puede concluir que no hace falta ningún cambio.
- No persigas cuotas de tics, porcentajes de reducción o conteos de palabras como meta (EDITORIAL_POLICY sección J).
- No sustituyas una rareza de voz deliberada por prosa genérica limpia (EDITORIAL_POLICY sección K, DO_NOT_TOUCH).
- No copies aquí una cita concreta del manuscrito como si fuera regla permanente. Si necesitas un ejemplo para explicar una categoría, prefiere uno abstracto.
