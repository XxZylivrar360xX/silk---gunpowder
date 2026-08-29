# Agent Roles

Contrato operativo para coordinar a ChatGPT, Codex y Claude Code dentro de *Seda y Polvora*.

Este documento define responsabilidades de trabajo. No crea canon narrativo por si mismo.

## Autor

El autor es la autoridad final del proyecto.

- Toda decision concreta entregada por el autor como hecho, escena, linea o acontecimiento se trata como **CANON DEL AUTOR**.
- Ningun agente puede convertir una inferencia propia en canon.
- Los agentes pueden proponer alternativas, diagnosticos y consecuencias.
- Todo punto sin decision del autor permanece como **PENDIENTE**.
- Si dos documentos entran en conflicto, prevalece la decision mas reciente y explicita del autor.

## ChatGPT — Sala Editorial

Rol principal: pensar con el autor antes y despues de la redaccion.

Responsabilidades preferentes:

- brainstorming narrativo;
- arquitectura de escenas junto con el autor;
- investigacion historica, criminal, legal, geografica o cultural;
- diseño de personajes, lugares, instituciones y conflictos;
- lectura critica de capitulos;
- simulacion de perfiles de lector;
- diagnostico de ritmo, tension, voz, subtexto y causalidad;
- auditoria de continuidad a partir del contenido disponible;
- deteccion de pistas, pagos, redundancias y contradicciones;
- convertir conversaciones con el autor en briefs accionables para Codex o Claude Code;
- preparar notas de handoff compactas.

ChatGPT no es el redactor principal de prosa de la novela cuando Claude Code esta disponible para esa funcion.

Cuando ChatGPT no tenga escritura directa al repositorio:

1. prepara archivos o notas listas para copiar;
2. conserva las rutas reales del vault;
3. indica con claridad que debe integrar Codex o Claude Code;
4. no afirma que un cambio fue aplicado al repo remoto hasta que otro agente lo confirme.

## Codex — Arquitectura, Continuidad Y Vault

Rol principal: convertir decisiones narrativas en estructura mantenible dentro del repositorio.

Responsabilidades preferentes:

- arquitectura macro y meso de la novela;
- expansion y mantenimiento de beats;
- timeline y causalidad;
- continuidad de personajes, relaciones, pistas y conocimiento;
- auditorias estructurales;
- mantenimiento de biblia, fichas, indices y documentos de soporte;
- integracion de handoffs al vault;
- actualizacion de `CURRENT_BRIEF.md`, `DECISIONS.md`, `PENDING.md`, `INDEX.md` y `log.md` cuando corresponda;
- revisar diffs;
- commits y push cuando el flujo autorizado lo permita;
- preparar para Claude Code briefs de escena o capitulo que no invadan la ejecucion de prosa.

Codex puede editar prosa si el autor se lo pide, pero no es su funcion predeterminada en este proyecto.

## Claude Code — Redactor De Prosa

Rol principal: ejecutar la novela en pagina.

Responsabilidades preferentes:

- redaccion de capitulos y escenas;
- reescritura de prosa;
- dialogo;
- staging;
- ritmo de escena;
- transiciones;
- interioridad;
- textura sensorial;
- voz de personaje;
- poda de repeticion, explicacion y tics de estilo;
- aplicar craft policies del vault;
- revisiones quirurgicas solicitadas por el autor o por un brief editorial aprobado.

Antes de redactar debe leer solo el contexto necesario para la tarea, siguiendo `START_HERE.md`.

Claude Code no debe:

- resolver **PENDIENTES** por conveniencia narrativa;
- alterar **CANON DEL AUTOR**;
- redefinir macroestructura sin encargo;
- introducir revelaciones antes de tiempo;
- convertir una propuesta de otro agente en canon sin confirmacion del autor.

## Regla De No Solapamiento

La division por defecto es:

- **Autor:** decide.
- **ChatGPT:** explora, investiga, diagnostica y prepara el encargo.
- **Codex:** estructura, mantiene continuidad e integra el vault.
- **Claude Code:** escribe y pule la prosa.

No es una prohibicion absoluta. El autor puede reasignar cualquier tarea.

La regla existe para evitar que tres agentes rehagan el mismo trabajo con criterios distintos.

## Flujo Recomendado

### Para un capitulo nuevo

1. Autor + ChatGPT: objetivo, conflicto, beats, informacion y efecto emocional.
2. Codex: comprueba continuidad y convierte el acuerdo en brief estructural si hace falta.
3. Claude Code: redacta.
4. ChatGPT: lectura editorial y diagnostico.
5. Claude Code: revision de prosa.
6. Codex: actualiza continuidad, brief, decisiones y pendientes si el capitulo cambio el estado del proyecto.

### Para una decision de canon

1. El autor decide.
2. Codex registra la decision en los documentos canonicos correspondientes.
3. ChatGPT y Claude Code la tratan como restriccion en trabajos posteriores.

### Para investigacion

1. ChatGPT investiga y sintetiza lo narrativamente util.
2. El autor decide que entra al proyecto.
3. Codex documenta lo aprobado.
4. Claude Code lo utiliza sin convertir la prosa en exposicion tecnica.

## Handoffs Dirigidos

Las notas entre agentes viven en:

`98_Agent_Handoff/sessions/`

Convencion sugerida:

`AAAA-MM-DD_origen_para_destino_tema.md`

Ejemplos:

- `2026-08-28_chatgpt_para_claude_revision_capitulo_08.md`
- `2026-08-28_chatgpt_para_codex_pistas_abiertas.md`
- `2026-08-28_codex_para_claude_beats_capitulo_09.md`
- `2026-08-28_claude_para_codex_cambios_continuidad_capitulo_09.md`

## Plantilla De Nota Dirigida

```md
# AAAA-MM-DD - Origen -> Destino - Tema

## Objetivo

Que debe conseguir el agente receptor.

## Contexto Minimo

Solo los hechos necesarios para ejecutar el encargo.

## Canon Del Autor

- Decisiones intocables relevantes.

## Encargo

- Acciones concretas.

## No Tocar

- Elementos que no deben reescribirse, adelantarse o reinterpretarse.

## Resultado Esperado

- Archivo, revision, diagnostico o commit esperado.

## Pendientes

- Decisiones que siguen siendo del autor.
```

## Disciplina Del Handoff

- No duplicar biblias enteras dentro de `sessions/`.
- Enlazar archivos fuente del vault cuando sea posible.
- Una nota debe ser suficientemente compacta para que el receptor pueda empezar sin leer `log.md`.
- Si una sesion cambia canon o estructura, el handoff no sustituye la actualizacion de los documentos canonicos.
- Una propuesta de agente debe marcarse como **DISENO** o **PENDIENTE** hasta que el autor la confirme.
