# Archivo de relevo

Historial de consulta, no instrucciones vigentes. Las copias conservan decisiones, diálogos, estados, contradicciones y rutas tal como estaban al corte; su conservación no revalida información superada.

## Corte del 2026-09-21

Copias íntegras, verificadas por SHA-256 antes de compactar:

- [[98_Agent_Handoff/archive/log_hasta_2026-09-21|Bitácora original]].
- [[98_Agent_Handoff/archive/2026-09-21_CURRENT_BRIEF|Brief acumulado original]].
- [[98_Agent_Handoff/archive/2026-09-21_PENDING|Pendientes originales, incluidos cierres y reservas]].
- [[98_Agent_Handoff/archive/2026-09-21_DECISIONS|Decisiones originales]].

Estas copias son inmutables. No corregir sus nombres, enlaces históricos ni canon superado por nuevas decisiones. Para estado actual, usar [[98_Agent_Handoff/CURRENT_BRIEF]], [[98_Agent_Handoff/PENDING]] y [[98_Agent_Handoff/BACKLOG]].

## ChatGPT (2026-10-03)

`archive/chatgpt/`: encargos, prompts, hitos y handoffs que ChatGPT dejaba antes del buzón actual (agosto–septiembre 2026), más las notas del buzón ya procesadas por Claude Code. Historial, no instrucciones vigentes; su contenido puede estar superado por el canon.

## Búsqueda por demanda

Desde la raíz del vault:

```powershell
rg -n -i "Palermo" 98_Agent_Handoff/sessions 98_Agent_Handoff/archive
rg -n "^##" 98_Agent_Handoff/archive/log_hasta_2026-09-21.md
```

Primero localizar coincidencias; después abrir sólo el tramo pertinente. No leer el archivo histórico completo por defecto. Las referencias antiguas a secciones de log/brief/pending/decisions se buscan en las copias correspondientes.

## Nuevos registros

Una nota por sesión en `98_Agent_Handoff/sessions/`. [[log]] enlaza las 30 más recientes; trasladar enlaces anteriores a índices `AAAA-MM_sesiones.md` en esta carpeta, enlazados aquí. Al rotar DECISIONS, archivar íntegramente las entradas retiradas y enlazar su archivo aquí. No mantener copias paralelas actualizables del mismo registro.

Markdown sigue siendo la fuente; una futura base de búsqueda deberá poder reconstruirse desde estos documentos.

## Snapshot del índice (2026-10-10)

[[98_Agent_Handoff/archive/2026-10-10_INDEX_anterior]] conserva la versión extensa del índice maestro antes de compactarlo. Es una captura histórica; para navegar y determinar estado actual, usa [[INDEX]] y las fuentes de dominio enlazadas ahí.

## Snapshot del log (2026-10-10)

[[98_Agent_Handoff/archive/2026-10-10_log_anterior]] conserva la bitácora con el detalle anterior a su compactación. [[log]] mantiene las referencias recientes; los datos de cada sesión deben consultarse en su fuente enlazada.

## Decisiones retiradas (2026-10-10)

[[98_Agent_Handoff/archive/2026-10-10_DECISIONS_archivadas]] conserva una decisión sobre el alcance y los títulos de la saga del 2026-09-16, sustituida por la arquitectura vigente de siete libros. Desde el 2026-10-12 conserva también las tres decisiones del 2026-09-21 sobre el cierre de la Parte III y los Caps. 39 y 40. Desde el 2026-10-14 conserva además Nomenclatura (09-13), Títulos del Libro I y Frontera IV/V (09-20) y Relevo compacto (09-21). En la segunda rotación del 2026-10-14 recibió Halbrook (09-28), la incubadora de Sombras y la trilogía de Elenna (10-03) y la reunión del 13 con Charles (10-04). El 2026-10-31 recibió Sombras de Poder: confirmaciones, Lunar Pearl, nombre y embarazo (10-13).

## Actualización concurrente preservada

Durante la compactación otra sesión agregó el Cap. 40. También se conservaron íntegros [[98_Agent_Handoff/archive/2026-09-21_CURRENT_BRIEF_cap40]] y [[98_Agent_Handoff/archive/2026-09-21_PENDING_cap40]]. El relevo compacto incorpora ese avance y la discrepancia Tommaso/Alessio.

- Bitácora al terminar esa sesión: [[98_Agent_Handoff/archive/log_hasta_2026-09-21_cap40]]. Conserva también el registro completo del Cap. 40.

- [[98_Agent_Handoff/archive/2026-09_sesiones]]: enlaces retirados del registro reciente.
- [[98_Agent_Handoff/archive/2026-10_sesiones]]: enlaces de octubre retirados del registro reciente.
- [[98_Agent_Handoff/archive/2026-11_sesiones]]: enlaces de noviembre retirados del registro reciente (desde el 2026-11-07; ampliado el 2026-11-09).

## Corte del 2026-10-03

Copias íntegras antes de compactar el relevo (el brief medía ~3,900 palabras):

- [[98_Agent_Handoff/archive/2026-10-03_CURRENT_BRIEF|Brief acumulado]].
- [[98_Agent_Handoff/archive/2026-10-03_PENDING|Pendientes]].

## Corte del 2026-10-04

Copias íntegras antes de compactar el relevo (el brief medía ~1,400 palabras):

- [[98_Agent_Handoff/archive/2026-10-04_CURRENT_BRIEF|Brief acumulado]].
- [[98_Agent_Handoff/archive/2026-10-04_PENDING|Pendientes]].

## Corte del 2026-10-06

Copias íntegras antes de compactar el relevo (el brief medía ~1,700 palabras; PENDING ~900), al cerrar la cascada del arco final:

- [[98_Agent_Handoff/archive/2026-10-06_CURRENT_BRIEF|Brief acumulado]].
- [[98_Agent_Handoff/archive/2026-10-06_PENDING|Pendientes]].

## Corte del 2026-10-14

Copias íntegras antes de compactar el relevo (el brief medía ~1,430 palabras; PENDING ~1,070). Los pendientes de fondo del Libro II pasaron a [[98_Agent_Handoff/BACKLOG]]; los 11 enlaces más antiguos de [[log]] pasaron a [[98_Agent_Handoff/archive/2026-10_sesiones]].

- [[98_Agent_Handoff/archive/2026-10-14_CURRENT_BRIEF|Brief acumulado]].
- [[98_Agent_Handoff/archive/2026-10-14_PENDING|Pendientes]].

## Corte del 2026-10-28

Copia íntegra antes de compactar el brief (medía ~1,450 palabras): la serie de la regla 05 (Caps. 12–22) quedó en una sola entrada con sus sesiones.

- [[98_Agent_Handoff/archive/2026-10-28_CURRENT_BRIEF|Brief acumulado]].

## Corte del 2026-10-29

Copias íntegras antes de compactar el relevo (el brief medía ~1,400 palabras; PENDING ~1,080). Las decisiones de fondo de PENDING (Fabrizio/Tommaso, lectura del libro, Cuatro Partes, Rocco) pasaron a [[98_Agent_Handoff/BACKLOG]]; los 98 enlaces más antiguos de [[log]] pasaron a [[98_Agent_Handoff/archive/2026-10_sesiones]], con su descripción.

- [[98_Agent_Handoff/archive/2026-10-29_CURRENT_BRIEF|Brief acumulado]].
- [[98_Agent_Handoff/archive/2026-10-29_PENDING|Pendientes]].

## Corte del 2026-11-04

Copias íntegras antes de compactar:

- [[98_Agent_Handoff/archive/2026-11-04_CURRENT_BRIEF|Brief acumulado]].
- [[98_Agent_Handoff/archive/2026-11-04_PENDING|Pendientes]].
- [[98_Agent_Handoff/archive/2026-11-04_DECISIONS_retiradas|Decisiones retiradas]].

## Corte del 2026-11-07

Copias íntegras antes de compactar el relevo (el brief medía ~1,300 palabras; PENDING ~830). El brief remite a los planes del Libro II y a las fichas en vez de repetir su canon. La reseña de ChatGPT de las Partes I–II y las 402 referencias dudosas pasaron de PENDING a [[98_Agent_Handoff/BACKLOG]]. Los 11 enlaces más antiguos de [[log]] (2026-10-29 a 2026-10-31) pasaron a [[98_Agent_Handoff/archive/2026-10_sesiones]], y las 8 entradas sueltas al pie de log.md se integraron al registro reciente.

- [[98_Agent_Handoff/archive/2026-11-07_CURRENT_BRIEF|Brief acumulado]].
- [[98_Agent_Handoff/archive/2026-11-07_PENDING|Pendientes]].

## Retiros de DECISIONS sin corte de relevo

- [[98_Agent_Handoff/archive/2026-11-01_DECISIONS_retiradas|2026-11-01]]: entradas desde el 2026-10-14, retiradas por el tope de 800 palabras.
- [[98_Agent_Handoff/archive/2026-11-08_DECISIONS|2026-11-08]]: entradas del 2026-11-01, retiradas para dejar sitio a la Parte III del nuevo cauce.
- [[98_Agent_Handoff/archive/2026-11-12_DECISIONS|2026-11-12]]: «Chiara en *Sombras de Poder*», «Por qué se fue Matteo», «Parte III del nuevo cauce» y las más antiguas que siguieron, retiradas para dejar sitio a las decisiones del Libro II.

## Corte del 2026-11-09

Rotación por límites, sin cambios de estado ni de canon (el brief medía 838 palabras; PENDING 845; DECISIONS 859). Diálogo de terceros (Parte I) y la protolectura de los caps. 1–8 pasaron de PENDING a [[98_Agent_Handoff/BACKLOG]]. Las dos decisiones del 2026-11-04 salieron de DECISIONS (y, el mismo día, las del 2026-11-05 y 2026-11-06, al entrar las de la Parte II y la del cierre de tarea). Los 9 enlaces más antiguos de [[log]] (2026-11-02 a 2026-11-06) pasaron a [[98_Agent_Handoff/archive/2026-11_sesiones]].

- [[98_Agent_Handoff/archive/2026-11-09_CURRENT_BRIEF|Brief acumulado]].
- [[98_Agent_Handoff/archive/2026-11-09_PENDING|Pendientes]].
- [[98_Agent_Handoff/archive/2026-11-09_DECISIONS_retiradas|Decisiones retiradas]].
