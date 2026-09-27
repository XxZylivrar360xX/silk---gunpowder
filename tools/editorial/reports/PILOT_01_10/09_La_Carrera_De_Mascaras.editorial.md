# Auditoría editorial — Capítulo 09

> Esto es diagnóstico, no una lista de correcciones. Una alerta —incluso HIGH— sólo pide lectura humana prioritaria.

## Resumen

- Palabras: 2525
- Párrafos narrativos: 101
- Diálogo aproximado: 17.9%
- Alertas HIGH / MEDIUM / LOW / INFO: 2 / 2 / 1 / 1

## Prioridad de lectura

### HIGH

- `LONG_DIALOGUE_INTERVENTION` · línea 35: Intervención de diálogo de 64 palabras; posible outlier para lectura humana. — “—Dos veces en la questura, de adolescente, en Palermo. —Lo dijo despacio, midiendo cuánto contar—. Una por una Vespa que no era mía. Otra por estar en una plaza que los carabinier…”
- `SHORT_PARAGRAPH_CLUSTER` · línea 187: Secuencia de 10 párrafos de 8 palabras o menos; revisar la cadencia, no uniformarla. — “—Esto fue una pésima idea —dijo Chiara. / —Sí. / El motor siguió tictaqueando. / —¿Ganamos?”

### MEDIUM

- `LONG_DIALOGUE_INTERVENTION` · línea 125: Intervención de diálogo de 45 palabras; posible outlier para lectura humana. — “—Bien. —Tyler le echó un ojo al motor por la rejilla, con el gesto de quien tasa sin tocar—. La recta está peor que el mes pasado. Pusieron guardaganado nuevo pasado el tanque de…”
- `NEGATIVE_SENTENCE_CHAIN` · línea 177: Tres o más oraciones consecutivas empiezan con «No»; posible cadena enfática o residuo de checklist. — “No un hombre rubio. No una mujer italiana. No una cara. No los dos juntos.”

### LOW

- `RHYTHM_SINGLE_SENTENCE_PARAGRAPH_OUTLIER` · métrica de capítulo: Outlier bajo del corpus en % de párrafos de una oración; no implica un problema.

### INFO

- `PHRASE_COMO_SI` · línea 181: Frase vigilada: 1 ocurrencia(s) en el capítulo; revisar en contexto. — “Cole se metió por un desvío de grava detrás de una tienda de forraje con las persianas bajas, apagó el motor y dejó las llaves en el contacto. El motor tictaqueó al enfriarse. Los…”

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
- Palabras/intervención, media: 10.762
- Palabras/intervención, mediana: 6.0
- Máximo: 64
- Más de 25 / 40 / 60 palabras: 4 / 2 / 1
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
