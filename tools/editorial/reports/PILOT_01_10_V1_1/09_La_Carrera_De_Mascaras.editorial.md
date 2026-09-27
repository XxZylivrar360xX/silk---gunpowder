# Auditoría editorial — Capítulo 09

- `editor_version`: `1.1`

> Esto es diagnóstico, no una lista de correcciones. Una alerta —incluso HIGH— sólo pide lectura humana prioritaria.

## Resumen

- Palabras: 2525
- Párrafos narrativos: 101
- Diálogo aproximado: 10.1%
- Alertas HIGH / MEDIUM / LOW / INFO: 0 / 1 / 4 / 2

## Prioridad de lectura

### HIGH

- Sin alertas.

### MEDIUM

- `NEGATIVE_SENTENCE_CHAIN` · `descriptive/inventory` · línea 177: Tres o más oraciones consecutivas empiezan con «No»; posible cadena enfática o residuo de checklist. — “No un hombre rubio. No una mujer italiana. No una cara. No los dos juntos.”

### LOW

- `LONG_DIALOGUE_INTERVENTION` · `descriptive/inventory` · línea 35: Intervención estimada en 58 palabras habladas; la longitud aislada nunca eleva a HIGH. — “—Dos veces en la questura, de adolescente, en Palermo. —Lo dijo despacio, midiendo cuánto contar—. Una por una Vespa que no era mía. Otra por estar en una plaza que los carabinier…”
- `SHORT_DIALOGUE_CLUSTER` · `descriptive/inventory` · línea 187: Secuencia dialogue de 10 párrafos de 8 palabras o menos; revisar la cadencia, no uniformarla. — “—Esto fue una pésima idea —dijo Chiara. / —Sí. / El motor siguió tictaqueando. / —¿Ganamos?”
- `DIALOGUE_PERCENT_OUTLIER` · `descriptive/inventory` · métrica de capítulo: Outlier bajo del corpus en % aproximado de diálogo; no implica un problema.
- `RHYTHM_SINGLE_SENTENCE_PARAGRAPH_OUTLIER` · `descriptive/inventory` · métrica de capítulo: Outlier bajo del corpus en % de párrafos de una oración; no implica un problema.

### INFO

- `CROSS_CHAPTER_PASSAGE_SIMILARITY` · `descriptive/inventory` · línea 47: Posible similitud con 08_La_Noche_Del_Ladrillo.md:39 (score 0.1741); señal experimental. — “Bajó con zapatos planos y un abrigo sobre un suéter oscuro, que era lo más cómodo que tenía a mano sin subir a cambiarse del todo. Cuando salió por la puerta de servicio del Monarch, el coche ya estaba contra la acera,…”
- `PHRASE_COMO_SI` · `descriptive/inventory` · línea 181: Frase vigilada: 1 ocurrencia(s) en el capítulo; revisar en contexto. — “Cole se metió por un desvío de grava detrás de una tienda de forraje con las persianas bajas, apagó el motor y dejó las llaves en el contacto. El motor tictaqueó al enfriarse. Los…”

## Repeticiones

- `como si`: 1 · 0.396/1,000 palabras · líneas 181

### N-gramas locales

- Sin n-gramas por encima del umbral local.

## Ritmo

- Oraciones aproximadas: 208
- Palabras/oración, media: 12.139
- Palabras/oración, mediana: 8.0
- Palabras/párrafo, media: 25
- Palabras/párrafo, mediana: 15.0
- Párrafos de una oración: 45.5%
- Máxima secuencia de párrafos cortos: 10
- Distribución 1–5 / 6–10 / 11–20 / 21–40 / 41+: 24 / 15 / 16 / 21 / 25

## Diálogo

- Intervenciones: 42
- Palabras de párrafos de diálogo, bruto: 452
- Palabras habladas estimadas: 256
- Palabras/intervención, media: 6.095
- Palabras/intervención, mediana: 3.0
- Máximo: 58
- Más de 25 / 40 / 60 palabras: 1 / 1 / 0
- Máximo intercambio sin acción: 7

## Léxico / gestos

- Adverbios en `-mente`: 2 (0.792/1,000 palabras).
- Palabras frecuentes sin stopwords: cole (25), habia (20), chiara (19), mas (17), cara (12), coche (12), nada (10), despues (10), dijo (9), tenia (8), mano (8), puerta (8), nadie (7), siempre (7), dejo (7).
- mirar: 5 (1.980/1,000; clusters: 0).
- asentir: 1 (0.396/1,000; clusters: 0).
- pasarse una mano por la cara: 1 (0.396/1,000; clusters: 0).
- levantar la vista: 2 (0.792/1,000; clusters: 0).

## Metadata

- Metadata inicial: sí
- Título Markdown: sí
- Número filename/título: coincide
- Marcadores en metadata: ninguno
- Marcadores en prosa: 0
- Comentarios HTML internos: 0
- Headings internos: 0
