# AGENTS.md

Guía operativa para agentes que trabajen en este vault.

Este repositorio es un vault de Obsidian para la novela original *Seda y Pólvora*. No es un proyecto de software: no hay build, tests ni dependencias. El trabajo consiste en leer, ordenar, documentar y editar Markdown con cuidado de canon.

## Regla Principal

Lee [`CLAUDE.md`](CLAUDE.md) al inicio de cualquier sesión sustantiva. Ese archivo contiene la guía completa heredada del trabajo previo con Claude Code y gobierna el estilo, la estructura del vault, las reglas narrativas y la convención de canon.

Este archivo no sustituye a `CLAUDE.md`; lo resume para agentes.

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
- [`log.md`](log.md): bitácora de sesiones. Registra decisiones relevantes, archivos tocados y pendientes nuevos.
- [`06_Relationships/Hitos.md`](06_Relationships/Hitos.md): documento central de hitos obligatorios. La trama se construye alrededor de estos hitos.
- [`06_Relationships/Cole_y_Chiara.md`](06_Relationships/Cole_y_Chiara.md): arquitectura de la relación central.
- [`00_Biblia/`](00_Biblia): visión, temas, principios narrativos y reglas del mundo.

## Flujo De Trabajo

Antes de editar:

1. Revisa `CLAUDE.md`.
2. Revisa `INDEX.md`.
3. Lee los archivos directamente relacionados con la solicitud.
4. Verifica pendientes existentes con búsqueda de texto si hace falta.

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
