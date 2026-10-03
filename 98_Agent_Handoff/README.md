# Agent Handoff

Relevo entre agentes. Roles y permisos en [[98_Agent_Handoff/AGENT_ROLES]] (vigente desde 2026-10-03).

## Estructura

```text
98_Agent_Handoff/
├── README.md, START_HERE.md, AGENT_ROLES.md   ← reglas de arranque y roles
├── CURRENT_BRIEF.md, PENDING.md,              ← estado vivo (lo mantiene Claude Code)
│   DECISIONS.md, BACKLOG.md
├── ChatGPT/     ← buzon de ChatGPT: README + notas nuevas sin procesar
├── encargos/    ← encargos por etapas para Claude Code / Codex (ENCARGO_*, TRIAJE_*)
├── sessions/    ← notas de sesion y handoffs Claude <-> Codex
└── archive/     ← historial inmutable; archive/chatgpt/ = notas de ChatGPT ya procesadas o anteriores al buzon
```

## Quien escribe donde

| Espacio | Claude Code | Codex | ChatGPT |
|---|---|---|---|
| Archivos raiz (brief, pending, decisions, backlog, roles, start) | mantiene | solo lectura (reporta a Claude) | solo lectura |
| `ChatGPT/` | procesa y archiva | solo lectura | escribe (notas nuevas) |
| `encargos/` | crea y ejecuta | ejecuta lo que se le encarga | solo lectura |
| `sessions/` | escribe | escribe sus reportes | solo lectura |
| `archive/` | mueve ahi lo cerrado | no toca | solo lectura |

## Uso

1. Leer `START_HERE.md`; `AGENT_ROLES.md` si hay coordinacion entre agentes.
2. Leer `CURRENT_BRIEF.md`; revisar `PENDING.md` antes de editar.
3. Claude Code revisa `ChatGPT/` al arrancar.
4. Al cerrar, Claude Code actualiza `CURRENT_BRIEF.md` (y `DECISIONS.md` si hubo decisiones). Nota de sesion en `sessions/` si fue sustantiva.
5. Un encargo cerrado se mueve de `encargos/` a `archive/`.

Brief, PENDING y DECISIONS: maximo 800 palabras cada uno. Limites y rotacion: [[98_Agent_Handoff/START_HERE]]. Historial: [[98_Agent_Handoff/archive/README]].

## Notas Dirigidas

En `sessions/`, con nombre `AAAA-MM-DD_origen_para_destino_tema.md` (p. ej. `2026-10-03_claude_para_codex_sustitucion_nombres.md`). ChatGPT no usa `sessions/`: escribe en su buzon.

## Regla

Esto no reemplaza `CLAUDE.md`, `INDEX.md` ni `log.md`. Ninguna nota de agente crea canon por si sola. La autoridad final es el autor.
