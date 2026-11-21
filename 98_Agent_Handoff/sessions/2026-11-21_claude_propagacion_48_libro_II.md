# 2026-11-21 — Libro II: propagación de la numeración de 48

**Agente:** Claude Code. **Orden del autor:** «Sí, propágala» (la Fase 1, aprobada el 2026-11-18 con 48 capítulos, no se había propagado).

## Resultado

- **[[11_Books/Book_02_Sombras_De_Poder/00_Book_Map]]:** tabla nueva de 48 (Parte, capítulo, qué absorbe, POV, archivo, número anterior) y equivalencia 58 → 48; la tabla de 58 queda plegada. Partes: I = 1–12, II = 13–26, III = 27–33, IV = 34–48. Se declara el bloque sin POV de Chiara de *Stavanger* (39) a *Torna a casa* (44) (regla 3 de perspectiva; DISEÑO).
- **Archivos:** conservan su nombre (convención del Libro I). Se retiraron con `git rm` nueve placeholders sin prosa que la Fase 1 funde o reparte: `03_Bellandi`, `07_El_Farol`, `11_Capacidad`, `14_Senor_Militar`, `16_El_Otro_Dario`, `24_La_Jaula`, `32_Vacio`, `40_Una_Sola_Frase` y `51_La_Fecha`. Su carga quedó anotada en el comentario del placeholder que la absorbe y en la ficha tachada de la guía.
- **Stavanger + Henrik:** la prosa de `Henrik.md` va tal cual al final de `Stavanger.md`, tras un `***`, y `Henrik.md` se retiró. Sin reescribir. Cap. 39 (~2,600 palabras); *Ya llegó* es el 40.
- **Cabeceras:** el número de capítulo de 48 en los placeholders que quedan y en la metadata `capitulo:` de los borradores.
- **Herramientas:** `tools/build_sombras.py` lleva 48 capítulos; `SELECTIONS` del audio, `total: 48` y los números nuevos (sin *Henrik*).
- **[[11_Books/Book_02_Sombras_De_Poder/00_Guia_Redaccion_Capitulos]]:** fichas, Partes, distribución, elipsis, tics, señales y POV ajenos en 48; cada ficha dice «antes N». Las fichas fundidas se conservan tachadas. **Las referencias dentro del texto de las fichas siguen en la numeración anterior** (aviso al inicio).
- **[[11_Books/Book_02_Sombras_De_Poder/00_Matriz_Temporal]]:** columna «Caps. (48)». La Parte III cierra ahora en el 33; la depresión y la frase de Mabel entran en el 34.
- Aviso de numeración en las cuatro tarjetas y en el mapa de la Fase 3; notas en la Fase 1, la columna, INDEX, DECISIONS (con rotación de «Fase 3 del Libro II» a [[98_Agent_Handoff/archive/2026-11-21_DECISIONS_retiradas]]), PENDING y el brief.

## Siguen abiertos (autor)

- Excepción de los tics 4 y 5 en capítulos seguidos (19 y 20, las dos velas).
- Señal 3 (el cigarro): sale o pasa al 41.
- De la columna: deuda personal de Mack Calderon con Crowe; motivo de Amanda; motivo de Manfred para entregar las cartas.
- Rehacer la guía con la columna nueva (Halbrook villano del tablero, Crowe caudillo de la calle); al hacerlo se traducen las referencias internas a 48.

## Verificación

`tools/build_sombras.py` y `build_audiobook.py` compilan; EPUB, PDF y audio regenerados en el cierre (`regenerar-y-subir`).
