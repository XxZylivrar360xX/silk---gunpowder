# ENCARGO — Auditoría editorial Parte I, lote B (Caps. 8 y 18–24), por etapas

**Creado:** 2026-09-27, a petición del autor. **Terminal:** B, en paralelo con la terminal A (Caps. 4, 6, 7, 11 y 13). **No tocar los capítulos de A.**
**Por qué por etapas:** para que ninguna sesión cargue los ocho capítulos, sus cruces y la cirugía a la vez. **Cada etapa se ejecuta en una sesión limpia** (terminal nueva o `/clear`) y no depende del chat anterior: todo lo que necesita está en este encargo y en el mapa.

**Cómo se invoca cada etapa** (el autor pega esto):

> Ejecuta la etapa N de `98_Agent_Handoff/ENCARGO_Auditoria_Parte_I_Lote_B.md`.

---

## Reglas comunes a todas las etapas

1. **Lectura mínima al arrancar:** este encargo completo; la tabla **"Estado de etapas"** del mapa (`13_Auditorias/Book_01_Seda_y_Polvora/Audit_Caps_08_18-24_Lote_B.md`), si ya existe, y sólo las secciones del mapa que la etapa indique; la skill `editorial-surgery` y sus tres políticas (EDITORIAL_POLICY, DO_NOT_TOUCH y MICROEDICION). **No leer** START_HERE, el brief completo, `log.md` ni el dictamen entero. Del dictamen sólo hacen falta la matriz y la adenda B, que ya están resumidas aquí abajo.
2. **Verificar la etapa anterior:** si la tabla de estado no marca la etapa previa como hecha, detenerse y avisar al autor.
3. **Capítulos:** leer completos sólo los de la etapa en curso. Los cruces de pagos se hacen **con búsquedas** (`rg`/Grep), sin abrir archivos enteros: `06_Relationships/`, `01_Timeline/`, `02_Characters/`, `03_Factions/`, `07_Ideas/`, los Book Maps y los Caps. 26–44. Es la lección del 14 con el imán: antes de proponer cortar un objeto, frase o gesto, buscar sus pagos fuera de la Parte I.
4. **Formato:** el modelo es `13_Auditorias/Book_01_Seda_y_Polvora/Audit_Caps_15-17.md`, pero **no leerlo entero**. Basta con §1 (tablas de candidatos), §3 (función por movimiento) y §9 (registro de SURGERY con before/after).
5. **Política:** Prioridad C = protección y microedición; no hay cirugía profunda sin una causa concreta. Aplicar §L (el narrador no adelanta el futuro) y revisar saltos de POV. Palabras liberadas **sin cuotas** (§J), pero siempre medidas y con su origen.
6. **Archivos compartidos con la terminal A** (tabla de avance del dictamen, adenda B, `CURRENT_BRIEF.md`, `log.md` e `INDEX.md`): sólo se tocan en la **etapa 5**, releyéndolos justo antes, con Edit puntual y conservando los cambios ajenos. Si un script corta bloques, debe conservar los finales de línea **CRLF** (verificarlo al terminar).
7. **Al cerrar cada etapa:** actualizar la tabla "Estado de etapas" del mapa, reportar al autor en 5–8 líneas y terminar con la línea de checkpoint que sugiere `/clear` o terminal nueva. **No encadenar la etapa siguiente.**
8. **No tocar:** el EPUB; los capítulos de la terminal A; y los pendientes aparte (Natalie Keegan en el Cap. 3, el recuerdo de Palermo del 12 y las flores de la carta del 16).

---

## Datos del lote (para no releer el dictamen)

**Matriz:**

| Cap. | Archivo | Diagnóstico | Intervención | Palabras (prosa, 27-09) |
|---|---|---|---|---|
| 8 | `08_La_Carrera_De_Mascaras.md` | Muy buen cambio de terreno y confianza | LIGERA | 2,675 |
| 18 | `18_El_Dia_Nublado.md` | Centro temático de autonomía; proteger | MÍNIMA | 3,166 |
| 19 | `19_Tierra_Buena.md` | Lateral pero ahora estructuralmente útil | LIGERA | 1,639 |
| 20 | `20_El_Mirador.md` | Centro relacional; proteger | MÍNIMA | 2,260 |
| 21 | `21_El_Primer_Huesped.md` | Muy buen beat de familia elegida; housekeeping | LIGERA | 1,817 |
| 22 | `22_Causalidad.md` | Bisagra breve y eficiente | MÍNIMA | 898 |
| 23 | `23_La_Letra_Pequena.md` | Hilo legal funcional | LIGERA | 1,780 |
| 24 | `24_Bajo_Juramento.md` | Tommaso gana importancia retroactiva | LIGERA–MEDIA | 2,239 |

Todos están en `11_Books/Book_01_Seda_y_Polvora/Part_01_Dos_Mundos/`. El dictamen prohíbe tocar el corazón de *El mirador*, eliminar *Tierra buena* y convertir a Tommaso en presagio obvio de muerte.

**Siembras de la adenda B para este lote:**

| # | Siembra | Estado | Condiciones |
|---|---|---|---|
| S1 | **Nadir y la moto** (5-sexies) | APROBADO en concepto; PENDIENTE: capítulo | Nadir toma del fondo del Patio (tratos y mercancía, no cocaína) para una moto, sin avisar. Kal lo descubre por la moto frente al taller. Líneas canon: "—¿Por qué no me dijiste?" / "—Porque ibas a decir que no." / "—Iba a decir que sí." Kal repone el fondo, Nadir se lo paga en abonos y la moto se queda. Después del 17 (Nadir desobedece "Avísenme" sabiendo la regla) y antes del 25, en paralelo a la deuda con Anya. Escena nueva de no más de ~600 palabras, ya pagada con las 1,134 que liberó el 5-ter. Paga en el 42 (F1) |
| S2 | Costo del trato con Irene | DISEÑO | Nadir ausente o cansado por las rutas de la Ronda, sin explicarlo ni quejarse, una o dos veces en 17–24. Puede ir en la escena de S1 |
| S3 | Camp Alder como geografía (hilo B) | PENDIENTE: capítulo | La cerca, una sola imagen, y Kal que desvía la mirada o cambia de ruta sin decir nada. **En el 8 o en el 19**; el 20 queda descartado |
| S4 | Casi-confesión del 20 (hilo A) | DISEÑO | Uno abre la boca, piensa en el costo y elige una verdad más chica. **Sólo un silencio, sin línea nueva.** Si ya existe, se protege |
| S5 | Rima 24↔44 (hilo C) | APROBADO | Uno o dos gestos concretos de la red de Chiara (la misma llamada, el mismo favor) que el 44 pueda repetir casi textualmente. Dentro de escenas existentes |
| S6 | Matteo y Fabrizio (hilo C) | APROBADO | Una línea funcional en el **23** (una firma, una llamada, una corrección en una junta). Sin escenas nuevas. No repetir los gestos del 5 (llamada de Fabrizio) ni del 16 ("Matteo cubre el piso") |

**Proteger (ya aplicado o cobrado por otros):** "Ciao, Kal" → "Ciao, tesoro" en el 19 (adenda A); la silla verde que Héctor critica en el 18 (paga el 16); el trato de Irene vivo y la regla "Avísenme" (17 operado).
**Saldo de palabras de partida:** el 5-ter liberó 1,134. S1 cuesta ≤600, así que quedan ~530 para Irene en el 32, que pide 800–1,000.

---

## Etapa 1 — AUDIT de los Caps. 8, 18, 19 y 20

**Lee:** esos cuatro capítulos completos. Si hace falta cruzar, las fichas de voz de `12_Craft_Policies/voice/` de los personajes en juego, por búsqueda.
**Hace:**
- Crea el mapa `Audit_Caps_08_18-24_Lote_B.md` con: cabecera, tabla **"Estado de etapas"** (E1–E5), §1 candidatos por categoría, §2 prolepsis y POV, §3 función por movimiento con palabras, §4 protegido y §5 lo que no es de microedición. Todo **sólo para 8, 18, 19 y 20**.
- **Siembras de esta etapa, sólo como propuesta:**
  - **S3:** evalúa el 8 y el 19 con la imagen concreta y el lugar exacto, y recomienda uno.
  - **S4:** ¿ya existe en el 20? Si no, dónde cabe el silencio.
  - **S1 y S2:** anota si el 18, el 19 o el 20 son candidatos para la moto y por qué, sin decidir todavía.
- Deja en el mapa un **§ Decisiones (borrador)** con las preguntas de estos capítulos, **sin preguntarle todavía al autor.**

**No hace:** tocar prosa ni leer del 21 en adelante.
**Cierra:** estado E1 = hecha, más el checkpoint.

## Etapa 2 — AUDIT de los Caps. 21–24, consolidación y preguntas

**Lee:** del mapa, la tabla de estado, §3 y § Decisiones (borrador). Los Caps. 21–24 completos. El **Cap. 44** (`Part_03_Ardizzone/44_A_Oscuras.md`, ~2,270 palabras) completo, sólo para S5. El ledger de revelaciones (`12_Craft_Policies/revelations/Book_01_Seda_y_Polvora.md`), sólo la sección de Tommaso, por búsqueda.
**Hace:**
- Añade al mapa §1–§5 para 21–24, con la misma estructura de E1.
- **S5:** propone el gesto o los gestos de la red de Chiara en el 23–24 que el 44 repite, citando las líneas del 44.
- **S6:** propone la línea de Matteo o Fabrizio en el 23.
- **S1:** consolida los candidatos de todo el lote (18–24): 2 o 3 capítulos con pros y contras, una recomendación, y si el pago en el 42 lleva línea o sólo conducta. **S2:** su lugar.
- **Balance de palabras del lote:** lo que libera la poda de 8 y 18–24, lo que cuestan S1 a S6 y el saldo final para el 32.
- Convierte el borrador en **§ Decisiones que necesito**, numeradas y con recomendación. **Le pregunta todo junto al autor** y, cuando responda, **anota sus respuestas en el mapa**, en el § Decisiones.

**No hace:** tocar prosa.
**Cierra:** estado E2 = hecha, con las decisiones registradas, más el checkpoint.

## Etapa 3 — SURGERY de los Caps. 8, 18, 19 y 20

**Lee:** del mapa, la tabla de estado, § Decisiones (respuestas del autor) y §1 y §4 de esos cuatro capítulos. Los cuatro capítulos completos, porque hay que verificar las costuras.
**Hace:**
- Antes de editar, comprueba con `git diff --stat` que los cuatro coinciden con el estado auditado. Si algo cambió, se detiene y avisa.
- Aplica lo aprobado para 8, 18, 19 y 20, incluidas S3 y S4 si caen aquí. **Si la moto (S1) cae en uno de estos capítulos**, no la escribe: marca en el mapa el punto exacto de inserción (línea y frase ancla) para E5.
- Añade nota de cirugía en la cabecera de cada capítulo operado (estado conservado).
- Registra en el mapa, **§9 Resultado (parte 1)**, el before/after, la categoría y qué conserva, con las palabras antes y después por capítulo. Verifica CRLF.

**Cierra:** estado E3 = hecha, más el checkpoint.

## Etapa 4 — SURGERY de los Caps. 21–24

**Lee:** del mapa, la tabla de estado, § Decisiones y §1 y §4 de esos cuatro capítulos. Los cuatro capítulos completos.
**Hace:** lo mismo que E3, para 21–24, incluidas S5 y S6. Si S1 o S2 caen aquí, marca el punto de inserción para E5. Añade al mapa el **§9 Resultado (parte 2)**.

**Cierra:** estado E4 = hecha, más el checkpoint.

## Etapa 5 — Escena de la moto y registro final

**Aviso de rol:** escribir la escena nueva es redacción, no microedición. Se hace aquí por la adenda (escena pagada con el 5-ter) y queda **BORRADOR/DISEÑO hasta que la lea el autor.**
**Lee:** del mapa, la tabla de estado, § Decisiones (S1 y S2) y el punto de inserción. Sólo el capítulo elegido, completo. Fichas por búsqueda: `02_Characters/Nadir_Amrani.md` y `02_Characters/Kal_Mercer.md`, y las voces de `12_Craft_Policies/voice/` (Nadir y Kal). El 42, sólo por búsqueda de la escena F1, para no contradecir el pago.
**Hace:**
1. Escribe la escena de la moto (≤600 palabras) en el punto marcado, con las tres líneas canon **textuales** y S2 si se decidió que va ahí. Sin glosa del narrador y sin prolepsis. Mide las palabras.
2. **Registro compartido** (regla común 6): fila del lote B en la tabla de avance del dictamen; en la adenda B, marcar S1–S6 como aplicadas o resueltas y la decisión D1 y el hilo B de la sección D; una línea en `CURRENT_BRIEF.md`, una en `log.md` y una en `INDEX.md` (enlace al mapa). Actualizar la metadata del Book Map y la ficha de Nadir (nota de moto sembrada).
3. Cierra el mapa con la **autocrítica** (MICROEDICION §F) y el saldo final de palabras para el 32.

**Cierra:** estado E5 = hecha. Reporta al autor qué debe leer (la escena de la moto y cada línea nueva del agente) y agrega el checkpoint.

---

## Si algo sale mal

- **Contexto al límite a mitad de una etapa:** guarda en el mapa lo hecho, marca la etapa como "parcial: hecho X, falta Y" y detente. La siguiente sesión retoma desde ahí.
- **Aparece un problema estructural** (motivación rota o un arco que hay que reordenar): se reporta y no se opera (skill, "Cuándo se activa").
- **El autor cambia una decisión entre etapas:** se anota en § Decisiones con la fecha, y manda la versión más reciente.
