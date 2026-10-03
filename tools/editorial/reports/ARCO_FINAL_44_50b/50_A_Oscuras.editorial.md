# Auditoría editorial — Capítulo 50

- `editor_version`: `1.1`

> Esto es diagnóstico, no una lista de correcciones. Una alerta —incluso HIGH— sólo pide lectura humana prioritaria.

## Resumen

- Palabras: 3963
- Párrafos narrativos: 143
- Diálogo aproximado: 11.8%
- Alertas HIGH / MEDIUM / LOW / INFO: 0 / 1 / 11 / 3

## Prioridad de lectura

### HIGH

- Sin alertas.

### MEDIUM

- `LONG_DIALOGUE_INTERVENTION` · `descriptive/inventory` · línea 198: Intervención estimada en 76 palabras habladas; la longitud aislada nunca eleva a HIGH. — “—Pagué todo. Le di mi nombre a un hombre que cobraba en la banqueta desde niño. Le quedé a deber a Dario lo que él quiera, cuando él quiera, y no sé qué es. Me senté a tomar café…”

### LOW

- `GESTURE_CLUSTER_MIRAR` · `descriptive/inventory` · línea 74: El gesto «mirar» aparece agrupado en una ventana de 20 líneas. — “Chiara miró la taza. El café tenía una nata delgada que se rompía en la orilla. / Mabel miró el billete. Lo dejó donde estaba. / El Lancia estaba frío por dentro. Chiara lo encend…”
- `PHRASE_COMO_SI` · `descriptive/inventory` · línea 132: Frase vigilada: 4 ocurrencia(s) en el capítulo; revisar en contexto. — “Chiara se inclinó sobre el volante para verla por el parabrisas. No había torre. Había un rectángulo más negro que el cielo, sin una sola ventana, y detrás, muy al norte, la loma…”
- `LONG_DIALOGUE_INTERVENTION` · `descriptive/inventory` · línea 160: Intervención estimada en 41 palabras habladas; la longitud aislada nunca eleva a HIGH. — “—Señora Bellandi. El generador sólo da para la jaula y las cámaras. Los elevadores están parados. Hay dos huéspedes atorados en el de la Torre Sur, ya les hablaron los bomberos po…”
- `POSSIBLE_EDITORIAL_INSTRUCTION_LEAK` · `descriptive/inventory` · línea 170: Verbo ambiguo compatible con narración normal; revisar sólo como señal de baja confianza. — “No contó los pisos. A partir de cierto punto los descansos eran todos el mismo: el letrero verde, el número pintado en la pared de concreto, el barandal frío, el siguiente tramo.…”
- `REPEATED_NGRAM_4` · `descriptive/inventory` · línea 178: N-grama de 4 palabras repetido 3 veces en el capítulo. — “junto a la puerta”
- `LONG_DIALOGUE_INTERVENTION` · `descriptive/inventory` · línea 194: Intervención estimada en 41 palabras habladas; la longitud aislada nunca eleva a HIGH. — “—Pero eso no Te da derecho. —Levantó la vista hacia el círculo de luz en el techo—. No así. No para quitármelo como se le quita algo a una niña que se portó mal, porque se puede.…”
- `REPEATED_NGRAM_4` · `descriptive/inventory` · línea 194: N-grama de 4 palabras repetido 3 veces en el capítulo. — “el circulo de luz”
- `LONG_DIALOGUE_INTERVENTION` · `descriptive/inventory` · línea 214: Intervención estimada en 41 palabras habladas; la longitud aislada nunca eleva a HIGH. — “—Subió. Estuvo aquí, del otro lado de esa puerta, con la mano así, y no tocó, y yo estaba aquí dentro. Lo tuviste a tres metros. Y me lo dejaste ver en una pantalla, de espaldas,…”
- `NO_FUE_FUE` · `descriptive/inventory` · línea 308: Construcción «No fue X. Fue Y.»; revisar si la antítesis explica de más. — “No fue un ruido. Fue algo más simple: una forma donde un momento antes no había ninguna.”
- `DIALOGUE_INTERVENTION_MEDIAN_OUTLIER` · `descriptive/inventory` · métrica de capítulo: Outlier alto del corpus en mediana de intervención; no implica un problema.
- `DIALOGUE_PERCENT_OUTLIER` · `descriptive/inventory` · métrica de capítulo: Outlier bajo del corpus en % aproximado de diálogo; no implica un problema.

### INFO

- `CROSS_CHAPTER_PASSAGE_SIMILARITY` · `descriptive/inventory` · línea 32: Posible similitud con 48_Su_Nombre.md:63 (score 0.1233); señal experimental. — “Chiara estaba ahí desde las siete. Había llegado con el último turno de la cena, cuando la vitrina ya tenía más charolas vacías que pan, y se había sentado en el extremo de la barra con el saco puesto. Mabel le había se…”
- `PHRASE_UN_SEGUNDO_DE_MAS` · `descriptive/inventory` · línea 32: Frase vigilada: 1 ocurrencia(s) en el capítulo; revisar en contexto. — “Chiara estaba ahí desde las siete. Había llegado con el último turno de la cena, cuando la vitrina ya tenía más charolas vacías que pan, y se había sentado en el extremo de la bar…”
- `CROSS_CHAPTER_PASSAGE_SIMILARITY` · `descriptive/inventory` · línea 156: Posible similitud con 49_Enfrente.md:224 (score 0.1348); señal experimental. — “Eso fue lo primero. No la oscuridad, que con las luces de emergencia era una penumbra amarilla en la que se adivinaban las mesas y las columnas, sino el silencio de las máquinas: cuatrocientas pantallas negras, sin camp…”

## Repeticiones

- `como si`: 4 · 1.009/1,000 palabras · líneas 132, 280, 322, 322
- `un segundo de más`: 1 · 0.252/1,000 palabras · líneas 32

### N-gramas locales

- `el circulo de luz` (4 palabras): 3
- `junto a la puerta` (4 palabras): 3
- `luz del telefono` (3 palabras): 3

## Ritmo

- Oraciones aproximadas: 350
- Palabras/oración, media: 11.323
- Palabras/oración, mediana: 8.0
- Palabras/párrafo, media: 27.713
- Palabras/párrafo, mediana: 19.0
- Párrafos de una oración: 38.5%
- Máxima secuencia de párrafos cortos: 2
- Distribución 1–5 / 6–10 / 11–20 / 21–40 / 41+: 21 / 23 / 30 / 35 / 34

## Diálogo

- Intervenciones: 34
- Palabras de párrafos de diálogo, bruto: 661
- Palabras habladas estimadas: 466
- Palabras/intervención, media: 13.706
- Palabras/intervención, mediana: 7.0
- Máximo: 76
- Más de 25 / 40 / 60 palabras: 6 / 4 / 1
- Máximo intercambio sin acción: 3

## Léxico / gestos

- Adverbios en `-mente`: 0 (0.000/1,000 palabras).
- Palabras frecuentes sin stopwords: chiara (36), habia (33), mabel (18), mano (17), cuadro (15), puerta (14), quedo (14), manos (14), luz (14), dejo (13), mas (13), despues (13), tenia (12), telefono (12), arriba (11).
- mirar: 9 (2.271/1,000; clusters: 2).
- sonreír: 2 (0.505/1,000; clusters: 0).
- levantar la vista: 1 (0.252/1,000; clusters: 0).
- quedarse quieto/a: 1 (0.252/1,000; clusters: 0).

## Metadata

- Metadata inicial: sí
- Título Markdown: sí
- Número filename/título: coincide
- Marcadores en metadata: ninguno
- Marcadores en prosa: 0
- Comentarios HTML internos: 0
- Headings internos: 0
