# Encargo para Codex: renumeración y propagación mecánica de la Parte II

Creado: 2026-11-08, Claude Code, por orden del autor. La Parte II del nuevo cauce (nuevos 20–32) está redactada. Este encargo cubre **sólo lo mecánico**. El canon lo propaga Claude Code (ver «Fuera de alcance»). Contrato: [[98_Agent_Handoff/AGENT_ROLES]], sección Codex.

Modelo a seguir: la renumeración de la Parte I, [[98_Agent_Handoff/sessions/2026-11-08_claude_renumeracion_parte_I]]. Usa el mismo criterio: **los archivos conservan su nombre**; cambian el encabezado, las filas y las notas de numeración.

## Tabla de renumeración (manda)

| Nuevo | Archivo (`Part_02_Con_Peores_Personas_He_Tratado/`) | Título | POV | Encabezado hoy → nuevo | Nota de sesión |
|---|---|---|---|---|---|
| 20 | `22a_La_Cifra` | La cifra | Chiara | 23 → 20 | `2026-11-07_claude_fase4_cap20_la_cifra` |
| 21 | `22b_Con_Su_Proveedor` | Con su proveedor | Kal | 24 → 21 | `2026-11-08_claude_fase4_cap21_con_su_proveedor` |
| 22 | `24b_Lo_Que_Cueste` | Lo que cueste | Kal | 26 → 22 | `2026-11-08_claude_fase4_cap22_lo_que_cueste` |
| 23 | `24c_El_Corral` | Oveja entre lobos | Kal | 27 → 23 | `2026-11-08_claude_fase4_cap23_oveja_entre_lobos` |
| 24 | `24d_Vienes_Conmigo` | Vienes conmigo | Chiara | 28 → 24 | `2026-11-08_claude_fase4_cap24_vienes_conmigo` |
| 25 | `25_Libros_Abiertos` | Libros abiertos | Chiara | 29 → 25 | `2026-11-08_claude_fase4_cap25_libros_abiertos` |
| 26 | `26_Me_Encuentro_Bien` | Me encuentro bien | Chiara | 30 → 26 | `2026-11-08_claude_fase4_cap26_me_encuentro_bien` |
| 27 | `29_El_Patio_Ajeno` | Una silla | Kal | 33 → 27 | `2026-11-08_claude_fase4_cap27_una_silla` |
| 28 | `30_Media_Baraja` | Media Baraja | Chiara | 34 → 28 | `2026-11-08_claude_fase4_cap28_media_baraja` |
| 29 | `31_Vamos_A_Casa` | Vamos a casa | Chiara | 35 → 29 | `2026-11-07_claude_fase4_cap29_vamos_a_casa` |
| 30 | `32_Linea_Directa` | Línea directa | Kal | 36 → 30 | `2026-11-08_claude_fase4_cap30_linea_directa` |
| 31 | `33_Mas_De_La_Cuenta` | Lo único que es mío | Chiara | 37 → 31 | `2026-11-08_claude_fase4_cap31_lo_unico_que_es_mio` |
| 32 | `34_Mi_Pareja` | Mi pareja | Kal | 39 → 32 | `2026-11-08_claude_fase4_cap32_mi_pareja` |

**Retirados** (ya están en `Escenas_Eliminadas/` con `EPUB: EXCLUDE`, y no existen en `Part_02_.../`):

| Archivo | Título | Retirado al hacer | Destino |
|---|---|---|---|
| 24 | Bajo juramento | nuevo 22 | `Escenas_Eliminadas/24_Bajo_Juramento_Version_2026-11-08` |
| 27 | Riesgo pendiente / Lleve equipaje | nuevo 28 | `Escenas_Eliminadas/27_Riesgo_Pendiente_Version_2026-11-08` |
| 28 | No hace falta / La correa | nuevo 27 | `Escenas_Eliminadas/28_La_Correa_Version_2026-11-08` |
| 33b | La mano | nuevo 23 | `Escenas_Eliminadas/33b_La_Mano_Version_2026-11-08` |

Las notas de sesión están en `98_Agent_Handoff/sessions/`. De cada una, lee sólo la sección «Para propagar»: el conteo de palabras y las líneas que tocan los archivos de la lista de abajo.

## Tareas

1. **Encabezados.** En cada uno de los 13 archivos, cambia `# Capítulo NN — …` al número nuevo de la tabla. Añade una línea dentro del bloque `<!-- -->` del encabezado: `Renumerado 2026-11-08 (nuevo cauce, Parte II): antes Cap. NN.` No toques la prosa.
2. **[[11_Books/Book_01_Mascaras_De_Cristal/00_Book_Map]].**
   - Las filas de la Parte II pasan a los Caps. 20–32 de la tabla. Los cuatro retirados van con «—» y el enlace a su copia en `Escenas_Eliminadas/`, igual que los marcadores de la Parte I.
   - Actualiza la nota de cabecera: la Parte II ya está en la numeración del cauce y desaparece el hueco 20–22.
   - Revisa si la Parte III (archivos 35 en adelante) ya lleva los encabezados del cauce (33–47). Si no, **no la toques**: anótalo en el reporte.
3. **[[12_Craft_Policies/CHAPTER_STATUS]].** Filas de la Parte II con su número y título nuevos, el estado BORRADOR, la fecha 2026-11-08 y el conteo de la nota de sesión. Los retirados quedan como `RETIRADO`, con enlace a su copia. Añade una línea de cabecera como la de la Parte I.
4. **[[11_Books/Book_01_Mascaras_De_Cristal/Escenas_Eliminadas/README]].** Las filas que pidan las notas: cada `*_Version_2026-11-08` de la Parte II y los cuatro retirados.
5. **Enlaces rotos.** Busca con `rg` los enlaces vivos a `Part_02_Con_Peores_Personas_He_Tratado/24_Bajo_Juramento`, `/27_Riesgo_Pendiente`, `/28_La_Correa` y `/33b_La_Mano`.
   - Fuera de `sessions/`, `archive/` y `Escenas_Eliminadas/`, apúntalos a su copia retirada.
   - La nota del 28 nombra ya algunos: `02_Characters/Warren_Halbrook.md`, `00_Book_Map.md` y `06_Relationships/Hitos.md`. **En `Hitos.md` sólo cambia la ruta del enlace**, ni una palabra más.
   - No reescribas las notas fechadas de planes y sesiones: conservan la numeración con que se escribieron.
6. **Audio.** Corre `python -B ./tools/audiolibro/build_audiobook.py --estado` (sin red, no genera audio).
   - Comprueba que la Parte II sale del 20 al 32, sin números repetidos con la Parte III. Los repetidos de antes eran el 35 y el 39.
   - Comprueba que los archivos 24, 27, 28 y 33b ya no aparecen.
   - Si algo no cuadra, repórtalo; no edites el script.
7. **Verificación final.**
   - `rg "^# Capítulo"` en `Part_02_.../` da 20–32 sin huecos ni repetidos.
   - No queda ningún enlace vivo a los cuatro retirados fuera de las carpetas exentas.

## No tocar

- La prosa de ningún capítulo.
- El canon: `06_Relationships/Hitos.md` (salvo la ruta del enlace del punto 5), `12_Craft_Policies/revelations/`, `milestones/`, las fichas de `02_Characters/` (salvo rutas de enlace), `voice/` y `00_Mapa_Cauce_Cap11_Camp_Alder.md`.
- `CURRENT_BRIEF.md`, `PENDING.md`, `DECISIONS.md`, `log.md` e `INDEX.md`.
- EPUB, PDF, commits y push.

## Reporte

Déjalo en `98_Agent_Handoff/sessions/2026-11-08_codex_para_claude_renumeracion_parte_II.md`, con:

- los archivos tocados;
- los enlaces corregidos;
- la salida resumida de `--estado`;
- lo que no cuadró o quedó sin resolver.

## Fuera de alcance: lo hace Claude Code después

Propagar el canon de las 13 notas: `Hitos.md`, `revelations/`, `milestones/`, las fichas de personaje y de voz, el «Avance de la Fase 4» del mapa del cauce, `CURRENT_BRIEF`, `PENDING` y `log`. Claude revisa además el reporte de Codex.
