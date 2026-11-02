# 2026-10-31 — Claude Code: carretera del Libro I y candidatos a Escenas eliminadas

## Qué se hizo

- Preocupación del autor: el libro se siente como micro-arcos sin trama principal; los dos picos (corral / Il Consorzio, contra Chiara; Camp Alder / Halbrook, contra Kal) no comparten una trama que atropelle a ambos.
- Pasos 1 y 2: [[13_Auditorias/Book_01_Mascaras_De_Cristal/Carretera_Libro_I]] (DISEÑO). Columna externa: dos pasados cobran la casa; Varek, cobrador de en medio. Vigas: detonante 5, giro 1 en el 17 (propuesto), punto medio 31–32, correa 34–36, pacto 37–38, todo perdido 51–52, clímax 53–59, desenlace 60. Hueco: 18–30. Clasificación: 39 de carga, 15 puentes, 6 candidatos.
- Página para el autor (privada): https://claude.ai/artifact/CzmmYjpXaoSnN75Gn7EJB1. HTML fuente en el scratchpad de la sesión (no en el vault).
- Prosa: 214,220 palabras. Parte I: 96 mil (45 %).

## DECISIÓN DEL AUTOR (2026-10-31)

| Cap. | Archivo | Decisión |
|---|---|---|
| 6 *Sin llamar a nadie* | 05b | Fusionar (con el 5 o el 7) |
| 14 *El farol* | 11 | Escenas eliminadas |
| 16 *Por su cuenta* | 12b | Escenas eliminadas |
| 23 *Lo que nadie estaba mirando* | 19 | Escenas eliminadas |
| 28 *Nada caro* y 29 *Bajo juramento* | 23, 24 | Fusionar en uno |

**Segunda ronda (autor, 2026-10-31):** el arco de Walt (licencia, torneo, condicional, pub) queda suspendido en el Libro I y es **candidato a *Sombras de Poder***. **No se renumera hasta que la carretera quede bien armada.** Fase 1: adelante.

## Plan de ejecución (DISEÑO)

1. **HECHO 2026-10-31. Mover.** Crear `11_Books/Book_01_Mascaras_De_Cristal/Escenas_Eliminadas/` con README (qué cargaba cada escena y la fecha de salida). `git mv` de 11, 12b, 19 y `00_Plan_Arco_Walt_Condicional`; 53 enlaces del vault reescritos (34 archivos); encabezado `ESCENA ELIMINADA` + `EPUB: EXCLUDE`. `build_epub.py` sólo recorre las carpetas `Part_*`, así que el EPUB no las toma.
2. **Reubicar la carga — HECHO 2026-10-31 (DECISIÓN DEL AUTOR; prosa DISEÑO pendiente de lectura).**
   - Cap. 15 *Roma Atrii* (archivo 12): «La noche del primer torneo» y «ocupada con las mesas»; el torneo queda fuera de escena. Sale la sección del contrato de Keegan (dependía de la sociedad); texto en el README de `Escenas_Eliminadas/`.
   - Cap. 24 (archivo 20): una línea en el recuento del día de Kal: Harper, fuera de la barra de Mabel, trabaja las doce hectáreas («la tierra era buena y el agua no era suya»). La carga del 23 incluía el cambio de trabajo de Harper, que el archivo 31 cita.
   - Destilería: sin costura (siembra en el 24, el Monarch es cliente en el 27). Sin otras menciones de la condicional terminada ni del pub en los capítulos vigentes.
   - Nota de suspensión en [[02_Characters/Natalie_Keegan]]: hecha; cameo del 37 cortado el 2026-11-01.
3. **Fusiones — HECHAS 2026-11-01 (prosa DISEÑO, espera lectura):** 05b como coda del 05a, con V-1 (§Fusión del 05b); 23 + 24 en *Bajo juramento* (§Arco legal de Hoover). Fase B de Codex hecha en las dos (23 a `Escenas_Eliminadas/`, 05b retirado con `git rm`).
4. **Renumerar una sola vez, cuando la carretera quede armada** (autor; 60 → **56** con H13): Book_Map, CHAPTER_STATUS, timeline, matrices, guía de lectura del 34–60, `build_audiobook.py --estado`, INDEX.
5. **Paso 3 — HECHO 2026-11-01 (auditoría, sin prosa nueva):** los puentes 3–30 ya cierran con saldo. Carretera aprobada por el autor; [[98_Agent_Handoff/sessions/2026-11-01_claude_paso3_saldos_carretera]].

## Rediseño de la Parte I (2026-10-31)

Plan: [[11_Books/Book_01_Mascaras_De_Cristal/Part_01_Dos_Mundos/00_Plan_Rediseno_Parte_I]]. Columna: la unión invisible (canon, «catástrofe disponible») y tres ojos que se acercan: V (Monarch/Varek, el reloj), P (Palermo), K (el pasado de Kal). 8 escalones de una línea o un beat, la costura del 15 y la opción P-3 (Tommaso pregunta por los domingos). Nada aplicado.

**DECISIÓN DEL AUTOR (2026-10-31):** columna aprobada; P-3 aprobado en versión del autor (la misa para Alessio lleva a «¿todavía cabalgas los domingos?»). Escalones en estudio. **CANON DEL AUTOR:** H13 (Valenti en persona, el pañuelo y la bala, tras una vela en Santa Lucía) cierra la Parte I como capítulo propio después del 25 y sustituye a P-2. Costuras en 47, 31, 58 y Hitos.

## Arco legal de Hoover (archivos 23–24, Caps. 28–29): estudio y decisiones

**Estudio (2026-10-31, DISEÑO):** 4,612 palabras de prosa. Carga: «mi... amigo» (CANON; rima en tres tiempos con «mi... bueno. Mi amiga» de Matteo, `02:477`, y «Mi... Mi pareja», `34:404`, H21); la mentira de Tommaso (fuerza C, deuda sin cobrar); el registro semipúblico (U-1 del rediseño); Rivers/Connors; Krane y la media hoja; la participación en Villani; la moto de Nadir. Dependen: 30 (24b: detonante de Nadir, cifra, Villani), 31 (24c: abre con la mentira), 33 (25, H15: Villani), 36 (28), 40 (32: Kawasaki), **53 (44: origen de Krane, Connors «El que perdió contra ella»)**, 54–56 (45–47: Krane) y el Libro II (Krane, Rivers & Krane, el Lancia en el choque de Tommaso). El rumor de Hoover en el Monarch (`05c:427`) sólo lo cobra este arco. Corrección a la carretera: el 29 es PUENTE fuerte, no candidato; el 28 es casi todo andamio. **Hueco de la fase 1:** el 19 eliminado tenía la escena donde Chiara nombra a Rivers y la enemistad con Connors; el 23 la da por vista (`23:76` «broma sobre tomates», `23:162` «a su manera»).

**DECISIÓN DEL AUTOR (2026-10-31). EJECUTADA 2026-11-01 (puntos 1–9; prosa DISEÑO): [[98_Agent_Handoff/sessions/2026-11-01_claude_fusion_bajo_juramento]]. Fase B de Codex hecha: el 23 está en `Escenas_Eliminadas/` ([[98_Agent_Handoff/sessions/2026-10-31_codex_para_claude_bajo_juramento_mecanica]]).**

1. **Fusionar y reducir** el 28 y el 29 en un capítulo de ~3,000 palabras (~3,400 con la videollamada, salvo poda adicional). No sale del libro.
2. **Título:** *Bajo juramento*.
3. **Abre con la videollamada de los tomates** (escena eliminada del 19; no es hito, pero es un momento importante para el autor: Chiara se ríe ya sin medirse, porque tiene confianza con Kal). Trae «también estoy buscando abogado» → Rivers y Connors; repara el hueco de la fase 1. Cronología: semanas después de la compra de la parcela, con tomates verdes; cabe antes del sobre con sello.
4. **Se conserva:** el sobre y Héctor («que salga caro de la cuenta correcta»); el mensaje de Chiara con el favor de prensa (rima con el 53); Rivers en una escena (sin contrato, «cosas débiles en el orden correcto», Connors); el loft («Te estoy avisando»); la audiencia con Tommaso entrando por sorpresa, Chiara con «mi... amigo» intacto y contrainterrogatorio podado, la mentira de Tommaso íntegra, el pasillo («Tommaso, no»); el acuerdo en un párrafo, la media hoja a Krane, la escalinata y «No antes».
5. **Sale o se comprime:** la llamada de la lista de testigos; la oferta del cuarto día y «lo quiero por escrito»; contador y empleados en dos o tres líneas; la firma en Villani en una línea (el Lancia ya lo cuenta el 30, `24b:78`); Garrett y Rocco en pocas líneas, conservando el intercambio de Rocco (decisión del autor 2026-10-22).
6. **La moto de Nadir** (~440 palabras) pasa al Cap. 30 *Lo que cueste* (24b).
7. **Hoover es socio del lote** (Lote Almendra), como en el 05c y el Cap. 1; «concesionario» queda para Villani.
8. **Una línea cobra el rumor del 05c:** Hoover llegó a Tommaso por la reunión con la mesa del Monarch. El motivo de Tommaso para mentir sigue sin explicarse (REGLA DURA).
9. **Natalie:** se corta su cameo en el Cap. 46 (archivo 37, Thanksgiving, `37:220`); se respeta el CANON del 2026-10-30. Walt prepara los platos para la estación; Nat no sale en escena. Ficha con nota de suspensión.

Ejecución: `chapter-drafting` (fusión y videollamada, moto en el 24b) y `editorial-surgery` (cameo del 37). Después, `build_audiobook.py --estado`.

## Fusión del 05b en el 05a (Cap. 6 → coda del 5): estudio y decisiones

**EJECUTADA (prosa DISEÑO), 2026-11-01:** [[98_Agent_Handoff/sessions/2026-11-01_claude_fusion_05b_coda_05a]]. Coda de 2,502 palabras; capítulo de 5,854. Fase B de Codex hecha el 2026-11-01 (05b retirado con `git rm`, enlaces y tablas al día, sin renumerar): [[98_Agent_Handoff/sessions/2026-11-01_codex_para_claude_fusion_05b_mecanica]].

**Estudio (2026-11-01, DISEÑO):** 05b = 2,871 palabras de prosa (05a 3,361; 05c 3,690). Carga y dependencias:

- Rutina tras Varga y salida de carga (batería, carrito, «pídamelo el día que pueda decir que me lo pidió»); el carrito se cobra dentro del propio 05b («La rueda del carrito se rompió»).
- Cena con Blake: primera vez que se ve a Collins (lo da por hecho el encabezado del 08b), «Ésas trabajan para nosotros», «Monto» (primera mención del hipódromo en prosa: [[05_Locations/Hipodromo_Del_Monarch]]; sigue en el 06).
- Bisagra, sobre, «Usted es alta» (cobro CANON en el Libro II, La Esquina de Mabel); Walt y el teléfono de Natalie («uno de botones», cobrado en `10:56`).
- Pasillo de Tommaso: «Alessio también decía eso»; Varek preguntó por Palermo y Tommaso «le dio la versión» (escalera P de [[12_Craft_Policies/revelations/Book_01_Mascaras_De_Cristal]]).
- Registro de accesos → contrato de proveedor de Almendra, «leí una grúa» (Fabrizio), la caseta deja pasar a Kal sin llamar a nadie. Lo cobran `05c:13` (abre con la caseta), `22a:151` (gafete), `29:47` (la caseta de Varek «ya tenía su nombre») y `47:169` (rima de Chiara con la pluma).
- El beso de Blake, que contrasta con la apertura del 05c (Rocco).
- Varga ya no carga nada más: `05a:336` ya dice «—Varga no volvió.». **La primera línea del 05b repite esa frase y se reescribe al fusionar.**

**DECISIÓN DEL AUTOR (2026-11-01):**

1. **Coda del 05a**, tras «No la acomodó.». El 05c queda intacto (su primera línea sigue funcionando).
2. **Poda ligera:** el 05b baja a ~2,200 palabras; capítulo fusionado ~5,600 (título *Cliente y proveedor*). Lista de problemas más corta; salida de carga comprimida, conservando «pídamelo»; se conservan las dos salidas con Blake (el escalón «no se bajó» / «esta vez sí se bajó»).
3. **V-1 en la misma pasada**, tras la caseta: 2–3 líneas; un trámite sin nombre desde la oficina de la dirección pide el nombre completo del responsable de Almendra. Rima: la caseta deja de verlo y la dirección empieza a verlo. Administrativo, sin confirmar que Varek dirige nada (regla de [[02_Characters/Nereo_Volpi]]).
4. **Archivo 05b:** `git rm` cuando su prosa esté en el 05a; lo podado va al README de `Escenas_Eliminadas/`.

**Ejecución:** Claude, `chapter-drafting` (costura, primera línea, poda, V-1) y `editorial-surgery` (verificación). Después, **fase B de Codex:** reescribir los 14 enlaces de 9 archivos vivos que apuntan al 05b (sin tocar `sessions/` ni `archive/`); pasar el historial del encabezado del 05b al del 05a; marcar «fusionado en el 5» en Book_Map, CHAPTER_STATUS, la carretera y la matriz de renombramiento, sin renumerar; `build_audiobook.py --estado`; comprobar que el EPUB arma sin el 05b; conteo de palabras; listar los «Cap. 6» de las fichas que se refieran a *Sin llamar a nadie*, para la renumeración final.

## Preguntas abiertas para el autor

- Puntos 1, 2 y 5 del §4 de la carretera (aprobar la columna, el giro en el 17, tope de palabras).
- Destino del arco de Walt en *Sombras de Poder*: dónde cae y qué cambia (Walt seguiría en condicional durante todo el Libro I).
