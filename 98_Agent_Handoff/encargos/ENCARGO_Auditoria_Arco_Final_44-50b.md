# ENCARGO — Auditoría del arco final del Libro I (Caps. 44–50b), por etapas

**Creado:** 2026-10-02, a petición del autor, el mismo día en que se redactaron 44–49 y 50b y se reescribió el 50.
**Por qué por etapas:** el arco suma unas 30,900 palabras, todo en BORRADOR y recién escrito. Ninguna sesión debe cargar los ocho capítulos, sus cruces y la cirugía a la vez. **Cada etapa se ejecuta en una sesión limpia** (terminal nueva o `/clear`) y no depende del chat anterior: lo que necesita está en este encargo y en el mapa.
**Terminal:** una sola. Las etapas son secuenciales.

**Cómo se invoca cada etapa** (el autor pega esto):

> Ejecuta la etapa N de `98_Agent_Handoff/encargos/ENCARGO_Auditoria_Arco_Final_44-50b.md`.

**Mapa de la auditoría** (lo crea E0): `13_Auditorias/Book_01_Mascaras_De_Cristal/Audit_Caps_44-50b_Arco_Final.md`. Formato como `Audit_Caps_35-44_Parte_III.md` (tabla de estado, §0–§5 por capítulo, § Decisiones, § 9 Resultado), **sin leerlo entero**: basta con su tabla de estado, una tabla de §1 y una de §9.

**Orden lógico (recomendación aceptada por el autor):** primero el oficio, revisando el arco como bloque (E1–E3). Luego el autor decide y se corrige lo estructural (E4–E5). Después el autor lee. La microedición va al final, capítulo por capítulo (E6–E8). Pulir frases antes de cerrar la estructura es trabajo que se pierde.

---

## Reglas comunes a todas las etapas

1. **Lectura mínima al arrancar:** este encargo completo; la tabla **"Estado de etapas"** del mapa y sólo las secciones que la etapa indique. **No leer** START_HERE, el brief completo ni `log.md`.
2. **Verificar la etapa anterior:** si la tabla no la marca como HECHA (o la puerta del autor no está marcada), detenerse y avisar.
3. **Capítulos:** leer completos sólo los de la etapa. Los cruces se hacen **con búsquedas** (`rg`/Grep): `06_Relationships/`, `01_Timeline/`, `02_Characters/`, `03_Factions/`, `05_Locations/`, Book Maps, Caps. 1–43 y Libro II. Antes de proponer cortar un objeto, frase, gesto o plan, **buscar sus pagos** en el resto del arco y en *Sombras de Poder*.
4. **Canon:** el plan [[11_Books/Book_01_Mascaras_De_Cristal/00_Plan_Arco_Final_Sin_Kal]] marca qué es CANON DEL AUTOR y qué es DISEÑO. Lo canon no se reinterpreta ni se "mejora" (la línea del Lancia y la columna del 50, "Ciao, bella", Halbrook sin nombre ni diálogo en el 50b, la deuda abierta con Dario, la negativa de Valenti y la oferta del Monarch). Lo DISEÑO del agente sí se discute.
5. **Estado:** los ocho siguen en **BORRADOR**. Ninguna etapa los sube de estado. CLOSE ([[12_Craft_Policies/CHAPTER_LIFECYCLE]]) sólo si el autor lo pide aparte; TERMINADO sólo lo declara él.
6. **Prosa:** E0–E3 no tocan prosa (AUDIT). E4–E5 sólo aplican lo aprobado en § Decisiones. E6–E8 siguen la skill `editorial-surgery`.
7. **Finales de línea:** el 49 está en CRLF; los demás, en LF. Verificar con `file` antes de editar y conservarlos.
8. **Cierre de cada etapa:** actualizar la fila de la tabla de estado (HECHA, fecha y una nota de una línea). El registro compartido (brief, log, INDEX) se toca sólo en E5 y E8.

## Políticas por eje (qué se audita con qué)

| Eje | Política | Gate de [[12_Craft_Policies/CHAPTER_LIFECYCLE]] |
|---|---|---|
| Función, posición en el arco y consecuencia | [[12_Craft_Policies/Redaccion_De_Capitulos]], plan del arco | A |
| Puesta en escena | `12_Craft_Policies/staging_rules/` (01–04 y WATCHLIST) | A / C |
| Revelaciones y su orden | [[12_Craft_Policies/revelations/Book_01_Mascaras_De_Cristal]], `revelations/SAGA_LEVEL.md` | B |
| Hitos | [[12_Craft_Policies/milestones/INDEX]], `06_Relationships/Hitos.md` | B |
| Voz por personaje | `12_Craft_Policies/voice/` (Chiara, Héctor, Lucía, Mabel, Marisol, Nadir, Dario y Kal) | C |
| Diálogo | `12_Craft_Policies/dialogue_rules/` (01–04 y WATCHLIST) | C |
| Tono | `12_Craft_Policies/tonal_calibration/` | C |
| Editorial (glosa, tics, redundancia, §L prolepsis) | `12_Craft_Policies/editorial/` (EDITORIAL_POLICY, MICROEDICION, DO_NOT_TOUCH) | D |
| Dependencias, siembras y cascada | plan del arco (§ Siembras, § Cascada pendiente) | E |
| Higiene y metadata | — | F |

## Datos del arco (para no releer el plan entero)

| Cap. | Archivo | Días | Núcleo | Palabras* |
|---|---|---|---|---|
| 44 | `44_Jurisdiccion.md` | D5–D6 | Institución: abogados, Krane, Connors, Rowe, Lucía | 2,464 |
| 45 | `45_Ropa_Limpia.md` | D6–D8 | Su red: Kenji, Mabel, Bonnie/Mei-Lin, prueba de vida (lavandería), Torre Norte | 4,776 |
| 46 | `46_Llaves.md` | D8–D9 | Los de Kal: El Patio, Nadir y las llaves, Garrett, Marisol | 3,707 |
| 47 | `47_Intereses.md` | D9–D10 | Las armas de Dario: intereses, "A él no", cuenta abierta, fecha del traslado | 4,603 |
| 48 | `48_Su_Nombre.md` | D10–D12 | El sur: Rafe, Bravos, Mabel de puente, el nombre como precio, Mei-Lin muda | 4,087 |
| 49 | `49_Enfrente.md` | D12–D13 | Il Consigliere: Valenti niega al hombre y ofrece la corona | 3,460 |
| 50 | `50_A_Oscuras.md` | D13 | Asalto fallido, apagón, columna canon, "Ciao, bella" | 5,165 |
| 50b | `50b_La_Tierra_Bajo_Sus_Botas.md` | D14, alba | Halbrook llega (narrador externo) | 2,211 |

*`wc -w` con metadata. E0 mide la prosa sin metadata. Ruta: `11_Books/Book_01_Mascaras_De_Cristal/Part_03_Ardizzone/`.

**Ya hecho:** [[13_Auditorias/Book_01_Mascaras_De_Cristal/Audit_Cap_44_Jurisdiccion]] (AUDIT del 44, 2026-10-02). C1 está resuelto. **C2 (Krane penalista) falta propagarlo al 45 (l. 65), al 46 (l. 62, 68–70) y al 47 (l. 198).** C3 (el Cap. 19 dice "fiscal del distrito") queda fuera de este arco, pero se registra en § Decisiones. C4: verificar que el 50 reescrito ya no duplica el material del 44.

**Riesgos a vigilar en el bloque:** cuatro capítulos seguidos de 3,500 a 4,800 palabras (ritmo); la misma escena repetida (Chiara pide, alguien niega, Chiara paga) sin escalar; Chiara evita el loft en todo el arco (verificarlo); las siembras de Garrett (46, 47 y 50); Mei-Lin muda en el 48; las fechas D5–D14 contra Los_Tres_Dias y el timeline.

---

## Etapa 0 — Métricas deterministas y creación del mapa

**Lee:** `tools/editorial/README.md` (sección de ejecución) y `tools/editorial/pilot_01_10.json` como modelo de manifiesto.
- Crea `tools/editorial/arco_final_44_50b.json` (modo `audit_only`, los ocho capítulos en orden) y corre `editorial_audit.py` con salida en `tools/editorial/reports/ARCO_FINAL_44_50b/`.
- Crea el mapa con la tabla de estado (E0–E8 y las dos puertas del autor), las palabras de prosa por capítulo, los finales de línea y el último commit.
- Resume en el mapa (§ Métricas) sólo las alertas `high` y `medium` por capítulo, con una línea cada una. Una alerta no es un error: sirve para priorizar la lectura de E1–E3.
**No hace:** leer capítulos completos ni proponer cambios.

## Etapa 1 — AUDIT de oficio de 44, 45 y 46

**Lee:** del mapa, la tabla de estado y § Métricas de 44–46. El audit del 44 existente (no repetirlo: validarlo y completarlo con los ejes que no cubrió). Los Caps. 45 y 46 completos y el 44 completo. Las fichas de voz de los personajes con diálogo. Por búsqueda: Krane, Rivers, Connors, Rowe en 44–50; "loft" en 44–50; Kenji, Bonnie y Mei-Lin en los Caps. 1–43; Walt, Danny y Garrett en Parte III.
- §0–§5 por capítulo, según los ejes de la tabla de políticas.
- Propagación de C2: anotar las líneas exactas del 45 y el 46 que hay que corregir.
- Abre § Decisiones (borrador), numeradas D1…
**No hace:** tocar prosa.

## Etapa 2 — AUDIT de oficio de 47, 48 y 49

**Lee:** del mapa, la tabla de estado, §0 de 44–46 y § Decisiones. Los Caps. 47, 48 y 49 completos. Por búsqueda: las armas largas en los Caps. 39 y 43 (qué se pactó y quién se quedó con ellas); Rafe y Bravos en el 13 y en Parte II/III; Valenti, Il Consorzio y Mei-Lin en el Libro I y en `01_Timeline/03_Libro_02_Sombras_De_Poder.md`; "Monarch" y "dueña" en el Libro II.
- §0–§5 por capítulo. C2 en el 47 (l. 198).
- Revisar que el patrón "pide, la niegan, paga" escale de verdad entre el 47, el 48 y el 49.
- Agrega D…
**No hace:** tocar prosa.

## Etapa 3 — AUDIT de 50 y 50b, y consolidación del arco

**Lee:** del mapa, la tabla de estado, §0 y §3 de 44–49 y § Decisiones. Los Caps. 50 y 50b completos. El ledger de revelaciones del Libro I. Por búsqueda: "Ciao" en 35–50; Halbrook en el 27 y en su ficha; el cuadro del lago en el 31 y el 33; H20 en Hitos; D5–D14 en `06_Relationships/Los_Tres_Dias.md` y `01_Timeline/02_Libro_01_Mascaras_De_Cristal.md`.
- §0–§5 de 50 y 50b. Cotejar la columna canon del 50 palabra por palabra contra el plan.
- **§ Arco** (lectura en bloque, apoyada en el mapa): tabla de días D5–D14; orden de revelaciones contra el ledger; hitos cubiertos y faltantes; voces cruzadas (¿Chiara cambia de voz del 44 al 50?); ritmo y extensión por capítulo; siembras del plan (cumplidas, rotas o faltantes); escenas o gestos repetidos entre capítulos.
- **§ Decisiones que necesito del autor:** consolidar D1…Dn en preguntas cerradas con propuesta, y separar lo estructural (va a E4–E5) de lo editorial (va a E6–E8).
**No hace:** tocar prosa.

## 🟡 Puerta del autor 1 — responder § Decisiones

El autor contesta en el mapa o en el chat. El agente de E4 marca la puerta como cumplida sólo si cada decisión estructural tiene respuesta o veto.

## Etapa 4 — Correcciones estructurales y de continuidad de 44–47

**Lee:** del mapa, la tabla de estado, § Decisiones con respuestas y §1 y §4 de 44–47. Los capítulos que se van a tocar, completos.
- `git diff --stat` antes. Aplica sólo lo aprobado (incluye la propagación de C2), con registro por cambio en § 9 Resultado (parte 1). Al terminar, lee las costuras enteras.
- Si un cambio rompe un pago del arco o del Libro II, se conserva y se anota.
**No hace:** microedición estilística.

## Etapa 5 — Correcciones estructurales de 48–50b y registro intermedio

Igual que E4 para 48, 49, 50 y 50b; § 9 Resultado (parte 2).
- Registro compartido: CURRENT_BRIEF (una línea), `log.md` (enlace), INDEX (mapa y encargo), el plan del arco (marcar lo corregido) y PENDING (lo que quedó para el autor).
- Dejar escrito para el autor qué leer: cambios de esta pasada y líneas DISEÑO del agente.

## 🟡 Puerta del autor 2 — lectura de los capítulos

El autor lee los ocho capítulos (o los que quiera) y lo indica. Sin esta puerta, E6–E8 no arrancan. Los capítulos que el autor pida rehacer salen del encargo y vuelven a redacción.

## Etapa 6 — Microedición de 44, 45 y 46

**Lee:** la skill `editorial-surgery` y sus tres políticas; del mapa, la tabla de estado, § Métricas y §1 C (glosa, tic, repetición) de 44–46. Los tres capítulos completos.
- AUDIT editorial y luego SURGERY con el veto libre del autor (como en la Parte II): sin cuotas (§J), aplicando §L (prolepsis) y DO_NOT_TOUCH. Autocrítica según MICROEDICION §F. Se registra en § 9 Resultado (parte 3).

## Etapa 7 — Microedición de 47, 48 y 49

Igual que E6, en § 9 Resultado (parte 4).

## Etapa 8 — Microedición de 50 y 50b, y registro final

Igual que E6 para 50 y 50b (el 50 tiene la columna canon: no se toca; el 50b, protegerlo, que no explique). § 9 Resultado (parte 5).
- Registro final: brief, log, INDEX, plan del arco y Book Map. **Cascada pendiente** del plan (Hitos H20, Trilogy Structure, Book Maps, ficha de Halbrook, Los_Tres_Dias, timeline y Nota Editorial): **sólo listarla** en PENDING con estado. Ejecutarla es otro encargo.
- Opcional, a petición del autor: correr de nuevo E0 para comparar métricas antes y después.
- **Encargo cerrado.** CLOSE de los capítulos, sólo si el autor lo pide.

## Si algo sale mal

- Si una etapa se corta a medias, la tabla de estado queda EN CURSO con una nota de hasta dónde llegó. La siguiente sesión retoma esa etapa, no la siguiente.
- Si aparece un problema estructural en E6–E8, se reporta como BLOCKED (gate A) y no se intenta arreglar con microedición.
- Si el autor reescribe un capítulo entre etapas, su AUDIT se invalida: se marca y se repite.
