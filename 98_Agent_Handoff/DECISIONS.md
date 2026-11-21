# Decisiones recientes

Máximo 800 palabras; conservar sólo decisiones operativas recientes y enlaces a sus fuentes. El historial íntegro anterior al corte está en [[98_Agent_Handoff/archive/2026-09-21_DECISIONS]]; las del 2026-11-01, en [[98_Agent_Handoff/archive/2026-11-08_DECISIONS]]; las del 2026-11-04 al 2026-11-06, en [[98_Agent_Handoff/archive/2026-11-09_DECISIONS_retiradas]]; la Fase 3 del Libro II, en [[98_Agent_Handoff/archive/2026-11-21_DECISIONS_retiradas]]. Archivar entradas antiguas antes de retirarlas.

## 2026-11-21 — Cirugía de la lectura corrida (Libro I)

**DECISIÓN DEL AUTOR:** el método es capítulo por capítulo, del 1 al 47, con verificación doble y un commit por capítulo. Hay siete decisiones transversales: la luz de invierno se corrige y se conservan las horas; Chiara tutea a Meiko y Meiko le habla de usted; el Peugeot lleva una línea de lógica y en el 35 Kal va en el Audi; la redundancia entre POV se reduce a una línea; se marca el salto a junio; Kal le pasa el parte a Nadir en el 21; hay un gesto entre los Varek en el 20. Detalle: [[13_Auditorias/Book_01_Mascaras_De_Cristal/Cirugia_Lectura_Libro_I]].

## 2026-11-21 — Diálogo ping-pong prohibido

**DECISIÓN DEL AUTOR:** desde hoy quedan prohibidos los diálogos ping-pong en toda la saga; las interacciones entre personajes se escriben como conversaciones. Se revocan las excepciones de la regla 05 y de la regla de puesta en escena 04. Umbral (cinco o más réplicas seguidas de ≤14 palabras habladas) y detector: [[12_Craft_Policies/dialogue_rules/05-esticomitia-de-una-sola-voz]], `tools/editorial/pingpong_audit.py`. **Complemento (mismo día):** regla 06 «Réplica mínima» (máximo 25 % de réplicas de ≤3 palabras por capítulo fuera de la acción) y ficha de Kal replanteada: [[12_Craft_Policies/dialogue_rules/06-replica-minima]]. Contrapeso: regla 07 «Réplica que se debe» ([[12_Craft_Policies/dialogue_rules/07-replica-que-se-debe]]), aplicada en los caps. 3, 15, 18, 32 y 33.

## 2026-11-21 — Libro II en 48 capítulos (propagado)

**DECISIÓN DEL AUTOR (2026-11-18), propagada el 2026-11-21:** la Fase 1 ([[11_Books/Book_02_Sombras_De_Poder/00_Fase1_Tres_Pruebas]]) deja el Libro II en **48 capítulos**: I = 1–12, II = 13–26, III = 27–33, IV = 34–48. Los archivos conservan su nombre (tabla y equivalencias en [[11_Books/Book_02_Sombras_De_Poder/00_Book_Map]]); nueve placeholders fundidos se retiraron y *Stavanger* y *Henrik* son un solo archivo, sin reescribir. Abiertos: la excepción de los tics 4 y 5 seguidos y la señal 3. Detalle: [[98_Agent_Handoff/sessions/2026-11-21_claude_propagacion_48_libro_II]].

## 2026-11-17 — Kal nunca deja de pagarle a Crowe (Libro II)

**DECISIÓN DEL AUTOR («Escenario 1»):** la cuota mensual de Kal a Crowe sigue hasta la muerte de Crowe (como en los caps. 45 y 55); la guerra de la Parte III nace de las noches de Kal contra la gente de Crowe, no de la deuda. Supera la (P) de «no la paga hasta saber» (cap. 32). [[98_Agent_Handoff/sessions/2026-11-16_claude_lote1_integracion]]

## 2026-11-13 — El arco de Meiko en cuatro capítulos (Libro II, 57 caps.)

**DECISIÓN DEL AUTOR:** el antiguo 36 se parte en *Las latas* (36, Kal) y *Lo del hermano* (37, Kal); siguen *Perdóname, jefe* (38, Nadir) y *Lo que queda* (39, ahora de Chiara). Todo lo demás sube uno: Parte III 32–40, Parte IV 41–57. **CANON:** Kal le contesta a Meiko «—Eso ya no importa, estás aquí… con nosotros.»; no llora hasta decirle a Chiara «Iba a decirle que sin importar lo que tuvo que hacer, era de los míos.». Bonnie se va después del entierro; la tarde del entierro le dice a Chiara, que todavía le habla de planes, que no va a quedarse, y le cuenta la traición. Fuente: [[11_Books/Book_02_Sombras_De_Poder/00_Guia_Redaccion_Capitulos]].

## 2026-11-12 — «Lo siento, ¿vale?» y Meiko en el final

**DECISIÓN DEL AUTOR:** F2 se queda en la Parte III. El final del Libro II la cobra con ecos de Kal y Chiara (recuerdos de Meiko o de aquel día), no con venganza ni de forma textual. «Lo siento, ¿vale?» va en el cap. 38: Kal vuelve del entierro y encuentra a Chiara rota en el suelo de la Villa, con la foto de la cena de Navidad (todos los chicos sonriendo). Kal se disculpa porque el código de su jerarquía costó una vida, y a Chiara le costó a Meiko y a Bonnie. La foto se siembra en el cap. 20. Resuelto el golpe fallido en la entrada de arriba. Fuente: [[11_Books/Book_02_Sombras_De_Poder/00_Guia_Redaccion_Capitulos]].

## 2026-11-09 — Cierre de tarea: regenerar y subir

**DECISIÓN DEL AUTOR (proceso):** si una tarea cambió prosa, al terminarla se regeneran EPUB, PDF y audiolibro (incremental), aunque sean borradores, y todo se sube a `develop` (commit y push autorizados; nunca `main` ni `--force`). Supersede la regla de regenerar sólo con bloque confirmado. Protocolo: skill `regenerar-y-subir`; reglas en `CLAUDE.md` y `AGENTS.md`.
