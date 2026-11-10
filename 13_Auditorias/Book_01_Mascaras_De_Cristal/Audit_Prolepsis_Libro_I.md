# AUDIT — Prolepsis en *Máscaras de Cristal* (libro completo)

**Modo:** AUDIT. No toca prosa. Cualquier corte espera la decisión del autor y luego se hace con `editorial-surgery`.
**Política:** [[12_Craft_Policies/editorial/EDITORIAL_POLICY]] §L (y §G), [[12_Craft_Policies/editorial/MICROEDICION]] (PROLEPSIS DE NARRADOR, PRESAGIO GARANTIZADO), [[12_Craft_Policies/revelations/Book_01_Mascaras_De_Cristal]].
**Numeración:** nuevo cauce del 2026-11-08, 47 caps. Se cita como `Cap.:línea de archivo` (archivo entre paréntesis cuando ayuda).
**Corpus:** `tools/editorial/libro_01_completo.json` (47 archivos, cotejados 1:1 con [[11_Books/Book_01_Mascaras_De_Cristal/00_Book_Map]]).

## Etapas

| Fase | Alcance | Estado | Fecha |
|---|---|---|---|
| 0 | Taxonomía | **HECHA** | 2026-11-10 |
| 1 | Barrido mecánico (detector + pasada amplia de recall) y triage | **HECHA** | 2026-11-10 |
| 1b | Verificación de cortes dictados en auditorías anteriores | **HECHA** | 2026-11-10 |
| 2 | Cruce semántico contra el mapa de revelaciones y el Libro II | PENDIENTE | — |
| 3 | Decisiones del autor (§ Decisiones) | PENDIENTE | — |
| 4 | Cirugía de lo aprobado, regeneración y subida | PENDIENTE | — |

## 0. Taxonomía

| Familia | Qué es | Trato |
|---|---|---|
| **Prolepsis de narrador** | El narrador afirma o confirma algo posterior al presente de la escena, aunque sea vago («ni después», «nunca sabría», «todavía no.» como promesa). | **Cortar** (§L). |
| **Presagio garantizado** | Una intuición del POV que el texto confirma con una certeza que el personaje no podía tener. | Cortar la confirmación; la intuición se queda. |
| **Prolepsis de personaje** | Lo que el POV cree, planea, teme o amenaza, aunque luego resulte cierto o falso. Incluye el plan en estilo indirecto libre. | **Proteger.** La ironía es del lector. |
| **Siembra muda** | Un objeto o un gesto que se cobra después sin que el narrador lo explique. | **Proteger**; sólo se corta la glosa que la explica. |
| **Prolepsis entre libros** | Cualquier anuncio de lo que pertenece al Libro II (H1, embarazo, incendio, Bonnie/Mei-Lin como arco, Halbrook antes del 47). | La más grave. Va a la Fase 2. |
| **Analepsis cerrada** | Dentro de un recuerdo, una anticipación que el mismo recuerdo resuelve antes de volver al presente. | Conservar, salvo que la catástrofe se revele más adelante en el libro (§L). |
| **Iterativo** | «Desde entonces…», «no volvió a…». | Lícito si cubre un tramo ya pasado o la escena misma; dudoso si se extiende al futuro de la trama. |

Las **líneas canon del autor** quedan fuera del alcance: si alguna cae en una familia prohibida, se reporta y no se propone corte.

## 1. Método

1. **Detector** (`tools/editorial/prolepsis_audit.py` + `checks/prolepsis.py` + `prolepsis_config.json`, `audit_only`, sin dependencias). Separa cada línea en narración, inciso de diálogo, parlamento, cita y cursiva. Revisa narración e inciso, y la cursiva con severidad rebajada. Excluye por defecto el parlamento (prolepsis de personaje lícita); `--incluir-dialogo` lo añade. Tiene 19 patrones en tres fuerzas. Pruebas: `tests/test_prolepsis.py`, con los casos ya dictados en auditorías anteriores como regresión.
2. **Pasada amplia de recall** (ad hoc): «más tarde», «años», «la última vez», «todavía no + imperfecto», «iba a + terminar/costar», «nunca/jamás + -ría» en narración. Se hizo para medir qué se le escapa al detector. Aportó tres casos que no tenían marcador fuerte (14:244, 14:200, 15:157); ninguno exige corte.
3. **Triage** con lectura de contexto de cada candidato ambiguo.

**Resultado:** 27 candidatos del detector (medium 4, low 12, info 11) más 3 de la pasada amplia. Quedan **1 corte recomendado**, **4 dudosas**, **1 protegida** y 24 falsos positivos o lícitos. El libro está casi limpio de marcadores explícitos: las auditorías por lote ya habían cortado la mayoría (§1b). Reporte crudo: `tools/editorial/reports/PROLEPSIS_LIBRO_01/`.

### A. Corte recomendado

| ID | Cap.:línea | Texto | Diagnóstico | Propuesta |
|---|---|---|---|---|
| P1 | 29:352 (`31`) | «Chiara sintió en el brazo que la sostenía que algo le tiraba del costado, y en la cara de él no se vio nada. **Todavía no.**» | **PROLEPSIS DE NARRADOR.** Promete que la cara de Kal lo dejará ver después, y la escena no lo cobra. No es canon: entró en la reescritura de Fase 4 del 2026-11-07 ([[98_Agent_Handoff/sessions/2026-11-07_claude_fase4_cap29_vamos_a_casa]]), después de la auditoría de la Parte II (B22), que había dejado la frase cerrada en «no se vio nada». | Cortar «Todavía no.» (−2). Las costillas y el gesto de minimizar se quedan. |

### B. Dudosas (decide el autor)

| ID | Cap.:línea | Texto | Lectura | Recomendación |
|---|---|---|---|---|
| D1 | 3:123 (`03`) | «No parecía un hombre libre. Todavía no.» | Es una percepción de Kal («parecía»), es decir, expectativa del POV, pero la cadencia del «Todavía no.» suelto es la misma que la de P1. | **CONSERVAR.** Es lo que Kal espera de Walt, no un dato del narrador. |
| D2 | 13:388 (`12`) | «Villani recordaría la venta en efectivo… alguien de la Fiscalía empezaría a hacer preguntas… El expediente seguiría abierto. Su nombre se iba a ir del centro…» | Es el plan de Chiara en estilo indirecto libre (POV Chiara), pero va en cinco futuros seguidos sin marca de cálculo, y puede leerse como si el narrador certificara el resultado. | **CONSERVAR** si el libro cumple el plan. Si algún punto no se cumple, basta una marca de cálculo al inicio («Contaba con que Villani recordaría…»). |
| D3 | 22:338 (`24b`) | «Ella no volvió a tocar el tema. Él tampoco.» | Es la misma forma que «No volvieron a hablar del balcón» (cortada en el Cap. 10 antiguo como prolepsis dudosa). Aquí la acota la cena: el párrafo siguiente abre con «Cuando se fue, pasada la medianoche». | **CONSERVAR.** La escena la cierra. Sólo hay que cortarla si el tema de Nadir no vuelve a salir entre ellos en todo el libro y se quiere evitar la lectura de «nunca». |
| D4 | 2:34 (`02`) | «…un ala de museo que la mitad de los invitados no volvería a visitar…» | Sarcasmo social con el registro de Chiara, no un hecho de trama. | **CONSERVAR.** |

### C. Protegida

| ID | Cap.:línea | Texto | Por qué |
|---|---|---|---|
| R1 | 14:242–244 (`14`) | «Fue la última vez que Kal vio a Dale vivo.» + la celda, la camisa y Ruth | Es una analepsis cerrada: la anticipación se resuelve en el párrafo siguiente, dentro del mismo recuerdo, La muerte de Dale se cuenta ahí mismo; el mirador (Cap. 18, `20`) añade el juego, la rosa y la lápida, pero no reserva la muerte. La línea viene de los planes del autor ([[11_Books/Book_01_Mascaras_De_Cristal/Part_01_Dos_Mundos/00_Plan_Cap12_Dos_Sillas_POV_Chiara]]). |

### D. Falsos positivos o lícitos (sin acción)

- **Acotados a la escena:** 7:561 y 8:89 («la primera vez en toda la noche / esa noche»); 12:532, 16:123 y 30:242 («no volvió a preguntar», dentro de la escena).
- **Iterativos hacia atrás:** 13:78, 14:26, 18:17, 35:89, 40:90 y 45:45 («desde entonces», sobre un tramo ya vivido).
- **Memoria o incertidumbre del POV:** 21:50 («sin saber todavía qué estaba viendo», recuerdo de lo ya vivido que se resuelve en la escena), 23:154, 36:347, 39:23 y 46:107.
- **Hipótesis o habla referida:** 14:22, 36:61, 37:165 y 24:184 («lo que ella no podía saber» es pasado, no futuro).
- **Cursiva de personaje:** 7:267 (*todavía no* es la muletilla de Tommaso).
- **Pasada amplia:** 14:200 (símil de hábito: «una pieza que todavía no sabía si iba a necesitar»); 15:157 y 16:269 (el café que Héctor «no iba a terminar»: conocimiento de Chiara y luego de Kal sobre Héctor, con eco entre capítulos).

## 1b. Verificación de dictámenes anteriores

Se buscaron en los 47 capítulos los 13 textos que las auditorías por lote dictaron como prolepsis (Caps. 5, 9, 10 y 12 de la numeración antigua; arco final B2 y B5). Los 12 de corte siguen **aplicados**. El único que sigue en el texto es el protegido B2 del arco final («en una columna que todavía no tiene título», hoy 42:87), conforme a lo dictado.

## 2. Pendiente: cruce semántico (Fase 2)

El regex no atrapa la prolepsis sin marcador. Falta tomar cada revelación reservada de [[12_Craft_Policies/revelations/Book_01_Mascaras_De_Cristal]] y cada materia del Libro II (H1, embarazo, incendio, Bonnie y Mei-Lin como arco, Halbrook antes del 47) y buscar sus palabras clave en los capítulos anteriores a la revelación, por Parte. Ahí se separan la siembra muda (proteger) y la glosa que la explica (cortar).

## Decisiones

| ID | Pregunta | Recomendación |
|---|---|---|
| P1 | ¿Cortar «Todavía no.» en 29:352? | Sí. |
| D1–D4 | ¿Conservar las cuatro dudosas? | Sí, las cuatro. D2 se revisa en la Fase 2 contra lo que el libro cumple del plan. |
| F2 | ¿Seguir con el cruce semántico (Fase 2)? | Sí, por Parte. |
