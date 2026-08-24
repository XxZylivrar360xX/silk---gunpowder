# AGENTS.md

Guía operativa para agentes que trabajen en este vault.

Este repositorio es un vault de Obsidian para la novela original *Seda y Pólvora*. No es un proyecto de software: no hay build, tests ni dependencias. El trabajo consiste en leer, ordenar, documentar y editar Markdown con cuidado de canon.

## Regla Principal

Lee [`CLAUDE.md`](CLAUDE.md) y [`98_Agent_Handoff/START_HERE.md`](98_Agent_Handoff/START_HERE.md) al inicio de cualquier sesión sustantiva. `CLAUDE.md` debe mantenerse corto; el contexto operativo vive en `98_Agent_Handoff/`.

No leas `log.md` completo salvo petición explícita. Usa `rg` para ubicar entradas concretas.

## Idioma

Responde siempre en español de México. Usa "tú". No uses voseo.

El contenido del vault se escribe en español. Los nombres de archivos y carpetas se mantienen sin tildes ni eñes cuando se creen rutas nuevas.

## Canon

Respeta la convención del vault:

- **CANON DEL AUTOR**: intocable. No lo reinterpretes, no lo sustituyas y no reescribas líneas de diálogo canon.
- **DISEÑO**: inferencias o consecuencias derivadas por el agente. Pueden discutirse.
- **PENDIENTE**: falta decisión del autor. No lo rellenes por conveniencia.

Cuando integres material nuevo del usuario, trátalo como canon del autor si lo entrega como acontecimiento, línea, escena o decisión concreta.

## Archivos Clave

- [`INDEX.md`](INDEX.md): índice maestro del vault. Actualízalo si agregas archivos o hitos mayores.
- [`98_Agent_Handoff/START_HERE.md`](98_Agent_Handoff/START_HERE.md): protocolo barato de arranque y tabla de rutas.
- [`98_Agent_Handoff/CURRENT_BRIEF.md`](98_Agent_Handoff/CURRENT_BRIEF.md): estado vivo para relevo.
- [`98_Agent_Handoff/PENDING.md`](98_Agent_Handoff/PENDING.md): pendientes activos.
- [`log.md`](log.md): bitácora larga. No es lectura de arranque.
- [`06_Relationships/Hitos.md`](06_Relationships/Hitos.md): documento central de hitos obligatorios. La trama se construye alrededor de estos hitos.
- [`06_Relationships/Cole_y_Chiara.md`](06_Relationships/Cole_y_Chiara.md): arquitectura de la relación central.
- [`00_Biblia/`](00_Biblia): visión, temas, principios narrativos y reglas del mundo.

## Relevo Entre Agentes

Usa `98_Agent_Handoff/` para handoffs compactos.

- `CURRENT_BRIEF.md`: estado actual en una pagina.
- `START_HERE.md`: ruta barata de lectura.
- `PENDING.md`: decisiones abiertas y trabajo siguiente.
- `DECISIONS.md`: decisiones recientes en formato corto.
- `sessions/`: notas breves por sesion sustantiva.

Al cerrar una sesion, actualiza `CURRENT_BRIEF.md` si cambio el foco de trabajo. Si hubo una decision importante, agregala tambien a `DECISIONS.md`.

## Flujo De Trabajo

Antes de editar:

1. Revisa `CLAUDE.md`.
2. Revisa `98_Agent_Handoff/START_HERE.md`.
3. Revisa `98_Agent_Handoff/CURRENT_BRIEF.md`.
4. Usa `INDEX.md` para ubicar archivos.
5. Lee solo los archivos directamente relacionados con la solicitud.

Al editar:

1. Mantén cambios acotados.
2. Usa enlaces Obsidian con formato `[[Carpeta/Archivo]]`.
3. No borres canon sin marcar decanonización y motivo.
4. Añade `> **PENDIENTE:**` para decisiones abiertas.
5. Actualiza `INDEX.md` y `log.md` cuando el cambio afecte navegación, canon o continuidad.

Después de editar:

1. Revisa `git diff`.
2. Resume qué cambió y qué queda pendiente.
3. No hagas commit ni push salvo que el usuario lo pida o el flujo de la sesión lo haga claramente conveniente.

## Referencia Externa

`99_Reference/` es material de inspiración externo y no es canon. No copies escenas, biografías ni formulaciones desde ahí. Antes de usarlo, lee [`99_Reference/README.md`](99_Reference/README.md).

## Reglas Narrativas Mínimas

- La relación de Cole y Chiara es la maquinaria del ascenso, no un adorno.
- Pase lo que pase, Cole y Chiara no se separan, pero el lector debe llegar a creer que sí.
- El romance avanza por trabajo compartido, escenas pequeñas y peligro, no por declaraciones limpias.
- El territorio y el relato deben avanzar juntos.
- La violencia tiene que cambiar una relación o una estructura; si no, sobra.
- La ciudad se escribe como un lugar concreto, nunca como decorado genérico.
