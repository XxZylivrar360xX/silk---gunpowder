# V1 vs V1.1 — calibración editorial

La V1 se conserva como baseline; V1.1 cambia heurísticas y severidades, no la prosa.

## Conteos

| Severidad | V1 | V1.1 | Delta |
|---|---:|---:|---:|
| HIGH | 15 | 1 | -14 |
| MEDIUM | 40 | 17 | -23 |
| LOW | 112 | 138 | +26 |
| INFO | 9 | 33 | +24 |

## Las 15 HIGH originales

### 01_Un_Hombre_De_Negocios_Intachable.md:655 · `LONG_DIALOGUE_INTERVENTION`

- Resultado V1.1: **bajó** — LONG_DIALOGUE_INTERVENTION · MEDIUM
- Motivo técnico: La severidad usa palabras habladas estimadas; un parlamento aislado nunca es HIGH.

### 02_Demasiado_Listo.md:163 · `SHORT_PARAGRAPH_CLUSTER`

- Resultado V1.1: **cambió** — SHORT_DIALOGUE_CLUSTER · LOW
- Motivo técnico: V1.1 clasifica la secuencia por proporción de diálogo y reserva HIGH para narración excepcional.

### 03_Los_Viejos_Dias.md:475 · `LONG_DIALOGUE_INTERVENTION`

- Resultado V1.1: **bajó** — LONG_DIALOGUE_INTERVENTION · MEDIUM
- Motivo técnico: La severidad usa palabras habladas estimadas; un parlamento aislado nunca es HIGH.

### 03_Los_Viejos_Dias.md:511 · `SHORT_PARAGRAPH_CLUSTER`

- Resultado V1.1: **cambió** — SHORT_MIXED_CLUSTER · LOW
- Motivo técnico: V1.1 clasifica la secuencia por proporción de diálogo y reserva HIGH para narración excepcional.

### 03_Los_Viejos_Dias.md:629 · `LONG_DIALOGUE_INTERVENTION`

- Resultado V1.1: **bajó** — LONG_DIALOGUE_INTERVENTION · MEDIUM
- Motivo técnico: La severidad usa palabras habladas estimadas; un parlamento aislado nunca es HIGH.

### 04_La_Primera_Llamada.md:469 · `SHORT_PARAGRAPH_CLUSTER`

- Resultado V1.1: **cambió** — SHORT_NARRATIVE_CLUSTER · MEDIUM
- Motivo técnico: V1.1 clasifica la secuencia por proporción de diálogo y reserva HIGH para narración excepcional.

### 05_La_Casa_No_Quiere_Ruido.md:199 · `SHORT_PARAGRAPH_CLUSTER`

- Resultado V1.1: **cambió** — SHORT_MIXED_CLUSTER · LOW
- Motivo técnico: V1.1 clasifica la secuencia por proporción de diálogo y reserva HIGH para narración excepcional.

### 06_Una_Amiga.md:43 · `SHORT_PARAGRAPH_CLUSTER`

- Resultado V1.1: **cambió** — SHORT_MIXED_CLUSTER · LOW
- Motivo técnico: V1.1 clasifica la secuencia por proporción de diálogo y reserva HIGH para narración excepcional.

### 07_Ambos.md:237 · `LONG_DIALOGUE_INTERVENTION`

- Resultado V1.1: **bajó** — LONG_DIALOGUE_INTERVENTION · MEDIUM
- Motivo técnico: La severidad usa palabras habladas estimadas; un parlamento aislado nunca es HIGH.

### 09_La_Carrera_De_Mascaras.md:35 · `LONG_DIALOGUE_INTERVENTION`

- Resultado V1.1: **bajó** — LONG_DIALOGUE_INTERVENTION · LOW
- Motivo técnico: La severidad usa palabras habladas estimadas; un parlamento aislado nunca es HIGH.

### 09_La_Carrera_De_Mascaras.md:187 · `SHORT_PARAGRAPH_CLUSTER`

- Resultado V1.1: **cambió** — SHORT_DIALOGUE_CLUSTER · LOW
- Motivo técnico: V1.1 clasifica la secuencia por proporción de diálogo y reserva HIGH para narración excepcional.

### 10_El_Corral.md:250 · `LONG_DIALOGUE_INTERVENTION`

- Resultado V1.1: **cambió** — LONG_DIALOGUE_CLUSTER · HIGH
- Motivo técnico: La prioridad proviene de la concentración de intervenciones largas, no de longitud aislada.

### 10_El_Corral.md:254 · `LONG_DIALOGUE_INTERVENTION`

- Resultado V1.1: **cambió** — LONG_DIALOGUE_CLUSTER · HIGH
- Motivo técnico: La prioridad proviene de la concentración de intervenciones largas, no de longitud aislada.

### 10_El_Corral.md:346 · `LONG_DIALOGUE_INTERVENTION`

- Resultado V1.1: **bajó** — LONG_DIALOGUE_INTERVENTION · LOW
- Motivo técnico: La severidad usa palabras habladas estimadas; un parlamento aislado nunca es HIGH.

### 10_El_Corral.md:394 · `LONG_DIALOGUE_INTERVENTION`

- Resultado V1.1: **desapareció** — Sin alerta equivalente.
- Motivo técnico: La señal simple ya no cumple la política HIGH de V1.1.
