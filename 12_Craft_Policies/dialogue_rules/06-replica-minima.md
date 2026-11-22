# Regla: Replica minima

**Tipo:** anti-patron de dialogo (complemento de la regla 05).
**Estado:** **DECISION DEL AUTOR (2026-11-21)**; redaccion del agente. Aplicada al Libro I el mismo dia (33 % → 26 %). Evaluacion que la motiva: [[13_Auditorias/Book_01_Mascaras_De_Cristal/Audit_Dialogos_Cortos_Libro_I]]. Va junto con el replanteamiento de la ficha de Kal ([[12_Craft_Policies/voice/Kal_Mercer]], «Economia, no mutismo»).

## El patron

La replica de tres palabras o menos usada por defecto: «Si.», «No.», «Lo se.», «¿Y?», «¿Cuando?», «Chiara.», «Mas o menos.». Una sola no es problema. El problema es cuando el libro entero contesta asi: en el Libro I era un tercio de las replicas (33 %). Suena a una sola maquina, casi siempre la de Kal, obliga al otro a interrogar (pregunta corta, respuesta corta) y quita el golpe a las cortas que si importan.

## Cuando se queda

Una replica de tres palabras o menos se justifica solo si cumple al menos una de estas:

1. **Decision o negativa** que cambia la escena («Si.» a la propuesta; «No.» que corta un plan).
2. **Rompe una serie larga**: llega despues de turnos con cuerpo y su brevedad es el golpe.
3. **Accion o peligro**: ordenes, gritos, radio, persecucion.
4. **Dato concreto**: un nombre, una hora, un objeto, una cifra que la escena necesita («Una cerca.»).
5. **Cortesia de mesa con un rival**: la frase plana como arma.

Si no cumple ninguna, se arregla.

## Como se arregla

1. **Darle contenido.** La replica dice lo mismo, pero entrega un dato, una razon o una vuelta de la voz de quien habla (ficha).
2. **Fundirla.** Juntarla con la replica anterior o la siguiente del mismo hablante, o con la del otro si ese turno sobra.
3. **Quitar la pregunta que la provoca.** Si el otro pregunta solo para sacarle la respuesta, la pregunta sobra: que siga con su agenda o que el que sabe lo suelte solo.
4. **Gesto que hace algo.** Sustituir la replica por una accion que cambie algo (regla de puesta en escena 04), no por un beat decorativo.
5. **Dejarla y ganarla.** Si es golpe, que lo sea: que llegue despues de turnos con cuerpo.

No inflar: el arreglo prefiere fundir y sustituir antes que alargar. La extension del capitulo no debe crecer mas de un 3 %.

## Vara

- Por capitulo, **como maximo un 25 %** de replicas de tres palabras o menos, sin contar escenas de accion. Referencia del propio libro: los capitulos mejor resueltos andaban entre 16 % y 23 %.
- Recursos secos con racion (ver ficha de Kal): el nombre solo como bisagra, una vez por capitulo; «Lo se» / «Ya se» como replica completa, evitar; «Si.» / «No.» solos, solo como decision.
- Medicion: `python tools/editorial/pingpong_audit.py --cortas` (porcentaje por capitulo). El numero es alarma, no veredicto: decide la lista de «Cuando se queda».

## Excepciones

- Lineas CANON DEL AUTOR: literales.
- Tramos aprobados por el autor el 2026-11-21 (regla 05): los ojos del Cap. 3, la vela del 12, «Ladro» del 33, los dos tramos de H21 del 34, la moto de Nadir del 24b y la llave del 36.
- Cap. 4 (archivo `04_Tarifa_Nocturna`) sobre la vara (33 % con la llamada, la rampa y Russ/Danny restituidos literales): excepcion aprobada por el autor el 2026-11-21, por la llamada, la rampa y la ventanilla. No obliga a recortar; la cirugia no debe subirlo.
- Cap. 5 (archivo `05a_Cliente_Y_Proveedor`) sobre la vara (32 %): excepcion aprobada por el autor el 2026-11-21 (la llamada de la factura, el elevador, la reunion y Kyle). La cirugia no debe subirlo.
- Cap. 7 (archivo `06_Ambos`) sobre la vara (34 %): excepcion aprobada por el autor el 2026-11-21 (H2-b: el reto, la ruleta, el tuteo, las canciones y el cierre; con los remates restituidos «Yo si», «¿Con cara?» y «Fue una noche rara»).

## Relacion con otras reglas

- `05-esticomitia-de-una-sola-voz.md`: la 05 mira la serie (ping-pong); esta mira la replica suelta.
- `01-interrogatorio-terapeutico-escalonado.md`: el par pregunta corta / respuesta corta es su version de bolsillo.
- `staging_rules/04-dialogo-de-guion-sin-anclaje.md`: el gesto que sustituye una replica tiene que hacer algo.
