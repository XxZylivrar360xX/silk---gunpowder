# Encargo: Fase 4 en paralelo, capítulos «Reusa»

Creado: 2026-11-07, Claude Code (terminal principal), por orden del autor. Vigente mientras la terminal principal avanza en orden por los nuevos Caps. 13–18.

## Contexto

Libro I, *Máscaras de Cristal*, nuevo cauce: [[11_Books/Book_01_Mascaras_De_Cristal/00_Plan_Nuevo_Cauce]]. Las Fases 0–3 están aprobadas. El mapa viejo → nuevo manda: [[11_Books/Book_01_Mascaras_De_Cristal/00_Mapa_Cauce_Cap11_Camp_Alder]] (tarjeta, POV y verbo de cada capítulo). La Fase 4 reconstruye capítulo por capítulo. Para el método, sigue como modelo el nuevo Cap. 12: [[98_Agent_Handoff/sessions/2026-11-07_claude_fase4_cap12_pov_chiara]] y su plan en `Part_01_Dos_Mundos/00_Plan_Cap12_Dos_Sillas_POV_Chiara.md`.

Para que no se crucen las terminales, éstas sólo trabajan los capítulos marcados **Reusa** en el mapa: cambian poco y dependen poco de la Parte I, que se está reescribiendo.

## Reparto

| Terminal | Nuevo cap. | Archivo | Verbo en el mapa |
|---|---|---|---|
| **B** | 19 | `Part_01_Dos_Mundos/21b_Grazie.md` | Reusa (cierra la Parte I; Il Consorzio le recuerda a Chiara su deber) |
| **B** | 20 | `Part_02_Con_Peores_Personas_He_Tratado/22a_La_Cifra.md` | Reusa y unifica el POV (Chiara; Ferreyra ya es CANON) |
| **B** | 29 | `Part_02_Con_Peores_Personas_He_Tratado/31_Vamos_A_Casa.md` | Reusa y unifica el POV (Chiara; H7) |
| **B** | 32 | `Part_02_Con_Peores_Personas_He_Tratado/34_Mi_Pareja.md` | Reusa (Kal; la palabra le llega a Crowe; cierra la Parte II) |
| **C** | 37 | `Part_03_Ardizzone/41_La_Otra_Mitad.md` | Reusa y unifica el POV (Chiara) |
| **C** | 38 | `Part_03_Ardizzone/42_Nada.md` | Reusa (Chiara; F1) |

Orden dentro de cada terminal: el de la tabla. Un capítulo a la vez y lectura del autor antes de pasar al siguiente, salvo que él diga otra cosa.

## Método por capítulo

1. Lee la fila del capítulo en el mapa y su tarjeta (enlace en el plan del nuevo cauce, tercera tanda). Lee también lo vigente que lo afecte en `Plan_Nuevo_Cauce` (fuerzas: el Tasador trabaja para Halbrook; Halbrook fuera de la prosa salvo el epílogo; Varek con policías propios, sin Lucía; Dario fuera del robo del Monarch; Vento muere en el nuevo 23).
2. Usa la skill `chapter-drafting` para escribir y `editorial-surgery` si sólo hace falta microedición.
3. Antes de tocar prosa, presenta al autor un plan corto: qué cambia, qué se conserva (líneas CANON DEL AUTOR literales) y qué se pierde. Si hay decisiones, pregúntalas. **No rellenes un PENDIENTE.**
4. Guarda la versión anterior íntegra en `Escenas_Eliminadas/` (`NN_Titulo_Version_2026-11-07.md`), como en el Cap. 12.
5. Reescribe, con un solo POV, el del dueño del capítulo según el mapa ([[12_Craft_Policies/Arquitectura_De_Perspectiva]]). Aplica la regla 06 ([[12_Craft_Policies/staging_rules/06-capitulo-de-estaciones]]) y la de diálogo 05. Objetivo: 3,500–4,000 palabras, salvo que el mapa diga otra cosa.
6. Para la **apertura por residuo** no tienes el capítulo anterior definitivo. Escribe la apertura apoyada en la tarjeta anterior del mapa y márcala en la metadata: `Costura de apertura PROVISIONAL: depende del nuevo NN`. Lo mismo para el cierre si engancha con el siguiente.
7. Deja el capítulo como `Estado: BORRADOR`, con su nota de metadata dentro del bloque `<!-- -->` del encabezado, nunca fuera.

## Lo que NO tocan B y C

- **Archivos compartidos:** `CURRENT_BRIEF.md`, `PENDING.md`, `DECISIONS.md`, `log.md`, `INDEX.md`, `CHAPTER_STATUS`, `00_Book_Map.md`, fichas de `02_Characters/`, `revelations/`, `milestones/` ni `Hitos.md`. Los edita sólo la terminal principal.
- `python -B ./tools/audiolibro/build_audiobook.py --estado` (escribe la bitácora compartida).
- EPUB, PDF, commits y push.
- Capítulos fuera de su reparto, aunque vean un error: lo anotan en su nota.

## Canon reciente que deben respetar (2026-11-07)

- **Dana Collins**, la teniente de la VED, es **ex amante de Kal** de antes de la cárcel (sustituye a Anya Voronina, retirada). Hereda «Ojos azules» y la barra del Monarch (archivo 35). En el archivo 24c, Kal le dice a Voss «Tranquilo, compañero» y Voss contesta «No soy su compañero».
- Detalle de esto y del resto de la sesión: [[98_Agent_Handoff/sessions/2026-11-07_claude_collins_sustituye_a_anya]].

## Al cerrar cada capítulo

Una nota por capítulo en `98_Agent_Handoff/sessions/2026-11-07_claude_fase4_capNN_<slug>.md` (o con la fecha del día), con:

- qué se hizo y el conteo antes → después;
- decisiones del autor (CANON) y DISEÑO del agente, separadas;
- **Para propagar (lo hace la terminal principal):** cada cambio que deba llegar a brief, log, CHAPTER_STATUS, Book_Map, fichas, ledger o hitos, uno por línea con el archivo destino;
- las costuras provisionales y de qué capítulo dependen;
- «audio PENDIENTE: archivo NN».

Termina tu respuesta al autor con una línea: `Listo para propagar: sessions/<nota>`.
