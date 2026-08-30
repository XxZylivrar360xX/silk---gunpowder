# Stack editorial determinista

Herramienta local de auditoría para *Seda y Pólvora*. Lee un corpus explícito de capítulos, separa metadata y prosa, calcula métricas mecánicas y genera alertas auditables en Markdown y JSON.

Una alerta no es un error. Incluso `high` sólo significa que conviene leer ese punto antes que otros; nunca ordena corregirlo.

## Límites de V1.1

- Modo único: `audit_only`.
- Sólo biblioteca estándar de Python 3; no hay paquetes, APIs, modelos ni acceso a red.
- No existe `--fix` ni escritura sobre capítulos.
- No atribuye automáticamente diálogos a personajes.
- Separa `dialogue_paragraph_words_raw` de `spoken_words_estimate` mediante una heurística conservadora de incisos; ante ambigüedad no eleva severidad.
- La similaridad entre pasajes es experimental, léxica y determinista; no equivale a similaridad semántica.
- Oraciones, proporción de diálogo y gestos son aproximaciones mecánicas, no análisis lingüístico.
- Los enlaces Obsidian, headings, separadores y el comentario HTML inicial no cuentan como prosa estilística.
- Un comentario HTML inicial sí se inspecciona como metadata; los comentarios internos se reportan aparte.

## Ejecutar el piloto V1.1 sobre 01–10

Desde la raíz del vault:

```bash
python tools/editorial/editorial_audit.py \
  --manifest tools/editorial/pilot_01_10.json \
  --output tools/editorial/reports/PILOT_01_10_V1_1
```

`reports/PILOT_01_10/` conserva los artefactos V1 como baseline y V1.1 rechaza escribir ahí. La salida nueva incluye diez reportes, `PILOT_01_10_V1_1_GLOBAL.md`, `PILOT_01_10_V1_1.json` y `V1_VS_V1_1.md`.

Opciones:

- `--config`: usa otra configuración JSON;
- `--chapter`: filtra por número o fragmento del filename para depuración;
- `--quiet`: no imprime el resumen final.

El manifiesto es la fuente autoritativa del corpus: enumera cada path y debe declarar `mode: audit_only`. El auditor rechaza manifiestos con otro modo.

## Pruebas

```bash
python -m unittest discover -s tools/editorial/tests -v
```

En entornos sincronizados se puede añadir `-B` para evitar crear `__pycache__`; no es requisito lógico del auditor. `known_cases.json` conserva los casos V1 y `regression_v1_1.json` contiene los falsos positivos y positivos compuestos usados para calibrar V1.1.

## Estructura

- `editorial_audit.py`: CLI, segunda pasada estadística y render de reportes.
- `editorial_config.json`: frases, regex, stopwords, gestos, umbrales, severidades y límites de salida.
- `pilot_01_10.json`: corpus fijo del piloto.
- `checks/`: extracción común y checks de repetición, tics, ritmo, diálogo, léxico, metadata y similaridad experimental.
- `tests/`: casos de calibración deterministas.
- `reports/`: V1 queda en `reports/PILOT_01_10/`; V1.1 queda en `reports/PILOT_01_10_V1_1/`.

## Agregar o ajustar una regla

1. Añade primero un caso mínimo a `known_cases.json` y una aserción al módulo de pruebas pertinente.
2. Si es una frase, regex, gesto, stopword, exclusión o umbral, modifícalo en `editorial_config.json`.
3. Sólo crea código nuevo cuando la regla no pueda expresarse con la configuración existente.
4. Ejecuta las pruebas y el piloto completo.
5. Calibra con lectura humana: la meta es precisión, no volumen de alertas.

Los patrones regex deben ser conservadores. Si una regla requiere sintaxis o semántica profunda, se pospone: V1.1 no incorpora dependencias externas.

## Severidades

- `high`: lectura humana prioritaria. Se reserva para una señal determinista de confianza alta, una combinación de señales o una concentración excepcional; una sola métrica mecánica simple no basta salvo casos extremadamente confiables.
- `medium`: patrón suficientemente concentrado o extenso para revisión.
- `low`: señal débil o mecánica útil para comparar.
- `info`: ocurrencia aislada o dato descriptivo.

No hay autofix. Los reportes son insumo para el autor y la sala editorial.

V1.1 etiqueta además la naturaleza de la señal como `high-confidence`, `compound` o `descriptive/inventory`. Un parlamento aislado nunca es `high` sólo por longitud y un cluster corto predominantemente dialogado nunca es `high` sólo por longitud.
