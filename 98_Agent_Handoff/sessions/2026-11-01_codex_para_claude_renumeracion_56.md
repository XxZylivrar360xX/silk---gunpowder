# 2026-11-01 — Codex para Claude — Numeración del 2026-11-01

Encargo: [[98_Agent_Handoff/encargos/ENCARGO_Codex_Renumeracion_56]]. **Ejecutado; pendiente de verificación de Claude.** La numeración del 2026-11-01 tiene 56 capítulos; se distingue de la de 56 del 2026-10-22.

## Resultado

51 encabezados renumerados con comprobación previa contra la tabla del encargo; línea de trazabilidad añadida al principio de su comentario inicial. Los archivos 01–05a quedaron idénticos byte a byte. *Grazie* pasó del encabezado provisional 25 al 22 (el alias anterior del mapa y de estados decía 25b). Los títulos se tomaron de los encabezados.

Mapa regenerado, cinco retiradas aparte, partes I 1–22 / II 23–39 / III 40–56, arco sin Kal 49–56, Ciao en el 55 y desenlace en el 56. La columna Capítulo de CHAPTER_STATUS está actualizada, incluido el título ya vigente *Dos sillas vacías*; las otras tres columnas no cambiaron. Conserva sus 32 filas originales: 27 vigentes y 5 retiradas; no se inventaron estados para los capítulos sin fila.

Cronología del Libro I, milestones, matriz temporal e INDEX actualizados por archivo y función, porque mezclaban varias numeraciones anteriores. Las citas archivo:línea de la matriz conservan el prefijo; los números de línea citados son históricos. Se identificaron las filas retiradas y los cálculos originales de calendario no se reinterpretaron.

## Archivos tocados

65 archivos existentes respecto al estado recibido, más este reporte. Había cambios editoriales previos y archivos sin seguimiento; se conservaron.

**Capítulos (51; sólo encabezado y una línea de comentario):**

- **11_Books/Book_01_Mascaras_De_Cristal/Part_01_Dos_Mundos/**: 05c_La_Pizza_De_Calabaza.md, 06_Ambos.md, 07_La_Noche_Del_Ladrillo.md, 08_La_Carrera_De_Mascaras.md, 08b_La_Sargenta.md, 09_La_Balanza.md, 10_El_Loft_Del_Soltero.md, 12_Roma_Atrii.md, 13_Auster.md, 14_La_Regla_Del_Telefono.md, 15_El_Porton.md, 16_El_Sobre_Rojo.md, 17_Cuentas_Claras.md, 18_El_Dia_Nublado.md, 20_El_Mirador.md, 21_El_Primer_Huesped.md, 21b_Grazie.md.

- **11_Books/Book_01_Mascaras_De_Cristal/Part_02_Con_Peores_Personas_He_Tratado/**: 22a_La_Cifra.md, 22b_Con_Su_Proveedor.md, 24_Bajo_Juramento.md, 24b_Lo_Que_Cueste.md, 24c_El_Corral.md, 24d_Vienes_Conmigo.md, 25_Libros_Abiertos.md, 26_Me_Encuentro_Bien.md, 27_Riesgo_Pendiente.md, 28_La_Correa.md, 29_El_Patio_Ajeno.md, 30_Media_Baraja.md, 31_Vamos_A_Casa.md, 32_Linea_Directa.md, 33_Mas_De_La_Cuenta.md, 33b_La_Mano.md, 34_Mi_Pareja.md.

- **11_Books/Book_01_Mascaras_De_Cristal/Part_03_Ardizzone/**: 35_Sin_Fecha_De_Regreso.md, 36_Tambien_Las_Mananas.md, 37_Cuatro_Letras.md, 38_Al_Reves.md, 39_Un_Par_De_Dias_Mas.md, 40_Mecanico.md, 41_La_Otra_Mitad.md, 42_Nada.md, 43_La_Puerta.md, 44_Jurisdiccion.md, 45_Ropa_Limpia.md, 46_Llaves.md, 47_Intereses.md, 48_Su_Nombre.md, 49_Enfrente.md, 50_A_Oscuras.md, 50b_La_Tierra_Bajo_Sus_Botas.md.

**Documentos y bitácoras (14):**

- [[INDEX]]
- [[01_Timeline/02_Libro_01_Mascaras_De_Cristal]]
- [[01_Timeline/08_Matriz_Renombramiento_Capitulos_Libro_I]]
- [[12_Craft_Policies/CHAPTER_STATUS]]
- [[12_Craft_Policies/milestones/INDEX]]
- [[tools/audiolibro/bitacora/Mascaras_De_Cristal]]
- tools/audiolibro/bitacora/Mascaras_De_Cristal.json
- [[11_Books/Book_01_Mascaras_De_Cristal/00_Plan_Hilo_Tasador]]
- [[11_Books/Book_01_Mascaras_De_Cristal/00_Book_Map]]
- [[11_Books/Book_01_Mascaras_De_Cristal/00_Plan_Arco_Final_Sin_Kal]]
- [[11_Books/Book_01_Mascaras_De_Cristal/Part_01_Dos_Mundos/00_Plan_Rediseno_Parte_I]]
- [[98_Agent_Handoff/sessions/2026-10-31_claude_guia_lectura_caps34_60]]
- [[13_Auditorias/Book_01_Mascaras_De_Cristal/Carretera_Libro_I]]
- [[13_Auditorias/Book_01_Mascaras_De_Cristal/Matriz_Temporal_Libro_I]]

En los seis documentos de equivalencia se añadió exclusivamente la nota superior (y, en la guía de lectura, la tabla completa 34–60 → 30–56). El cuerpo anterior quedó idéntico, incluida la nota histórica de «56 caps.» del 2026-10-22. No se tocaron CLAUDE.md, AGENTS.md, Hitos.md, 00_Biblia/, CURRENT_BRIEF.md, PENDING.md, DECISIONS.md ni log.md. Claude conserva su actualización y el enlace de bitácora.

## Comprobaciones y salidas

- rg --no-heading "^# Capítulo" con las tres carpetas Part_0*: **56 coincidencias; números ordenados 1–56; 0 huecos; 0 repetidos.** Partes: 22 + 17 + 17.
- Comparación con copia previa a la intervención: prosa fuera de comentarios y encabezado **idéntica en los 56 capítulos**; títulos conservados; cinco primeros archivos idénticos byte a byte. En los otros 51, la única adición al comentario es la línea requerida.
- Tabla principal del mapa: **56 filas que coinciden exactamente con los encabezados**, por archivo, número y título; cinco filas fuera del libro.
- CHAPTER_STATUS: **32 identidades de fila conservadas; Estado, Última revisión y Bloqueador idénticos**, incluso al separar las retiradas.
- Enlaces: **0 destinos nuevos rotos**; el único destino añadido fue el Book_Map, existente. Ningún nombre de archivo cambió; búsqueda de enlaces wiki con ancla #Capítulo: **0**. Las rutas preexistentes se conservaron.
- format_markdown de tools/epub-build/build_epub.py: salida **idéntica antes/después para los 56 capítulos**; el encabezado pierde su número por el patrón de la línea 45. No se generó EPUB.
- git -c core.safecrlf=false diff --check -- con los 65 archivos del alcance: **exit 0, sin salida**.
- git diff --check global: **exit 2**, exclusivamente por espacios finales **preexistentes** en 02_Characters/Natalie_Keegan.md:18, archivo no tocado; además Git emite avisos de normalización LF/CRLF. No se corrigió trabajo ajeno.
- Sin generación de EPUB, PDF ni audio; sin commit ni push.

## Audiolibro

Ejecutado python -B .\tools\audiolibro\build_audiobook.py --estado (sin red). Salida: **«Bitácora: 51 sin audio al día — tools\audiolibro\bitacora\Mascaras_De_Cristal.md»**.

**Caps. 6–56 (todos los renumerados) requieren audio con el número hablado nuevo.** El script los registra literalmente como SIN AUDIO, porque busca el archivo de audio con el número nuevo; no significa que se haya borrado audio anterior. Caps. 1–5: AL DIA. *Grazie* ya estaba SIN AUDIO antes. El estado recibido tenía 37 AL DIA, 18 PENDIENTE y 1 SIN AUDIO; ahora hay 5 AL DIA y 51 SIN AUDIO. Se conservaron los audios y el historial de bitácora; no se cambió manualmente la clasificación del script.

## Referencias conservadas para que Claude decida

Las siguientes **no se corrigieron**: están fuera del alcance de sustitución o en contenido explícitamente histórico de documentos vivos. Las líneas corresponden al cierre de esta intervención. Algunas mezclan número de archivo, de capítulo y numeraciones más antiguas: no aplicar un desplazamiento global.

### Prioridad: navegación, relevo y cruces entre libros

| Documento | Líneas | Referencia conservada / motivo de posible confusión |
|---|---|---|
| [[README]] | 15 | El manuscrito llega al «capítulo 50b»; ahora desenlace 56. |
| [[11_Books/README]] | 32 | Cierre en 50b y Ciao en 50; hoy 56 y 55. |
| [[CLAUDE]] | 43 | 60 capítulos, partes/arco final 53–60 y Ciao 59; reservado a Claude. |
| [[98_Agent_Handoff/CURRENT_BRIEF]] | 3, 7, 8, 14, 15, 20, 32 | Numeración de 60, lectura 34–60, renumeración pendiente y referencias recientes. |
| [[98_Agent_Handoff/PENDING]] | 14, 18, 23, 24, 28, 53 | Arco final 50–57 y referencias de varias épocas. |
| [[98_Agent_Handoff/DECISIONS]] | 11, 13, 15, 19, 23, 27, 31 | Crowe en el 12; fusiones/retiradas y Grazie tras el 25 en numeración anterior. |
| [[98_Agent_Handoff/BACKLOG]] | 12, 36, 37, 40, 41, 42, 74, 75, 77, 80, 81 | Cruces a capítulos de épocas distintas; evaluar por archivo. |
| [[01_Timeline/01_Indice_Cronologico]] | 16, 18, 27 | Ciao 50 / Halbrook 50b; hoy 55 / 56. |
| [[01_Timeline/03_Libro_02_Sombras_De_Poder]] | 16, 45, 290, 372, 382, 413, 415, 426, 428, 453, 513, 521, 530 | Cruces al I: 50b, piano 38, italiano 8, cigarro 50, Dario 47, Eagle Eye 22/24c y Rowe 9/44. |
| [[01_Timeline/05_Libro_04_Cuentas_De_Sangre]] | 10 | Lo que Corrado hizo en el Cap. 9 (archivo 09, hoy 11). |
| [[11_Books/Book_02_Sombras_De_Poder/00_Book_Map]] | 13, 49, 61, 89, 91, 99, 100, 101, 102, 103, 104, 105, 148 | Cruces al I y tabla de deudas con números de archivo (44, 47–50b); no son números actuales. |
| [[11_Books/Book_02_Sombras_De_Poder/00_Boceto_Lista_Capitulos]] | 147, 266, 268, 288, 447 | Deuda 47 → 52; piano 38 → 43; boca del Monarch 24c → 27–28; cigarro 50 → 55. |
| [[11_Books/Book_02_Sombras_De_Poder/00_Plan_Cuatro_Partes]] | 56, 69, 73, 141 | Muñeca 9–10, piano 38, levantón 12 y mensaje 26 del I. |
| [[11_Books/Book_02_Sombras_De_Poder/00_Diseno_Cobro_Del_Levanton]] | 3, 15, 22, 37, 44, 54, 58 | Cap. 12 / archivo 09: hoy 11. |
| [[11_Books/Book_02_Sombras_De_Poder/00_Diseno_Nombre_Y_Embarazo]] | 13, 79 | Cigarro del 50: hoy 55; el mirador 20 de la línea 14 ya coincide. |
| [[11_Books/Book_02_Sombras_De_Poder/Part_02_Nieve_Y_Ceniza/00_Diseno_Robo_Joyeria]] | 51 | Boca del Monarch enseñada en el 24c, hoy 27–28. |
| [[12_Craft_Policies/voice/Leone_Valenti]] | 3, 26, 32 | Caps. 49 y 58 (archivos 40 y 49): hoy 45 y 54. |
| [[12_Craft_Policies/voice/Silas_Crowe]] | 3, 33 | Primera aparición en el 12: hoy 11. |
| [[12_Craft_Policies/voice/00_Registro_Espanol_Neutro]] | 13, 14 | Travis/Cody en 26 → 23; referencia a 23 (11) mezcla épocas. |
| [[04_Concepts/Fe_y_Velas]] | 23 | Cap. 9 y parrilla del 31; distinguir archivo 09 → 11 y 31 → 35. |

### Otros documentos de dominio con referencias anteriores

Censo de líneas con referencias numéricas conservadas en planes, guías, incubación y fichas de voz. Incluye ejemplos fechados o supersedidos dentro de documentos de uso vivo; no prescribe su actualización. Se excluyeron las carpetas históricas, fichas de Characters/Factions/Locations, ledgers, dictámenes fechados y números propios de otros libros.

| Documento | Líneas conservadas |
|---|---|
| [[00_Biblia/00_Trilogy_Structure]] | 110, 112, 124, 142, 211, 246, 264, 443, 447, 718, 752, 758, 779, 781, 797, 804 |
| [[06_Relationships/Hitos]] | 15, 24, 30, 31, 37, 38, 39, 40, 45, 46, 146, 172, 270, 276, 278, 338, 352, 511, 513, 515, 517, 519, 521, 527, 539, 549, 555, 557, 559, 563, 589, 595, 607, 609, 650, 658, 660, 670, 674, 736, 753, 807, 821, 1034, 1157, 1159, 1161, 1171, 1173, 1263, 1272, 1273, 1274, 1357, 1389, 1507, 1515, 1517, 1519, 1553, 1556, 1562, 1592, 1594, 1660, 1702, 1738, 1742, 1752, 1768, 1927, 2078, 2114, 2298, 2300, 2310, 2316, 2318, 2333, 2341, 2353, 2357, 2363, 2365, 2369, 2375, 2391, 2445, 2459, 2469, 2485, 2487, 2489, 2540, 2542, 2546, 2557, 2805 |
| [[06_Relationships/Kal_y_Chiara]] | 202, 206, 207, 295, 318, 328, 331, 341, 453, 459, 516, 543, 593, 609, 612 |
| [[06_Relationships/Momentos_de_Fractura]] | 26, 444 |
| [[07_Ideas/Corrado_Manfred_Gabe]] | 7, 23, 24, 52, 56, 75, 88, 90, 93 |
| [[07_Ideas/El_Chico_Del_Patio]] | 3, 117 |
| [[07_Ideas/El_Infarto_De_Hector]] | 3, 5, 11, 89 |
| [[07_Ideas/El_Mirador]] | 3, 5 |
| [[07_Ideas/Escenas_Guia/El_Parador_Del_Norte]] | 5, 174 |
| [[07_Ideas/Escenas_Guia/README]] | 16 |
| [[07_Ideas/Incubacion_Escenas/Libro_02_Sombras_De_Poder/Stavanger_Ya_Llego_Material_Narrativo]] | 13, 34, 442, 443 |
| [[07_Ideas/La_Graduacion_De_Marisol]] | 7, 81, 91 |
| [[07_Ideas/Libro_04_Incubadora/01_Nicholas_Voss]] | 9 |
| [[07_Ideas/Libro_04_Incubadora/02_Caso_Vera_y_Antagonista]] | 11, 14, 20, 98 |
| [[07_Ideas/Libro_04_Incubadora/05_Volpi_y_Corrado]] | 7 |
| [[07_Ideas/Origen_de_i_Sussurri]] | 3, 13, 24, 62 |
| [[11_Books/Book_01_Mascaras_De_Cristal/00_Plan_Reubicacion_Corral]] | 14, 21, 24, 26, 28, 30, 37, 57, 72, 77, 79 |
| [[11_Books/Book_01_Mascaras_De_Cristal/00_Plan_Vento]] | 5, 22, 41, 43, 60 |
| [[11_Books/Book_01_Mascaras_De_Cristal/00_Propuesta_Titulos]] | 3 |
| [[11_Books/Book_01_Mascaras_De_Cristal/Part_02_Con_Peores_Personas_He_Tratado/00_Plan_Robo_Monarch]] | 6, 12, 15, 22, 23, 26, 27, 34, 44, 52, 59, 73, 81 |
| [[11_Books/Book_01_Mascaras_De_Cristal/Part_03_Ardizzone/00_Plan_Cierre_Parte_III]] | 8, 12, 16, 17, 50, 55, 62, 64, 75, 76, 86, 90, 92, 93, 98, 112, 114, 124, 126, 140, 154, 162, 166, 167, 170, 179, 180, 184, 185, 186 |
| [[12_Craft_Policies/Redaccion_De_Capitulos]] | 24 |
| [[12_Craft_Policies/dialogue_rules/05-esticomitia-de-una-sola-voz]] | 4, 54, 56 |
| [[12_Craft_Policies/editorial/PILOT_01_10]] | 5, 7, 11, 32 |
| [[12_Craft_Policies/staging_rules/01-vineta-de-tesis-sin-encarnacion-espacial]] | 13 |
| [[12_Craft_Policies/staging_rules/03-presentacion-por-catalogo-en-vez-de-gesto]] | 4, 15, 16, 17 |
| [[12_Craft_Policies/staging_rules/04-dialogo-de-guion-sin-anclaje]] | 4, 17, 18, 19 |
| [[12_Craft_Policies/staging_rules/05-gesto-de-manos-en-serie]] | 15, 16, 17 |
| [[12_Craft_Policies/voice/Alessio_Lusardi]] | 3 |
| [[12_Craft_Policies/voice/Chiara_Bellandi]] | 3, 11, 13, 15, 26, 32, 33, 36, 37, 38, 39, 45, 47, 57, 107 |
| [[12_Craft_Policies/voice/Danny_Hayes]] | 3 |
| [[12_Craft_Policies/voice/Dario_Varek]] | 3, 10 |
| [[12_Craft_Policies/voice/Enzo]] | 3 |
| [[12_Craft_Policies/voice/Fabrizio_Rinaldi]] | 3 |
| [[12_Craft_Policies/voice/Harper_Walker]] | 3 |
| [[12_Craft_Policies/voice/Hector_Navarro]] | 3, 23, 27, 58, 59, 64 |
| [[12_Craft_Policies/voice/Irene_Salcedo]] | 3, 14, 41 |
| [[12_Craft_Policies/voice/Kal_Mercer]] | 3, 7, 9, 11, 13, 29, 35, 37, 39, 42, 44, 46, 52, 81, 86, 96 |
| [[12_Craft_Policies/voice/Lucia_Varek]] | 3, 14 |
| [[12_Craft_Policies/voice/Mabel_Ortiz]] | 3, 12 |
| [[12_Craft_Policies/voice/Marisol_Grayson]] | 3, 5 |
| [[12_Craft_Policies/voice/Matteo_Bellacorte]] | 3 |
| [[12_Craft_Policies/voice/Nadir_Amrani]] | 3 |
| [[12_Craft_Policies/voice/Natalie_Keegan]] | 3 |
| [[12_Craft_Policies/voice/Tommaso_Lusardi]] | 8 |
| [[12_Craft_Policies/voice/Walt_Keegan]] | 3 |

### Restos intencionales dentro de los archivos intervenidos

- Book_Map: notas fechadas de arquitectura/retitulado y montaje conservan sus números de época, identificados desde la nota inicial; las referencias «hoy Caps.» ya están convertidas. No se reescribieron los diseños macro históricos.
- CHAPTER_STATUS: se conservaron **todas** las referencias numéricas en Última revisión y Bloqueador (32 filas); la nota inicial explica la convención. Incluyen secuelas del Corral y costuras de Grazie de numeraciones anteriores; no se interpretaron como cambios de estado.
- Cronología del I: línea 70, H12 «Cap. 29» tachado; referencias «de entonces» y bloque histórico de H13 señalados por supersesión. La renumeración no resuelve sus descripciones superadas.
- Matriz temporal: citas archivo:línea (26:118, 31:167, 27:77 y 23:314) conservan localizadores históricos, ahora identificados como archivo; sus números de línea no se recalcularon. Diagnósticos de calendario, ropa y muestras anteriores no se reauditoran por esta tarea.
- Los 56 comentarios iniciales de capítulos contienen referencias fechadas anteriores. En particular, 21b_Grazie.md:4 aún conserva la explicación de su encabezado provisional 25; la nueva primera línea del comentario registra la renumeración. No se actualizaron esas bitácoras internas.
- Los seis documentos con nota/tabla superior conservan el cuerpo íntegro por orden expresa; los números antiguos se leen con esa equivalencia, incluida la guía del autor.
- log.md conserva sus enlaces y descripciones históricas (no se actualizó por prohibición del encargo).

## Relevo

Claude: verificar esta pasada y después actualizar los archivos de relevo, CLAUDE.md y log.md que reservó el encargo. Elegir cuáles referencias de las tablas requieren equivalencia o actualización; no se propagó nada fuera del alcance. No hace falta generar EPUB para validar esta renumeración.
