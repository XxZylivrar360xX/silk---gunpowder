# AUDIT — Parte I, lote B — Caps. 8 y 18–24

**Encargo:** [[98_Agent_Handoff/encargos/ENCARGO_Auditoria_Parte_I_Lote_B]] (terminal B, por etapas). **Modo:** AUDIT en E1–E2 (no toca prosa); SURGERY en E3–E4; redacción de la escena de la moto (S1) en E5.
**Política:** [[12_Craft_Policies/editorial/EDITORIAL_POLICY]] (§L prolepsis, §J sin cuotas), [[12_Craft_Policies/editorial/DO_NOT_TOUCH]], [[12_Craft_Policies/editorial/MICROEDICION]]. Prioridad C: protección y microedición.
**Dictamen de origen:** [[13_Auditorias/Book_01_Mascaras_De_Cristal/Auditoria_Editorial_Part_01]] (matriz y adenda B, resumidas en el encargo).
**No se tocan aquí:** los Caps. 4, 6, 7, 11 y 13 (terminal A), el EPUB, Natalie Keegan en el 3, el recuerdo de Palermo del 12 ni las flores de la carta del 16.

## Estado de etapas

| Etapa | Alcance | Estado | Fecha | Nota |
|---|---|---|---|---|
| E1 | AUDIT 8, 18, 19, 20 | **HECHA** | 2026-09-27 | §1–§5 y § Decisiones (borrador) sólo para estos cuatro |
| E2 | AUDIT 21–24, consolidación y preguntas al autor | **HECHA** | 2026-09-27 | §0–§5 de 21–24, S1/S2/S5/S6, balance; decisiones D1–D18 respondidas por el autor ("todo según recomendación") |
| E3 | SURGERY 8, 18, 19, 20 | **HECHA** | 2026-09-27 | §9 Resultado (parte 1). Poda −257, S3 +42, neto −215. S4 protegida sin añadir; S1 no cae aquí (va en el 23) |
| E4 | SURGERY 21–24 | **HECHA** | 2026-09-27 | §9 Resultado (parte 2). Poda −93, mecánica +4, S5+S6 +29, neto −60. Punto de inserción de la moto marcado en el 23 (entre 183 y el *** de 185) para E5 |
| E5 | Escena de la moto y registro final | **HECHA** | 2026-09-27 | §9 Resultado (parte 3). Moto en el 23 (+438, con S2 dentro), BORRADOR/DISEÑO. Registro compartido hecho. Saldo para el 32: ≈ +970 |

**Estado de los capítulos auditados en E1 (para el `git diff --stat` de E3):** los cuatro sin cambios en el árbol de trabajo al 2026-09-27; último commit `a8b7be0`. Palabras de prosa (sin metadata, `wc -w`, con encabezado): 8 = 2,699 · 18 = 3,187 · 19 = 1,650 · 20 = 2,277. La matriz del encargo da cifras un poco menores (2,675 / 3,166 / 1,639 / 2,260) porque cuenta distinto; para el antes/después de E3 se usa `wc -w`.

**Estado de los capítulos auditados en E2 (para el `git diff --stat` de E4):** 21–24 sin cambios en el árbol de trabajo al 2026-09-27; último commit `a8b7be0`. Palabras (`wc -w`, mismo criterio): 21 = 1,824 · 22 = 904 · 23 = 1,788 · 24 = 2,251.

---

# Parte 1 — Caps. 8, 18, 19 y 20 (E1)

## 0. Diagnóstico corto

- **8 (LIGERA).** Funciona. Hay dos problemas de continuidad (el "semanas atrás" y el amanecer a las dos de la mañana), una prolepsis chica (la Colombina, que el autor dejó disponible para reaparecer), un salto de POV hacia Kal en el "Mandorla" y dos glosas que repiten el centro del capítulo ("el reverso", "el camaleón perfecto"). **"Camaleón" es palabra de Kal, dicha una vez y sólo a ella** (ficha de Kal; `Kal_y_Chiara` §366): que el narrador de Chiara la gaste aquí le resta fuerza a esa detonación. Es el mejor lugar para **S3** (Camp Alder).
- **18 (MÍNIMA).** Es el centro temático y se protege. Cortes de tic ("la clase de" aparece 9 veces; "con la misma … con la que") y una certificación. El problema real está en el **cierre**: la frase de "al día siguiente" es PROLEPSIS (§L es posterior a la aprobación del capítulo) y el último párrafo **contradice** el regreso en auto ("con la nube todavía sin romperse", 273, contra "de camino a casa, la nube por fin se abrió y salió el sol", 323). Además es de noche.
- **19 (LIGERA).** Útil y se conserva entero como capítulo. Sobra la explicación de cómo se llevan Kal y Claudio (50). Hay un tic de "la misma" y otro de "de verdad", y un salto de POV de autor en la videollamada (Chiara antes de contestar) que recomiendo conservar como contracorte. Es el único de los cuatro que podría alojar **S1**.
- **20 (MÍNIMA).** Se protege casi entero. El drift y el mirador el autor los declaró perfectos, y quedan intocables aunque tengan rarezas (110). Sólo hay una repetición de "la distancia que había cuidado durante meses" (178 contra 202) y una generalización opcional en 218. **S4 ya existe** en el penthouse ("la verdad de lo pequeño", 180–188).

**Palabras que libera E1, según las recomendaciones:** 8 = −78 · 18 = −112 · 19 = −55 · 20 = −5. **Total: −250.** Con las opciones marcadas como veto libre la cifra baja a unas −200; con la opcional del 20 sube a −274. S3 cuesta unas +45 y S4, 0.

## 1. Candidatos por categoría

### A. Continuidad y mecánica (prioridad 1)

| # | Cap:línea | Texto | Problema | Propuesta | Palabras |
|---|---|---|---|---|---|
| A1 | 8:57 | "Lo había armado sola **semanas atrás**, en el asiento trasero de un taxi, con un ladrillo…" | La noche del ladrillo es del Cap. 7, y la metadata del 8 fija "días después del Capítulo 7" | "**días atrás**" | 0 |
| A2 | 8:219 + 221 | "Entró a la ciudad por el sur, **con el cielo empezando a decidirse por un gris muy claro sobre el agua**." / "Pasaban de las dos de la mañana." | A las dos no clarea. La hora está fijada por la cadena Gelsomino (8:30) → tienda → carrera de madrugada | **(a, recomendada)** cortar la cláusula del cielo. **(b)** subir la hora a "Pasaban de las cinco". Toca cronología: **D4** | −14 |
| A3 | 18:321 (2.ª frase) + 323 | "Al día siguiente, cuando alguien preguntó, los dos dijeron que eran buenos amigos…" / "Ese jueves, de camino a casa, la nube por fin se abrió y salió el sol de siempre, tarde y sin ganas…" | 323 **contradice** 273 (el regreso "con la nube todavía sin romperse") y la hora (ya era de noche antes del golf, 65; después se duermen en el penthouse, 319). La 2.ª frase de 321 es PROLEPSIS (ver B1) | **(a, recomendada)** cortar la 2.ª frase de 321 y todo 323. El capítulo cierra en *"Nadie llamó a eso una cita."*, que ya rima con el marco de 21. **(b)** cortar sólo la prolepsis y reformular 323 sin sol. **(c)** conservar. **D5** | −52 |

### B. Prolepsis y saltos de POV (§L y MICROEDICION C)

| # | Cap:línea | Texto | Categoría | Propuesta | Palabras |
|---|---|---|---|---|---|
| B1 | 18:321 | "Al día siguiente, cuando alguien preguntó, los dos dijeron que eran buenos amigos, y lo dijeron sin que se les moviera un músculo." | **PROLEPSIS DE NARRADOR**: confirma un hecho posterior a la escena. Es una coda inocua, pero §L no distingue por gravedad | Va con A3 | (en A3) |
| B2 | 8:219 | "…entre el respaldo y un trapo de taller. **No volvió a acordarse de ella.**" | **PROLEPSIS**: promete que la Colombina no vuelve a la cabeza de Chiara, y la ficha de Chiara (§272) la deja "disponible para reaparecer — decisión del autor" | Cortar la frase | −6 |
| B3 | 8:137 | "…el principio de una sonrisa que no llegó a completarse**, porque acababa de entender de dónde había salido esa palabra**." | **SALTO DE POV**: la sección es de Chiara, que no puede saber qué entendió Kal. La cláusula es, sin embargo, la única señal para el lector de que *Mandorla* significa algo | Convertirlo en una lectura de Chiara: "…que no llegó a completarse**: había entendido de dónde salía esa palabra**." La deducción se apoya en la sonrisa, que ella sí ve | −3 |
| B4 | 18:215 | "No dio nombres, no hizo falta: **lo que Kal necesitaba saber ya lo tenía guardado desde antes sin haberlo pedido**, un rubio de ojos azules…" | **SALTO DE POV**: la interioridad de Kal va metida en la réplica de Chiara, y en 217 vuelve a Chiara | "No dio nombres, no hizo falta: **Kal ya sabía de quién hablaba**, un rubio de ojos azules…". Conserva el dato (Kal sabía de Blake) como saber compartido | −8 |
| — | 18:111 | "Kal la miró de reojo, un segundo, calculando si eso era una trampa o una invitación, y decidiendo que probablemente era las dos cosas." | Posible SALTO a Kal | **CONSERVAR (DUDOSA).** El 18 alterna la focalización por párrafo a lo largo de todo el capítulo (ver §2). Esta es humor y no revela nada |
| — | 19:108 | "Del otro lado, Chiara vio el nombre en la pantalla y, por un segundo entero, el pánico específico…" | SALTO DE POV (la sección es de Kal y la llamada todavía no conecta) | **CONSERVAR como contracorte.** Es un beat pedido por el autor (metadata: los dos botones) y "Del otro lado" marca el corte espacial. Un `***` a media llamada rompe más de lo que arregla. **D7** |
| — | 8:231 | "…iba una máscara que Kal vio por el espejo, no recogió y no salió a devolverle." | Chiara ya se bajó: la percepción es de Kal | **CONSERVAR.** Es el beat canon del objeto (metadata; Hitos H9), contado desde fuera (el espejo, lo que no hace) y no desde la cabeza de Kal |
| — | 20:154 | "Chiara lo guardó… como algo que un día, si la vida se lo permitía, iba a devolverle en otra forma." | ¿Prolepsis? | **CONSERVAR.** Es intención de Chiara, que §L permite, y está en el mirador, que es intocable |
| — | 19:98 | "…las manos nuevas que el Patio iba a necesitar…" | ¿Prolepsis? | **CONSERVAR.** Es expectativa de Kal, no un anuncio del narrador |

### C. Glosa, tic, repetición y certificación

| # | Cap:línea | Texto | Categoría | Propuesta | Palabras |
|---|---|---|---|---|---|
| C1 | 8:15 | "Esa semana, sin embargo, había estado llegando con el día ya archivado. Ordenado de antemano. Recortado." | REPETICIÓN FUNCIONAL con 21 ("Antes le dejaba siempre un hilo suelto… Esta semana traía todo con el dobladillo cosido"), que es más concreto y más relacional (el hilo es para que *él* tire). El diálogo de 17 ya lo demuestra | Cortar el párrafo 15. Sin costura: 13 cierra en "antes de hablar." y 17 abre el diálogo | −16 |
| C2 | 8:115 | "Era el reverso de la primera reunión en el Monarch — sólo que esta vez la que estaba parada en un cuarto que no era suyo era ella." | GLOSA + REPETICIÓN FUNCIONAL: 113 ya compara con "una junta del Monarch", y 163 formula la inversión en la escena donde ocurre | Cortar. **DUDOSA:** veto libre (es un eco del Cap. 2) | −28 |
| C3 | 8:125 | "…para poder gritarlo en una recta sin que sirviera de nada después en una comisaría. **El camaleón perfecto: cambiaba de color sin cambiar una sola letra.**" | Ornamento tras la explicación, y **gasta una palabra canon**: "camaleón" es de Kal, una sola vez y sólo delante de ella. No aparece en ningún otro lugar de la prosa del Libro I | Cortar. **D3** | −11 |
| C4 | 18:97 | "…alguien se salía con la suya delante de ella. **Una vez más, Kal Mercer lo había conseguido.**" | COMPETENCIA EXPLICADA: la mueca y "se salía con la suya" ya lo dicen | Cortar | −8 |
| C5 | 18:79 | "…decidió seguirle la corriente**, con la misma naturalidad con la que aceptaba todo lo que él improvisaba**." | TIC ("con la misma … con la que", 5 veces en el 18) + INTENSIFICADOR ("todo" choca con la confusión de 77) | Cortar la cola | −13 |
| C6 | 18:87 | "Se sostuvieron la mirada un momento de más**, con esa clase de tensión que no pedía nada en voz alta pero tampoco se molestaba en esconderse del todo**." | GLOSA + TIC ("la clase de", 9 veces; "molestarse en", 3 veces en 61–145) | Cortar la cola. **DUDOSA:** veto libre | −20 |
| C7 | 18:145 | "…la risa se le escapara, corta y genuina**, la clase que no se molestaba en contener delante de él**." | TIC (los mismos dos) | Cortar la cola | −11 |
| C8 | 19:50 | "Ninguno de los dos le debía al otro una explicación por lo que acababa de pasar en esa puerta **— así funcionaban, y así les había funcionado bien hasta ahora: cada quien en lo suyo, sin pisarse, de acuerdo casi siempre y en desacuerdo alguna vez, sin que ninguna de las dos cosas se convirtiera nunca en problema**." | GLOSA expositiva. La primera cláusula ya dice la relación; el resto es resumen (y "hasta ahora" suena a presagio) | Cortar desde la raya | −36 |
| C9 | 19:108 | "…antes de que lo desechara **con la misma velocidad con la que hacía cualquier otra cosa**." | TIC ("la misma", 4 veces en el 19: 46, 94, 98, 108). 98 es un eco deliberado de 46 y se protege | Cortar la cola | −11 |
| C10 | 19:20 | "…Garrett **llevaba los lentes** como quien lleva una herramienta, no una vanidad." | REPETICIÓN LEXICAL: el párrafo abre con "Garrett llevaba, como siempre, los lentes oscuros puestos" | "…habría tolerado. **Los lentes eran una herramienta, no una vanidad.**" | −4 |
| C11 | 19:134, 142 | "…que reservaba para cuando **de verdad** no sabía…" / "…un terreno donde **de verdad** puede ayudar" | TIC: "de verdad" aparece 5 veces en la última escena (102, 126, 132, 134, 142) | Quitar "de verdad" en esas dos. Se quedan en 126 y 132, que miden algo | −4 |
| C12 | 20:178 | "…sin la distancia de cortesía **que había cuidado durante meses**." | REPETICIÓN LEXICAL con 202 ("La distancia que habían cuidado durante meses se fue cerrando sola"), que es la que fija la metadata | Cortar la relativa. La de 202 queda sola | −5 |
| C13 | 20:218 | "…sin que hiciera falta preguntar hacia dónde**, y en el trayecto corto hasta la habitación no hubo ni un segundo de la clase de duda que suele acompañar a estas cosas**." | INTENSIFICADOR / generalización del narrador | **Opcional, recomiendo conservar:** el autor revisó esta línea el 2026-09-10 y la dejó. **D8** | (−24) |
| — | 18:77 | "No hacía falta: era exactamente la clase de cosa que hacía cuando quería sacarla de donde ella se sentía cómoda…" | ¿GLOSA? | **CONSERVAR (INTERIORIDAD).** Chiara reconoce el patrón de H9 (Cap. 8); es una rima entre capítulos |
| — | 18:191 | "Ninguno de los dos le puso nombre a la indirecta que acababan de lanzarse sin querer." | ¿GLOSA? | **CONSERVAR (DUDOSA).** Es la única señal de que "siete años" es una indirecta; sin ella el chiste se pierde |
| — | 18:273 / 315 | "…el de la hierba y las canciones y las habitaciones separadas…" / "…a la noche de la hierba, al choque de puños y a las habitaciones separadas." | REPETICIÓN LEXICAL de dos callbacks, a 40 líneas | **CONSERVAR (DUDOSA).** Los tres pagos son reales (hierba y habitaciones del 6, puños del 7); 315 marca el hito del hombro. Si el autor quiere podar, se toca 273, no 315 |
| — | 8:21 / 125 | "un segundo tarde" dos veces | REPETICIÓN LEXICAL | **CONSERVAR.** 125 está fijado por la metadata, y en 21 es el mismo síntoma: Chiara pierde el control desde el principio de la noche |
| — | 8:163 | "Éste era uno de los cuartos donde él leía la sala antes que ella." | ¿GLOSA de 161? | **CONSERVAR.** Es el descubrimiento del POV que la metadata pone como centro. Con C2 cortado, es la única formulación |
| — | 19:126 / 134 | "…para que él supiera que la había sorprendido de verdad" / "Nunca paras de sorprenderme." | REPETICIÓN FUNCIONAL | **CONSERVAR.** Narración y réplica; la réplica es la de ella |

## 2. Prolepsis y POV — lectura por capítulo

- **8:** POV de Chiara, sostenido. Hay un salto (B3) y una percepción externa de Kal en el cierre (8:231, se protege). Prolepsis: B2. "Trabajo temprano —dijo Kal, que era verdad" (223) es certificación del narrador, pero es humor y se conserva.
- **18:** focalización **alterna por párrafo** en todo el capítulo: Kal en 15–21, 207, 259, 299–301; Chiara en 61, 77, 185, 217, 263, 297. En el nudo de H4 (259 Kal lo sabe → 263 Chiara ve que lo sabe → 297/299 cada uno en su cabeza) la alternancia **es la escena** y está aprobada: se protege. Sólo se corrige un salto dentro de una misma réplica (B4). 111 se conserva. Prolepsis: B1.
- **19:** POV de Kal, con un contracorte a Chiara en la videollamada (19:108, se conserva). El flashback del parque es memoria del POV y está permitido.
- **20:** Kal en la apertura y la bolera; Chiara en el espejo (196) y en 210; Kal en 206. Es el mismo patrón dual del 18 en escenas íntimas, y el autor ya lo aprobó (CLOSE 2026-09-12). Sin prolepsis.

## 3. Función por movimiento

Palabras con `wc -w` por rango de líneas.

**Cap. 8 (2,699)**

| Líneas | Movimiento | Palabras | Función | Veredicto |
|---|---|---|---|---|
| 11–43 | Terraza del Gelsomino: el día recortado, la navaja, "lo más ilegal", "ponte algo cómodo" | 391 | Residuo del 7 (retroceso), dos líneas canon | C1 |
| 47–75 | El Peugeot, "¿Esto es el algún día…?" | 267 | Ella se sube voluntariamente; Kal no la engaña | A1 |
| 79–103 | La Tramoya: máscaras | 376 | Las máscaras fijadas como carácter | Intacto |
| 107–145 | Kingsley Field, Tyler, Mac y Mandorla | 688 | Chiara no sabe leer la sala; los apodos | **S3** aquí; C2, C3, B3 |
| 149–173 | La carrera y la risa | 406 | Centro del capítulo, no se explica | Protegido |
| 177–185 | Patrullas, la radio que ficha el coche | 220 | Riesgo; el coche y no las personas | Protegido |
| 189–215 | Grava, sin máscaras, "¿Ganamos?" | 137 | Conversación mínima canon | Protegido |
| 219–233 | Regreso, la Colombina olvidada | 199 | Objeto; cierre sin beso | A2, B2 |

**Cap. 18 (3,187)**

| Líneas | Movimiento | Palabras | Función | Veredicto |
|---|---|---|---|---|
| 15–21 | La frase de Héctor, "somos sólo buenos amigos" | 111 | Residuo del 16 y el marco | Protegido |
| 25–47 | El chiste del porcentaje | 176 | Siembra del "porcentaje" que paga el 19 | Protegido |
| 51–99 | Día nublado, Gelsomino, Enzo, la cuenta | 714 | Expansión del autor (09-07) | C4, C5, C6 |
| 103–113 | Auto: reglas de vestimenta | 121 | Juego de reglas de Chiara | 111 conservado |
| 117–147 | Boutique: boina, falda | 230 | Coqueteo; el espejo al que 20:196 hace eco | C7 |
| 151–167 | Entradas y palos | 210 | "Préstamo temporal" cumplido | Intacto |
| 171–243 | Golf y preguntas | 629 | Escalada hasta la pregunta pivote | B4 |
| 247–267 | El exmarido; Kal deduce | 263 | **H4, núcleo** | Protegido |
| 271–277 | Regreso en silencio | 143 | Peso | Protegido (fija la nube que contradice 323) |
| 281–307 | Motor encendido, "Se quedó" | 367 | **H4, decisión** | Protegido |
| 311–323 | Penthouse: hombro, mano, dormirse; coda | 206 | Cierre | A3/B1 |

**Cap. 19 (1,650)**

| Líneas | Movimiento | Palabras | Función | Veredicto |
|---|---|---|---|---|
| 12–32 | Notaría con Garrett | 349 | Primera aparición de Garrett | C10 |
| 36–56 | Gelsomino: Claudio y Harper | 291 | Harper sin trabajo | C8 |
| 60–78 | La parcela, la oferta | 226 | Reclutamiento: confianza y no caridad | Protegido |
| 82–90 | Flashback del parque | 194 | Origen del instinto de Kal en Chiara | Protegido |
| 94–98 | Trato hecho | 84 | "Manos nuevas del Patio" | Protegido (candidato de inserción para S1, §4) |
| 102–156 | Videollamada: tomates, Rivers, "Ciao, tesoro" | 495 | Hilo legal; la única entrega de Rivers | C9, C11 |

**Cap. 20 (2,277)**

| Líneas | Movimiento | Palabras | Función | Veredicto |
|---|---|---|---|---|
| 16–36 | Residuo del 18, "Estás en otro lado", bolos | 250 | Kal calla lo que dedujo (hilo A en conducta) | Protegido |
| 40–92 | Bolera | 491 | Juego; ya podado el 09-10 | Intacto |
| 94–124 | Drift | 250 | **Intocable** (el autor lo declaró perfecto) | — |
| 128–166 | Mirador: Dale y Ruth | 387 | **Intocable**, corazón | — |
| 170–192 | Elevador, penthouse, vino, "la verdad de lo pequeño" | 438 | S4 ya presente | C12 |
| 194–216 | Baile, beso, "¿Seguro?" | 307 | Canon | Protegido |
| 218–224 | Habitación, la luz | 145 | Cierre canon | C13 opcional |

## 4. Protegido y siembras

### Protegido (ya aplicado o cobrado por otros)

- **19:156** "Ciao, tesoro" (adenda A). **18:63** la silla verde que critica Héctor (paga el 16). **19:142** Margaret Rivers, la única entrega. **18:37–47 / 19:128** el chiste del porcentaje. **18:197** el Nova del 78 ("Ésa no era la pregunta"): sólo aparece aquí, es voz y objeto disponible. **18:235** "No es una historia" (hilo B, paga en el 25). **18:15–17** la frase de Héctor. **18:299–301** "Se quedó" (canon H4). **8:145** "florero" (callback al 7, rima silenciosa con Blake). **8:185** la anáfora "No un hombre rubio…" (la metadata fija que se ficha el coche, no las personas). **8:171–173** la risa sin explicación. **20:18** "Kal no lo había vuelto a tocar. Ni una palabra." (hilo A: callar como protección, en conducta). **20:220** el núcleo de la seguridad (decisión del autor, 09-10).

### S3 — Camp Alder como geografía (hilo B)

**Recomiendo el 8.** Cruce: `05_Locations/Camp_Alder` lo sitúa "al noreste de San Aurelio, más allá de Kingsley Field", y el 43 lo describe como "una línea de cercas y luces bajas", con "cerca exterior", garita y reja, llegando "hacia el noreste, más allá de Kingsley Field". El 8 ya está en esa carretera.

- **Por qué el 8:** la geografía ya está en escena (el Peugeot va hacia el norte, a Kingsley). El POV es de Chiara, así que el gesto de Kal (no mirar) es **observable y no necesita glosa**, que es justo lo que pide el hilo B: "sin decir nada". Chiara no sabe qué es y no pregunta; el lector lo reconoce en el 27–29 y en el 43.
- **Contra del 8:** el capítulo usa mucho "reja" (Kingsley, 107–183). Para no confundirlas, la de Camp Alder debe llamarse **cerca** (la palabra del 43) y distinguirse por la luz: blanca, no de sodio.
- **Por qué no el 19:** el POV es de Kal. O el narrador nombra la base y explica por qué la evita (glosa, y adelanta el hilo), o el gesto queda raro dentro de su propia cabeza. Con Garrett o Harper al lado haría falta una línea de diálogo, y S3 pide una sola imagen.
- **Lugar exacto:** 8:109, entre "…la Carretera de Milla estirándose paralela a la reja hasta perderse." y "Cuando Kal salió de la autopista y bajó por una rampa sin señalizar…".
- **Texto propuesto (DISEÑO, unas 45 palabras):** *"Más allá de los hangares, donde la autopista seguía hacia el noreste, corría otra cerca, más alta, con alambre arriba y una luz blanca y pareja que no era la de Kingsley. Un letrero verde: CAMP ALDER. Kal no giró la cabeza."* Chiara no comenta, y la frase siguiente sigue igual.

### S4 — Casi-confesión del 20 (hilo A)

**Ya existe; recomiendo protegerla sin añadir nada.** En 20:180–188 Chiara enuncia su regla ("Nunca miento en lo pequeño") y responde a la verdad grande que Kal acaba de contar en el mirador con **"la verdad de lo pequeño"**. La estructura ya es la de alguien que elige una verdad más chica, y el lector acaba de ver la grande del otro lado. Kal, además, calla en 20:18 lo que dedujo en el 18.
- **Opción, si el autor quiere el silencio visible:** una pausa narrada, sin réplica nueva, antes de *"—Entonces te digo la verdad de lo pequeño."*: *"Se quedó un momento con la copa quieta."* (+8). No toca el mirador. **D2**

### S1 y S2 — la moto de Nadir (sólo candidatos; se decide en E2)

- **18: no recomendado.** El único hueco es el residuo de apertura (15–21, la semana de Kal "al taller"), y meter 600 palabras ahí retrasa H4 y le quita el tono al día nublado.
- **19: candidato viable.** Es un capítulo del Patio, con POV de Kal, cuyo tema es a quién le das tu confianza y cómo se paga ("No necesito caridad"; "manos nuevas que el Patio iba a necesitar", 98). La moto pagada en abonos rima con Harper sin repetirla: Harper es una desconocida a la que se le da confianza; Nadir es de la casa y no pidió permiso. **Inserción posible:** una sección nueva entre 98 y 102 (Kal vuelve al taller esa tarde; la moto frente a la puerta), antes del salto de "Un par de semanas después". Cabe S2 (Nadir cansado de las rutas de la Ronda). **Contra:** el 19 ya carga a Garrett, Harper, el flashback y Rivers; con 600 palabras más pasa de ~1,600 a ~2,200 y suma un cuarto hilo. Y dos escenas de confianza en un capítulo pueden leerse como REPETICIÓN FUNCIONAL.
- **20: descartado** (corazón protegido).
- Falta comparar con 21–24 en E2 (el 21, "familia elegida", parece el rival natural).

## 5. Lo que no es de microedición (se reporta y no se opera)

- **18, la luz del día:** 4 p. m. en el Gelsomino → "el gris más oscuro que en esta ciudad hacía las veces de noche" antes de salir (65) → boutique → al menos once hoyos de golf → regreso. El golf queda jugado de noche, y Chiara vendía el campo "para ver el atardecer" (81). A3 arregla sólo la contradicción explícita del cierre; el resto es cronología interna de un capítulo aprobado y es decisión del autor. **D5**
- **19:60**, "el letrero nuevo **con el nombre del notario** grapado a un poste": no queda claro qué letrero sería. ¿"Vendido"? ¿El nombre del nuevo dueño? Es un dato raro, pero no está roto. **D9**
- **20:108** (sujeto ambiguo de "entendió") y **20:110** ("figurativamente…"): están en el drift, que el autor declaró perfecto. Se reportan y no se tocan.
- La **focalización alterna** del 18 y el 20 es convención de escena íntima ya aprobada, no un defecto de línea (§2).

## § Decisiones (borrador) — E1

*Superado en E2: consolidado en **§ Decisiones que necesito** (al final del mapa), que es la versión que manda. Se conserva como registro.*

1. **D1 — S3:** ¿Camp Alder en el 8 (recomendado), en 8:109 con el texto de §4? ¿O en el 19?
2. **D2 — S4:** ¿se protege tal cual, sin añadir nada (recomendado)? ¿O se agrega la pausa de 8 palabras antes de "la verdad de lo pequeño"?
3. **D3 — "camaleón" en el 8 (C3):** ¿se corta para reservar la palabra a Kal (recomendado)?
4. **D4 — El amanecer a las dos (A2):** ¿se corta la cláusula del cielo (recomendado) o se sube la hora a las cinco?
5. **D5 — El cierre del 18 (A3/B1):** ¿(a) cerrar en "Nadie llamó a eso una cita." (recomendado), (b) cortar sólo la prolepsis y reformular 323 sin sol, o (c) conservar? ¿Y se deja como está la luz del golf (§5)?
6. **D6 — Saltos de POV:** ¿se aprueban B3 (8:137) y B4 (18:215) como lecturas del POV? ¿Se conserva 18:111?
7. **D7 — La videollamada del 19:** ¿se conserva como contracorte (recomendado) o se abre `***`?
8. **D8 — 20:218 (C13):** ¿se conserva (recomendado) o se corta la generalización?
9. **D9 — El letrero del notario (19:60):** ¿se deja o se precisa?
10. **Veto libre (sólo avisar si no):** C2 (8:115, "el reverso") y C6 (18:87, "la clase de tensión").
11. **S1/S2:** el 19 es viable; el 18 y el 20 no. Se decide en E2 contra el 21–24.

---

# Parte 2 — Caps. 21, 22, 23 y 24 (E2)

## 0. Diagnóstico corto

- **21 (LIGERA).** El beat de familia elegida funciona y la estructura por bloques de POV está limpia. Lo que hay es poda de línea: en la apertura se dice tres veces que el cuerpo de Kal va antes que su cabeza (16, 24, 30), hay un "la clase de" y un "No hacía falta." que se repite (110 y 208), y un "con el mismo … con el que" (190). El *housekeeping* es de metadata: dos líneas de `Estado` (2 y 7). No hay prolepsis.
- **22 (MÍNIMA).** Bisagra eficiente. Tiene dos problemas de §L, que es posterior a su aprobación: **"O eso creían los dos esa mañana."** (54), que anuncia que se equivocan, y la cola del auto que "iba a tardar mucho tiempo en volver a existir" (44). La escena de Dario ya cobra la primera sola. El 22 es el único capítulo de la Parte I que usa `---` como separador (84).
- **23 (LIGERA).** El hilo legal es funcional y tiene buen oído (Héctor, Rivers, Garrett). Hay un error de mecánica en la escena de Rivers: revisa la segunda carpeta dos veces (79 y 101) y la cierra dos veces (107 y 147). Aquí caben **S5** y **S6**, y es mi candidato para **S1**.
- **24 (LIGERA–MEDIA).** Tommaso gana peso sin volverse presagio: nadie lo mira como hombre marcado, y el capítulo cierra su enigma en "Tommaso, no." (284). El problema real es el **cierre**: *"La idea, de todos modos, ya no se iba a ir."* (396) es PROLEPSIS, porque el Lancia se compra en el 25. Hay además un recordatorio innecesario de la lista de testigos (178), la lista de la firma repetida (360 → 374) y una atribución ambigua en 300–302.

**Palabras que libera E2 según las recomendaciones:** 21 = −29 · 22 = −28 · 23 = −6 · 24 = −28 (−20 sin C20). Mecánica que suma: +4 (A7, A8). **Neto: −87.** Las siembras del 23 (S5 y S6) suman +30 y van aparte; ver § Balance.

## 1. Candidatos por categoría

### A. Continuidad y mecánica (prioridad 1)

| # | Cap:línea | Texto | Problema | Propuesta | Palabras |
|---|---|---|---|---|---|
| A4 | 23:79 + 101 | "Rivers revisó la primera carpeta. **Después la segunda.**" / "…—Rivers **pasó a la segunda carpeta** sin levantar la vista—." | Revisa la segunda dos veces | 79: "Rivers **abrió** la primera carpeta." Así, 101 pasa a la segunda | −3 |
| A5 | 23:107 + 147 | "—Cerró la carpeta con un dedo—." / "**Cerró la carpeta.**" | La cierra dos veces sin reabrirla (entre una y otra sólo hay una hoja en blanco, la pluma y una nota) | Cortar 147. "¿Y ahora?" sigue directo a la sentencia de Rivers sobre los casos civiles | −3 |
| A6 | 22:84 | `---` | Único separador de este tipo en la Parte I; todos los demás usan `***` | `***`. **Veto libre:** si el guion marca a propósito el cambio al mundo de Dario, se conserva | 0 |
| A7 | 24:256 | "No giró la cabeza **junto a** Kal, ni junto a Chiara." | Falta el verbo del movimiento | "No giró la cabeza **al pasar** junto a Kal, ni junto a Chiara." | +2 |
| A8 | 24:300–302 | "—Lusardi mintió." / "—A favor mío, y sin que yo se lo pidiera. Lo cobro ahora y pregunto por qué después." | Atribución ambigua. Leo que Kal dice la primera y Rivers la segunda ("a favor mío" = de mi caso; ella fue quien le preguntó a Tommaso si alguien se lo había pedido). Pero "lo cobro" también suena a Kal | Etiqueta mínima: "—Lusardi mintió **—dijo Kal.**" **D17** | +2 |
| A9 | 23:165 | "Dinero, no todo **—** suficiente para que…" | Raya espaciada en narración (el resto del lote usa raya pegada o dos puntos) | "Dinero, no todo: suficiente para…" **Veto libre** | 0 |

### B. Prolepsis y saltos de POV (§L y MICROEDICION C)

| # | Cap:línea | Texto | Categoría | Propuesta | Palabras |
|---|---|---|---|---|---|
| B5 | 22:54 | "O eso creían los dos esa mañana." | **PROLEPSIS DE NARRADOR**: le anuncia al lector que el cierre falló antes de que la escena de Dario lo muestre. La metadata de 09-10 la dejó como "certeza limitada a lo que creen", pero §L (09-26) prohíbe justo esa forma | Cortar. La sección cierra en "…no le importaba a nadie a esa hora.", y el salto a Dario y "Como variación." cobran solos | −6 |
| B6 | 22:44 | "Ahí Kal hizo lo que sabía hacer: lo desarmó, lo guardó, **y ese auto en particular iba a tardar mucho tiempo en volver a existir en ningún registro que a alguien le interesara consultar**." | **PROLEPSIS** (menor): confirma un hecho futuro sobre el auto. Tiene humor de voz, así que es DUDOSA | "…lo que sabía hacer: lo desarmó y lo guardó." §L pide cortar, no suavizar. **D15** | −22 |
| B7 | 24:396 | "No llamó ese día. **La idea, de todos modos, ya no se iba a ir.**" | **PROLEPSIS**: confirma lo que paga el 25 (la compra del Lancia) | Cortar la 2.ª frase. El capítulo cierra en "No llamó ese día.", que es un hecho del día y deja la ironía al lector. **D15** | −11 |
| — | 21:30 | "Fue esa velocidad… lo que despertó a Chiara." | ¿SALTO DE POV? (el bloque es de Kal) | **CONSERVAR.** Kal ve que ella despierta; la causa es inferible desde fuera | |
| — | 21:120 | "…y por primera vez en años, Kal se durmió con alguien despierta a su lado sin sentir la necesidad de quedarse alerta él también." | ¿Prolepsis o certificación? | **CONSERVAR (INTERIORIDAD).** Es memoria de Kal sobre su pasado, no un anuncio, y el bloque del mezzanine es suyo por diseño | |
| — | 22:108 | "Dario no volvió a mencionarlo esa semana, ni la siguiente." | ¿Prolepsis? | **CONSERVAR.** Es sumario de una no-acción que no confirma ninguna revelación. Cierra en "Como variación.", que es el beat del capítulo | |
| — | 24:92 | "Kal la vio llegar antes de que terminara de formularse. **Chiara también.**" | ¿SALTO? | **CONSERVAR.** Kal lo lee en la mirada que sigue ("Miró a Rivers; después… miró a Kal") | |
| — | 24:210 / 226 | "Era mentira…" / "*Mentira*, pensó Kal." | ¿GLOSA doble? | **CONSERVAR.** Son dos mentiras distintas: la junta inventada (210) y el "No" al interés económico (226). Las dos están en el POV de Kal, que estuvo en esa mesa | |

### C. Glosa, tic, repetición y certificación

| # | Cap:línea | Texto | Categoría | Propuesta | Palabras |
|---|---|---|---|---|---|
| C14 | 21:24 | "Algo en el tono —ese temblor específico que Kal reconoció **antes de que la cabeza terminara de despertarle del todo**— lo puso de pie." | REPETICIÓN SINTÁCTICA: 30 repite la forma ("antes de que la mente terminara de procesar el resto") y 16 ya dijo el reflejo | Cortar la cola; queda "—ese temblor específico que Kal reconoció—". Se conserva el reconocimiento, que es interioridad | −10 |
| C15 | 21:42 | "—Kal. —Lo dijo sin levantar la voz**, con la clase de calma que no dejaba espacio para discutir**—." | TIC ("la clase de") + GLOSA: la réplica y "Kal no tuvo con qué contestarle eso" ya lo muestran | Cortar la cola. **Veto libre** | −11 |
| C16 | 21:208 | "Chiara no dijo nada más sobre eso. **No hacía falta.**" | TIC: repite 110 en el mismo capítulo ("Chiara no preguntó a quién se refería. No hacía falta."). La fórmula vuelve en 24:62 y dos veces en el 44 | Cortarla en 208 y conservar la de 110, que sí informa que ella sabe de Michael | −3 |
| C17 | 21:190 | "Marisol se despidió en la puerta **con el mismo aire con el que** hacía todo: rápido…" | TIC ("con el mismo … con el que", marcado ya en el 18 y el 19) | "…se despidió en la puerta **como** hacía todo: rápido…" | −5 |
| C18 | 21:76 | "Marisol se abrazó las **rodillas**…" | REPETICIÓN LEXICAL: "rodillas" 4 veces en 48–76 (dos de Kal y dos de Marisol) | Opcional: "…se abrazó las **piernas**…". Las dos de Kal (48 y 74) son eco deliberado y se quedan. **Veto libre** | 0 |
| C19 | 24:178 | "Llamaron a Tommaso veinte minutos después. **Rivers había dicho que aparecía en la lista contraria;** Krane lo trató…" | REPETICIÓN FUNCIONAL: el lector lo sabe por 23:273 y lo vio entrar en 24:28 | Cortar la cláusula | −9 |
| C20 | 24:374 | "…su nombre estaba en el papel, esta vez en el renglón que le tocaba**: participación, acceso, beneficios, obligaciones, una puerta de salida**." | REPETICIÓN FUNCIONAL de 360 ("acceso al piso, derecho sobre beneficios, obligaciones claras y una cláusula de salida"), a 14 líneas | Cortar la lista; cierra en "…el renglón que le tocaba.", que cobra "lo quiero por escrito" (23:185). **DUDOSA, veto libre:** la letanía tiene ritmo | −8 |
| — | 21:90 | "—¿Te duele mucho la cara? —preguntó, **al final**…" | ¿Mecánica? ("al final" y luego "después") | **CONSERVAR (DUDOSA).** Se lee como "por fin, tras el silencio" | |
| — | 21:186 | "…el golpe de la noche anterior había empezado a doler menos." | ¿EMOCIÓN EXPLICADA? | **CONSERVAR.** El doble sentido (golpe físico y golpe de orgullo) es valor no informativo, y el autor revisó esta frase en el SURGERY del 09-12 | |
| — | 21:48 / 62 | "Cada semáforo en rojo…" / "En cada semáforo en rojo estiraba una mano…" | REPETICIÓN LEXICAL | **CONSERVAR.** Es rima deliberada: la misma espera, de Kal a Chiara | |
| — | 22:58 | "…con la clase de cansancio que no se nota en la cara pero se siente en cómo alguien se sienta." | TIC ("la clase de") | **CONSERVAR (DUDOSA).** El juego "se siente / se sienta" es voz | |
| — | 22:76 | "Ninguno de los dos dijo la palabra *sociedad*… —ella la versión, él la evidencia—…" | ¿GLOSA? | **CONSERVAR.** Es la tesis "él territorio, ella relato", y *sociedad* es el puente al pleito del 23 | |
| — | 23:49 / 119 | "…una pieza que nadie había pedido" / "…como quien evalúa una pieza que nadie pidió" | REPETICIÓN LEXICAL | **CONSERVAR (eco).** Nadir no paga una pieza no pedida y Hoover no le paga a Kal; Kal se recuerda como esa pieza. Nadie lo explica | |
| — | 23:57–59 / 295 | "Con esa cara, hablar sale caro." / "Mi cara es gratis." / "Tienes cara de nada caro." | Repetición | **CONSERVAR.** Callback de Héctor que cierra el capítulo | |
| — | 23:119 / 283 | "Kal pensó en una mesa de casino. En Matteo… En Chiara…" / "Kal pensó en Tommaso. En su apellido. En Chiara. En aquella primera mesa." | REPETICIÓN SINTÁCTICA | **CONSERVAR (rima interna).** "En su apellido" es ambiguo (¿el de Tommaso? ¿qué pesa?), pero puede ser misterio deliberado (DO_NOT_TOUCH). **D18** | |
| — | 23:261 | "Kal asintió. Era suficiente para empezar." | ¿GLOSA? | **CONSERVAR.** Es cadencia de cierre de sección y responde al "Para ganar, no sé" | |
| — | 24:342 | "…qué enfermedad te impide recibir dinero sin convertirlo en otro negocio." | Eco de 23:69 y del 19 ("¿Un trato o un negocio?") | **CONSERVAR.** Rima de pareja | |

## 2. Prolepsis y POV — lectura por capítulo

- **21:** los bloques de POV siguen la metadata (Kal en la llamada, el trayecto y el mezzanine; Chiara en el loft, el desayuno y la despedida). No hay saltos que corregir (21:30 se conserva). No hay prolepsis.
- **22:** Kal en la llamada y el auto; Chiara en su parte; exterior en la oficina; Dario en la coda, visto desde fuera ("le cruzó la cara"). Prolepsis: **B5** y **B6**.
- **23:** POV de Kal sostenido en todas las secciones. Sin saltos. Sin prolepsis.
- **24:** POV de Kal sostenido (el pulgar de Chiara, la silla que cruje detrás, la mano en la mesa: todo lo que Kal ve u oye). Prolepsis: **B7**. **Tommaso:** no hay ningún presagio de muerte. La "corbata negra" (34) es vestuario y no señal, así que se conserva. La REGLA DURA de la metadata se cumple: Tommaso no explica nada, no recibe gratitud y no deja pista del Consorzio.

## 3. Función por movimiento

Palabras con `wc -w` por rango de líneas.

**Cap. 21 (1,824)**

| Líneas | Movimiento | Palabras | Función | Veredicto |
|---|---|---|---|---|
| 14–44 | La llamada de Marisol; Chiara conduce | 216 | Residuo del 20; Chiara pone límite al rosado | C14, C15 |
| 48–62 | Trayecto; el club; "Espera a que ella quiera contarlo" | 217 | Chiara frena a Kal; la mano en los semáforos | Protegido |
| 66–102 | El loft: Diego, "como alguien a quien mintieron" | 408 | Chiara hace el trabajo emocional; Kal calla | C18 opcional |
| 106–120 | Mezzanine: la promesa | 135 | Línea canon de Kal (Michael) | Protegido |
| 124–186 | Desayuno: "Por los dos", el Audi, "bambina" | 607 | Pago de hospitalidad; alianza Chiara-Marisol | Intacto |
| 190–210 | Despedida: "Papá", el huracán, "Volvemos adentro" | 229 | Cierre canon | C16, C17 |

**Cap. 22 (904)**

| Líneas | Movimiento | Palabras | Función | Veredicto |
|---|---|---|---|---|
| 12–28 | La llamada de las 3:11 | 181 | Chiara convierte su problema en el de Kal | Protegido (ver D16) |
| 32–44 | La farola, Danny, la grúa | 178 | Él, la evidencia | B6 |
| 48–54 | Ella, la versión | 188 | El trabajo de relato de Chiara | B5 |
| 58–82 | La oficina: "Prefiero no preguntar", "Gracias" | 161 | Sociedad sin nombre | Protegido |
| 86–110 | Dario y Tommaso: "Como variación." | 187 | Dario registra a Chiara; Tommaso anota | Protegido (siembra de Tommaso) |

**Cap. 23 (1,788)**

| Líneas | Movimiento | Palabras | Función | Veredicto |
|---|---|---|---|---|
| 15–65 | El sobre con sello; Héctor; "salga caro de la cuenta correcta" | 406 | Kal elige la vía civil | **S6** (15) |
| 69–161 | El mensaje de Chiara; Rivers | 690 | Teoría legal; la primera mesa como conducta previa | **S5** (71); A4, A5 |
| 165–185 | Primera oferta; "lo quiero por escrito" | 118 | Motivo de Kal | A9; **S1: inserción después de 185** |
| 189–241 | Loft: sinónimos, "Entonces tiene uno" | 316 | Chiara se ofrece de testigo | Protegido |
| 245–261 | Garrett y las carpetas | 96 | Competencia de Garrett | Intacto |
| 265–299 | Tommaso en la lista; "cara de nada caro" | 150 | Gancho del 24 | Protegido |

**Cap. 24 (2,251)**

| Líneas | Movimiento | Palabras | Función | Veredicto |
|---|---|---|---|---|
| 16–38 | La sala civil; entra Tommaso; "Nada." | 239 | Tono; la entrada de Tommaso | Protegido |
| 42–62 | Krane y el contador | 226 | La estrategia de Hoover | Intacto |
| 66–116 | Testimonio de Chiara: "mi... amigo" | 262 | **Primera grieta** (ledger) | Protegido |
| 120–174 | Contrainterrogatorio | 175 | "Con frecuencia", "cercano", "razones personales" (ledger) | Protegido |
| 178–256 | Tommaso bajo juramento | 429 | La mentira favorable | C19, A7 |
| 260–284 | El pasillo: "Tommaso, no." | 92 | El enigma queda abierto | Protegido |
| 288–302 | Cuarto intermedio; el acuerdo | 249 | Resolución sin fallo | A8 |
| 306–322 | Firma; Hoover; el número para Krane | 159 | Siembra de "Rivers & Krane" | Protegido |
| 326–348 | Escalinata: "Ambición" | 97 | Pareja | Protegido |
| 352–396 | Villani; el Lancia | 308 | Puente al 25 | C20, B7 |

## 4. Protegido y siembras

### Protegido (ya aplicado o cobrado por otros)

- **21:** 108 "Es la única promesa que me queda de mi pasado…" (canon); 132 "Para los dos. No solo por Kal. Por los dos."; 170–172 "¿Me equivoco, Chiara?" / "Sin duda alguna, bambina."; 194 "Papá" dicho a la vez; 206 el huracán Marisol y Michael; 210 "Volvemos adentro" (decisión del autor, 09-12).
- **22:** 94 "sin que llegara a ninguno de los socios" y 106 "Tommaso anotó." (**Tommaso como el que anota**; el 23–24 lo cobra); 110 "Como variación."; 50 el favor de turnos buenos al supervisor (economía de favores de Chiara, afín a S5).
- **23:** 19 el sobre como formalidad, no descubrimiento (metadata); 61 "Si esto lo arreglo con hombres, la próxima vez el papel vale más que yo."; 155 el fiscal (canon del 19); 185 "Porque esta vez lo quiero por escrito."; 221 y 235 Tommaso sembrado por Chiara.
- **24:** 94–98 "mi... amigo" (ledger: NO se corta); 122–140 el registro semipúblico (ledger); 174 la mano en el borde de la mesa ("Una vez. Nada más."); 206–218 el testimonio de Tommaso; 284 "El juicio ya lo entendemos. Tommaso, no."; 312 "Recuperé. No es lo mismo." (metadata); 320 el número para Krane; 348 "La soltó al llegar a la acera. No antes."
- **24:88** "También habló de participación." Parecía contradecir la alineación con el Cap. 2 que declara la metadata. Cruce: en 2:664–666 Chiara le pregunta el porcentaje y Kal contesta con porcentajes ("no doy porcentaje sin saber qué estoy comprando"). Es un estiramiento que el propio 23:217–221 reconoce ("No igual." / "Lo bastante parecido."), no un error. Se protege.

### S5 — Rima 24↔44 (hilo C)

Las líneas del 44 que pueden rimar ya existen, así que **el 44 no necesita cambio:**
- **44:67:** "Movió dos llamadas al ayuntamiento a través de alguien que le debía un favor de El Faro, y consiguió, **en menos de una hora**…"
- **44:87:** "…**un nombre en la oficina del fiscal de distrito que alguna vez le había debido un favor de prensa y que esta vez no devolvió la llamada**."

**Propuesta (dos gestos, dentro de la escena existente del mensaje en 23:69–71):**
1. **Gesto 1, ya existe y se protege (0 palabras):** 23:69 "La respuesta llegó **en menos de un minuto**". Es la red de Chiara funcionando a la velocidad que el 44 le niega ("en menos de una hora", y luego nada).
2. **Gesto 2, línea nueva (DISEÑO, +20):** una segunda frase en el mensaje de Chiara, en su voz y en la misma negrita: **"Si esto se pone penal, en la oficina del fiscal hay un nombre que me debe un favor de prensa."** Así el "esta vez" de 44:87 cobra algo que el lector ya vio. El "a su manera" de 23:157 gana un referente concreto (Rivers es la enemiga del fiscal; Chiara, la acreedora dentro de su oficina), y en el 44 el caso **sí** se pone penal, sin que el narrador lo anuncie: es un condicional del personaje (§L lo permite).
- **Por qué ahí y no en el 24:** el 24 es de Kal y Chiara ya testifica; su red no actúa en escena. El mensaje es el único gesto de red de Chiara en el 23–24 y ya tiene su voz.
- **Riesgo:** el mensaje se vuelve un poco menos ligero. Si el autor lo prefiere intacto, el gesto 1 solo ya rima, aunque sin texto casi idéntico.
- **Fuera de lote (se reporta):** "El Faro" (44:67) no aparece en ninguna prosa anterior del Libro I, así que el lector no sabe que es un periódico. Y 44:75 "¿Cómo que no está ahí." no cierra la interrogación (si es deliberado, se conserva). El 44 no se toca aquí.

### S6 — Matteo y Fabrizio (hilo C)

Contexto: Fabrizio ya tiene dos gestos (llamada en el 5, acta en el 11) y Matteo uno ("Matteo cubre el piso", 16). **El del 23 debería ser de Matteo.** Cruce: en 5:449 Almendra Towing ya es proveedor del Monarch, con "facturación a fin de mes", y la ficha dice que Matteo es "la primera persona del Monarch que mira a Kal como solución".
- **Recomendado (DISEÑO, +10), 23:15:** "El sobre llegó al taller a las nueve y doce de la mañana, entre una factura de neumáticos, **el cheque del mes del Monarch firmado por Matteo Bellacorte** y un aviso del condado…". Es una firma, es funcional (el Monarch sí paga en papel el mismo día en que Hoover lo borra del suyo) y nadie lo comenta. Además rima en silencio con 44:143 (la placa de Matteo en una puerta a la que ya no entra nadie).
- **Alternativa (+9), 23:119, en el recuerdo de Kal:** "En Fabrizio diciendo que la inteligencia no era un defecto." Es un eco casi textual de 2:674 (Fabrizio corrigiendo a Tommaso en la junta), sin inventar backstory. Contras: le da a Fabrizio su tercer gesto y es memoria, no acción.
- Descartadas: un acta o una copia de la propuesta en manos de Fabrizio (23:127–129), porque abre un hilo probatorio que el 24 tendría que usar y chocaría con la mentira de Tommaso; y un permiso firmado para que Chiara testifique, porque suena a "Matteo cubre el piso".

### S1 y S2 — la moto de Nadir (consolidado 18–24)

Cruce clave: en 17:206 Nadir dice **"Pensamos que ibas a decir que no"**, y en 17:212 Kal fija "Avísenme. Aunque sepan que voy a decir que no." La línea canon "—Porque ibas a decir que no." es la reincidencia textual: Nadir rompe la regla sabiendo cuál es. En F1 (42:176–186) Kal le reprocha a Chiara exactamente eso ("decidiste, tú sola, cuánto necesitaba saber yo"; "Esas dos frases no cuestan lo mismo").

| Candidato | Pros | Contras |
|---|---|---|
| **23, sección nueva entre 185 ("…lo quiero por escrito.") y 189 ("Hoover respondió…")** — **RECOMENDADO** | POV de Kal. El taller ya está en escena y Nadir aparece en 49. El tema del capítulo es dinero, papel y palabra: Kal exige "por escrito" a Hoover y acepta de Nadir abonos de palabra, un espejo sin glosa. La línea de Héctor justo antes ("Cuando eras chico no te enojabas si te quitaban algo") le da filo al "Iba a decir que sí". Cae varios capítulos después del 17 y antes del 25. El salto de tiempo del pleito ("al cuarto día" → "Hoover respondió") admite una sección intermedia | El 23 cargaría S5, S6 y S1 (de ~1,790 a ~2,420). Dos cuentas en paralelo pueden volverse tesis si el narrador las enlaza; la escena **no** debe mencionar a Hoover |
| **19, entre 98 y 102** | Capítulo del Patio sobre confianza y paga ("No necesito caridad") | Repetición funcional con Harper, cuarto hilo en un capítulo lateral, y está pegado al 17 (menos sensación de reincidencia) |
| **21** | Familia elegida, promesas de Kal | Rompe la unidad de Marisol y el plan de POV (el cierre es de Chiara); misma noche que el 20 |
| 18, 20, 22, 24 | — | Descartados: 18 y 20 son corazones protegidos (E1); el 22 es bisagra de 900 palabras; el 24 es el tribunal |

- **Pago en el 42: sólo conducta, sin línea nueva.** F1 ya dice lo necesario; el lector que recuerde la moto oye el eco de "Iba a decir que sí" contra "todavía no sé, dame un día". Una línea explícita sería glosa y el 42 está fuera de lote.
- **S2: dentro de la escena de la moto** (Nadir llega con cara de haber manejado toda la noche, o se queda dormido en el sillón de la oficina; nadie pregunta ni él explica que son las rutas de Irene). Alternativa si S1 no va en el 23: una cláusula en 23:49 ("Nadir, con los ojos de no haber dormido, junto al elevador dos…", +6).
- **Punto de inserción para E5 (si se aprueba el 23):** después de 23:185 "—Porque esta vez lo quiero por escrito." y antes de `***` + 23:189 "Hoover respondió con otra versión de la historia.". Sección nueva con su propio `***`.

## 5. Lo que no es de microedición (se reporta y no se opera)

- **21:14 y 22:12, dos aperturas seguidas con una llamada a las tres de la madrugada** ("tres y algo" / "tres y once") y Kal de pie antes de colgar. El 21 se insertó el 09-07 delante de un 22 que ya existía. Puede ser una rima (la imprecisión de Marisol contra la exactitud de Chiara) o un accidente de montaje. Es estructural (aperturas y cronología), así que no se toca. **D16**
- **Metadata del 21:** dos líneas de `Estado` (2 y 7). Es housekeeping sin prosa y se hace en E4 salvo veto. La ficha de Marisol tiene deuda documental (la graduación y el primer encuentro con Chiara), anotada en la metadata del 21; queda fuera del lote.
- **23:69 "días antes" y 23:19 "unos días antes":** entre la videollamada del 19 y el sobre pasan el 20, el 21 y el 22 ("días después" más "dos días después"). Es holgado pero no está roto. Se reporta.
- **El 44** (fuera de lote): "El Faro" sin siembra previa y la interrogación sin cerrar (ver S5).

---

# § Balance de palabras del lote (8 y 18–24)

Conteo con `wc -w`, según las recomendaciones. §J: es contabilidad, no meta.

| Concepto | Palabras |
|---|---|
| Saldo de partida (5-ter) | **+1,134** |
| Poda E1 (8, 18, 19, 20) | +250 |
| Poda E2 (21 −29 · 22 −28 · 23 −6 · 24 −28) | +91 |
| Mecánica que suma (A7, A8) | −4 |
| S1, la moto (con S2 dentro) | −600 (tope) |
| S3, Camp Alder (8) | −45 |
| S4, pausa del 20 | 0 (recomendado: no añadir) |
| S5, 2.º gesto del mensaje (23) | −20 |
| S6, el cheque de Matteo (23) | −10 |
| **Saldo final para Irene en el 32** | **≈ +796** |

El 32 pide 800–1,000. Si se ejercen los vetos libres (C2, C6, C15 y C20 conservados), el saldo baja a ≈ +729. Si S1 sale en ~500 palabras, sube a ≈ +896.

---

# § Decisiones que necesito (E2)

*Consolidadas de E1 y E2. Preguntadas al autor el 2026-09-27. Las respuestas se anotan aquí con fecha.*

**Caps. 8 y 18–20 (de E1)**

1. **D1 — S3, Camp Alder:** en el 8, en 8:109, con el texto de §4 (recomendado), o en el 19.
2. **D2 — S4:** proteger el 20 tal cual (recomendado) o añadir la pausa de 8 palabras antes de "la verdad de lo pequeño".
3. **D3 — "camaleón" en el 8 (C3):** cortarlo para reservar la palabra a Kal (recomendado).
4. **D4 — El amanecer a las dos (8, A2):** cortar la cláusula del cielo (recomendado) o subir la hora a las cinco.
5. **D5 — Cierre del 18 (A3/B1):** (a) cerrar en "Nadie llamó a eso una cita." (recomendado), (b) cortar sólo la prolepsis y reformular sin sol, o (c) conservar. La luz del golf queda como está.
6. **D6 — Saltos de POV:** aprobar B3 (8:137) y B4 (18:215) como lecturas del POV y conservar 18:111 (recomendado).
7. **D7 — La videollamada del 19:** conservar el contracorte (recomendado) o abrir `***`.
8. **D8 — 20:218 (C13):** conservar (recomendado) o cortar la generalización.
9. **D9 — El letrero del notario (19:60):** dejarlo (recomendado) o precisarlo.

**Caps. 21–24 (nuevas)**

10. **D10 — S1, lugar de la moto:** el **23**, sección nueva entre 185 y 189 (recomendado); alternativas, el 19 (entre 98 y 102) o el 21.
11. **D11 — S1, el pago en el 42:** sólo conducta, sin línea nueva (recomendado).
12. **D12 — S2:** dentro de la escena de la moto (recomendado); si no, una cláusula en 23:49.
13. **D13 — S5:** proteger 23:69 y añadir al mensaje de Chiara "Si esto se pone penal, en la oficina del fiscal hay un nombre que me debe un favor de prensa." (recomendado); o sólo el gesto 1, sin línea nueva.
14. **D14 — S6:** el cheque del Monarch firmado por Matteo en 23:15 (recomendado), o Fabrizio en el recuerdo de 23:119.
15. **D15 — Prolepsis:** cortar 22:54 "O eso creían los dos esa mañana." (recomendado), la cola del auto en 22:44 (recomendado, DUDOSA) y la 2.ª frase de 24:396 (recomendado).
16. **D16 — Las dos llamadas a las tres (21/22):** conservar como rima (recomendado) o marcarlo para cirugía estructural aparte.
17. **D17 — Atribución en 24:300–302:** ¿"—Lusardi mintió" es de Kal y "A favor mío…" de Rivers? Si es así, añadir "—dijo Kal" (recomendado).
18. **D18 — "En su apellido" (23:283):** conservar como misterio (recomendado) o precisar de quién es el apellido.

**Veto libre (sólo avisar si NO; si no se dice nada, se aplican):** C2 (8:115, "el reverso") · C6 (18:87, "la clase de tensión") · C15 (21:42, "la clase de calma") · C18 (21:76, "rodillas" → "piernas") · C20 (24:374, la lista de la firma) · A6 (22:84, `---` → `***`) · A9 (23:165, la raya) · el housekeeping de metadata del 21.

**Respuestas del autor (2026-09-27):** "todo según recomendación". Queda así:

- **D1** Camp Alder en el 8, en 8:109, con el texto de §4 (E3). **D2** El 20 se protege sin añadir nada. **D3** Se corta "camaleón" (C3). **D4** Se corta la cláusula del cielo (A2). **D5** (a): el 18 cierra en "Nadie llamó a eso una cita."; la luz del golf queda como está. **D6** B3 y B4 aprobados; 18:111 se conserva. **D7** Contracorte conservado. **D8** 20:218 se conserva. **D9** El letrero del notario se deja.
- **D10** La moto va en el **23**, sección nueva entre 185 y 189 (E4 marca el punto; E5 la escribe). **D11** El pago en el 42 es sólo conducta. **D12** S2 va dentro de la escena de la moto. **D13** S5: se protege 23:69 y se añade la segunda frase al mensaje de 23:71. **D14** S6: el cheque de Matteo en 23:15. **D15** Se cortan 22:54, la cola de 22:44 y la 2.ª frase de 24:396. **D16** Las dos llamadas a las tres se conservan como rima. **D17** Se añade "—dijo Kal" en 24:300. **D18** "En su apellido" se conserva.
- **Veto libre:** no se ejerció ninguno, así que se aplican C2, C6, C15, C18, C20, A6, A9 y el housekeeping del 21.
- **Saldo previsto para el 32:** ≈ +796 (con S1 a tope de 600).

---

# §9 Resultado (parte 1) — SURGERY de los Caps. 8, 18, 19 y 20 (E3, 2026-09-27)

**Autorización:** decisiones D1–D9 del autor ("todo según recomendación") y vetos libres no ejercidos (C2 y C6 se aplican). Antes de editar, `git diff --stat` confirmó que los cuatro capítulos seguían en `a8b7be0`, igual que en la auditoría. Los cuatro **siguen TERMINADO** y cada cabecera lleva una nota de cirugía en la línea de Estado.

**Prosa (`wc -w` sin metadata, con encabezado):** 8 = **2,699 → 2,663** (−78 de poda, +42 de S3) · 18 = **3,187 → 3,071** (−116) · 19 = **1,650 → 1,592** (−58) · 20 = **2,277 → 2,272** (−5).
**Poda E3: −257. Siembra S3: +42. Neto E3: −215.** El mapa preveía −250 de poda y +45 de S3; la diferencia es de conteo.

**S1 (la moto):** no cae en estos capítulos (D10: va en el 23), así que E3 no marca punto de inserción. **S4:** protegida sin añadir nada (D2).

### Cap. 8

| # | Before | After | Categoría | Qué ya hacía la escena / qué conserva |
|---|---|---|---|---|
| A1 | "Lo había armado sola **semanas atrás**…" | "…sola **días atrás**…" | Continuidad | La noche del ladrillo es del 7, días antes |
| C1 | "Esa semana, sin embargo, había estado llegando con el día ya archivado. Ordenado de antemano. Recortado." | (corte del párrafo) | REPETICIÓN FUNCIONAL | Lo hace el párrafo del "dobladillo cosido", más concreto y relacional. "…antes de hablar." pasa directo al diálogo sin costura |
| S3 | "…la Carretera de Milla estirándose paralela a la reja hasta perderse. Cuando Kal salió…" | "…hasta perderse. Más allá de los hangares, donde la autopista seguía hacia el noreste, corría otra cerca, más alta, con alambre arriba y una luz blanca y pareja que no era la de Kingsley. Un letrero verde: CAMP ALDER. Kal no giró la cabeza." ¶ "Cuando Kal salió…" | **Siembra (hilo B). Línea nueva del agente: BORRADOR hasta que la lea el autor** | Una sola imagen; "cerca" (palabra del 43) y luz blanca para no confundirla con la reja de Kingsley. Chiara no comenta; el gesto de Kal es observable desde su POV. El párrafo se parte en dos para que la rampa abra limpio |
| C2 | "Era el reverso de la primera reunión en el Monarch — sólo que esta vez la que estaba parada en un cuarto que no era suyo era ella." | (corte del párrafo) | GLOSA + REPETICIÓN FUNCIONAL | El párrafo anterior ya compara con "una junta del Monarch" y la carrera formula la inversión ("Éste era uno de los cuartos donde él leía la sala antes que ella") |
| C3 | "…sin que sirviera de nada después en una comisaría. El camaleón perfecto: cambiaba de color sin cambiar una sola letra." | "…en una comisaría." | GLOSA (ornamento) + palabra canon | "Camaleón" queda reservada a Kal, una vez y sólo delante de ella. El acertijo de Mac lo explica la frase anterior |
| B3 | "…una sonrisa que no llegó a completarse, porque acababa de entender de dónde había salido esa palabra." | "…que no llegó a completarse: había entendido de dónde salía esa palabra." | SALTO DE POV → lectura del POV | La deducción se apoya en la sonrisa, que Chiara sí ve. Se conserva la única señal de que *Mandorla* significa algo |
| A2 | "Entró a la ciudad por el sur, con el cielo empezando a decidirse por un gris muy claro sobre el agua." | "Entró a la ciudad por el sur." | Continuidad | A las dos de la mañana no clarea. "Pasaban de las dos" queda intacto |
| B2 | "…entre el respaldo y un trapo de taller. No volvió a acordarse de ella." | "…y un trapo de taller." | PROLEPSIS (§L) | La Colombina queda disponible para reaparecer. El beat canon del espejo, intacto |

### Cap. 18

| # | Before | After | Categoría | Qué ya hacía la escena / qué conserva |
|---|---|---|---|---|
| C5 | "…decidió seguirle la corriente con la misma naturalidad con la que aceptaba todo lo que él improvisaba." | "…decidió seguirle la corriente." | TIC + INTENSIFICADOR | El "todo" chocaba con la confusión previa. La réplica siguiente ("como si hubiera sido idea suya") ya muestra la naturalidad |
| C6 | "Se sostuvieron la mirada un momento de más, con esa clase de tensión que no pedía nada en voz alta pero tampoco se molestaba en esconderse del todo." | "Se sostuvieron la mirada un momento de más." | GLOSA + TIC | "Un momento de más" ya es la tensión |
| C4 | "…alguien se salía con la suya delante de ella. Una vez más, Kal Mercer lo había conseguido." | "…delante de ella." | COMPETENCIA EXPLICADA | La mueca y "se salía con la suya" lo dicen |
| C7 | "…corta y genuina, la clase que no se molestaba en contener delante de él." | "…corta y genuina." | TIC | La escena entera ya es "delante de él" |
| B4 | "No dio nombres, no hizo falta: lo que Kal necesitaba saber ya lo tenía guardado desde antes sin haberlo pedido, un rubio…" | "No dio nombres, no hizo falta: Kal ya sabía de quién hablaba, un rubio…" | SALTO DE POV → saber compartido | Se conserva el dato (Kal sabía de Blake) sin entrar en su cabeza a media réplica de Chiara |
| A3/B1 | "Nadie llamó a eso una cita. Al día siguiente, cuando alguien preguntó, los dos dijeron que eran buenos amigos, y lo dijeron sin que se les moviera un músculo." ¶ "Ese jueves, de camino a casa, la nube por fin se abrió y salió el sol de siempre, tarde y sin ganas, sobre una ciudad que ya había dejado de mirar el cielo." | "Nadie llamó a eso una cita." (fin) | PROLEPSIS (§L) + continuidad | El sol contradecía el regreso "con la nube todavía sin romperse" y la hora (ya dormían en el penthouse). La ficción de "buenos amigos" ya está en la apertura del 18 y la retoma el 20 |

**No se tocó:** la luz del golf (D5), 18:111 (D6), la silla verde, "No es una historia", "Se quedó", el Nova del 78, los callbacks de la hierba y las habitaciones.

### Cap. 19

| # | Before | After | Categoría | Qué ya hacía la escena / qué conserva |
|---|---|---|---|---|
| C10 | "…más largo de lo que cualquier reglamento militar habría tolerado, Garrett llevaba los lentes como quien lleva una herramienta, no una vanidad." | "…habría tolerado. Los lentes eran una herramienta, no una vanidad." | REPETICIÓN LEXICAL | El párrafo abre con "Garrett llevaba… los lentes oscuros". "Moreno, con barba corta…" queda como frase nominal (ver autocrítica) |
| C8 | "…por lo que acababa de pasar en esa puerta — así funcionaban, y así les había funcionado bien hasta ahora: cada quien en lo suyo… en problema." | "…en esa puerta." | GLOSA expositiva | La primera cláusula ya dice la relación; se va el "hasta ahora" con sabor a presagio |
| C9 | "…antes de que lo desechara con la misma velocidad con la que hacía cualquier otra cosa." | "…antes de que lo desechara." | TIC | Se conserva el eco deliberado de "la misma cara desconfiada" |
| C11 | "…para cuando de verdad no sabía…" / "…un terreno donde de verdad puede ayudar…" | "…para cuando no sabía…" / "…donde puede ayudar…" | TIC | Quedan los dos "de verdad" que miden algo (la sorpresa y la carcajada) |

**No se tocó:** "Ciao, tesoro", Margaret Rivers (única entrega), la videollamada con su contracorte (D7), el letrero del notario (D9), el flashback de Santa Lucía.

### Cap. 20

| # | Before | After | Categoría | Qué ya hacía la escena / qué conserva |
|---|---|---|---|---|
| C12 | "…no pegada, pero sin la distancia de cortesía que había cuidado durante meses." | "…sin la distancia de cortesía." | REPETICIÓN LEXICAL | La frase de los meses queda sola en el baile, que es la que fija la metadata |

**No se tocó:** el drift, el mirador, "la verdad de lo pequeño" (S4, D2), 20:218 (D8), el núcleo de la seguridad, la apertura ("Ni una palabra.").

**Finales de línea:** 8, 18 y 20 conservan CRLF (18 y 20 tienen una línea LF dentro de la metadata, anterior a E3 y fuera del diff). **El 19 ya estaba entero en LF** en el árbol de trabajo antes de E3; se conservó así (git lo normaliza al tocarlo). `git diff --stat`: 8 (+7 −9), 18 (+6 −8), 19 (+5 −5), 20 (+1 −1), contando la línea de Estado de cada cabecera.

### Autocrítica parcial (E3)

- **Más dudas:** C10 en el 19. Al cortar "Garrett llevaba los lentes", "Moreno, con barba corta…" queda como frase sin verbo. Funciona como retrato nominal, pero es la única costura visible. Si al autor le suena trunca: "Era moreno, con barba corta…" (+1).
- **Más agresivo:** el cierre del 18 (dos frases). Lo justifica la contradicción objetiva con el regreso en auto, no el gusto.
- **Línea nueva del agente:** S3 en el 8. La siembra está aprobada, pero la redacción es mía y queda para que la lea el autor.
- **De corte a protección:** en esta etapa no cambió ningún veredicto; se respetaron los protegidos de E1 (18:111, la videollamada, el espejo del 8, 20:154).
- **Riesgo de esterilizar:** bajo. Los cortes del 18 son colas de tic; chistes, réplicas y silencios quedan intactos.

---

# §9 Resultado (parte 2) — SURGERY de los Caps. 21, 22, 23 y 24 (E4, 2026-09-27)

**Autorización:** decisiones D10–D18 del autor ("todo según recomendación") y vetos libres no ejercidos (se aplican C15, C18, C20, A6, A9 y el housekeeping del 21). Antes de editar, `git diff --stat` confirmó que el 21, 22, 23 y 24 seguían en el estado auditado (sin cambios en el árbol de trabajo; sólo estaban modificados el 8 y el 18–20 de E3). Los cuatro **siguen TERMINADO**, y cada cabecera lleva una nota de cirugía en la línea de Estado.

**Prosa (`wc -w` sin metadata, con encabezado):** 21 = **1,824 → 1,794** (−30) · 22 = **904 → 875** (−29) · 23 = **1,788 → 1,811** (−6 de poda, +29 de S5 y S6) · 24 = **2,251 → 2,227** (−28 de poda, +4 de mecánica).
**Poda E4: −93. Mecánica que suma: +4. Siembras S5 y S6: +29. Neto E4: −60.** El mapa preveía −91, +4 y +30; la diferencia es de conteo (C17 salió en −6 y B6 en −22).

**S1 (la moto), punto de inserción para E5 (D10):** en `23_La_Letra_Pequena.md`, después de la línea 183 "—Porque esta vez lo quiero por escrito." y antes del `***` de la línea 185, que abre "Hoover respondió con otra versión de la historia." (187). Queda como sección nueva con su propio `***` delante: réplica (183) → `***` → **escena de la moto** → `***` (el actual, 185) → "Hoover respondió…" (187). S2 va dentro de la escena (D12). En E4 no se escribió prosa de la moto.

### Cap. 21

| # | Before | After | Categoría | Qué ya hacía la escena / qué conserva |
|---|---|---|---|---|
| C14 | "—ese temblor específico que Kal reconoció antes de que la cabeza terminara de despertarle del todo—" | "—ese temblor específico que Kal reconoció—" | REPETICIÓN SINTÁCTICA | El 16 ("reflejo que no le pertenecía a un hombre recién dormido") y el 30 ("antes de que la mente terminara…") ya dicen que el cuerpo va primero. Se conserva el reconocimiento (interioridad) |
| C15 | "—Lo dijo sin levantar la voz, con la clase de calma que no dejaba espacio para discutir—." | "—Lo dijo sin levantar la voz—." | TIC + GLOSA | La réplica y "Kal no tuvo con qué contestarle eso" muestran la calma |
| C18 | "Marisol se abrazó las rodillas contra el pecho" | "…las piernas contra el pecho" | REPETICIÓN LEXICAL | Las dos "rodillas" de Kal (48 y 74) quedan como eco deliberado |
| C17 | "…se despidió en la puerta con el mismo aire con el que hacía todo:" | "…en la puerta como hacía todo:" | TIC | Los dos puntos y la enumeración siguen igual |
| C16 | "Chiara no dijo nada más sobre eso. No hacía falta." | "Chiara no dijo nada más sobre eso." | TIC (repetía 110) | Se conserva la del mezzanine (110), que informa que ella sabe de Michael. El silencio de Chiara y el beso en la frente cierran solos |
| Housekeeping | Línea 2: "Estado: TERMINADO (ver linea de Estado mas abajo; la marca inicial 'borrador provisional' era historica…)" | Retirada. Queda una sola línea de Estado (la de la aprobación del 09-12), que registra la retirada | Metadata | No se pierde información: la línea retirada sólo remitía a la otra |

**No se tocó:** "Es la única promesa que me queda de mi pasado…", "Para los dos. No solo por Kal.", "¿Me equivoco, Chiara?" / "Sin duda alguna, bambina.", "Papá" dicho a la vez, el huracán Marisol, "Volvemos adentro", 21:30 (lectura de POV), 21:90 "al final", 21:120 y 21:186.

### Cap. 22

| # | Before | After | Categoría | Qué ya hacía la escena / qué conserva |
|---|---|---|---|---|
| B6 | "Ahí Kal hizo lo que sabía hacer: lo desarmó, lo guardó, y ese auto en particular iba a tardar mucho tiempo en volver a existir en ningún registro que a alguien le interesara consultar." | "Ahí Kal hizo lo que sabía hacer: lo desarmó y lo guardó." | PROLEPSIS (§L) | "Lo que sabía hacer" ya dice la competencia; el destino del auto lo cobra "Ésa es tu parte. Prefiero no preguntar." |
| B5 | "…no le importaba a nadie a esa hora." ¶ "O eso creían los dos esa mañana." | "…no le importaba a nadie a esa hora." | PROLEPSIS DE NARRADOR (§L) | La escena de Dario ("Sin que llegara a los socios… Interesante.") muestra, sin anunciarlo, que el cierre no fue tan limpio |
| A6 | `---` | `***` | Mecánica (separador) | Se normaliza con el resto de la Parte I; el cambio de mundo lo marca "Tommaso se lo mencionó…" |

**No se tocó:** "sin que llegara a ninguno de los socios", "Tommaso anotó.", "Como variación.", el favor de los turnos buenos, 22:58 "la clase de cansancio" (DUDOSA, voz), 22:76 *sociedad*, 22:108 y la llamada de las tres (D16).

### Cap. 23

| # | Before | After | Categoría | Qué ya hacía la escena / qué conserva |
|---|---|---|---|---|
| S6 | "…entre una factura de neumáticos y un aviso del condado…" | "…entre una factura de neumáticos, el cheque del mes del Monarch firmado por Matteo Bellacorte y un aviso del condado…" | **Siembra (hilo C). Línea nueva del agente: BORRADOR hasta que la lea el autor** | Es una firma sin comentario: el Monarch paga en papel el mismo día en que Hoover lo borra del suyo. Se conserva la enumeración del correo de taller (+10) |
| S5 | "**…Se pone insoportable cuando cree que le deben gratitud.**" | "**…gratitud. Si esto se pone penal, en la oficina del fiscal hay un nombre que me debe un favor de prensa.**" | **Siembra (hilo C, rima con 44:87). Línea nueva del agente: BORRADOR hasta que la lea el autor** | Se protege el gesto 1 ("en menos de un minuto"). Es un condicional del personaje, no un anuncio del narrador, y le da referente al "a su manera" de 23:157 (+19) |
| A4 | "Rivers revisó la primera carpeta. Después la segunda." | "Rivers abrió la primera carpeta." | Continuidad (mecánica) | Ahora "pasó a la segunda carpeta sin levantar la vista" (101) es el único paso a la segunda |
| A5 | "…puestas en el orden correcto." ¶ "Cerró la carpeta." ¶ "—¿Y ahora?" | "…puestas en el orden correcto." ¶ "—¿Y ahora?" | Continuidad (mecánica) | La carpeta ya se había cerrado con un dedo en 107. La sentencia de Rivers pasa directo a la pregunta de Kal |
| A9 | "Dinero, no todo — suficiente para que…" | "Dinero, no todo: suficiente para que…" | Mecánica (puntuación) | Mismo ritmo, sin raya espaciada en la narración |

**No se tocó:** el sobre como formalidad, "Si esto lo arreglo con hombres…", el fiscal (155), "Chiara ya se lo había dicho a su manera" (ahora con referente), "lo quiero por escrito", "Eso viene de Italia", Tommaso sembrado por Chiara (221 y 235), "En su apellido" (D18), "Tienes cara de nada caro" y los ecos de la pieza que nadie pidió.

### Cap. 24

| # | Before | After | Categoría | Qué ya hacía la escena / qué conserva |
|---|---|---|---|---|
| C19 | "Llamaron a Tommaso veinte minutos después. Rivers había dicho que aparecía en la lista contraria; Krane lo trató…" | "Llamaron a Tommaso veinte minutos después. Krane lo trató…" | REPETICIÓN FUNCIONAL | El lector lo sabe por la llamada del 23 y lo vio entrar al abrir el 24 |
| A7 | "No giró la cabeza junto a Kal, ni junto a Chiara." | "No giró la cabeza al pasar junto a Kal, ni junto a Chiara." | Mecánica (verbo faltante) | Se conserva la simetría "ni junto a Chiara" (+2) |
| A8 | "—Lusardi mintió." | "—Lusardi mintió —dijo Kal." | Mecánica (atribución, D17) | Deja claro que "A favor mío… Lo cobro ahora…" es de Rivers (+2) |
| C20 | "…en el renglón que le tocaba: participación, acceso, beneficios, obligaciones, una puerta de salida." | "…en el renglón que le tocaba." | REPETICIÓN FUNCIONAL de 360 | "El renglón que le tocaba" cobra "lo quiero por escrito" (23) sin repetir la lista que está 14 líneas antes |
| B7 | "No llamó ese día. La idea, de todos modos, ya no se iba a ir." | "No llamó ese día." | PROLEPSIS (§L) | El teléfono sostenido sin marcar y "Te conozco" dejan el Lancia abierto; el 25 lo paga sin aviso |

**No se tocó:** "mi... amigo", el registro semipúblico, la mano en el borde de la mesa, el testimonio de Tommaso, "Era mentira…" y "*Mentira*, pensó Kal" (son dos mentiras distintas), "El juicio ya lo entendemos. Tommaso, no.", "Recuperé. No es lo mismo.", el número para Krane, "No antes." y 24:88 "También habló de participación".

**Finales de línea:** los cuatro capítulos estaban enteros en CRLF antes de E4 y siguen así (0 líneas LF; el script leyó y escribió con `newline=""`). La advertencia de git "LF will be replaced by CRLF" es un aviso de autocrlf y no refleja LF en el archivo. `git diff --stat`: 21 (+6 −7), 22 (+3 −5), 23 (+5 −7), 24 (+6 −6), contando la línea de Estado de cada cabecera.

### Autocrítica (E4)

- **Más dudas:** S5, la segunda frase del mensaje de Chiara. Le da al mensaje un segundo movimiento, más serio, y acerca un poco la red de Chiara a lo penal. Lo sostiene que es un condicional del personaje, no del narrador, y que el 44 cobra el "esta vez". Si al autor le pesa, basta con quitar la frase: el gesto 1 sigue rimando.
- **Más agresivo:** B6 en el 22 (−22). Tenía humor de voz ("en ningún registro que a alguien le interesara consultar"), pero §L pide cortar, no suavizar, y la ironía se va con el anuncio.
- **De corte a protección:** en E4 ningún veredicto cambió. Se respetaron las protecciones de E2 (22:58, 21:90, 21:186 y 23:283).
- **Riesgo de esterilizar voz:** bajo, o medio en el 22 por B6. En el 21 los cortes son colas de tic y la voz de Marisol y Chiara queda intacta.
- **Racionalizar interioridad:** no. C14 conserva el reconocimiento de Kal y sólo quita la repetición del mecanismo.
- **Prosa más genérica:** C17 ("como hacía todo") es más plana que la fórmula, pero la fórmula era un tic marcado en tres capítulos seguidos.
- **Líneas nuevas del agente para que las lea el autor:** S6 (23:15) y S5 (23:71).

---

# §9 Resultado (parte 3) — Escena de la moto y registro final (E5, 2026-09-27)

**Rol:** redacción, no microedición (adenda B, 5-sexies; pagada con el 5-ter). **La escena entera es BORRADOR/DISEÑO del agente hasta que la lea el autor.** El 23 sigue TERMINADO en la prosa previa; la línea de Estado lo registra.

**Lugar (D10):** `23_La_Letra_Pequena.md`, sección nueva entre "—Porque esta vez lo quiero por escrito." y el `***` que abre "Hoover respondió con otra versión de la historia.". Queda: réplica → `***` → **moto** → `***` → Hoover.

**Palabras:** escena = **438** (`wc -w`), bajo el tope de 600. Prosa del 23: **1,811 → 2,250** (+439, con el separador).

**Qué hace la escena, beat por beat:**

| Beat | Qué pasa | Condición de la adenda que cumple |
|---|---|---|
| 1 | Kal llega a las siete y diez; la Kawasaki verde frente al taller; revisa la cadena: floja | "Kal lo descubre por la moto frente al taller" |
| 2 | Nadir dormido en el sillón de la oficina, botas y chamarra, "Olía a carretera" | **S2** (D12): cansancio de las rutas de la Ronda, sin explicar ni quejarse |
| 3 | Kal cuenta dos veces la caja de lámina "de los tratos, las piezas que no pasaban por factura y la mercancía que se movía sin papel"; falta lo que vale la moto | Fondo de tratos y mercancía, **no cocaína**. No se dice "el Patio": el nombre nace en el 38 |
| 4 | Nadir sobreexplica el precio (Phoenix, 4,200 → 3,600, llantas nuevas, *wallah*) | Ficha de voz: "Mintiendo/evadiendo: sobreexplica el número" |
| 5 | **"—¿Por qué no me dijiste?" / "—Porque ibas a decir que no." / "—Iba a decir que sí."** | Líneas canon **textuales** |
| 6 | Kal repone con su dinero; "Te lo pago" / "Ya sé"; abonos de doscientos por semana, "Trescientos cuando… Cuando se pueda" | Kal repone el fondo; Nadir paga en abonos. El "cuando se pueda" roza S2 sin nombrarlo |
| 7 | "No dijo dónde había pasado la noche."; afuera, la cadena: "Te la ajusto. Si hay que cambiarla, la pagas tú." / "Safi. Ésa te la pago de contado." | La moto se queda. Rima de conducta con la Honda de Rafa (Cap. 1: la cadena, los pagos), sin citarla |

**Controles:**
- **Sin glosa del narrador:** nadie enlaza la moto con el "Avísenme" del 17 ni con el "por escrito" de Hoover; la yuxtaposición queda al lector. La escena **no menciona a Hoover**.
- **Sin prolepsis (§L):** nada anuncia F1 ni el 42. El pago en el 42 es sólo conducta (D11); el 42 no se tocó.
- **POV:** Kal todo el tiempo. Lo de Nadir es observable (olor, ojos rojos, manos quietas); "como quien calcula antes de saber dónde está" es comparación desde fuera.
- **Voz de Nadir:** *khoya*, *wallah*, *safi* (tres en toda la escena, nunca dos en una línea); humor comercial herido ("Me sale caro"); se queda quieto cuando le importa ("Por una vez no tenía las manos ocupadas en nada"). **Voz de Kal:** frases cortas, trabaja mientras decide (cadena, caja, cartera), no explica por qué dice que sí.
- **Finales de línea:** el 23 queda entero en CRLF (0 LF sueltos). Se normalizó además un LF suelto que había en la línea 5 de la metadata.

**Registro compartido (regla común 6), releído justo antes y con edición puntual:**
- Dictamen, tabla de avance: fila del lote B y fila de cierre de la Parte I (reemplaza "resto").
- Adenda B: Camp Alder, S2, moto, casi-confesión del 20, rima 24↔44 y Matteo en el 23, marcados como aplicados o resueltos. Sección D: decisiones 1 (moto) y 2 (hilo B) resueltas.
- `CURRENT_BRIEF.md` (paso 11 y la moto en la evaluación de arco), `log.md`, `INDEX.md` (enlace al mapa), `00_Book_Map.md` (entrada del 23) y ficha de Nadir (Historia).

## § Saldo final de palabras (lote B)

| Concepto | Palabras |
|---|---|
| Saldo de partida (5-ter) | **+1,134** |
| Neto E3 (8, 18, 19, 20; poda −257, S3 +42) | +215 |
| Neto E4 (21–24; poda −93, mecánica +4, S5+S6 +29) | +60 |
| E5, la moto (con S2 dentro) | −438 |
| **Saldo final para Irene en el 32** | **≈ +971** |

El 32 pide 800–1,000: el saldo cabe entero. (La previsión de E2 era ≈ +796 con la moto a tope de 600.) Contabilidad, no meta (§J).

## Autocrítica final (MICROEDICION §F)

- **Más dudas:** el beat 3, la caja "de los tratos, las piezas que no pasaban por factura y la mercancía que se movía sin papel". Es la única frase que explica, y el "sin papel" puede leerse como eco buscado del "por escrito" de Hoover. Se sostiene porque la adenda exige que el lector sepa de qué fondo se trata (no cocaína). Si al autor le pesa, basta con "la caja de lámina de los tratos".
- **Más agresivo:** insertar una sección entera en un capítulo TERMINADO que ya cargaba S5 y S6. El 23 pasa de ~1,810 a ~2,250 palabras y ahora tiene dos cuentas en paralelo (Hoover y Nadir). La escena lo sostiene sin que el narrador las enlace, pero el autor debe juzgar si el capítulo aguanta el tercer hilo.
- **De corte a protección:** descarté una línea de Kal tipo "Kal no le preguntó" tras "No dijo dónde había pasado la noche": repetía la forma de 23:207 ("Kal tampoco preguntó") y explicaba el silencio.
- **Riesgo de esterilizar voz:** no aplica a prosa previa, que no se tocó.
- **Racionalizar interioridad:** bajo. Kal no piensa nada en la escena y todo pasa por conducta, como pide el pago en F1. El riesgo contrario es que el "Iba a decir que sí" se lea frío; lo sostiene la línea de Héctor justo antes ("Cuando eras chico no te enojabas si te quitaban algo").
- **Prosa genérica:** la Kawasaki verde, Phoenix y los números son detalles de mi invención (DISEÑO), igual que la cadena como cierre. Si el autor tenía otra moto en mente, cambian sin tocar las líneas canon.
- **Líneas nuevas del agente para que las lea el autor en todo el lote:** S3 (8:109), S6 (23:15), S5 (23:71) y la escena completa de la moto (23, entre "lo quiero por escrito" y "Hoover respondió").
