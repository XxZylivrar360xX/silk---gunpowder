# AUDIT — Parte II — Caps. 26–34 (*Con peores personas he tratado*)

**Encargo:** [[98_Agent_Handoff/ENCARGO_Auditoria_Parte_II]] (una terminal, nueve etapas secuenciales). **Modo:** AUDIT en E1–E4 (no toca prosa); SURGERY en E5–E8; escena de Irene y registro en E9.
**Política:** [[12_Craft_Policies/editorial/EDITORIAL_POLICY]] (§L prolepsis, §J sin cuotas), [[12_Craft_Policies/editorial/DO_NOT_TOUCH]], [[12_Craft_Policies/editorial/MICROEDICION]].
**Dictamen de origen:** [[13_Auditorias/Book_01_Seda_y_Polvora/Auditoria_Editorial_Part_02]] (matriz, inviolables y housekeeping resumidos en el encargo).
**Estado de los capítulos:** los nueve siguen en **BORRADOR**. La cirugía no los sube de estado. No hay CLOSE.
**No se tocan aquí:** el EPUB, la Parte I, la Parte III (sólo lectura por búsqueda), los archivos compartidos antes de E9.

## Estado de etapas

| Etapa | Alcance | Estado | Fecha | Nota |
|---|---|---|---|---|
| E1 | AUDIT 26, 27, 28 y cronología fija 26–31 | **HECHA** | 2026-09-27 | §0–§5 de 26–28, § Cronología 26–31, metadata anotada, § Decisiones (borrador) D1–D14 |
| E2 | AUDIT 29 y 30, plan contra Varek | **HECHA** | 2026-09-27 | §0–§5 de 29–30 (Parte 2), § Plan contra Varek (V1–V3), P2 y P4 evaluados, autos cerrados, cronología del 30 resuelta, § Metadata de 29–30, D15–D27 |
| E3 | AUDIT 31 y 32, diseño de Irene | **HECHA** | 2026-09-27 | §0–§5 de 31–32 (Parte 3), resumen del coche, P2 (Beretta: 31:83), P3 (gesto en la roca), P4 (no lo cubre el 32), § Irene en el 32 (inserción tras 32:131), § Metadata de 31–32, D28–D45; hallazgo: bloque de diseño de 32:23 impreso en el EPUB |
| E4 | AUDIT 33 y 34, consolidación y preguntas al autor | **HECHA** | 2026-09-27 | §0–§5 de 33–34 (Parte 4), ritual del *Ciao* conforme, P4 contra 33–44 (43 lo roza; queda para el Libro II), § Balance (saldo ≈ +1,850 a +1,980), D46–D52, **§ Decisiones que necesito con respuestas del autor** (V2, Beretta en el 31, Irene paquete completo, resto como veto libre) |
| E5 | SURGERY 26, 27, 28 | **HECHA** | 2026-09-27 | Aplicado todo lo aprobado (Q4, veto libre) y la metadata de 26–28; prosa 7,864 → 7,486 (−378); tres costuras ajustadas; finales de línea conservados. Ver § 9 Resultado (parte 1) |
| E6 | SURGERY 29, 30 | **HECHA** | 2026-09-27 | Aplicado Q1 (V2) y el veto libre de 29–30; prosa 7,762 → 6,922 (−840: 29 −219, 30 −621); inviolables intactos; ningún pago de 35–44 roto; metadata saneada (30:22 queda para E8); CRLF conservado. Ver § 9 Resultado (parte 2) |
| E7 | SURGERY 31, 32 | **HECHA** | 2026-09-27 | Aplicado Q2 (Beretta en 31:83) y el veto libre de 31–32, con P3 (gesto en la roca); prosa 6,128 → 5,780 (−348: 31 −258, 32 −90); bloque de 32:23 dentro del comentario (el EPUB vigente aún lo lleva); metadata saneada (32:4 y 32:15 para E9); inserción de Irene marcada tras 32:131; LF conservado. Ver § 9 Resultado (parte 3) |
| E8 | SURGERY 33, 34 y housekeeping documental | **HECHA** | 2026-09-27 | Aplicado el veto libre de 33–34 y D46 (a); prosa 5,249 → 4,896 (−353: 33 −303, 34 −50); metadata saneada; housekeeping por desfase hecho; H6 §5/§7 y H7 anotados sin sobrescribir (decisión del autor); LF conservado. Ver § 9 Resultado (parte 4) |
| E9 | Escena de Irene y registro final | **HECHA** | 2026-09-27 | Escena de Irene en el 32 (+621) e hilo A (+9), BORRADOR/DISEÑO; metadata del 32 saneada; registro compartido (dictamen, evaluación de arco, brief, log, INDEX, Book Map, fichas de Irene y Nadir); saldo final ≈ +2,260. Ver § 9 Resultado (parte 5). **Encargo cerrado.** |

**Estado de los capítulos auditados en E1 (para el `git diff --stat` de E5):** 26, 27 y 28 sin cambios en el árbol de trabajo al 2026-09-27; último commit `1af8c6a`. Palabras de prosa (`wc -w` desde el encabezado, sin metadata): 26 = 2,309 · 27 = 2,535 · 28 = 3,020. Finales de línea: mixtos CRLF/LF (26 verificado); conservarlos.
**Estado de los capítulos auditados en E2 (para el `git diff --stat` de E6):** 29 y 30 sin cambios en el árbol de trabajo al 2026-09-27; último commit `1af8c6a`. Palabras: 29 = 2,979 · 30 = 4,783. Finales de línea: mixtos CRLF/LF en los dos (verificado con `file`); conservarlos.
**Estado de los capítulos auditados en E3 (para el `git diff --stat` de E7):** 31 y 32 sin cambios en el árbol de trabajo al 2026-09-27; último commit `1af8c6a`. Palabras: 31 = 4,136 · 32 = 1,992 (sin el bloque de 32:23, 167). Finales de línea: LF en los dos (verificado con `file`); conservarlos.

---

# Parte 1 — Caps. 26, 27 y 28 (E1)

## 0. Diagnóstico corto

- **26 (MEDIA).** Funciona y se sostiene en dos escenas fuertes (Walt, el galpón). Los problemas son de **cronología** ("la segunda noche", "dos noches atrás"), una **recapitulación de H15** en el galpón (la lista convoy / parabrisas / niño / prisión que el lector acaba de leer en el 25), un error mecánico (el mensaje de Walt tiene diez palabras, no nueve) y un par de glosas que anuncian la línea de diálogo que viene justo después. Las tres líneas canon de Varek, el frío "con todo menos con un hombre" y la línea de Walt se protegen enteras.
- **27 (LIGERA).** Muy sólido. Tres cosas: la **cronología del regreso** (sale "con las últimas luces" y "maneja toda la noche" un trayecto de cuatro horas para llegar al amanecer), una **repetición funcional** entre el borrador *no es Varek* (62) y la decisión del camino de vuelta (146–150), y un problema de continuidad chico: Kal "intuía por cómo había amanecido ella" cuando se fue con ella dormida (148). El recorrido, la instalación y los contratistas se compactan poco: casi todo lo que parece recorrido es firma de Kal (catalogar, conducir él) y siembra de Camp Alder.
- **28 (MEDIA).** El capítulo más cargado de cronología vieja ("dos días" ×4, "la primera noche daba tono"), el del **bug del auto** (aquí el Peugeot, que es el canon de la Parte I; el 29–31 lo cambian por un Audi) y el que tiene más **glosas que traducen gestos** alrededor de la columna protegida. Hay dos **saltos de POV** hacia Kal en un capítulo de POV único de Chiara (58, 234) y uno de conocimiento imposible (222: lo que Varek le dijo a Kal en el hospital, con ella sedada). La columna "No vuelvas a hacer algo así sola" → "Sonó como una" y las líneas canon de H6 §2 quedan intactas.

## 1. Candidatos por categoría

Numeración continua para las tres partes del mapa: **A** = continuidad y mecánica; **B** = prolepsis y POV; **C** = glosa, tic, repetición. Las palabras son el efecto aproximado del corte propuesto (− libera).

### A. Continuidad y mecánica (prioridad 1)

| # | Cap:línea | Texto | Problema | Propuesta | Palabras |
|---|---|---|---|---|---|
| A1 | 26:109 | "…y **para la segunda noche** entendió que sus preguntas caminaban de vuelta…" | Cronología fija: todo el 26 cabe en un día; el galpón es esa misma noche | "y **para la noche** entendió…" (o "antes de que oscureciera") | −1 |
| A2 | 26:127 | "Se lo había contado él mismo, **dos noches atrás**, en el agua" | El jacuzzi fue la noche anterior | "**la noche anterior**" (se funde con C2) | 0 |
| A3 | 26:79 | "más tiempo del que hacía falta para leer **nueve palabras**" | *Cuida el barrio. Si Chiara necesita algo, ayúdala sin chistar.* = 10 palabras | "**diez palabras**" | 0 |
| A4 | 27:142 | "Salió **con las últimas luces** y **manejó toda la noche**." (con 144 "cuatro horas de recta" y 152 "con la primera claridad") | Cuatro horas desde el anochecer no llegan al amanecer; además la reunión fue "corta" (96) y Halbrook "tiene un vuelo" (100): no queda explicado el día entero allá | Ver **D3**. (a, recomendada) "**Lo soltaron ya de noche** y manejó hasta el amanecer" + dejar que el dolor explique la lentitud (144 ya dice "tomó las curvas despacio"). (b) conservar "con las últimas luces" y añadir una parada ("se orilló dos veces a respirar"). No cuadrar horas en prosa | ±0/+6 |
| A5 | 27:148 | "—eso Kal no lo sabía con detalle, pero **lo intuía por cómo había amanecido ella**, midiendo el aire—" | Kal se fue a las 5:40 con Chiara dormida (72): no la vio amanecer | "…lo intuía por cómo **había subido ella esa madrugada**, midiendo el aire" (27:30 confirma que estaban juntos antes de que se durmiera; 26:43 pone la advertencia en el ascensor privado) | 0 |
| A6 | 28:34 | "había hecho demasiadas preguntas **en dos días**" | Cronología fija | "**en un solo día**" o cortar "en dos días" | −3 |
| A7 | 28:36 | "**Los dos días anteriores** se los había pasado casi enteros moviéndose entre el casino, el barrio y el bloque de los Bravos al sur, y **una tarde**, cerca de El Patio, lo vio ella misma" | Cronología fija; además 28:74 fecha el avistamiento en El Patio "hace dos días" (antes de que Kal se fuera: compatible con 27:54, donde Walt ya había visto el sedán dos tardes atrás) | "**Desde que él se fue** se había movido entre el casino, el barrio y el bloque de los Bravos al sur. Días antes, cerca de El Patio, había visto ella misma un sedán oscuro…" (el avistamiento de El Patio queda antes de la salida de Kal; el del loft, "esa noche") | ±0 |
| A8 | 28:36 | "Varek le había dicho de madrugada, **junto al jacuzzi**, que…" | 26:43 lo pone "junto al ascensor privado", "con el pelo todavía húmedo del jacuzzi" | "…le había dicho esa madrugada, junto al ascensor, que…" (se funde con C12) | 0 |
| A9 | 28:40 | "Lo había llamado seis veces. **La primera noche daba tono. Desde el mediodía, la operadora.**" | Contradice 26:47 (a las 7:10 ya no daba tono) y supone varias noches | "Lo había llamado seis veces. **Las seis, la operadora.**" | −5 |
| A10 | 28:50 y 28:246 | "El **Peugeot**." / "las luces del **Peugeot** encenderse" | 29–31 lo tienen en un **Audi** (29:279, 30:43, 31:87…); la Parte I y la ficha fijan el Peugeot 106 XSi rojo. El error está del lado del 29–31, no del 28 | **No se toca en E5**: la versión se decide en E2 (bug Peugeot/Audi). Anotado aquí porque el 28 es el ancla | — |
| A11 | 28:176 | "…en vez de hacer lo que sea que **hiciste anoche**." | Lo que Kal hizo fue de día (Halbrook y la paliza); de noche manejaba | "…lo que sea que hiciste **ayer**." | 0 |
| A12 | 28:204 | "qué había hecho ella **los dos días que él estuvo sin dar señales**" | Cronología fija (y se funde con C9) | "qué había hecho ella **mientras él estuvo sin dar señales**" | −3 |
| A13 | 28:124 + 82 + 136 | Fotos: "**Un coche, dos veces, con la placa legible**" / sedán: "No le vi la placa. Nadie se la ha visto nunca." / "Walt vio un coche parado más tiempo del que debía" | El lector puede leer que el coche fotografiado es el sedán, y entonces la placa "nunca vista" contradice las fotos. Son dos coches distintos (uno de los Bravos, otro de Halbrook), pero la prosa no lo separa | **D6**: (a) "Un coche **de los Bravos**, dos veces…"; (b) dejar la ambigüedad si el autor la quiere. No es glosa: es un referente | +3 |
| A14 | 28:242 | "demasiado rápido para un hombre con **dos costillas rotas**" | 27:134 dice "dos costillas que iban a quejarse un mes", sin "rotas"; Chiara no las ha visto diagnosticar | DUDOSA — CONSERVAR: es la inferencia de Chiara, y "rotas" es hipérbole creíble. Se reporta, no se propone cambio | 0 |

**Protegido en esta capa:** 26:83 (Walt: "cuando un hombre como Kal desaparece **un par de días**" — es generalización, no cronología); 27:42 ("Un día. Dos, si el tráfico" — es la estimación del emisario); 27:54 ("dos tardes atrás", el sedán antes de la salida); 28:74 ("hace dos días", El Patio, antes de la salida, si se aplica A7); 28:78 ("Anoche. Antes de que oscureciera del todo" — dicho al amanecer, correcto).

### B. Prolepsis y saltos de POV (§L y MICROEDICION C)

| # | Cap:línea | Texto | Categoría | Propuesta | Palabras |
|---|---|---|---|---|---|
| B1 | 28:58 | "No era casualidad, **y él sabía reconocer cuándo un cuarto dejaba de ser un cuarto para volverse un puesto.**" | SALTO DE POV (Chiara POV; entra en lo que Kal sabe). Además 28:68 ya lo dice desde ella ("él ya lo había leído todo") | Cortar la oración entera. La enumeración de lo que vio sus ojos (lámpara, cortina, dónde se sentaba ella) queda como lo que Chiara ve que él ve | −21 |
| B2 | 28:222 | "Kal se quedó muy quieto. **A él se lo había dicho de pie junto a una cama de hospital, con las armas todavía calientes, y lo había dejado pasar como se deja pasar a un hombre que marca una pared. A ella se lo había dicho en un galpón helado, sola, a kilómetros de cualquier sitio.**" | SALTO DE POV / conocimiento imposible: Chiara estaba sedada en el hospital (26:125) y Kal no le contó esa frase. La metadata la llama "línea de escalada" (DISEÑO) | **D7.** (a, recomendada) cortar las dos oraciones; queda "Kal se quedó muy quieto." y la escalada la hace 226–228 ("Nada de eso le había movido los hombros. / Esto sí."), que es POV limpio. (b) conservar como voz de autor, contra la regla de POV único | −52 |
| B3 | 28:234 | "**Supo que faltaba algo.** No insistió. Chiara supo que él tampoco le había contado todo. Tampoco insistió." | SALTO DE POV (el primer "supo" es de Kal) | "**Él supo que faltaba algo; se le vio en la cara.** No insistió…" o, mejor, cortar la primera frase y dejar "No insistió" con sujeto Kal: "Kal no insistió. Chiara supo que él tampoco le había contado todo. Tampoco insistió." | −1 |
| B4 | 28:252 | "**No sabía todavía para qué las iba a necesitar.** Sólo sabía que no iba a dejar información útil tirada en una casa vacía." | PROLEPSIS DE NARRADOR (§L, ejemplo casi literal: "todavía no sabía que iba a necesitar…") | Cortar la primera oración; la segunda queda "No iba a dejar información útil tirada en una casa vacía." | −12 |
| B5 | 27:136 | "**Era gente con la que iba a volver a tratar**, y de la gente con la que uno vuelve a tratar conviene saberlo todo." | Límite de §L: es la expectativa de Kal (permitida), pero la forma "iba a volver a tratar" suena a confirmación del narrador | DUDOSA. (a, recomendada) comprimir a la máxima: "De la gente con la que uno vuelve a tratar conviene saberlo todo." Baja la certeza sin perder el cálculo. (b) conservar | −9 |
| B6 | 27:134 | "Dos costillas **que iban a quejarse un mes**." | Estimación de Kal sobre su propio cuerpo | PROTEGIDO (no es prolepsis: es diagnóstico de quien ha recibido palizas) | 0 |
| B7 | 26:155 | "que la hubiera dejado ir no era piedad. **Era que matarla esa noche le costaba más de lo que ella valía esa noche.**" | Certeza de Chiara sobre el cálculo de Varek | PROTEGIDO como INTERIORIDAD: es la lectura de ella y cierra el capítulo; no confirma nada futuro | 0 |

### C. Glosa, tic, repetición y certificación

| # | Cap:línea | Texto | Categoría | Propuesta | Palabras |
|---|---|---|---|---|---|
| C1 | 26:65 | "Chiara reconoció la frase antes de terminar de oírla. **La había oído antes, con esas mismas costuras, en otra boca.**" → "—Esa la dice Kal." | GLOSA (anuncia la línea siguiente) | Cortar la segunda oración | −11 |
| C2 | 26:127 | "Lo sabía todo. Se lo había contado él mismo, dos noches atrás, en el agua, sin nada entre los dos**: el convoy, el vidrio del parabrisas, el niño por la ventanilla, la prisión que cayó sobre él y no sobre el general.**" | REPETICIÓN FUNCIONAL con el 25 (foco del dictamen: "exposición repetida de H15") | Cortar la lista desde los dos puntos; queda "…Se lo había contado él mismo, la noche anterior, en el agua, sin nada entre los dos." (con A2). La copa en el tren se queda | −24 |
| C3 | 26:79 | "…y que estuvieran escritos con calma. **Un hombre al que se llevan a rastras no se sienta a repartir encargos por orden de importancia.**" → "—Entonces se fue por su propio pie —dijo." | DUDOSA — CONSERVAR: casi duplica la línea siguiente, pero es el razonamiento de ella (INTERIORIDAD) y tiene voz | Conservar. Si el autor quiere apretar, cortar la máxima | (−16) |
| C4 | 26:85 | "Walt la miró un segundo de más, **como si el silencio le hubiera dicho lo que ella no.**" → "—Va a levantarlas de todos modos." | GLOSA leve (anuncia la línea) | Cortar el "como si" | −10 |
| C5 | 26:103 | "…sonaron parejas sobre la grava, **y la conversación quedó cerrada sin que hiciera falta decirlo.**" | GLOSA leve de cierre | Cortar; el portazo lo hacen las botas | −9 |
| C6 | 27:62 vs 27:146–150 | 62: "Escribió *no es Varek*… Ella iba a pensar en Varek… A Kal, Varek no le quitaba el sueño… la calmaba con una media verdad por un lado y la empujaba a mirar hacia arriba por el otro…" / 148: "Ella iba a pensar en Varek. Kal lo sabía… Iba a dejar que persiguiera al hombre de al lado para que no mirara al de arriba." | REPETICIÓN FUNCIONAL: dos veces el mismo razonamiento (ella pensará en Varek; él la deja; "arriba") | **D5.** (a, recomendada) en 62, cortar desde "Ella iba a pensar en Varek —era lo que tenía delante…" hasta "…habían salido caminando." y conservar la conclusión táctica del borrador ("*no es Varek* también sobraba: …ella iba a tirar del hilo que fuera"). La decisión (IRONÍA CANON) queda donde la metadata la pone: en el camino de vuelta. Se pierde el eco de "*no por ella*" en 62; la frase canon sigue viva en 25 y en el cobro del 28. (b) al revés: cortar 148 y dejar 62 | −60 |
| C7 | 27:68 | "…supo, en el mismo segundo, cómo lo iba a leer ella. *Me encuentro bien* era una respuesta, y él le estaba respondiendo algo que ella todavía no había preguntado. **Chiara iba a oír eso antes que las palabras. Iba a saber que él había calculado el susto y había salido a cortarlo por delante.**" | REPETICIÓN FUNCIONAL con 26:41 (que el lector acaba de leer desde Chiara, con la misma imagen del susto) | Cortar las dos últimas oraciones; el espejo de los dos POV sobrevive en la primera mitad | −26 |
| C8 | 27:80 | "Conocía el tramo… **El cuerpo se acordaba de cosas que la cabeza no repasaba nunca: la forma de sentarse para un trayecto largo, la costumbre de anotar los kilómetros por si había que volver a pie. Dejó que se acordara. Era más barato que pelearse con eso.**" | Recorrido (foco del dictamen). Pero es la única entrada del capítulo a la "otra vida" de Kal por el cuerpo | DUDOSA — CONSERVAR. Si se aprieta, sólo "Dejó que se acordara. Era más barato que pelearse con eso." | (−10) |
| C9 | 28:106 vs 28:204 | 106: "—¿Qué hiciste tú mientras yo no estaba" / 204: "Kal preguntó… qué había hecho ella los dos días que él estuvo sin dar señales, más allá de las fotografías." | REPETICIÓN FUNCIONAL (la misma pregunta dos veces) | Conservar las dos (la segunda está bien marcada con "más allá de las fotografías") y sólo corregir la cronología (A12). Se reporta; no es corte | 0 |
| C10 | 28:96 | "…sin mirarla a ella ni una vez. **No era que no quisiera que lo tocara. Era que necesitaba decidir él mismo cuánto cuidado aceptaba, y ella, que llevaba media vida aprendiendo cuándo no acercarse, se lo dejó decidir.**" | GLOSA del "Puedo yo" y REPETICIÓN FUNCIONAL con 88 ("ese permiso le iba a costar a él más que los golpes") | Comprimir a "…sin mirarla a ella ni una vez. Ella, que llevaba media vida aprendiendo cuándo no acercarse, se lo dejó decidir." (se conserva lo de ella, que es interioridad) | −19 |
| C11 | 28:128 | "No corrigió un solo horario. No preguntó cómo había conseguido la placa. / **Chiara entendió, por todo lo que él no dijo, que el material servía.**" | GLOSA / COMPETENCIA EXPLICADA | Cortar el párrafo | −13 |
| C12 | 28:36 | "Varek le había dicho de madrugada, junto al jacuzzi, **que no confiaba en Kal, que lo iba a investigar, que lo iba a hacer seguir.** Chiara sumó una cosa con la otra sin pestañear. **Le sobraban motivos para hacerlo.**" | REPETICIÓN FUNCIONAL con 26:43 (misma advertencia, dos capítulos atrás) + GLOSA de cierre | "Varek le había dicho esa madrugada que lo iba a hacer seguir. Chiara sumó una cosa con la otra sin pestañear." (con A8) | −17 |
| C13 | 28:38 | "La otra razón de la sudadera no se la dijo. **Estaba debajo de la primera, cómoda, y no necesitaba que la nombraran.**" | DUDOSA — CONSERVAR: 32 ya lo sugiere ("estar acompañada"), pero la frase es la que convierte el gesto en tradecraft + ternura sin nombrar la ternura; es voz | Conservar | 0 |
| C14 | 28:158 | "**Eso dolió más de lo que debería haber dolido una frase tan corta.** Chiara se quedó con las manos quietas sobre la barra." | EMOCIÓN EXPLICADA | Cortar la primera oración; las manos quietas hacen el trabajo | −13 |
| C15 | 28:184 | "…y sabía exactamente cómo pesaba del otro lado. **Le ofrecía la puerta abierta en los dos sentidos: la de salir de la ciudad y la de salir de ella.** Era lo único que podía darle que no fuera una correa más." | GLOSA / REPETICIÓN dentro del párrafo (el doble sentido ya está en "las dos veces, la del viaje que le imponían y la que él mismo acababa de proponer") | Cortar la oración marcada. Se protege el resto del párrafo (Palermo, "una mano encima", la correa del título) | −19 |
| C16 | 28:224 | "…y volvió a mirarla a ella. **No dijo nada más de lo necesario, pero algo en cómo apretó la mandíbula le dijo a Chiara que la frase acababa de caerle en un sitio que él no esperaba.**" | REPETICIÓN FUNCIONAL con 226–228 ("Nada de eso le había movido los hombros. / Esto sí.") y contra la metadata ("ella lo ve y lo registra sin nombrarlo") | Comprimir a "…y volvió a mirarla a ella. Apretó la mandíbula." | −24 |
| C17 | 28:252 | "Quedarse ahí mirando la esquina no servía de nada. **Eso lo tuvo claro enseguida; era la clase de cosa que siempre tenía clara.**" | COMPETENCIA EXPLICADA | Cortar | −14 |
| C18 | 28:200 | "**Fue lo más parecido a una disculpa que iba a conseguir esa noche, y por ahora bastaba.**" | DUDOSA — CONSERVAR: glosa del "Lo sé", pero cierra la sección con la voz de Chiara | Conservar | 0 |
| C19 | 28:236 | "—Bien —dijo Kal, **y la palabra no significaba nada de lo que significa normalmente.**" | GLOSA leve | DUDOSA — CONSERVAR: marca el cambio de registro antes del "¿Nos podemos reunir?"; sin ella, "Bien" puede leerse como cierre | 0 |
| C20 | 26–28 | Preguntas cerradas con punto ("¿Quién fue." / "¿Qué trabajo.") | Tic tipográfico: 16 en el 28, 1 en el 27, 0 en el 26; 2 en toda la Parte I | FIRMA DE VOZ — CONSERVAR (interrogatorio plano de Kal y Chiara). Se reporta la densidad en el 28 para que el autor confirme que la quiere | 0 |

**Suma aproximada de lo recomendado (sin DUDOSAS):** 26 ≈ −55 · 27 ≈ −95 (con C6a) · 28 ≈ −195 (con B2a). Referencia, no meta (§J).

## 2. Prolepsis y POV — lectura por capítulo

- **26 (POV Chiara, único).** Limpio de prolepsis. Varek se ve siempre desde fuera ("la miró como un hombre que repasa una cifra"). El cierre (B7) es inferencia de ella. Sin saltos.
- **27 (POV Kal, único).** Sin saltos: Halbrook y los contratistas se leen por conducta. Una prolepsis limítrofe (B5). El "no les importaba cómo llegara mientras llegara" (78) es inferencia de Kal, se protege.
- **28 (POV Chiara, único).** Tres saltos o conocimientos imposibles (B1, B2, B3) y una prolepsis §L (B4). Es el capítulo que más necesita esta capa. 28:84 ("algo que no era sorpresa sino reconocimiento") se protege: es lectura de Chiara y siembra del sedán, no dato.

## 3. Función por movimiento

Palabras con `wc -w` por rango de líneas.

**Cap. 26 (2,309)**

| Líneas | Movimiento | Palabras | Función | Veredicto |
|---|---|---|---|---|
| 21–49 | La terraza sur, el desayuno siciliano, el mensaje, el recuerdo de Varek en el ascensor | 512 | H5 lado Chiara; lectura canon de "Me encuentro bien"; único lugar donde vive la advertencia de Varek (decisión del autor 2026-09-09) | Intacto (el espejo con el 27 se poda del lado del 27: C7) |
| 51–103 | Walt en la destilería: pedido, paciencia, el mensaje "Cuida el barrio", "lo que sea que es esto", línea canon | 747 | Confirma que Kal se fue por su pie; siembra la paciencia como cuchillo; canon de Walt | A3, C1, C4, C5 (C3 dudosa) |
| 105–111 | Chiara investiga en el Monarch | 108 | Transición; sus preguntas vuelven a Varek | A1 |
| 113–129 | El Lancia, el galpón, Varek cuenta el hospital y el ejército | 419 | Coartada fina; ella finge no saber | A2, C2 |
| 131–145 | Las tres líneas canon | 262 | Núcleo del capítulo | Intacto |
| 147–155 | El frío "con todo menos con un hombre", la medalla, "la dejó ir" | 261 | Alusión al diablo sin nombrarlo; ella se queda "más de lo prudente" | Intacto (B7 protegido) |

**Cap. 27 (2,535)**

| Líneas | Movimiento | Palabras | Función | Veredicto |
|---|---|---|---|---|
| 26–46 | La llamada de las tres | 256 | Convocatoria administrativa; "el reacomodo" | Intacto |
| 48–72 | Los dos mensajes y sus borradores; el sedán; Chiara dormida | 571 | Canon de los mensajes; siembra del sedán; IRONÍA canon | C6, C7 |
| 74–84 | Carretera al noreste, la instalación | 311 | "Conduce él"; la otra vida por el cuerpo; lugar sin ubicar | C8 dudosa. Poco que compactar: el dictamen pedía compactar recorrido, y aquí el recorrido es firma de Kal |
| 86–130 | Halbrook: oficina, expediente de Nadir, "riesgo pendiente" | 801 | Correa; siembra de Camp Alder ("un sitio donde usted ya estuvo"); versión de Halbrook | Intacto. (Nota de mecánica, no candidato: 130 "No les pedí que fueran innecesarios… **Le** pedí que **quede** claro" — ver D9) |
| 132–138 | Los contratistas | 251 | Kal cataloga; "un recordatorio, no un castigo"; descarta a la gente de Varek | B5. El resto se protege: "No eran matones de esquina ni caras que hubiera visto rondando a la gente de Varek" es lo que le permite a Kal saber que no fue Varek |
| 140–154 | El regreso de noche; decisión de no darle el nombre | 345 | IRONÍA canon; llegada al amanecer | A4, A5, C6 |

**Cap. 28 (3,020)**

| Líneas | Movimiento | Palabras | Función | Veredicto |
|---|---|---|---|---|
| 30–50 | La sudadera, el sedán, el sobre, el rezo, el Peugeot | 649 | H5 §14; tradecraft y ternura; siembra del sedán | A6–A10, C12 (C13 dudosa) |
| 52–100 | Kal entra; "¿Quién está mirando la calle."; la gasa, "Puedo yo"; "Gente de antes" | 642 | H6 §1; él lee el puesto; ella no lo toca | B1, C10 |
| 101–128 | Las fotografías | 199 | Activo que el 30 cobra | A13, C11 |
| 129–170 | "No deberías haber sido tú" → "Sonó como una." | 251 | **Columna protegida** (Hallazgo 2) | C14. Los cuatro renglones canon, intactos |
| 171–200 | "Puede que tenga que irme" → líneas canon H6 §2 → "¿Fue Varek?" | 446 | Canon del autor; doble ausencia | A11, C15 (C18 dudosa) |
| 202–242 | El taller contado; se guarda la tercera línea; "¿Nos podemos reunir?" | 588 | H6 §3; lo que lo saca es que le dijeran a ella qué puede hacer | A12, B2, B3, C16 (C9, C19 conservar) |
| 244–252 | El Peugeot sale "como un diablo"; ella recoge las fotos | 245 | H6 §4 | A10, B4, C17 |

## 4. Protegido y siembras

- **Canon de 26:** "Trabajas para mí. No conmigo." / "¿Te estás acostando con él?" / "Si hay que eliminar a Kal, entonces tú vas a hacerlo" + "vas a aprender tu lugar"; el mensaje *Me encuentro bien*; la línea de Walt (101); "el galpón se puso más frío"; el pasaje del diablo sin la palabra (147); la medalla y el pensamiento feo en italiano (149).
- **Motivo del clima en 26** (43 "como quien comenta el clima", 133 "como se pregunta si va a llover", 147 "Con el clima."): parece repetición lexical y es construcción. Se protege.
- **Canon de 27:** los dos mensajes y sus horas (5:30 Walt, 5:40 Chiara); "Nadie está fuera de nada. Está inactivo."; "riesgo pendiente"; "No es un castigo. Es un recordatorio."; "Le va a doler el costado en las curvas" y su eco en 144. **Siembra de Camp Alder** (120, "una entrada a un sitio donde usted ya estuvo. Material que sacar"): no podar. **Sedán** (54, 112): no resolver.
- **Canon de 28:** la columna 160–168; H6 §2 (180–182); "¿Nos podemos reunir?"; la sudadera como disfraz; se guarda la tercera línea (218, "al lado de otras que llevaba ahí desde Palermo"); "Nada de eso le había movido los hombros. / Esto sí."; las fotos que ella recoge (el 30 las cobra).
- **Interioridad protegida en 28:** 88 (el permiso que le cuesta más que los golpes), 142 ("No era mentira. No era tampoco toda la verdad." — es lo único que insinúa que Kal se volvió su único plan, motivación que la metadata guarda para el 30/31), 152, 174 (el tono aplicado "por primera vez a ella misma"), 186 (la cosa que no sabe dónde guardar).
- **Ritual del *Ciao*:** en 26–28 no aparece ni "Ciao" ni apodo; los mensajes son planos (conforme a la metadata). La revisión completa 26–34 es de E4.

## 5. Lo que no es de microedición (se reporta y no se opera)

1. **Autos (A10 + ficha de Chiara).** Kal: Peugeot 106 XSi rojo en la Parte I, la ficha y el 28; Audi en 29–31 (y una mención en el 37). Chiara: **Lancia** nuevo en el 26 (113, "todavía olía a sala de exhibición") y en 29–30; la ficha de Chiara (l. 328) y la metadata del 28 dicen **Mercedes-Benz Clase S** del Monarch. Es continuidad de objetos, no de prosa: E2 fija la versión.
2. **Geografía del 27:** 76 pasa por Kingsley Field y la reja; 80 dice que las carreras quedan "más al oeste, las Rutas de Milla". La ficha del taller lo pone junto a la reja de Kingsley Field y la Carretera de Milla. Compatible si la carretera al noreste arranca en el mismo punto y se separa después; lo anoto para housekeeping, no para prosa.
3. **Qué hizo Kal todo el día fuera (A4).** Si la reunión fue corta, la prosa no cuenta las horas entre la paliza y la salida. No hace falta contarlas; basta con que la hora de salida no choque (D3).
4. **La tercera línea de Varek** se guarda en 28 y reaparece en 30:111 ("la dejó exactamente donde la había dejado la noche anterior" — cronología: fue esa madrugada; ver § Cronología).

---

# § Cronología 26–31

**Secuencia fija (Hallazgo 4):** noche del Cap. 25 (jacuzzi; advertencia de Varek en el ascensor) → ~3 a. m. llamada; 5:30 / 5:40 mensajes; Kal sale → **día 1**: Chiara (Walt, Monarch, fotos de los Bravos, sedán junto al loft antes de oscurecer, galpón con Varek de noche) / Kal (Halbrook, paliza) → Kal maneja de vuelta de noche; Chiara en el loft con la sudadera desde las 11 → **amanecer del día 2**: Cap. 28 (loft) → mansión de Varek (29) → Media Baraja / roca (30) → El Patio (30) → lago y "Vamos a casa" (31), tarde-anochecer. Unas 24 horas entre la salida y el regreso, no "dos días".

| Cap:línea | Texto | ¿Compatible? | Corrección propuesta |
|---|---|---|---|
| 26:29 | "Anoche no se habían llamado de ninguna manera." | Sí | — |
| 26:33 / 26:77 | 5:40 (Chiara) / 5:30 (Walt) | Sí | — |
| 26:43 | "Esa misma madrugada… junto al ascensor privado" | Sí (ancla) | — |
| 26:45 | "A las siete y diez de la mañana" | Sí | — |
| 26:71 | "Kal salió de la ciudad esta madrugada." | Sí | — |
| 26:83 | "desaparece un par de días" (Walt, general) | Sí | — |
| 26:109 | "para la segunda noche" | **No** | A1: "para la noche" |
| 26:117 / 151 | "quedarse varada de noche" / "Los caminos del norte no tienen luz" | Sí (galpón, noche del día 1) | — |
| 26:127 | "dos noches atrás, en el agua" | **No** | A2: "la noche anterior" |
| 27:28 | "a las tres y algo de la mañana" | Sí | — |
| 27:42 | "Un día. Dos, si el tráfico." | Sí (estimación) | — |
| 27:54 | sedán "dos tardes atrás… y otra vez al día siguiente" | Sí (antes de la salida) | — |
| 27:82 | "A las tres horas y media" | Sí | — |
| 27:142 | "Salió con las últimas luces y manejó toda la noche." | **No** (4 h no llenan la noche) | A4 / D3 |
| 27:148 | "por cómo había amanecido ella" | **No** (continuidad, no hora) | A5 |
| 27:152 | "con la primera claridad" | Sí (ancla del regreso) | — |
| 28:34 | "en dos días" | **No** | A6 |
| 28:36 | "Los dos días anteriores… una tarde… Esa noche" | **No** | A7 |
| 28:36 | "de madrugada, junto al jacuzzi" | Hora sí; lugar **no** | A8 |
| 28:40 | "La primera noche daba tono. Desde el mediodía, la operadora." | **No** (26:47) | A9 |
| 28:46 | "A las cuatro y media se quedó dormida" | Sí | — |
| 28:74 | "Lo vi cerca de El Patio hace dos días." | Sí si A7 lo deja antes de la salida | — |
| 28:78 | "Anoche. Antes de que oscureciera del todo." | Sí | — |
| 28:164 | "que Chiara conocía de otro lado esa misma noche" (su propia cara en el galpón, 26:139) | Sí con la cronología fija (el galpón es esa noche) | — |
| 28:176 | "lo que sea que hiciste anoche" | **No** | A11: "ayer" |
| 28:204 | "los dos días que él estuvo sin dar señales" | **No** | A12 |
| 28:226 | "esa misma noche, un ultimátum… una paliza medida" | Sí (lo que ella vio fue esa noche; no fecha el ultimátum) | — |
| 28:248 | "el amanecer subiendo gris" | Sí | — |
| 29:4 (meta) | "el mismo amanecer, minutos después" | Sí | — |
| 29:69 / 71 / 169 / 177 | "esa mañana" ×4 | Sí | — |
| 29:241 / 245 | "dos horas antes" / "horas antes, en la cocina del loft" | Sí | — |
| 30:71 | "había pasado **dos días** mirando al hombre equivocado" | **No** | **E2:** "había pasado **el día entero** mirando al hombre equivocado" (A22) |
| 30:79 | "¿Por qué no me lo dijiste **anoche**?" | **No** (el loft fue al amanecer) | **E2:** "¿Por qué no me lo dijiste **en el loft**?" (A22) |
| 30:101 | "…en una roca, y no **anoche**." | **No** | **E2:** "…en una roca, y no **en casa**." (evita el tercer "en el loft" en veinte líneas; A22) |
| 30:109 | "no tenía ganas de pelear con él esa mañana" | Sí | — |
| 30:111 | "donde la había dejado **la noche anterior** con Kal" | **No** (fue esa madrugada) | **E2:** "donde la había dejado **esa madrugada** con Kal" (A22) |
| 30:195 | "No era lo mismo que **el día anterior**, en el loft" | **No** (el loft fue esa mañana) | **E2:** se va con el corte C47; si C47 no se aprueba, "que **esa mañana**, en el loft" |
| 30:201 | "Horas antes esas mismas fotografías…" | Sí | — |
| 30:245 | "por primera vez **en dos días**" | **No** | **E2:** "por primera vez **desde que leyó el mensaje**" (A22) |
| 30:407 / 409 | Walt: "¿Es por lo de anoche?" / Kal: "Es por lo de anoche, por lo de esta mañana y por lo de ahora." | Walt sí (no sabe cuándo); Kal: en habla, "anoche" abarca la carretera hasta el amanecer | **E2: CONSERVAR** (A23). La triple fórmula es ritmo de Kal |
| 30:435 | "Podías anoche. … Podías esta mañana." | Sí, en boca de Nadir: no conoce la agenda de Kal y el reproche es suyo, no dato del narrador; Kal pudo llamar desde la carretera | **E2: CONSERVAR** (A23) |
| 30:427 / 453 | "Desde antes de esta mañana" / "en algún punto de la carretera de vuelta" | Sí | — |
| 30:505 | "más de lo que sabíamos ayer… No dos tardes después." | Sí | — |
| 31:4 (meta) | "MISMO DÍA que los Caps. 28-31… del día que Halbrook sacó a Kal de la ciudad de madrugada" | **No** (el día del 28–31 es el del regreso; y "28-31" se incluye a sí mismo) | "mismo día que los Caps. 28–30 … el día del **regreso** de Kal" (E7) |
| 31:6 (meta) | "cierre del arco H5-H7 y de la Parte II, el mismo día que lo abrió H5" | **No** (H5 abre el día anterior; y no cierra la Parte II) | E7 |
| 31:17 (meta) | "costillas y la ceja de **esa misma madrugada**" | **No** (la paliza fue el día anterior) | "de la paliza del día anterior" (E7) |
| 31:23 (meta) | "esa misma madrugada había planteado parar" | Sí (el loft) | — |
| 31:87 / 99 | "esa mañana" / "esa tarde" | Sí | — |
| 31 prosa | "el mismo día que Halbrook sacó a Kal…" | **No aparece en prosa** (sólo en la metadata, 31:4) | — |

---

# § Metadata de 26–28 (se anota, no se toca; se sanea en E5)

| Cap:línea | Dice | Problema | Debe decir |
|---|---|---|---|
| 26:2, 27:2, 28:2 | "Parte II (La Construcción)" | Nombre operativo: *Con peores personas he tratado* | "Parte II (*Con peores personas he tratado*)" |
| 26:4 | "Un día después de H15 (la noche del jacuzzi)" | Es la mañana siguiente, no un día después | "La mañana siguiente a H15" |
| 26:9 | "Walt **got** un mensaje también" | Residuo en inglés | "Walt recibió un mensaje también" |
| 26:17 | Ritual del "Ciao, bello": "nace tras H21" | Revisar contra el canon del ritual (encargo: antes del 34, Kal también es "tesoro") en E4 | E4 |
| 27:4 | "los mismos **~2-3 días** que cubre el Cap. 26" | Cronología fija | "el mismo día que cubre el Cap. 26 (unas 24 horas)" |
| 27:10 | "(ya citados en **Cap. 27**)" | Los mensajes se citan en el 26 | "Cap. 26" |
| 27:14 | "el lector ya tiene la versión de Kal **desde el Cap. 26**" | La versión de Kal es del 25 (jacuzzi); el 26 la recuerda | "desde el Cap. 25" |
| 27:12 | "…relectura retrospectiva tras el **Cap. 31** (nombre Halbrook revelado a Chiara)" | El nombre se revela en el 30 (inviolable "Warren Halbrook") | "tras el Cap. 30" (confirmar en E2) |
| 27:20 | "se apoya en la siembra del **Cap. 26**… junto a la cama del hospital" | La frase "No por ella" vive en la Parte I (Caps. 9 y 25 por búsqueda) | Numeración vieja: "la siembra de la Parte I (H12)" |
| 27:21 | "su llegada física es la coda que cierra **el Libro I**" | Supersesión 2026-09-07/22: cierra el **Libro II** | "…que cierra el Libro II (*Sombras de Poder*)" |
| 28:4 | "la noche **siguiente** a la confrontación del taller del norte (cierre del **Cap. 27**)… Cierra con Kal cruzando a San Aurelio al amanecer" | El galpón es del 26, es **la misma noche**, y el 28 no cierra con el cruce (eso es el 27): cierra con Kal saliendo hacia Varek | "La misma noche de la confrontación del taller (Cap. 26) y el amanecer del día 2. Abre con Kal llegando al loft; cierra con Kal saliendo a ver a Varek." |
| 28:6, 9–15 | Mecánica de H6 §1–§4 | Coincide con la prosa; revisar contra Hitos en E8 (housekeeping "mecánica antigua de H6") | E8 |
| 28:16 | "el sedán es del aparato de Halbrook (sembrado en el **Cap. 28**)" | Se siembra en el 27 | "Cap. 27" |
| 28:17, 19 | "Sólo se entenderá del todo en el **Cap. 31**" / "Preparan su función en el **Cap. 31** (Kal se las pedirá…)" | Las fotografías vistas juntos son inviolable del **30** | "Cap. 30" (confirmar en E2) |
| 28:24 | "se apoya en la siembra del **Cap. 26**" | Igual que 27:20 | "Parte I (H12)"; y si se aplica B2a, la nota pasa a "línea retirada por POV" |
| 28:27 | "Chiara sigue a Kal en su propio sedán (**Mercedes-Benz Clase S** del Monarch), no en el **Peugeot** de él — ficha de Chiara, ya fijado en los **Caps. 30-32**" | La prosa del 26 y del 29–30 dice **Lancia**; numeración vieja (hoy 29–31) | Según lo que se decida en D4 / E2 |
| 26–28 | Duración "dos días" implícita | — | Fijar "unas 24 horas" |

---

# § 9 Resultado (parte 1) — SURGERY de 26, 27 y 28 (E5, 2026-09-27)

**Comprobación previa:** `git diff --stat` vacío en los tres capítulos (coinciden con el estado auditado en E1; último commit `1af8c6a`). **Autoridad:** § Respuestas del autor, Q4 (veto libre). **Estado:** los tres siguen **BORRADOR**; nota de cirugía añadida en su línea de Estado.

**Palabras de prosa** (`wc -w` desde el encabezado): 26 = 2,309 → **2,254** (−55) · 27 = 2,535 → **2,438** (−97) · 28 = 3,020 → **2,794** (−226). **Total −378** (el mapa estimaba −345; la diferencia es B2 y las costuras). **Finales de línea:** 26 sigue CRLF (154 CR en 155 líneas; la última sin salto, igual que antes); 27 y 28 siguen LF. Verificado con `tr -cd '\r'`.

## Cap. 26

| # | Before | After | Categoría | Qué ya hacía la escena / qué conserva |
|---|---|---|---|---|
| C1 | "Chiara reconoció la frase antes de terminar de oírla. La había oído antes, con esas mismas costuras, en otra boca." | "Chiara reconoció la frase antes de terminar de oírla." | GLOSA | "—Esa la dice Kal." dice lo mismo en voz de ella. Conserva el reconocimiento |
| A3 | "para leer nueve palabras" | "para leer diez palabras" | MECÁNICA | El mensaje tiene diez palabras |
| C4 | "Walt la miró un segundo de más, como si el silencio le hubiera dicho lo que ella no." | "Walt la miró un segundo de más." | GLOSA | "—Va a levantarlas de todos modos" hace la lectura. Conserva la mirada |
| C5 | "…sobre la grava, y la conversación quedó cerrada sin que hiciera falta decirlo." | "…sobre la grava." | GLOSA de cierre | Las botas cierran la escena solas |
| A1 | "para la segunda noche entendió" | "para la noche entendió" | CRONOLOGÍA | Todo el 26 cabe en un día |
| A2 + C2 | "…dos noches atrás, en el agua, sin nada entre los dos: el convoy, el vidrio del parabrisas, el niño por la ventanilla, la prisión que cayó sobre él y no sobre el general." | "…la noche anterior, en el agua, sin nada entre los dos." | CRONOLOGÍA + REPETICIÓN FUNCIONAL (H15) | El lector acaba de leer la lista en el 25. Conserva que ella lo sabe todo y la copa en el tren |

**Conservado a propósito:** C3 (la máxima "Un hombre al que se llevan a rastras…", razonamiento de ella); las tres líneas canon de Varek, la de Walt, el motivo del clima y el pasaje del diablo sin nombrarlo; B7 (el cierre, lectura de Chiara).

## Cap. 27

| # | Before | After | Categoría | Qué ya hacía la escena / qué conserva |
|---|---|---|---|---|
| C6a | "…con el pulgar encima. Ella iba a pensar en Varek —era lo que tenía delante: la frase de Dario junto a la cama del hospital, *no por ella*, y la manera nueva en que la miraba en el piso de juego—. A Kal, Varek no le quitaba el sueño; ya habían estado los dos en un cuarto con las armas fuera y habían salido caminando. El peso de verdad…" | "…con el pulgar encima. El peso de verdad…" | REPETICIÓN FUNCIONAL | La decisión (IRONÍA CANON) vive en 146–150 con las mismas ideas. Conserva el borrador *no es Varek*, el peso de la carretera y "mirar hacia arriba". Sale el eco *no por ella* (vivo en el 25) |
| C7 | "…que ella todavía no había preguntado. Chiara iba a oír eso antes que las palabras. Iba a saber que él había calculado el susto y había salido a cortarlo por delante." | "…que ella todavía no había preguntado." | REPETICIÓN FUNCIONAL con 26:41 | El espejo de POV sobrevive en la primera mitad |
| D9 | "Le pedí que quede claro en qué punto estamos." | "Les pedí que quedara claro en qué punto estamos." | MECÁNICA | Concordancia; Halbrook habla ordenado |
| B5a | "Era gente con la que iba a volver a tratar, y de la gente con la que uno vuelve a tratar conviene saberlo todo." | "De la gente con la que uno vuelve a tratar conviene saberlo todo." | PROLEPSIS limítrofe (§L) | Baja la certeza del narrador; conserva el cálculo de Kal |
| A4 (D3a) | "Salió con las últimas luces y manejó toda la noche." | "Lo soltaron ya de noche y manejó hasta el amanecer." | CRONOLOGÍA | Las cuatro horas de recta y "tomó las curvas despacio" (144) se quedan; ya no hay contradicción de horas |
| A5 (D14) | "lo intuía por cómo había amanecido ella, midiendo el aire" | "lo intuía por cómo había subido ella, midiendo el aire" | CONTINUIDAD | Kal se fue con ella dormida. **Costura:** se quitó "esa madrugada" del texto aprobado porque la oración ya dice "de madrugada" |

**Conservado a propósito:** C8 (la otra vida por el cuerpo); B6 ("Dos costillas que iban a quejarse un mes"); los mensajes y sus horas; Halbrook entero; la siembra de Camp Alder (120) y del sedán (54, 112); el catálogo de los contratistas, incluido "caras que hubiera visto rondando a la gente de Varek".

## Cap. 28

| # | Before | After | Categoría | Qué ya hacía la escena / qué conserva |
|---|---|---|---|---|
| A6 | "demasiadas preguntas en dos días y las preguntas volvían" | "demasiadas preguntas y las preguntas volvían" | CRONOLOGÍA | — |
| A7 | "Los dos días anteriores se los había pasado casi enteros moviéndose entre… y una tarde, cerca de El Patio, lo vio ella misma: un sedán oscuro…" | "Desde que él se fue se había movido entre… Días antes, cerca de El Patio, había visto ella misma un sedán oscuro…" | CRONOLOGÍA | El avistamiento de El Patio queda antes de la salida (compatible con 27:54 y 28:74 "hace dos días"); el del loft, esa noche |
| A8 + C12 | "Varek le había dicho de madrugada, junto al jacuzzi, que no confiaba en Kal, que lo iba a investigar, que lo iba a hacer seguir. Chiara sumó… sin pestañear. Le sobraban motivos para hacerlo." | "Varek le había dicho esa madrugada que lo iba a hacer seguir. Chiara sumó una cosa con la otra sin pestañear." | CONTINUIDAD (lugar: ascensor, no jacuzzi) + REPETICIÓN de 26:43 + GLOSA | Conserva la atribución equivocada a Varek |
| A9 | "La primera noche daba tono. Desde el mediodía, la operadora." | "Las seis, la operadora." | CRONOLOGÍA (26:47) | — |
| B1 | "…sin que la calle la viera a ella. No era casualidad, y él sabía reconocer cuándo un cuarto dejaba de ser un cuarto para volverse un puesto." | "…sin que la calle la viera a ella." | SALTO DE POV | La enumeración ya es lo que Chiara ve que él ve; 68 lo dice desde ella |
| C10 | "…sin mirarla a ella ni una vez. No era que no quisiera que lo tocara. Era que necesitaba decidir él mismo cuánto cuidado aceptaba, y ella, que llevaba media vida…" | "…sin mirarla ni una vez. Ella, que llevaba media vida…" | GLOSA + REPETICIÓN con 88 | 88 ya da el permiso que le cuesta. **Costura:** se quitó "a ella" para no encadenar "a ella. Ella" |
| A13 (D6) | "Un coche, dos veces, con la placa legible." | "Un coche de los Bravos, dos veces, con la placa legible." | CONTINUIDAD (referente) | Separa el coche fotografiado del sedán sin placa |
| C11 | "Chiara entendió, por todo lo que él no dijo, que el material servía." (párrafo) | — | COMPETENCIA EXPLICADA | "No corrigió un solo horario. No preguntó cómo había conseguido la placa." lo dice |
| C14 | "Eso dolió más de lo que debería haber dolido una frase tan corta. Chiara se quedó con las manos quietas…" | "Chiara se quedó con las manos quietas…" | EMOCIÓN EXPLICADA | Las manos quietas hacen el trabajo |
| A11 | "lo que sea que hiciste anoche" | "lo que sea que hiciste ayer" | CRONOLOGÍA | — |
| C15 | "…cómo pesaba del otro lado. Le ofrecía la puerta abierta en los dos sentidos: la de salir de la ciudad y la de salir de ella. Era lo único…" | "…cómo pesaba del otro lado. Era lo único…" | GLOSA | "las dos veces, la del viaje… y la que él mismo acababa de proponer" ya da el doble sentido. Conserva Palermo, la mano encima y la correa del título |
| A12 | "los dos días que él estuvo sin dar señales" | "mientras él estuvo sin dar señales" | CRONOLOGÍA | — |
| B2a (D7) | "Kal se quedó muy quieto. A él se lo había dicho de pie junto a una cama de hospital… A ella se lo había dicho en un galpón helado, sola, a kilómetros de cualquier sitio." | "Kal se quedó muy quieto. Bajó los ojos un instante…" | SALTO DE POV / conocimiento imposible | La escalada queda en "Nada de eso le había movido los hombros. / Esto sí.". **Costura:** se unió con el párrafo siguiente para no abrir dos párrafos seguidos con "Kal" |
| C16 | "…y volvió a mirarla a ella. No dijo nada más de lo necesario, pero algo en cómo apretó la mandíbula le dijo a Chiara que la frase acababa de caerle en un sitio que él no esperaba." | "…y volvió a mirarla a ella. Apretó la mandíbula." | REPETICIÓN FUNCIONAL + contra la metadata ("sin nombrarlo") | El gesto queda; la lectura la hace 226–228 |
| B3 | "Supo que faltaba algo. No insistió. Chiara supo…" | "Kal no insistió. Chiara supo…" | SALTO DE POV | "¿Eso fue todo?" / "Fue suficiente." ya muestra que él nota el hueco |
| C17 | "…no servía de nada. Eso lo tuvo claro enseguida; era la clase de cosa que siempre tenía clara." | "…no servía de nada." | COMPETENCIA EXPLICADA | — |
| B4 | "No sabía todavía para qué las iba a necesitar. Sólo sabía que no iba a dejar información útil…" | "No iba a dejar información útil…" | PROLEPSIS DE NARRADOR (§L) | Las fotos siguen saliendo con ella; el 30 las cobra |

**Conservado a propósito:** la columna 160–168 ("No vuelvas a hacer algo así sola" → "Sonó como una."), H6 §2, "¿Nos podemos reunir?", la tercera línea guardada "desde Palermo" (218), la sudadera y "La otra razón… no necesitaba que la nombraran" (C13), 88, 142, 174, 186 (interioridad), C18 ("Fue lo más parecido a una disculpa…"), C19 ("Bien… no significaba nada…"), las 16 preguntas con punto (C20, firma), "dos costillas rotas" (A14, inferencia de ella), el **Peugeot** en 50 y 246 (D15: es el ancla; el Audi del 29–30 se corrige en E6).

## Metadata saneada

- **26:** nombre de la Parte II; "La mañana siguiente a H15… todo el capítulo cabe en ese día"; "Walt recibió"; ritual del *Ciao*: nace en el 35, nunca *Ciao, bello* (D52).
- **27:** nombre de la Parte II; "el mismo día que cubre el Cap. 26 (unas 24 horas)"; mensajes "citados en Cap. 26"; "Prepara el Cap. 28" (era 29: los indicios del sedán los detecta Chiara en el 28; corrección de numeración no listada en E1); relectura "tras el Cap. 30"; versión de Kal "desde el Cap. 25"; siembra "de la Parte I (H12)" con nota del corte C6a; Halbrook llega a la coda que cierra el **Libro II**.
- **28:** nombre de la Parte II; ventana temporal reescrita (misma noche del galpón, amanecer siguiente, abre en el loft y cierra con Kal saliendo a ver a Varek); sedán "sembrado en el Cap. 27"; fotografías en el **Cap. 30** (17 y 19); nota de que la línea de escalada se retiró por POV (D7); Chiara en el **Lancia**, el Mercedes es corporativo, autos fijados en D15.
- **No se tocó (E8):** la mecánica de H6 §1–§4 en 28:6–15, que coincide con la prosa y se revisa contra Hitos en el housekeeping.

## Autocrítica E5 (MICROEDICION §F)

- **Lo más dudoso:** A4, "Lo soltaron ya de noche". Resuelve las horas, pero "soltaron" le da a la reunión un matiz de retención que la escena (corta, con Halbrook que "tiene un vuelo") no muestra; deja implícito que lo tuvieron esperando. Si el autor lo lee como un hueco, la alternativa (b) de D3 sigue disponible.
- **Lo más agresivo:** B2a (−52): retira una línea de DISEÑO con buen ritmo. La justifica el POV único; la escalada sobrevive en "Esto sí.".
- **Pareció corte y quedó protegido:** C13 y C18 en el 28 (glosas en apariencia, pero son voz de Chiara y cierres de sección); C3 en el 26.
- **Riesgo de esterilizar:** bajo. Los cortes del 28 quitan narrador que traducía gestos; los gestos (manos quietas, mandíbula, las fotos alineadas) quedaron todos.
- **Racionalizar interioridad:** no. C10 conserva lo de ella ("media vida aprendiendo cuándo no acercarse") y quita sólo lo que el narrador decía de él.
- **Prosa más genérica:** las únicas palabras nuevas son de cronología ("Desde que él se fue", "Días antes", "Las seis, la operadora", "Lo soltaron ya de noche") y "de los Bravos". Las tres costuras fueron sólo cortes o uniones.

---

# Parte 2 — Caps. 29 y 30 (E2)

## 0. Diagnóstico corto

- **29 (LIGERA–MEDIA).** La negociación funciona: Kal no se ofrece, Varek nombra la silla, "Bellandi no", la actuación conjunta y "Estás loco" están bien construidos. Cuatro cosas: el **bug del auto** (Kal sale del loft en el Peugeot y llega en un Audi), la **mesa con demasiadas semillas** (Vivian, el puerto, la pelirroja, de dónde sabe Vivian el nombre de Kal) con una glosa larga que explica la escena de Vivian que el lector acaba de ver, tres continuidades chicas (la "curiosidad que había prometido por teléfono" que la llamada no contiene, Varek que se sienta dos veces, el tú aislado de "Te trataron mal") y una **certificación con salto de POV** en la prueba de sincronía (253). Tics locales: "un grado" ×3, "dos veces" ×4.
- **30 (PROFUNDA).** El capítulo hace todo lo que el dictamen pide que haga, y lo hace **dos veces**: la prosa narra el trato del 29 tres veces (el 29 en escena, Kal a Chiara en 115–157, Kal al grupo en 475–479), cierra cada beat con una glosa que explica cómo cambiaron ("era su manera de decir que algo había cambiado", "No era lo mismo que… Aquí había negociado…", "lo que acababa de aprender esa misma mañana… a hacer distinto") y entra en la cabeza de Kal siete veces dentro de la sección de Chiara. El **plan contra Varek** (339–359) da el mecanismo de la caída de Dario ("uno por uno, los pedazos… no queda nada que sea sólo suyo", "cómo se desmonta un imperio"), que pertenece al Libro III. Cronología: seis referencias de "dos días"/"anoche". Continuidad: Kal pregunta "¿Qué sedán?" cuando Walt se lo había contado en el 27. Tics: la familia "sin adornarlo / no lo suavizó" ×8, "guardó donde guardaba" ×3 (×5 contando 28–29), "terminara de asentarse" ×2 (×3 con el 29). **Todos los inviolables sobreviven a la poda propuesta**; lo que baja es glosa, recapitulación, salto de POV y certeza.

## 1. Candidatos por categoría (29 y 30)

### A. Continuidad y mecánica

| # | Cap:línea | Texto | Problema | Propuesta | Palabras |
|---|---|---|---|---|---|
| A15 | 29:279 · 30:43 | "caminó hacia el **Audi**" / "detuvo el **Audi** junto a un roble solo" | 28:50 y 28:246 lo hacen salir del loft en el **Peugeot** minutos antes (y 28:50 es un reconocimiento: "El Peugeot."). Kal tiene los dos autos (el Audi A7 es el segundo auto del Cap. 9; el 31 y el 34 lo usan a propósito; el 43 vuelve al Peugeot) | **D15:** "hacia el **Peugeot**" y "detuvo el **Peugeot**". El 31 sigue en el Audi: entre el 30 y el 31 Kal pasa por el taller, donde cambia de coche sin que haga falta decirlo. Son las dos únicas menciones de Audi en 29–30 | 0 |
| A16 | 29:109 | "…la curiosidad genuina **que había prometido por teléfono**." | La llamada del 29:33 son cuatro palabras de Varek: *Ven ahora. Sabes dónde.* No promete nada | "…algo que no estaba en las anteriores: la curiosidad genuina." | −4 |
| A17 | 29:33 | "La llamada había durado **nueve palabras de él**" | 28:240 sólo deja oír "¿Nos podemos reunir?" (tres); Chiara oye el principio y la puerta se cierra | DUDOSA — CONSERVAR: el resto lo dijo en la escalera; no hay contradicción | 0 |
| A18 | 29:57 / 59 | "…antes de sentarse él." / "—dijo Varek, **sentándose por fin**—" | Varek se sienta dos veces | Cortar "sentándose por fin": "—No pregunto qué pasó —dijo Varek—." | −3 |
| A19 | 29:53 | "—Mercer. … **Te** trataron mal." | Único tú de Varek antes del trato; todo lo demás es usted hasta "Tu Chiara" (219, canon) y el 39 ("tendrás tu ventana") | **D20.** DUDOSA — CONSERVAR (recomendado): el tú al herido es condescendencia de dueño, rima con "Tu Chiara". Si el autor quiere el usted limpio hasta el trato: "Lo trataron mal." | 0 |
| A20 | 29:283 | "el **gris** del Lancia" | 25:33: "el Lancia **oscuro**" | DUDOSA — CONSERVAR: gris oscuro es compatible. Se reporta | 0 |
| A21 | 29:19 / 30 fotos | Metadata: las fotografías "vuelven en el Cap. 31" | Vuelven en el 30 (inviolable) | Metadata, E6 | — |
| A22 | 30:71, 79, 101, 111, 195, 245 | "dos días" / "anoche" / "la noche anterior" / "el día anterior" | Cronología fija (§ Cronología) | Las seis correcciones de la tabla de § Cronología | ±0 |
| A23 | 30:409 · 30:435 | "por lo de anoche" (Kal) / "Podías anoche" (Nadir) | En habla | CONSERVAR (resuelto en § Cronología) | 0 |
| A24 | 30:493–499 | "—¿Y el sedán? … —**¿Qué sedán?** … —El que Walt vio dos veces cerca de aquí. … Nadir también lo vio. **No dijimos nada porque no había nada que decir**" | Kal lo sabe: Walt se lo contó (27:54, 27:112) y lo habló con Chiara en el 28 y en el 30:65. El "No dijimos nada" contradice que Walt se lo dijera. 505 ("No dos tardes después") sí depende de que Walt avisó tarde | **D18.** Kal: "—**¿Lo volvieron a ver?**" · Héctor: "—**Walt no fue el único.** —Héctor no levantó la voz—. Nadir también lo vio. No lo dijimos porque no había nada que decir, pero ya que estamos contando todo." | ±0 |
| A25 | 30:475 | "Le ofrecí el cargamento, **el mismo armamento largo que Halbrook mueve para pagar favores.**" | Dato nuevo sin pago y en contra de la mecánica fijada: las armas largas son las que se **roban** de Camp Alder por encargo de Halbrook (Hitos H19; ficha de Halbrook) y el pago a Varek (Hitos l. 1623) | **D19:** cortar la aposición (se funde con C46) | −10 |

### B. Prolepsis y saltos de POV

El 29 es POV único de Kal. El 30 es POV de Chiara hasta el corte de 399 y POV de Kal en la coda (excepción autorizada por el autor; limpia: no vuelve). Todos los saltos están en la sección de Chiara.

| # | Cap:línea | Texto | Categoría | Propuesta | Palabras |
|---|---|---|---|---|---|
| B8 | 30:63 | "—Se lo dijo directo, sin adornarlo, **sabiendo exactamente el peso que le estaba quitando de encima a una parte de ella y el que le estaba poniendo a otra**—" | SALTO DE POV + TIC (C59) | "—Se lo dijo directo—." | −26 |
| B9 | 30:233 | "Chiara no contestó eso, **y el silencio duró lo suficiente como para que ambos entendieran que la pregunta no necesitaba respuesta esa mañana.**" | SALTO DE POV ("ambos entendieran") + GLOSA | "Chiara no contestó eso." (251 hace el trabajo desde ella) | −20 |
| B10 | 30:301 | "—dijo, al fin, **sabiendo cómo sonaba en cuanto lo dijo en voz alta.**" | SALTO DE POV | "—dijo, al fin." | −9 |
| B11 | 30:309 | "Kal se quedó con la mandíbula tensa un momento, **midiendo la distancia entre lo que quería hacer y lo que acababa de aprender esa misma mañana, en esa misma roca, a hacer distinto.**" | SALTO DE POV + GLOSA de cambio (dictamen) | "Kal se quedó con la mandíbula tensa un momento." La línea siguiente ("una orden con otro nombre") dice el aprendizaje en su boca | −25 |
| B12 | 30:365 | "No se dieron la mano. **No hacía falta un gesto para sellarlo; los dos sabían, sin decirlo, que la palabra ya pesaba lo suficiente.**" | SALTO DE POV + GLOSA | "No se dieron la mano." | −20 |
| B13 | 30:375 | "Kal se quedó callado un momento, **buscando cómo decir lo que seguía sin que le pesara más de lo que ya le pesaba.**" | SALTO DE POV | "Kal se quedó callado un momento." (la pausa antes de la línea titular se conserva) | −17 |
| B14 | 30:379 | "Chiara no dijo nada. **No hacía falta decir nada, y** los dos se quedaron un momento así, con el agua cubriendo el silencio, **sin que ninguno de los dos sintiera la necesidad de llenarlo con algo más.**" | GLOSA + SALTO DE POV | "Chiara no dijo nada. Se quedaron un momento así, con el agua cubriendo el silencio." | −20 |
| B15 | 29:253 | "…ni la tentación **—que los dos sintieron, y los dos apagaron en el mismo instante—** de mirarse…" | SALTO DE POV (Kal no puede saber lo que ella sintió) | Se resuelve con C33 | — |
| B16 | 30:73 | "—dijo Kal, **como si le hubiera leído el pensamiento**—" | Comparación desde Chiara | DUDOSA — CONSERVAR (es un "como si", no un dato) | 0 |
| B17 | 29:37 · 29:277 | "la otra mitad se la iba a cobrar en cuanto se detuviera" → "el costado empezara por fin a cobrarle la cuenta completa" | Expectativa de Kal y su cobro en el mismo capítulo | PROTEGIDO (no es prolepsis de narrador; es eco interno) | 0 |
| B18 | 30:343 | "como si estuviera describiendo cómo se arregla un motor **y no cómo se desmonta un imperio**" | Límite de §L: símil de Chiara que nombra el final del arco de Dario (Libro III) | Se resuelve en § Plan contra Varek | — |

### C. Glosa, tic, repetición y certificación

**Cap. 29**

| # | Línea | Texto | Categoría | Propuesta | Palabras |
|---|---|---|---|---|---|
| C21 | 29:43 | "…llevaba la cuenta de dónde estaba, **sin que nadie tuviera que decírselo dos veces.**" | REPETICIÓN LEXICAL ("dos veces" ya en la misma frase: "que se identificara dos veces") | Cortar la cláusula. "Eso también era información." se protege | −8 |
| C22 | 29:57 | "Era temprano para beber y los dos lo sabían, y ninguno lo dijo, porque decirlo hubiera sido admitir que la hora tenía algo que ver con lo que venía." | GLOSA leve | DUDOSA — CONSERVAR: es el cálculo de Kal y la regla del capítulo (nada se dice que pueda usarse) | 0 |
| C23 | 29:69 · 85 · 207 | "no cambió la expresión **ni un grado**" / "cambió de todos modos, **un grado**" / "algo en su cara se movió **un grado**" | TIC | Conservar el de 85 (la nube; es la imagen). 69: "Varek no cambió la expresión." · 207: "algo en su cara se movió, como cuando…" | −6 |
| C24 | 29:71 | "Kal tardó, aun así, medio segundo de más en hablar primero **— el primero de la mañana en que dudó antes de decir algo.**" | GLOSA (subraya lo que el "medio segundo de más" ya dice) | "Kal tardó, aun así, medio segundo de más en hablar." | −14 |
| C25 | 29:95 | "…conseguir la palabra que quiere **sin tener que pedirla dos veces.**" | REPETICIÓN LEXICAL (cuarto "dos veces") | Opcional, con C21: cortar la cláusula. DUDOSA — si se conserva, que sea éste y no el de 43 | (−6) |
| C26 | 29:107 | "Dejó que el silencio hiciera el trabajo que cualquier explicación hubiera arruinado." | GLOSA leve | DUDOSA — CONSERVAR: es el método del capítulo dicho una vez | 0 |
| C27 | 29:147 | "**Fue todo lo que dijeron sobre el tema, y fue suficiente.** Varek no se levantó…" | GLOSA | Cortar la primera oración; la puerta entornada cierra | −11 |
| C28 | 29:167 | "…que ya sabía que iba a cuadrar. **No miró a Kal para explicarle nada, y no hacía falta: la escena hablaba sola. La hija cerrando negocio de puerto delante del padre… antes de sentarse.**" | GLOSA (explica la escena que el lector acaba de leer: "la escena hablaba sola" y después la habla) — foco del dictamen: compactar Vivian | Cortar desde "No miró a Kal…" hasta el final del párrafo | −68 |
| C29 | 29:177 | "No preguntó quién. **No preguntó de qué universidad, ni de qué taller, ni por qué su mundo y el de esta mujer que acababa de cerrar un trato de puerto delante de su padre compartían, aunque fuera por una frase de nada, un aula.** Preguntar hubiera sido dibujar un círculo." | REPETICIÓN FUNCIONAL (Vivian y el puerto por tercera vez en veinte líneas) + la conclusión que el 30:291 dice en boca de Kal | "No preguntó quién. Preguntar hubiera sido dibujar un círculo. Levantó el vaso…" (el primer trago, canon, se queda) | −45 |
| C30 | 29:185 | "No fue una pregunta ni una presentación. **Kal no supo, y no lo iba a preguntar, si sabía su nombre por negocios, por el Monarch, por algo que su padre había dicho, o porque en esa casa las cosas simplemente se sabían.**" | "Demasiadas semillas en una mesa" (dictamen) | **D22.** (a, recomendada) "Kal no supo de dónde sabía su nombre." (b) conservar: la lista es el temperamento de Kal y dice cómo funciona la casa | −25 |
| C31 | 29:245 | "Era la misma cara que le había visto horas antes, en la cocina del loft… Y Kal, al mismo tiempo, sin haberlo hablado, sin haberlo ensayado ni una vez, entendió exactamente lo mismo que esa habitación necesitaba de él." | INTERIORIDAD | PROTEGIDO: la memoria del loft es de Kal; la sincronía se cuenta desde él | 0 |
| C32 | 29:223 | "Tampoco le creyó del todo, **y Kal lo supo por cómo la sonrisa que le siguió no le llegó a los ojos.**" | Fórmula gastada | DUDOSA — CONSERVAR: es la lectura de Kal; se reporta el cliché | 0 |
| C33 | 29:253 | "**Fue perfecto, y fue rápido, y no tuvo ni un gramo de más.** Varek los miró… No llegó. **Ninguno de los dos improvisó peor que eso: ni un gesto de más, ni una palabra que sobrara, ni la tentación —que los dos sintieron, y los dos apagaron en el mismo instante— de mirarse el tiempo suficiente como para que significara algo.**" | COMPETENCIA EXPLICADA + SALTO DE POV (B15). "Ninguno de los dos improvisó peor que eso" además se lee al revés | **D21.** (a, recomendada) "Varek los miró a los dos… esperando el cruce de miradas que los delatara. No llegó. Kal sintió la tentación de mirarla el tiempo suficiente como para que significara algo, y la apagó." (b) cortar todo después de "No llegó." | −40 / −62 |
| C34 | 29:271 | "Lo dijo como quien constata el clima" | Motivo del clima (26) | PROTEGIDO | 0 |

**Cap. 30**

| # | Línea | Texto | Categoría | Propuesta | Palabras |
|---|---|---|---|---|---|
| C37 | 30:69 | "—No lo sé con certeza. **—Fue honesto, y eso pesaba más que una respuesta segura—.** Pero ahora sé…" | GLOSA | "—No lo sé con certeza. Pero ahora sé…" | −9 |
| C38 | 30:83 · 131 · 343 · 359 | "como quien admite un defecto de fábrica en una máquina" / "con el que un mecánico describe una falla que ya reparó" / "cómo se arregla un motor" / "resuelto una ruta de entrega" | REPETICIÓN SINTÁCTICA: cuatro símiles de oficio para el tono de Kal | Conservar el de 83 (el mejor, y va con la confesión "llevo toda la vida sin saber compartir"). Los otros tres caen con C44, § Plan y C54 | — |
| C39 | 30:89 | "**Chiara hizo la cuenta sin que hiciera falta que él la dijera en voz alta: Halbrook, el golpe, el loft, Varek, y ahora esto, una crisis montada sobre la otra sin un solo momento libre para volver a su propia gente.**" | RECAPITULACIÓN (el lector acaba de leer 27–29) | Cortar el párrafo; "No he visto a nadie desde que Halbrook me sacó de la ciudad" ya lo dice | −40 |
| C40 | 30:95 · 169 | "escuchando el agua, **dejando que la frase terminara de asentarse antes de decidir qué hacer con ella.**" / "**Chiara dejó que eso terminara de asentarse.**" | TIC (29:273 lo dijo primero, y mejor, tras "Estás loco") | 95: "Chiara se quedó con eso un momento largo, escuchando el agua." · 169: cortar la oración; queda "No era una solución: era un techo…" | −21 |
| C41 | 30:99 | "No sintió el impulso de reclamarle nada… un hombre sin salidas va a golpear la única puerta que conoce — y entender no era lo mismo que estar contenta." | INTERIORIDAD | PROTEGIDO | 0 |
| C42 | 30:109 · 111 | "Un hombre que no se defendía dejaba menos espacio para pelear…" / la tercera línea guardada y "no se creyó del todo su propia distinción" | INTERIORIDAD; simetría canon con la omisión de Kal | PROTEGIDO (sólo la cronología de A22) | 0 |
| C44 | 30:131 | "**Se lo dijo sin adorno, casi con el mismo tono con el que un mecánico describe una falla que ya reparó.** Chiara lo miró un momento, **reconstruyendo la frase por dentro antes de decir en voz alta lo que ya había entendido.**" | GLOSA (anuncia la línea siguiente) + TIC + C38 | "Chiara lo miró un momento." | −40 |
| C45 | 30:141 · 269 | "**Lo guardó donde guardaba todo lo que todavía no sabía qué hacer con ello.**" / "**Chiara guardó eso donde guardaba lo que todavía no podía usar.**" | TIC: "guardar donde guardaba" ×5 en 28–30 (28:218 canon; 29:189 Kal y la pelirroja; 30:111 la tercera línea; 30:141; 30:269) | Cortar 141 y 269. Se quedan 28:218, 29:189 y 30:111 (tres personajes-momentos distintos). El resto de 141 (el camaleón sin la palabra, "podría usarse contra ella") se protege | −23 |
| C46 | 30:475 · 479 | "Necesitaba una puerta a Camp Alder… Le ofrecí el cargamento, el mismo armamento largo… No le bastó. Terminó ofreciéndome…" / "**—No lo adornó—.** Eso no resuelve lo de Nadir. **No toca el papel, no toca a Halbrook, no toca Camp Alder.** Compra presión local, nada más. **Si alguien intenta algo aquí, primero tiene que pasar por Varek.** Y Varek no sabe por qué me importa. No le di el nombre." | REPETICIÓN FUNCIONAL: tercera narración del trato, casi con las palabras de 173 | 475: "—Necesitaba una puerta a Camp Alder. Fui a pedírsela a Varek esta mañana. Terminó ofreciéndome algo más grande: una silla en su mesa." · 479: "—Mientras esté sentado ahí, la gente que reconozca como mía queda bajo su nombre. Eso no resuelve lo de Nadir. Compra presión local, nada más. Y Varek no sabe por qué me importa. No le di el nombre." El grupo recibe lo que necesita; el lector no lo relee | −45 |
| C47 | 30:195 | "Chiara entendió las dos cosas al mismo tiempo… sin contradecirse. **No era lo mismo que el día anterior, en el loft —ahí decidía por ella. Aquí había negociado una condición que le dejaba a ella la decisión abierta, sin pedirle permiso para intentarlo y sin quitárselo después.**" | GLOSA sobre cómo han cambiado (dictamen) + cronología | Cortar desde "No era lo mismo…". La columna protegida la cobra la escena de Marisol ("Ya sabes cómo termina eso") | −45 |
| C48 | 30:207 | "Preguntó permiso, **y eso, viniendo de él, era su manera de decir que algo había cambiado.**" | GLOSA de cambio | "Preguntó permiso." | −14 |
| C49 | 30:217 | "Se quedaron así un momento, **cada uno mirando la misma imagen y viendo cosas distintas: Kal veía calles, salidas, territorio; Chiara veía nombres, deudas, quién trabajaba para quién.** Ninguno de los dos había visto la fotografía completa hasta que la vieron juntos." | GLOSA (el diálogo de 211–215 acaba de mostrarlo) | **D26.** (a, recomendada) cortar la enumeración: "Se quedaron así un momento. Ninguno de los dos había visto la fotografía completa hasta que la vieron juntos." (la última oración es la tesis de la alianza; se protege). (b) cortar el párrafo | −24 / −44 |
| C50 | 30:251 | "Chiara construía redundancias… se había saltado todas las capas sin darse cuenta." | INTERIORIDAD (motivo "Kal se volvió su único plan"; ver P3) | PROTEGIDO | 0 |
| C51 | 30:259 · 267 | "En el patio de Varek había una mujer. Su hija. **Entró como quien entra a su propia casa, cerró un trato de puerto delante de él —cifra, contraoferta, hecho— y se fue sin pedirle permiso a nadie. Varek la trató como algo normal.**" / 267: "Sé que cerró un trato delante de su padre y que él no la corrigió por hacerlo, sólo por el precio." | REPETICIÓN FUNCIONAL dentro del 30 y con la escena del 29 (foco: compactar Vivian → Marisol) | 259: "—En el patio de Varek estaba su hija." Se queda 267 entero | −30 |
| C52 | 30:283 | "haciendo el mismo cálculo que él ya había hecho en el patio" | Inferencia de Chiara | DUDOSA — CONSERVAR | 0 |
| C53 | 30:291 · 307 · 311 | "dos mundos que llevo años manteniendo separados…" / "Lo dijo como quien señala un mapa… Ya sabes cómo termina eso." / "una orden con otro nombre" | Columna protegida (aplicación de "no decidas por mí") | PROTEGIDO | 0 |
| C54 | 30:359 | "**No había en su cara ni en su voz nada que sonara a discurso, nada que sonara a plan escrito en una servilleta: sonaba exactamente a él, resolviendo un problema en voz alta de la misma manera en que hubiera resuelto una ruta de entrega. Y por eso, precisamente por eso, le creyó entero.**" | GLOSA + C38 (y certifica que no es un plan justo después de un plan) | Ver § Plan: "Chiara lo miró." o cortar hasta "—De acuerdo —dijo—." | −45 |
| C55 | 30:415 | "—Kal lo miró directo, **algo que no había logrado hacer con Chiara hasta que no le quedó otra opción**—." | GLOSA: señala la rima Chiara/Nadir que la metadata pide "no señalada" | "—Kal lo miró directo—." | −13 |
| C56 | 30:419 · 437 | "No era pregunta. Era la manera de repetir algo…" / "No dijo *era para protegerte*, ni *no había tiempo*…" | Lectura de Kal / eco sintáctico de 29:273 | DUDOSA — CONSERVAR: el eco del "no dijo" es la rima de conducta entre las dos confrontaciones | 0 |
| C57 | 30:443 | "—preguntó, **y con eso la conversación cambió de forma: dejó de ser sobre lo que Kal había hecho mal y pasó a ser sobre lo que había que hacer.**" | GLOSA (la pregunta ya es la agencia de Nadir) | "—¿Qué sabe exactamente? —preguntó." | −24 |
| C58 | 30:461 | "**Eso se quedó flotando el tiempo suficiente para que todos entendieran el tamaño real de lo que se acababa de decir.**" | GLOSA | Cortar; Danny entra con la pregunta | −21 |
| C59 | 30 (8 casos) | "sin adornarlo" (63), "sin adorno" (131), "sin dulcificarlo" (185), "no se anduvo con rodeos" (409), "No lo suavizó" (459), "sin adornarlo, porque adornarlo hubiera sido peor" (469), "No lo adornó" (479); más 29:101 | TIC de acotación | Conservar 185 (Bellandi), 409 ("No con ellos") y 459 (antes de "instalación federal"). Los demás caen: 63 (B8), 131 (C44), 469 → "—Todavía no tengo salida. No tengo un plan completo…" sin acotación, 479 (C46) | −10 |
| C60 | 30:481 | "Walt asintió despacio, **el tipo de asentimiento que en él equivalía a haber entendido el mapa completo de una sola pasada.**" | COMPETENCIA EXPLICADA (483 la demuestra) | "Walt asintió despacio." | −17 |
| C61 | 30:491 | "un gesto que Kal conocía desde niño" | — | PROTEGIDO: Héctor lo crió (ficha) | 0 |
| C62 | 30:507 | "Nadie preguntó por Varek… y Kal no les dio ninguna." | Misterio deliberado (Halbrook y Varek no coordinados) | PROTEGIDO | 0 |
| C63 | 30:511 | El peso repartido de cada uno | Recuento | DUDOSA — CONSERVAR: es la pausa que Nadir rompe; lectura de Kal | 0 |
| C64 | 30:391 | "…**lo cual, viniendo de él, era casi una declaración**" | GLOSA leve | DUDOSA — CONSERVAR (coqueteo en voz de Chiara; con C48 queda el único "viniendo de él") | 0 |

*(C35, C36 y C43 quedaron sin usar al consolidar la tabla.)*

**Suma aproximada de lo recomendado (sin DUDOSAS):** 29 ≈ −225 (con C30a y C33a) · 30 ≈ −610 (con V2 del plan, C49a y C54). Referencia, no meta (§J); el 30 queda en ≈ 4,170.

## 2. Prolepsis y POV — lectura por capítulo

- **29 (POV Kal, único).** Limpio de prolepsis. Un salto (B15, la tentación "que los dos sintieron"). Las inferencias sobre Varek (69, 85, 217, 223) son lectura de Kal y se protegen. "Varek sabía qué era Camp Alder" (85) es inferencia por conducta, no dato.
- **30 (POV Chiara → corte → POV Kal).** La excepción de POV es del autor y está bien ejecutada: un solo corte (399), Chiara ya fuera. Dentro de la sección de Chiara hay **siete** entradas a la cabeza de Kal (B8–B14): es la capa que más trabajo pide después del plan. La coda de Kal está limpia. Prolepsis: ninguna de narrador en sentido estricto; el plan (339–343) y el símil del "imperio" (B18) son certeza de personaje sobre el Libro III y se tratan en § Plan.

## 3. Función por movimiento

**Cap. 29 (2,979)**

| Líneas | Movimiento | Palabras | Función | Veredicto |
|---|---|---|---|---|
| 33–45 | El camino, el cuerpo, la casa que ya sabe su nombre | 339 | Costura con el 28; dolor aplazado (se cobra en 277) | C21. Resto intacto |
| 49–59 | El patio, el bourbon, "Te trataron mal" | 223 | Registro de la casa | A18, A19; C22 conservar |
| 61–71 | "¿El Lancia? / Sigue ahí. / Déjala." | 140 | Siembra de la prueba de Varek | C23, C24 |
| 73–147 | Camp Alder, la promesa, la silla, el paraguas | 496 | **Núcleo canon** (Kal no se ofrece; Varek nombra la silla; "La que usted reconozca como suya") | A16, C27; C25, C26 dudosas. Diálogo intacto |
| 151–189 | Vivian, el puerto, la pelirroja | 525 | Siembra Vivian + Marisol; primer trago | C28, C29, C30. Queda ≈ 390 |
| 193–237 | "Bellandi no", "un activo", "Tu Chiara", cuarenta y tres minutos | 415 | Chiara como activo; la prueba | C23. Intacto el diálogo |
| 241–261 | Chiara en el patio, "la misma habitación", "Bienvenido" | 411 | Actuación conjunta, canon | C33 (B15); C31 protegido |
| 265–279 | "Estás loco." Kal no la sigue | 242 | Canon; Kal no decide por ella | Intacto (A15 en 279) |
| 283–293 | La carretera, las luces, el Lancia detrás | 175 | Ella elige la ruta | Intacto |

**Cap. 30 (4,783) — los movimientos del dictamen**

| Líneas | Movimiento | Palabras | Función y pagos | Veredicto |
|---|---|---|---|---|
| 43–55 | Llegada a Las Cascadas; "Te voy a contar todo" | 217 | Terreno neutral; promesa de verdad | **Conservar** (A15 en 43) |
| 59–73 | **Halbrook** ("Warren Halbrook") + sedán + **Kal admite el antagonista equivocado** | 247 | Dos inviolables; paga 27 y 28 | **Conservar**, con B8 y C37. El sedán queda sin resolver (paga 32, Irene) |
| 75–95 | **La mentira de Kal**: golpes, "¿por qué no me lo dijiste?", "llevo toda la vida sin saber compartir", Nadir no lo sabe, "la mitad de la baraja" | 280 | Título del capítulo (93); Nadir como palanca | **Conservar**, comprimir: C39 (−40), C40, A22 |
| 99–111 | Chiara no reclama; "No me gusta"; guarda la tercera línea | 255 | Interioridad; simetría de omisiones (P3 del 31 la necesita viva) | **Conservar** (sólo A22) |
| 115–177 | **La silla** + **Nadir** bajo el paraguas | 386 | Inviolable (explicación de la silla); "No le pediste la silla / Hiciste que te la ofreciera"; 33:89 y 39 cobran la silla y la puerta | **Conservar** el diálogo; **comprimir** C44 (−40), C45, C40 |
| 179–195 | **Chiara como activo** ("Bellandi no") | 140 | Inviolable; paga "no decidas por mí" | **Conservar** el diálogo; **cortar** la glosa C47 (−45) |
| 199–217 | **Fotografías** vistas juntos | 264 | Inviolable; paga 28 | **Conservar**; C48, C49 (−38) |
| 219–251 | ***i Sussurri***, "sususus", "¿Y por qué fuiste?" | 256 | Inviolable (nacimiento funcional); motivo de Chiara (251) | **Conservar**; B9, A22 |
| 255–269 | **Vivian** | 126 | Chiara aprende que Vivian participa | **Comprimir**: C51 (−30), C45 |
| 271–313 | **Marisol** ("¿Y qué le vas a decir?") | 277 | Aplicación de la columna; cobra 33 | **Conservar**; B10, B11 (−34) |
| 315–333 | **Kenji** ("Oda / el de la caja") | 126 | Siembra del 33 | **Conservar** (E4 comprueba el pago) |
| 337–355 | **Estrategia conjunta** + **Varek futuro** | 194 | Pacto (inviolable) / mecanismo de la caída (Libro III) | **Cortar la certeza**: § Plan (V2 −55). Se conserva 353–355 (El Patio + *i Sussurri*) |
| 357–365 | "Alineados" | 89 | El pacto con nombre | **Conservar** la palabra; C54, B12 |
| 369–379 | **Línea titular** | 135 | Inviolable | **Conservar** la línea; B13, B14 (−37) |
| 383–397 | El pantalón; se separan sin mirar el espejo | 183 | Coda ligera; la unión sin proximidad | **Conservar** (C64 dudosa) |
| 401–407 | **El Patio**: el taller, los cuatro | 157 | Textura; A23 | **Conservar** |
| 409–443 | **Nadir descubre que fue usado** | 333 | Inviolable (se entera por Kal); rima con Chiara; recupera agencia | **Conservar**; C55, C57 (−37) |
| 445–469 | **Camp Alder**: la base, la llave, "¿Cómo sales?" / "Todavía no tengo salida" | 339 | Inviolables (Danny; no hay plan completo); cobra 39 y H19 | **Conservar**; C58, C59 (−31) |
| 473–489 | La silla contada al grupo; Walt: "atado a dos hombres" | 213 | "Prefiero elegir a quién" (voz) | **Comprimir** C46 (−45, incluye A25), C60 |
| 491–507 | **Sedán** | 184 | Siembra sin resolver (Irene en el 32) | **Corregir** A24; resto intacto |
| 511–549 | **Pesca** | 363 | Descomprime; siembra 31 y la llamada del 32 | **Conservar** (Walt y la hielera son el grupo que el 31 cobra) |

## 4. Protegido y siembras

- **Canon de 29:** "Ven ahora. Sabes dónde."; Camp Alder / cargamento / "Una promesa es interesante. No es urgente."; "Veo que usted tiene filo para cerrar negocios de niños… de adultos" / "Una silla." / "En la que importa."; "Su gente opera bajo su nombre. Y su nombre queda bajo el mío." / "La que usted reconozca como suya."; el primer trago con la pelirroja; "Bellandi no." / "Estoy protegiendo un activo." / "Tu Chiara" → "Bellandi."; los cuarenta y tres minutos; "Me alegra que todos entendamos la misma habitación."; "Bienvenido, Mercer."; "—Estás loco." como último diálogo; el cierre vehicular sin palabra.
- **Inviolables del 30 (encargo), con su línea:** "Warren Halbrook" (59); Kal admite el antagonista equivocado (73); Nadir como palanca (63, 161–163); la explicación de la silla (145); "Bellandi no" (185–189); las fotografías vistas juntos (199–217); el nacimiento funcional Patio + *i Sussurri* (223, 353–355); "Con peores personas he tratado" (377); Nadir se entera por Kal (409–439); Danny pregunta por la salida (463–469); todavía no hay plan completo (469).
- **Protegidos además en 30:** "Te voy a contar todo" (53); "llevo toda la vida sin saber compartir eso con nadie" + el defecto de fábrica (81–83); "No puedo pedirte que estemos en esto juntos y guardarme la mitad de la baraja" (93, título); la tercera línea guardada y la distinción que no se cree (111); el camaleón sin la palabra (141); "sususus / Eso dije" (235–243); "Ya sabes cómo termina eso" / "una orden con otro nombre" (307–311); "A ella no. Alrededor." (317); "Mientras tanto nadie más decide con quién cenas" (351: es el puente a la línea titular, "para que tú puedas ver a quien tú quieras"; se conserva en toda versión del plan); "Alineados"; el pantalón y "¿Debo preocuparme?"; "Ninguno de los dos miró el espejo"; "Siempre termino debiéndole a alguien. Prefiero elegir a quién."; el perro dos calles más allá; la hielera de Walt.
- **Siembras que cobra la Parte III (por búsqueda):** la silla (33:89), la puerta a Camp Alder y la distracción de Dario (39:163–187; Hitos H19), Kenji/Oda (33), la pesca (31, 32). **No hay en 35–44 ningún pago de "necesarios", "uno por uno", "pedazos", "sólo suyo", "desmontar" ni "alineados"**: el plan de caída no tiene cobro en el Libro I.
- **Ritual del *Ciao* en 29–30:** sin "Ciao" ni apodos; "Tu Chiara" es de Varek. Conforme a la metadata (pre-H16).

## 5. Lo que no es de microedición (se reporta y no se opera)

1. **Autos (cierra D4 de E1).** Kal tiene dos autos: el Peugeot 106 XSi (Parte I, ficha, 28, 43) y el Audi A7 (Cap. 9; 31; 34 lo nombra "segundo auto"). La discontinuidad es sólo 28 → 29 (minutos). Corrección mínima en A15 (dos palabras en prosa). Chiara: **Lancia** (comprado en el 25; prosa de 26, 29, 30 y 34); el **Mercedes** es el coche corporativo del Monarch (ficha l. 328, y lo usa en el 38). La metadata del 28 (l. 27) está mal y la ficha de Chiara no registra el Lancia: housekeeping (E5 para la metadata; E8/E9 para la ficha).
2. **P4 (Nadir hace algo duro por el grupo y le cuesta).** El final del 30 **no** lo cubre: Nadir recibe la noticia, reclama, recupera agencia con preguntas y rompe la tensión con la pesca. Es reacción y agencia, no un acto que le cueste. No recomiendo añadirlo al 30 (va contra la poda y el capítulo ya carga el grupo entero). Candidato natural: la salida de la mercancía en el 32 si **Nadir** la elige y le cuesta (rutas, dinero, orgullo); se evalúa en E3 junto con Irene. Si no, queda para la Parte III.
3. **P2 (Beretta .25).** El 30 tiene un punto viable después del pacto del 29: **30:209**, "Fue por el sobre y volvió" — el sobre está en el bolso que se quedó en el Lancia mientras ella entraba a casa de Varek, y la imagen sería una sola: el sobre sale del bolso de al lado de la Beretta .25 (≈ +10 palabras, sin glosa, sin que Kal la vea). Riesgo: la pistola aparece junto a las fotos de los Bravos, justo después de la casa de Varek; se lee como contexto armado, más cerca del presagio. **Recomendación provisional: el 31** (vestidor: un cambio de bolso es doméstico y no amenaza nada, que es lo que el 44 necesita para que "llevaba ahí desde hacía años" sea verdad). El 30:209 queda como alternativa. E3 decide.
4. **La mecánica de las armas largas (A25)** está fijada en Hitos H19 y en la ficha de Halbrook; el 30 no debe añadir otra. Se reporta como corte, no como cambio de canon.
5. **Metadata del 30 con numeración vieja** (el "Cap. 30" que es el 29, el "Cap. 32" que es el 31, "cierre del Cap. 30"): ver § Metadata de 29–30.
6. **Dario_Varek.md l. 51** ("cuando Kal se ofrece a trabajar para él") y Hitos H6 §5–6 siguen con la mecánica antigua. Housekeeping ya listado (E8).

---

## Autocrítica E2 (MICROEDICION §F)

- **Lo más dudoso:** C49 (fotografías). La enumeración es glosa, pero es también el único sitio donde el texto formula la división del trabajo que el 30 funda; si el autor la siente como tesis, se conserva entera.
- **Lo más agresivo:** el plan (V2) y C46: quitan un pasaje que el autor escribió como cierre del pacto y la tercera narración del trato. Los dos se apoyan en búsquedas (sin pagos en 35–44; la caída es del Libro III).
- **Pareció corte y quedó protegido:** 30:251 (las redundancias de Chiara), porque es la única entrada al motivo "Kal se volvió su único plan" y P3 del 31 la puede necesitar; 29:245 (la cara del loft), porque es memoria de Kal, no recap.
- **Riesgo de esterilizar:** moderado en el 30. Se quita mucha glosa de narrador en la voz de Chiara; queda la de ella donde es interioridad (99, 109, 111, 141, 251). Se conservan los símiles de oficio en uno (83), no en cero.
- **Racionalizar interioridad:** B11 y B13 cortan dos pensamientos de Kal; están en sección de Chiara, así que no son interioridad del POV. Ninguna propuesta convierte percepción en explicación.
- **Prosa más genérica:** las tres líneas nuevas posibles (D18, D21a, V1/V3) son mínimas; la recomendada para el plan (V2) no escribe nada.

---

# § Plan contra Varek

**Líneas exactas (30:337–365):**

> —Entonces qué hacemos —dijo Chiara.
> —Lo que hicimos ahí adentro. —Kal miró hacia la dirección de donde habían venido…—. Entrar. Volvernos necesarios. Aprender cómo funciona por dentro, hasta que sepamos más de su estructura que él mismo.
> —Y después.
> —Después dejamos de necesitarlo. —Se encogió de hombros, **como si estuviera describiendo cómo se arregla un motor y no cómo se desmonta un imperio**—. **Un hombre que decide todo tiene que decidir todo él solo. Si le quitamos, uno por uno, los pedazos que sólo él sabe mover, un día se despierta y no queda nada que sea sólo suyo.**
> —Eso puede tardar años. / —Puede.
> —¿Y mientras tanto? / —Mientras tanto nadie más decide con quién cenas.
> —Y mientras aprendemos cómo funciona por dentro —agregó Chiara—, *i Sussurri* puede decirnos con quién habla, a quién le debe favores, dónde le tiembla el negocio… / —Y El Patio puede moverte lo que *i Sussurri* no puede… Nunca hicimos esto juntos. / —No como esto.
> **Chiara lo miró. No había en su cara ni en su voz nada que sonara a discurso, nada que sonara a plan escrito en una servilleta… Y por eso, precisamente por eso, le creyó entero.**
> —De acuerdo —dijo—. Alineados. / —Alineados.
> No se dieron la mano. **No hacía falta un gesto para sellarlo; los dos sabían, sin decirlo, que la palabra ya pesaba lo suficiente.**

Metadata 30:24 lo formula todavía con más certeza: "desmontar a Varek desde dentro… absorber funciones, quitarle a Varek la capacidad de decidir sus vidas".

**Qué pagan:**
- **En 35–44:** nada de la caída. Sí se cobran la silla (33:89) y la puerta (39: Dario da la ventana de Camp Alder; Hitos H19, "la entrada de H6 y el asalto son la misma operación"). "Volvernos necesarios" es exactamente lo que el 39 muestra.
- **Libro II (`03_Libro_02_Sombras_De_Poder.md`):** Kal como "activo de campo" de Dario (escolta de cocaína, canon 2026-09-26); "El pacto de H6 y sus consecuencias siguen activos; **la caída de Dario pertenece a *Voto de Ceniza*** (Libro III)". El arco de Kal en el II es "operador → jefe informal → centro de gravedad", no desmontar a Varek.
- **Dario_Varek.md:** la caída es el arresto del empresario, dentro de la Guerra de los Tres (Libro III).
- **Conclusión:** "Entrar / volvernos necesarios / aprender cómo funciona por dentro" y "dejar de necesitarlo" son la **dirección** que el Libro II cumple. "Uno por uno, los pedazos… no queda nada que sea sólo suyo" y "cómo se desmonta un imperio" son el **mecanismo de la caída** de un libro que todavía no empieza, dicho con certeza por dos personajes que llevan una mañana aliados. Eso es lo que baja.

**Tres versiones de "pacto, no plan":**

**V1 — Dirección con una línea nueva de duda (reformula).** Se conserva 339; 341–347 pasan a:
> —Y después.
> —Después, que nos necesite más de lo que nosotros lo necesitamos a él.
> —Eso puede tardar años.
> —Puede.

Se cortan el símil del imperio y el "uno por uno"; 359 queda en "Chiara lo miró."; 365 en "No se dieron la mano." Autonomía como meta, sin caída. Coste ≈ −95. Riesgo: línea nueva del agente en boca de Kal, justo antes de la línea titular.

**V2 — Sólo cortar (recomendada).** Sin prosa nueva:
> —Y después.
> —Después dejamos de necesitarlo.
> —Eso puede tardar años.
> —Puede.
> —¿Y mientras tanto?
> —Mientras tanto nadie más decide con quién cenas.

Se va la oración del encogimiento de hombros con el imperio y las dos oraciones del "uno por uno". "Dejamos de necesitarlo" conserva las cuatro direcciones que pide el encargo (entender dónde están, hacerse necesarios, ganar autonomía, dejar de depender) y ninguna certeza de caída; "Eso puede tardar años / Puede" ya es la duda. 353–355 (El Patio + *i Sussurri*) intacto. 359 se corta (C54: "Chiara lo miró." puede quedarse como puente o cortarse y pasar directo a "—De acuerdo —dijo—."); 365 → "No se dieron la mano." (B12). Coste ≈ −100 contando C54 y B12. **Por qué ésta:** es la menor intrusión (EDITORIAL_POLICY §H), no pone palabras del agente en un pasaje que desemboca en la línea canon, y el cierre queda como pacto: "Alineados", no un programa.

**V3 — Duda en boca de Chiara (reformula, más pacto).** V2 más un cambio en quien pone el límite:
> —Después dejamos de necesitarlo.
> —Si nos deja.
> —Puede.

("Eso puede tardar años" se sustituye.) Baja la certeza al máximo y da a Chiara la última palabra del cálculo, en su registro. Riesgo: línea nueva del agente y cambia el ritmo del "¿Y mientras tanto?". Coste ≈ −105.

**Recomendación:** **V2.** Es la única que no escribe; si al autor le parece que "Dejamos de necesitarlo" sigue sonando a programa, V3 es la alternativa. Metadata 30:24 se reescribe en E6 con la versión elegida ("pacto: entrar, hacerse necesarios, dejar de depender; sin plan de caída, que es del Libro III").

---

# § Metadata de 29–30 (se anota, no se toca; se sanea en E6)

| Cap:línea | Dice | Problema | Debe decir |
|---|---|---|---|
| 29:6 | "Ejecuta H6, secciones 5-6" | Hitos H6 §5 documenta la mecánica vieja ("Kal ofrece trabajar para Varek") | Se deja; la corrección es de Hitos (E8) |
| 29:19 | "…sin mencionarlas ni usarlas aquí — vuelven en el **Cap. 31**" | Las fotografías vuelven en el 30 | "Cap. 30" |
| 29:21 | "…espera minutos reales antes de subir al **Audi**" | D15 | "al Peugeot" |
| 29:26 | VEHÍCULOS: "Chiara conduce el Lancia (el mismo del **Cap. 27**). Kal conduce un Audi. **Discontinuidad conocida y aceptada**…" | El Lancia es del 26 (comprado en el 25); la discontinuidad se resuelve con D15 | "Chiara conduce el Lancia (comprado en el Cap. 25; Cap. 26). Kal, el Peugeot, continuidad directa con el 28; el Audi vuelve en el 31." |
| 29:28 | Lista de documentos desactualizados | Siguen desactualizados (Dario_Varek l. 51, Hitos H6 §5) | E8 |
| 30:9 | "consecuencias de la REESCRITURA PROFUNDA del **Cap. 30**" | Numeración vieja: es la del 29 | "Cap. 29" |
| 30:11 | "…no por recapitulación del **Cap. 30**" | Igual | "Cap. 29" |
| 30:17 y 30:23 | "CAMBIO DE REGLA" y "NUEVA REGLA": el mismo texto dos veces | Duplicado | Dejar uno |
| 30:24 | EL PACTO: "desmontar a Varek desde dentro… absorber funciones, quitarle a Varek la capacidad de decidir sus vidas" | Certeza que el dictamen baja | Según D16 |
| 30:31 | "Chiara llega en su Lancia, Kal en su **Audi** (continuidad directa con el cierre del **Cap. 30**)" | D15; numeración | "Kal en su Peugeot (continuidad con el 28 y el cierre del 29)" |
| 30:34 | "…el saneamiento de H7 en el **Cap. 32**" | Hoy es el 31 | "Cap. 31" |
| 30:38 | "RESUELTO… el **Cap. 32** fue saneado… 'Peugeot' (pasa a Audi/Lancia)… Cap. 32 no cambia de posición" | Numeración vieja (hoy 31); y el 32 actual es otro capítulo | "Cap. 31" en las cuatro menciones |
| 30:27 | Coda: "NADIR SE ENTERA AQUÍ POR PRIMERA VEZ…", "Kal NO llama a Chiara todavía… línea canon de apertura del **Cap. 32** ('Ponte algo cómodo…')" | Esa línea abre el 31 (31:39, confirmado por búsqueda; la prosa dice "Ponte algo cómodo para ir a pescar", no la cita de la metadata: E3 lo revisa) | "Cap. 31" |
| 30:15 | "PAYOFF DEL SEDÁN… Chiara pregunta por el sedán del Cap. 28" | Correcto; añadir que en la coda Kal ya lo conocía por Walt (A24) | E6 |

---

# § 9 Resultado (parte 2) — SURGERY de 29 y 30 (E6, 2026-09-27)

**Comprobación previa:** `git diff --stat` sin cambios en 29 y 30 (coinciden con el estado auditado en E2; último commit `1af8c6a`). **Autoridad:** § Respuestas del autor, Q1 (V2) y Q4 (veto libre). **Estado:** los dos siguen **BORRADOR**; nota de cirugía añadida en su línea de Estado. **Método:** script de reemplazos exactos (cada fragmento debía aparecer una sola vez; si no, abortaba), todo dentro de una línea o una línea entera con su blanco.

**Palabras de prosa** (`wc -w` desde el encabezado): 29 = 2,979 → **2,760** (−219) · 30 = 4,783 → **4,162** (−621). **Total −840** (E2 estimaba ≈ −225 y ≈ −610). **Finales de línea:** los dos, CRLF en todas las líneas antes y después (293/293 y 549 → 542/542; el E2 los había anotado "mixtos": el conteo de hoy da CRLF uniforme, sin cambio por la cirugía).

## Cap. 29

| # | Before | After | Categoría | Qué ya hacía la escena / qué conserva |
|---|---|---|---|---|
| A15 | "caminó hacia el Audi" | "caminó hacia el Peugeot" | CONTINUIDAD (D15) | Minutos antes sale del loft en el Peugeot (28). Conserva el cierre vehicular intacto |
| C21 | "…la cuenta de dónde estaba, sin que nadie tuviera que decírselo dos veces." | "…la cuenta de dónde estaba." | REPETICIÓN LEXICAL | "que se identificara dos veces" ya está en la frase. Conserva "Eso también era información." |
| A18 | "—dijo Varek, sentándose por fin—." | "—dijo Varek—." | CONTINUIDAD | Ya se había sentado en 57 |
| C23 | "no cambió la expresión ni un grado" / "se movió un grado, como cuando" | "no cambió la expresión" / "se movió, como cuando" | TIC | Queda el "un grado" de la nube (85), que es la imagen |
| C24 | "…en hablar primero — el primero de la mañana en que dudó antes de decir algo." | "…en hablar." | GLOSA | "medio segundo de más" ya dice la duda |
| A16 | "la curiosidad genuina que había prometido por teléfono." | "la curiosidad genuina." | CONTINUIDAD | La llamada (*Ven ahora. Sabes dónde.*) no promete nada |
| C27 | "Fue todo lo que dijeron sobre el tema, y fue suficiente. Varek no se levantó…" | "Varek no se levantó…" | GLOSA | La puerta entornada cierra el movimiento |
| C28 | "…que ya sabía que iba a cuadrar. No miró a Kal para explicarle nada… antes de sentarse." (−68) | "…que ya sabía que iba a cuadrar." | GLOSA (compactar Vivian) | La cifra, la contraoferta y el "Ni una disculpa" lo muestran. Conserva el asentimiento de balance |
| C29 | "No preguntó quién. No preguntó de qué universidad… un aula. Preguntar…" | "No preguntó quién. Preguntar…" | REPETICIÓN FUNCIONAL | El 30:291 dice los dos mundos en boca de Kal. Conserva "dibujar un círculo" y el primer trago (canon) |
| C30a | "Kal no supo, y no lo iba a preguntar, si sabía su nombre por negocios, por el Monarch… se sabían." | "Kal no supo de dónde sabía su nombre." | SEMILLAS DE MÁS (D22a) | Conserva el hecho: la casa sabe su nombre |
| C33a + B15 | "Fue perfecto, y fue rápido… No llegó. Ninguno de los dos improvisó peor que eso… —que los dos sintieron, y los dos apagaron…— de mirarse…" | "Varek los miró… No llegó. Kal sintió la tentación de mirarla el tiempo suficiente como para que significara algo, y la apagó." | COMPETENCIA EXPLICADA + SALTO DE POV (D21a) | La actuación ya se vio. Conserva la tentación, contada desde el único POV que puede contarla |

**Conservado a propósito (29):** "Te trataron mal" (D20, tú de dueño al herido); "nueve palabras de él" (A17); "el gris del Lancia" (A20); C22 (temprano para beber), C25 (el cuarto "dos veces", 95: queda como único eco con el de 43 fuera), C26, C31 (la cara del loft), C32; el motivo del clima (271); "guardaba" de 189 (uno de los tres que se quedan).

## Cap. 30 — por movimiento

| Mov. | # | Before | After | Categoría | Qué ya hacía / qué conserva |
|---|---|---|---|---|---|
| Llegada | A15 | "detuvo el Audi junto a un roble solo" | "detuvo el Peugeot…" | CONTINUIDAD | — |
| Halbrook | B8 | "—Se lo dijo directo, sin adornarlo, sabiendo exactamente el peso que le estaba quitando de encima…—" | "—Se lo dijo directo—." | SALTO DE POV + TIC | "No Varek." hace el peso. **Inviolables intactos:** "Warren Halbrook", antagonista equivocado (73), Nadir como palanca |
| Halbrook | C37 | "—No lo sé con certeza. —Fue honesto, y eso pesaba más que una respuesta segura—. Pero ahora sé…" | "—No lo sé con certeza. Pero ahora sé…" | GLOSA | La frase es honesta sola |
| Halbrook | A22 | "había pasado dos días mirando" | "había pasado el día entero mirando" | CRONOLOGÍA | — |
| Mentira | A22 | "¿Por qué no me lo dijiste anoche?" | "…en el loft?" | CRONOLOGÍA | — |
| Mentira | C39 | Párrafo "Chiara hizo la cuenta… sin un solo momento libre para volver a su propia gente." (−40) | (cortado) | RECAPITULACIÓN | "No he visto a nadie desde que Halbrook me sacó de la ciudad" lo dice. Conserva el título ("la mitad de la baraja") y el defecto de fábrica |
| Mentira | C40 | "…escuchando el agua, dejando que la frase terminara de asentarse antes de decidir qué hacer con ella." | "…escuchando el agua." | TIC | Queda el "asentarse" del 29:273 |
| Reclamo | A22 | "en una roca, y no anoche." / "la noche anterior con Kal" | "en una roca, y no en casa." / "esa madrugada con Kal" | CRONOLOGÍA | Protegidos 99, 109 y la tercera línea guardada (111) |
| Silla | C44 | "Se lo dijo sin adorno, casi con el mismo tono con el que un mecánico… reconstruyendo la frase por dentro…" (−40) | "Chiara lo miró un momento." | GLOSA + TIC + símil de oficio | "No le pediste la silla" es la reconstrucción. **Inviolable** (explicación de la silla, 145) intacto |
| Silla | C45 | "…podría usarse contra ella. Lo guardó donde guardaba todo lo que todavía no sabía qué hacer con ello." | "…podría usarse contra ella." | TIC | Conserva el camaleón sin la palabra |
| Silla | C40 | "Chiara dejó que eso terminara de asentarse. No era una solución…" | "No era una solución…" | TIC | — |
| Activo | C47 | "…sin contradecirse. No era lo mismo que el día anterior, en el loft… sin quitárselo después." (−45) | "…sin contradecirse." | GLOSA de cambio + CRONOLOGÍA | La escena de Marisol cobra la columna ("Ya sabes cómo termina eso"). **"Bellandi no"** intacto |
| Fotos | C48 | "Preguntó permiso, y eso, viniendo de él, era su manera de decir que algo había cambiado." | "Preguntó permiso." | GLOSA de cambio | El "No dijo *quiero verlas*…" ya lo muestra |
| Fotos | C49a | "Se quedaron así un momento, cada uno mirando… Kal veía calles…; Chiara veía nombres… Ninguno…" | "Se quedaron así un momento. Ninguno de los dos había visto la fotografía completa hasta que la vieron juntos." | GLOSA (D26a) | El diálogo de las dos fotos lo mostró. Conserva la tesis de la alianza. **Inviolable** intacto |
| *Sussurri* | B9 | "Chiara no contestó eso, y el silencio duró lo suficiente como para que ambos entendieran…" | "Chiara no contestó eso." | SALTO DE POV + GLOSA | 251 (redundancias) hace el trabajo desde ella; protegido |
| *Sussurri* | A22 | "por primera vez en dos días" | "por primera vez desde que leyó el mensaje" | CRONOLOGÍA | "sususus / Eso dije" intacto |
| Vivian | C51 | "—En el patio de Varek había una mujer. Su hija. Entró como quien entra a su propia casa, cerró un trato de puerto… Varek la trató como algo normal." | "—En el patio de Varek estaba su hija." | REPETICIÓN FUNCIONAL | 267 ("cerró un trato delante de su padre… sólo por el precio") da el dato una vez. Costura leída: Chiara duda ("No sabía que participaba de verdad") y Kal confirma; se sostiene |
| Vivian | C45 | Párrafo "Chiara guardó eso donde guardaba lo que todavía no podía usar." | (cortado) | TIC | "¿Eso es todo?" pasa directo; la alternancia de voces se lee sin acotación |
| Marisol | B10 | "—dijo, al fin, sabiendo cómo sonaba en cuanto lo dijo en voz alta." | "—dijo, al fin." | SALTO DE POV | "¿Y cuando te pregunte por qué?" lo hace sonar |
| Marisol | B11 | "…la mandíbula tensa un momento, midiendo la distancia entre lo que quería hacer y lo que acababa de aprender…" (−25) | "…la mandíbula tensa un momento." | SALTO DE POV + GLOSA de cambio | "una orden con otro nombre" dice el aprendizaje en su boca. Columna protegida intacta |
| Pacto | **V2** | "—Después dejamos de necesitarlo. —Se encogió de hombros, como si estuviera describiendo cómo se arregla un motor y no cómo se desmonta un imperio—. Un hombre que decide todo… uno por uno, los pedazos… no queda nada que sea sólo suyo." | "—Después dejamos de necesitarlo." | CERTEZA DE PLAN (decisión Q1) | Se va el mecanismo de la caída (Libro III) y el símil del imperio (B18). Conserva la dirección: entrar, volvernos necesarios, aprender por dentro, dejar de necesitarlo; "Eso puede tardar años / Puede" es la duda. "Mientras tanto nadie más decide con quién cenas" y El Patio + *i Sussurri* intactos |
| Pacto | C54 | "Chiara lo miró. No había en su cara ni en su voz nada que sonara a discurso… le creyó entero." (−45) | "Chiara lo miró." | GLOSA + símil de oficio | Se deja "Chiara lo miró." como puente: atribuye el "—De acuerdo —dijo—" a ella sin ambigüedad |
| Pacto | B12 | "No se dieron la mano. No hacía falta un gesto para sellarlo; los dos sabían…" | "No se dieron la mano." | SALTO DE POV + GLOSA | "Alineados" ×2 sella |
| Titular | B13 | "Kal se quedó callado un momento, buscando cómo decir lo que seguía…" | "Kal se quedó callado un momento." | SALTO DE POV | Pausa antes de la línea canon conservada. **"Con peores personas he tratado"** intacto |
| Titular | B14 | "Chiara no dijo nada. No hacía falta decir nada, y los dos se quedaron… sin que ninguno de los dos sintiera la necesidad…" | "Chiara no dijo nada. Se quedaron un momento así, con el agua cubriendo el silencio." | GLOSA + SALTO DE POV | Conserva el agua y el silencio |
| Nadir | C55 | "—Kal lo miró directo, algo que no había logrado hacer con Chiara hasta que no le quedó otra opción—." | "—Kal lo miró directo—." | GLOSA (señala la rima que la metadata pide "no señalada") | **Nadir se entera por Kal**, intacto |
| Nadir | C57 | "—preguntó, y con eso la conversación cambió de forma: dejó de ser sobre lo que Kal había hecho mal…" | "—preguntó." | GLOSA | La pregunta es la agencia de Nadir |
| Camp Alder | C58 | Párrafo "Eso se quedó flotando el tiempo suficiente para que todos entendieran el tamaño real…" | (cortado) | GLOSA | "instalación federal" cierra; Danny entra con la pregunta. **Danny / "Todavía no tengo salida" / "No tengo un plan completo"** intactos |
| Camp Alder | C59 | "—Todavía no tengo salida. —Kal lo dijo sin adornarlo, porque adornarlo hubiera sido peor—. Tengo…" | "—Todavía no tengo salida. Tengo…" | TIC | Quedan 185, 409 y 459 de la familia |
| Silla al grupo | C46 + A25 | "…esta mañana. Le ofrecí el cargamento, el mismo armamento largo que Halbrook mueve para pagar favores. No le bastó. Terminó…" / "—No lo adornó—. … No toca el papel, no toca a Halbrook, no toca Camp Alder. … Si alguien intenta algo aquí, primero tiene que pasar por Varek." | "…esta mañana. Terminó ofreciéndome algo más grande: una silla en su mesa." / "…queda bajo su nombre. Eso no resuelve lo de Nadir. Compra presión local, nada más. Y Varek no sabe…" | REPETICIÓN FUNCIONAL (tercera narración del trato) + mecánica contraria a H19 | El grupo recibe lo que necesita; Walt ("atado a dos hombres") y "Prefiero elegir a quién" intactos. Se conserva la acotación "Kal miró a Walt, después a Héctor" |
| Silla al grupo | C60 | "Walt asintió despacio, el tipo de asentimiento que en él equivalía a haber entendido el mapa completo…" | "Walt asintió despacio." | COMPETENCIA EXPLICADA | La línea siguiente de Walt la demuestra |
| Sedán | A24 | "—¿Qué sedán?" / "—El que Walt vio dos veces cerca de aquí. … No dijimos nada porque…" | "—¿Lo volvieron a ver?" / "—Walt no fue el único. … No lo dijimos porque…" | CONTINUIDAD (D18) | Kal lo sabía por Walt (27). "No dos tardes después" (505) sigue cobrando el aviso tardío. Sedán sin resolver (paga el 32, Irene) |

**Conservado a propósito (30):** B16 ("como si le hubiera leído el pensamiento"); el defecto de fábrica (único símil de oficio que queda); 99, 109, 111 y 251 (interioridad de Chiara; 251 lo necesita P3 del 31); "A ella no. Alrededor."; Kenji/Oda completo; C52; C56 (el "No dijo *era para protegerte*…", rima de conducta con 29:273); C61–C63; C64 ("viniendo de él, era casi una declaración", ahora el único "viniendo de él"); "por lo de anoche" de Walt y Kal y "Podías anoche" de Nadir (A23, en habla); la pesca entera.

**Pagos comprobados al operar:** ningún corte toca un pago de 35–44 (la silla del 33:89 y la puerta del 39 siguen sembradas en 145 y en la coda; "necesarios" se queda en 339). No hubo que restaurar nada.

**Beretta:** no cae en el 30 (Q2: el 31, en E7). **P4:** no se añade nada (veto libre D25).

## Metadata saneada (29 y 30)

- **29:** Estado con nota de cirugía; fotografías "vuelven en el Cap. 30"; "subir al Peugeot"; VEHÍCULOS reescrito (Lancia del 25/26; Peugeot en continuidad con el 28; Audi desde el 31). 29:6 (H6 §5) y 29:28 (documentos desactualizados) quedan para E8.
- **30:** Estado con nota de cirugía; numeración vieja corregida (Cap. 30 → 29 en 9, 11, 25, 32 y 36; Cap. 32 → 31 en 27, 34 y 38); "CAMBIO DE REGLA" (17) eliminado por duplicar "NUEVA REGLA" (23); EL PACTO (24) reescrito como pacto sin plan de caída (Libro III); VEHÍCULOS con el Peugeot; nota del sedán en 15. **No se tocó** 30:22 ("El Cap. 32 no cambia de posición"): su numeración es ambigua (el mismo párrafo llama "Cap. 33" al de Marisol/Kenji, que es la numeración actual); se reporta para E8.

## Autocrítica E6 (MICROEDICION §F)

- **Lo más dudoso:** C51 junto con el corte del "guardó" de 269: Vivian queda en dos líneas de Kal y la duda de Chiara ("No sabía que participaba de verdad") llega antes de que Kal diga que participa. Se lee como Chiara adelantándose, que es su registro, pero si el autor lo siente brusco, restaurar "Entró como quien entra a su propia casa" basta.
- **Lo más agresivo:** V2 (decisión del autor) y C46: quitan el mecanismo de la caída y la tercera narración del trato. El 30 pierde 621 palabras sin perder un solo beat del dictamen.
- **Pareció corte y quedó protegido:** "Chiara lo miró." antes del "De acuerdo" (C54 permitía cortarlo): hace falta para atribuir la línea. La acotación "Kal miró a Walt, después a Héctor" en C46 (la propuesta la omitía): es gesto, no glosa.
- **Riesgo de esterilizar:** moderado en la sección de Chiara, que pierde casi toda la glosa del narrador; queda su interioridad donde es suya (99, 109, 111, 141, 251) y un símil de oficio. El 29 conserva todas sus lecturas de Kal.
- **Racionalizar interioridad:** no; los cortes de pensamiento (B8–B14) eran de Kal dentro del POV de Chiara. C33a convierte una certeza doble en una tentación de Kal, más percepción, no menos.
- **Prosa más genérica:** las dos únicas líneas nuevas son D18 ("¿Lo volvieron a ver?" / "Walt no fue el único.") y C33a; las dos son más cortas que lo que sustituyen y están en el registro de cada personaje.

---

# Parte 3 — Caps. 31 y 32 (E3)

## 0. Diagnóstico corto

- **31 (MEDIA).** Cumple todo lo que promete: vestidor, sándwiches, Harper, Chiara aprendiendo a pescar, el grupo, el segundo beso, "Vamos a casa", el sillón. Los problemas son de **punto de vista**: es un capítulo de POV único de Chiara y entra cuatro veces en Kal o en Harper (57, 153, 175, 261). También hay **glosas copiadas de su propia metadata** ("como quien reporta un dato", "porque ya no hacía falta", el asentimiento de Walt traducido), una **mirada de "los demás" antes de que los demás aparezcan** (177) y un **choque de medidas** en el sillón (medio metro / nueve pulgadas). El resumen del coche es más corto de lo que decía el dictamen (129 palabras). Se puede reducir, pero conviene conservar una línea. La tienda de pesca y el juego acuático se conservan casi enteros. La competencia se comprime poco.
- **32 (LIGERA).** El procedimiento está bien armado y es sobrio. Hay cinco hallazgos que no son de gusto: (1) un **bloque de DISEÑO fuera del comentario HTML** (línea 23), que `build_epub.py` no filtra y que **hoy se imprime en el EPUB** con diálogo de la Parte III (residuo de metadata, prioridad 2); (2) una **prolepsis de narrador** en la última línea ("no volvió a pensar en la tarjeta hasta mucho después", §L); (3) un **salto de POV** a Chiara en la coda (225); (4) **cronología interna**: el aviso del Tasador ("la semana siguiente") queda después de la segunda visita de Lucía ("diez días después"), aunque el texto lo cuenta antes; (5) el coche de Lucía es "un **sedán** gris, sin marcas" en un capítulo que va a recibir el sedán de Halbrook (P1). La metadata dice "unos días después del 31", pero la prosa arranca **a la mañana siguiente** (el sillón).

## 1. Candidatos por categoría (31 y 32)

### A. Continuidad y mecánica

| # | Cap:línea | Texto | Problema | Propuesta | Palabras |
|---|---|---|---|---|---|
| A26 | 31:177 | "sin la curiosidad abierta **con la que la habían mirado los demás**" | Harper es la primera del grupo que aparece (Nadir, Danny, Héctor y Walt llegan en 183–209). Nadie la ha mirado todavía | "Miró a Chiara un momento: una evaluación rápida, cerrada…" | −10 |
| A27 | 31:351 / 407 / 503 | "desplazado **casi medio metro**" / "por **nueve pulgadas** de sillón" / "**cuatro centímetros**" | Medio metro no son nueve pulgadas (≈ 23 cm), y el capítulo mezcla sistemas. El 32 cobra los "cuatro centímetros" | "por **medio metro** de sillón" (407) | 0 |
| A28 | 31:39 | "Ponte algo cómodo **para ir a pescar** … Porque quizá te vayas a mojar." | La metadata (31:7) da como canon "— Ponte algo cómodo, porque quizá te vayas a mojar." La prosa añade "para ir a pescar", que es lo que hace posible la reacción canon "¿A pescar? ¿Yo… a… pescar?" | **DUDOSA — CONSERVAR.** No tocar sin el autor (DO_NOT_TOUCH: diálogo canon). Si el autor quiere la línea literal, la pesca tendría que llegar por otra vía. Recomendación: conservar la prosa y corregir la cita de la metadata | 0 |
| A29 | 32:39 | "Era un **sedán** gris, sin marcas" | Es el coche de Lucía. Con el sedán de Halbrook vivo desde el 28 y 30 (y con P1 metiéndolo en este mismo capítulo), el lector lee una alarma que la escena no usa | "Era un **coche** gris, sin marcas" | 0 |
| A30 | 32:145 / 161 | "**La semana siguiente**, cerrando la caja, Héctor lo comentó" / "Lucía volvió al taller **diez días después** de la primera visita" | Día 0, visita; día 2, llamada; el jueves siguiente, el arresto; "un jueves más tarde" Héctor avisa que la llantera volvió a abrir (≈ día 10); Kal pasa "dos días después" (≈ día 12); el Tasador, "la semana siguiente" (≈ día 17+). Lucía vuelve el día 10, y el texto la pone después | "**Días después**, cerrando la caja…" y "Lucía volvió al taller **dos semanas** después de la primera visita". Así queda dentro de la ventana de 10 a 14 días de la metadata y dentro de las dos semanas de P1 | +1 |
| A31 | 32:203 | "colgando las llaves con más cuidado del necesario" | 31:357: en el loft, las llaves van "en el cuenco de la entrada". En el 32 los ganchos son los del taller (81, 179) | "dejando las llaves en el cuenco con más cuidado del necesario" | 0 |
| A32 | 32:27–33 | La prosa arranca la mañana siguiente al 31 (el sillón, "Ya era mañana") y Lucía llega esa misma mañana | La metadata (32:5) dice "arranca unos días después del Cap. 31" | Corregir la metadata (E7): "arranca a la mañana siguiente del 31". La prosa no cambia | 0 |
| A33 | 32:23 | `> **DISEÑO RESERVADO PARA PARTE III…**` (167 palabras, con diálogo de Lucía y Kal) | Está **después** del `-->`: `build_epub.py` sólo quita comentarios HTML, así que **se imprime en el EPUB** entre la metadata y el encabezado. Es el único capítulo del libro con texto entre `-->` y `# Capítulo` (verificado por búsqueda) | **E7:** meter el bloque dentro del comentario (o moverlo a `PENDING.md` / Hitos, como pide él mismo). No toca prosa. Hasta que se corrija, el EPUB vigente lo lleva | 0 (prosa) |
| A34 | 32:199 | "la tarjeta… en el bolsillo del pecho, **donde meses atrás había llevado una coartada**" | El 13 no pone la coartada en ningún bolsillo; la coartada fue el favor de Chiara | DUDOSA — CONSERVAR como figura (la coartada fue un papel que llevó encima en la comisaría). Se reporta | 0 |
| A35 | 31:343 | "la luz del porche que alguien —**Walt, probablemente**— había dejado encendida" | Walt pasó la tarde en el lago y salió con ellos | DUDOSA — CONSERVAR: es la conjetura de Chiara, y Walt pudo dejarla antes de salir | 0 |

### B. Prolepsis y saltos de POV

| # | Cap:línea | Texto | Problema | Propuesta | Palabras |
|---|---|---|---|---|---|
| B19 | 31:57 | "…con **una expresión que Kal no le había visto nunca**: la de una mujer que sabía sentarse a negociar con Dario Varek y no tenía la menor idea de qué se usaba para ir a pescar." | Salto a Kal: Chiara no puede ver su propia expresión ni saber qué le ha visto Kal | Pasar el contraste a la cabeza de Chiara: "…sin decidirse. Sabía sentarse a negociar con Dario Varek. No tenía la menor idea de qué se usaba para ir a pescar." | −9 |
| B20 | 31:153 | "Kal no dijo que sí. No dijo que no. **Por primera vez en mucho tiempo no sintió la urgencia de corregir la palabra, y tampoco estaba listo para quedarse con ella.**" | Salto a Kal, y además explica lo que el puente falso ya muestra | Cortar la segunda mitad: "Kal no dijo que sí. No dijo que no." | −25 |
| B21 | 31:175 | "…y el asunto, evidentemente, quedaba cerrado ahí — **no porque lo hubiera perdonado, sino porque ya había decidido no gastar más palabras en algo que no iba a cambiar**." | Salto a Harper; glosa de la metadata ("cierra el asunto callándose") | "Se bajó del capó sin prisa y caminó hacia las cañas." | −31 |
| B22 | 31:261 | "Algo le tiró del costado al hacerlo — las costillas todavía le cobraban esa clase de cosas — y **lo dejó pasar sin que se le notara en la cara**, como dejaba pasar todo lo demás." | Si no se le nota, Chiara no lo sabe. Pero ella está en sus brazos | Hacerlo observable: "Algo le tiró del costado al hacerlo; Chiara lo sintió en el brazo que la sostenía, y en la cara de él no se vio nada." (la metadata pide un reconocimiento mínimo del costado, y se conserva) | ±0 |
| B23 | 32:225 | "…se acercó a él sin prisa, **no para pedirle explicaciones, sino porque ya había decidido, sin anunciarlo, que aquello era un dato más que guardar, no un problema que resolver esa noche**." | Salto a Chiara en un capítulo de POV único de Kal; glosa | "…la dejó en el fregadero y se acercó a él sin prisa." Lo que la metadata pide ("lo archiva") ya lo hacen la copa y el silencio | −26 |
| B24 | 32:227 | "Kal la dejó acercarse, **y no volvió a pensar en la tarjeta hasta mucho después**." | **PROLEPSIS DE NARRADOR** (§L): anuncia que la tarjeta volverá (H20). Se corta, no se suaviza | "Kal la dejó acercarse." | −10 |
| — | 32:215 | "dándole vueltas a algo que no dijo **todavía**" | "todavía" promete que lo dirá. Es la redacción que el autor aprobó el 2026-09-20 (metadata 32:13) | DUDOSA — CONSERVAR (línea tocada por el autor). Se reporta la sombra de prolepsis. Si el autor quiere, se quita "todavía" | 0 |

### C. Glosa, tic, repetición y certificación

**Cap. 31**

| # | Línea | Texto | Categoría | Propuesta | Palabras |
|---|---|---|---|---|---|
| C65 | 77 | "…entender que Kal Mercer, **que esa misma mañana había negociado con Dario Varek**, acababa de vestirla…" | REPETICIÓN FUNCIONAL: el contraste "Varek / algo doméstico" aparece tres veces (57, 77, 405) | Cortar la aposición en 77. Se conservan 57 (en la versión B19) y 405 (clímax cómico del sillón) | −9 |
| C66 | 83 | "Confiar en que un hombre eligiera bien su ropa era una cosa nueva. Confiar en éste, en particular, no lo era." | INTERIORIDAD | **Conservar** | 0 |
| C67 | 89–99 | El resumen del coche (129 palabras): Nadir se enojó y después bromeó; "Ninguno salió corriendo"; Walt, Danny, Héctor; la pesca, idea de Nadir | REPETICIÓN FUNCIONAL con la coda del 30 (409–489), que lo dramatiza | Ver § El resumen del coche: queda la pregunta de Chiara, Nadir comprimido, **Danny y Camp Alder** (la honestidad de Kal después de la media baraja) e "Idea de Nadir."; se cortan Walt, Héctor y la justificación de la pesca | −55 |
| C68 | 163 | "…ninguno de los dos dijo nada más sobre el tema, **porque ya no hacía falta**." | GLOSA. La metadata lo prohíbe expresamente ("No se verbaliza la tesis") | Cortar la cláusula | −4 |
| C69 | 181 | "**Lo dijo sin intención de incomodar a nadie, como quien reporta un dato,** y volvió a lo suyo…" | GLOSA copiada de la metadata; TIC "como quien" | "Volvió a lo suyo antes de que a Chiara le diera tiempo de contestar." | −12 |
| C70 | 211 | "**Chiara no necesitó que dijera nada más. Entendió exactamente lo que ese asentimiento significaba,** y siguió caminando hacia la orilla." | GLOSA (la metadata pide que Walt cobre "MUY ligero") | "Chiara siguió caminando hacia la orilla." | −14 |
| C71 | 215 | "La dejó llegar a él, **que era su manera de decir que ese día no tenía prisa por nada**." | GLOSA | "La dejó llegar a él." | −12 |
| C72 | 237 | "…y Héctor, desde la orilla, sin levantar la vista de su propia caña, **dijo que en cuarenta años de pescar en ese lago nunca había visto una discusión tan tonta ganar tanto tiempo**." | REPETICIÓN FUNCIONAL: el 239–241 le da a Héctor su línea directa ("Yo no juzgo nada") | Comprimir: "…se rió más fuerte de lo que llevaba riéndose en semanas." y pasar a 239. DUDOSA: el estilo indirecto es color de Héctor; si el autor lo quiere, se queda | −31 |
| C73 | 243 | "La discusión, entendió, era el punto. **Resolverla la hubiera matado.**" | INTERIORIDAD / GLOSA | DUDOSA — CONSERVAR la primera (lectura de Chiara, que es negociadora); la segunda es candidata a corte | −4 |
| C74 | 323 | "Ningún nombre nuevo para lo que eran, ninguna pregunta sobre qué venía después, ninguna cuenta pendiente del galpón ni de la mansión ni de nada que no fuera el sol cayendo despacio detrás de un lago que no le pertenecía a ninguno de los dos y que por una tarde les había servido igual a los dos." | GLOSA de narrador: enumera lo que la escena no hizo (la metadata pedía el beso "sin glosa") | (a) cortar el párrafo y cerrar la sección en "a algo parecido a estar en casa"; (b) conservar sólo "el sol cayendo despacio detrás de un lago que no le pertenecía a ninguno de los dos". Recomendación: **(a)**, porque la línea de "casa" es la que rima con 345 | −57 |
| C75 | 343 | "dijo, sin ningún peso especial en la voz, **como quien dice cualquier otra cosa después de un día largo**:" | GLOSA / TIC "como quien" | Conservar "sin ningún peso especial en la voz" (es la instrucción de lectura de "Vamos a casa") y cortar el resto | −9 |
| C76 | 45 | "—Sí. A pescar. —Sonó divertido, no burlón, como quien ya esperaba exactamente esa reacción." | TIC "como quien" | DUDOSA — CONSERVAR: es percepción de Chiara por teléfono | 0 |
| C77 | 101 | "No hizo más preguntas. La mañana seria ya había terminado." | VALOR NO INFORMATIVO | **Conservar** (cierra el resumen, y con C67 lo necesita más) | 0 |
| C78 | 179 | "No sonrió. No hacía falta que sonriera para que no sonara hostil" | FIRMA (Harper) | **Conservar** | 0 |

**Cap. 32**

| # | Línea | Texto | Categoría | Propuesta | Palabras |
|---|---|---|---|---|---|
| C79 | 53 | "Kal sabía, sin que nadie se lo dijera, que una subjefa no entregaba papeles de rutina. **Eso ya era información, y ella probablemente lo sabía tan bien como él.**" | INTERIORIDAD (cálculo de Kal) / GLOSA | DUDOSA — CONSERVAR: es el método de Kal leyendo a la institución, que es el tema del capítulo | 0 |
| C80 | 121 | "Eso era todo lo que Kal sabía. **Era, también, exactamente lo que hacía falta.**" | COMPETENCIA EXPLICADA (el resultado lo demuestra en 137) | Cortar la segunda frase | −7 |
| C81 | 129 | "pensando que si alguna vez tenía algo que de verdad importara, ese circuito de escritorios era exactamente el tipo de cosa que no podía permitirse." | REPETICIÓN FUNCIONAL con 181–185 | **Conservar**: 129 siembra y 185 cobra en diálogo | 0 |
| C82 | 135 | "Le llegó por partes, **como suelen llegar esas cosas**." | TIC (sentencia) | Cortar la cláusula | −5 |
| C83 | 143 | "No sintió gran cosa. Fue, sobre todo, la comprobación de que un problema se había resuelto sin que él tuviera que resolverlo con las manos, y que eso —**a diferencia de lo que había hecho toda su vida**— **no le había costado una sola llamada a Héctor**." | GLOSA; REPETICIÓN FUNCIONAL con 213 ("Se resolvió sin que Héctor tuviera que romperle nada a nadie") | "No sintió gran cosa. Un problema se había resuelto sin que él tuviera que resolverlo con las manos." (Héctor queda para la línea de Kal a Chiara, que es mejor) | −27 |
| C84 | 173 | "**Lo dijo sin orgullo, como quien lee un resultado, no como quien lo celebra**—. Eso no significa que confíe en usted." | GLOSA; TIC "como quien" (doble) | Cortar el inciso: "…un expediente que aguanta una revisión. Eso no significa que confíe en usted." | −14 |
| C85 | 29–31 | El sillón: los cuatro centímetros, "No hacía falta que supiera que él se le había adelantado." | Pago del 31 | **Conservar** (protegido por el encargo) | 0 |
| C86 | 147–157 | Crowe: "¿Y Portillo?" / "Nada." / "Al muchacho no le gustó la respuesta." | Siembra (Parte III / Libro II) | **Conservar** (protegido por el encargo) | 0 |

**Familia "como quien" en 31–32:** 31:45 (conservar), 31:181 (C69), 31:343 (C75), 32:49 ("como quien lee un lugar antes de hablar en él": conservar, primera y mejor) y 32:173 (C84). Quedan dos.

## 2. Prolepsis y POV — lectura por capítulo

- **31 (POV único de Chiara, según la metadata).** Sin prolepsis. Hay cuatro entradas fuera del POV: B19 (Kal), B20 (Kal), B21 (Harper) y B22 (Kal, resuelto como percepción de ella). El 177 ("del tipo que hace alguien acostumbrada a medir a la gente…") es inferencia de Chiara y se queda. El 429 ("Kal también se dio cuenta") es observable.
- **32 (POV único de Kal).** Una prolepsis (B24) y una entrada en Chiara (B23). "todavía" (215) queda como duda. Con la escena de Irene sigue siendo POV Kal: la escena nueva no debe entrar en Irene ni en Tomás.

## 3. Función por movimiento

**Cap. 31 (4,136)**

| Líneas | Movimiento | Palabras | Función | Veredicto |
|---|---|---|---|---|
| 33–51 | Monarch; la llamada; "¿A pescar? ¿Yo… a… pescar?" | 210 | Apertura canon; costura con el 30 ("el nombre de un general") | **Conservar** (A28 en duda) |
| 55–83 | **Vestidor** | 426 | Inviolable; Kal decide su ropa y ella lo deja: la columna 28–34 en clave doméstica | B19, C65. **Candidato P2** en 83 |
| 87–101 | **Resumen del coche** | 188 | Costura con el 30 | **Comprimir** (C67) |
| 105–113 | Tienda de pesca | 117 | Humor ("la mitad del negocio"): es voz, no inventario | **Conservar.** El dictamen la marca, pero ya es mínima |
| 117–163 | **Sándwiches**; llamada de Nadir; Harper plantada; "¿novia?"; el puente | 367 | Inviolables (sándwiches, Harper); la etiqueta que no se desmiente | B20, C68 |
| 167–211 | El lago; **Harper**; Nadir, Danny, Héctor; Walt | 587 | Inviolable (el grupo); Harper con voz propia | A26, B21, C69, C70 |
| 215–223 | **Chiara aprende a pescar** | 174 | Inviolable | C71 |
| 227–243 | Competencia | 309 | Descomprime; siembra el "nadie ganó" que el 309 cobra | **Comprimir poco** (C72, C73) |
| 247–257 | Fe en la parrilla | 116 | Siembra protegida (Parte III / Libro II) | **Intacto** |
| 261–299 | Juego acuático ("Si me sueltas, me muero") | 344 | Canon; rima física con H12, sin nombrarla; "Los dos estamos igual de mojados. Nadie perdió." rima con 309 | **Conservar** (sólo B22) |
| 303–323 | La roca; "Gracias por traerme / Gracias por venir"; **segundo beso** | 317 | Inviolable; siembra "casa"; lugar de P3 | C74. **P3** en 317 |
| 327–331 | Recogida y despedidas | 182 | Cierre del grupo; Harper devuelve el abrazo | **Conservar** |
| 335–345 | Camino de vuelta; **"Vamos a casa"** | 189 | Inviolable | C75 |
| 349–509 | **Sillón**: "No era una orden / Sonó como una", "señora Mercer", **los cuatro centímetros** | 590 | Inviolable; coda del arco H5–H7 | A27. **Intacto** en lo demás |

**Cap. 32 (1,992, sin el bloque de la línea 23)**

| Líneas | Movimiento | Palabras | Función | Veredicto |
|---|---|---|---|---|
| 27–33 | El sillón a la mañana siguiente | 123 | Pago del 31 | **Conservar** |
| 37–69 | Lucía en el taller; el convenio | 330 | Pretexto administrativo real | A29. **Conservar** |
| 73–109 | La oficina: "Se cayó. Eso no es lo mismo que decir que le creí."; el número del Departamento | 404 | Núcleo: policía que prueba si puede usar lo que Kal sabe | **Conservar** (C79 en duda) |
| 113–121 | Portillo y Eddie Sosa | 196 | Kal decide sin gastar a Héctor | C80 |
| 125–131 | La llamada por tres escritorios | 113 | Siembra del canal directo | **Conservar.** **Punto de inserción de Irene** al final (131) |
| 135–143 | El resultado llega por partes | 176 | Procedimiento visto de lado | C82, C83 |
| 145–157 | Crowe | 84 | Siembra protegida | A30. **Intacto** |
| 161–195 | Lucía vuelve; la tarjeta | 305 | El canal directo (H20) | A30, C84 |
| 199–227 | Coda con Chiara | 248 | "Una Varek con línea directa a ti." Ella lo archiva | A31, B23, B24. **Lugar opcional del hilo A** (P1) |

## 4. Protegido y siembras

- **Inviolables del 31 (encargo), con su línea:** vestidor (57–83); sándwiches (119–127); Harper (169–181, 331); Chiara aprendiendo a pescar (223); el grupo (183–243, 327–331); segundo beso (321); "Vamos a casa" (345); sillón (349–509); "No era una orden / Sonó como una" (435–437); los cuatro centímetros (503), que el 32:27–31 arregla.
- **Protegidos además en 31:** "¿A pescar? ¿Yo… a… pescar?" y "¿Eso es toda la invitación?"; "No de ella. Con ella"; "Confiar en éste, en particular, no lo era"; "la mitad del negocio"; el puente falso ("No hay ningún puente en esta carretera, Kal."); "Kal habla de ti más de lo que cree que habla de ti"; "una sardina con aspiraciones"; la garza; "Yo no juzgo nada. Yo como lo que agarren."; "Si me sueltas, me muero" → "Kal Mercer, no vayas a soltarme"; "Nadie perdió. / Yo lo disfruté más."; "Nadir va a seguir discutiéndolo un mes. / Dos."; "a algo parecido a estar en casa"; "¡Te domaron!", "señora Mercer" / "señor Mercer"; "Estoy demasiado cansado para volver a tener esa conversación."
- **Protegidos en 32:** los cuatro centímetros; "Se cayó. Eso no es lo mismo que decir que le creí."; "Yo remolco coches. No cobro cuentos."; "No le voy a creer nada que no pueda confirmar solo"; los tres escritorios; Portillo con el cigarro; Crowe ("Nada."); "Yo tampoco confío en usted. / Bien. Así funciona mejor."; la tarjeta "sin acercarla del todo hacia él"; "Una Varek con línea directa a ti." / "No sé si eso me deja más tranquila o menos." / "Yo tampoco lo sé."
- **Fe en la parrilla (31:249–255) y Crowe (32:147–155):** intactos, como pide el encargo.
- **Ritual del *Ciao* en 31–32:** ningún "Ciao" ni apodo; "señora/señor Mercer" es broma de Nadir y respuesta de Chiara, no apodo de pareja. Conforme a la metadata (pre-H16). E4 lo consolida para 26–34.
- **Pagos buscados:** no hay Irene, Ronda ni "mercancía" en la prosa de 33–44 (búsqueda): la escena del 32 no choca con nada de la Parte III. La Beretta sólo aparece en 44:219 ("que llevaba ahí desde hacía años", en el bolso).

## 5. Lo que no es de microedición (se reporta y no se opera)

1. **El bloque de DISEÑO de 32:23** se imprime en el EPUB (A33). No es prosa: se corrige en E7 al sanear la metadata. El EPUB **no** se regenera por esto (regla del vault); se anota para la próxima regeneración.
2. **P4 (Nadir hace algo duro por el grupo y le cuesta).** Con el diseño aprobado de P1, **el 32 no lo cubre**: Nadir sale de la mercancía **sin saber por qué** (hilo A), así que no puede elegirlo ni pagarlo como un acto por el grupo. Lo que sí le toca es un costo pasivo (pierde las rutas, que eran su forma de pagar el 17, y no le dan la razón). Si se le diera a elegir, se rompería el hilo A y Kal tendría que contarle lo de Halbrook y la Ronda. **Recomendación: P4 queda para la Parte III**; E4 lo comprueba contra 33–44. No se añade nada en el 31 ni en el 32.
3. **Resumen del 30 en el 31:** el dictamen lo pedía reducir; la reducción (C67) es corta porque el pasaje ya es corto. No hay más recapitulación del 30 en el 31 (búsqueda de "Halbrook", "Camp Alder", "Varek" y "sedán": sólo 33, 57, 77, 95, 99 y 405).

---

# § El resumen del coche (31:89–99) frente al 30

| Línea del 31 | Dice | ¿Lo dramatiza el 30? | Veredicto |
|---|---|---|---|
| 89 | "¿Cómo se lo tomó Nadir?" | — | **Queda**: es Chiara preocupándose por Nadir, que en el 30 fue palanca sin saberlo |
| 91 | "Al principio, nada bien. —Kal no lo dulcificó—. Se enojó. Tenía razón en enojarse. Después hizo las preguntas que había que hacer, y después empezó a bromear, que en él es la manera de decir que ya está bien." | Sí (30:409–443, 511–549) | **Comprimir:** "—Mal. Tenía razón en enojarse. —Kal no lo dulcificó—. Después empezó a bromear." La glosa de lo que significa bromear en Nadir se va; el 31 lo muestra en el lago |
| 93–95 | "¿Y los demás?" / "Ninguno salió corriendo. Walt ya está pensando… Danny me preguntó cómo pienso salir de Camp Alder, y no tuve una buena respuesta. Héctor preguntó por el sedán." | Sí, los tres (30:445–507) | **Queda sólo Danny**: "—Danny me preguntó cómo pienso salir de Camp Alder. No tuve una buena respuesta." Es lo único que Chiara no sabía y es Kal jugando con la baraja entera la misma tarde del pacto. Walt y Héctor se van. "¿Y los demás?" se va con ellos |
| 97–99 | "¿Y la pesca?" / "Idea de Nadir. En cuanto entendió que no había nada más que hacer esa tarde ni con Halbrook ni con Varek, decidió que lo único responsable era ir a pescar." | Sí (30:511–549) | **Comprimir:** "—Idea de Nadir." Si el autor quiere la broma, "decidió que lo único responsable era ir a pescar" se puede quedar sin la primera mitad |
| 101 | "Chiara sonrió… La mañana seria ya había terminado." | — | **Queda** |

Resultado: de 129 a ≈ 70 palabras (C67). **La frase "el mismo día que Halbrook sacó a Kal…" no está en la prosa**: sólo en la metadata (31:4), y se corrige en E7 (§ Cronología).

---

# § P2 — Beretta .25: el 30 o el 31

**Recomendación: el 31, en el vestidor (31:83).** Queda después del pacto con Dario (29) y del pacto del 30. Es un **cambio de bolso** (la imagen que pide el canon). El contexto es doméstico, no hay amenaza cerca y Kal está de espaldas o ya bajando. Así, el 44 ("la mano le fue al bolso… la Beretta .25 que llevaba ahí desde hacía años") cobra un objeto que el lector vio pasar de un bolso a otro sin que nadie lo comentara.

- **Punto exacto:** 31:83, después de "…a abrocharse las botas". Hoy la frase sigue con "y no dijo nada más sobre el asunto". La imagen entra antes de las dos frases de interioridad, que se quedan.
- **Forma (diseño, no prosa final):** Chiara vacía el bolso del Monarch en uno de lona (o en la bolsa que se lleva al lago): teléfono, llaves, la Beretta .25. Una enumeración de tres, sin detenerse en la tercera, sin que Kal la vea o sin que diga nada. ≈ +15 a +20 palabras.
- **Riesgos:** (1) que Kal la vea y no diga nada puede leerse como que ya lo sabe. Es mejor que salga del vestidor antes ("Kal bajó a esperarla…"), pero eso agrega una acción. La alternativa es que el cambio de bolso ocurra mientras él mira el desastre del vestidor (57–71), sin línea nueva de él. (2) Que la pistola llegue al lago: es coherente con "desde hacía años" (va a todas partes con ella) y no se vuelve a ver.
- **Alternativa: 30:209** ("Fue por el sobre y volvió": el sobre sale del bolso de al lado de la Beretta). Es viable, pero la pistola aparece junto a las fotos de los Bravos, a la salida de casa de Varek. Se lee como contexto armado y queda más cerca del presagio.

---

# § P3 — Casi-confesión del lago (hilo A)

**¿Existe ya?** No del todo. El 31 tiene el silencio ("después de un rato de silencio que no pedía llenarse", 307; "al rato", 317), pero ahí nadie **abre la boca y elige una verdad más chica**: "Gracias por traerme" llega sin que el lector vea la elección. El diseño (Evaluación de arco, 5-quater: 20, 25, 31, 36) pide que la elección se vea y que el narrador no la explique.

**Dónde cabe:** 31:315–317, entre "…él dejó que se quedara ahí." y "—Gracias por traerme —dijo Chiara, al rato."

**Forma recomendada (sólo un silencio, sin línea nueva de diálogo):** un gesto de Chiara (abre la boca y no dice eso) y después la línea que ya existe. En diseño: *Chiara tomó aire para decir algo y lo soltó.* / "—Gracias por traerme." (≈ +8 palabras; se quita "al rato", que el gesto reemplaza). El lector tiene con qué llenar el hueco (la sudadera del 28, el rezo por él, "Kal se volvió su único plan", 30:251) y nadie se lo dice. Es Chiara porque el POV es suyo; si fuera Kal, tendría que ser algo que ella viera en la cara de él, y el beso que viene después necesita que ella sea la que mira.

**Alternativa:** no añadir nada y dar por cubierto el tramo con el silencio de 307. Recomendación: la forma de arriba, porque cuesta ocho palabras y hace visible la elección.

---

# § Irene en el 32 (P1) — diseño, sin prosa

**Condiciones (encargo y 5-ter):** el sedán de Halbrook que vigila a Nadir aparece en las rutas de la Ronda y Tomás Vale lo ve. Irene teme, sin decirlo, que un hombre con papeles frágiles bajo presión federal cambie lo que sabe (y Nadir conoce sus rutas). Irene no sabe quién está detrás y dice que no le importa. Nadir sale de la mercancía, pero la deuda no se perdona, cambia de forma. Kal no le cuenta lo de Halbrook y acepta el favor abierto que se negó a deber en el 17. Irene no amenaza a Nadir ni abre un frente que el Libro I tenga que cerrar. 800–1,000 palabras, dentro de las dos semanas del 32.

**1. Punto de inserción: después de 32:131**, con la frase ancla "Lo archivó, junto con el resto, y volvió al taller." Sección propia con `***` antes y después. La siguiente sección arranca con "Le llegó por partes…" (C82 la deja en "Le llegó por partes.").
- **Por qué ahí:** Kal acaba de volverse **fuente de la policía** por tres escritorios. La escena siguiente trata de alguien que teme que un hombre bajo presión le cambie lo que sabe a una institución. Nadie lo dice; la ironía es del lector. El orden queda así: policía (Lucía) → calle (Irene) → el resultado llega por partes → Crowe → Lucía vuelve. Kal queda apretado entre los dos lados dentro de la ventana de A30 (día 2 o 3).
- **Descartado:** entre Crowe (157) y la vuelta de Lucía (161), porque pone dos tasadores de la calle seguidos y el de Crowe pierde filo. Tampoco en la coda, que es de Chiara.

**2. Escena propia, no entrelazada con Lucía.** POV de Kal, como todo el capítulo. No entra en Irene ni en Tomás.

**3. Quién va: Irene en persona, en su terreno (el Canal Seco), y Tomás como testigo del sedán.**
- **La cita** llega por Walt, en una línea (Walt fue el conducto del 17 y conoce los dos frentes): "Irene quiere verte. Hoy. Solo." Kal va solo. Eso vuelve más limpia la omisión: nadie del Patio lo ve callar.
- **Tomás** lo recibe y lo cachea (el gesto propio que 5-ter le dio al cortar su escena del 17). Delante de Irene cuenta el sedán en dos frases de testigo: dónde, cuántas veces, que no era policía de la ciudad. Es la primera línea de Tomás en el libro.
- **Irene** está con la libreta (la del 17, "ya volviendo a sus cuentas"). Habla en cuentas (ficha de voz: "lo que se debe, lo que se cobra, lo que se perdona"). No pregunta de quién es el sedán: "No sé de quién es. No me importa de quién es." El temor no se explica: basta con que diga que Nadir conoce sus rutas y que alguien está mirando a Nadir.
- **Alternativa:** Tomás va al taller a buscarlo. Se descarta porque sería el tercer visitante del taller en el capítulo (Lucía dos veces) y rompería la simetría policía/calle.

**4. Mecánica del cambio de forma (sin cifras):** Irene saca a Nadir de la mercancía desde hoy ("Su muchacho ya no carga nada mío"). Lo que faltaba del trato no se perdona: se convierte en un favor abierto de Kal, sin fecha ni precio, que Irene cobrará cuando quiera. Kal lo acepta **sin negociarlo**, que es lo contrario del 17 ("No le voy a deber un favor. Le voy a proponer un negocio."). El lector lo mide solo; nadie recuerda el 17 en voz alta.

**5. Kal no le cuenta lo de Halbrook.** Irene no pregunta, y Kal no ofrece. Si Irene tantea ("¿Usted sabe de quién es?"), Kal da una verdad más chica ("Sé que no es suyo ni mío"). Opcional; dentro del hilo A.

**6. Cierre (tres opciones):**
- **(a)** "—Ahora sí me debe, señor Mercer." Irene lo anota en la libreta y no espera respuesta. Es la línea del diseño, con el trato del 17 debajo. Cierra en el objeto, como Lucía con la tarjeta, y las dos mitades del capítulo riman: tarjeta y libreta.
- **(b)** Sin la frase: Irene escribe algo en la libreta, la cierra y dice "—Tomás lo acompaña." El lector entiende qué anotó. Es más seco y más Irene ("deja que el silencio después de una frase haga el trabajo"), pero exige que el favor haya quedado explícito antes.
- **(c)** Invertida: Kal lo dice primero ("—Le debo una.") e Irene corrige: "—Me debe lo que yo diga que me debe." Tiene más filo, pero se acerca a una amenaza y abre la cuenta con un tono que el Libro II tendría que cerrar. Contradice el límite de 5-ter.
- **Recomendación: (a)**, con la anotación en la libreta como último gesto y sin réplica de Kal.

**7. Nadir se entera (cola breve de la misma sección, ≈ 80–100 palabras).** Kal le dice que se acabó lo de Irene. Nadir pregunta por qué ahora. Kal contesta con la palabra del 17: "Porque ya alcanzó." (Irene decidía "el tiempo que usted decida que alcanza"). Es verdad y no lo es. Nadir no le cree del todo y no insiste. **No repetir el costo de S2 del 23** (Nadir dormido en el sillón de la oficina, oliendo a carretera, el café frío): Nadir aparece despierto, en otra cosa (con la moto, la Kawasaki verde, que es su orgullo y no su cansancio, o en la calle), y el costo se ve en que pierde algo que era suyo, no en fatiga. **Alternativa:** que la noticia quede fuera de escena y sólo se sepa en la coda por Chiara (hilo A). Recomendación: la cola, porque es el único sitio donde el lector ve que Kal también le administra la verdad a Nadir, justo después del 30 ("Nadir se entera de la verdad directamente por Kal"). La rima es deliberada: en el 30 se la dijo, aquí no.

**8. Hilo A de Chiara (opcional): sí, mínimo, en la coda del 32.** Entre "—Yo tampoco lo sé." (223) y "Ella no dijo nada más" (225), Chiara pregunta una sola cosa que no debería saber sin los *sussurri*: en diseño, "¿Y el Canal Seco?". Kal contesta con algo más chico ("Nada que no se arregle"). Ella deja la copa en el fregadero sin insistir; B23 ya quitó la glosa. El lector ve que Kal le dio la línea de Lucía y se guardó la de Irene, y que ella lo notó. ≈ +20 a +30 palabras. Cambia el peso de "No sé si eso me deja más tranquila o menos", que ahora vale para las dos cosas. **Riesgo:** hace la coda menos doméstica de lo que pide la metadata. Recomendación: **sí**, porque sin esto el hilo A del 32 lo ve sólo el lector.

**9. Qué no hace la escena:** no nombra a Halbrook ni a Varek (Irene no sabe; Kal no dice); no explica el temor de Irene; no amenaza a Nadir; no fija el contenido del favor; no trae a Rafe, a los Bravos ni a Lucía; no usa la palabra "federal" en boca de nadie (el lector la pone). Tomás no se vuelve personaje con interioridad.

**10. Costo estimado:** escena ≈ 750–850 + cola de Nadir ≈ 80–100 + hilo A ≈ 25 = **≈ 855–975 palabras**. Poda del 32 (C80, C82, C83, C84, B23, B24) ≈ −89. **Neto del 32 ≈ +770 a +890.** Cabe en el saldo de la Parte I (≈ +971) sin tocar la poda de la Parte II.

---

# § Metadata de 31–32 (se anota, no se toca; se sanea en E7)

| Cap:línea | Dice | Problema | Debe decir |
|---|---|---|---|
| 31:2 | "sexto capítulo de la Parte II, **cierre de la Parte II**" | El 31 es el sexto, pero no cierra la Parte II (siguen 32–34) | "sexto capítulo de la Parte II; cierra el arco H5–H7" |
| 31:4 | "MISMO DÍA que los **Caps. 28-31**… la tarde-anochecer **del día que Halbrook sacó a Kal de la ciudad de madrugada**" | § Cronología: el día del 28–31 es el del regreso; "28-31" se incluye a sí mismo | "mismo día que los Caps. 28–30… la tarde-anochecer del día del **regreso** de Kal (Halbrook se lo llevó la madrugada anterior)" |
| 31:4 / 31:10 | "al cierre de la coda del **Cap. 31**" (×2) | Numeración vieja: la coda del Patio está en el 30 | "Cap. 30" |
| 31:6 | "cierre del arco H5-H7 **y de la Parte II, el mismo día que lo abrió H5**" | H5 abre el día anterior y el 31 no cierra la Parte II | "cierre del arco H5–H7" |
| 31:7 | Línea canon: "— Ponte algo cómodo, porque quizá te vayas a mojar." | La prosa dice "Ponte algo cómodo para ir a pescar… Porque quizá te vayas a mojar." (A28) | Según D32 |
| 31:17 | "sigue con las costillas y la ceja **de esa misma madrugada**" | La paliza fue el día anterior | "de la paliza del día anterior" |
| 31:23 | "la verdadera última escena **de la Parte II**" | Igual que 31:2 | "la última escena del arco H5–H7" |
| 31:24 | "eco intencional **del Cap. 29**" | "No era una orden / Sonó como una" es del 28 (columna protegida) | "del Cap. 28" |
| 31:24 | "la misma regla del 'novia' del teléfono" | Correcto | — |
| 31:27 | "VEHÍCULOS: Kal conduce el Audi… Sin Peugeot." | Correcto con D15 | Añadir: "el Peugeot se queda en el taller (30)" |
| 32:5 | "arranca **unos dias despues** del Cap. 31… NOTA DE CONTINUIDAD, sin resolver: el Cap. 33… 'varios dias despues'…" | La prosa arranca a la mañana siguiente (A32). La nota del 33 **ya está resuelta** (33:6 dice "varios días después del Cap. 32… cerca de dos semanas") | "arranca a la mañana siguiente del Cap. 31 y se extiende cerca de dos semanas". Quitar la nota |
| 32:15 | "Vivian Varek, Dario Varek, Camp Alder y **Halbrook no aparecen ni se mencionan**" | Con P1, el sedán de Halbrook entra (sin nombre) | E9, al escribir a Irene: "Halbrook no se nombra; su sedán entra por la Ronda (P1)" |
| 32:4 | Protagonistas | Falta Irene / Tomás / Walt si entra P1 | E9 |
| 32:23 | Bloque DISEÑO fuera del comentario | A33: se imprime en el EPUB | E7: dentro del comentario |

---

# § 9 Resultado (parte 3) — SURGERY de 31 y 32 (E7, 2026-09-27)

Aplicado según Q2 (Beretta en el 31) y Q4 (veto libre de la fila "El 31 y el 32", más D28, D33, D37 y D38). Antes de editar, `git diff --stat` confirmó 31 y 32 sin cambios desde E3. **Palabras de prosa:** 31 = 4,136 → 3,878 (−258); 32 = 1,992 → 1,902 (−90). Total E7: **−348**. Finales de línea: LF en los dos, conservados (0 CR). Los dos siguen **BORRADOR**.

## Cap. 31

| # | Before | After | Categoría | Qué ya hacía la escena / qué conserva |
|---|---|---|---|---|
| B19 | "…sin decidirse, con una expresión que Kal no le había visto nunca: la de una mujer que sabía sentarse a negociar con Dario Varek y no tenía la menor idea de qué se usaba para ir a pescar." | "…sin decidirse. Sabía sentarse a negociar con Dario Varek. No tenía la menor idea de qué se usaba para ir a pescar." | SALTO DE POV | Chiara no puede ver su propia expresión. Conserva el contraste Varek/pesca, ahora desde su cabeza |
| C65 | "que Kal Mercer, que esa misma mañana había negociado con Dario Varek, acababa de vestirla" | "que Kal Mercer acababa de vestirla" | REPETICIÓN FUNCIONAL | El contraste queda en 57 y en el sillón (401) |
| P2 | "…a abrocharse las botas, y no dijo nada más sobre el asunto." | "…a abrocharse las botas, pasó el teléfono, las llaves y la Beretta .25 del bolso del trabajo a uno de lona, y no dijo nada más sobre el asunto." | SIEMBRA (canon, Q2) | Primera aparición: tercer objeto de una enumeración, sin detenerse, sin que Kal comente. El 44:219 la cobra ("llevaba ahí desde hacía años"). El bolso del sillón ("Chiara dejó el bolso sobre la mesa") queda como el de lona. **+17** |
| C67 | "—Al principio, nada bien. … Se enojó. Tenía razón en enojarse. Después hizo las preguntas…, que en él es la manera de decir que ya está bien." / "—¿Y los demás?" / "—Ninguno salió corriendo. Walt… Danny… Héctor preguntó por el sedán." / "—¿Y la pesca?" / "—Idea de Nadir. En cuanto entendió…" | "—Mal. Tenía razón en enojarse. —Kal no lo dulcificó—. Después empezó a bromear. Danny me preguntó cómo pienso salir de Camp Alder, y no tuve una buena respuesta." / "—¿Y la pesca?" / "—Idea de Nadir." | REPETICIÓN FUNCIONAL | El 30 dramatiza a Walt, Héctor y la idea de la pesca. Queda lo que Chiara no sabía: Nadir y Danny/Camp Alder. Al irse "¿Y los demás?", Danny se une a la línea de Kal sin costura |
| B20 | "Kal no dijo que sí. No dijo que no. Por primera vez en mucho tiempo no sintió la urgencia…" | "Kal no dijo que sí. No dijo que no." | SALTO DE POV / GLOSA | El puente falso lo muestra |
| C68 | "…sobre el tema, porque ya no hacía falta." | "…sobre el tema." | GLOSA | La metadata prohíbe verbalizar la tesis |
| B21 | "…caminó hacia las cañas, y el asunto, evidentemente, quedaba cerrado ahí — no porque lo hubiera perdonado, sino porque…" | "…caminó hacia las cañas." | SALTO DE POV (Harper) | El silencio de Harper cierra el asunto |
| A26 | "Miró a Chiara un momento, sin la curiosidad abierta con la que la habían mirado los demás: una evaluación…" | "Miró a Chiara un momento: una evaluación…" | CONTINUIDAD | Nadie del grupo la había mirado todavía. Conserva "cerrada", que hace el contraste solo |
| C69 | "Lo dijo sin intención de incomodar a nadie, como quien reporta un dato, y volvió a lo suyo…" | "Volvió a lo suyo…" | GLOSA / TIC "como quien" | Copiaba la metadata |
| C70 | "Chiara no necesitó que dijera nada más. Entendió exactamente lo que ese asentimiento significaba, y siguió…" | "Chiara siguió caminando hacia la orilla." | GLOSA | Walt cobra "MUY ligero": el asentimiento basta |
| C71 | "La dejó llegar a él, que era su manera de decir que ese día no tenía prisa por nada." | "La dejó llegar a él." | GLOSA | — |
| C73 | "La discusión, entendió, era el punto. Resolverla la hubiera matado." | "La discusión, entendió, era el punto." | GLOSA | Conserva la lectura de Chiara (negociadora) |
| B22 | "…esa clase de cosas — y lo dejó pasar sin que se le notara en la cara, como dejaba pasar todo lo demás." | "…esa clase de cosas —. Chiara lo sintió en el brazo que la sostenía, y en la cara de él no se vio nada." | SALTO DE POV | Conserva las costillas (la metadata pide reconocimiento mínimo) y el gesto de minimizar, ahora observable. Se conservó el inciso de las costillas, que la propuesta de E3 no mencionaba, para cumplir su "±0" |
| P3 | "…él dejó que se quedara ahí." / "—Gracias por traerme —dijo Chiara, al rato." | "…él dejó que se quedara ahí." / "Chiara tomó aire para decir algo y lo soltó." / "—Gracias por traerme." | SIEMBRA (hilo A, veto libre) | La elección de una verdad más chica se ve y no se explica. El gesto reemplaza "al rato". **+6** |
| C74 | Párrafo "Ningún nombre nuevo para lo que eran, … les había servido igual a los dos." | (cortado) | GLOSA | La sección cierra en "a algo parecido a estar en casa", que rima con "Vamos a casa" |
| C75 | "sin ningún peso especial en la voz, como quien dice cualquier otra cosa después de un día largo:" | "sin ningún peso especial en la voz:" | GLOSA / TIC | Conserva la instrucción de lectura de "Vamos a casa" |
| A27 | "por nueve pulgadas de sillón" | "por medio metro de sillón" | CONTINUIDAD | Rima con "casi medio metro" del mismo pasaje; los cuatro centímetros quedan intactos |

**Conservados según Q4:** C72 (Héctor en estilo indirecto), C66, C76, C77, C78, A28 (la prosa de la llamada manda; se corrigió la metadata), A35 ("Walt, probablemente"). La tienda de pesca, el juego acuático, la fe en la parrilla y el sillón no se tocaron. Inviolables intactos.

## Cap. 32

| # | Before | After | Categoría | Qué ya hacía la escena / qué conserva |
|---|---|---|---|---|
| A33 | `-->` antes del bloque `> **DISEÑO RESERVADO PARA PARTE III…**` | `-->` después del bloque | RESIDUO DE METADATA | El bloque ya no se imprimirá en el próximo EPUB. **El EPUB vigente lo sigue llevando** (no se regeneró, regla del vault) |
| A29 | "Era un sedán gris, sin marcas" | "Era un coche gris, sin marcas" | CONTINUIDAD | Deja "sedán" libre para el de Halbrook (P1) |
| C80 | "Eso era todo lo que Kal sabía. Era, también, exactamente lo que hacía falta." | "Eso era todo lo que Kal sabía." | COMPETENCIA EXPLICADA | El resultado lo demuestra |
| C82 | "Le llegó por partes, como suelen llegar esas cosas." | "Le llegó por partes." | TIC | — |
| C83 | "No sintió gran cosa. Fue, sobre todo, la comprobación de que un problema se había resuelto… y que eso —a diferencia de…— no le había costado una sola llamada a Héctor." | "No sintió gran cosa. Un problema se había resuelto sin que él tuviera que resolverlo con las manos." | GLOSA / REPETICIÓN FUNCIONAL | Héctor queda para la línea de Kal a Chiara ("sin que Héctor tuviera que romperle nada a nadie") |
| A30 | "La semana siguiente, cerrando la caja" / "diez días después de la primera visita" | "Días después, cerrando la caja" / "dos semanas después de la primera visita" | CONTINUIDAD | El Tasador queda antes de la vuelta de Lucía, como lo cuenta el texto |
| C84 | "…una revisión. —Lo dijo sin orgullo, como quien lee un resultado, no como quien lo celebra—. Eso no significa…" | "…una revisión. Eso no significa…" | GLOSA / TIC doble | La línea se sostiene sola |
| A31 | "colgando las llaves con más cuidado del necesario" | "dejando las llaves en el cuenco con más cuidado del necesario" | CONTINUIDAD | El cuenco del loft (Cap. 31) |
| B23 | "…la dejó en el fregadero, y se acercó a él sin prisa, no para pedirle explicaciones, sino porque ya había decidido…" | "…la dejó en el fregadero y se acercó a él sin prisa." | SALTO DE POV / GLOSA | La copa y el silencio archivan el dato |
| B24 | "Kal la dejó acercarse, y no volvió a pensar en la tarjeta hasta mucho después." | "Kal la dejó acercarse." | PROLEPSIS DE NARRADOR (§L) | Se corta, no se suaviza |

**Conservados según Q4:** "todavía" (32:215, aprobado por el autor), C79, C81, C85 (el sillón), C86 (Crowe), A34 (la coartada como figura).

## Metadata saneada (31 y 32)

- **31:** Estado (cierra el arco H5–H7, no la Parte II; nota de cirugía); ventana temporal (Caps. 28–30, día del regreso de Kal; coda del Cap. 30); Función (sin "y de la Parte II"); línea canon de la llamada según la prosa (D32); EN EL CAMINO reescrito para el resumen comprimido; costillas "de la paliza del día anterior"; "la última escena del arco H5–H7"; eco "del Cap. 28"; el Peugeot se queda en el taller (30).
- **32:** Estado (nota de cirugía); ventana temporal ("a la mañana siguiente del Cap. 31… cerca de dos semanas"; se retira la nota vieja del 33, ya resuelta). **Quedan para E9:** 32:4 (Protagonistas: Irene, Tomás, Walt) y 32:15 (Halbrook no se nombra; su sedán entra por la Ronda).
- **Queda sin tocar en 31:23:** "esa misma madrugada había planteado parar lo que construían". No estaba en la tabla de E3; se anota para E8 por si el autor quiere revisar en qué momento lo planteó Kal.

## Punto de inserción de Irene (P1, para E9)

- **Después de 32:131**, frase ancla: **"Lo archivó, junto con el resto, y volvió al taller."** (sigue en la línea 131 después de la cirugía: el traslado del `-->` no cambió el número de líneas).
- Sección propia con `***` antes y después. La sección siguiente arranca con **"Le llegó por partes."** (ya comprimida por C82).
- Coda: el hilo A ("¿Y el Canal Seco?") entra entre "—Yo tampoco lo sé." y "Ella no dijo nada más." (B23 ya quitó la glosa de esa línea).
- Paquete aprobado (Q3): Irene en persona en el Canal Seco; la cita por Walt; Kal va solo; Tomás cachea y cuenta el sedán; cierre "—Ahora sí me debe, señor Mercer." con la libreta, sin réplica; cola de Nadir "Porque ya alcanzó.".

## Autocrítica E7 (MICROEDICION §F)

- **Lo más dudoso:** P2. La Beretta entra delante de Kal; que él no diga nada puede leerse como que ya lo sabe. Se eligió enterrarla en una enumeración de cuatro acciones para que no pese más que las botas. Si el autor la quiere fuera de la vista de Kal, habría que añadir una salida suya del vestidor.
- **Lo más agresivo:** C67 (−71 en el diálogo del coche). Walt y Héctor desaparecen del resumen; se apoya en que el 30 los muestra en escena.
- **Pareció corte y quedó protegido:** el inciso de las costillas en B22 (la propuesta lo omitía; es información que Chiara tiene y que la metadata pide); C72, por veto libre.
- **Riesgo de esterilizar:** moderado en el 31 (C74 y C71 tenían cadencia cálida), bajo en el 32.
- **Racionalizar interioridad:** B19 y B22 van en sentido contrario: vuelven pensamiento propio o percepción del POV lo que antes era interioridad ajena.
- **Prosa más genérica:** las líneas nuevas son B19 (dos frases cortas), B22, P2 y P3. Son del agente y el autor debe leerlas.

---

# Parte 4 — Caps. 33 y 34 (E4)

**Estado para el `git diff --stat` de E8:** 33 y 34 sin cambios en el árbol de trabajo al 2026-09-27; último commit `1af8c6a`. Palabras: 33 = 3,720 · 34 = 1,529. Finales de línea: LF en los dos (verificado con `file`); conservarlos.

## 0. Diagnóstico corto

- **33 (MEDIA).** La escena del Monarch funciona, y el miniromance que señala el dictamen **no está en el diálogo sino en el narrador**. Kenji y Marisol hablan con química y respeto: él asume el error, ella lo encontró, nadie coquetea. Pero Chiara nombra la química tres veces: la calma que "le cuesta" a Kenji (45, 137, 185), "más difícil de leer" (137, 187) y "notó el cambio sin necesitar nombrarlo" (181), justo antes de nombrarlo. Se compacta el narrador y **el diálogo de los dos se queda entero**, porque lo cobran 38:109 y el canon del noviazgo fuera de foco. En la coda, las líneas canon quedan intactas; salen dos glosas pegadas a "La suficiente para preocuparme" (391 y 395) y los tics ("guardar donde guardaba" ×2, "hacer el trabajo", "ya no hacía falta"). Hay un salto de POV hacia Marisol (69) y una cronología vieja: "hace unos días" (91), cuando ya pasaron semanas. La metadata también está vieja.
- **34 (MÍNIMA).** La transición Marisol → compromiso funciona **sin líneas nuevas**. El gozne es "el ejemplo" (52) → un silencio que "no era el de siempre" (64) → la broma sobre "tu propio juego" (66–70) → el falso alivio (72–74) → la pregunta canon (76). La única calibración está en 148: el narrador explica el chiste de "¿Y lo nuevo?" (inviolable) con un salto de POV ("los dos entendieron"). Explicarlo le quita la gracia. Además hay un "un grado" (76). Queda una duda de continuidad: palomitas en Il Gelsomino, que es un restaurante (34). El canon de H21 se cotejó línea por línea con `Hitos.md` (2399–2427) y es literal.

## 1. Candidatos por categoría (33 y 34)

### A. Continuidad y mecánica

| # | Cap:línea | Texto | Problema | Propuesta | Palabras |
|---|---|---|---|---|---|
| A36 | 33:91 | "Kal descubrió algo **hace unos días**." | Vivian lo dice en el 29, el día del regreso. El 32 dura unas dos semanas (A30) y el 33 es "varios días después" | "hace **unas semanas**" | 0 |
| A37 | 33:223 · 391 | "después de la semana que habían tenido" / "esa semana" | Es la semana del propio 33 | CONSERVAR | 0 |
| A38 | 34:34 | "Los vi en **Il Gelsomino**. Compartiendo una bolsa de **palomitas**" | Il Gelsomino es el restaurante italiano de H2-a (`05_Locations/San_Aurelio.md`), así que las palomitas no caben ahí. Es una línea de DISEÑO del agente (H21 no la contiene) | **D46.** (a, recomendada) "Los vi a la salida del cine." (b) conservar el lugar y cambiar el objeto (un postre); (c) conservar | 0 |
| A39 | 33:67 | "la única vez que se habían visto de verdad" | Cap. 21, primera interacción Chiara–Marisol | Compatible | 0 |
| A40 | 34:46 · 66 | "dos años" / "Una niña de veinte años" | Ficha de Marisol: veinte (borrador del Cap. 15) | Compatible | 0 |

### B. Prolepsis y saltos de POV

El 33 es POV único de Chiara y el 34, POV único de Kal. **Ninguno tiene prolepsis de narrador**, y el 33 no presagia la muerte de Kenji (verificado).

| # | Cap:línea | Texto | Categoría | Propuesta | Palabras |
|---|---|---|---|---|---|
| B25 | 33:69 | "Era la pregunta que le había estado haciendo a Kenji, **reciclada ahora contra las dos personas que tenía enfrente, porque a esas alturas ya sospechaba que eran la misma cosa con dos caras.**" | SALTO DE POV (la sospecha de Marisol dada como dato); 73 lo muestra | "No era una pregunta hecha a Chiara. Era la pregunta que le había estado haciendo a Kenji." | −23 |
| B26 | 34:148 | "Kal y Chiara se miraron**, y los dos entendieron en el mismo instante que probablemente eran las únicas dos personas de esa llamada —y quizá de todo su círculo cercano— que hasta hacía diez segundos no habían terminado de aceptar algo que los demás llevaban tiempo dando por hecho.**" | SALTO DE POV + GLOSA: explica "¿Y lo nuevo?" | "Kal y Chiara se miraron." Se quedan los silencios de 148 y "Kal colgó sin despedirse." | −45 |
| B27 | 34:172 | "con la certeza incómoda de que ningún minuto gastado en otra cosa le iba a alcanzar después" | Límite de §L | PROTEGIDO: es lo que Kal siente, no un hecho futuro dicho por el narrador | 0 |

### C. Glosa, tic, repetición y certificación

**Cap. 33**

| # | Línea | Texto | Categoría | Propuesta | Palabras |
|---|---|---|---|---|---|
| C87 | 107 | "No llegó ninguna. **Chiara se quedó con eso, sin explicarlo más, y algo** en la postura de Marisol bajó un grado**, no del todo, pero lo suficiente para que se notara.**" | GLOSA ("No llegó ninguna" ya lo dice) + INTENSIFICADOR ("un grado" ya es la medida) | "No llegó ninguna. Algo en la postura de Marisol bajó un grado." | −20 |
| C88 | 121 | "Pero dejó de tener los brazos cruzados de la misma manera**, y cuando volvió a hablar, ya no sonaba a alguien atacando una excusa, sino a alguien haciendo preguntas de verdad.**" | GLOSA (anuncia la pregunta de 123) | Cortar desde la coma. Los brazos se quedan (motivo 41 → 93 → 121 → 219) | −21 |
| C89 | 127 | "Marisol lo miró como si esa respuesta la hubiera descolocado…" | GLOSA leve | DUDOSA — CONSERVAR: es la química vista desde Chiara, una sola vez | 0 |
| C90 | 137 | "Fue lo más cerca que Chiara lo había visto de perder el hilo de su propia calma**, y no fue por presión, ni por miedo a que Chiara lo estuviera oyendo: fue porque, evidentemente, Marisol le resultaba más difícil de leer de lo que estaba acostumbrado.**" | GLOSA + REPETICIÓN FUNCIONAL (185–187) | Cortar desde la coma. Queda la calma que se le escapa, que es un dato que sólo Chiara tiene | −30 |
| C91 | 141 | "—preguntó Chiara**, con curiosidad genuina, no como interrogatorio.**" | GLOSA (el cálculo de Marisol en 143 es la respuesta) | "—preguntó Chiara." | −7 |
| C92 | 153 | "casi de pasada**, como si no le pareciera gran cosa**" | REPETICIÓN (dos incisos con el mismo trabajo) | "casi de pasada" | −8 |
| C93 | 159 | "**Guardó eso donde guardaba las cosas que no sabía todavía qué hacer con ellas.**" | TIC: familia C45, sexta aparición en 28–33 | Cortar; "Chiara sintió algo parecido a reconocerse ahí, aunque no lo dijo." cierra la sección | −14 |
| C94 | 163 | "un billete de veinte asomado que nadie había terminado de guardar **desde que la conversación empezó a importar más que el trabajo**" | GLOSA (el billete es el gesto) | Cortar la cláusula | −11 |
| C95 | 181–187 | "Chiara los miró a los dos, uno y otro**, y notó el cambio sin necesitar nombrarlo: la conversación ya no giraba… terminar de contestar.** / Marisol seguía sin estar del todo tranquila. Pero ya no quería irse. / **Kenji seguía siendo el mismo hombre calmado… nunca verle.** / **Cada uno había encontrado a alguien más difícil de leer… entender ahí.**" | **Foco del dictamen (miniromance).** REPETICIÓN FUNCIONAL (la calma de Kenji por tercera vez, "más difícil de leer" por segunda) + GLOSA que nombra lo que dice que no hace falta nombrar | **D47.** "Chiara los miró a los dos, uno y otro. / Marisol seguía sin estar del todo tranquila. Pero ya no quería irse." | −96 |
| C96 | 199 | "Había una versión de sí misma… porque organizar era lo que sabía hacer con la incomodidad. Esta vez no insistió…" | GLOSA de cambio / INTERIORIDAD | DUDOSA — CONSERVAR: es la función del capítulo según la metadata ("aprende a dejar de administrar") y es el único sitio donde se dice, desde dentro | 0 |
| C97 | 267 | "Lo tomó como algo que guardar**, de la misma manera en que se guardaba todo lo demás.**" | TIC (guardar) | "Lo tomó como algo que guardar." | −12 |
| C98 | 309 | "Ninguno de los dos lo comentó**, porque ya no hacía falta comentarlo.**" | GLOSA + TIC ("no hacía falta", familia de B12 y B14) | "Ninguno de los dos lo comentó." Lo no dicho prepara el 34 | −7 |
| C99 | 343 | "la mandíbula un poco tensa**, reconstruyendo en silencio algo que a Chiara le tomó menos tiempo explicar de lo que a él le tomó procesar.**" | GLOSA, con lógica rota: ella todavía no ha explicado nada | "Kal se quedó con eso un segundo, la mandíbula un poco tensa." | −21 |
| C100 | 361 | "el susto y el orgullo llegando casi al mismo tiempo…" | INTERIORIDAD (lectura de Chiara; la metadata pide el orgullo sin verbalizarlo) | PROTEGIDO | 0 |
| C101 | 391 | "Kal tardó en contestar. **No porque no supiera la respuesta, entendió Chiara, sino porque decirla en voz alta le costaba un esfuerzo distinto del que le costaba resolver cualquier otra cosa esa semana.**" | GLOSA justo antes de la línea canon. Es además la tesis del 34 (a Kal le cuesta nombrar lo que siente), que el 34 dramatiza entera | **D48.** Cortar: "Kal tardó en contestar." | −29 |
| C102 | 395 | "y dejó que la frase se quedara ahí, sola**, haciendo el trabajo que tenía que hacer sin que nadie más la tocara.**" | GLOSA + TIC ("hacer el trabajo": 29:107, 34:42) | Cortar desde la coma. "No lo felicitó… como si acabara de aprobar un examen" se queda (voz, humor) | −14 |
| C103 | 89 | "sin dorarlo y sin encogerlo" | Familia "sin adornarlo" (C59) | DUDOSA — CONSERVAR: el par es medida, no acotación, y es el hilo A (ella administra la verdad) | 0 |
| C104 | 73 | "con la velocidad de alguien acostumbrada a conectar puntos…" | COMPETENCIA EXPLICADA leve | DUDOSA — CONSERVAR: rima con "Veo que sigues conectando puntos" (327) | 0 |
| C105 | 125 | "Lo supe cuando empecé a acordarme de cosas que no necesitaba recordar." | Química | PROTEGIDO: es la única línea que dice la atracción, y la dice Kenji como definición de su error | 0 |

**Cap. 34**

| # | Línea | Texto | Categoría | Propuesta | Palabras |
|---|---|---|---|---|---|
| C106 | 76 | "algo en su voz **cambió, se afiló un grado**" | TIC "un grado" (29:85 conservado; 33:107) | "algo en su voz se afiló" | −3 |
| C107 | 156 | "No era una acusación. Era casi ternura disfrazada de cifra." | GLOSA de la línea canon | **D49.** DUDOSA — CONSERVAR: es la lectura de Kal, y "ternura disfrazada de cifra" es voz. Alternativa: cortar las dos oraciones (−10) | 0 |
| C108 | 168 | "**No era una confesión construida; era** lo único que le había quedado…" | GLOSA leve: certifica que no es discurso, que es justo lo que H21 prohíbe | "Era lo único que le había quedado…" El símil del motor se queda: con C38 del 30, es el segundo de la familia, no el quinto | −5 |
| C109 | 114 | "Era mentira, y los dos lo sabían: los sobornos cariñosos casi siempre funcionaban cuando estaban solos, en el loft…" | Leve (los dos) | DUDOSA — CONSERVAR: humor, y fija la diferencia entre el loft y el mundo que la escena necesita | 0 |
| C110 | 42 | "había dejado que el silencio hiciera el trabajo que hacía con hombres que mentían por oficio" | Eco de 29:107 | PROTEGIDO: es el método de Kal nombrado, y es lo que Marisol derrota | 0 |

**Suma de lo recomendado (sin DUDOSAS):** 33 ≈ −313 · 34 ≈ −53. Es referencia, no meta (§J).

## 2. Prolepsis y POV — lectura por capítulo

- **33 (POV Chiara, único).** No hay prolepsis. Hay un salto (B25). Las lecturas de Chiara sobre Kenji y Marisol (45, 57 "probablemente", 115, 121, 179 "probablemente", 361) están enmarcadas como suyas y se protegen. La de 137 se va con C90 porque "evidentemente" la vuelve dato.
- **34 (POV Kal, único).** No hay prolepsis; B27 es sentimiento del POV. Hay un salto (B26). "Kal no le pidió que tradujera" (176) cumple la regla de voz.

## 3. Función por movimiento

**Cap. 33 (3,720)**

| Líneas | Movimiento | Palabras | Función | Veredicto |
|---|---|---|---|---|
| 29–49 | El Monarch por la mañana; el corredor; Marisol en la caja | 531 | Costura con 30–32 ("una silla que todavía no sabía bien cómo nombrar"); la calma de Kenji "le cuesta" por primera vez | **Intacto** |
| 53–85 | "¿Me buscabas?" → "Empezó conmigo" | 406 | Marisol acusa; Chiara no niega lo obvio (83: hilo A) | B25 |
| 89–107 | La verdad administrada y la disculpa sin justificación | 292 | Chiara no nombra a Halbrook, la silla ni el pacto; "Desde mi lado de la calle…" | C87 (C103 dudosa) |
| 111–137 | Kenji asume el error | 393 | **Respeto**: "No hubiera sido cierto." **Química**: "acordarme de cosas…" | C88, C90 (C89 dudosa, C105 protegida) |
| 141–159 | Cómo lo encontró; "Quería saber por qué" | 181 | Marisol invierte la regla de Kal; Chiara se reconoce | C91, C92, C93 |
| 163–187 | El billete; "Tenía una tarea"; "No soy tan adulto / Pareces uno" | 295 | Química en diálogo; **el narrador la nombra tres veces** | C94, **C95 (−96)** |
| 191–219 | Chiara se retira; "contar dinero" | 284 | Deja de administrar; los dos se quedan hablando fuera de su oído | **Intacto** (C96 dudosa) |
| 223–309 | Loft: ciabatta, *Ladro*, *Assaggia*, *Manca sale*, el abrazo | 561 | Registro privado post-H7 sin etiqueta; italiano suelto | C97, C98 |
| 311–409 | "Seguramente le parta las piernas" → "La suficiente para preocuparme" → el turno de caja | 762 | **Canon del autor**; pago de la columna 28 → 29 → 30 | C99, C101, C102. Diálogo intacto |

**Cap. 34 (1,529)**

| Líneas | Movimiento | Palabras | Función | Veredicto |
|---|---|---|---|---|
| 20–22 | El camino de grava; el Audi; las etiquetas de Walt | 195 | Lugar concreto; Chiara descalza "algo que jamás haría en el Lancia" | **Intacto** |
| 24–74 | Marisol le gana a Kal; "el ejemplo"; "tu propio juego"; falso alivio | 389 | **Transición Marisol → compromiso.** Funciona sin líneas nuevas | A38. Resto intacto (C110 protegida) |
| 76–114 | Pregunta canon; freno; volante; "sobornos cariñosos" | 315 | H21 canon literal | C106 (C109 dudosa) |
| 116–150 | La llamada: "Mi pareja." / "¿Y lo nuevo?" | 235 | Canon; el chiste es el pago | **B26 (−45)** |
| 152–182 | Tren; "el efectivo de este auto"; "Ahora sé todo lo que puede salir mal"; *Tiri fuori*; "ninguno de los dos tuvo que preguntar adónde" | 389 | Canon, más la explicación emocional que H21 dejó abierta | C108 (C107 dudosa; B27 protegida) |

## 4. Protegido y siembras

- **Canon del 33 (metadata: "CANON DEL AUTOR"):** "Seguramente le parta las piernas." / "Eso me dejaría sin un buen elemento en el casino."; "La suficiente para preocuparme. No la suficiente para escoger por ella."; "tú cubres su turno… Sabia decisión."; la pregunta base "¿Qué importancia tiene para ti con quién sale Marisol?".
- **Kenji y Marisol, química y respeto (se queda todo el diálogo):** "No hubiera sido cierto."; "acordarme de cosas que no necesitaba recordar"; "información que no debería estar dándote gratis" / "No te la estoy cobrando"; "Todavía estoy decidiendo qué hago yo con eso"; "Tenía una tarea. El plan se fue complicando solo."; "No soy tan adulto." / "Pareces uno. Es molesto."; "Contar dinero… La otra parte es lo que estaba pasando hace diez minutos."; "Desde mi lado de la calle la diferencia era bastante pequeña"; "Yo no me alejé. Quería saber por qué." **Qué se compacta:** sólo el narrador que lo traduce (C87, C88, C90, C94, C95).
- **Pagos en 35–44 (búsqueda):** **38:109**, en el yate. Kenji aparece sin el chaleco del Monarch y le dice algo a Marisol; "Marisol se detuvo medio segundo y dejó de moverse, cosa que no hacía nunca". El pasaje cobra el 33 sin nombrarlo y necesita que el lector ya tenga la química, que el diálogo del 33 le da. 34:24–62 (Kal los vigila y Marisol lo derrota) cobra el "Quería saber por qué". Canon de las fichas: noviazgo fuera de foco en los Libros I y II, y muerte de Kenji en Santa Lucía (Libro II). **El 33 no presagia nada** y la poda no toca ninguna línea de los dos. *Ladro*, *Assaggia* y *Manca sale* no se cobran en 35–44; se protegen como registro privado y voz de Chiara.
- **Motivos que se protegen en el 33:** los brazos de Marisol (41 → 93 → 121 → 219); el cajón y el billete (53 → 163); la calma de Kenji en dos apariciones (45 y 137, después de C90); 83 (a la gente inteligente se le miente sobre lo no obvio: hilo A); 151; 199; 361.
- **Canon del 34 (Hitos H21, 2399–2427), verificado literal:** "¿le tienes miedo al compromiso?" / "¡¿Qué?!" ×2 / "Yo creí que era porque querías que no le pusiéramos nombre a esto."; "Los sobornos cariñosos…"; "Sabes que Chiara y yo…" / "Sí." / "…ella es mi…" / "Mi pareja." / "Ajá." / "Y ya." / "¿Y lo nuevo?"; el efectivo del Audi; los dedos entrelazados; *Tiri fuori il meglio di me…* Además: "Yo no hago esto. No así." / "¿Y ahora?" / "Ahora sé todo lo que puede salir mal." (recorte del autor, 2026-09-20); "Esta vez, cuando volvieron, ninguno de los dos tuvo que preguntar adónde." (encargo).

## 5. Lo que no es de microedición (se reporta y no se opera)

1. **Metadata del 33 (E8):** "unos días después del Cap. 31" (el 32 arranca a la mañana siguiente, A32); "Cierra la Parte II (penúltimo capítulo…)"; la lista de documentos desactualizados (Hitos: "falta un hito para la periferia dentro de la apertura de Parte III", cuando el capítulo ya está en la Parte II); "Lancia/Audi" (ya fijado, D15).
2. **Metadata del 34 (E8):** "La periferia" ×3 (el título vigente es *Más de la cuenta*); "Chiara vino con él **desde el norte**", cuando la prosa la trae de la destilería de Walt; la línea "Lo haré cuando tú pongas el ejemplo" se cita como línea de Marisol, pero la prosa la da en estilo indirecto ("me dijo que me lo iba a contar el día que yo pusiera el ejemplo"); el ritual del *Ciao* "queda para una escena futura sin fecha", cuando ya nace en el 35.
3. **P4 (Nadir hace algo duro por el grupo y le cuesta), comprobado contra 33–44.** El 33 y el 34 no lo tocan. **43:145–155** lo roza: Nadir dice "Contigo", se detiene a medio camino del helicóptero para volver por Kal y Héctor lo mete a la fuerza. En 44:49 quiere ir y Héctor se lo impide. Es una decisión que Nadir **no llega a tomar**, un acto frustrado, no uno pagado. Recomendación: **no añadir nada en el Libro I**. P4 queda para el Libro II (F2), con el 43 como antecedente. Ver D50.
4. **Ritual del *Ciao* en 26–34 (búsqueda):** en la prosa no hay "Ciao", "tesoro", "amore" ni "cariño" como apodo (en 34:112–114, "cariñosos" es adjetivo). **Conforme con el canon:** Kal recibe "Ciao, tesoro" por última vez en **19:156**, antes de formalizarse; el 34 formaliza sin apodo; "amore mio" y el ritual nacen en el **35**, y el 42 vuelve a "Ciao, tesoro" como regresión. No hace falta ninguna siembra. La metadata que choca: **26:17** ("Ciao, bello… nace tras H21") pasa a "*Ciao, bella* / *Ciao, bellissimo* nace en el 35; nunca *Ciao, bello*" (E5); y 34:12 (punto 2).

---

# § 9 Resultado (parte 4) — SURGERY de 33 y 34, y housekeeping documental (E8, 2026-09-27)

Aplicado según Q4 (veto libre de la fila "El 33 y el 34", más D46 (a) y B25–B26). Antes de editar, `git diff --stat` confirmó que 33 y 34 no habían cambiado desde E4. **Palabras de prosa:** 33 = 3,720 → 3,417 (−303); 34 = 1,529 → 1,479 (−50). Total E8: **−353**. Finales de línea: LF en los dos, conservados (0 CR). Los dos siguen en **BORRADOR**.

## Cap. 33

| # | Before | After | Categoría | Qué ya hacía la escena / qué conserva |
|---|---|---|---|---|
| A36 | "Kal descubrió algo hace unos días." | "…hace unas semanas." | CONTINUIDAD | El 32 dura unas dos semanas |
| B25 | "…haciendo a Kenji, reciclada ahora contra las dos personas que tenía enfrente, porque a esas alturas ya sospechaba que eran la misma cosa con dos caras." | "…haciendo a Kenji." | SALTO DE POV | 73 muestra cómo encaja la sospecha |
| C87 | "No llegó ninguna. Chiara se quedó con eso, sin explicarlo más, y algo en la postura de Marisol bajó un grado, no del todo, pero lo suficiente para que se notara." | "No llegó ninguna. Algo en la postura de Marisol bajó un grado." | GLOSA + INTENSIFICADOR | "Un grado" ya es la medida |
| C88 | "…de la misma manera, y cuando volvió a hablar, ya no sonaba a alguien atacando una excusa, sino a alguien haciendo preguntas de verdad." | "…de la misma manera." | GLOSA | La pregunta de 123 lo demuestra. Se queda el motivo de los brazos |
| C90 | "…de su propia calma, y no fue por presión… fue porque, evidentemente, Marisol le resultaba más difícil de leer de lo que estaba acostumbrado." | "…de su propia calma." | GLOSA + REPETICIÓN | La calma que se le escapa es lo que ve Chiara; se va el "evidentemente" |
| C91 | "—preguntó Chiara, con curiosidad genuina, no como interrogatorio." | "—preguntó Chiara." | GLOSA | El cálculo de Marisol (143) responde |
| C92 | "casi de pasada, como si no le pareciera gran cosa" | "casi de pasada" | REPETICIÓN | — |
| C93 | "…aunque no lo dijo. Guardó eso donde guardaba las cosas que no sabía todavía qué hacer con ellas." | "…aunque no lo dijo." | TIC (familia C45) | La sección cierra en el reconocimiento |
| C94 | "…que nadie había terminado de guardar desde que la conversación empezó a importar más que el trabajo." | "…que nadie había terminado de guardar." | GLOSA | El billete es el gesto |
| C95 | Cuatro párrafos: "Chiara los miró… y notó el cambio sin necesitar nombrarlo… / Marisol seguía… / Kenji seguía siendo el mismo hombre calmado… / Cada uno había encontrado a alguien más difícil de leer…" | "Chiara los miró a los dos, uno y otro. / Marisol seguía sin estar del todo tranquila. Pero ya no quería irse." | REPETICIÓN FUNCIONAL + GLOSA (miniromance del narrador, D47) | El diálogo de los dos queda entero; "Pero ya no quería irse." hace el trabajo |
| C97 | "Lo tomó como algo que guardar, de la misma manera en que se guardaba todo lo demás." | "Lo tomó como algo que guardar." | TIC | — |
| C98 | "Ninguno de los dos lo comentó, porque ya no hacía falta comentarlo." | "Ninguno de los dos lo comentó." | GLOSA + TIC | Lo no dicho prepara el 34 |
| C99 | "…la mandíbula un poco tensa, reconstruyendo en silencio algo que a Chiara le tomó menos tiempo explicar de lo que a él le tomó procesar." | "…la mandíbula un poco tensa." | GLOSA (lógica rota) | — |
| C101 | "Kal tardó en contestar. No porque no supiera la respuesta, entendió Chiara, sino porque decirla en voz alta le costaba un esfuerzo distinto…" | "Kal tardó en contestar." | GLOSA antes de línea canon (D48) | El 34 dramatiza la tesis |
| C102 | "…se quedara ahí, sola, haciendo el trabajo que tenía que hacer sin que nadie más la tocara." | "…se quedara ahí, sola." | GLOSA + TIC | Se queda "No lo felicitó… como si acabara de aprobar un examen" |

**Conservados:** C89, C96, C100, C103, C104 y C105. Todo el diálogo de Kenji y Marisol (pago en 38:109), el canon de la coda y *Ladro* / *Assaggia* / *Manca sale*.

## Cap. 34

| # | Before | After | Categoría | Qué ya hacía la escena / qué conserva |
|---|---|---|---|---|
| A38 | "—Los vi en Il Gelsomino. Compartiendo una bolsa de palomitas…" | "—Los vi a la salida del cine. Compartiendo una bolsa de palomitas…" | CONTINUIDAD (D46 a) | Las palomitas se quedan porque la réplica "Eso es exactamente lo más normal del mundo" las necesita. **Línea del agente (5 palabras)** |
| C106 | "algo en su voz cambió, se afiló un grado" | "algo en su voz se afiló" | TIC | — |
| B26 | "Kal y Chiara se miraron, y los dos entendieron en el mismo instante que probablemente eran las únicas dos personas…" | "Kal y Chiara se miraron." | SALTO DE POV + GLOSA | El chiste de "¿Y lo nuevo?" se cobra solo, entre los dos silencios y "Kal colgó sin despedirse." |
| C108 | "No era una confesión construida; era lo único que le había quedado…" | "Era lo único que le había quedado…" | GLOSA leve | Se queda el símil del motor |

**Conservados:** C107 ("ternura disfrazada de cifra", D49), C109, C110 y B27. El canon de H21 queda literal.

## Metadata saneada (33 y 34)

- **33:** Estado (nota de cirugía); ventana temporal (el 32 arranca a la mañana siguiente del 31; "unas semanas" después del día del regreso); Función ("penúltimo capítulo… el 34 la cierra"; "Cap. 30 (Media Baraja, en las cascadas)"); pago "La correa / El patio ajeno / Media Baraja"; VEHÍCULOS (Lancia / Audi fijados); nota de Hitos ("La periferia" ya está en la Parte II).
- **34:** Estado (nota de cirugía); "La periferia" pasa a *Más de la cuenta* ×3 (la nota histórica de la renumeración se conserva con aclaración); Función (el 35 abre la Parte III; H16 cae en el 36); la línea de Marisol, anotada como estilo indirecto en la prosa; el ritual del *Ciao* nace en el 35; "desde la destilería de Walt".

## Housekeeping documental — hecho

| Referencia vieja | Dónde | Qué se hizo |
|---|---|---|
| El 31 "cierra la Parte II" / "última línea de la Parte II" | Hitos, nota ESCRITO de H7 (l. 1709) | Corregido en la nota del agente: cierra el arco H5–H7 |
| "río norte" | Hitos H7 (nota ESCRITO, texto del hito, PENDIENTE de `05_Locations/`) | Nota ESCRITO corregida ("el lago, antes río norte"). El texto del hito **se conserva** con una nota de geografía vigente; el PENDIENTE se anota |
| "Caps. 28-31" / "coda del Cap. 31" / "Caps. 32-33" | Book Map, entrada del 31 | Numeración corregida a 28–30, coda del 30, Caps. 32–34 |
| "La Construccion" | Book Map, encabezado de la Parte II | Pasa a "Con peores personas he tratado", con nota del título anterior |
| Mecánica vieja de H6 ("Kal se ofrece a trabajar para Varek") | Timeline Libro I (l. 85); `Dario_Varek.md` l. 51 (DISEÑO) | Corregido con referencia al Cap. 29 |
| "Cap. 32 no cambia de posición" (30:21, numeración ambigua) | Metadata del 30 | Nota aclaratoria; el texto original se conserva |
| Documentos desactualizados | Metadata del 29 (l. 28) | Nota: anotados en Hitos, ficha de Dario y timeline |
| El Lancia no estaba registrado | Ficha de Chiara (l. 328) | Nota: Lancia desde el 25; el Mercedes sigue siendo corporativo |
| "H7 — El río" | Timeline Libro I | Se añade "(en la prosa, el lago; Cap. 31)" |
| "dos días" / "segunda noche" | Timeline Libro I | Búsqueda: 0 apariciones. No hizo falta nada |
| Halbrook "llega al cierre del Libro I" | Fichas, Hitos, timeline, Biblia, Book Map | Búsqueda: 0 apariciones fuera de la metadata ya saneada en E5 |

## Housekeeping — pendiente para el autor (contradicción de canon, no desfase; **no se sobrescribió**)

1. **Hitos H6 §5** (canon del hito): "Kal ofrece trabajar para Varek". La prosa y el dictamen dicen que Varek le ofrece la silla. Se añadió una nota con las dos versiones, y lo mismo en la sección CANON de `Dario_Varek.md` (l. 161). **Decides tú** si reescribes el hito.
2. **Hitos H6 §7:** "pactan… deshacer la organización de Varek desde dentro", con el DISEÑO "hasta que la organización sea suya". Contra Q1 (V2) no hay contradicción de dirección, pero sí de certeza. Se añadió una nota de alcance.
3. **Hitos H7:** "viaje masivo al río norte" (el texto del hito se conserva con nota). La entrada de `05_Locations/` para el lago y la formación de roca sigue pendiente (BACKLOG l. 27).
4. **`00_Front_Matter/00_Nota_Editorial.md` l. 19:** "Part 02 - La Construccion". No estaba en la lista del dictamen y puede imprimirse en el EPUB. No se tocó; decide el autor.
5. **31:23:** "esa misma madrugada había planteado parar lo que construían" (anotado en E7). Sigue abierto para el autor.
6. **Hitos, título de H7 ("El río"):** se deja como nombre del hito.

## Autocrítica E8 (MICROEDICION §F)

- **Lo más dudoso:** B26. Sin la glosa, el silencio después de "¿Y lo nuevo?" depende de que el lector entienda solo que los demás ya lo sabían. Las tres líneas del canon lo sostienen, pero si el autor siente que el chiste queda seco, bastaría media frase de vuelta, sin el salto de POV.
- **Lo más agresivo:** C95 (−96). Se apoya en que la calma de Kenji ya está en 45 y 137.
- **Pareció corte y quedó protegido:** 33:199 (dejar de administrar), 33:125 y C107.
- **Riesgo de esterilizar:** moderado en el 33, porque la sección del Monarch pierde cinco cierres de párrafo reflexivos seguidos; bajo en el 34.
- **Prosa más genérica:** la única línea nueva es A38 ("a la salida del cine"). Las notas de housekeeping son documentales y no tocan la prosa.
- **Alcance:** el encargo (regla 8) reserva Hitos, fichas y Book Map para E9, pero E8 pide housekeeping de esos mismos archivos. Me limité a correcciones puntuales de desfase y a notas que no borran nada. El registro de E9 (bloques de avance, entradas de capítulos, fichas de Irene y Nadir) queda intacto.

---

# § 9 Resultado (parte 5) — Escena de Irene y registro final (E9, 2026-09-27)

**Rol:** redacción, no microedición (decisión 5-ter, paquete Q3). Todo lo nuevo queda **BORRADOR/DISEÑO hasta lectura del autor**. El 32 sigue BORRADOR. Finales de línea: LF en el 32, conservado; CRLF conservado en el dictamen y en la ficha de Irene.

## Lo escrito en el 32

| Pieza | Dónde | Palabras | Qué hace |
|---|---|---|---|
| Escena de Irene | Sección propia tras "Lo archivó, junto con el resto, y volvió al taller.", antes de "Le llegó por partes." | 525 | Walt trae el recado ("Irene quiere verte. Hoy. Solo."; "¿Voy contigo?" / "No."). Kal va solo en el Audi. Tomás cachea ("Brazos.") y cuenta el carro en una línea de testigo ("Policía de aquí no es; a los de aquí los conozco."). Irene lo cruza con la libreta: "Las tres veces cargaba su muchacho." "No sé de quién es el carro. No me importa de quién es. Usted a lo mejor sí sabe." Kal da la verdad más chica: "Yo no lo he visto." / "No le pregunté." El temor sale sólo como lista de rutas contada con los dedos y "Y alguien lo está mirando." Nadir fuera de la mercancía "desde hoy"; lo que faltaba se cambia por un favor abierto "cuando lo necesite, se lo mando decir con Tomás". Kal: "Está bien." / "¿No va a regatear?" / "Hoy no." Cierre: "—Ahora sí me debe, señor Mercer." y la línea en la libreta, sin réplica |
| Cola de Nadir | Misma sección | 96 | Nadir tensa la cadena de la Kawasaki (la que en el 23 estaba floja; sin glosa). "¿Por qué ahora?" / "Porque ya alcanzó." Nadir prueba la tensión con el pulgar (gesto de Kal en el 23). "Wallah. Qué barato me salió": minimiza con humor comercial (ficha de voz, *herido*) y deja ver que sospecha quién pagó. No se repite el cansancio del 23 |
| Hilo A | Coda, entre "—Yo tampoco lo sé." y "Ella no dijo nada más." | 9 | "—¿Y el Canal Seco?" / "—Nada que no se arregle." (Kal dice "se arregla" cuando no está arreglado: ficha de voz) |
| **Total** | | **630** | Prosa del 32: 1,902 (tras E7) → **2,531** |

**Rango del diseño (800–1,000):** quedó en ≈ 630. No se rellenó para alcanzarlo (EDITORIAL_POLICY §J): cada beat del paquete aprobado está en escena y lo demás habría sido textura o glosa. Si el autor quiere más aire, el lugar natural es el trayecto por el Canal Seco (el mercado de día), no el diálogo.

**Qué no hace (§ Irene, punto 9), verificado:** no nombra a Halbrook, Varek, Camp Alder ni "federal"; no explica el temor de Irene; Irene no amenaza a Nadir; el favor no tiene contenido; no aparecen Rafe, los Bravos ni Lucía; Tomás no tiene interioridad; nadie recuerda el 17 en voz alta (el contraste queda en "¿No va a regatear?" / "Hoy no.").

**Metadata del 32 saneada (32:2, 32:4, 32:7, 32:15):** nota de E9 en Estado; Irene, Tomás, Walt y Nadir en el reparto; el Canal Seco en Lugares; la regla "Halbrook no aparece" se amplía con cómo se nombra el carro.

## Registro compartido hecho

- `Auditoria_Editorial_Part_02.md`: bloque **AVANCE DE LA EJECUCIÓN** al inicio y tabla de housekeeping marcada (hecho / en parte / anotado).
- `Evaluacion_Arco_Libro_I.md`: 5-ter con nota APLICADO; 5-quater con Beretta, casi-confesiones y certeza del plan aplicadas, y Nadir (F2) resuelto como Libro II.
- `CURRENT_BRIEF.md` (sección nueva, una entrada), `log.md` (una línea), `INDEX.md` (enlace al mapa).
- Book Map: entrada del 32 y nota de la auditoría de 26–34. Fichas: `Irene_Salcedo.md` y `Nadir_Amrani.md`.

## Abierto para el autor

1. **Danny.** El 17 los puso a cargar a los dos; la escena sólo saca a Nadir ("su muchacho"). ¿Danny sigue cargando, sale con él o se da por terminado fuera de escena?
2. **Líneas nuevas del agente** (todas en el 32): las de Walt, Tomás, Irene y Nadir de la tabla de arriba, y "¿Y el Canal Seco?" / "Nada que no se arregle.".
3. Lo que dejó E8: H6 §5/§7, H7 y `05_Locations/` del lago, `00_Nota_Editorial.md` l. 19, 31:23.
4. El EPUB vigente aún imprime el bloque de diseño de 32:23 y no tiene nada de E5–E9. **No se regeneró.**

## Saldo final de palabras de la Parte II

| | Palabras |
|---|---|
| Prosa de partida 26–34 | 27,003 |
| Poda E5–E8 (neta, ya con Beretta y gesto de la roca) | −1,919 (26–28 −378 · 29–30 −840 · 31–32 −348 · 33–34 −353) |
| Irene e hilo A (E9) | +630 |
| **Prosa final 26–34** | **≈ 25,714** |
| Saldo heredado de la Parte I | +971 |
| **Saldo final (Parte I + Parte II)** | **≈ +2,260** |

Irene se pagó con la poda de la Parte II sola; el saldo de la Parte I queda intacto como margen.

## Autocrítica E9 (MICROEDICION §F)

- **Lo más dudoso:** "Wallah. Qué barato me salió". Hace el trabajo del costo de Nadir en cuatro palabras, pero depende de que el lector lea ironía y sospecha, no alivio. Si se lee como alivio, Nadir pierde la herida y la rima con el 30 se debilita.
- **Lo más agresivo:** "Yo no lo he visto." Es una línea del agente que no estaba en el paquete (el diseño dejaba el tanteo como opcional). Convierte la omisión de Kal en una verdad literal que esconde (Walt, Nadir y Chiara lo vieron, él no). Refuerza el hilo A, pero agrega una mentira por omisión más marcada que el silencio.
- **Pareció necesario y se quitó:** un pensamiento de Kal que recordaba el 17 ("para no deberle nada") y "como si ya lo supiera" en Walt. Los dos explicaban lo que la escena ya muestra.
- **Riesgo de esterilizar:** bajo; es prosa nueva. El riesgo es el contrario: el regateo de las naranjas es textura del agente que puede sobrar si el autor la siente decorativa (≈ 30 palabras).
- **Riesgo de racionalizar interioridad:** bajo. La escena no entra en la cabeza de Kal más que en "Kal esperó el resto."; el temor de Irene no se explica.
- **Prosa más genérica:** Irene habla en cuentas y cuenta con los dedos (ficha); Tomás usa un imperativo seco; Nadir, darija y humor comercial. El riesgo mayor es que Walt sea demasiado neutro, porque sólo dice el recado.

---

# § Balance de palabras de la Parte II (E4)

Palabras de prosa de partida: **27,003** (26–34). Saldo heredado de la Parte I: **≈ +971**.

| Cap. | Antes | Libera (recomendado, sin DUDOSAS) | Añade | Neto | Después (≈) |
|---|---|---|---|---|---|
| 26 | 2,309 | −55 | — | −55 | 2,254 |
| 27 | 2,535 | −95 | (A4: +6 ya descontado) | −95 | 2,440 |
| 28 | 3,020 | −195 | — | −195 | 2,825 |
| 29 | 2,979 | −225 | — | −225 | 2,754 |
| 30 | 4,783 | −610 (con V2, C49a, C54) | — | −610 | 4,173 |
| 31 | 4,136 | −251 (sin C72; −282 con C72) | P2 Beretta +15 a +20 · P3 gesto +8 | ≈ −226 | ≈ 3,910 |
| 32 | 1,992 | −88 | **P1 Irene** +855 a +975 (escena 750–850, cola de Nadir 80–100, hilo A ≈ 25) | ≈ +767 a +887 | ≈ 2,760–2,880 |
| 33 | 3,720 | −313 | — | −313 | 3,407 |
| 34 | 1,529 | −53 | — | −53 | 1,476 |
| **Parte II** | **27,003** | **≈ −1,885** | **≈ +878 a +1,003** | **≈ −882 a −1,007** | **≈ 26,000–26,120** |

- **P4:** 0 (no se añade; D50).
- **Saldo final:** +971 (Parte I) + 1,885 (poda de la Parte II) − 878 a 1,003 (P1–P3) = **≈ +1,850 a +1,980**. Irene se paga dos veces: con el saldo de la Parte I sola, o con la poda de la Parte II sola.
- **Referencia, no meta (§J).** Si el autor veta cortes, el saldo baja palabra por palabra. Irene cabe incluso sin la poda (+971 contra ≈ 975 en el peor caso; si faltaran unas pocas palabras, se ajusta la cola de Nadir).

---

# § Decisiones (borrador) — E1

*No se le preguntan todavía al autor; E4 las consolida con recomendación y vetos libres.* **→ Consolidadas en E4: ver § Decisiones que necesito, al final del mapa.**

- **D1 — Cronología 26–28.** Aplicar A1, A2, A6, A7, A9, A11 y A12 tal como están. Recomendación: sí; son correcciones de desfase, no de diseño.
- **D2 — Mensaje de Walt.** "nueve" → "diez palabras" (A3). Recomendación: sí.
- **D3 — La vuelta del 27 (A4).** (a) "Lo soltaron ya de noche y manejó hasta el amanecer"; (b) conservar "con las últimas luces" y añadir una parada. Recomendación: (a).
- **D4 — Autos.** Kal: ¿Peugeot (Parte I, 28) o Audi (29–31)? Chiara: ¿Lancia (26, 29–30) o Mercedes (ficha, metadata del 28)? Recomendación provisional: Kal **Peugeot** en toda la Parte II (el objeto está cargado desde el 1, el 7 y el 8); Chiara **Lancia** en la prosa y corregir la ficha. Se cierra en E2 con la búsqueda en 30–31 y 35–44. **→ Cerrada en E2: D15.**
- **D5 — Repetición del borrador *no es Varek* (C6).** (a) comprimir 27:62 y dejar la decisión en 146–150; (b) al revés. Recomendación: (a).
- **D6 — El coche de las fotos (A13).** ¿"Un coche de los Bravos" o se deja ambiguo? Recomendación: aclarar.
- **D7 — La escalada del hospital en 28:222 (B2).** (a) cortar por POV; (b) conservar como voz de autor. Recomendación: (a).
- **D8 — Saltos de POV y prolepsis de 28 (B1, B3, B4).** Aplicar. Recomendación: sí.
- **D9 — Halbrook, 27:130.** "No les pedí que fueran innecesarios… **Le** pedí que **quede** claro". ¿Error ("Les pedí que quedara claro") o rasgo de habla? Recomendación: corregir; Halbrook no se equivoca en la concordancia.
- **D10 — Glosas de 26 (C1, C2, C4, C5).** Aplicar. C3 conservar. Recomendación: sí.
- **D11 — Glosas y repeticiones de 28 (C10, C11, C12, C14, C15, C16, C17).** Aplicar. C9, C13, C18, C19 conservar. Recomendación: sí.
- **D12 — 27: C7 y B5.** Aplicar ambas; C8 conservar. Recomendación: sí.
- **D13 — Preguntas con punto (C20).** ¿Se quedan las 16 del 28? Recomendación: sí, como firma; el autor confirma.
- **D14 — A5 (Kal "intuía por cómo había amanecido ella").** "por cómo había subido ella esa madrugada". Recomendación: sí. Requiere que el autor confirme que Kal estaba con ella cuando volvió del ascensor (27:30 lo sugiere).

## Decisiones (borrador) — E2

*Igual que las de E1: no se le preguntan todavía al autor; E4 las consolida.*

- **D15 — Autos (cierra D4).** Kal: Peugeot en 28–30 (A15: "Audi" → "Peugeot" en 29:279 y 30:43); Audi desde el 31 (segundo auto, Cap. 9). Chiara: Lancia en la prosa; el Mercedes es el coche corporativo; se corrigen la metadata del 28 y la ficha. Recomendación: sí.
- **D16 — Plan contra Varek.** V1 (reformula: "que nos necesite más de lo que nosotros lo necesitamos a él"), **V2 (sólo cortar: queda "Después dejamos de necesitarlo")** o V3 (duda de Chiara: "Si nos deja."). Recomendación: **V2**. Es la corrección estructural principal del encargo.
- **D17 — Poda del 30 por movimiento.** Aplicar B8–B14, C37, C39, C40, C44, C45, C46, C47, C48, C51, C54, C55, C57, C58, C59 y C60 tal como están en §1. Recomendación: sí. Ningún inviolable se toca.
- **D18 — El sedán en el taller (A24).** "¿Qué sedán?" → "¿Lo volvieron a ver?" y Héctor: "Walt no fue el único… No lo dijimos porque…". Recomendación: sí (Kal ya lo sabía por Walt en el 27).
- **D19 — "el mismo armamento largo que Halbrook mueve para pagar favores" (A25).** Cortar la aposición: contradice la mecánica de H19. Recomendación: sí.
- **D20 — "Te trataron mal" (A19).** Conservar el tú (condescendencia al herido; rima con "Tu Chiara") o "Lo trataron mal". Recomendación: conservar.
- **D21 — La prueba de sincronía del 29 (C33).** (a) "No llegó. Kal sintió la tentación de mirarla el tiempo suficiente como para que significara algo, y la apagó."; (b) cortar todo tras "No llegó.". Recomendación: (a), porque conserva la tentación desde el único POV que puede contarla.
- **D22 — Mesa de Vivian en el 29 (C28, C29, C30).** C28 y C29 aplicar; C30: (a) "Kal no supo de dónde sabía su nombre." o (b) conservar la lista. Recomendación: C28 y C29 sí; C30 (a).
- **D23 — Continuidades chicas del 29 (A16, A18, C21, C23, C24, C27).** Aplicar. Recomendación: sí. C22, C25, C26, C31, C32 se conservan.
- **D24 — P2, Beretta.** El 30 es viable en 209 (el sobre sale del bolso de al lado de la Beretta .25), pero la recomendación provisional es **el 31** (cambio de bolso en el vestidor, sin contexto de amenaza). E3 decide entre los dos.
- **D25 — P4, Nadir.** El 30 no lo cubre; no se añade en el 30. Se evalúa en E3 si la salida de la mercancía del 32 la elige y la paga Nadir. Recomendación: no tocar el 30.
- **D26 — Fotografías (C49).** (a) cortar la enumeración y conservar "Ninguno de los dos había visto la fotografía completa hasta que la vieron juntos."; (b) cortar el párrafo. Recomendación: (a).
- **D27 — Tics de 29–30 (C40, C45, C59, C23).** Aplicar los cortes listados y conservar la primera o mejor aparición de cada familia (29:273 "asentarse"; 28:218, 29:189, 30:111 "guardaba"; 30:185, 409, 459 "adornar/suavizar"; 29:85 "un grado"). Recomendación: sí.

## Decisiones (borrador) — E3

*Igual que las anteriores: no se le preguntan todavía al autor; E4 las consolida.*

- **D28 — POV del 31 (B19–B22).** Aplicar las cuatro: B19 pasa el contraste a la cabeza de Chiara, B20 y B21 cortan y B22 vuelve observable el costado. Recomendación: sí.
- **D29 — Glosas del 31 (C65, C68–C71, C75).** Aplicar. C66, C77 y C78 se conservan; C76 queda en duda y se conserva. Recomendación: sí.
- **D30 — Resumen del coche (C67).** Queda Danny y Camp Alder; Nadir se comprime; Walt, Héctor y la justificación de la pesca se van. Recomendación: sí. Alternativa: cortar también a Danny (queda sólo Nadir y "Idea de Nadir").
- **D31 — Competencia y cierre de la roca (C72, C73, C74).** C72 comprimir (en duda); C73 cortar sólo "Resolverla la hubiera matado."; C74 (a), cortar el párrafo tras el beso. Recomendación: C74 sí; C72 y C73, a criterio del autor.
- **D32 — Línea canon de la llamada (A28).** ¿La prosa ("Ponte algo cómodo para ir a pescar… Porque quizá te vayas a mojar") o la metadata ("Ponte algo cómodo, porque quizá te vayas a mojar")? Recomendación: conservar la prosa, porque sostiene "¿A pescar?", y corregir la metadata.
- **D33 — Continuidades del 31 (A26, A27).** A26: fuera "con la que la habían mirado los demás". A27: "medio metro de sillón". Recomendación: sí.
- **D34 — P2, Beretta (cierra D24).** **31:83**, cambio de bolso en el vestidor (teléfono, llaves, la Beretta .25), sin que Kal la vea o sin comentario. La alternativa es 30:209. Recomendación: el 31.
- **D35 — P3, casi-confesión del lago.** Un gesto de Chiara antes de "Gracias por traerme" (toma aire para decir algo y lo suelta), sin diálogo nuevo; se quita "al rato". ≈ +8. Alternativa: nada. Recomendación: el gesto.
- **D36 — P4, Nadir (cierra D25).** El 32 no lo cubre con el hilo A intacto. Queda para la Parte III, y E4 lo comprueba. Recomendación: no añadir nada en 30–32.
- **D37 — Correcciones del 32 (A29, A30, A31).** "coche gris"; "Días después" y "dos semanas después"; "las llaves en el cuenco". Recomendación: sí.
- **D38 — Prolepsis y POV del 32 (B23, B24).** Cortar las dos. Sobre "todavía" (32:215): conservarlo (lo aprobó el autor) o quitarlo. Recomendación: B23 y B24 sí; "todavía", preguntar.
- **D39 — Glosas del 32 (C80, C82, C83, C84).** Aplicar. C79 y C81 se conservan. Recomendación: sí.
- **D40 — Bloque de diseño de 32:23 (A33).** Meterlo dentro del comentario en E7 y anotar que el EPUB vigente lo lleva impreso (sin regenerar). Recomendación: sí.
- **D41 — Irene: inserción y reparto.** Después de 32:131, escena propia en POV de Kal, en el Canal Seco. Irene en persona; Tomás cachea y cuenta el sedán; la cita llega por Walt; Kal va solo. Recomendación: sí.
- **D42 — Irene: cierre.** (a) "Ahora sí me debe, señor Mercer." y la anotación en la libreta; (b) sólo la libreta; (c) "Me debe lo que yo diga que me debe." Recomendación: **(a)**. (c) se descarta porque suena a amenaza.
- **D43 — Irene: Nadir se entera.** Cola breve: "Porque ya alcanzó.", sin la imagen del cansancio del 23. Alternativa: fuera de escena. Recomendación: la cola.
- **D44 — Irene: hilo A de Chiara.** Una pregunta en la coda ("¿Y el Canal Seco?") y una respuesta más chica de Kal. ≈ +25. Recomendación: sí.
- **D45 — Metadata de 31–32.** Aplicar la tabla de § Metadata de 31–32 en E7 (salvo 32:4 y 32:15, que van en E9). Recomendación: sí.

---

## Autocrítica E3 (MICROEDICION §F)

- **Lo más dudoso:** C72 (Héctor en estilo indirecto) y C74 (el párrafo tras el beso). Los dos tienen cadencia; C74 se apoya en que la metadata del autor pedía el beso "sin glosa" y en que "casa" debe quedar como última nota antes del coche.
- **Lo más agresivo:** C67. El dictamen pedía reducir el resumen; el pasaje ya es corto, y la propuesta conserva a Danny y Camp Alder por una razón de arco (Kal con la baraja entera), no por economía.
- **Pareció corte y quedó protegido:** la tienda de pesca (el dictamen la marca, pero es voz y ya es mínima); el juego acuático ("Nadie perdió" rima con la roca); 32:129 (siembra del canal directo que 185 cobra); 32:53 (el cálculo de Kal es el tema del capítulo).
- **Riesgo de esterilizar:** bajo en el 32, donde se quitan cuatro frases de narrador. Moderado en el 31: se quitan varias glosas de tono cálido, pero todas repetían lo que el gesto ya daba o copiaban la metadata.
- **Racionalizar interioridad:** B19 hace lo contrario: convierte una percepción imposible de Kal en pensamiento de Chiara. B22 cambia interioridad ajena por sensación propia del POV.
- **Prosa más genérica:** las líneas nuevas posibles (B19, B22, P2, P3 y todo P1) son diseño, no redacción; P1 se escribe en E9 y queda BORRADOR hasta que lo lea el autor.

## Decisiones (borrador) — E4

- **D46 — Palomitas en Il Gelsomino (A38).** (a) "Los vi a la salida del cine."; (b) un postre en Il Gelsomino; (c) conservar. Recomendación: (a).
- **D47 — Compactar el narrador de Kenji/Marisol en el 33 (C95, con C87, C88, C90 y C94).** El diálogo de los dos queda entero. Recomendación: sí.
- **D48 — La glosa antes de "La suficiente para preocuparme" (C101).** Recomendación: cortarla, porque el 34 dramatiza lo que dice.
- **D49 — "No era una acusación. Era casi ternura disfrazada de cifra." (C107).** Recomendación: conservar.
- **D50 — P4, Nadir.** El 43 lo roza con un acto frustrado. Recomendación: no añadir nada en el Libro I; queda para el Libro II (F2).
- **D51 — El resto del 33 y el 34 (A36, B25, B26, C91–C94, C97–C99, C102, C106, C108).** Recomendación: aplicar.
- **D52 — Metadata de 33–34 (§5, puntos 1, 2 y 4) y 26:17.** Se sanea en E8 (y en E5 la del 26). Recomendación: sí.

## Autocrítica E4 (MICROEDICION §F)

- **Lo más dudoso:** C101. La frase es la tesis del 34 dicha por adelantado. Cortarla apuesta a que el lector la recibe en el 34. Si el autor la siente como puente, se conserva sin costo para nadie.
- **Lo más agresivo:** C95 (−96). Quita tres oraciones seguidas de la voz de Chiara. Se apoya en que todas repiten algo dicho antes (45, 137) y en que "Pero ya no quería irse." hace el trabajo sola.
- **Pareció corte y quedó protegido:** 33:199 (el dictamen no quiere glosas de cambio, pero es la única entrada a la función del capítulo); 33:125 (parece miniromance y es la definición del error de Kenji); 34:42 (el eco de 29:107 es el método que Marisol derrota).
- **Riesgo de esterilizar:** moderado en el 33 y bajo en el 34. Se conservan las dudosas de voz (C89, C103, C104, C107, C109).
- **Racionalizar interioridad:** ninguna propuesta convierte percepción en explicación. C90 hace lo contrario: quita el "evidentemente" que volvía dato una lectura de Chiara.
- **Prosa más genérica:** la única línea nueva posible es A38 (a), de cinco palabras, en un pasaje de DISEÑO del agente.

---

# § Decisiones que necesito (E4, 2026-09-27)

Consolida D1–D52. **Veto libre:** lo que el autor no objete se aplica tal como está en la columna "Si no dices nada", en la SURGERY indicada. Para el detalle de cada una, ver los borradores E1–E4 y §1 de cada parte.

## Preguntas abiertas (necesitan elección)

| # | Decisión | Opciones | Recomendación | Etapa |
|---|---|---|---|---|
| **Q1** | Plan contra Varek en el 30 (D16) | V1 reformula ("que nos necesite más…") · **V2 sólo cortar ("Después dejamos de necesitarlo.")** · V3 duda de Chiara ("Si nos deja.") | **V2** | E6 |
| **Q2** | Beretta .25, primera aparición (D24, D34) | **31:83, cambio de bolso en el vestidor** · 30:209, el sobre sale del bolso junto a la pistola | **31** | E7 |
| **Q3** | Irene en el 32 (D41–D44) | **Paquete recomendado:** tras 32:131, Irene en persona en el Canal Seco, Tomás cachea y cuenta el sedán, cierre "Ahora sí me debe, señor Mercer." y la libreta, cola de Nadir "Porque ya alcanzó.", hilo A "¿Y el Canal Seco?" · variante con cierre (b), sólo la libreta · variante mínima sin cola ni hilo A | **Paquete recomendado** | E9 |
| **Q4** | Todo lo demás (abajo) | Aplicar como veto libre · excepciones | **Aplicar** | E5–E8 |

## Vetos libres (se aplican si no dices nada)

| Tema | Decisiones | Si no dices nada |
|---|---|---|
| Cronología 26–31 | D1, D3, D14 | Aplicar la tabla de § Cronología; la vuelta del 27, "Lo soltaron ya de noche y manejó hasta el amanecer" (D3a); "por cómo había subido ella esa madrugada" (D14) |
| Mecánica chica | D2, D6, D9, D19, D33, D37, D46 | "diez palabras"; el coche de las fotos es "de los Bravos"; Halbrook "Les pedí que quedara claro"; fuera la aposición del armamento largo; A26–A27; A29–A31; "a la salida del cine" |
| Autos | D15 | Kal en el Peugeot en 28–30 y en el Audi desde el 31; Chiara en el Lancia; el Mercedes es el coche corporativo |
| POV y prolepsis | D7, D8, D28, D38, B25, B26 | Aplicar todos; en el 32 se conserva "todavía" (215) |
| Glosas y tics 26–28 | D5, D10, D11, D12, D13 | Aplicar C6a, C1–C2, C4–C5, C7, C10–C12, C14–C17 y B5; conservar C3, C8, C9, C13, C18–C20 (las 16 preguntas con punto del 28 se quedan como firma) |
| Poda del 29 y el 30 | D17, D18, D20–D23, D26, D27 | Aplicar la lista de D17, el sedán (A24), C33a, C28, C29, C30a, D23, C49a y los tics; se conserva el "Te trataron mal" |
| El 31 y el 32 | D29–D32, D35, D39, D40, D45 | Glosas del 31; resumen del coche con Danny (C67); C73 y C74 sí, C72 se conserva; la línea de la llamada según la prosa; **P3, el gesto en la roca (+8)**; glosas del 32; el bloque de 32:23 dentro del comentario; metadata |
| El 33 y el 34 | D47, D48, D49, D51, D52 | Compactar el narrador de Kenji/Marisol; cortar C101; conservar C107; el resto de §1; metadata en E8 |
| P4 | D25, D36, D50 | No se añade nada en el Libro I; queda para el Libro II |

## Respuestas del autor (2026-09-27)

- **Q1 — Plan contra Varek:** **V2, sólo cortar.** Se aplica en E6 junto con C54 y B12; la metadata 30:24 se reescribe como "pacto: entrar, hacerse necesarios, dejar de depender; sin plan de caída (Libro III)".
- **Q2 — Beretta .25:** **31:83, cambio de bolso en el vestidor.** E7. 30:209 queda descartado.
- **Q3 — Irene:** **paquete completo.** Tras 32:131: Irene en persona en el Canal Seco, Tomás cachea y cuenta el sedán, la cita llega por Walt y Kal va solo; cierre "Ahora sí me debe, señor Mercer." con la libreta, sin réplica; cola de Nadir "Porque ya alcanzó."; hilo A "¿Y el Canal Seco?" en la coda. E7 marca el punto; E9 escribe.
- **Q4 — Resto:** **aplicar todo como veto libre**, tal como está en la tabla de arriba, incluidos P3 (el gesto en la roca), D46 (a) ("a la salida del cine"), D47–D49 y D50 (P4 para el Libro II).
- **Mandan estas respuestas.** Si el autor cambia una decisión entre etapas, se anota aquí con fecha y manda la más reciente.
