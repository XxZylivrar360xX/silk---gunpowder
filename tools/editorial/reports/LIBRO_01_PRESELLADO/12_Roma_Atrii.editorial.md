# Auditoría editorial — Capítulo 12

- `editor_version`: `1.1`

> Esto es diagnóstico, no una lista de correcciones. Una alerta —incluso HIGH— sólo pide lectura humana prioritaria.

## Resumen

- Palabras: 3946
- Párrafos narrativos: 187
- Diálogo aproximado: 22.7%
- Alertas HIGH / MEDIUM / LOW / INFO: 1 / 1 / 9 / 2

## Prioridad de lectura

### HIGH

- `CHAPTER_NUMBER_MISMATCH` · `descriptive/inventory` · línea 12: Filename indica capítulo 12; el título indica 13. — “Capítulo 13 — Roma Atrii”

### MEDIUM

- `REPEATED_NGRAM_6` · `descriptive/inventory` · línea 290: N-grama de 6 palabras repetido 3 veces en el capítulo. — “un corredor de piezas del norte”

### LOW

- `SHORT_MIXED_CLUSTER` · `descriptive/inventory` · línea 120: Secuencia mixed de 6 párrafos de 8 palabras o menos; revisar la cadencia, no uniformarla. — “—No. Sabe escribir cuatro palabras. Leer, ninguna. / —¿El chico? / Chiara negó con la cabeza. / —¿Quién es?”
- `LONG_DIALOGUE_INTERVENTION` · `descriptive/inventory` · línea 142: Intervención estimada en 42 palabras habladas; la longitud aislada nunca eleva a HIGH. — “—Kenji sabe lo de su caja. El chico sabía una dirección y un nombre que no entendía. Si alguno cae, cae con eso y nada más. —Lo dijo al ritmo de quien cuenta las piezas de algo qu…”
- `LONG_DIALOGUE_INTERVENTION` · `descriptive/inventory` · línea 164: Intervención estimada en 45 palabras habladas; la longitud aislada nunca eleva a HIGH. — “—Es iglesia, un poco. —Casi sonrió—. Crecí aprendiendo que una confesión no vale nada si le llega al oído equivocado. Y creo en Dios, Kal. Creo en Dios, y en que una mentira dicha…”
- `PHRASE_NO_CONTESTO` · `descriptive/inventory` · línea 172: Frase vigilada: 2 ocurrencia(s) en el capítulo; revisar en contexto. — “Kal no contestó. Abrió la boca para otra cosa, cuántos, quiénes, en qué pisos, ella se lo vio, y la cerró.”
- `LONG_DIALOGUE_INTERVENTION` · `descriptive/inventory` · línea 184: Intervención estimada en 52 palabras habladas; la longitud aislada nunca eleva a HIGH. — “—Un muchacho de la estación de la Ronda Exterior —dijo Mabel, sirviéndole sin que se lo pidiera—. Dice que dos hombres de traje se estacionan ahí cada tantas noches, pasada la med…”
- `LONG_DIALOGUE_INTERVENTION` · `descriptive/inventory` · línea 190: Intervención estimada en 43 palabras habladas; la longitud aislada nunca eleva a HIGH. — “—Yo no dije fiscales. Digo que nadie de traje espera a nadie en una gasolinera de la Ronda a esa hora, a menos que no quiera que lo vean esperando. El resto lo armas tú, que para…”
- `NO_PORQUE_SINO` · `descriptive/inventory` · línea 260: Construcción «No porque X, sino porque Y»; revisar su concentración. — “No porque creyera que su padre podía arreglarlo todo, sino porque por un instante bastaba con que él estuviera delante.”
- `NO_ERA_ERA` · `descriptive/inventory` · línea 276: Construcción «No era X. Era Y.»; revisar si la antítesis explica de más. — “No era una acusación todavía. Era peor: era una dirección.”
- `LONG_DIALOGUE_INTERVENTION` · `descriptive/inventory` · línea 318: Intervención estimada en 58 palabras habladas; la longitud aislada nunca eleva a HIGH. — “—Hay otro sospechoso: Rafe Domínguez, del sur. Si te preguntan por piezas en efectivo, Garrett las recogió en Villani Motors, cerca de Cedar Flats, hace cosa de dos meses. Si te p…”

### INFO

- `CROSS_CHAPTER_PASSAGE_SIMILARITY` · `descriptive/inventory` · línea 28: Posible similitud con 09_La_Balanza.md:283 (score 0.1883); señal experimental. — “Era joven, flaco, con el pelo recién cortado y un vaso de agua que no tocaba. Lo había visto una sola vez, desde arriba, desde la ventana del cuarto sin dueño de la casa común, con la férula en el alféizar: bajando de u…”
- `PHRASE_COMO_SI` · `descriptive/inventory` · línea 202: Frase vigilada: 3 ocurrencia(s) en el capítulo; revisar en contexto. — “—¿Sabes qué no me cuadra? Que de repente todo Las Calderas habla de Rafe Domínguez como si fuera noticia. Y Rafe Domínguez lleva siendo el mismo desde que yo era joven. —Mabel vol…”

## Repeticiones

- `como si`: 3 · 0.760/1,000 palabras · líneas 202, 378, 388
- `no contestó`: 2 · 0.507/1,000 palabras · líneas 172, 354

### N-gramas locales

- `un corredor de piezas del norte` (6 palabras): 3
- `la chaqueta cafe` (3 palabras): 3

## Ritmo

- Oraciones aproximadas: 391
- Palabras/oración, media: 10.092
- Palabras/oración, mediana: 6.0
- Palabras/párrafo, media: 21.102
- Palabras/párrafo, mediana: 12.0
- Párrafos de una oración: 42.8%
- Máxima secuencia de párrafos cortos: 6
- Distribución 1–5 / 6–10 / 11–20 / 21–40 / 41+: 46 / 37 / 41 / 32 / 31

## Diálogo

- Intervenciones: 90
- Palabras de párrafos de diálogo, bruto: 1154
- Palabras habladas estimadas: 897
- Palabras/intervención, media: 9.967
- Palabras/intervención, mediana: 6.0
- Máximo: 58
- Más de 25 / 40 / 60 palabras: 13 / 5 / 0
- Máximo intercambio sin acción: 5

## Léxico / gestos

- Adverbios en `-mente`: 1 (0.253/1,000 palabras).
- Palabras frecuentes sin stopwords: habia (36), chiara (32), kal (27), kenji (23), nadie (21), quien (18), dijo (18), nombre (18), caja (17), mas (15), papel (15), noche (13), pregunto (11), despues (11), alguien (11).
- mirar: 11 (2.788/1,000; clusters: 0).
- sonreír: 3 (0.760/1,000; clusters: 0).
- encogerse de hombros: 1 (0.253/1,000; clusters: 0).
- levantar la vista: 2 (0.507/1,000; clusters: 0).

## Metadata

- Metadata inicial: sí
- Título Markdown: sí
- Número filename/título: NO coincide
- Marcadores en metadata: ninguno
- Marcadores en prosa: 0
- Comentarios HTML internos: 0
- Headings internos: 0
