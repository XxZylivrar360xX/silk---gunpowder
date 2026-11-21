# Auditoría editorial — Capítulo 50

- `editor_version`: `1.1`

> Esto es diagnóstico, no una lista de correcciones. Una alerta —incluso HIGH— sólo pide lectura humana prioritaria.

## Resumen

- Palabras: 3946
- Párrafos narrativos: 140
- Diálogo aproximado: 11.5%
- Alertas HIGH / MEDIUM / LOW / INFO: 1 / 1 / 8 / 4

## Prioridad de lectura

### HIGH

- `CHAPTER_NUMBER_MISMATCH` · `descriptive/inventory` · línea 37: Filename indica capítulo 50; el título indica 46. — “Capítulo 46 — A oscuras”

### MEDIUM

- `LONG_DIALOGUE_INTERVENTION` · `descriptive/inventory` · línea 205: Intervención estimada en 76 palabras habladas; la longitud aislada nunca eleva a HIGH. — “—Pagué todo. Le di mi nombre a un hombre que cobraba en la acera desde niño. Le quedé a deber a Varek lo que él quiera, cuando él quiera, y no sé qué es. Me senté a tomar café con…”

### LOW

- `GESTURE_CLUSTER_MIRAR` · `descriptive/inventory` · línea 81: El gesto «mirar» aparece agrupado en una ventana de 20 líneas. — “Chiara miró la taza. El café tenía una nata delgada que se rompía en la orilla. / Mabel miró el billete. Lo dejó donde estaba. / El Lancia estaba frío por dentro. Chiara lo encend…”
- `LONG_DIALOGUE_INTERVENTION` · `descriptive/inventory` · línea 167: Intervención estimada en 41 palabras habladas; la longitud aislada nunca eleva a HIGH. — “—Señora Bellandi. El generador sólo da para la jaula y las cámaras. Los elevadores están parados. Hay dos huéspedes atorados en el de la Torre Sur, ya les hablaron los bomberos po…”
- `POSSIBLE_EDITORIAL_INSTRUCTION_LEAK` · `descriptive/inventory` · línea 177: Verbo ambiguo compatible con narración normal; revisar sólo como señal de baja confianza. — “No contó los pisos. A partir de cierto punto los descansos eran todos el mismo: el letrero verde, el número pintado en la pared de concreto, el barandal frío, el siguiente tramo.…”
- `REPEATED_NGRAM_4` · `descriptive/inventory` · línea 185: N-grama de 4 palabras repetido 3 veces en el capítulo. — “junto a la puerta”
- `LONG_DIALOGUE_INTERVENTION` · `descriptive/inventory` · línea 201: Intervención estimada en 41 palabras habladas; la longitud aislada nunca eleva a HIGH. — “—Pero eso no Te da derecho. —Levantó la vista hacia el círculo de luz en el techo—. No así. No para quitármelo como se le quita algo a una niña que se portó mal, porque se puede.…”
- `REPEATED_NGRAM_4` · `descriptive/inventory` · línea 201: N-grama de 4 palabras repetido 3 veces en el capítulo. — “el circulo de luz”
- `LONG_DIALOGUE_INTERVENTION` · `descriptive/inventory` · línea 221: Intervención estimada en 41 palabras habladas; la longitud aislada nunca eleva a HIGH. — “—Subió. Estuvo aquí, del otro lado de esa puerta, con la mano así, y no tocó, y yo estaba aquí dentro. Lo tuviste a seis metros. Y me lo dejaste ver en una pantalla, de espaldas,…”
- `DIALOGUE_INTERVENTION_MEDIAN_OUTLIER` · `descriptive/inventory` · métrica de capítulo: Outlier alto del corpus en mediana de intervención; no implica un problema.

### INFO

- `PHRASE_UN_SEGUNDO_DE_MAS` · `descriptive/inventory` · línea 43: Frase vigilada: 1 ocurrencia(s) en el capítulo; revisar en contexto. — “Chiara estaba ahí desde las siete. Había llegado con el último turno de la cena, cuando la vitrina ya tenía más charolas vacías que pan, y se había sentado en el extremo de la bar…”
- `CROSS_CHAPTER_PASSAGE_SIMILARITY` · `descriptive/inventory` · línea 97: Posible similitud con 45_Ropa_Limpia.md:260 (score 0.1244); señal experimental. — “El Lancia estaba frío por dentro. Chiara lo encendió y se quedó un momento con las manos en el volante, mirando Avenida Almendra por el parabrisas: la cortina bajada de la tlapalería, el poste con el anuncio de un circo…”
- `PHRASE_COMO_SI` · `descriptive/inventory` · línea 139: Frase vigilada: 3 ocurrencia(s) en el capítulo; revisar en contexto. — “Chiara se inclinó sobre el volante para verla por el parabrisas. No había torre. Había un rectángulo más negro que el cielo, sin una sola ventana, y detrás, muy al norte, la loma…”
- `CROSS_CHAPTER_PASSAGE_SIMILARITY` · `descriptive/inventory` · línea 163: Posible similitud con 49_Enfrente.md:217 (score 0.1614); señal experimental. — “Eso fue lo primero. No la oscuridad, que con las luces de emergencia era una penumbra amarilla en la que se adivinaban las mesas y las columnas, sino el silencio de las máquinas: cuatrocientas pantallas negras, sin camp…”

## Repeticiones

- `como si`: 3 · 0.760/1,000 palabras · líneas 139, 285, 327
- `un segundo de más`: 1 · 0.253/1,000 palabras · líneas 43

### N-gramas locales

- `el circulo de luz` (4 palabras): 3
- `junto a la puerta` (4 palabras): 3
- `luz del telefono` (3 palabras): 3

## Ritmo

- Oraciones aproximadas: 346
- Palabras/oración, media: 11.405
- Palabras/oración, mediana: 8.0
- Palabras/párrafo, media: 28.186
- Palabras/párrafo, mediana: 20.0
- Párrafos de una oración: 37.9%
- Máxima secuencia de párrafos cortos: 2
- Distribución 1–5 / 6–10 / 11–20 / 21–40 / 41+: 18 / 24 / 29 / 35 / 34

## Diálogo

- Intervenciones: 30
- Palabras de párrafos de diálogo, bruto: 652
- Palabras habladas estimadas: 454
- Palabras/intervención, media: 15.133
- Palabras/intervención, mediana: 7.0
- Máximo: 76
- Más de 25 / 40 / 60 palabras: 6 / 4 / 1
- Máximo intercambio sin acción: 3

## Léxico / gestos

- Adverbios en `-mente`: 0 (0.000/1,000 palabras).
- Palabras frecuentes sin stopwords: chiara (36), habia (31), mano (17), mabel (16), cuadro (15), puerta (14), quedo (14), luz (14), dejo (13), mas (13), despues (13), manos (13), tenia (12), lado (12), telefono (12).
- mirar: 9 (2.281/1,000; clusters: 2).
- sonreír: 3 (0.760/1,000; clusters: 0).
- levantar la vista: 1 (0.253/1,000; clusters: 0).
- quedarse quieto/a: 1 (0.253/1,000; clusters: 0).

## Metadata

- Metadata inicial: sí
- Título Markdown: sí
- Número filename/título: NO coincide
- Marcadores en metadata: ninguno
- Marcadores en prosa: 0
- Comentarios HTML internos: 0
- Headings internos: 0
