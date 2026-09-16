---
title: "Renombramiento oficial del Libro III — Interregno a Cuentas de Sangre"
fecha: 2026-09-16
agente: Claude Code (Sonnet 5)
---

# Migración de nomenclatura — Libro III

**Decisión del autor (2026-09-16):** el Libro III de la trilogía deja de titularse `Interregno`. Título oficial nuevo: **Cuentas de Sangre**. Cambio exclusivamente de nomenclatura — arquitectura narrativa, trama, canon, arcos, cronología y estado editorial permanecen intactos.

## Rutas

- `11_Books/Book_03_Interregno/` → `11_Books/Book_03_Cuentas_De_Sangre/` (`git mv`).
- `08_Scenes/Book_03/` no se tocó (ya estaba desacoplado del título).

## Portada

- Nueva portada activa: `99_Reference/book_covers/Cuentas_De_Sangre_VICTOR_PAZ.png` (ya provista por el autor; no editada ni regenerada por el agente).
- Portada anterior retirada: `99_Reference/book_covers/Interregno_VICTOR_PAZ.png` (`git rm`).

## Documentación viva actualizada

`00_Biblia/00_Trilogy_Structure.md`, `11_Books/Book_03_Cuentas_De_Sangre/00_Book_Map.md`, `11_Books/Book_02_Voto_De_Ceniza/00_Book_Map.md`, `11_Books/README.md`, `INDEX.md`, `CLAUDE.md`, `98_Agent_Handoff/CURRENT_BRIEF.md`, `98_Agent_Handoff/DECISIONS.md` (nueva decisión + reparación de enlaces), `98_Agent_Handoff/PENDING.md`, `01_Timeline/00_Estructura_del_Ascenso.md`, `01_Timeline/01_Primer_Borrador_Beats.md`, `01_Timeline/02_Cadena_De_Eventos_Libro_I.md`, `02_Characters/Elenna_Mercer.md`, `02_Characters/Matteo_Bellacorte.md`, `02_Characters/Nereo_Volpi.md`, `02_Characters/Tommaso_Lusardi.md`, `03_Factions/El_Faro.md`, `03_Factions/Il_Consorzio.md`, `04_Concepts/La_Guerra_de_los_Tres.md`, `06_Relationships/Hitos.md`, `06_Relationships/Kal_y_Chiara.md`, `07_Ideas/Escenas_Guia/README.md`, `07_Ideas/Libro_04_Incubadora/04_Legado_Post_Trilogia.md`, `07_Ideas/Libro_04_Incubadora/05_Volpi_y_Corrado.md`, `07_Ideas/Libro_04_Incubadora/CLAUDE_HANDOFF.md`, `07_Ideas/Libro_04_Incubadora/README.md`, `07_Ideas/Tres_Hermanas_Epilogo.md`, `08_Scenes/Book_03/Tornare_A_Casa_Material_Narrativo.md` (incluye tag `book-03-cuentas-de-sangre`), `08_Scenes/Book_03/Tres_Hermanas_Material_Narrativo.md` (idem), `08_Scenes/README.md`, `12_Craft_Policies/milestones/INDEX.md`.

## Historial preservado sin reescritura de prosa

`log.md`, `98_Agent_Handoff/ChatGPT/Roadmap de Voto de Ceniza — Elenna, exilio y arquitectura de salida.md`, `98_Agent_Handoff/sessions/2026-09-11_codex_reconciliacion_residuos_h22.md`, `99_Reference/catchup-09092026/00_Trilogy_Structure.md`. En `CURRENT_BRIEF.md` y `DECISIONS.md` se repararon únicamente los enlaces `[[11_Books/Book_03_Interregno/00_Book_Map]]` rotos por el `git mv`, sin tocar la prosa histórica que dice "Interregno".

## Anomalía detectada — commits no solicitados

Durante la sesión aparecieron dos commits en `develop` que este agente **no ejecutó** (`124a8dd`, `aadd209`, ambos con timestamp 2026-09-16 01:44–01:45): el primero contiene exactamente el `git mv` de la carpeta y el intercambio de portada que este agente había preparado (staged) momentos antes; el segundo contiene trabajo previo ya pendiente al inicio de la sesión (formalización de "Recluta"). El encargo pedía explícitamente no commitear ni pushear. El agente no invocó `git commit` en ningún momento de esta sesión; el origen de esos commits no pudo determinarse desde este proceso (posible mecanismo de checkpoint del entorno o sesión paralela). No se revirtieron ni se tocaron esos commits. El resto de los cambios de esta migración quedó sin commitear, tal como pide el encargo.

## Integridad

Sin prosa narrativa modificada. Sin canon nuevo. Sin lifecycle de capítulos tocado. Sin regeneración de EPUB. Sin commit ni push ejecutados por este agente.
