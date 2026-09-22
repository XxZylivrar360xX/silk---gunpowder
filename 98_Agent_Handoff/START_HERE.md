# Start Here

Entrada compacta para cualquier agente que continue el vault.

## Objetivo

Trabajar en *Seda y Polvora* sin cargar todo el contexto historico. Leer lo minimo suficiente y abrir documentos grandes solo cuando la tarea lo exija.

## Orden Barato

1. `CLAUDE.md`
2. `98_Agent_Handoff/CURRENT_BRIEF.md`
3. `98_Agent_Handoff/PENDING.md`
4. `98_Agent_Handoff/AGENT_ROLES.md` si hay coordinacion o relevo entre agentes
5. `INDEX.md`
6. Archivos especificos de la tarea

`log.md` es índice breve. Para antecedentes, buscar con `rg` en `98_Agent_Handoff/sessions/` y `98_Agent_Handoff/archive/`; no cargar el historial completo.

## Tabla De Rutas

| Necesitas | Lee |
|---|---|
| Estado actual | `98_Agent_Handoff/CURRENT_BRIEF.md` |
| Siguiente trabajo | `98_Agent_Handoff/PENDING.md` |
| Decisiones de fondo por tema | `98_Agent_Handoff/BACKLOG.md` (por demanda) |
| Historial anterior y búsqueda | `98_Agent_Handoff/archive/README.md` (por demanda) |
| Decisiones recientes | `98_Agent_Handoff/DECISIONS.md` |
| Roles de agentes | `98_Agent_Handoff/AGENT_ROLES.md` |
| Handoff de otra sesion | `98_Agent_Handoff/sessions/` |
| Mapa del vault | `INDEX.md` |
| Tesis de la novela | `00_Biblia/Vision.md` |
| Reglas de escritura | `00_Biblia/Principios_Narrativos.md` |
| Línea temporal macro | `01_Timeline/00_README.md` y `01_Timeline/01_Indice_Cronologico.md` |
| Acontecimientos por libro | `01_Timeline/02_Libro_01_Seda_y_Polvora.md` a `06_Libro_05_Camino_A_Casa.md` |
| Kal/Chiara | `06_Relationships/Kal_y_Chiara.md` |
| Hitos canon | `06_Relationships/Hitos.md` |
| Fracturas | `06_Relationships/Momentos_de_Fractura.md` |
| Voto de Ceniza / Guerra de los Tres | `04_Concepts/La_Guerra_de_los_Tres.md` |
| Reparto | `02_Characters/Auditoria_Reparto.md` |

## Regla De Contexto

Primero buscar, luego leer. Preferir:

- `rg -n "termino" archivo.md`
- `Get-Content -TotalCount` o `-Tail`
- lectura de secciones concretas

Evitar:

- abrir archivos históricos completos;
- abrir `Hitos.md` completo si solo se necesita un hito;
- resumir al chat lo que ya quedo escrito en el vault.

## Coordinacion Entre Agentes

La division predeterminada esta en `98_Agent_Handoff/AGENT_ROLES.md`.

Resumen:

- Autor: decide.
- ChatGPT: sala editorial, investigacion, diagnostico y briefs.
- Codex: arquitectura, continuidad, mantenimiento e integracion del vault.
- Claude Code: redaccion y revision de prosa.

Si una sesion deja trabajo dirigido a otro agente, crear una nota breve en `98_Agent_Handoff/sessions/`.

## Cierre De Sesion

Si hubo cambio sustantivo:

1. Crear una nota breve en `sessions/` con fecha, agente, resultado, fuentes, verificación y pendientes. El detalle se registra una sola vez.
2. Actualizar `CURRENT_BRIEF.md` sustituyendo estado superado, no anteponiendo la sesión. Máximo 800 palabras: foco, estado, fuentes, restricciones y siguiente paso.
3. Actualizar `PENDING.md`: sólo trabajo inmediato abierto, máximo 800 palabras. Retirar lo resuelto y dejar su resultado en la nota de sesión. Pasar decisiones de fondo a `BACKLOG.md`; no cerrarlas por inferencia.
4. Registrar decisiones nuevas brevemente en `DECISIONS.md`, con fuente. Máximo 800 palabras; archivar entradas antiguas antes de retirarlas y enlazar el archivo desde `archive/README.md`.
5. Si cambió canon, continuidad o estructura, añadir a `log.md` un enlace de una línea a la sesión. Máximo 30 enlaces recientes; mover los anteriores a un índice `archive/AAAA-MM_sesiones.md`, enlazado desde `archive/README.md`.
6. Actualizar navegación en INDEX cuando corresponda. Verificar diff, límites y enlaces. No modificar copias históricas para hacerlas coincidir con canon posterior.

Antes de reemplazar un archivo compartido, comprobar que no cambió desde su lectura; incorporar primero cualquier actualización de otra sesión. Markdown es la fuente; no se requiere base de datos.
