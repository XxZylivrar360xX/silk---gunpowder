# SURGERY C21 — El mirador

**Fecha:** 2026-09-12. **Agente:** Claude Code. **Encargo:** ejecutar la edición localizada ya diagnosticada en [[98_Agent_Handoff/sessions/2026-09-09_codex_revision_editorial_cap_21]], respetando las decisiones autorales fijadas para seguridad/consentimiento y drift. Sin nueva auditoría, sin AUDIT/CLOSE/VERIFY formal, sin M5/M6.

## Hallazgo inicial

Antes de tocar una sola línea, se leyó el capítulo completo ([[11_Books/Book_01_Seda_y_Polvora/Part_01_Dos_Mundos/21_El_Mirador]]) y su comentario de cabecera. El comentario y `CURRENT_BRIEF.md` (entradas del 2026-09-10, bajo "REVISIÓN EDITORIAL CAP. 21") documentan que **la totalidad de la cirugía pedida en este encargo ya fue ejecutada el 2026-09-10** por Claude Code, con las mismas decisiones autorales que trae este encargo (conservar núcleo de seguridad, no invertir drift, no tocar Hitos.md más allá de la sincronización documental ya hecha entonces).

Se contrastó línea por línea cada instrucción del encargo contra la prosa vigente. Resultado: **cero intervenciones nuevas requeridas.** El archivo en disco (rama `develop`, árbol limpio al inicio de la sesión) ya cumple todos los puntos.

## Intervenciones

Ninguna. Todo lo pedido ya estaba aplicado:

| Zona | Estado verificado |
|---|---|
| Posición física post-beso («Se levantó») | Ausente. Texto actual: «Le tomó la mano. Cole la siguió sin que hiciera falta preguntar hacia dónde...» |
| Sintaxis «Lo vi el marcador» | Ya dice «Lo vi en el marcador.» |
| Pinos «torpes pero de pie» | Ya dice «Cuatro pinos cayeron.» sin contradicción. |
| Concordancia «un chuza limpio» | Ya dice «una chuza limpia.» |
| Duplicación de sonrisa | Una sola descripción cerca del beso («Le salió la sonrisa que no calculaba, la misma que Cole ya había aprendido a distinguir de todas las demás»). «Yo también» y «Solo quería oírtelo decir» intactos. |
| Botella | Ya es inequívoca: «La botella que habían comprado era un Chiaretto de Bardolino, rosado de verdad...» |
| Golf, búnker | Ya dice «el búnker del octavo hoyo», coincide con el ancla de C19. |
| Apertura «Estás en otro lado» | Ya anclada: «Chiara lo notó una noche en el casino, antes de que él dijera nada.» |
| Bolera (glosas negocio/dinero/poder, «dejó de importarle perder») | Ausentes. Juego, apuestas tontas, papas, risas y aplausos intactos. |
| Penthouse (glosas «no necesitaba traducción», copas que no van a terminar) | Ausentes. Canciones, rosado, espejo, proximidad y atmósfera intactos. |
| Baile («Dos personas que negociaban con criminales...») | Ausente. Mano, torpeza, balanceo, iniciativa e intimidad intactos. |
| Beso/dormitorio (glosas «llevaban meses siendo cuidadosos», «certeza tranquila... ya habían decidido semanas atrás») | Ausentes. Núcleo «¿Seguro?» / «Llevo meses seguro» intacto; línea de cierre de seguridad en L220 conservada tal como el autor la resolvió el 2026-09-10. |
| Drift (hablantes) | Prosa sin tocar; no se invirtió nada. |
| H11 / Hitos.md | No se tocó en esta sesión (ya se había sincronizado el 2026-09-10). |

## Decisiones autorales respetadas

- Seguridad explícita: conservada.
- Drift: prosa actual conservada, no invertida.
- H11: no modificado en esta sesión.

## Resultado

- Errores objetivos resueltos: sí (ya lo estaban).
- Continuidad menor resuelta: sí (ya lo estaba).
- Glosas localizadas reducidas: sí (ya lo estaba).
- Baile preservado: sí.
- Consentimiento preservado: sí.
- Otras zonas modificadas: ninguna.
- Lifecycle: sin cambios (sigue BORRADOR).
- EPUB: no regenerado.
- Commit/push: ninguno.

## Housekeeping de esta sesión

- Creado este archivo de sesión.
- Actualizada `98_Agent_Handoff/CURRENT_BRIEF.md` con nota de reconfirmación.
- Corregida la entrada obsoleta de Cap. 21 en `PENDING.md` (decía «manuscrito sin modificar», desactualizada desde el cierre del 2026-09-10) a «SURGERY aplicada; pendiente VERIFY/CLOSE.»
- No se marcó la deuda como resuelta; no se cambió lifecycle del capítulo.

## Autocrítica

No aplica autocrítica de intervenciones (MICROEDICION sección F) porque no hubo intervenciones nuevas en esta sesión — el trabajo real fue verificación documental, no cirugía. El riesgo principal era el opuesto: aplicar de oficio una segunda ronda de cortes sobre una prosa ya podada, lo cual habría violado EDITORIAL_POLICY sección J (no perseguir cuotas) y sección K (no esterilizar). Se optó por no inventar correcciones para justificar la sesión, conforme a EDITORIAL_POLICY sección I.

## Siguiente paso

`VERIFY C21` — sigue siendo el paso pendiente real, ahora sin trabajo de SURGERY bloqueándolo.
