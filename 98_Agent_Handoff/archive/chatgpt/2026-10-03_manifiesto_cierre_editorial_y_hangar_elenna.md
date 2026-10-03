# Manifiesto — Cierre editorial y hangar Elenna

## Identidad

- Chat: conversación actual de *Seda y Pólvora*; el título exacto visible en la UI no está disponible para esta herramienta.
- Slug de incubadora: `cierre_editorial_y_hangar_elenna`
- Alcance: lectura crítica del cierre editorial del Libro I discutida en esta conversación; transición conceptual hacia *Sombras de Poder*; incubación del payoff familiar Chiara–Elenna en la despedida del hangar de *Camino a Casa*.
- Fuera de alcance: mantenimiento del repo; integración de canon; edición de `CURRENT_BRIEF`, `PENDING`, `DECISIONS`, `START_HERE` o `AGENT_ROLES`; prosa final; arquitectura vigente del arco final del Libro I cuando `develop` haya supersedido conclusiones anteriores de esta conversación.

## Encargo del autor

El autor utilizó esta conversación para revisar críticamente el cierre editorial del Libro I y detectar costuras entre sus partes, y después para incubar el cierre emocional de Chiara y Elenna en el hangar.

Antes de migrar se contrastó la conversación contra `develop`. Las conclusiones editoriales que ya fueron absorbidas por auditorías, encargos o arquitectura posterior del repo no deben duplicarse ni reintroducir estados supersedidos. La migración priorizará únicamente decisiones y propuestas que sigan vivas y que Claude Code deba evaluar o propagar.

## Entregas previstas

1. `2026-10-03_migracion_cierre_editorial_y_hangar_elenna.md` — decisiones y pendientes vivos de esta incubadora, con énfasis en cartas de Chiara, raíces de San Aurelio, reconocimiento de Elenna como policía y payoff `Estoy orgullosa de ti, Elenna`.

## Archivos del repo que toca

- [[07_Ideas/Libro_04_Incubadora/06_Escenas_Faro]]
- [[07_Ideas/Libro_04_Incubadora/03_Relaciones_Elenna]]
- [[02_Characters/Elenna_Mercer]]
- [[02_Characters/Chiara_Bellandi]]
- [[11_Books/Book_05_Juramento_De_Hierro/00_Book_Map]]
- [[11_Books/Book_06_Camino_A_Casa/00_Book_Map]]
- Como antecedente editorial solamente: auditorías y encargos vigentes del Libro I bajo `13_Auditorias/` y `98_Agent_Handoff/encargos/`.

## Cruces con otras incubadoras

- El estado de `develop` manda sobre cualquier conclusión anterior de esta conversación acerca del cierre o numeración del Libro I.
- Si una auditoría o decisión ya existe en el repo, esta incubadora no la duplica: sólo migra material nuevo o todavía no propagado.
- Claude Code, como maintainer principal, decide cómo convertir las notas del buzón en canon, PENDIENTE, ajustes de fichas, escenas faro o Book Maps, siempre con validación del autor.
