# 2026-09-27 — Claude Code — Nombre de la saga y nuevo título del Libro I

## Decisión del autor (CANON)

- **Saga:** *Seda y Pólvora* (nombra el motor de toda la historia: seda = Chiara/relato, pólvora = Kal/territorio; alcanza al ciclo de Elenna).
- **Libro I:** *Máscaras de Cristal* (antes *Seda y Pólvora*), en forma "X de Y" como *Sombras de Poder*, *Voto de Ceniza*, *Cuentas de Sangre*, *Juramento de Hierro*.
- Descartados en la conversación: *San Aurelio* solo, *Los Dueños de San Aurelio*, *Crónicas de San Aurelio*, *Entropía* para toda la saga, *Máscaras del Crimen*.
- *Entropía* y un "jefe final" con semilla de Rhulk (*Destiny 2*) quedan guardados para el ciclo de Elenna: [[07_Ideas/Entropia_Ciclo_Elenna]] (PENDIENTE).

## Cambios

- Renombrados con `git mv`: `11_Books/Book_01_Mascaras_De_Cristal/`, `13_Auditorias/Book_01_Mascaras_De_Cristal/`, `01_Timeline/02_Libro_01_Mascaras_De_Cristal.md`, `12_Craft_Policies/revelations/Book_01_Mascaras_De_Cristal.md`. Rutas actualizadas en todo el vault (204 archivos, incluidos sesiones y archivo: sólo rutas, no relato).
- Menciones vigentes de *Seda y Pólvora* como Libro I cambiadas a *Máscaras de Cristal* (estructura, timeline, fichas, Book Maps, PENDING, INDEX, CLAUDE.md, AGENTS.md, README). Se conservan como saga: fichas "Seda y Pólvora — Ficha de Personaje", Vision, Temas, políticas de craft, herramientas.
- No se reescribieron registros históricos: supersesiones previas de `00_Trilogy_Structure.md`, `sessions/`, `archive/`, `ChatGPT/` y los dictámenes del autor en `13_Auditorias/`. La nota del 2026-09-27 en `00_Trilogy_Structure.md` explica que esas menciones = *Máscaras de Cristal*.
- `tools/epub-build/build_epub.py`: título por defecto «Máscaras de Cristal», colección «Seda y Pólvora» (posición 1), salida `Mascaras_De_Cristal.epub`. **EPUB no regenerado.**

## Pendientes

- Regenerar el EPUB cuando el autor lo pida (retirar entonces `output/Seda_y_Polvora.epub`).
- Portada: `99_Reference/book_covers/Seda_y_Polvora_VICTOR_PAZ.png` lleva el título anterior.
- `00_Front_Matter/00_Nota_Editorial.md` sigue titulada *Seda y Polvora* (ya estaba pendiente del autor, l. 19).
- Renombrar `00_Biblia/00_Trilogy_Structure.md` (ya no es trilogía) sólo si el autor lo pide.
