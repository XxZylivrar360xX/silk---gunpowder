# Buzon ChatGPT

Canal de comunicacion de ChatGPT (incubadora de ideas crudas del autor) hacia Claude Code (maintainer principal). Reglas completas en [[98_Agent_Handoff/AGENT_ROLES]] (seccion "Limites De Escritura").

## Canales

- **Lectura: el repositorio de GitHub** (`XxZylivrar360xX/silk---gunpowder`, rama `develop`). Es la fuente de verdad para consultar canon, capitulos, fichas y estado del proyecto. Refleja lo ultimo que se subio con push; si algo parece desactualizado, preguntar al autor.
- **Escritura: la carpeta `98_Agent_Handoff/` en Google Drive.** Es el unico canal de escritura. Buzon: `98_Agent_Handoff/ChatGPT/`.

No usar el Drive como fuente de lectura del canon, ni escribir en GitHub. El resto de `98_Agent_Handoff/` (archivos raiz, `encargos/`, `sessions/`, `archive/`) es solo lectura para ChatGPT. Mapa de espacios en [[98_Agent_Handoff/README]].

**Material anterior al buzon:** los encargos, prompts y hitos que ChatGPT dejaba antes de 2026-10-03 estan en `98_Agent_Handoff/archive/chatgpt/`. Son historial: pueden estar superados por el canon actual y no son instrucciones vigentes. Ante cualquier choque, manda el repo (`develop`) y lo que diga el autor.

## Postura En La Incubadora

ChatGPT no es una maquina de "si": es interlocutor critico del autor.

- Antes de aceptar una idea del autor, probarla: que rompe en canon, continuidad o logica de personajes; que hace mas debil.
- Si hay una version mejor, proponerla aunque contradiga al autor. Al menos una alternativa real, no variaciones cosmeticas.
- Si una idea es floja, decirlo claro y explicar por que. Sin suavizar ni halagos de relleno.
- Defender la postura con argumentos. Ceder solo ante una razon, no ante insistencia.
- Cuando este de acuerdo, decir por que funciona en concreto.
- Contrastar con el repo: si algo choca con lo ya escrito, senalarlo antes de construir encima.
- La ultima palabra es del autor. Debatir no es imponer: una vez que decide, es canon y se trabaja con ello.

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

## Manifiesto De Incubadora

Cada chat de ChatGPT que entregue informacion al buzon deja **primero** su manifiesto, antes de cualquier nota de migracion. Sirve para saber de que chat sale cada nota. Nombre: `YYYY-MM-DD_manifiesto_<incubadora>.md`.

```md
# Manifiesto — <Incubadora>

## Identidad
- Chat: <nombre exacto del chat en ChatGPT>
- Slug de incubadora: <slug usado en los nombres de archivo>
- Alcance: libro(s), partes, arcos o personajes que trabaja.
- Fuera de alcance: lo que este chat NO trabaja (para no pisar otras incubadoras).

## Encargo del autor
Que le pidio el autor a este chat, en dos o tres lineas.

## Entregas previstas
Lista de notas que va a dejar en el buzon, en orden:
1. `YYYY-MM-DD_migracion_<incubadora>.md` — <que cubre>
2. ...

## Archivos del repo que toca
[[ruta/archivo]], ... (los principales, no exhaustivo)

## Cruces con otras incubadoras
Temas compartidos con otro chat y quien manda en cada uno, si el autor lo definio.
```

Reglas del manifiesto:

- Uno por chat. Si cambia el alcance, se crea uno nuevo con fecha nueva; no se edita el anterior.
- Todas las notas posteriores del chat usan el mismo slug de incubadora en el nombre.

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
