# ENCARGO — Auditoría editorial Parte III (Caps. 35–44), por etapas

**Creado:** 2026-09-27, a petición del autor, después de cerrar la auditoría de la Parte II (commit `7d4ab6c`).
**Por qué por etapas:** la Parte III suma ~32,000 palabras y el 38 sólo tiene ~8,600. Ninguna sesión debe cargar todos los capítulos, sus cruces y la cirugía a la vez. **Cada etapa se ejecuta en una sesión limpia** (terminal nueva o `/clear`) y no depende del chat anterior: todo lo que necesita está en este encargo y en el mapa.
**Terminal:** una sola. Las etapas son secuenciales; no hay terminal paralela.

**Cómo se invoca cada etapa** (el autor pega esto):

> Ejecuta la etapa N de `98_Agent_Handoff/encargos/ENCARGO_Auditoria_Parte_III.md`.

**Mapa de la auditoría** (lo crea E1): `13_Auditorias/Book_01_Mascaras_De_Cristal/Audit_Caps_35-44_Parte_III.md`. Modelo de formato: `Audit_Caps_26-34_Parte_II.md` (tabla de estado, §0–§5 por capítulo, § Decisiones, § 9 Resultado), **sin leerlo entero**: basta con su tabla de estado, una tabla de §1 y una de §9.

---

## Reglas comunes a todas las etapas

1. **Lectura mínima al arrancar:** este encargo completo; la tabla **"Estado de etapas"** del mapa, si ya existe, y sólo las secciones del mapa que la etapa indique; la skill `editorial-surgery` y sus tres políticas (EDITORIAL_POLICY, DO_NOT_TOUCH y MICROEDICION). **No leer** START_HERE, el brief completo, `log.md`, el dictamen de la Parte III ni la evaluación de arco enteros: lo necesario está resumido aquí abajo.
2. **Verificar la etapa anterior:** si la tabla de estado no marca la etapa previa como hecha, detenerse y avisar al autor.
3. **Capítulos:** leer completos sólo los de la etapa en curso. Los cruces se hacen **con búsquedas** (`rg`/Grep), sin abrir archivos enteros: `06_Relationships/`, `01_Timeline/`, `02_Characters/`, `03_Factions/`, `04_Concepts/`, `05_Locations/`, los Book Maps, las Partes I–II y `01_Timeline/03_Libro_02_Sombras_De_Poder.md`. Antes de proponer cortar un objeto, frase, gesto o plan, **buscar sus pagos en los capítulos posteriores de la Parte III y en el Libro II** (lección del imán del 14). La Parte III cierra el libro: casi todo lo que siembra se cobra en *Sombras de Poder*.
4. **Política:** prioridad según la matriz de abajo. Aplicar §L (el narrador no adelanta el futuro; aquí pesa doble con Tommaso, Mei-Lin, Héctor y Bonnie, cuyos destinos están en libros posteriores) y revisar saltos de POV. Palabras liberadas **sin cuotas** (§J): el rango del dictamen para el 38 (5,500–6,500 finales) es referencia, no meta. **Tampoco hay mínimo para lo que se escribe:** si una escena nueva cumple su función en menos palabras que su rango, se deja así y se reporta (lección de la escena de Irene, Parte II E9).
5. **Estado de los capítulos:** los diez están en **BORRADOR**. La cirugía no los sube de estado: siguen BORRADOR hasta que el autor los lea. El cierre de estado que pide el dictamen ("marcar 35–44 como cerrados sólo después de la pasada editorial") **no es parte de este encargo**: es un CLOSE posterior y sólo el autor declara TERMINADO.
6. **Lo estructural** (reubicar la coda del 35, poda profunda del 38, peripecia del 36, escena de Anya) está autorizado por el dictamen **sólo como propuesta**: se mapea en AUDIT, el autor decide en E4 y se ejecuta en SURGERY. Si aparece otro problema estructural no previsto, se reporta y no se opera. **No dividir el 38 ni renumerar** (el dictamen lo descarta).
7. **Archivos compartidos** (dictamen de la Parte III, evaluación de arco, Hitos, fichas, `CURRENT_BRIEF.md`, `PENDING.md`, `log.md`, `INDEX.md`, Book Map, `00_Plan_Cierre_Parte_III.md`): se tocan **sólo en E8** (housekeeping documental, con Edit puntual y sin borrar canon) **y en E9** (registro). La metadata de cada capítulo se sanea en su SURGERY. Se releen justo antes de editar. Si un script reescribe un archivo, debe conservar sus finales de línea (hoy el 36 es CRLF y los demás LF; verificarlo con `file` al empezar y al terminar).
8. **Al cerrar cada etapa:** actualizar la tabla "Estado de etapas" del mapa, reportar al autor en 5–8 líneas y terminar con la línea de checkpoint que sugiere `/clear` o terminal nueva. **No encadenar la etapa siguiente.**
9. **No tocar:** el EPUB (no se regenera en ningún momento de este encargo); las Partes I y II (ya auditadas); los libros II–VI salvo lectura por búsqueda.
10. **Bloques de diseño impresos:** en la Parte II apareció un bloque `> **DISEÑO…**` fuera del comentario HTML que el EPUB imprimía. En cada AUDIT, comprobar que ningún bloque de diseño o nota quede fuera de `<!-- -->`.

---

## Datos de la Parte III (para no releer el dictamen)

**Veredicto:** funciona como tercer acto y como final de novela. No necesita reconstrucción, capítulos nuevos (salvo lo que el autor ya decidió, ver P1), mover la reconciliación del Libro II hacia atrás ni engordar Camp Alder. Columna: hogar → ausencia → amenaza → Palermo → decisiones unilaterales → fractura → puerta → pérdida de control → regreso. Consigna: **"hacer que todo lo anterior llegue más limpio hasta 'Ciao, bella'"**; corregir 35, simplificar 36, adelgazar 38, proteger 39–44.

**Forma:** tres movimientos. I — La casa crece / las sillas empiezan a vaciarse (35–38, el falso punto alto). II — Las dos mitades (39–42: los dos protegen al otro administrándole información y fracasan por lo mismo). III — Puertas (43–44, corto a propósito; no inflarlo).

**Matriz** (palabras de prosa, `wc -w` desde el encabezado, 2026-09-27):

| Cap. | Archivo | Diagnóstico | Intervención | Palabras | Foco |
|---|---|---|---|---|---|
| 35 | `35_Sin_Fecha_De_Regreso.md` | Excelente apertura temática; coda fuera de cronología | **ALTA** | 2,256 | La escena de las invitaciones del yate ocurre después del 36 (Kal recibe la carta en el 37): residuo de montaje, no analepsis |
| 36 | `36_Tambien_Las_Mananas.md` | Centro emocional excelente; demasiados incidentes | **MEDIA–ALTA** | 2,462 | Densidad de peripecia antes de la llave; sangre y lodo de la apertura; susto cardíaco de Héctor; POV (metadata dice Chiara único y las tres primeras escenas son de Kal); Stella; origen de la Romanée-Conti |
| 37 | `37_Cuatro_Letras.md` | Compacto y funcional | MÍNIMA | 2,072 | No añadir, no explicar ROMA; título aún "provisional" |
| 38 | `38_Al_Reves.md` | Importantísimo pero sobredimensionado; conflicto de canon | **ALTA / PRINCIPAL** | 8,628 | Poda profunda; **la vela** de Santa Lucía; firma de Bonnie; título aún "provisional" |
| 39 | `39_Un_Par_De_Dias_Mas.md` | Ya depurado | MÍNIMA | 1,988 | No reabrir salvo continuidad |
| 40 | `40_Mecanico.md` | Largo pero justificado | MEDIA–LIGERA | 5,234 | ¿Llegada, casa, cata y cortesía de La Mesa pueden perder 10–15 % sin perder atmósfera? |
| 41 | `41_La_Otra_Mitad.md` | Causalidad muy buena | LIGERA–MEDIA | 1,966 | Que Bonnie no salga como confidente íntima; firma de Bonnie |
| 42 | `42_Nada.md` | Cerrado | MÍNIMA | 2,963 | Proteger |
| 43 | `43_La_Puerta.md` | Clímax moral correcto | MÍNIMA | 2,150 | Proteger; no convertir Camp Alder en set piece |
| 44 | `44_A_Oscuras.md` | Funciona como final de novela | MÍNIMA / HOUSEKEEPING | 2,280 | Proteger; metadata |

Todos están en `11_Books/Book_01_Mascaras_De_Cristal/Part_03_Ardizzone/`. Total ≈ **31,999**. Prioridad: **A** 38, 35, 36; **B** 40, 41; **C** 37, 39, 42, 43, 44 (proteger; no buscar cambios porque sí).

**El 35 — opciones del dictamen para la coda de las invitaciones**, en orden de preferencia: (1) mover el beat al final del 36; (2) convertirlo en una coda brevísima entre 36 y 37; (3) eliminar la escena y dejar que el 37 revele que Kal recibió una carta distinta. **No** arreglarlo escribiendo "tres semanas después" dentro del 35.

**El 36 — pregunta del dictamen:** cuánto incidente hace falta antes de la llave. Corazón inviolable: yegua → botella → llave, y **"Ya pasas las noches ahí. Quiero que pases también las mañanas, si estás de acuerdo."** (H16). Revisar: la apertura de sangre y lodo promete algo que no se cobra si el origen de la Romanée-Conti no importa después (buscar si se cobra); el susto cardíaco de Héctor puede leerse como presagio de una muerte que ocurre en *Voto de Ceniza* ("¿qué aporta que no aporte Héctor cansándose y Kal obligándolo a descansar?"). Viaje a Kingsley, caballo que se escapa y persecución de cuatro horas: candidatos a compactar.

**Inviolables del 38:** la fiesta como cruce de mundos ("por una noche, todos caben"); Blake: "No te dejé por nadie. Terminé contigo por ti." y "Ella me lo contará si quiere." (Blake queda cerrado, pero no necesita ~2,000 palabras); el piano (puerta a Kal que Chiara no abrió preguntando); **ROMA → AMOR**; **H13**; "Me voy esta noche." / "Voy contigo."; Marisol: "cuando estamos enamorados" y "¿cómo que estamos?" (preparan "Por mucho que yo esté enamorado de ti…" en F1). La calidez de Fabrizio (hace legible el enfriamiento del 41). Tommaso se despide con una inclinación y un "Chiara" que no parece despedida: **sin presagio**.
**Dónde podar el 38 (dictamen):** recorrido coral de invitados; reiteraciones de cómo se mezclan las tres fiestas; extensión de Blake; transición cubierta/proa; glosas del piano; explicación posterior a ROMA; logística del flashback de H13; interpretación de la bala; descripción del aeropuerto; llamada de Marisol antes de la línea final. Referencia: bajar hacia 5,500–6,500.
**La vela (ALTA / CANON):** en 38:495, Chiara va a misa a Santa Lucía y puede "encender la vela sin que nadie le preguntara por quién". Choca con `04_Concepts/Fe_y_Velas.md`: el ritual de la vela por Kal nace después de F4, en *Sombras de Poder*. Preferencia del dictamen: **retirar la vela**; Santa Lucía y la misa se quedan (la fe de Chiara sin pedir nada es siembra del 44).
**Pendiente del autor en el 38** (`PENDING.md`): peso de "Y tú eres mi gente" frente a F1; ingreso de Blake con el capitán; yate alquilado y piano; coche de Sam; siembra Marisol–Kenji; abreviatura "Sra." en diálogo canon. **No reescribir esa línea sin el autor**; E2 sólo lo mapea.

**Bonnie (37, 38, 41):** la misma firma corporal (leer salidas) tres veces en pocos capítulos se vuelve etiqueta. Una firma fuerte y variaciones: en uno de los tres beats, cambiar la conducta por lectura de vehículos, manos, sonido del motor, posición de otros o conocimiento del barrio, **sin añadir biografía**. Mei-Lin: suficiente, no tocar, no sembrar su muerte. En el 41, Chiara debe sonar a quien explica por qué le asigna una tarea a una operadora, no a quien busca apoyo.

**Personajes (no añadir):** Matteo (primera silla vacía; anomalía documental sin resolver), Lucía (Auster → Línea directa → A oscuras, nada más), Nadir/Héctor/Danny/Garrett (el 43 cobra; "Héctor jalando físicamente a Nadir"; sin arengas), Dario (estructura vigente, no antagonista final), Halbrook (sombra causal parcialmente invisible), La Mesa (la presión entra, no domina).

**Siembras y pendientes que caen en la Parte III:**

| # | Siembra | Estado | Condiciones |
|---|---|---|---|
| P1 | **Anya en el Monarch** | CANON DEL AUTOR (2026-09-26, ficha `02_Characters/Anya_Voronina.md`, § "Libro I — Anya en el Monarch"); **capítulo PENDIENTE (diseño: 36–37)** | Anya, rubia, llega al Monarch buscando a Kal; él está detrás de la barra arreglando una máquina de hielo, siente un escalofrío y se esconde por reflejo; Chiara lo ve de lejos y levanta una ceja. Anya lo llama "Kal" y luego "Ojos azules"; Chiara registra el apodo y el nerviosismo de Kal. **Regla:** Chiara conecta puntos **por la conducta de Kal**, no porque Anya insinúe nada ("no hay celos, hay información"; Kal administrando). Pendientes del autor: capítulo exacto, la línea de Anya que deja abierta la deuda, qué le dice Kal a Chiara después. AUDIT diseña (sin prosa); E4 pregunta; E9 escribe sólo si el autor lo aprueba |
| P2 | **Casi-confesión del 36** (hilo A) | DISEÑO | Como en el 20, 25 y 31: si ya existe un silencio donde uno elige una verdad más chica, se protege; si no, sólo un gesto o un silencio, sin línea nueva |
| P3 | **Bonnie y Mei-Lin como amigas** | Laguna (evaluación de arco) | Falta un gesto de amistad entre ellas, no sólo de trabajo. Sólo evaluar si 37–39 ya lo tienen; proponer, no escribir, salvo aprobación. No empujar el Libro II |
| P4 | **Penthouse o loft como pregunta** y **loft como hogar vivido** | Implícito | Que se lea como pregunta antes del 42 y que 36–43 muestren rutina doméstica. Sólo evaluar y proteger lo que ya exista |
| — | Ya aplicado, **proteger**: ritual del *Ciao* (36 llamada de la noche; 41 "Ciao, bella" / "Ciao"; 42 "Ciao, tesoro" y la mano de Kal quieta en la manija; 43 los labios sin sonido "en el acento malo de siempre"); Crowe en el 37 (cuota subida a la ferretería "por la competencia"); cocaína en el 37 ("La muevo; no la vendo. Y en la Almendra, nunca."); rimas 14↔44 (buzón sin mensaje) y 24↔44 (las puertas de Chiara); la Beretta del 44 ("llevaba ahí desde hacía años", sembrada en el 31); la moto paga en el 42 sólo por conducta | BORRADOR | No podar. Son pagos del Libro I o siembras del Libro II |
| — | "Kal cree que el corral fue por su pasado" / Chiara cree que fue el Consorzio (38) | PENDIENTE (toca H12) | No resolver aquí. Si el 38 lo roza, se reporta |
| — | No sembrar: la muerte de Mei-Lin, la de Tommaso, la de Héctor, el incendio, el collar "Retorna a casa", la vela por Kal, la liberación de Kal | — | — |

**Saldo de palabras de partida:** Partes I y II dejan **≈ +2,260** (ver `Audit_Caps_26-34_Parte_II.md`, § 9 parte 5). Lo que libere la Parte III es margen adicional, no meta. Anya (P1) no tiene rango fijado; E1 lo estima.

**Housekeeping de la Parte III (dictamen):** sincronizar títulos 36–38 (la prosa del 37 y el 38 aún dice "título provisional" en el encabezado: **eso es prosa impresa**, se corrige en SURGERY si el autor confirma los títulos); eliminar referencias a Parte IV dentro del Libro I; trasladar documentalmente el Cap. 45 a *Sombras de Poder*; actualizar `00_Plan_Cierre_Parte_III.md` (tabla con "45 (IV.1)", "Parte III termina en oscuridad y Parte IV abre con la luz": ahora la luz y "Ciao, bella" están dentro del 44 y el 45 abre el Libro II; ya tiene una nota parcial en la l. 13); actualizar `00_Book_Map.md` (premisa vieja: "ascenso hasta imperio", "San Aurelio no puede moverse sin ellos"; el Libro I es encuentro + construcción + primera prueba); retirar la vela del 38; Stella como canon o cambio de nombre; metadata del origen de la Romanée-Conti; POV del 36 en metadata; firma de Bonnie. Heredado de la Parte II (sólo si el autor ya decidió; si no, se deja): `00_Front_Matter/00_Nota_Editorial.md` l. 19 ("Part 02 - La Construccion").

---

## Etapa 1 — AUDIT de los Caps. 35, 36 y 37, y diseño de Anya

**Lee:** los Caps. 35, 36 y 37 completos. Por búsqueda: la carta del yate en 37 y 38; "Romanée", "sangre", "lodo" en 36–44 y en el Libro II (¿se cobra el origen?); el infarto de Héctor en la Parte I y su muerte en `01_Timeline/`; "Stella" en fichas e Hitos; H16 en `06_Relationships/Hitos.md`; la ficha de Anya (§ Libro I y § F4) y su voz si existe en `12_Craft_Policies/voice/`; "Monarch", "máquina de hielo", "barra" en 36–38; Bonnie en 37 (firma).
**Hace:**
- Crea el mapa con cabecera, tabla "Estado de etapas" (E1–E9) y las palabras y finales de línea de 35–37 para el `git diff --stat` de E5.
- Añade §0–§5 para 35, 36 y 37 (§0 diagnóstico, §1 candidatos por categoría con numeración continua A/B/C, §2 prolepsis y POV, §3 función por movimiento, §4 protegido y siembras, §5 lo que no es de microedición).
- **§ Cronología 35–37:** dónde cae la coda de las invitaciones; evalúa las tres opciones del dictamen con la frase ancla de inserción de cada una y lo que obliga a cambiar en el 37. Recomienda una.
- **§ El 36:** inventario de incidentes antes de la llave, con qué paga cada uno después (búsqueda) y qué se compacta; Héctor; sangre y lodo; POV y metadata; Stella.
- **P1, Anya:** capítulo y punto de inserción (línea y frase ancla), POV (la regla exige que Chiara vea la conducta de Kal: probablemente POV Chiara), cómo entra el Monarch en ese capítulo, la línea de Anya que deja abierta la deuda (dos o tres opciones), qué le dice Kal a Chiara después (dos o tres opciones, incluida "nada"), costo estimado. **Sin escribir prosa.**
- **P2:** ¿ya existe la casi-confesión en el 36? Si no, dónde cabe el silencio.
- § Decisiones (borrador) con numeración D1…

**No hace:** tocar prosa.
**Cierra:** estado E1 = hecha, más el checkpoint.

## Etapa 2 — AUDIT del Cap. 38

**Lee:** del mapa, la tabla de estado y § Decisiones (borrador). El Cap. 38 completo (es largo: leerlo por bloques si hace falta, pero entero antes de clasificar). Por búsqueda: `04_Concepts/Fe_y_Velas.md`; Blake en la Parte I y en el Libro II; "piano", "Träumerei", "ROMA", "AMOR" en 37–44; H13 en Hitos; la bala y el pañuelo en 38–44 y el Libro II; Marisol "enamorad" en 38 y 42; Bonnie en 37, 38 y 41 (firma); Fabrizio y Tommaso en 41–44 y en el Libro II.
**Hace:**
- Añade §0–§5 para el 38, con **§3 por movimiento** (día previo, llegada, invitados, Blake, proa, piano, ROMA → AMOR, H13 y flashback, bala, Palermo, aeropuerto, Marisol): qué hace cada uno, qué se poda y cuánto.
- **§ La vela:** before/after propuesto (retirar; Santa Lucía y la misa se quedan).
- **§ Bonnie:** los tres beats de la firma, cuál se varía y con qué conducta (de la lista del dictamen).
- Mapea, sin decidir, los pendientes del autor en el 38 (`PENDING.md`: "Y tú eres mi gente", Blake con el capitán, yate/piano, coche de Sam, Marisol–Kenji, "Sra."), y la sospecha sobre el corral.
- Estima el total de la poda con y sin los candidatos dudosos. Si el 38 no baja sin dañar inviolables, se dice.
- Suma decisiones a § Decisiones (borrador).

**No hace:** tocar prosa.
**Cierra:** estado E2 = hecha, más el checkpoint.

## Etapa 3 — AUDIT de los Caps. 39, 40 y 41

**Lee:** del mapa, la tabla de estado, §4 del 38 y § Decisiones (borrador). Los Caps. 39, 40 y 41 completos. Por búsqueda: La Mesa, Valenti, Livia, Ettore y Alessio en el Libro II; "Mecánico"; Bonnie y Mei-Lin en el Libro II (para no sembrar de más); Matteo como anomalía documental; Volpi.
**Hace:**
- Añade §0–§5 para 39, 40 y 41. El 39: sólo continuidad. El 40: la pregunta del 10–15 % en llegada, casa, cata y cortesía de La Mesa, protegiendo "¿Y usted qué es, señor Mercer?" / "—Mecánico.". El 41: cada línea que empuje a Bonnie hacia confidente íntima, y la firma.
- **P3:** ¿37–39 ya tienen un gesto de amistad entre Bonnie y Mei-Lin? Si no, dónde cabría, sin escribirlo.
- Suma decisiones a § Decisiones (borrador).

**No hace:** tocar prosa.
**Cierra:** estado E3 = hecha, más el checkpoint.

## Etapa 4 — AUDIT de los Caps. 42, 43 y 44, consolidación y preguntas

**Lee:** del mapa, la tabla de estado, §3 de cada capítulo y § Decisiones (borrador). Los Caps. 42, 43 y 44 completos. Por búsqueda: las apariciones del ritual del *Ciao* en 35–44; los pagos de la Parte I en el 44 (buzón, abogados, Beretta, loft).
**Hace:**
- Añade §0–§5 para 42, 43 y 44. Proteger es el objetivo: sólo continuidad, prolepsis (§L), POV y glosas evidentes. El 43 no crece; el 44 no explica.
- **Ritual del *Ciao*** en 35–44: resultado de la búsqueda contra la tabla de la evaluación de arco (36, 41, 42, 43). Si algo choca, se reporta.
- **P4:** penthouse o loft como pregunta y rutina doméstica en 36–43: qué existe y se protege.
- **§ Metadata de 35–44:** tabla de lo que se sanea en cada SURGERY (títulos, POV, Stella, Romanée-Conti, referencias a Parte IV y al 45).
- **§ Balance de palabras de la Parte III:** lo que libera cada capítulo, lo que cuestan P1–P4 y el saldo final, partiendo de ≈ +2,260.
- Convierte el borrador en **§ Decisiones que necesito**: preguntas abiertas numeradas (Q1…) con recomendación, más la tabla de **vetos libres** (lo que se aplica si el autor no dice nada). Como mínimo: la coda del 35, el alcance de la poda del 36 (y Héctor), el paquete de la poda del 38, la vela, Stella, los títulos 36–38, la firma de Bonnie, **Anya sí o no y con qué paquete**, P2–P4 y los pendientes del 38 que el autor quiera resolver ahora. **Le pregunta todo junto al autor** y, cuando responda, **anota sus respuestas en el mapa**, con fecha.

**No hace:** tocar prosa.
**Cierra:** estado E4 = hecha, con las decisiones registradas, más el checkpoint.

## Etapa 5 — SURGERY de los Caps. 35, 36 y 37

**Lee:** del mapa, la tabla de estado, § Decisiones (respuestas), § Cronología 35–37, § El 36 y §1 y §4 de esos capítulos. Los tres capítulos completos.
**Hace:**
- Antes de editar, comprueba con `git diff --stat` que los tres coinciden con el estado auditado. Si algo cambió, se detiene y avisa.
- Aplica lo aprobado: la reubicación de la coda del 35 (y lo que obligue en el 36 o el 37), la compactación del 36, lo del 37. Si la reubicación deja una costura, se lee la costura entera.
- **Anya (P1):** no la escribe. Marca en el mapa el punto exacto de inserción (línea y frase ancla), porque la cirugía puede mover líneas.
- Sanea la **metadata** de 35–37 y añade nota de cirugía en su línea de Estado (siguen BORRADOR).
- Registra en el mapa **§9 Resultado (parte 1)**: before/after, categoría, qué ya hacía la escena y qué conserva, palabras antes y después. Verifica finales de línea.

**Cierra:** estado E5 = hecha, más el checkpoint.

## Etapa 6 — SURGERY del Cap. 38

**Lee:** del mapa, la tabla de estado, § Decisiones y §1, §3 y §4 del 38, § La vela y § Bonnie. El 38 completo.
**Hace:**
- `git diff --stat` como en E5.
- Aplica lo aprobado **movimiento por movimiento**, con el registro completo, sin tocar los inviolables, y lee las costuras enteras al terminar. Si un corte rompe un pago de 39–44 o del Libro II, se conserva y se anota.
- La vela y la variación de la firma de Bonnie que caiga en el 38.
- Metadata y nota de cirugía (sigue BORRADOR).
- Añade al mapa **§9 Resultado (parte 2)**.
- **Si el contexto se llena:** partir en "E6a, hasta el piano" y "E6b, de ROMA al final" (ver "Si algo sale mal").

**Cierra:** estado E6 = hecha, más el checkpoint.

## Etapa 7 — SURGERY de los Caps. 39, 40 y 41

**Lee:** del mapa, la tabla de estado, § Decisiones y §1 y §4 del 39, 40 y 41. Los tres capítulos completos.
**Hace:**
- `git diff --stat` como en E5.
- Aplica lo aprobado: la poda ligera del 40, Bonnie en el 41 (confidencia y firma), la continuidad del 39. P3 sólo si se aprobó y el autor pidió que lo escriba el agente.
- Metadata y nota de cirugía en 39–41 (siguen BORRADOR). Añade al mapa **§9 Resultado (parte 3)**.

**Cierra:** estado E7 = hecha, más el checkpoint.

## Etapa 8 — SURGERY de los Caps. 42, 43 y 44, y housekeeping documental

**Lee:** del mapa, la tabla de estado, § Decisiones, § Metadata de 35–44 y §1 y §4 del 42, 43 y 44. Los tres capítulos completos. Para el housekeeping, **sólo por búsqueda**: "IV.1", "Parte IV" y "45" en `00_Plan_Cierre_Parte_III.md`, `00_Book_Map.md`, `01_Timeline/` e Hitos; "imperio" y "no puede moverse sin ellos" en el Book Map; "provisional" en 35–38 y en el Book Map; "vela" en Hitos y fichas de Chiara.
**Hace:**
- `git diff --stat` como en E5. Aplica lo aprobado para 42–44 (mínimo), con nota de cirugía (siguen BORRADOR).
- **Housekeeping documental** (sin prosa): corrige, con Edit puntual, las referencias viejas de la lista del dictamen (Plan de cierre, Book Map, Cap. 45 al Libro II, Parte IV, títulos). Cuando haya contradicción de canon y no de simple desfase, **no sobrescribe**: la anota en el mapa para el autor.
- Añade al mapa **§9 Resultado (parte 4)** y la lista de housekeeping hecho y pendiente.

**Cierra:** estado E8 = hecha, más el checkpoint.

## Etapa 9 — Escena de Anya (si se aprobó) y registro final

**Aviso de rol:** escribir la escena nueva es redacción, no microedición. Se hace aquí sólo si el autor la aprobó en E4, y queda **BORRADOR/DISEÑO hasta que la lea el autor.** Si no se aprobó, esta etapa es sólo el registro.
**Lee:** del mapa, la tabla de estado, § Decisiones (P1) y el punto de inserción. Sólo el capítulo que recibe a Anya, completo. Por búsqueda: `02_Characters/Anya_Voronina.md`, su voz en `12_Craft_Policies/voice/` si existe, `Kal_Mercer.md` y `Chiara_Bellandi.md` de voz, el Monarch en `05_Locations/`, y lo que F4 necesita de esta escena en `01_Timeline/03_Libro_02_Sombras_De_Poder.md`.
**Hace:**
1. Si se aprobó: escribe la escena de Anya en el punto marcado, con lo aprobado en § Decisiones. Sin glosa, sin prolepsis de F4, sin explicar lo que Chiara deduce. Mide las palabras y sanea la metadata del capítulo.
2. **Registro compartido** (regla común 7):
   - en el dictamen de la Parte III, un bloque **AVANCE DE LA EJECUCIÓN** al inicio (como el de las Partes I y II) y la lista de housekeeping marcada;
   - en la evaluación de arco, P1–P4 como aplicadas o resueltas, y el estado del ritual del *Ciao* y las rimas;
   - en la ficha de Anya, el capítulo y las líneas, si se escribió; en `PENDING.md`, retirar lo resuelto del 38 y de los títulos;
   - una línea en `CURRENT_BRIEF.md`, una en `log.md` y una en `INDEX.md` (enlace al mapa);
   - la entrada de los capítulos operados en el Book Map.
3. Cierra el mapa con la **autocrítica** (MICROEDICION §F) y el saldo final de palabras del Libro I.

**Cierra:** estado E9 = hecha. Reporta al autor qué debe leer (la coda del 35 reubicada, el 36 compactado, el 38 podado, la escena de Anya si existe y cada línea nueva del agente), recuerda que el cierre de estado (CLOSE) y la regeneración del EPUB quedan para cuando él los pida, y agrega el checkpoint.

---

## Si algo sale mal

- **Contexto al límite a mitad de una etapa:** guarda en el mapa lo hecho, marca la etapa como "parcial: hecho X, falta Y" y detente. La siguiente sesión retoma desde ahí. En E2 y E6 (el 38) es lo más probable: se puede partir en "a" y "b".
- **Aparece un problema estructural no previsto:** se reporta y no se opera (skill, "Cuándo se activa").
- **El autor cambia una decisión entre etapas:** se anota en § Decisiones con la fecha, y manda la versión más reciente.
- **Un capítulo cambió fuera del encargo** (el `git diff --stat` no coincide): detenerse y avisar; no reauditar por cuenta propia.
