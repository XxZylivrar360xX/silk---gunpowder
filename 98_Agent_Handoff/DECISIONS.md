# Decisiones recientes

Máximo 800 palabras; conservar sólo decisiones operativas recientes y enlaces a sus fuentes. El historial íntegro anterior al corte está en [[98_Agent_Handoff/archive/2026-09-21_DECISIONS]]; las del 2026-11-01, en [[98_Agent_Handoff/archive/2026-11-08_DECISIONS]]; las del 2026-11-04 al 2026-11-06, en [[98_Agent_Handoff/archive/2026-11-09_DECISIONS_retiradas]]; la Fase 3 del Libro II, en [[98_Agent_Handoff/archive/2026-11-21_DECISIONS_retiradas]]. Archivar entradas antiguas antes de retirarlas.

## 2026-11-21 — Diálogo ping-pong prohibido

**DECISIÓN DEL AUTOR:** desde hoy quedan prohibidos los diálogos ping-pong en toda la saga; las interacciones entre personajes se escriben como conversaciones. Se revocan las excepciones de la regla 05 y de la regla de puesta en escena 04. Umbral (cinco o más réplicas seguidas de ≤14 palabras habladas) y detector: [[12_Craft_Policies/dialogue_rules/05-esticomitia-de-una-sola-voz]], `tools/editorial/pingpong_audit.py`. Libro I en reescritura.

## 2026-11-21 — Libro II en 48 capítulos (propagado)

**DECISIÓN DEL AUTOR (2026-11-18), propagada el 2026-11-21:** la Fase 1 ([[11_Books/Book_02_Sombras_De_Poder/00_Fase1_Tres_Pruebas]]) deja el Libro II en **48 capítulos**: I = 1–12, II = 13–26, III = 27–33, IV = 34–48. Los archivos conservan su nombre (tabla y equivalencias en [[11_Books/Book_02_Sombras_De_Poder/00_Book_Map]]); nueve placeholders fundidos se retiraron y *Stavanger* y *Henrik* son un solo archivo, sin reescribir. Abiertos: la excepción de los tics 4 y 5 seguidos y la señal 3. Detalle: [[98_Agent_Handoff/sessions/2026-11-21_claude_propagacion_48_libro_II]].

## 2026-11-17 — Kal nunca deja de pagarle a Crowe (Libro II)

**DECISIÓN DEL AUTOR («Escenario 1»):** la cuota mensual de Kal a Crowe sigue hasta la muerte de Crowe (como en los caps. 45 y 55); la guerra de la Parte III nace de las noches de Kal contra la gente de Crowe, no de la deuda. Supera la (P) de «no la paga hasta saber» (cap. 32). [[98_Agent_Handoff/sessions/2026-11-16_claude_lote1_integracion]]

## 2026-11-13 — El arco de Meiko en cuatro capítulos (Libro II, 57 caps.)

**DECISIÓN DEL AUTOR:** el antiguo 36 se parte en *Las latas* (36, Kal) y *Lo del hermano* (37, Kal); siguen *Perdóname, jefe* (38, Nadir) y *Lo que queda* (39, ahora de Chiara). Todo lo demás sube uno: Parte III 32–40, Parte IV 41–57. **CANON:** Kal le contesta a Meiko «—Eso ya no importa, estás aquí… con nosotros.»; no llora hasta decirle a Chiara «Iba a decirle que sin importar lo que tuvo que hacer, era de los míos.». Bonnie se va después del entierro; la tarde del entierro le dice a Chiara, que todavía le habla de planes, que no va a quedarse, y le cuenta la traición. Fuente: [[11_Books/Book_02_Sombras_De_Poder/00_Guia_Redaccion_Capitulos]].

## 2026-11-12 — El golpe fallido lo hacen los chicos (Libro II, 56 caps.)

**DECISIÓN DEL AUTOR:** el golpe fallido no es una venganza de Kal. Nadir organiza a los chicos sin decirle y los lleva contra los Calderos para cobrar a Meiko. Mueren inocentes; ningún chico muere (hay heridos); el Caldero sobrevive. Kal se entera tarde, los saca y deja la línea «Yo no voy a arriesgar a nadie para fundamentar una guerra» (siembra *Voto de Ceniza*). Nadir empieza así su separación voluntaria de la banda, a lo largo de la saga. Las bandas fijan la fecha de la tormenta sin Kal. La Parte IV queda en 17 capítulos y el libro en 56. El autor quiere vivir la tormenta desde Chiara (por diseñar). Fuente: [[11_Books/Book_02_Sombras_De_Poder/00_Guia_Redaccion_Capitulos]].

## 2026-11-12 — «Lo siento, ¿vale?» y Meiko en el final

**DECISIÓN DEL AUTOR:** F2 se queda en la Parte III. El final del Libro II la cobra con ecos de Kal y Chiara (recuerdos de Meiko o de aquel día), no con venganza ni de forma textual. «Lo siento, ¿vale?» va en el cap. 38: Kal vuelve del entierro y encuentra a Chiara rota en el suelo de la Villa, con la foto de la cena de Navidad (todos los chicos sonriendo). Kal se disculpa porque el código de su jerarquía costó una vida, y a Chiara le costó a Meiko y a Bonnie. La foto se siembra en el cap. 20. Resuelto el golpe fallido en la entrada de arriba. Fuente: [[11_Books/Book_02_Sombras_De_Poder/00_Guia_Redaccion_Capitulos]].

## 2026-11-12 — Columna del Libro II

**DECISIÓN DEL AUTOR:** se aprueba la columna de [[11_Books/Book_02_Sombras_De_Poder/00_Carretera_Libro_II]] (decisión 1): Crowe cobra en la calle, Kal absorbe las deudas de los suyos, Halbrook cosecha lo visible y Varek elimina en silencio con motivos propios; por dentro, cada cobro produce un secreto («estoy bien» / el papel). Las decisiones 2–14 siguen abiertas. Archivo: [[98_Agent_Handoff/archive/2026-11-12_DECISIONS]] (Chiara en *Sombras de Poder*, 2026-11-07).

## 2026-11-09 — Cierre de tarea: regenerar y subir

**DECISIÓN DEL AUTOR (proceso):** si una tarea cambió prosa, al terminarla se regeneran EPUB, PDF y audiolibro (incremental), aunque sean borradores, y todo se sube a `develop` (commit y push autorizados; nunca `main` ni `--force`). Supersede la regla de regenerar sólo con bloque confirmado. Protocolo: skill `regenerar-y-subir`; reglas en `CLAUDE.md` y `AGENTS.md`.
