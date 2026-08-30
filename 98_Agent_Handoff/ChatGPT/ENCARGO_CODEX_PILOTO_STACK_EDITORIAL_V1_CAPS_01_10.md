# Encargo para Codex — Piloto V1 del stack editorial (Capítulos 1–10)

**Proyecto:** *Seda y Pólvora*  
**Repositorio:** `XxZylivrar360xX/silk---gunpowder`  
**Branch obligatoria:** `develop`  
**Tipo:** herramienta editorial local / auditoría determinista  
**Fase:** PILOTO V1  
**Corpus inicial:** capítulos 01–10 de `Part_01_El_Encuentro_Y_La_Nada`  
**Modo obligatorio:** `audit_only`  
**NO modificar prosa. NO autofix. NO commit. NO push.**

---

# 0. Objetivo

Construir la primera versión de un **stack editorial determinista** para *Seda y Pólvora*.

Esta herramienta NO edita capítulos.

Su función es:

> leer un corpus de capítulos, medir patrones estilísticos y mecánicos, levantar alertas auditables y producir reportes Markdown para que un editor humano/agente decida qué merece revisión.

La filosofía central es:

> **Una alerta no es un error.**
>
> El linter señala dónde mirar; nunca decide por sí mismo que una frase debe cambiar.

El piloto se calibrará exclusivamente con los capítulos **1–10** antes de permitir cualquier uso sobre el resto de la Parte I.

---

# 1. Leer antes de implementar

Seguir `AGENTS.md`.

Leer:

1. `CLAUDE.md`
2. `98_Agent_Handoff/START_HERE.md`
3. `98_Agent_Handoff/CURRENT_BRIEF.md`
4. `INDEX.md`
5. capítulos 01–10
6. políticas de voz/craft relevantes para Cole y Chiara, usando búsqueda antes de abrir archivos grandes.

No leer `log.md` completo.

---

# 2. Restricción técnica principal

## V1 DEBE usar sólo Python estándar

No añadir:

- `requirements.txt`;
- Poetry;
- pip packages;
- PyYAML;
- spaCy;
- nltk;
- pandas;
- numpy;
- dependencias de IA;
- APIs externas.

Debe funcionar con una instalación razonablemente moderna de Python 3.

Preferir:

- `argparse`
- `re`
- `json`
- `pathlib`
- `collections`
- `statistics`
- `dataclasses`
- `unittest`

Si alguna métrica sofisticada exige una dependencia externa:

> NO implementarla todavía.

Registrar la limitación en README.

---

# 3. Estructura esperada

Crear:

```text
tools/editorial/
├── README.md
├── editorial_audit.py
├── editorial_config.json
├── pilot_01_10.json
├── checks/
│   ├── __init__.py
│   ├── common.py
│   ├── repetitions.py
│   ├── tics.py
│   ├── rhythm.py
│   ├── dialogue.py
│   ├── metadata.py
│   └── lexical.py
├── tests/
│   ├── __init__.py
│   ├── test_repetitions.py
│   ├── test_tics.py
│   ├── test_dialogue.py
│   └── known_cases.json
└── reports/
    └── .gitkeep
```

Crear también:

```text
12_Craft_Policies/editorial/
├── EDITORIAL_POLICY.md
├── DO_NOT_TOUCH.md
└── PILOT_01_10.md
```

NO crear todavía la skill de Claude.

La skill será Fase 2, después de calibrar los falsos positivos del auditor determinista.

---

# 4. Corpus del piloto

`pilot_01_10.json` debe fijar explícitamente los diez archivos.

No inferirlos mediante `glob` como fuente principal.

Usar los paths vigentes en `develop`:

```text
11_Books/Book_01_Seda_y_Polvora/Part_01_El_Encuentro_Y_La_Nada/
```

y los capítulos numerados 01 a 10 actualmente existentes.

Motivo:

- evita incluir archivos renumerados por accidente;
- hace reproducible el piloto;
- no depende todavía de metadata `Estado:` potencialmente desfasada.

Formato orientativo:

```json
{
  "pilot": "01_10",
  "mode": "audit_only",
  "chapters": [
    "11_Books/.../01_....md",
    "...",
    "11_Books/.../10_....md"
  ]
}
```

Usar los nombres reales, no puntos suspensivos.

---

# 5. Separación entre metadata y prosa

Los capítulos contienen comentario HTML inicial con metadata.

El auditor debe distinguir:

1. metadata interna;
2. título Markdown;
3. prosa narrativa real.

Por defecto, las métricas estilísticas NO deben contar el comentario HTML inicial.

La comprobación de metadata sí debe inspeccionarlo.

Tampoco contar como prosa:

- headings Markdown;
- separadores `***` / `---` usados como transición;
- enlaces Obsidian si aparecieran fuera del texto narrativo.

Documentar el criterio.

---

# 6. Modelo de alerta

Crear una estructura común, por ejemplo mediante `dataclass`:

```python
Alert(
    check_id="TIC_UN_SEGUNDO_DE_MAS",
    severity="medium",
    chapter="09_La_Carrera_De_Mascaras.md",
    line=123,
    excerpt="...",
    message="...",
    metric={...}
)
```

Severidades permitidas:

- `info`
- `low`
- `medium`
- `high`

### Regla

`high` NO significa "hay que corregir".

Significa:

> merece lectura humana prioritaria.

Los reportes deben decir esto explícitamente.

---

# 7. Check — repeticiones

Implementar como mínimo:

## A. Frases configurables

Contar frases exactas configuradas.

Ejemplos iniciales:

- `un segundo de más`
- `un momento de más`
- `no dijo nada`
- `no contestó`
- `de alguna manera`
- `como si`

No asumir que sean malas.

Reportar:

- ocurrencias por capítulo;
- ocurrencias globales;
- líneas;
- densidad por 1,000 palabras.

## B. N-gramas repetidos

Detectar n-gramas de palabras repetidos de longitud configurable, por ejemplo:

- 3
- 4
- 5
- 6
- 7
- 8 palabras.

Filtrar ruido.

No reportar automáticamente n-gramas compuestos sólo por palabras funcionales frecuentes.

Crear lista simple de stopwords españolas dentro de configuración o módulo común.

Ignorar o bajar prioridad para:

- fórmulas de diálogo inevitables;
- nombres completos repetidos;
- títulos.

El reporte global debe mostrar los n-gramas más frecuentes del corpus.

---

# 8. Check — tics / construcciones configurables

Configurar patrones, NO codificar todos directamente.

Primera batería:

### Frases

- `un segundo de más`
- `un momento de más`
- `de alguna manera`
- `no hacía falta`
- `como si`

### Patrones aproximados

- `No era X. Era Y.`
- `No fue X. Fue Y.`
- `No porque X, sino porque Y.`
- cadenas negativas tipo:
  `No X. No Y. No Z.`
- explicación negativa:
  `No [algo] — [explicación]`

No intentar análisis lingüístico perfecto.

Regex conservadoras > falsos positivos masivos.

El reporte debe incluir excerpt y línea para inspección.

---

# 9. Check — ritmo

Medir por capítulo:

- palabras;
- párrafos narrativos;
- oraciones aproximadas;
- palabras por oración:
  - media
  - mediana
- palabras por párrafo:
  - media
  - mediana
- porcentaje de párrafos de una sola oración;
- cantidad máxima de párrafos cortos consecutivos;
- cantidad de párrafos <= N palabras, configurable;
- distribución aproximada de tamaños.

No declarar que párrafos cortos son malos.

Levantar alerta sólo por:

- concentración anormal respecto al corpus;
- secuencias largas;
- umbrales configurables.

Para el piloto, si todavía no existe baseline global al procesar un capítulo, calcular estadísticas primero y alertar en una segunda pasada.

---

# 10. Check — diálogo

Identificar intervenciones de diálogo narrativo que empiezan con raya `—`.

Medir:

- número de intervenciones;
- palabras por intervención:
  - media
  - mediana
  - máximo;
- intervenciones > 25, > 40 y > 60 palabras;
- proporción aproximada diálogo / narración;
- secuencias largas de intercambio sin acción intermedia.

## Importante

V1 NO debe intentar atribuir automáticamente cada diálogo a Cole o Chiara salvo que la atribución sea inequívoca.

No inventar speaker attribution mediante heurísticas frágiles.

### Fingerprint V1

El "fingerprint de voz" de personajes queda como **Fase 1.5 / extensión opcional**.

Para V1, producir:

- perfil del diálogo por capítulo;
- posibles outliers.

Si se puede atribuir un speaker únicamente cuando está explícitamente marcado en la misma línea o adyacencia inequívoca, puede registrarse como experimento, pero NO convertirlo en criterio editorial principal.

Documentar la limitación.

---

# 11. Check — lexical

Medir:

- palabras más frecuentes excluyendo stopwords;
- adverbios terminados en `-mente`;
- verbos/gestos configurables.

Lista inicial de gestos para observar, no condenar:

- mirar
- sonreír
- asentir
- suspirar
- encogerse de hombros
- pasarse una mano por la cara
- levantar la vista
- quedarse quieto/a
- tardar / demorarse antes de responder

Buscar variantes razonables con patrones configurables.

Reportar densidad y clustering.

---

# 12. Check — metadata / residuos internos

Detectar:

- `TODO`
- `FIXME`
- `[PENDIENTE`
- `> **PENDIENTE`
- `nota de autor`
- `nota editorial`
- comentarios internos fuera del bloque HTML inicial;
- headings inesperados dentro de prosa;
- metadata ausente;
- título Markdown ausente;
- discrepancia obvia entre número del filename y `# Capítulo N`.

### Importante

Un `PENDIENTE` dentro del comentario HTML inicial NO es necesariamente error del manuscrito.

Clasificarlo como metadata, no contaminar métricas de prosa.

---

# 13. Casos conocidos — tests de calibración

Crear:

`tools/editorial/tests/known_cases.json`

Debe contener ejemplos sintetizados/minimizados basados en problemas REALES ya encontrados durante el triaje.

No hace falta copiar párrafos largos.

Casos iniciales:

## Deben levantar alerta

### A. Residuo de instrucción editorial

Ejemplo histórico ya eliminado:

> `No narró lo que hizo con el coche.`

Clasificación esperada:

`EDITORIAL_INSTRUCTION_LEAK`

### B. Checklist negativo de prompt

Ejemplo histórico:

> `No hubo beso. No hubo un "sube". No hubo nada que se pareciera a una frase importante.`

Esperar alerta por cadena negativa / posible residuo de instrucción.

### C. Tic repetitivo

Varias apariciones cercanas de:

> `un segundo de más`

Debe detectar densidad/repetición.

### D. Explicación negativa en serie

Tres oraciones consecutivas empezando con `No`.

Debe levantar alerta, no error.

## NO deben levantar alerta alta por sí solos

### E.

> `Cole pagó la taza.`

Frase corta deliberada.

No marcarla como mala sólo por ser párrafo corto.

### F.

> `—Sí.`

No marcar una intervención mínima de diálogo como problema.

### G.

Un único `como si` bien aislado.

No high.

### H.

Una secuencia breve de párrafos cortos durante acción.

No high automáticamente sin clustering excesivo.

---

# 14. Configuración

`editorial_config.json` debe permitir modificar sin editar Python:

- frases vigiladas;
- regex de patrones;
- stopwords adicionales;
- n-gram lengths;
- thresholds de párrafo;
- thresholds de diálogo;
- severidades;
- gestos vigilados;
- exclusiones.

Ejemplo conceptual:

```json
{
  "phrases": {
    "un segundo de más": {
      "severity": "medium",
      "global_threshold": 3
    }
  }
}
```

No copiar literalmente si una estructura mejor simplifica el código.

---

# 15. CLI

El comando base debe funcionar desde raíz:

```bash
python tools/editorial/editorial_audit.py \
  --manifest tools/editorial/pilot_01_10.json \
  --output tools/editorial/reports/PILOT_01_10
```

Debe crear:

```text
tools/editorial/reports/PILOT_01_10/
├── 01_....editorial.md
├── 02_....editorial.md
├── ...
├── 10_....editorial.md
├── PILOT_01_10_GLOBAL.md
└── PILOT_01_10.json
```

El JSON es salida estructurada para futuras skills/agentes.

Markdown es para lectura humana.

Opciones mínimas:

```text
--manifest
--config
--output
--quiet
```

Puede incluir `--chapter` para depuración si es barato.

### Protección

NO implementar `--fix`.

NO implementar ninguna opción que escriba en capítulos.

---

# 16. Reporte individual

Cada reporte debe contener aproximadamente:

```markdown
# Auditoría editorial — Capítulo 09

> Esto es diagnóstico, no lista de correcciones.

## Resumen
- palabras
- párrafos
- diálogo %
- alertas high / medium / low / info

## Prioridad de lectura
### HIGH
...
### MEDIUM
...

## Repeticiones
...

## Ritmo
...

## Diálogo
...

## Léxico / gestos
...

## Metadata
...
```

No imprimir cientos de ocurrencias.

Aplicar límites configurables y resumir.

---

# 17. Reporte global

`PILOT_01_10_GLOBAL.md` debe ser el corazón del piloto.

Incluir:

## Corpus

- capítulos;
- palabras totales;
- palabras por capítulo.

## Patrones globales

- frases vigiladas más frecuentes;
- n-gramas destacables;
- gestos;
- adverbios;
- construcciones/tics.

## Ritmo comparado

Tabla por capítulo con:

- palabras;
- mediana oración;
- % párrafos de una oración;
- diálogo %;
- mediana de intervención.

## Outliers

Identificar estadísticamente valores claramente alejados del corpus usando una técnica simple y documentada.

Preferir IQR o z-score simple.

No llamar al outlier "problema".

## Top de alertas para calibración

Mostrar máximo configurable, por ejemplo 30.

Objetivo:

> poder leer las alertas más importantes y decidir cuántas son realmente útiles.

---

# 18. Política editorial

Crear `12_Craft_Policies/editorial/EDITORIAL_POLICY.md`.

Debe establecer:

## Principio

La edición final ocurre DESPUÉS del triaje estructural.

## Diferencia

- estructura = qué pasa / por qué / dónde / consecuencia;
- edición = cómo llega al lector.

## Una alerta no ordena modificar.

## Prioridad

1. continuidad rota;
2. residuos de prompt / metadata filtrada;
3. sobreexplicación;
4. voz;
5. ritmo;
6. repetición;
7. ornamento.

## No esterilizar

Repetición deliberada, frase corta y silencio son herramientas narrativas.

No optimizar prosa hacia una uniformidad estadística.

---

# 19. DO_NOT_TOUCH

Crear:

`12_Craft_Policies/editorial/DO_NOT_TOUCH.md`

Debe proteger durante edición final:

- CANON DEL AUTOR;
- diálogos canon;
- beats;
- motivaciones;
- cronología;
- orden de revelaciones;
- misterios deliberados;
- consecuencias;
- objetos recurrentes;
- progresión Cole/Chiara.

Prohibido que una pasada editorial:

- añada backstory;
- mueva escenas;
- anticipe información;
- "mejore" decisiones de personajes;
- vuelva explícito el subtexto;
- convierta rarezas de voz en español neutro genérico;
- cambie arquitectura porque "suena mejor".

---

# 20. Documento del piloto

Crear:

`12_Craft_Policies/editorial/PILOT_01_10.md`

Registrar:

- por qué 1–10;
- fecha;
- estado `audit_only`;
- qué se mide;
- qué NO se mide;
- criterios de éxito.

### Criterio de éxito inicial

No buscamos muchas alertas.

Buscamos precisión.

Objetivo de calibración:

> de las ~30 alertas de mayor prioridad, idealmente al menos dos tercios deben ser cosas que un editor humano considere razonable revisar.

Esto NO es test automático.

Es criterio para ChatGPT + autor después de ejecutar el reporte.

---

# 21. Actualizar AGENTS.md y CLAUDE.md mínimamente

Ambos dicen actualmente que:

> no hay build, tests ni dependencias.

Después de este encargo existirán tests/herramientas Python auxiliares.

Actualizar esa afirmación SIN convertir los archivos en manuales técnicos.

Dirección:

> El repo sigue siendo primordialmente un vault narrativo de Obsidian, no una aplicación de software. Puede contener herramientas locales auxiliares bajo `tools/` (EPUB, auditoría editorial), preferentemente sin dependencias externas.

Agregar una referencia breve a:

`tools/editorial/README.md`

sólo donde sea útil.

NO cargar `CLAUDE.md` de detalles del stack.

---

# 22. README del stack

Explicar:

- propósito;
- límites;
- comando de piloto;
- cómo ejecutar tests;
- estructura;
- cómo añadir una regla;
- qué significa cada severidad;
- que no existe autofix.

Comando de tests esperado:

```bash
python -m unittest discover -s tools/editorial/tests -v
```

Los tests deben funcionar desde raíz.

---

# 23. Ejecución obligatoria del piloto

Después de implementar:

1. ejecutar tests;
2. ejecutar auditor sobre capítulos 1–10;
3. NO editar capítulos según el resultado;
4. revisar que el auditor no haya modificado ningún capítulo;
5. dejar generados los reportes.

Si el auditor falla:

> arreglar el auditor, NO adaptar la prosa para que pase.

---

# 24. No hacer todavía

NO:

- construir skill de Claude;
- generar prompts de reescritura;
- editar prosa;
- crear autofix;
- llamar una API/LLM;
- clasificar texto como "escrito por IA";
- usar detectores probabilísticos de IA;
- hacer embeddings;
- atribuir voz mediante IA;
- procesar capítulos 11–19;
- cambiar estados narrativos;
- marcar capítulos CERRADO;
- regenerar EPUB;
- hacer commit;
- hacer push.

---

# 25. Entrega

Al terminar, devolver de forma compacta:

1. archivos creados/modificados;
2. versión de Python usada;
3. resultado de tests;
4. comando exacto ejecutado para el piloto;
5. número total de alertas:
   - high
   - medium
   - low
   - info
6. top 10 alertas por prioridad, SIN corregirlas;
7. path de:
   - `PILOT_01_10_GLOBAL.md`
   - JSON global;
8. falsos positivos evidentes detectados por ti;
9. `git diff --stat`;
10. confirmación explícita de que los capítulos 01–10 quedaron byte-for-byte sin edición de prosa.

**NO commit.**  
**NO push.**

Esperar calibración del autor + ChatGPT antes de cualquier Fase 2.
