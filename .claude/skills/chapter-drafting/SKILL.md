---
name: chapter-drafting
description: Redacta prosa nueva de capítulo o escena en este vault (primer borrador, reescritura de una escena o capítulo completo a partir de estructura, beats o plan). Indica qué leer antes, qué reglas de oficio aplicar y qué actualizar después. No se activa para auditoría o microedición de prosa ya escrita (eso es `editorial-surgery`), brainstorming sin prosa, diseño estructural de libro, generación de EPUB ni cierre técnico de capítulo.
user-invocable: true
---

# Redacción de capítulos

Método para pasar de estructura a prosa en `11_Books/` (o `10_Chapters/`). Esta skill contiene **método y ruta de lectura**, no verdad del proyecto: canon, fichas, hitos, secretos y planes siguen viviendo en el vault y se leen bajo demanda.

## Cuándo se activa

Sí: escribir un capítulo o escena nuevos, redactar desde beats o plan, reescribir una escena completa por encargo del autor, convertir un boceto en prosa.

No: auditar, microeditar o verificar prosa existente (`editorial-surgery`); cerrar o aprobar un capítulo (workflow CLOSE en `editorial-surgery`); decidir estructura de libro, mover hitos o rellenar un PENDIENTE del autor.

Si la escena exige una decisión que el vault marca como **PENDIENTE**, no la resuelvas por conveniencia: márcala como provisional en la prosa y repórtala.

## Antes de escribir

1. **Ubica el capítulo:** libro, número, archivo y fase en el `00_Book_Map.md` del libro activo. Si el capítulo toca la escala del libro, lee el plan que manda (ver `CLAUDE.md`: `00_Trilogy_Structure.md` y, según el libro, `00_Plan_Arco_Final_Sin_Kal.md` o `00_Plan_Cuatro_Partes.md`).
2. **Comprueba el estado:** si el capítulo está SELLADO, CONGELADO o TERMINADO, no lo reescribas sin orden explícita del autor ([[12_Craft_Policies/CHAPTER_LIFECYCLE]]).
3. **Lee la política base:** [[12_Craft_Policies/Redaccion_De_Capitulos]] completa. Es corta y rige la unidad de capítulo, la apertura por residuo, el punto de vista, la exposición, el registro, las acotaciones, el registro privado de Kal y Chiara y la provisionalidad.
4. **Registro de lengua:** [[12_Craft_Policies/voice/00_Registro_Espanol_Neutro]]. Narración y diálogo en español neutro latinoamericano; respeta sus excepciones de voz.
5. **Carga solo lo específico de la escena:**
   - el final del capítulo anterior (para elegir el residuo de apertura);
   - la ficha de voz de cada personaje que habla (`12_Craft_Policies/voice/`); si no existe, créala primero;
   - la ficha de personaje y lugar cuando haga falta (`02_Characters/`, ciudad);
   - [[12_Craft_Policies/revelations/Book_01_Mascaras_De_Cristal]] (o el ledger del libro activo y `SAGA_LEVEL`) si la escena toca secretos, mentiras, pasado o información retenida;
   - [[12_Craft_Policies/milestones/INDEX]] y `06_Relationships/Hitos.md` si la escena ejecuta o depende de un hito;
   - `12_Craft_Policies/tonal_calibration/` si existe guía para ese capítulo.
6. **No leas de más:** nada de `log.md` completo ni capítulos fuera de los necesarios. Sigue las reglas de ahorro de `CLAUDE.md`.

## Mientras escribes

- Precedencia en conflicto (README de `12_Craft_Policies`): revelations > milestones > voice > dialogue/staging rules; `Redaccion_De_Capitulos` gobierna la unidad de capítulo.
- Respeta las reglas intocables de `CLAUDE.md` (la violencia cambia algo, la ciudad es lugar concreto, la relación es maquinaria del ascenso).
- El narrador no adelanta el futuro (EDITORIAL_POLICY sección L): nada de "no podía saber que…".
- Diálogo canon del autor se copia literal; no se reinterpreta ni se neutraliza.

## Antes de entregar

1. Repasa [[12_Craft_Policies/Redaccion_De_Capitulos]] sección "Unidad mínima": poder, relación, ciudad, consecuencia.
2. Repasa los anti-patrones de `12_Craft_Policies/dialogue_rules/` (si hubo diálogo emocional largo) y `12_Craft_Policies/staging_rules/`.
3. Revisa los regionalismos contra el glosario de registro neutro.
4. Marca el capítulo `Estado: BORRADOR`. Nunca lo declares TERMINADO.

## Al cerrar

- Si se sembró, reveló o pagó algo: actualiza `revelations/`. Si hubo hito irreversible: `milestones/INDEX.md`. Si una voz mostró un patrón nuevo real: su ficha.
- Corre `python -B ./tools/audiolibro/build_audiobook.py --estado` para marcar el audio PENDIENTE (sin red, no genera audio).
- Actualiza `98_Agent_Handoff/CURRENT_BRIEF.md`; si cambió canon o continuidad, también `log.md` e `INDEX.md`.
- No regeneres EPUB por un borrador.
- No hagas commit ni push salvo que el autor lo pida.
