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

No leer `log.md` completo. Usar `rg` sobre `log.md` si hace falta ubicar una sesion.

## Tabla De Rutas

| Necesitas | Lee |
|---|---|
| Estado actual | `98_Agent_Handoff/CURRENT_BRIEF.md` |
| Siguiente trabajo | `98_Agent_Handoff/PENDING.md` |
| Decisiones recientes | `98_Agent_Handoff/DECISIONS.md` |
| Roles de agentes | `98_Agent_Handoff/AGENT_ROLES.md` |
| Handoff de otra sesion | `98_Agent_Handoff/sessions/` |
| Mapa del vault | `INDEX.md` |
| Tesis de la novela | `00_Biblia/Vision.md` |
| Reglas de escritura | `00_Biblia/Principios_Narrativos.md` |
| Fases | `01_Timeline/00_Estructura_del_Ascenso.md` |
| Outline macro | `01_Timeline/01_Primer_Borrador_Beats.md` |
| Cole/Chiara | `06_Relationships/Cole_y_Chiara.md` |
| Hitos canon | `06_Relationships/Hitos.md` |
| Fracturas | `06_Relationships/Momentos_de_Fractura.md` |
| Parte III / Guerra | `04_Concepts/La_Guerra_de_los_Tres.md` |
| Reparto | `02_Characters/Auditoria_Reparto.md` |

## Regla De Contexto

Primero buscar, luego leer. Preferir:

- `rg -n "termino" archivo.md`
- `Get-Content -TotalCount` o `-Tail`
- lectura de secciones concretas

Evitar:

- abrir `log.md` completo;
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

1. Actualizar `CURRENT_BRIEF.md`.
2. Agregar decision corta a `DECISIONS.md` si aplica.
3. Actualizar `PENDING.md` si cambio el siguiente trabajo.
4. Crear nota corta en `sessions/` si ayuda al relevo o deja un encargo dirigido.
5. Actualizar `log.md` si cambio canon, continuidad o estructura.
