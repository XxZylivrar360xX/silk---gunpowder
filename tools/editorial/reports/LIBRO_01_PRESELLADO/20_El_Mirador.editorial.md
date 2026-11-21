# Auditoría editorial — Capítulo 20

- `editor_version`: `1.1`

> Esto es diagnóstico, no una lista de correcciones. Una alerta —incluso HIGH— sólo pide lectura humana prioritaria.

## Resumen

- Palabras: 5315
- Párrafos narrativos: 237
- Diálogo aproximado: 11.4%
- Alertas HIGH / MEDIUM / LOW / INFO: 1 / 1 / 9 / 2

## Prioridad de lectura

### HIGH

- `CHAPTER_NUMBER_MISMATCH` · `descriptive/inventory` · línea 11: Filename indica capítulo 20; el título indica 18. — “Capítulo 18 — En lo pequeño”

### MEDIUM

- `REPEATED_NGRAM_6` · `descriptive/inventory` · línea 47: N-grama de 6 palabras repetido 3 veces en el capítulo. — “a la altura de los ojos”

### LOW

- `PHRASE_COMO_SI` · `descriptive/inventory` · línea 31: Frase vigilada: 11 ocurrencia(s) en el capítulo; revisar en contexto. — “—Bolos —dijo, como si la palabra sola explicara todo—. Hay una bolera en la playa. Nunca he ido a una.”
- `GESTURE_CLUSTER_MIRAR` · `descriptive/inventory` · línea 103: El gesto «mirar» aparece agrupado en una ventana de 20 líneas. — “En la última ronda Chiara se quedó un rato con la bola contra el pecho, mirando la flecha, y tiró como él le había dicho. Los diez pinos se fueron juntos. / Después la bajó. Chiar…”
- `REPEATED_NGRAM_5` · `descriptive/inventory` · línea 133: N-grama de 5 palabras repetido 3 veces en el capítulo. — “kal se quedo con la”
- `PHRASE_NO_DIJO_NADA` · `descriptive/inventory` · línea 177: Frase vigilada: 6 ocurrencia(s) en el capítulo; revisar en contexto. — “No dijo nada más. Tomó la curva siguiente a una velocidad que no correspondía, la cola se soltó y el auto bajó la curva entera de lado, sin tocar una sola vez el borde del camino.…”
- `REPEATED_NGRAM_4` · `descriptive/inventory` · línea 177: N-grama de 4 palabras repetido 4 veces en el capítulo. — “no dijo nada mas”
- `REPEATED_NGRAM_5` · `descriptive/inventory` · línea 185: N-grama de 5 palabras repetido 3 veces en el capítulo. — “y por primera vez en”
- `POSSIBLE_EDITORIAL_INSTRUCTION_LEAK` · `descriptive/inventory` · línea 217: Verbo ambiguo compatible con narración normal; revisar sólo como señal de baja confianza. — “No contó el resto. Lo tenía entero, la calle y los zapatos mal puestos y lo que vino después, y se lo quedó.”
- `SHORT_MIXED_CLUSTER` · `descriptive/inventory` · línea 277: Secuencia mixed de 6 párrafos de 8 palabras o menos; revisar la cadencia, no uniformarla. — “Chiara se apartó lo suficiente para mirarlo. / —¿Seguro? / —Llevo meses seguro. / —Yo también. —Sonrió—. Sólo quería oírtelo decir.”
- `PHRASE_NO_CONTESTO` · `descriptive/inventory` · línea 413: Frase vigilada: 3 ocurrencia(s) en el capítulo; revisar en contexto. — “Marisol no contestó, pero algo en sus hombros bajó un poco. Chiara tomó la bolsa de las manos de Kal sin mirarlo y se la acomodó a Marisol contra la cara, y Marisol subió la mano…”

### INFO

- `CROSS_CHAPTER_PASSAGE_SIMILARITY` · `descriptive/inventory` · línea 299: Posible similitud con 07_La_Noche_Del_Ladrillo.md:359 (score 0.1582); señal experimental. — “El teléfono sonó a las tres y algo de la madrugada. La pantalla encendió lo poco que había entre la cama y la puerta: un calcetín oscuro en el suelo, doblado sobre sí mismo; más arriba, colgado de la lámpara de la mesa…”
- `PHRASE_UN_SEGUNDO_DE_MAS` · `descriptive/inventory` · línea 375: Frase vigilada: 1 ocurrencia(s) en el capítulo; revisar en contexto. — “Marisol miró la casa un segundo de más antes de dejarse caer en el sofá —el vacío de doble altura, la escalera abierta, el mezzanine suspendido sobre la sala—, como si el espacio…”

## Repeticiones

- `como si`: 11 · 2.070/1,000 palabras · líneas 31, 65, 107, 179, 221, 273, 375, 381
- `no contestó`: 3 · 0.564/1,000 palabras · líneas 413, 445, 493
- `no dijo nada`: 6 · 1.129/1,000 palabras · líneas 177, 209, 257, 371, 377, 501
- `un segundo de más`: 1 · 0.188/1,000 palabras · líneas 375

### N-gramas locales

- `no dijo nada` (3 palabras): 6
- `no dijo nada mas` (4 palabras): 4
- `kal se quedo` (3 palabras): 4
- `a la altura de los ojos` (6 palabras): 3
- `kal se quedo con la` (5 palabras): 3
- `y por primera vez en` (5 palabras): 3
- `bolsa de maiz` (3 palabras): 3
- `una sola vez` (3 palabras): 3

## Ritmo

- Oraciones aproximadas: 454
- Palabras/oración, media: 11.707
- Palabras/oración, mediana: 7.0
- Palabras/párrafo, media: 22.426
- Palabras/párrafo, mediana: 13.0
- Párrafos de una oración: 52.7%
- Máxima secuencia de párrafos cortos: 6
- Distribución 1–5 / 6–10 / 11–20 / 21–40 / 41+: 70 / 33 / 46 / 44 / 44

## Diálogo

- Intervenciones: 112
- Palabras de párrafos de diálogo, bruto: 1037
- Palabras habladas estimadas: 606
- Palabras/intervención, media: 5.411
- Palabras/intervención, mediana: 4.0
- Máximo: 35
- Más de 25 / 40 / 60 palabras: 1 / 0 / 0
- Máximo intercambio sin acción: 5

## Léxico / gestos

- Adverbios en `-mente`: 2 (0.376/1,000 palabras).
- Palabras frecuentes sin stopwords: kal (76), chiara (54), dijo (37), habia (36), marisol (34), mas (33), mano (22), nada (21), lado (20), despues (16), quedo (16), ahi (13), ninguno (12), mirando (12), todavia (11).
- mirar: 23 (4.327/1,000; clusters: 4).
- sonreír: 6 (1.129/1,000; clusters: 0).
- encogerse de hombros: 1 (0.188/1,000; clusters: 0).
- pasarse una mano por la cara: 1 (0.188/1,000; clusters: 0).
- levantar la vista: 2 (0.376/1,000; clusters: 0).
- quedarse quieto/a: 1 (0.188/1,000; clusters: 0).

## Metadata

- Metadata inicial: sí
- Título Markdown: sí
- Número filename/título: NO coincide
- Marcadores en metadata: ninguno
- Marcadores en prosa: 0
- Comentarios HTML internos: 0
- Headings internos: 0
