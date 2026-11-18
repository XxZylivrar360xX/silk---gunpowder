# Lote 1 de *Sombras de Poder*: reglas para las terminales gemelas

Fecha: 2026-11-16 · Agente: Claude Code (terminal principal) · Encargo del autor: redacción en lote de los momentos clave del Libro II con terminales en paralelo. **Excepción al bloqueo de prosa del Libro II abierta por el autor** para estos capítulos.

| Terminal | Capítulo(s) | POV | Archivo que crea |
|---|---|---|---|
| T1 | 20 *El collar* | Kal | `11_Books/Book_02_Sombras_De_Poder/Part_02_Nieve_Y_Ceniza/20b_El_Collar.md` |
| T2 | 23 *La vela tardía* | Kal | `11_Books/Book_02_Sombras_De_Poder/Part_02_Nieve_Y_Ceniza/23_La_Vela_Tardia.md` |
| T3 | 45 *Lo poco que llegué a saber* | Kal | `11_Books/Book_02_Sombras_De_Poder/Part_04_Torna_A_Casa/45_Lo_Poco_Que_Llegue_A_Saber.md` |
| T4 | 52 *Santa Lucía* y 53 *Torna a casa* | Kal / externo | `.../Part_04_Torna_A_Casa/52_Santa_Lucia.md` y `53_Torna_A_Casa.md` |

La terminal principal integra al final: revisión de continuidad y `editorial-surgery`, handoff (brief, PENDING, log, Book_Map, CHAPTER_STATUS) y un solo commit con `regenerar-y-subir`.

---

## Reglas comunes (todas las terminales)

### Lo que puedes tocar

- **Sólo** el archivo o los archivos de tu capítulo y **una** nota de sesión propia: `98_Agent_Handoff/sessions/2026-11-16_claude_capNN_<titulo>.md`.
- **No toques** `CURRENT_BRIEF`, `PENDING`, `DECISIONS`, `BACKLOG`, `log.md`, `INDEX.md`, `00_Book_Map`, la guía, las tarjetas, las fichas, `Hitos.md`, `CHAPTER_STATUS`, `tools/build_sombras.py` ni otros capítulos. Si algo de eso debería cambiar, anótalo en tu nota bajo **«Para integrar»**.
- **Nada de git** (ni status con cambios, ni commit, ni push, ni checkout) y **nada de regenerar** EPUB, PDF o audio. Lo hace la terminal principal.
- El vault vive **sólo** en `H:\Mi unidad\Home_Vaults\Seda y Polvora`. No leas ni edites nada en G:.

### Antes de escribir

1. Lee `CLAUDE.md` (ya cargado), luego invoca la skill **`chapter-drafting`** y síguela.
2. Fuentes, en este orden de mando: `00_Plan_Cuatro_Partes.md` (hechos) → `00_Carretera_Libro_II.md` (columna y reloj) → la tarjeta de tu capítulo en `Part_0X_.../00_Tarjetas_Parte_X.md` → **sólo la ficha de tu capítulo** en `00_Guia_Redaccion_Capitulos.md` (búscala con `rg -n "^\*\*NN\. "`), más las secciones «Reglas de prosa propias de este libro» y «Lo que el lector no puede saber todavía» → el diseño específico que se te indica → las fichas de voz (`12_Craft_Policies/voice/`) de quien habla. No leas `Hitos.md` completo: búscalo con `rg`.
3. **PENDIENTES y propuestas:** antes de redactar, junta en **un solo mensaje** al autor todo lo que tu capítulo toca y que esté marcado PENDIENTE, «Opción», «por confirmar» o (P), con tu recomendación para cada uno, y **espera su respuesta**. No rellenes nada por conveniencia. Cita sus respuestas textuales en tu nota de sesión.
4. Lo que es CANON DEL AUTOR (líneas incluidas) se usa textual; sólo admite ajustes de puntuación.

### Al escribir

- Un solo POV por capítulo, el que fija la guía. `estado: BORRADOR` en el frontmatter, con el mismo formato que `Part_03_Exilio/36_Las_Latas.md` (title, type, estado, libro, capitulo, pov, ventana_temporal, localizacion, personajes).
- Español neutro en narración y diálogo ([[12_Craft_Policies/voice/00_Registro_Espanol_Neutro]]). Raya de diálogo. Pregunta de tono plano sin signos y con punto; nunca «¿» suelto. «Dijo» funcional; nada de adverbios en «-mente» en las acotaciones.
- Abre por residuo del capítulo anterior, sin resumir. Cierra con saldo (regla de la trenza): algo que Crowe cobra o ve, algo que Halbrook o Varek registran, o un secreto nuevo entre ellos.
- **Secretos que no se tocan:** Varek–Volpi (velado), el embarazo (no existe hasta «Sono incinta.»), la liberación de Kal, que Crowe trabaja para Halbrook (Chiara no lo sabe), la línea Tommaso → Meiko. El papel de Chiara: la prosa **nunca** dice «nombre» ni anuncia un secreto.
- Velas: Chiara reza en italiano, sin glosa. Técnica criminal fuera de cuadro.
- Meiko viva: presente, normal y querida, sin ningún gesto que se lea como presagio. Para su manera de ser, lee [[02_Characters/Meiko_Nakano]] y [[11_Books/00_Arco_Meiko_Nakano]] (el «hábito PENDIENTE» que aún cita la guía puede estar superado por el arco; si dudas, pregunta).

### Al terminar

1. Revisa tu capítulo contra las guardas de vigilancia del plan, los «No hacer» de su ficha y las reglas de arriba.
2. Escribe tu nota de sesión: archivo y palabras; fuentes leídas; **decisiones del autor tomadas en tu terminal (textuales)**; dudas que quedaron abiertas; siembras y cobros que tocaste (con capítulo de destino); **«Para integrar»** (cambios que la terminal principal debe hacer en otros archivos).
3. Dile al autor en tres líneas qué quedó y que está listo para integrar. No hagas nada más.

---

## T1 · Cap. 20, *El collar*

- **Diseño que manda:** `Part_02_Nieve_Y_Ceniza/00_Diseno_Navidad_Almendra_Towing.md` (CANON del 2026-10-14 en sus ocho puntos; su recomendación de POV Chiara está **superada**: POV Kal, un solo capítulo). Lee sus preguntas abiertas (§ al final) y llévalas al autor.
- **Canon clave:** Kaito en el portón, Meiko le grita que se largue; «¿Todo bien?» / «Todo bien, jefe». La foto de la cena la toma Chiara con el teléfono de Kal, ella no sale y Kal mira por encima del lente, a ella (lo cobran el 39 y el 57): pasa de largo, en una línea. El precio del regalo no llega.
- **Pregunta obligada al autor:** si este capítulo lleva una de las siembras de «sono a casa» ([[06_Relationships/Kal_y_Chiara#CANON — La llegada: «sono a casa»]]; el plan de cinco siembras espera su visto bueno). También: la opción de las luces en el garaje (depende del 19, sin prosa), si nieva o hiela, y si va Tommaso.
- Medida: si pasa de ~8,000 palabras, avisa antes de seguir.

## T2 · Cap. 23, *La vela tardía*

- **Fuentes extra:** [[04_Concepts/Fe_y_Velas]]; [[11_Books/Book_02_Sombras_De_Poder/00_Diseno_Nombre_Y_Embarazo]] (tic 4); lee, sin editarlos, `Part_03_Exilio/37_Lo_Del_Hermano.md` (cobra «Lo del hermano queda saldado») y `Part_04_Torna_A_Casa/57_La_Chimenea.md` (cobra el papel).
- **Siembra obligatoria para el 57:** en POV de Kal tiene que verse el papel (crema, grueso, el de las notas de ella, olor a canela) doblado en sus manos junto a la vela, y que él no pregunta. El 57 lo cobra con «la noche que le contó lo de la bahía. No había preguntado.».
- **Oración canon:** *«Dio, grazie per averlo riportato a casa.»*
- **Pregunta obligada al autor:** si Chiara dice «La próxima vez, dímelo antes» o lo deja en silencio. También la (P) del motivo de Kal para aceptar la incursión (paraguas de Dario tras Washington) y cómo paga la deuda de Kaito.

## T3 · Cap. 45, *Lo poco que llegué a saber*

- **Diseño que manda:** `Part_04_Torna_A_Casa/00_Diseno_Cartas_De_Dale.md`. Lee, sin editarlo, `Part_04_Torna_A_Casa/Stavanger.md` (el capítulo siguiente) para que el cierre empalme.
- **Canon clave:** siete cartas de Dale desde la cárcel, en un sobre de paquetería sin remitente, al taller; las entrega Manfred Gabe (primera aparición del nombre; Kal no le ve la cara y lo lee como un amigo más de su padre). Kal las lee solo, se desahoga con Chiara y las devuelve a la tumba de Dale en [[05_Locations/Cementerio_Santa_Lucia]]. Línea final de la última carta, textual: *«Lamento haberte arrebatado tu origen, te devuelvo lo poco que llegué a saber, no fui un padre para ti, pero eso no cambia que sí me importabas. -Dale»*
- **No hacer:** voz de terapia en las cartas, absolución en voz alta, que Chiara las lea, pista de que Manfred es alguien más que un civil. Ninguna de las dos deudas (Crowe, Varek) se confiesa.
- Residuo de la elipsis E (guía): dos cobros de Crowe en *El Faro*, el sobre sin abrir desde semanas atrás, Nadir con la grieta abierta.

## T4 · Caps. 52, *Santa Lucía*, y 53, *Torna a casa*

- **Fuentes extra:** sección «El final» del plan; [[04_Concepts/Fe_y_Velas]] (la vela de Kal, única en el libro); [[11_Books/Book_02_Sombras_De_Poder/00_Diseno_Nombre_Y_Embarazo]] (tic 9 en el 53); lee, sin editarlos, `54_Dime_Amore.md` a `57_La_Chimenea.md` para que la mañana y la salida empalmen con la noche ya escrita (hora, ropa, quién está, la placa del collar, Nat).
- **52 (Kal):** esa mañana, antes de las 11. Va solo a la Iglesia Santa Lucía, enciende una vela, se sienta a mirar el altar y el Cristo. No reza en voz alta, no habla con nadie, **no hay llamada**. Es corto: el miedo admitido sin convertirlo en acción.
- **53 (externo, nunca con interioridad de Chiara):** Chiara le pone la mano en el pecho, sobre la placa: «—Torna a casa.». Enciende la vela. Kal cree que habla de los dos; ella sabe que habla de los tres, **sin que la prosa lo diga**. Nada de «nuestro hijo».
- **Preguntas al autor:** cualquier hueco de horario entre la iglesia y la salida; si el 53 incluye a alguien más en la Villa; dónde queda la siembra de Nat si no está antes (el PENDING la pide antes del 54).

---

## Prompts para pegar

Cada terminal se abre en `H:\Mi unidad\Home_Vaults\Seda y Polvora`. Ver el bloque de cada una en el chat de la terminal principal.
