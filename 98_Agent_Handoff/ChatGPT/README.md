# Buzon ChatGPT

Canal de comunicacion de ChatGPT (incubadora de ideas crudas del autor) hacia Claude Code (maintainer principal). Reglas completas en [[98_Agent_Handoff/AGENT_ROLES]] (seccion "Limites De Escritura").

## Canales

- **Lectura: el repositorio de GitHub** (`XxZylivrar360xX/silk---gunpowder`, rama `develop`). Es la fuente de verdad para consultar canon, capitulos, fichas y estado del proyecto. Refleja lo ultimo que se subio con push; si algo parece desactualizado, preguntar al autor.
- **Escritura: la carpeta `98_Agent_Handoff/` en Google Drive.** Es el unico canal de escritura. Buzon: `98_Agent_Handoff/ChatGPT/`.

No usar el Drive como fuente de lectura del canon, ni escribir en GitHub. El resto de `98_Agent_Handoff/` (`AGENT_ROLES`, `START_HERE`, `CURRENT_BRIEF`, `PENDING`, `DECISIONS`, `BACKLOG`, `sessions/`) es solo lectura para ChatGPT.

## Reglas

1. ChatGPT solo escribe en este buzon. Fuera de `98_Agent_Handoff/` todo es **solo lectura**; cualquier modificacion fuera requiere solicitud explicita del autor para ese cambio concreto.
2. **Solo escribe cuando el autor lo autoriza** ("guarda esto"). Propone la nota en el chat primero si el autor no la pidio directamente.
3. **No todo merece nota.** Solo cuando salga una idea nueva, una decision del autor, una consecuencia que Claude deba revisar o un pendiente que valga conservar. Una revision que termina en "esta bien" no va al buzon.
4. **Un tema = un archivo**, autocontenido: `YYYY-MM-DD_tema.md`. Si una conversacion mezcla varias ideas del mismo tema, se condensan en una sola nota.
5. **Buzon plano:** sin subcarpetas.
6. **No duplicar el sistema de estado:** nada de `CURRENT_BRIEF_CHATGPT.md`, `PENDING_CHATGPT.md`, copias de fichas, biblia, timeline o capitulos. La nota **apunta** al repo, no lo reproduce. ChatGPT entrega notas; Claude mantiene el estado.
7. Crear archivos nuevos en lugar de editar notas anteriores (Drive sincroniza con retraso). No borrar nada sin pedirlo el autor.
8. Lo que llega aqui es propuesta: no es canon hasta que el autor lo valide y Claude Code lo integre (o lo descarte).

## Plantilla De Nota

```md
# Tema

## Objetivo
Que problema o idea se trabajo.

## Contexto minimo
Solo lo necesario para entender de donde sale la conversacion.

Archivos relacionados:
- [[11_Books/.../Capitulo]]
- [[02_Characters/Personaje]]

## Canon del autor
Solo decisiones que el autor dijo explicitamente en la conversacion.
- CANON DEL AUTOR: ...

## Propuestas
- DISENO: ideas prometedoras, aun no canon.
- PENDIENTE: abiertos, alternativas incompatibles, continuidad por comprobar.

## Preguntas para el autor
Solo lo que sigue necesitando decision.
```

Para lectura critica o auditoria, agregar al final:

```md
## Diagnostico
## Riesgos detectados
## Recomendaciones
```

## Nota De Migracion (volcado de una incubadora)

Cuando el autor diga "migra", "prepara la migracion" o similar, ChatGPT usa este formato sin que se lo tengan que pegar. Para pasar al buzon todo lo acumulado en una conversacion larga. Nombre: `YYYY-MM-DD_migracion_<incubadora>.md`. Si pasa de ~40 items, partir en varias notas por bloque tematico (`..._migracion_<incubadora>_parte1.md`).

```md
# Migracion — <Incubadora>

## Alcance
Libro(s), partes o arcos que cubre. Periodo de la conversacion.

## Decisiones
Cada item es atomico (una sola decision) y lleva ID para poder propagarlo por partes.

### M-01 — <titulo corto>
- Estado: CANON DEL AUTOR | DISENO | PENDIENTE
- Enunciado: una o dos frases, sin justificacion larga.
- Choca con el repo: [[ruta/archivo]] dice "<cita breve>" | No choca | No verificado
- Archivos afectados: [[ruta/archivo]], [[ruta/archivo]]
- Depende de: M-xx (si aplica)

### M-02 — ...

## Descartado
Ideas que se exploraron y el autor rechazo (una linea cada una), para que no se reintroduzcan.

## Preguntas para el autor
Numeradas, cada una ligada a su M-xx.
```

Reglas de la nota de migracion:

- CANON DEL AUTOR solo si el autor lo dijo explicitamente; ante la duda, DISENO.
- Comparar contra `develop` antes de escribir: todo choque con el repo se declara en "Choca con el repo". Es lo mas importante de la nota.
- Rutas reales del repo, no nombres aproximados.
- Sin prosa de capitulo ni resumen narrativo de la conversacion.

## Procesamiento (Claude Code)

Al arrancar sesion, Claude revisa las notas nuevas y, con validacion del autor, las convierte en canon, `PENDING`, decision, ajuste de capitulo o Book Map, o las descarta. Las notas ya procesadas se mueven a `98_Agent_Handoff/archive/chatgpt/` para que el buzon solo muestre lo pendiente.
