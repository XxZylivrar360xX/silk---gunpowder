# 2026-11-21 — Ping-pong prohibido y barrido del Libro I

**DECISIÓN DEL AUTOR (2026-11-21):** desde hoy quedan prohibidos los diálogos ping-pong; las interacciones entre personajes se escriben como conversaciones. Registrado en la regla de diálogo 05 (umbral operativo; excepciones revocadas), la regla de puesta en escena 04, `CLAUDE.md`, `AGENTS.md` y `DECISIONS.md`.

## Herramienta

`tools/editorial/pingpong_audit.py` (sin dependencias, solo lectura): marca cinco o más réplicas seguidas de ≤14 palabras habladas, con beats de una línea en medio. `--book 2` para el Libro II.

## Barrido (BORRADOR, espera lectura del autor)

- Antes: **117 tramos en 31 archivos**. Después: **9 tramos en 4 archivos**, todos canon o protegidos (abajo).
- Cinco agentes, por bloques: 47–34, 33–22a, 20–07, 06–05a, 04–01. Los caps. 1–6 se hicieron después de que la sesión «Editorial Libro 1» commiteara su microedición (`b834809`), sin deshacerla.
- Técnicas de la regla 05: asimetría de largo según la ficha (Nadir calcula, Danny se encima, Blake contesta por ella, Lucía deja silencios, Fabrizio se contesta solo), turno perdido, réplicas fundidas, contestar otra cosa, gesto en lugar de réplica. Sin cambios de trama ni de orden de beats. Neto: −200 líneas aprox. (réplicas fundidas).
- **Corrección posterior:** un agente había reescrito tres pasajes protegidos; se restauraron literales: la ciabatta, «Ladro» y «Assaggia» del 33 (pago en Stavanger, CANON 2026-10-03), «¿Depende de qué?» del 3 (CANON 2026-10-04) y «El dentista no tiene un casino» del 4. Verificación: 271 citas canon de Hitos, DECISIONS, Kal_y_Chiara y Book_Map, sin pérdidas en los archivos tocados.

## Detalles menores inventados (revisar en lectura)

Caja de aceite de Russ y camión de la lavandería (4); «A mí me puso dos» de Walt sobre Keene y Nat «a esa hora» en la tumba (3); «tres personas que no se conocían entre sí» (12); Chiara aprendió de obras en italiano y Nadir «un tercio más» (10); «tarifa nocturna» del patrullero (8b); «En mi familia me dirían que no sé negociar» (7).

## Residual (DECISIÓN DEL AUTOR, 2026-11-21)

- **Quedan como excepción:** los ojos del 3; la vela del 12; «Ladro» del 33; H21 del 34 («Chiaraaa…» y «Mi pareja»).
- **Reescritos por orden del autor:** la ciabatta y «Assaggia» del 33; el inicio de la llamada de Danny y «Intenso» del 34. La ciabatta conserva sus líneas ancla, y *Ya llegó* (Libro II) espeja el texto nuevo para que el pago siga literal.
- Libro II sin barrer (51 tramos).

## Complemento: regla 06 «Réplica mínima» (DECISIÓN DEL AUTOR, mismo día)

- Evaluación: [[13_Auditorias/Book_01_Mascaras_De_Cristal/Audit_Dialogos_Cortos_Libro_I]]. Ficha de Kal replanteada («corto sobre sí mismo, largo sobre el mundo»); regla [[12_Craft_Policies/dialogue_rules/06-replica-minima]]; detector `--cortas`.
- Barrido en dos tandas (ocho agentes, 38 archivos): el libro pasa de **33 % a 26 %** de réplicas de ≤3 palabras; neto −200 líneas aprox. Sobre la vara del 25 % quedan, a propósito, capítulos con acción (8, 8b, 9, 43), con líneas decididas por el autor (4, 5a, 6, 20) o con texto protegido (33: la caja de Kenji y Marisol, la ciabatta, «Ladro», «Assaggia»).
- **Restaurados literales tras la revisión** (los encabezados los marcan como literales sin citar las líneas, y los barridos los habían tocado): la moto de Nadir del 24b; la llamada, las caballerizas, la botella y la llave del 36; «¿Qué haces aquí?» de la escena de Collins del 35.
- Detalles menores inventados por los agentes (revisar en lectura): ver los reportes resumidos en el chat del 2026-11-21; los más visibles: la caldera del loft (43), «Diez años comió a la hora que le dijeron» (1), los carritos del club (18), la tabla de centímetros del letrero (18), el peso de Chiara «en agosto» (40), la Ruta de Milla como comparación de Palermo (40).
- **PENDIENTE del autor:** dos tramos canon literales que son ping-pong: la moto de Nadir (24b, «Te lo pago / Ya sé / … / Te sale lo que costó») y la llave del 36 («¿Faltó más, verdad? Lo sabía.» / «No.» …).

