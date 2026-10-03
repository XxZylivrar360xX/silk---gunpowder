# Agent Roles

Contrato operativo para coordinar a Claude Code, Codex y ChatGPT dentro de *Seda y Polvora*.

Este documento define responsabilidades de trabajo. No crea canon narrativo por si mismo.

**Vigente desde 2026-10-03.** Sustituye la division anterior (ChatGPT sala editorial / Codex arquitectura y vault / Claude Code solo prosa).

## Jerarquia

1. **Autor:** decide. Autoridad final.
2. **Claude Code:** maintainer principal del repositorio.
3. **Codex:** apoyo de mantenimiento, por encargo.
4. **ChatGPT:** incubadora de ideas crudas; escritura restringida a `98_Agent_Handoff/`.

Si dos agentes discrepan sobre el estado del vault, manda lo que registre Claude Code, salvo decision posterior y explicita del autor.

## Autor

- Toda decision concreta entregada por el autor como hecho, escena, linea o acontecimiento se trata como **CANON DEL AUTOR**.
- Ningun agente puede convertir una inferencia propia en canon.
- Los agentes pueden proponer alternativas, diagnosticos y consecuencias.
- Todo punto sin decision del autor permanece como **PENDIENTE**.
- Un libro **SELLADO** (solo lo declara el autor) esta terminado y listo para lectura de terceros: su texto queda congelado. Ningun agente lo edita sin orden explicita del autor; los choques con decisiones posteriores se reportan, no se propagan.
- Si dos documentos entran en conflicto, prevalece la decision mas reciente y explicita del autor.
- El autor puede reasignar cualquier tarea a cualquier agente.

## Claude Code — Maintainer Principal

Rol principal: responsable global del repositorio: prosa, canon, continuidad, estructura y documentacion de relevo.

Responsabilidades:

- redaccion, reescritura y revision quirurgica de prosa;
- arquitectura macro y meso, beats, timeline y causalidad;
- continuidad de personajes, relaciones, pistas y conocimiento;
- registrar decisiones del autor en los documentos canonicos;
- mantenimiento de biblia, fichas, `INDEX.md`, `log.md`, `CURRENT_BRIEF.md`, `PENDING.md`, `DECISIONS.md` y `BACKLOG.md`;
- revisar el buzon `98_Agent_Handoff/ChatGPT/` al arrancar sesion y procesar lo que llegue (integrar, descartar o convertir en PENDIENTE, siempre con validacion del autor);
- encargar a Codex tareas acotadas y revisar su resultado;
- revisar diffs; commits y push solo cuando el autor lo pida;
- regenerar EPUB/PDF segun `CLAUDE.md`.

Claude Code no debe:

- resolver **PENDIENTES** por conveniencia narrativa;
- alterar **CANON DEL AUTOR**;
- convertir una propuesta de otro agente en canon sin confirmacion del autor.

## Codex — Apoyo De Mantenimiento

Rol principal: ejecutar tareas de mantenimiento acotadas que encarguen el autor o Claude Code.

Responsabilidades tipicas:

- auditorias pequenas y verificaciones puntuales;
- analisis cortos (conteos, busquedas, cruces de referencias);
- sustituciones masivas y renombrados;
- correccion de enlaces, frontmatter e indices;
- herramientas auxiliares bajo `tools/`.

Reglas:

- Trabaja por encargo concreto; no abre frentes propios ni redefine estructura.
- No redacta prosa de la novela salvo pedido explicito del autor.
- No toca canon, `Hitos.md`, `00_Biblia/00_Trilogy_Structure.md` ni decisiones del autor sin encargo explicito.
- No actualiza `CURRENT_BRIEF.md`, `PENDING.md` ni `DECISIONS.md` por iniciativa propia: deja un reporte para Claude Code.
- Al terminar, deja reporte breve en `98_Agent_Handoff/sessions/AAAA-MM-DD_codex_para_claude_tema.md` con archivos tocados y lo que quedo sin resolver.
- Commits y push solo cuando el autor lo pida.

## ChatGPT — Incubadora De Ideas

Rol principal: conversar con el autor sobre ideas crudas y dejarlas por escrito para que Claude Code las procese.

Responsabilidades:

- brainstorming narrativo y exploracion de ideas del autor;
- investigacion historica, criminal, legal, geografica o cultural;
- lectura critica y diagnostico cuando el autor lo pida;
- convertir conversaciones con el autor en notas o briefs para Claude Code.

Todo lo que produce ChatGPT es **propuesta**: no es canon ni DISENO aprobado hasta que el autor lo valide y Claude Code lo integre.

### Limites De Escritura (Google Drive)

Canales de ChatGPT:

- **Lectura:** el repositorio de GitHub (`XxZylivrar360xX/silk---gunpowder`, rama `develop`) es su fuente de lectura del canon y del estado del proyecto.
- **Escritura:** la carpeta `98_Agent_Handoff/` en Google Drive es su unico canal de escritura. No escribe en GitHub.

Reglas obligatorias:

- **Solo escribe dentro de `98_Agent_Handoff/`.** Buzon preferente: `98_Agent_Handoff/ChatGPT/`, un archivo por mensaje, nombre `YYYY-MM-DD_tema.md`.
- **Todo lo que esta fuera de `98_Agent_Handoff/` es solo lectura.** Crear, modificar, mover o borrar algo fuera de esa carpeta requiere solicitud explicita del autor para ese cambio concreto. La autorizacion no se extiende a otros cambios ni a conversaciones posteriores.
- Dentro de `98_Agent_Handoff/`, crear archivos nuevos en lugar de editar los de otros agentes (Drive sincroniza con retraso y puede generar copias en conflicto). No editar `CURRENT_BRIEF.md`, `PENDING.md`, `DECISIONS.md`, `START_HERE.md` ni este archivo.
- Nunca borrar archivos, tampoco dentro de `98_Agent_Handoff/`, sin pedirlo el autor.
- No afirmar que algo quedo integrado al vault hasta que Claude Code lo confirme.
- No redactar prosa final de la novela para insertarse directamente.

## Flujo Recomendado

### Idea nueva

1. Autor + ChatGPT exploran la idea.
2. ChatGPT deja nota en `98_Agent_Handoff/ChatGPT/`.
3. Claude Code la lee, la contrasta con canon y continuidad, y la presenta al autor.
4. El autor decide; Claude Code integra o la registra como PENDIENTE.

### Capitulo nuevo o revision

1. Claude Code prepara contexto, beats y continuidad (con ideas de ChatGPT si las hay).
2. Claude Code redacta o revisa.
3. Claude Code actualiza brief, decisiones, pendientes e indices.
4. Si hace falta un barrido mecanico (sustituciones, enlaces, conteos), lo encarga a Codex.

### Decision de canon

1. El autor decide.
2. Claude Code la registra en los documentos canonicos.
3. Codex y ChatGPT la tratan como restriccion.

## Handoffs Dirigidos

Mapa de espacios y permisos por carpeta: [[98_Agent_Handoff/README]]. Encargos por etapas en `98_Agent_Handoff/encargos/`.

Notas entre agentes en `98_Agent_Handoff/sessions/` (excepto ChatGPT, que usa su buzon).

Convencion: `AAAA-MM-DD_origen_para_destino_tema.md`

Ejemplos:

- `2026-10-03_claude_para_codex_sustitucion_nombres.md`
- `2026-10-03_codex_para_claude_reporte_enlaces_rotos.md`
- `98_Agent_Handoff/ChatGPT/2026-10-03_idea_escena_bodega.md`

## Plantilla De Nota Dirigida

```md
# AAAA-MM-DD - Origen -> Destino - Tema

## Objetivo
## Contexto Minimo
## Canon Del Autor
## Encargo
## No Tocar
## Resultado Esperado
## Pendientes
```

## Disciplina Del Handoff

- No duplicar biblias enteras dentro de `sessions/` ni del buzon.
- Enlazar archivos fuente del vault cuando sea posible.
- Una nota debe ser suficientemente compacta para empezar sin leer `log.md`.
- Un handoff no sustituye la actualizacion de los documentos canonicos (eso lo hace Claude Code).
- Una propuesta de agente se marca como **DISENO** o **PENDIENTE** hasta que el autor la confirme.
