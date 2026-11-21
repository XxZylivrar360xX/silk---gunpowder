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

| Cap. | Título | Archivo | Transversal | Estado | Commit |
|---|---|---|---|---|---|
| 1 | Un hombre de negocios intachable | `01_Un_Hombre_De_Negocios_Intachable` | Peugeot (línea de lógica) | pendiente | |
| 2 | Demasiado listo | `02_Demasiado_Listo` |  | pendiente | |
| 3 | Lo que no cambió | `03_Los_Viejos_Dias` |  | pendiente | |
| 4 | Tarifa nocturna | `04_Tarifa_Nocturna` |  | pendiente | |
| 5 | Cliente y proveedor | `05a_Cliente_Y_Proveedor` |  | pendiente | |
| 6 | Sólo una cena | `05c_La_Pizza_De_Calabaza` |  | pendiente | |
| 7 | Ambos | `06_Ambos` | tuteo prematuro; Peugeot D5 | pendiente | |
| 8 | La noche del ladrillo | `07_La_Noche_Del_Ladrillo` | Peugeot D5 («lo confirmó») | pendiente | |
| 9 | Mandorla | `08_La_Carrera_De_Mascaras` | Peugeot D5 | pendiente | |
| 10 | Una pésima idea | `08b_La_Sargenta` |  | pendiente | |
| 11 | La balanza | `09_La_Balanza` |  | pendiente | |
| 12 | La invitada | `10_El_Loft_Del_Soltero` |  | pendiente | |
| 13 | Roma Atrii | `12_Roma_Atrii` | redundancia POV | pendiente | |
| 14 | Con miedo y todo | `14_La_Regla_Del_Telefono` | redundancia POV | pendiente | |
| 15 | Yo lo llevo | `15_El_Porton` | redundancia POV | pendiente | |
| 16 | Canal Seco | `17_Cuentas_Claras` | redundancia POV; salto a junio | pendiente | |
| 17 | Día nublado | `18_El_Dia_Nublado` | salto a junio | pendiente | |
| 18 | En lo pequeño | `20_El_Mirador` |  | pendiente | |
| 19 | Grazie | `21b_Grazie` |  | pendiente | |
| 20 | Algo más que dinero | `22a_La_Cifra` | gesto Varek | pendiente | |
| 21 | La versión pública | `22b_Con_Su_Proveedor` | Kal le pasa el parte a Nadir | pendiente | |
| 22 | Lo que cueste | `24b_Lo_Que_Cueste` | Nadir (ya cubierto por el 21) | pendiente | |
| 23 | Luces fuera | `24c_El_Corral` |  | pendiente | |
| 24 | Vienes conmigo | `24d_Vienes_Conmigo` | Nadir (ya cubierto por el 21) | pendiente | |
| 25 | Libros abiertos | `25_Libros_Abiertos` |  | pendiente | |
| 26 | Me encuentro bien | `26_Me_Encuentro_Bien` |  | pendiente | |
| 27 | Una silla | `29_El_Patio_Ajeno` |  | pendiente | |
| 28 | Media baraja | `30_Media_Baraja` |  | pendiente | |
| 29 | Vamos a casa | `31_Vamos_A_Casa` |  | pendiente | |
| 30 | Línea directa | `32_Linea_Directa` |  | pendiente | |
| 31 | Lo único que es mío | `33_Mas_De_La_Cuenta` |  | pendiente | |
| 32 | A ti por mí | `34_Mi_Pareja` |  | pendiente | |
| 33 | Cambio de firmas | `35_Sin_Fecha_De_Regreso` |  | pendiente | |
| 34 | También las mañanas | `36_Tambien_Las_Mananas` | usted Chiara–Héctor (canon) | pendiente | |
| 35 | Al revés | `38_Al_Reves` | Peugeot → Audi la noche de la incursión | pendiente | |
| 36 | Mecánico | `40_Mecanico` | Volpi fuera (D8) | pendiente | |
| 37 | Reclamable | `41_La_Otra_Mitad` |  | pendiente | |
| 38 | Nada | `42_Nada` |  | pendiente | |
| 39 | Expediente sellado | `43_La_Puerta` |  | pendiente | |
| 40 | No puedo sacarlo | `44_Jurisdiccion` | usted Chiara–Héctor | pendiente | |
| 41 | Ropa limpia | `45_Ropa_Limpia` | luz; tú Chiara→Meiko | pendiente | |
| 42 | Navajas y tinta | `46_Llaves` | luz; Nadir de tú (ficha) | pendiente | |
| 43 | Una cuenta abierta | `47_Intereses` |  | pendiente | |
| 44 | Su nombre | `48_Su_Nombre` | usted Meiko→Chiara | pendiente | |
| 45 | Por si vuelve | `49_Enfrente` | luz | pendiente | |
| 46 | A oscuras | `50_A_Oscuras` |  | pendiente | |
| 47 | La tierra bajo sus botas | `50b_La_Tierra_Bajo_Sus_Botas` | luz (canon: «todavía de noche») | pendiente | |
