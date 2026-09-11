# Microedición

Procedimiento operativo para intervenir prosa ya escrita y ya autorizada para edición. No decide qué se puede tocar — eso lo fija [[12_Craft_Policies/editorial/DO_NOT_TOUCH]] — ni qué se busca — eso lo fija [[12_Craft_Policies/editorial/EDITORIAL_POLICY]]. Este documento es agnóstico al agente: sirve igual para Claude, Codex o un editor humano.

Los tres modos de esta sección (AUDIT, SURGERY, VERIFY) diagnostican o intervienen prosa. Certificar si un capítulo ya está maduro para presentarse al autor como terminado es una pregunta distinta — eso es el workflow CLOSE, definido en [[12_Craft_Policies/CHAPTER_LIFECYCLE]]. CLOSE pertenece al ciclo de vida del capítulo, no a la microedición.

## A. Modos de trabajo

Toda tarea de microedición declara uno de tres modos antes de empezar.

### AUDIT

No modifica prosa. Objetivo: detectar, comparar, clasificar, priorizar y proteger deliberadamente.

Salida esperada:

- mapa de hallazgos (dónde está cada candidato y por qué se marcó);
- candidatos a intervención, con categoría (ver sección C);
- casos evaluados y protegidos (no solo los cortados);
- riesgos o zonas dudosas para decisión del autor.

### SURGERY

Puede modificar prosa, únicamente dentro del ámbito autorizado por el encargo. Objetivo: ejecutar intervenciones quirúrgicas puntuales, no una reescritura.

Toda intervención de SURGERY debe registrar:

- **before/after** exacto del fragmento;
- **categoría** (sección C);
- **razón** del corte, compresión o reformulación;
- **qué ya hacía la escena** sin esa frase (qué información, efecto o gesto la volvía prescindible);
- **qué conserva la nueva versión** (qué función seguía viva y no se perdió).

### VERIFY

No abre una nueva ronda editorial general. Evalúa una cirugía ya realizada — propia o de otro agente — contra su propio objetivo declarado.

Preguntas obligatorias:

- ¿se perdió información?
- ¿se perdió voz?
- ¿se rompió un callback o eco posterior?
- ¿se tocó una semilla o siembra reservada para más adelante?
- ¿se eliminó valor no informativo (ver [[12_Craft_Policies/editorial/EDITORIAL_POLICY|EDITORIAL_POLICY]] sección B) sin haberlo evaluado?
- ¿quedó una costura (transición, referente o ritmo que delata el corte)?
- ¿debe restaurarse algo?

VERIFY puede recomendar restaurar una intervención de SURGERY. No inicia por su cuenta una nueva pasada de candidatos nuevos.

## B. Lectura antes de editar

Cuando el encargo compara varias apariciones de un patrón o abarca varios capítulos, se lee primero **todo** el ámbito autorizado antes de tocar una sola línea. No se corrige la primera coincidencia encontrada sin conocer las demás — la primera aparición de un patrón puede ser justo la que hay que proteger porque las siguientes son las repeticiones.

## C. Clasificación de candidatos

Categorías mínimas. No todas son categorías de corte: algunas existen para nombrar por qué algo se protege.

**Categorías que suelen habilitar intervención:**

- **GLOSA** — el narrador explica un efecto que la acción o el diálogo ya dejaron claro.
- **TIC** — una construcción se repite sin variar de función.
- **REPETICIÓN LEXICAL** — misma palabra o frase exacta reaparece cerca.
- **REPETICIÓN SINTÁCTICA** — misma forma de frase reaparece con otro contenido.
- **REPETICIÓN FUNCIONAL** — dos pasajes distintos cumplen el mismo trabajo narrativo.
- **COMPETENCIA EXPLICADA** — se certifica una habilidad o acierto ya demostrado en escena.
- **EMOCIÓN EXPLICADA** — se nombra un sentimiento que la imagen o el gesto anterior ya mostraron.
- **INTENSIFICADOR** — refuerzo que no agrega una medida, un riesgo o una segunda lectura.
- **PRESAGIO GARANTIZADO** — una intuición se resuelve con certeza que el personaje no podía tener.
- **CONOCIMIENTO CORPORAL INJUSTIFICADO** — una reacción física se convierte en diagnóstico o dato objetivo.

**Categorías de protección (no se cortan por defecto):**

- **VALOR NO INFORMATIVO** — la frase no aporta dato nuevo pero sostiene voz, ritmo o tema.
- **INTERIORIDAD** — revela algo que solo el punto de vista puede entregar.
- **FIRMA DE VOZ** — patrón deliberado de una ficha de `voice/`, aunque se repita.
- **DUDOSA — CONSERVAR** — no se resolvió con certeza; se protege por defecto y se documenta la duda para el autor.

Una misma frase puede evaluarse bajo dos categorías (por ejemplo, candidata a GLOSA pero protegida como INTERIORIDAD). La clasificación final es la que gana después de aplicar el árbol de decisión.

## D. Árbol de decisión

Antes de modificar cualquier candidato, en orden:

1. **¿Cambia canon, estructura, motivación, consecuencia o revelación?**
   Sí → detener, es asunto de [[12_Craft_Policies/editorial/DO_NOT_TOUCH|DO_NOT_TOUCH]] o de cirugía estructural, no de microedición.
   No → continuar.

2. **¿La acción o el diálogo ya comunican esto?**
   No → proteger (probablemente es información nueva, no candidato real).
   Sí → continuar.

3. **¿La frase añade información invisible (interioridad, ver EDITORIAL_POLICY sección E)?**
   Sí → proteger.
   No → continuar.

4. **¿Tiene valor no informativo alto (voz, ritmo, tema)?**
   Sí → proteger, o marcar DUDOSA — CONSERVAR si el valor no es evidente.
   No → continuar: es candidata real.

5. **¿Puede resolverse cortando sin dejar costura?**
   Sí → cortar.
   No → continuar.

6. **¿Puede comprimirse sin perder la función que sí sobrevive?**
   Sí → comprimir.
   No → continuar.

7. **Solo entonces, reformular** — y solo si la función necesita sobrevivir pero la formulación concreta es el problema. No sustituir un tic por un sinónimo del mismo tic.

## E. Protecciones deliberadas

Toda auditoría o cirugía de alcance amplio registra ejemplos de material evaluado y conservado, no solo lo cortado. El objetivo es que quede claro que un patrón "no se vio y decidió protegerse", no que "no se vio porque no se buscó".

No hay un número fijo universal de protecciones a documentar — el alcance del encargo define cuántas son razonables. Un encargo sobre tres capítulos no rinde la misma cantidad que uno sobre un solo párrafo.

## F. Autocrítica obligatoria

Toda tarea de microedición sustantiva (AUDIT amplio o SURGERY con más de una intervención) cierra con una autocrítica que responda:

- ¿qué cambio genera más dudas?
- ¿cuál fue el cambio más agresivo?
- ¿hubo algún caso que inicialmente pareció corte y terminó protegido? ¿por qué cambió el veredicto?
- ¿existe riesgo de haber esterilizado voz?
- ¿existe riesgo de haber racionalizado interioridad (convertido percepción en explicación)?
- ¿existe riesgo de haber dejado la prosa más genérica que antes?

## G. Sin segunda pasada automática

Al terminar el encargo, detenerse. No se aprovecha que el archivo está abierto para iniciar otra ronda de auditoría o corte. Una nueva pasada necesita nuevo ámbito autorizado por el autor, no la inercia de la sesión.
