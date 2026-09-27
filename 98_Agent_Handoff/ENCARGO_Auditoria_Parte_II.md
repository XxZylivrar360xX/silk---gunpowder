# ENCARGO — Auditoría editorial Parte II (Caps. 26–34), por etapas

**Creado:** 2026-09-27, a petición del autor, después de cerrar la auditoría de la Parte I (Caps. 1–25).
**Por qué por etapas:** la Parte II suma ~27,000 palabras y el 30 necesita edición profunda. Ninguna sesión debe cargar todos los capítulos, sus cruces y la cirugía a la vez. **Cada etapa se ejecuta en una sesión limpia** (terminal nueva o `/clear`) y no depende del chat anterior: todo lo que necesita está en este encargo y en el mapa.
**Terminal:** una sola. Las etapas son secuenciales; no hay terminal paralela.

**Cómo se invoca cada etapa** (el autor pega esto):

> Ejecuta la etapa N de `98_Agent_Handoff/ENCARGO_Auditoria_Parte_II.md`.

---

## Reglas comunes a todas las etapas

1. **Lectura mínima al arrancar:** este encargo completo; la tabla **"Estado de etapas"** del mapa (`13_Auditorias/Book_01_Mascaras_De_Cristal/Audit_Caps_26-34_Parte_II.md`), si ya existe, y sólo las secciones del mapa que la etapa indique; la skill `editorial-surgery` y sus tres políticas (EDITORIAL_POLICY, DO_NOT_TOUCH y MICROEDICION). **No leer** START_HERE, el brief completo, `log.md`, el dictamen de la Parte II ni la evaluación de arco enteros: lo necesario está resumido aquí abajo.
2. **Verificar la etapa anterior:** si la tabla de estado no marca la etapa previa como hecha, detenerse y avisar al autor.
3. **Capítulos:** leer completos sólo los de la etapa en curso. Los cruces se hacen **con búsquedas** (`rg`/Grep), sin abrir archivos enteros: `06_Relationships/`, `01_Timeline/`, `02_Characters/`, `03_Factions/`, `05_Locations/`, `07_Ideas/`, los Book Maps, la Parte I y los Caps. 35–44. Antes de proponer cortar un objeto, frase, gesto o plan, **buscar sus pagos en la Parte III y en el Libro II** (lección del imán del 14).
4. **Formato:** el modelo es `13_Auditorias/Book_01_Mascaras_De_Cristal/Audit_Caps_08_18-24_Lote_B.md`, pero **no leerlo entero**. Basta con la tabla de estado, una tabla de §1 y una de §9.
5. **Política:** Prioridad según la matriz de abajo. Aplicar §L (el narrador no adelanta el futuro) y revisar saltos de POV. Palabras liberadas **sin cuotas** (§J): el 15–20 % del 30 es la referencia del dictamen, no una meta.
6. **Estado de los capítulos:** los nueve están en **BORRADOR**. La cirugía no los sube de estado: siguen BORRADOR hasta que el autor los lea. No hay CLOSE en este encargo.
7. **Lo estructural** (poda del 30, plan contra Varek, cronología 26–31) está autorizado por el dictamen **sólo como propuesta**: se mapea en AUDIT, el autor decide en E4 y se ejecuta en SURGERY. Si aparece otro problema estructural no previsto (motivación rota, un arco que hay que reordenar), se reporta y no se opera.
8. **Archivos compartidos** (dictamen de la Parte II, evaluación de arco, Hitos, fichas, `CURRENT_BRIEF.md`, `log.md`, `INDEX.md`, Book Map): sólo se tocan en **E9**, salvo la metadata de cada capítulo, que se sanea en su SURGERY. Se releen justo antes y se editan con Edit puntual. Si un script reescribe un archivo, debe conservar sus finales de línea (CRLF o LF, los que tenga); verificarlo al terminar.
9. **Al cerrar cada etapa:** actualizar la tabla "Estado de etapas" del mapa, reportar al autor en 5–8 líneas y terminar con la línea de checkpoint que sugiere `/clear` o terminal nueva. **No encadenar la etapa siguiente.**
10. **No tocar:** el EPUB; la Parte I (ya auditada); la Parte III salvo lectura por búsqueda.

---

## Datos de la Parte II (para no releer el dictamen)

**Forma:** tres movimientos. I — La crisis (26–30). II — La casa (31). III — La consolidación (32–34). El dictamen no recomienda eliminar, fusionar ni reordenar capítulos, ni insertar personajes del Libro II (**ni Riley, ni Mei-Lin, ni Ren Wei**). Halbrook **no** necesita más siembra en el Libro I. Consigna: **"hacer más visible la progresión y menos visibles las explicaciones".**

**Matriz** (palabras de prosa, `wc -w` desde el encabezado, 2026-09-27):

| Cap. | Archivo | Diagnóstico | Intervención | Palabras | Foco |
|---|---|---|---|---|---|
| 26 | `26_Me_Encuentro_Bien.md` | Sólido | MEDIA | 2,309 | Cronología; exposición repetida de H15 (lo que Chiara ya sabe por el jacuzzi) |
| 27 | `27_Riesgo_Pendiente.md` | Muy sólido | LIGERA | 2,535 | Compactar recorrido, instalación y contratistas; metadata vieja ("Halbrook llega al cierre del Libro I": ahora llega al cierre del **Libro II**) |
| 28 | `28_La_Correa.md` | Sólido | MEDIA | 3,020 | Glosas que traducen gestos; cronología |
| 29 | `29_El_Patio_Ajeno.md` | Muy sólido | LIGERA–MEDIA | 2,979 | Demasiadas semillas en una mesa; compactar Vivian → Marisol; **bug Peugeot → Audi** (28→29) |
| 30 | `30_Media_Baraja.md` | Necesita intervención | **PROFUNDA** | 4,783 | Sobrecarga, exposición, repetición y **plan contra Varek demasiado adelantado** |
| 31 | `31_Vamos_A_Casa.md` | Emocionalmente fuerte | MEDIA | 4,136 | Resumen repetido del 30; tienda de pesca, competencia y juego acuático; metadata "cierre de Parte II" |
| 32 | `32_Linea_Directa.md` | Muy sólido | LIGERA | 1,992 | Apretar el procedimiento; metadata. **Recibe la escena de Irene** |
| 33 | `33_Mas_De_La_Cuenta.md` | Funciona y es útil | MEDIA | 3,720 | Compactar Kenji/Marisol: química y respeto, no miniromance |
| 34 | `34_Mi_Pareja.md` | Muy sólido | MÍNIMA | 1,529 | Calibración fina de la transición Marisol → compromiso |

Todos están en `11_Books/Book_01_Mascaras_De_Cristal/Part_02_Con_Peores_Personas_He_Tratado/`. Prioridad: **alta** 30; **media-alta** 26, 28, 31, 33; **media** 29; **ligera** 27, 32; **mínima** 34.

**Columna que se protege (Hallazgo 2):** 28 descubren el problema ("No vuelvas a hacer algo así sola." / "No me digas qué puedo hacer." / "No era una orden." / "Sonó como una.") → 29 Kal abre ruta y ella decide tomarla → 30 lo vuelven sistema → 33 lo aplican a otros ("La suficiente para preocuparme. No la suficiente para escoger por ella.") → 34 compromiso sin control. **Se protegen los beats y se quitan las glosas que los traducen.**

**Inviolables del 30:** "Warren Halbrook"; Kal admite que dejó a Chiara mirar al antagonista equivocado; Nadir como palanca; la explicación de la silla; "Bellandi no"; las fotografías vistas juntos; el nacimiento funcional Patio + *i Sussurri*; "Con peores personas he tratado"; Nadir se entera de la verdad directamente por Kal; Danny pregunta por la salida de Camp Alder; **todavía no hay plan completo**. Baja: la explicación del futuro de Varek, recapitulaciones, glosas sobre cómo han cambiado, información que el lector ya tiene. Objetivo: **que termine como un pacto, no como un plan maestro de los dos libros siguientes.** El plan "volvernos necesarios… quitarle uno por uno los pedazos… hasta que no quede nada que sea sólo suyo" pertenece a *Sombras de Poder*: se conserva la dirección (entender dónde están, hacerse necesarios, ganar autonomía, dejar de depender de Varek) y se baja la **certeza**.

**Inviolables del 31:** vestidor, sándwiches, Harper, Chiara aprendiendo a pescar, el grupo, segundo beso, "Vamos a casa", sillón, "No era una orden / Sonó como una", los cuatro centímetros (que el 32 arregla a la mañana siguiente). El 31 **no se mueve ni pierde su coda**: cierra el arco H5–H7, no la Parte II. Se reduce **el resumen en el coche** de cómo reaccionaron Nadir, Walt, Danny y Héctor, porque el 30 ya lo dramatiza.

**Del 29 y el 34:** Kal no pide trabajar para Dario: consigue que Dario le ofrezca la silla (se queda). En el 34 se conservan "¿Y lo nuevo?" de Nadir y "Esta vez, cuando volvieron, ninguno de los dos tuvo que preguntar adónde.".

**Cronología que se fija (Hallazgo 4):** noche del Cap. 25 → madrugada, sale Kal → día fuera (Halbrook) → conduce de vuelta toda la noche → amanecer siguiente, Cap. 28 → Varek → Media Baraja → El Patio → lago. Unas 24 horas, no "dos días". Sobreviven "dos días", "la segunda noche", "los dos días anteriores", metadata de "2–3 días" y el 31 diciendo "el mismo día que Halbrook sacó a Kal de la ciudad de madrugada" (el día del 28–31 es el del **regreso**). Los personajes no tienen que contar horas; sólo no puede haber contradicción.

**Siembras y pendientes que caen en la Parte II:**

| # | Siembra | Estado | Condiciones |
|---|---|---|---|
| P1 | **Irene en el 32** (5-ter) | Nivel medio APROBADO; escena en DISEÑO | Gancho: el sedán de Halbrook que vigila a Nadir (28) aparece en las rutas de la Ronda; lo ve Tomás Vale. Temor de Irene: un hombre con papeles frágiles bajo presión federal puede cambiar lo que sabe, y Nadir conoce sus rutas; nadie lo explica. Irene cita a Kal (o manda a Tomás), no sabe quién está detrás y dice que no le importa. Nadir sale de la mercancía; la deuda no se perdona, cambia de forma. Kal no le cuenta lo de Halbrook y **acepta el favor abierto que se negó a deber en el 17**. Cierre del estilo "Ahora sí me debe" (redacción a decidir). Irene no amenaza a Nadir ni abre un frente que el Libro I deba cerrar. **800–1,000 palabras**, dentro de las dos semanas del 32. Kal queda apretado entre la policía (Lucía) y la calle (Irene). Opcional (hilo A): Chiara se entera por los *sussurri* y nota que Kal administra información |
| P2 | **Beretta .25**, primera aparición | CANON del autor: después del pacto con Dario, **30 o 31**; falta capítulo | Una sola imagen concreta (el bolso, un cambio de bolso), sin glosa y sin presagio. El 44 la cobra: "llevaba ahí desde hacía años" |
| P3 | Casi-confesión del tramo (hilo A), **31** | DISEÑO | Como en el 20: si ya existe un silencio donde uno elige una verdad más chica, se protege; si no, sólo un silencio, sin línea nueva |
| P4 | Nadir hace algo duro por el grupo y le cuesta (laguna para F2) | DISEÑO, "Parte II o III" | Sólo evaluar si el final del 30 (Nadir recupera agencia) o la salida de la mercancía en el 32 ya lo cubren. Proponer, no escribir, salvo aprobación |
| — | Ya aplicado, **proteger**: fe en la parrilla del 31 (Chiara se persigna, Nadir dice *bismillah*, Kal bromea con los peces y deja el tenedor quieto); Crowe en el 32 (el Tasador pregunta quién arregló lo de Portillo y cuánto cobró: "nada") | BORRADOR | No podar. Son siembras de la Parte III y del Libro II |
| — | Ritual del *Ciao*: antes del 34, Kal también es "tesoro"; después de formalizarse, "amore", "amore mio", "cariño" | CANON | Revisar por búsqueda que 26–34 lo respeten. Si algo choca, se reporta |
| — | No sembrar: maternidad/Elenna, Riley, Mei-Lin, Ren Wei, más Halbrook | — | — |

**Saldo de palabras de partida:** la Parte I deja **≈ +971** para Irene (ver `Audit_Caps_08_18-24_Lote_B.md`, § Saldo final). Irene cuesta 800–1,000, así que cabe sin la poda de la Parte II. Lo que libere la Parte II es margen adicional, no meta.

**Housekeeping de la Parte II (dictamen):** duración real 26–31; "segunda noche / dos días"; el 31 como "cierre de Parte II"; Halbrook "llega al cierre del Libro I"; Peugeot/Audi 28→29; lago contra documentos viejos del "río norte"; mecánica antigua de H6 en Hitos y fichas; Book Map con "La Construcción" contra el nombre operativo de la Parte II; estrategia explícita contra Dario en el 30.

---

## Etapa 1 — AUDIT de los Caps. 26, 27 y 28, y cronología fija

**Lee:** esos tres capítulos completos. Por búsqueda, en 26–31 y en su metadata: "dos días", "segunda noche", "días anteriores", "madrugada", "amanecer", "esa noche", "ayer", "Peugeot", "Audi". Las fichas de voz de `12_Craft_Policies/voice/` de los personajes en juego, por búsqueda.
**Hace:**
- Crea el mapa `Audit_Caps_26-34_Parte_II.md` con: cabecera, tabla **"Estado de etapas"** (E1–E9), estado de los capítulos para el `git diff --stat` de la SURGERY, y para 26–28: §0 diagnóstico, §1 candidatos por categoría, §2 prolepsis y POV, §3 función por movimiento con palabras, §4 protegido y §5 lo que no es de microedición.
- **§ Cronología 26–31:** la secuencia fija de arriba y la tabla de **todas** las referencias temporales encontradas en 26–31 (capítulo:línea, texto, compatible o no, corrección propuesta). El 29–31 se cubre sólo por búsqueda.
- **Metadata:** anota qué dice mal la de 26–28 (Halbrook, duración, H6), sin tocarla.
- Deja un **§ Decisiones (borrador)** con las preguntas de estos capítulos, **sin preguntarle todavía al autor.**

**No hace:** tocar prosa ni metadata; leer completos el 29 en adelante.
**Cierra:** estado E1 = hecha, más el checkpoint.

## Etapa 2 — AUDIT de los Caps. 29 y 30

**Lee:** del mapa, la tabla de estado, § Cronología y § Decisiones (borrador). Los Caps. 29 y 30 completos. Por búsqueda en 35–44, en `01_Timeline/03_Libro_02_Sombras_De_Poder.md` y en `02_Characters/Dario_Varek.md`: los pagos del plan contra Varek ("pieza por pieza", "necesarios", "la silla", "desmontar"), de la silla y del pacto.
**Hace:**
- Añade §0–§5 para 29 y 30.
- **El 30, a fondo:** §3 función por movimiento con palabras (los ~17 movimientos del dictamen: Halbrook → mentira de Kal → Nadir → silla → Chiara como activo → fotografías → *i Sussurri* → Vivian → Marisol → Kenji → estrategia conjunta → Varek futuro → línea titular → El Patio → Nadir descubre que fue usado → Camp Alder → sedán → pesca). Para cada uno: conservar, comprimir o cortar, con razón y pagos encontrados. Marca los inviolables.
- **§ Plan contra Varek:** cita las líneas exactas del plan, qué pagan en 35–44 y en el Libro II, y **dos o tres versiones** de "pacto, no plan" (dirección sin certeza), con recomendación. Es la corrección estructural principal: el autor decide en E4.
- **P2 (Beretta):** si el 30 es candidato después del pacto, dónde exactamente y con qué imagen.
- **P4:** si el final del 30 ya cubre "Nadir hace algo duro y le cuesta".
- Bug Peugeot/Audi: la corrección mínima, con la versión que respeta 28 y lo que venga después (buscar el auto en 30–31 y 35–44).
- Suma preguntas a § Decisiones (borrador).

**No hace:** tocar prosa.
**Cierra:** estado E2 = hecha, más el checkpoint.

## Etapa 3 — AUDIT de los Caps. 31 y 32, y diseño de Irene

**Lee:** del mapa, la tabla de estado, § Cronología, §3 del 30 (sólo el cierre: Nadir, Danny, Héctor, Walt, pesca) y § Decisiones (borrador). Los Caps. 31 y 32 completos. Por búsqueda: el trato del 17 (`17_Cuentas_Claras.md`: "favor", "debe", "Tomás"), el sedán del 28, `02_Characters/Irene_Salcedo.md`, `02_Characters/Tomas_Vale.md` (si existe), `03_Factions/La_Ronda_del_Canal.md`, la voz de Irene y la escena de la moto en el 23 (para no repetir su costo de S2).
**Hace:**
- Añade §0–§5 para 31 y 32.
- **El 31:** el resumen del coche frente a la escena del 30 (qué queda y qué se va); tienda de pesca, competencia y juego acuático; los inviolables; la frase "el mismo día que Halbrook sacó a Kal…".
- **P2 (Beretta):** si el 31 es mejor candidato que el 30. Recomienda uno.
- **P3:** ¿ya existe la casi-confesión en el 31? Si no, dónde cabe el silencio.
- **P1, Irene en el 32:** punto de inserción (línea y frase ancla), si es escena propia o se entrelaza con Lucía, POV, quién va (Irene o Tomás), el cierre ("Ahora sí me debe" u otra redacción, dos o tres opciones), si entra el hilo A de Chiara, y el costo estimado. **Sin escribir prosa.**
- Suma preguntas a § Decisiones (borrador).

**No hace:** tocar prosa.
**Cierra:** estado E3 = hecha, más el checkpoint.

## Etapa 4 — AUDIT de los Caps. 33 y 34, consolidación y preguntas

**Lee:** del mapa, la tabla de estado, §3 de cada capítulo y § Decisiones (borrador). Los Caps. 33 y 34 completos. Por búsqueda, en 35–44: Kenji y Marisol (para no podar lo que la Parte III cobra).
**Hace:**
- Añade §0–§5 para 33 y 34. En el 33, qué de Kenji/Marisol es química y respeto (se queda) y qué es miniromance (se compacta), con los pagos en 35–44. En el 34, sólo la calibración de la transición.
- **Ritual del *Ciao*** en 26–34: resultado de la búsqueda.
- **Balance de palabras de la Parte II:** lo que libera la poda de cada capítulo, lo que cuestan P1–P4 y el saldo final, partiendo de ≈ +971.
- Convierte el borrador en **§ Decisiones que necesito**, numeradas y con recomendación, incluidos los vetos libres (lo que se aplica si el autor no dice nada). **Le pregunta todo junto al autor** y, cuando responda, **anota sus respuestas en el mapa**, con fecha.

**No hace:** tocar prosa.
**Cierra:** estado E4 = hecha, con las decisiones registradas, más el checkpoint.

## Etapa 5 — SURGERY de los Caps. 26, 27 y 28

**Lee:** del mapa, la tabla de estado, § Decisiones (respuestas), § Cronología y §1 y §4 de esos capítulos. Los tres capítulos completos.
**Hace:**
- Antes de editar, comprueba con `git diff --stat` que los tres coinciden con el estado auditado. Si algo cambió, se detiene y avisa.
- Aplica lo aprobado para 26–28, incluidas las correcciones de cronología que caen aquí.
- Sanea la **metadata** de 26–28 (Halbrook al cierre del Libro II, duración, H6) y añade nota de cirugía en su línea de Estado (siguen BORRADOR).
- Registra en el mapa **§9 Resultado (parte 1)**: before/after, categoría, qué ya hacía la escena y qué conserva, palabras antes y después. Verifica finales de línea.

**Cierra:** estado E5 = hecha, más el checkpoint.

## Etapa 6 — SURGERY de los Caps. 29 y 30

**Lee:** del mapa, la tabla de estado, § Decisiones, § Plan contra Varek y §1, §3 y §4 del 29 y el 30. Los dos capítulos completos.
**Hace:**
- `git diff --stat` como en E5.
- Aplica lo aprobado: el bug Peugeot/Audi, la poda del 30 por movimiento, la versión elegida de "pacto, no plan" y la Beretta si cae en el 30.
- **La poda del 30 es la intervención más grande del encargo.** Se hace movimiento por movimiento, con el registro completo, sin tocar los inviolables y leyendo las costuras enteras al terminar. Si al operar aparece que un corte rompe un pago de 35–44, se conserva y se anota.
- Metadata y nota de cirugía en 29 y 30 (siguen BORRADOR).
- Añade al mapa **§9 Resultado (parte 2)**.

**Cierra:** estado E6 = hecha, más el checkpoint.

## Etapa 7 — SURGERY de los Caps. 31 y 32

**Lee:** del mapa, la tabla de estado, § Decisiones y §1 y §4 del 31 y el 32. Los dos capítulos completos.
**Hace:**
- `git diff --stat` como en E5.
- Aplica lo aprobado: el resumen del coche, la cronología del 31, la poda cotidiana, la Beretta si cae en el 31 y P3 si se aprobó.
- **Metadata del 31:** deja de ser "cierre de Parte II"; cierra el arco H5–H7.
- **Irene (P1):** no la escribe. Marca en el mapa el punto exacto de inserción en el 32 (línea y frase ancla) para E9.
- Nota de cirugía en 31 y 32 (siguen BORRADOR). Añade al mapa **§9 Resultado (parte 3)**.

**Cierra:** estado E7 = hecha, más el checkpoint.

## Etapa 8 — SURGERY de los Caps. 33 y 34, y housekeeping documental

**Lee:** del mapa, la tabla de estado, § Decisiones y §1 y §4 del 33 y el 34. Los dos capítulos completos. Para el housekeeping, **sólo por búsqueda**: "río norte" y "lago", la mecánica de H6 en `06_Relationships/Hitos.md` y las fichas, "La Construcción" en `00_Book_Map.md` y `01_Timeline/`, "cierre de Parte II", "dos días" en `01_Timeline/02_Libro_01_Mascaras_De_Cristal.md`.
**Hace:**
- `git diff --stat` como en E5. Aplica lo aprobado para 33 y 34, con nota de cirugía (siguen BORRADOR).
- **Housekeeping documental** (sin prosa): corrige, con Edit puntual, las referencias viejas de la lista del dictamen. Cuando haya contradicción de canon y no de simple desfase, **no sobrescribe**: la anota en el mapa para el autor.
- Añade al mapa **§9 Resultado (parte 4)** y la lista de housekeeping hecho y pendiente.

**Cierra:** estado E8 = hecha, más el checkpoint.

## Etapa 9 — Escena de Irene y registro final

**Aviso de rol:** escribir la escena nueva es redacción, no microedición. Se hace aquí por la decisión 5-ter (escena pagada con el saldo de la Parte I) y queda **BORRADOR/DISEÑO hasta que la lea el autor.**
**Lee:** del mapa, la tabla de estado, § Decisiones (P1) y el punto de inserción. Sólo el Cap. 32, completo. Por búsqueda: `02_Characters/Irene_Salcedo.md`, Tomás Vale, `12_Craft_Policies/voice/Irene_Salcedo.md`, `Kal_Mercer.md` y `Nadir_Amrani.md`, el trato del 17 y la escena de la moto del 23 (para no repetir el cansancio de Nadir con la misma imagen).
**Hace:**
1. Escribe la escena de Irene (800–1,000 palabras) en el punto marcado, con lo aprobado en § Decisiones. Sin glosa del narrador, sin prolepsis, sin explicar el temor de Irene. Mide las palabras.
2. **Registro compartido** (regla común 8):
   - en el dictamen de la Parte II, un bloque **AVANCE DE LA EJECUCIÓN** al inicio (como el de la Parte I) y la tabla de housekeeping marcada;
   - en la evaluación de arco, P1–P4 como aplicadas o resueltas (5-ter Irene, 5-quater Beretta y Nadir, casi-confesiones, certeza del plan del 30);
   - una línea en `CURRENT_BRIEF.md`, una en `log.md` y una en `INDEX.md` (enlace al mapa);
   - la entrada de los capítulos operados en el Book Map y las fichas de Irene y Nadir.
3. Cierra el mapa con la **autocrítica** (MICROEDICION §F) y el saldo final de palabras.

**Cierra:** estado E9 = hecha. Reporta al autor qué debe leer (la escena de Irene, la versión nueva del plan del 30, la Beretta y cada línea nueva del agente) y agrega el checkpoint.

---

## Si algo sale mal

- **Contexto al límite a mitad de una etapa:** guarda en el mapa lo hecho, marca la etapa como "parcial: hecho X, falta Y" y detente. La siguiente sesión retoma desde ahí. En E6 (el 30) es lo más probable: se puede partir en "E6a, el 29 y la mitad del 30" y "E6b, el resto".
- **Aparece un problema estructural no previsto:** se reporta y no se opera (skill, "Cuándo se activa").
- **El autor cambia una decisión entre etapas:** se anota en § Decisiones con la fecha, y manda la versión más reciente.
