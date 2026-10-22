# 2026-10-22 — Retitulado (segunda ronda) y numeración corrida del Libro I

**Agente:** Claude Code (orquestador) + tres subagentes (sustitución, verificación, renumeración). Sin commit.

## Decisiones del autor

- **Regla de títulos:** cada título sale de una palabra o frase del capítulo que pesa distinto al terminarlo. Propuesta y tabla: [[11_Books/Book_01_Mascaras_De_Cristal/00_Propuesta_Titulos]].
- **Retitulados (número nuevo, archivo):** 12 (10) *Los muchachos comen* · 17 (15) *Yo lo llevo* · 19 (17) *Le quedé debiendo* · 21 (19) *Lo que nadie estaba mirando* · 22 (20) *Lo pequeño* · 25 (23) *Nada caro* · 31 (27) *Lleve equipaje* · 32 (28) *No hace falta* (de "*Cielo*, no hace falta"; *Te queda grande* duró un día) · 33 (29) *Una silla* · 37 (33) *Lo único que es mío* · 54 (49) *Por si vuelve*.
- **Probados y revertidos a la primera ronda (2026-09-20):** 18 (16) *El sobre rojo* · 20 (18) *El día nublado* · 23 (21) *El primer huésped* · 24 (22) *Causalidad*.
- **Se mantienen:** 36 (32) *Línea directa* · 44 (39) *Un par de días más* · 45 (40) *Mecánico*.
- **Numeración corrida definitiva:** 56 capítulos, `# Capítulo N — Título` en todos; archivos sin renombrar. Tabla archivo → capítulo en [[11_Books/Book_01_Mascaras_De_Cristal/00_Book_Map]].

## Qué se tocó

- Encabezados de los 56 capítulos y nota de retitulado/renumeración en su comentario de metadata; prosa intacta (verificado por diff).
- Book_Map, CHAPTER_STATUS, Timeline del Libro I, BRIEF, PENDING, INDEX y la regla de supersesión de CLAUDE.md a numeración nueva.
- Aviso de numeración anterior en Hitos, planes del Libro I, matrices y 45 fichas; títulos viejos actualizados en fichas de Valenti, Elenna, Connors, Nadir, Dario, La Ronda, y en dos planes del Libro II.
- EPUB/PDF: prueba en carpeta temporal, 56 capítulos en orden; no se regeneraron los oficiales.

## Pendientes

- Las referencias `archivo:línea` de PENDING se corrieron una línea por la nota insertada en cada capítulo.
- La Timeline del Libro I no menciona el Cap. 38 *La mano*.
- Regenerar EPUB/PDF cuando el autor lo pida.
