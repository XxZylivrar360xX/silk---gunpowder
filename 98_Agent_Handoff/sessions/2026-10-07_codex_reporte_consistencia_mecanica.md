# 2026-10-07 — Codex — Reporte de consistencia mecánica

## Alcance

Auditoría de navegación y referencias en documentos vigentes, con contraste de `INDEX.md`, brief, línea temporal, mapas de libros y estructura macro. Las menciones dentro de `archive/`, `sessions/` y bloques expresamente supersedidos se trataron como historial. No se modificó canon ni se corrigieron archivos.

## Discrepancias

1. **Enlace roto a la matriz de títulos (prioridad alta).** `11_Books/Book_01_Mascaras_De_Cristal/00_Book_Map.md:28` y `98_Agent_Handoff/DECISIONS.md:43` enlazan `[[01_Timeline/07_Matriz_Renombramiento_Capitulos_Libro_I]]`, ruta inexistente. La matriz vigente está en `01_Timeline/08_Matriz_Renombramiento_Capitulos_Libro_I.md`; `INDEX.md:198` usa la ruta correcta.

2. **Rangos de capítulos de las Partes I y II desfasados en el índice.** `INDEX.md:187` dice Parte I C01–C26 y Parte II C27–C34. El estado vigente en `98_Agent_Handoff/CURRENT_BRIEF.md:11` las registra como Parte I 1–25 (con 24b y 24c) y Parte II 26–34. El propio `INDEX.md:187` también conserva la frase “Cap. 32 — La periferia”, aunque el brief sitúa la Parte II en 26–34; revisar la ficha al sincronizar los rangos.

3. **Epílogo frente a capítulo 50b.** `01_Timeline/02_Libro_01_Mascaras_De_Cristal.md:5` describe el mapa como tres Partes “más el epílogo”. La supersesión del mismo archivo (`:9`) y `11_Books/Book_01_Mascaras_De_Cristal/00_Book_Map.md:352` ubican el Cap. 50b dentro de la Parte III; `INDEX.md:187` dice que la carpeta de epílogo se retiró. La descripción de alcance del timeline quedó desactualizada o ambigua.

4. **Conteo de libros en el índice.** `INDEX.md:190` llama a `01_Indice_Cronologico` la continuidad de “los seis libros”; el propio índice enumera los libros I–VII en `INDEX.md:194–200`, y `01_Timeline/01_Indice_Cronologico.md` también declara siete.

5. **Resumen viejo de la Parte III sigue junto al vigente.** `11_Books/Book_01_Mascaras_De_Cristal/00_Book_Map.md:350` presenta los Caps. 35–44 como diez capítulos y dice que el 44 cierra el Libro I. La nota de esa línea aclara que ese 44 se rehízo como “Jurisdicción” y que “A oscuras” pasó al 50; la sección siguiente (`:352`) da el arco vigente 44–50b. La supersesión se puede reconstruir, pero el resumen viejo queda visible como afirmación junto al actual.

## Pendiente para Claude Code

Confirmar y sincronizar las referencias/rangos señalados. No se tomó ninguna decisión de canon ni se editaron los documentos fuente.
