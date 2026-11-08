# 2026-11-08 - Codex para Claude - Renumeracion de la Parte III

## Resultado

Por solicitud explicita del autor, Parte III renumerada a 33-47. Libro completo: 47 encabezados activos, del 1 al 47 sin huecos ni repetidos; Book_Map coincide. Nombres de archivo, titulos y prosa conservados. Archivos 37 y 39 siguen como marcadores excluidos, sin numero nuevo.

## Archivos tocados

- [[11_Books/Book_01_Mascaras_De_Cristal/Part_03_Ardizzone/35_Sin_Fecha_De_Regreso]]
- [[11_Books/Book_01_Mascaras_De_Cristal/Part_03_Ardizzone/40_Mecanico]]
- [[11_Books/Book_01_Mascaras_De_Cristal/Part_03_Ardizzone/44_Jurisdiccion]]
- [[11_Books/Book_01_Mascaras_De_Cristal/Part_03_Ardizzone/45_Ropa_Limpia]]
- [[11_Books/Book_01_Mascaras_De_Cristal/Part_03_Ardizzone/46_Llaves]]
- [[11_Books/Book_01_Mascaras_De_Cristal/Part_03_Ardizzone/47_Intereses]]
- [[11_Books/Book_01_Mascaras_De_Cristal/Part_03_Ardizzone/48_Su_Nombre]]
- [[11_Books/Book_01_Mascaras_De_Cristal/Part_03_Ardizzone/49_Enfrente]]
- [[11_Books/Book_01_Mascaras_De_Cristal/Part_03_Ardizzone/50_A_Oscuras]]
- [[11_Books/Book_01_Mascaras_De_Cristal/Part_03_Ardizzone/50b_La_Tierra_Bajo_Sus_Botas]]
- [[11_Books/Book_01_Mascaras_De_Cristal/00_Book_Map]]: filas 33-47, dos marcadores y notas de numeracion operativa. Las secciones historicas conservan sus numeros.
- [[12_Craft_Policies/CHAPTER_STATUS]]: 15 filas BORRADOR y dos FUNDIDOS; no habia filas de Parte III. Conteos y evidencia de 33-39 tomados de las notas de Fase 4, incluido el ajuste final de Al reves (~4,900). Para 40-47 se conserva como fuente la metadata de cada archivo; no se simula una revision de prosa nueva.
- [[11_Books/Book_01_Mascaras_De_Cristal/Escenas_Eliminadas/README]]: nueve versiones previas indexadas, con numeros historicos y destinos actuales.
- `tools/audiolibro/bitacora/Mascaras_De_Cristal.md` y `.json`: regenerados con --estado.

## Correccion de metadata

El archivo 40, Mecanico (nuevo 36), contenia una mencion literal del marcador de exclusion al describir el archivo 39. `is_epub_excluded` busca esa cadena en todo el archivo, por lo que el capitulo 36 quedaba fuera de audio y EPUB. Se sustituyo solo esa referencia explicativa por "marcador excluido de EPUB" dentro del comentario, sin modificar scripts ni prosa.

## Verificacion

- Comparacion de prosa antes/despues de renumerar: sin cambios, excluyendo comentarios y numero del encabezado.
- Encabezados y tabla principal: 1-47 exactos; Parte III 33-47.
- --estado ejecutado sin red ni generacion de audio. Resultado final y comprobacion completa de la bitacora al cierre, abajo.
- git diff revisado; diff --check de los archivos de esta tarea sin errores de whitespace (Git advierte conversion LF/CRLF).

## Relevo

No se modificaron CURRENT_BRIEF, PENDING, DECISIONS, log, INDEX, canon ni notas historicas. Claude debe actualizar el estado vivo, que aun dice que falta renumerar Parte III. No se regeneraron EPUB/PDF; sin commit ni push. Las referencias narrativas antiguas fuera de los indices quedan para propagacion de Claude; no se hizo sustitucion global de numeros.

**Audio final verificado:** 47 capitulos enumerados exactamente del 1 al 47, incluido Mecanico (36). 9 al dia y 38 sin audio al dia. Los marcadores 37 y 39 no aparecen como capitulos independientes.
