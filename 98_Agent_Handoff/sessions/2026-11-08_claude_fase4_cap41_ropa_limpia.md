# Fase 4, nuevo 41 *Ropa limpia* (archivo 45): ajuste al cauce y poda

Fecha: 2026-11-08. Terminal A, Claude Code. Encargo: [[98_Agent_Handoff/encargos/ENCARGO_Fase4_Parte_III_Cierre]]. Verbo: «Ajusta al cauce». La poda se hizo con la skill `editorial-surgery`, en modo SURGERY y sólo dentro del 41.

## Qué se hizo

- Revisión contra el nuevo 39 (la puerta del sábado 18, en escena), el 35 (el plato de Acción de Gracias, *La Notte Bellandi*), el 38 («Se acabó tu parte») y el calendario del nuevo 40.
- Versión anterior íntegra: [[11_Books/Book_01_Mascaras_De_Cristal/Escenas_Eliminadas/45_Ropa_Limpia_Version_2026-11-08]].
- Conteo de prosa (wc): 4,492 → 4,339.
- Metadata: «Cap. NN» pasados a la numeración de 47 y ventana temporal ajustada.

## Decisiones del autor (CANON, 2026-11-08)

1. **Poda media.** Se aplicaron −183 palabras: Krane sin diálogo (se queda la solicitud federal), la redundancia «cobran cada dos semanas», el cierre de Kenji, el delantal de Mabel, el billete, las dudas del recepcionista, el mármol repetido, el resumen de la lavandería ante Bonnie, «Bonnie no dijo nada. Chiara tampoco.», la glosa de la garganta y la espera del volante. **No llega a ~3,950**: lo que queda es geografía protegida (DO_NOT_TOUCH) o beats con carga. Candidatos que todavía se pueden cortar, cada uno con su costo, para que decida el autor (unas 230 palabras en total):
   - el cierre de la mañana con Kenji, «Que tenga buen día… No era lo que decía siempre» (~45; se pierde la señal de que va a ayudar);
   - la fila de contratistas con gafete (~45; se pierde la imagen que planta a Kenji);
   - el párrafo del día en el despacho (~60; se pierde el residuo institucional del 40);
   - parte de la logística de Mei-Lin (~40; se adelgaza «horarios del lote»);
   - «Mei no lo dijo para molestarla / Fue una buena pregunta» (~25; se pierde el cobro de la pregunta).
2. **Eco de Mabel:** «La última comida de Mabel le había llegado en papel aluminio, de manos de Kal, un jueves de Acción de Gracias.» (después de «No has comido.»).
3. **Hueco de la etiqueta:** Kal entra el 19 y MERCER aparece hasta las noches del 27 y el 28. Se queda mudo; la respuesta llega en *Voto de Ceniza*, junto con la liberación.
4. **Vento** no entra.

## DISEÑO del agente

- El capítulo arranca el **lunes 20 dic** (antes era el miércoles 22), siguiendo al nuevo 40. Kenji, «día de pago», y la nómina del fin de semana cuadran con un lunes. «Hace tres días que no viene» (Mabel, martes 21) cuadra si Kal desayunó ahí por última vez el viernes 17.
- La hoja de salida lleva boca abajo «desde el domingo de la semana anterior» (antes decía «desde hacía una semana»).

## Comprobaciones de cauce (limpias)

Halbrook, Crowe, Matteo y la incursión no aparecen. Mei-Lin sólo aporta oficio y su pregunta ambigua, sin adelantar F2. Lucía «no llamó» y no hay jefe de policía. La grabación cuadra con el 39 (19:04, de espaldas; en el 39 Kal mueve los labios y la cámara no los ve).

## Para propagar (lo hace la terminal principal)

- `00_Mapa_Cauce_Cap11_Camp_Alder.md` («Avance de la Fase 4»): nuevo 41 ajustado (Chiara, ~4,340, del lunes 20 al miércoles 29 dic, eco del plato, hueco de la etiqueta mudo).
- `12_Craft_Policies/CHAPTER_STATUS`: archivo 45, BORRADOR, ajustado al cauce y podado el 2026-11-08.
- `01_Timeline/02_Libro_01_Mascaras_De_Cristal.md`: la fila de *Ropa limpia* empieza el lunes 20 dic.
- `13_Auditorias/Book_01_Mascaras_De_Cristal/Matriz_Temporal_Libro_I.md`: la «semana extra de custodia» (22–29) pasa a ser del 20 al 29.
- `02_Characters/Mabel_Ortiz.md`: el eco del plato de Acción de Gracias en el nuevo 41.
- `12_Craft_Policies/revelations/Book_01_Mascaras_De_Cristal.md`: el hueco de la etiqueta (19 → 27 dic) queda como misterio deliberado hasta *Voto de Ceniza*.
- PENDING: la decisión sobre los ~230 de poda opcional que quedan.
- Brief/log: una línea con el enlace a esta nota.

## Costuras

- **41 → 42 (B):** la ropa doblada en cuadro, «Antenoche y anoche», y «Mis compañeras dicen que es militar. Yo digo que alguien le enseñó.» no cambian. Walt puede leerla tal cual.
- **41 → 47 (C):** **la grabación no cambia.** Chiara la manda borrar, sin copia. Si el expediente del 47 trae un fotograma, alguien lo copió antes del borrado. El ledger («La grabación borrada y el fotograma») **prohíbe explicar en el I cómo llegó**: el 47 sólo lo muestra.

**Propagado** el 2026-11-08 en esta misma terminal, por orden del autor: mapa, CHAPTER_STATUS, timeline, matriz temporal, Krane, Rivers & Krane, Connors, Mabel, ledger, PENDING, brief, log y `--estado`.
- **41 → 46 (C):** el beat de recepción («subió y no tocó») ya está en el 41 y tiene que salir del archivo 50.
- 40 → 41: el 41 abre con «Puedo averiguar si lo trasladan», que es la última línea del 40. Cerrada.

audio PENDIENTE: archivo 45

## Revisión de costuras 40–47 (2026-11-08, después del commit a942a56)

- **41 → 42 (ropa doblada):** cuadra. «Salió el lunes en la noche. El martes también.» Corregí la metadata del 42: su ventana decía «horas después del amanecer en el Cutoff» (mié 29) y es el **jue 30**, como dicen la costura y el timeline. La prosa no cambia.
- **41 → 47 (grabación):** cuadra. El fotograma coincide con el 41 (19:04, de espaldas, chaqueta oscura, «ancho en las orillas»), y «La grabación de la que salió ese cuadro ya no existía» no explica la copia, como pide el ledger.
- **43 → 45/46 (cuenta abierta):** cuadra. Una sola deuda, «lo que él quiera, cuando él quiera», y el 40 («ya le debía uno») la anticipa.
- **44 → 46 (Rafe, Mabel):** cuadra. Cerré la costura PROVISIONAL en la metadata del 46.
- **Calendario 40–46:** dom 19 · lun 20–mié 29 · jue 30 · vie 31 · sáb 1–lun 3 · lun 3–mar 4 · mar 4 de noche (el convoy de Lucía, «el martes en la noche»). Sin choques.
- **Para la lectura (no es un defecto):** en el 46, Chiara tiene «Lucía Varek, el número directo, el de verdad». En el 40 no lo tenía; le queda de la llamada de Lucía en el 43.
