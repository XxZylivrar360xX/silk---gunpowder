# 2026-10-10 - Codex - Auditoría global de mantenimiento del vault

## Dictamen

Sí necesita mantenimiento. La arquitectura general del universo está bien separada —biblia, timeline, fichas, relaciones, lugares, libros, políticas y handoff— y `11_Books` ya concentra correctamente la prosa. El problema principal no es que falten carpetas: son las rutas y los estados viejos que siguen activos en puntos de entrada, más duplicación que encarece encontrar la fuente vigente.

## Alcance y método

- Inventario: 653 archivos, 564 Markdown; se revisaron los puntos de entrada, los siete mapas, las carpetas de libro, reglas de handoff, archivos de control y el árbol principal.
- Revisión estática de enlaces: 4,709 wikilinks en 383 Markdown operativos (excluye archivo histórico, sesiones, buzon, referencias externas y plantillas). Salieron 20 destinos no resolubles por ruta; se contrastaron ejemplos con el árbol. No todos equivalen a enlaces rotos: hay rutas a carpetas y nombres de capítulos/personajes que requieren decidir el destino correcto.
- Esto es una auditoría de mantenimiento, navegación y coherencia de estado. No es lectura línea por línea de los capítulos ni una auditoría integral de canon.
- No se editó canon ni prosa durante esta auditoría. La revisión partió de cambios previos del usuario/Codex que ya estaban en el árbol (`11_Books/README.md`, el mapa del Libro II y `99_Reference/archivos_externos/`); se conservaron.

## Hallazgos priorizados

### P1 — README raíz describe un proyecto que ya no existe

`README.md` afirma que no hay prosa de capítulos, presenta el proyecto como cimientos y dirige a `10_Chapters/`, carpeta que no existe. El manuscrito vive en `11_Books/`; el Libro I llega al 50b y el Libro II ya contiene borradores. El orden de lectura también recomienda `01_Timeline/00_Estructura_del_Ascenso.md` sin advertir la jerarquía vigente de `00_Biblia/00_Trilogy_Structure.md`. Un agente o lector nuevo puede arrancar con instrucciones y escala superadas.

### P1 — INDEX es voluminoso y conserva rutas obsoletas

`INDEX.md` mide ~87 KB / 11,986 palabras y mezcla navegación con largos resúmenes de capítulos, sesiones y decisiones ya guardadas en sus fuentes. Sus avisos superiores eran de septiembre; enlazaba `10_Chapters/README` y la carpeta `07_Ideas/Escenas_Guia` como si fuera una nota. La guía sigue en `07_Ideas/Escenas_Guia/README.md`; `08_Scenes/` es un dominio separado. También había rutas a la matriz de renombramiento con el número `07_` cuando el archivo actual es `08_Matriz_Renombramiento_Capitulos_Libro_I.md`. La referencia a EPUB de 44 capítulos era una foto fechada y podía confundirse con el montaje vigente.

### P1 — Dos fuentes discrepan sobre el estado editorial

`98_Agent_Handoff/CURRENT_BRIEF.md` dice que ningún capítulo está TERMINADO. Sin embargo, `12_Craft_Policies/CHAPTER_STATUS.md` registra capítulos TERMINADO y la metadata actual de C01 sigue diciendo TERMINADO, incluso después de cambios fechados el 2026-10-08. El lifecycle exige aprobación expresa del autor para ese estado. Hay que reconciliar el brief con el ledger y la metadata antes de usar TERMINADO como señal de cierre; esta auditoría no decide cuál cambiar.

### P1 — Enlaces operativos rotos o dirigidos a destinos antiguos

La revisión encontró rutas antiguas de capítulos fusionados/renumerados, como `16_Cuatro_Letras` (ahora `16_El_Sobre_Rojo`) y `44_A_Oscuras` (ahora `50_A_Oscuras`); referencias a `Kingsley_Field` sin nota de ese nombre; enlaces a carpetas de libro en vez de `00_Book_Map`; y la matriz con número viejo. Cinco imágenes referenciadas desde `character_art/` existen actualmente en `character_props/`: el problema es de rutas, no de archivos faltantes. Conviene reparar destinos existentes y marcar como PENDIENTE solo lo que realmente necesite una decisión.

### P2 — Los documentos de relevo y bitácora se desalinearon

`log.md` contiene 30 entradas y ~2,058 palabras; el protocolo pide una línea de enlace por sesión, con el detalle en `sessions/`. `CURRENT_BRIEF.md` está en ~804 palabras frente al máximo de 800; `PENDING.md` ronda el límite. `DECISIONS.md` tiene fecha de modificación del 2026-10-04, mientras que H23 (boda / «Il Mondo») se registró el 2026-10-09 en Hitos y en el log, no en DECISIONS. Revisar decisiones importantes recientes y reducir el log al formato de índice.

### P2 — Índices y mapas consumen demasiado para orientar

`INDEX.md` es más extenso que varios documentos de canon. `11_Books/Book_01.../00_Book_Map.md` mide ~91 KB; `06_Relationships/Hitos.md`, ~252 KB; `00_Biblia/00_Trilogy_Structure.md`, ~58 KB. Son fuentes valiosas y no deben truncarse a ciegas, pero los mapas de entrada deben priorizar estado vigente y enlaces por tarea; supersesiones e historial repetido deberían poder consultarse sin cargar toda la referencia.

### P3 — Higiene de archivos auxiliares

Hay nueve `.pyc` rastreados en `tools/editorial/checks/__pycache__/`; `.gitignore` no declara exclusiones Python. No afectan el canon y sí agregan ruido binario al mantenimiento. También llegó `99_Reference/archivos_externos/` con el paquete de ERP que originó esta conversación; `99_Reference/README.md` todavía no lo cataloga, aunque sí fija que el material externo no es canon.

## Uso y estado de `11_Books`

- Libro I: carpetas de partes con manuscrito; `00_Front_Matter` sirve al montaje editorial.
- Libro II: borradores en Partes I y II; Parte III está vacía como carpeta local prevista.
- Libros III–VII: mapas sin carpetas de partes, coherente con que sus desgloses aún no están aprobados.

No recomiendo borrar partes solo porque hoy tengan pocos archivos. Antes hay que distinguir scaffolding confirmado de carpetas residuales. La guía de consulta añadida a `11_Books/README.md` y la corrección de estado en el mapa del Libro II ya resuelven dos problemas concretos detectados antes de esta auditoría.

## Secuencia recomendada de mantenimiento

1. Actualizar README raíz e INDEX: quitar rutas muertas, señalar jerarquía de fuentes y convertir INDEX en catálogo breve por dominio.
2. Reconciliar TERMINADO entre brief, ledger y metadata; revisar DECISIONS contra decisiones del 2026-10-09/10.
3. Corregir los enlaces activos y recuperar, reemplazar o retirar de las fichas las imágenes ausentes.
4. Compactar log y bajar el peso de los mapas de entrada mediante secciones vigentes enlazables; conservar el archivo histórico intacto.
5. Excluir y retirar los `.pyc` rastreados; catalogar el material externo nuevo bajo `99_Reference/`.
6. Después, revisar carpetas locales poco usadas con el criterio de uso confirmado, no solo su recuento de archivos.

## Límites

No se modificaron estos documentos durante la auditoría. Los hallazgos de enlace son candidatos estáticos; las rutas con alias, anchors o estructura deliberada deben confirmarse al hacer el barrido de reparación. No se ejecutó la auditoría editorial de prosa ni se infirió canon.

## Mantenimiento iniciado (2026-10-10)

Tras cerrar el dictamen se actualizaron README raíz y `08_Scenes/README.md`, y se compactó `INDEX.md`; su versión extensa quedó archivada. También se corrigieron el estado del manuscrito en CURRENT_BRIEF, el registro H23 en DECISIONS, rutas de capítulos y mapa, referencias a Kingsley Field e imágenes de personaje, y se catalogó `archivos_externos/`. `log.md` quedó en formato de índice y los nueve `.pyc` se retiraron. El segundo barrido estático encontró 0 destinos sin resolver en 384 notas operativas (4,432 enlaces). La revisión de carpetas poco usadas queda para otra ronda.
