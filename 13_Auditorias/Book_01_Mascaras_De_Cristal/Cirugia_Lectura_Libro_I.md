# Cirugía de la lectura corrida (Libro I)

Plan de trabajo, en marcha desde el 2026-11-21 (DECISIÓN DEL AUTOR sobre el método). Fuente de hallazgos: [[13_Auditorias/Book_01_Mascaras_De_Cristal/Lectura_Corrida_Libro_I_2026-11-21]], junto con lo pendiente del [[13_Auditorias/Book_01_Mascaras_De_Cristal/Audit_Presellado_Libro_I]] y los detalles inventados en los barridos de diálogo ([[98_Agent_Handoff/sessions/2026-11-21_claude_pingpong_libro_I]]).

## Método (aprobado por el autor)

1. Los capítulos se trabajan **en orden, del 1 al 47, uno a la vez y en la sesión principal**, sin agentes en paralelo que editen.
2. **Ficha del capítulo**, con los hallazgos en tres grupos:
   - **Seguro:** réplicas infladas por los barridos de hoy, glosa, tics, erratas y lo que ya decidió el autor. Lo aplica el agente.
   - **Decisión del autor:** se le pregunta en una tanda corta, con opciones.
   - **Canon intocable:** en lista visible.
3. Se aplica con la skill `editorial-surgery`.
4. **Verificación doble:**
   - Automática: el revisor de canon (incluidas las escenas que el encabezado marca como literales), `pingpong_audit.py` y `--cortas`.
   - Un **segundo lector**: un agente nuevo, sin el razonamiento previo, lee el capítulo arreglado y marca lo forzado y las contradicciones.
5. Se muestra al autor el antes y el después de cada cambio no mecánico, y se hace **un commit por capítulo**.
6. Al cerrar cada Parte se regeneran EPUB, PDF y audio (incremental), se actualiza el brief y se sugiere `/clear` o una terminal nueva.

**Regla aprendida (2026-11-21):** al alargar una réplica, el añadido trae un dato o una acción, nunca una explicación de lo que ya se vio.

## Lecciones de los barridos del 2026-11-21 (leer antes de empezar)

1. **Herramientas** (desde la raíz; `-I -X utf8` evita errores de codificación en Windows):
   - `python -I -X utf8 tools/editorial/canon_check.py ARCHIVO.md` compara contra HEAD y avisa si se perdió una cita protegida; `--contra <commit>` compara contra otra versión.
   - `python -I -X utf8 tools/editorial/pingpong_audit.py ARCHIVO.md` detecta ping-pong; con `--cortas` mide las réplicas de ≤3 palabras (regla 06).
2. **Límite del revisor:** no detecta las notas que protegen una escena entera sin citar líneas («la moto de Nadir, literal salvo la primera frase»; «Literales: la llamada, el Penthouse…»; «la escena de Collins»). En los barridos de hoy esas escenas se tocaron y hubo que restaurarlas: la moto del 22 (24b), cuatro escenas del 34 (36) y Collins en el 33 (35). **Antes de editar, leer el encabezado completo y listar a mano las escenas literales.**
3. **No repartir la edición en agentes paralelos.** Los forks perdieron canon tres veces: la ciabatta del 31, «¿Depende de qué?» del 3 y «El dentista no tiene un casino» del 4. Los agentes sirven para leer (el segundo lector), no para editar.
4. **Las réplicas infladas de hoy** están listadas por capítulo en la lectura corrida: se recortan o se revierten. Detalles inventados por los barridos, por verificar: ver [[98_Agent_Handoff/sessions/2026-11-21_claude_pingpong_libro_I]].
5. **Excepciones aprobadas** (reglas 05 y 06; no se tocan): los ojos del 3, la vela del 13, «Ladro» del 31, los dos tramos de H21 del 32 («Chiaraaa…» y «Mi pareja»), la moto de Nadir del 22 y la llave del 34; la llamada y la rampa del 4 (literales, restituidas); el cap. 4 entero queda sobre la vara de la regla 06 (33 %), por la llamada, la rampa y la ventanilla (DECISIÓN DEL AUTOR).
6. **Eco entre libros:** la ciabatta del 31 se repite literal en *Ya llegó* (Libro II). Si se toca una, se toca la otra.
7. **Capítulo no es archivo.** La tabla de abajo da la equivalencia. La lectura corrida usa número de capítulo y, entre paréntesis, el prefijo de archivo; las notas de sesión de hoy a veces usan el prefijo. Las líneas citadas son de la prosa del 2026-11-21 y pueden haberse movido.
8. **Otra sesión puede estar editando el Libro I.** El 2026-11-21 lo hizo «Editorial Libro 1». Correr `git status` antes de abrir cada archivo y no tocar lo que aparezca modificado sin saber de quién es.
9. **Audio del Libro I suspendido** hasta cerrar esta cirugía (28 de 47 caps. al día). EPUB y PDF se regeneran al cerrar cada Parte con la skill `regenerar-y-subir`; mientras tanto, commit por capítulo sin regenerar.
10. **Encabezado completo, sin recortar** (aprendido en el cap. 4): las notas «se conservan literales…» suelen estar al final de líneas larguísimas; cortarlas con `cut` las esconde. Si el encabezado pesa más de ~10 KB, buscar en él con grep «literal|intact|canon|se conserva». Comparar contra `b834809` lo que el barrido tocó en esas escenas y restituirlo.
11. **Vara de la regla 06:** varios capítulos ya estaban sobre el 25 % antes de esta cirugía; los recortes no deben subirlo. Si la escena es canon o de radio, se pregunta al autor por la excepción (aprobadas: caps. 4, 5, 7, 10, 11, 17, 18, 19, 22, 23 y 27, en la regla 06). Para cortar un ping-pong que abre un recorte, usar un beat de narración de más de 12 palabras, no otra explicación.
12. **Herramientas en Windows:** escribir los scripts de reemplazo con Write en el scratchpad y correrlos con `python -I -X utf8 script.py ARCHIVO </dev/null`; nunca `python -` ni `cat >` sin entrada, que dejan la terminal colgada.

## Decisiones transversales (DECISIÓN DEL AUTOR, 2026-11-21)

1. **Luz en invierno** (41, 42, 45 y 47): se conservan las horas y se corrige lo que se ve. En el 47, «hacia las 5, primeras luces» pasa a «todavía de noche», y la primera luz llega después, dentro de la escena.
2. **Chiara y Meiko:** Chiara la tutea; Meiko le habla de usted y le dice «señora».
3. **El Peugeot a la vista:** una sola línea de lógica, temprano (nadie le ha visto la cara, las placas cambian, Kal es soberbio con ese coche). La noche de la incursión (cap. 35) Kal va en el Audi.
4. **Redundancia entre POV** (13–16): la segunda versión se reduce a una línea, salvo lo que el primer POV no podía ver.
5. **Salto a junio** (16→17): una línea al abrir el 17 que marque el tiempo transcurrido; «una semana entera» pasa a «semanas» y sale «el martes».
6. **Nadir sabe lo que no vio** (22 y 24): en el 21, media línea en la que Kal le pasa el parte a Nadir.
7. **Los Varek:** en el pasillo del 20, un gesto entre Dario y Lucía que muestre el parentesco sin decirlo, y que Kal registra.

**Seguros ya decididos antes:**
- Peugeot: Chiara sabe desde el 7 (D5); en el 8 y el 9 «lo había armado» pasa a confirmar.
- Volpi no se escribe en el Libro I (D8); sale del 36.
- Nadir y Chiara se hablan de usted hasta el atentado y de tú después (ficha de Nadir).
- Chiara le habla de usted a Héctor (escena literal del 34).

## Seguimiento

**Arrastres para capítulos siguientes** (vistos al operar uno anterior; se atienden al llegar a su capítulo):
- ~~Cap. 3: «pastillas de freno del Ford»~~ resuelto: el 3 dice «la treinta y uno».
- ~~Cap. 4: el segundo pleito de la pintura~~ resuelto (sale el Taurus).
- ~~Cap. 5: la teniente~~ falsa alarma (lo dice Chiara y pregunta Kal).
- ~~Cap. 9: el malvavisco~~ resuelto (debajo del asiento).
- ~~Cap. 9: «Lo había armado»~~ resuelto (D5).
- ~~Cap. 14: el chico de la cerca~~ resuelto (una línea).
- Ficha de Chiara (l. ~330, «se disculpa sin argumentar»): desde el cap. 13 defiende la red y pierde (DECISIÓN DEL AUTOR); ajustar al cerrar el libro.
- ~~Cap. 16: «los meseros de la Isla»~~ resuelto («La Isla»).
- ~~Cap. 10: martes y jueves~~ resuelto («los martes a las diez»).
- ~~Cap. 22: la hoja arrancada frente a la doblada~~ resuelto («La hoja que Kal no dobló»).
- ~~Cap. 25: «Una semana antes»~~ resuelto («No hacía ni dos semanas»).
- ~~Cap. 26: «neurólogo»~~ resuelto («La neurocirujana»).
- Lenguaje neutro (DECISIÓN DEL AUTOR, 2026-11-21: «todo hay que neutralizarlo»): «¿vale?» pasa a «¿sí?» (hechos el 23 y el 27); «arcén» a «acotamiento»; «grifo» a «llave». Quedan «grifo» en los caps. 2 y 8 (archivos `02` y `07`), para la pasada final; revisar cada capítulo que siga.
- ~~Cap. 28: las fotos en la barra del loft~~ resuelto («Las recogí de la barra antes de salir»).
- «Me explico» de Chiara: sale el del 28; quedan el 27, el 31 y el 32. Dejar uno o dos al operar el 31 y el 32.
- Cap. 30 (costura 29→30): «Ella había dicho que lo arreglaría mañana» (en el 29 sólo lo decide), «de la noche anterior» (no hay café en el 29) y «lo giró»/«lo empujó».
- Cap. 33: revisar otra vez la apertura (costura 32→33: la amenaza de los aretes se cobra con «No te muevas de ahí») cuando la sesión de la Parte II cierre el 32. Arrastres de la II hacia la III: se atienden al final de la III (DECISIÓN DEL AUTOR, 2026-11-21).
- ~~Peugeot → Audi «la noche de la incursión»~~ resuelto en el cap. 39 (archivo `43_La_Puerta`; la línea no estaba en el 35).

| Cap. | Título | Archivo | Transversal | Estado | Commit |
|---|---|---|---|---|---|
| 1 | Un hombre de negocios intachable | `01_Un_Hombre_De_Negocios_Intachable` | Peugeot (línea de lógica) | hecho, BORRADOR | `1938c39` |
| 2 | Demasiado listo | `02_Demasiado_Listo` |  | hecho, BORRADOR | ver git log |
| 3 | Lo que no cambió | `03_Los_Viejos_Dias` |  | hecho, BORRADOR | ver git log |
| 4 | Tarifa nocturna | `04_Tarifa_Nocturna` |  | hecho, BORRADOR | ver git log |
| 5 | Cliente y proveedor | `05a_Cliente_Y_Proveedor` |  | hecho, BORRADOR | ver git log |
| 6 | Sólo una cena | `05c_La_Pizza_De_Calabaza` |  | hecho, BORRADOR | ver git log |
| 7 | Ambos | `06_Ambos` | tuteo prematuro; Peugeot D5 | hecho, BORRADOR | ver git log |
| 8 | La noche del ladrillo | `07_La_Noche_Del_Ladrillo` | Peugeot D5 («lo confirmó») | hecho, BORRADOR | ver git log |
| 9 | Mandorla | `08_La_Carrera_De_Mascaras` | Peugeot D5 | hecho, BORRADOR | ver git log |
| 10 | Una pésima idea | `08b_La_Sargenta` |  | hecho, BORRADOR | ver git log |
| 11 | La balanza | `09_La_Balanza` |  | hecho, BORRADOR | ver git log |
| 12 | La invitada | `10_El_Loft_Del_Soltero` | salida de la casa común (una línea) | hecho, BORRADOR | ver git log |
| 13 | Roma Atrii | `12_Roma_Atrii` | redundancia POV (el 13 es la primera versión; se reduce en el 14) | hecho, BORRADOR | ver git log |
| 14 | Con miedo y todo | `14_La_Regla_Del_Telefono` | redundancia POV (el chico de la cerca en una línea) | hecho, BORRADOR | ver git log |
| 15 | Yo lo llevo | `15_El_Porton` | redundancia POV (casino y cuarto en una línea) | hecho, BORRADOR | ver git log |
| 16 | Canal Seco | `17_Cuentas_Claras` | redundancia POV (prohibición al chico, fuera); salto a junio (cae en el 17) | hecho, BORRADOR | ver git log |
| 17 | Día nublado | `18_El_Dia_Nublado` | salto a junio («el resto de la primavera»; «semanas») | hecho, BORRADOR | ver git log |
| 18 | En lo pequeño | `20_El_Mirador` |  | hecho, BORRADOR | ver git log |
| 19 | Grazie | `21b_Grazie` |  | hecho, BORRADOR; cierra la Parte I (EPUB y PDF regenerados) | ver git log |
| 20 | Algo más que dinero | `22a_La_Cifra` | gesto Varek; tiempo desde el 19 (cuatro días) | hecho, BORRADOR | ver git log |
| 21 | La versión pública | `22b_Con_Su_Proveedor` | Kal le pasa el parte a Nadir (coda al cierre) | hecho, BORRADOR | ver git log |
| 22 | Lo que cueste | `24b_Lo_Que_Cueste` | Nadir (ya cubierto por el 21) | hecho, BORRADOR | ver git log |
| 23 | Luces fuera | `24c_El_Corral` | siembra de Eagle Eye y la mansión para el 24 | hecho, BORRADOR | ver git log |
| 24 | Vienes conmigo | `24d_Vienes_Conmigo` | Nadir (ya cubierto por el 21) | hecho, BORRADOR | ver git log |
| 25 | Libros abiertos | `25_Libros_Abiertos` |  | hecho, BORRADOR | ver git log |
| 26 | Me encuentro bien | `26_Me_Encuentro_Bien` |  | hecho, BORRADOR | ver git log |
| 27 | Una silla | `29_El_Patio_Ajeno` |  | hecho, BORRADOR | ver git log |
| 28 | Media baraja | `30_Media_Baraja` | fotos (costura 27→28) | hecho, BORRADOR | ver git log |
| 29 | Vamos a casa | `31_Vamos_A_Casa` | plática del camino de vuelta (DECISIÓN DEL AUTOR) | hecho, BORRADOR | ver git log |
| 30 | Línea directa | `32_Linea_Directa` |  | pendiente | |
| 31 | Lo único que es mío | `33_Mas_De_La_Cuenta` |  | pendiente | |
| 32 | A ti por mí | `34_Mi_Pareja` |  | pendiente | |
| 33 | Cambio de firmas | `35_Sin_Fecha_De_Regreso` | costura 32→33 (revisar al cerrar el 32) | hecho, BORRADOR (en paralelo con la Parte II) | ver git log |
| 34 | También las mañanas | `36_Tambien_Las_Mananas` | usted Chiara–Héctor (canon) | hecho, BORRADOR (en paralelo con la Parte II) | ver git log |
| 35 | Al revés | `38_Al_Reves` | Peugeot → Audi la noche de la incursión (no aplica: la línea está en el 39) | hecho, BORRADOR (en paralelo con la Parte II) | ver git log |
| 36 | Mecánico | `40_Mecanico` | Volpi fuera (D8) | hecho, BORRADOR (en paralelo con la Parte II) | ver git log |
| 37 | Reclamable | `41_La_Otra_Mitad` | despacho al día (con el 34) | hecho, BORRADOR (en paralelo con la Parte II) | ver git log |
| 38 | Nada | `42_Nada` | camioneta al depósito municipal (decisión del autor) | hecho, BORRADOR (en paralelo con la Parte II) | ver git log |
| 39 | Expediente sellado | `43_La_Puerta` | Peugeot → Audi la noche de la incursión | hecho, BORRADOR (en paralelo con la Parte II) | ver git log |
| 40 | No puedo sacarlo | `44_Jurisdiccion` | usted Chiara–Héctor; «Entramos cuatro… Salimos tres» | hecho, BORRADOR (en paralelo con la Parte II) | ver git log |
| 41 | Ropa limpia | `45_Ropa_Limpia` | luz; tú Chiara→Meiko | hecho, BORRADOR (en paralelo con la Parte II) | ver git log |
| 42 | Navajas y tinta | `46_Llaves` | luz; Nadir de tú (ficha); «Entramos cuatro… Salimos tres» | hecho, BORRADOR (en paralelo con la Parte II) | ver git log |
| 43 | Una cuenta abierta | `47_Intereses` | tics «Eso no es lo que le pregunté» y «nada fácil, Bellandi» | hecho, BORRADOR (en paralelo con la Parte II) | ver git log |
| 44 | Su nombre | `48_Su_Nombre` | usted Meiko→Chiara | pendiente | |
| 45 | Por si vuelve | `49_Enfrente` | luz | pendiente | |
| 46 | A oscuras | `50_A_Oscuras` |  | pendiente | |
| 47 | La tierra bajo sus botas | `50b_La_Tierra_Bajo_Sus_Botas` | luz (canon: «todavía de noche») | pendiente | |
