# 2026-11-01 — Codex para Claude — Fusión 05b: fase B mecánica

## Resultado

Encargo del autor ejecutado en `develop`, sin editar prosa narrativa ni renumerar. Sin commit, push ni regeneración de EPUB o audio. Se conservaron los cambios que ya existían al arrancar. `CURRENT_BRIEF.md`, `PENDING.md` y `DECISIONS.md` quedan para Claude.

Fuentes de arranque: [[CLAUDE]], [[98_Agent_Handoff/AGENT_ROLES]], [[98_Agent_Handoff/START_HERE]], [[98_Agent_Handoff/CURRENT_BRIEF]] y §«Fusión del 05b en el 05a» de [[98_Agent_Handoff/sessions/2026-10-31_claude_carretera_libro_i]].

## Verificación previa y trabajo realizado

- **Condiciones previas cumplidas antes de editar:** el 05a contenía «Me dejaron pasar sin llamar a nadie» y «Bellandi:** La rueda del carrito»; el README de `Escenas_Eliminadas/` ya tenía la entrada y el texto podado del 05b.
- Copiado íntegro el contenido del comentario HTML inicial del 05b al final del comentario inicial del 05a, bajo la línea solicitada: `Historial del antiguo Cap. 6 *Sin llamar a nadie* (05b), fusionado como coda el 2026-11-01:`.
- Ejecutado `git rm -- 11_Books/Book_01_Mascaras_De_Cristal/Part_01_Dos_Mundos/05b_Sin_Llamar_A_Nadie.md`. Su eliminación queda en el índice por efecto de ese comando; no se prepararon otros cambios para commit. Sin tocar residuos ni otros archivos de la carpeta.
- Redirigidos **7 wikilinks en 7 archivos**, conservando alias salvo las conversiones numéricas pedidas. Los alias `5b` y `Cap. 6 (archivo 05b)` pasan a `Cap. 5 (archivo 05a, antes 05b)`. En CHAPTER_STATUS, el título del antiguo 6 se conserva como etiqueta de la fila retirada.
- Actualizada sólo la referencia de capítulo/archivo del comentario inicial del 08b: la cena ahora remite al Cap. 5 (05a, antes 05b).
- Book_Map: fila 5 con conteo; fila 6 marcada **FUSIONADO en el 5 (05a), 2026-11-01**, conservando los números.
- CHAPTER_STATUS: desglosada la fila agrupada 05a–05c en sus filas 5, 6 y 7, sin renumerar; conservado el estado y cierre heredados del 5 y del 7. El 6 queda fusionado, con fecha 2026-11-01; la prosa DISEÑO sigue pendiente de lectura.
- Matriz: conserva su fila histórica agrupada `5a-5c`; dentro de ella se añadieron el conteo del 5 y el retiro/fusión del 6. **La fila histórica `6 — Ambos` quedó idéntica**: usa numeración anterior y no es el capítulo retirado.
- Carretera, §2/Parte I: sólo cambiaron las filas 5 y 6. **Sección 4 y decisiones intactas**.
- README de Escenas eliminadas: sustituida la indicación «aún en Part_01…» por el retiro con `git rm`; texto podado intacto.
- En `log.md`, enlazado este reporte dentro de la entrada existente de la fusión; se conservan 30 entradas recientes. No se modificó INDEX: la navegación a capítulos ya estaba cubierta y el reporte queda enlazado desde log.

## Conteos

Método solicitado: `len(re.sub(r'<!--.*?-->','',t,flags=re.S).split())`.

| Archivo | Palabras |
|---|---:|
| 05a fusionado — Cliente y proveedor | **5,869** |
| 05c — La pizza de calabaza | **3,690** |

**Diferencia aclarada con las 5,854 de Claude:** el método solicitado incluye los 7 tokens del encabezado Markdown y 8 separadores `***`. Si se excluyen también esos 15 tokens, da exactamente **5,854**. No hay diferencia de prosa. Frente a la meta aproximada de 5,600, el conteo solicitado queda 269 arriba (~4.8 %); sin encabezado/separadores, 254 arriba (~4.5 %). No se podó nada.

## Audiolibro

Ejecutado `python -B .\tools\audiolibro\build_audiobook.py --estado`, salida exitosa:

> Bitácora: 6 sin audio al día — tools\audiolibro\bitacora\Mascaras_De_Cristal.md

- **49 de 55** capítulos vigentes al día. Cap. 5, *Cliente y proveedor*: **PENDIENTE — cambió la prosa**.
- Los otros pendientes son los Caps. 15, 24, 29, 30 y 46, por cambios de prosa previos a esta fase B.
- El 05b ya no aparece en `capitulos` del JSON ni en las tablas vigentes del Markdown. Su historial de audio se conserva.
- Markdown y JSON regenerados exclusivamente por el script; sin red ni generación de audio. El arreglo `historial` del JSON quedó idéntico al inicial.

## EPUB

Inspección estática de `tools/epub-build/build_epub.py`: `rg -n "05b|Sin_Llamar_A_Nadie"` no devuelve coincidencias. El descubrimiento usa carpetas `Part_*` (`collect_part_sections`, líneas 143–148) y `folder.glob("*.md")` (`collect_folder`, línea 117). No hay ruta fija al archivo retirado. **No se ejecutó el generador ni se regeneró EPUB**; ésta es una comprobación estática, no una compilación.

## Inventario para la renumeración futura

Barrido con `rg` de `Cap. 6`, `Capítulo 6`, `Sin llamar a nadie`, `05b` y `5b` en fichas (`02_Characters/`, `03_Factions/`, `05_Locations/`), Hitos, Kal_y_Chiara, BACKLOG y `01_Timeline/`. Se distinguió la numeración antigua de *Ambos* y del antiguo *Una amiga*.

**Referencia al Cap. 6 que sí era Sin llamar a nadie, encontrada al inicio:**

| Archivo:línea | Texto corto | Resultado |
|---|---|---|
| `02_Characters/Dana_Collins.md:53` | `Cap. 6 (archivo 05b)`; cena con Blake y la teniente | Corregida por el punto 3 a `Cap. 5 (archivo 05a, antes 05b)` |

**Referencias de archivo/alias relacionadas, sin otro cambio por este inventario:**

| Archivo:línea | Texto corto | Estado |
|---|---|---|
| `02_Characters/Blake_Stanton.md:72` | Antes `5b`: grúa, cena, «Monto» y beso | Wikilink/alias corregidos por el punto 3 |
| `05_Locations/Hipodromo_Del_Monarch.md:13` | Antes `5b`: Blake no oye que Chiara monta | Wikilink/alias corregidos por el punto 3 |
| `01_Timeline/08_Matriz_Renombramiento_Capitulos_Libro_I.md:35` | `Sin llamar a nadie (Cap. 6, fusionado como coda del 5)` | Marca de retiro añadida por el punto 4; conservar hasta renumerar |
| `02_Characters/Natalie_Keegan.md:18` | `menciones en los archivos 05b y 05c` | **Referencia corta pendiente para Claude**, sin wikilink; no se editó |

Fuera de ese conjunto, `Part_01_Dos_Mundos/08b_La_Sargenta.md:8` decía «la vio en la cena del Cap. 6 (archivo 05b)»; quedó corregido sólo en su comentario HTML, como se pidió.

**No quedan otras menciones de Cap. 6/Capítulo 6 a Sin llamar a nadie en el conjunto inspeccionado.** Hitos, Kal_y_Chiara y BACKLOG no aportaron candidatos de ese capítulo. Las coincidencias sobre penthouse, hierba, espejo, torta, música y Danny corresponden a *Ambos* y se dejaron intactas.

## Archivos tocados

Modificados manualmente:

- `01_Timeline/08_Matriz_Renombramiento_Capitulos_Libro_I.md`
- `02_Characters/Blake_Stanton.md`
- `02_Characters/Dana_Collins.md`
- `05_Locations/Hipodromo_Del_Monarch.md`
- `11_Books/Book_01_Mascaras_De_Cristal/00_Book_Map.md`
- `11_Books/Book_01_Mascaras_De_Cristal/Escenas_Eliminadas/README.md`
- `11_Books/Book_01_Mascaras_De_Cristal/Part_01_Dos_Mundos/05a_Cliente_Y_Proveedor.md` (sólo comentario inicial)
- `11_Books/Book_01_Mascaras_De_Cristal/Part_01_Dos_Mundos/08b_La_Sargenta.md` (sólo comentario inicial)
- `12_Craft_Policies/CHAPTER_STATUS.md`
- `12_Craft_Policies/milestones/INDEX.md`
- `12_Craft_Policies/revelations/Book_01_Mascaras_De_Cristal.md`
- `13_Auditorias/Book_01_Mascaras_De_Cristal/Carretera_Libro_I.md`
- `log.md`

Retirado: `11_Books/Book_01_Mascaras_De_Cristal/Part_01_Dos_Mundos/05b_Sin_Llamar_A_Nadie.md`.

Regenerados por `--estado`: `tools/audiolibro/bitacora/Mascaras_De_Cristal.md` y `.json`.

Creado: este reporte. **Total: 17 rutas** (13 modificaciones manuales, 1 retiro, 2 archivos generados y 1 reporte nuevo).

## Verificación y anomalías

- La búsqueda inicial de `05b_Sin_Llamar_A_Nadie` arrojó **14 coincidencias en los 9 archivos esperados**, no 14 wikilinks: 7 wikilinks, 1 nombre en código en la matriz y 6 registros históricos del audio. **Ningún archivo adicional** en esa búsqueda viva.
- Tras la fase B sólo quedan las 6 menciones históricas del audiolibro en ese barrido vivo; no son wikilinks. No se reescribieron acontecimientos pasados. Sessions, archive, ChatGPT, `97_Supersedido/` y el JSON de editorial quedaron intactos; el JSON de audio sólo cambió por el script.
- Comparación con una instantánea inicial de 920 archivos: ningún archivo previo fuera del alcance cambió durante esta fase B. Prosa del 05a y del 08b idéntica tras quitar comentarios HTML; **05c idéntico completo**. Historial inicial del 05b copiado íntegro.
- Revisados los diffs de la fase B frente al estado de trabajo inicial, además de los diffs de git. `git diff --check` de los archivos de esta tarea: **sin errores**. El chequeo global detecta espacios finales **preexistentes**, sin modificar aquí, en `02_Characters/Edward_Connors.md:10` y `02_Characters/Natalie_Keegan.md:18`.
- Permanecen textos históricos/propuestas anteriores en Book_Map, milestones y otras secciones de la Carretera; se cambiaron sus destinos de enlace donde correspondía, sin hacer renumeración ni modificar decisiones del §4. Las redirecciones solicitadas dejan dos enlaces consecutivos al 05a en Book_Map y milestones; se conservaron las dos referencias originales.
- Para Claude: actualizar el relevo vivo al revisar esta fase B y, cuando toque la renumeración, atender la referencia corta de Natalie. Sin dudas bloqueantes.
