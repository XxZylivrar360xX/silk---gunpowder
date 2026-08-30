# Auditoría editorial global — PILOT_01_10_V1_1

- `editor_version`: `1.1`

> Esto es diagnóstico, no una lista de correcciones. HIGH significa lectura humana prioritaria, no obligación de modificar.

## Corpus

- Capítulos: 10.
- Palabras totales: 42534.
- Alertas HIGH / MEDIUM / LOW / INFO: 1 / 17 / 138 / 33.

| Capítulo | Palabras |
|---|---:|
| 01 · 01_Un_Hombre_De_Negocios_Intachable.md | 7995 |
| 02 · 02_Demasiado_Listo.md | 6972 |
| 03 · 03_Los_Viejos_Dias.md | 4864 |
| 04 · 04_La_Primera_Llamada.md | 2360 |
| 05 · 05_La_Casa_No_Quiere_Ruido.md | 2795 |
| 06 · 06_Una_Amiga.md | 1809 |
| 07 · 07_Ambos.md | 4435 |
| 08 · 08_La_Noche_Del_Ladrillo.md | 2780 |
| 09 · 09_La_Carrera_De_Mascaras.md | 2525 |
| 10 · 10_El_Corral.md | 5999 |

## Señales por confianza

- `high-confidence`: 0 alertas.
- `compound`: 2 alertas.
- `descriptive/inventory`: 187 alertas.

## Patrones globales

### Frases vigiladas

- `como si`: 91 (2.139/1,000 palabras; capítulos: 10; umbral global 12: alcanzado).
- `de alguna manera`: 1 (0.024/1,000 palabras; capítulos: 1; umbral global 3: no alcanzado).
- `no contestó`: 13 (0.306/1,000 palabras; capítulos: 6; umbral global 4: alcanzado).
- `no dijo nada`: 12 (0.282/1,000 palabras; capítulos: 5; umbral global 4: alcanzado).
- `no hacía falta`: 8 (0.188/1,000 palabras; capítulos: 5; umbral global 3: alcanzado).
- `un momento de más`: 2 (0.047/1,000 palabras; capítulos: 1; umbral global 3: no alcanzado).
- `un segundo de más`: 3 (0.071/1,000 palabras; capítulos: 2; umbral global 3: alcanzado).

### N-gramas destacables

- `levanto la vista` (3 palabras): 13
- `por primera vez` (3 palabras): 13
- `solto una risa` (3 palabras): 13
- `no dijo nada` (3 palabras): 12
- `de san aurelio` (3 palabras): 10
- `en voz alta` (3 palabras): 10
- `cerro los ojos` (3 palabras): 9
- `chiara se quedo` (3 palabras): 9
- `cole miro el` (3 palabras): 9
- `cole se quedo` (3 palabras): 9
- `se quedo mirando` (3 palabras): 9
- `chiara lo miro` (3 palabras): 8
- `cole dejo la` (3 palabras): 8
- `cole miro la` (3 palabras): 8
- `de almendra towing` (3 palabras): 8
- `primera vez en` (3 palabras): 8
- `cole levanto la` (3 palabras): 7
- `en voz baja` (3 palabras): 7
- `por primera vez en` (4 palabras): 6
- `bolsa de papel` (3 palabras): 6
- `cerro la carpeta` (3 palabras): 6
- `cole abrio la` (3 palabras): 6
- `el distrito marino` (3 palabras): 6
- `habia aprendido a` (3 palabras): 6
- `jefe de policia` (3 palabras): 6
- `la primera vez` (3 palabras): 6
- `levanto la mano` (3 palabras): 6
- `piso de juego` (3 palabras): 6
- `puerta de servicio` (3 palabras): 6
- `toda la noche` (3 palabras): 6

### Gestos y adverbios

- mirar: 190 (4.467/1,000).
- sonreír: 72 (1.693/1,000).
- asentir: 12 (0.282/1,000).
- levantar la vista: 13 (0.306/1,000).
- quedarse quieto/a: 6 (0.141/1,000).
- suspirar: 2 (0.047/1,000).
- tardar antes de responder: 2 (0.047/1,000).
- pasarse una mano por la cara: 2 (0.047/1,000).
- Adverbios terminados en `-mente`: 50 (1.176/1,000).

### Construcciones / tics

- `NEGATIVE_DASH_EXPLANATION`: 5
- `NEGATIVE_SENTENCE_CHAIN`: 7
- `NO_ERA_ERA`: 15
- `NO_FUE_FUE`: 3
- `NO_PORQUE_SINO`: 6

### Similaridad entre pasajes (experimental)

- **INFO** · 08_La_Noche_Del_Ladrillo.md:39 ↔ 09_La_Carrera_De_Mascaras.md:47 · score `0.1741` (Jaccard 0.1951; shingles 0.1111).
  - A: “Fue entonces cuando pasó por la calle lo que en el Departamento llamaban, medio en broma y medio no, el terror de la policía: un Peugeot 106 XSi reacondicionado, rojo, con un motor que sonaba mejor de lo que cualquier c…”
  - B: “Bajó con zapatos planos y un abrigo sobre un suéter oscuro, que era lo más cómodo que tenía a mano sin subir a cambiarse del todo. Cuando salió por la puerta de servicio del Monarch, el coche ya estaba contra la acera,…”
- **INFO** · 07_Ambos.md:353 ↔ 08_La_Noche_Del_Ladrillo.md:93 · score `0.1727` (Jaccard 0.1905; shingles 0.1194).
  - A: “Le puso el celular con la letra abierta en la mano, como quien entrega un arma que no sabe usar, y esperó a que empezara el verso. Cole fracasó en el primer intento, en el segundo se acercó, y para el tercero ya se reía…”
  - B: “Se acordó del penthouse, sin buscarlo. De un teléfono sostenido como quien entrega un arma que no sabe usar. Es un dueto. Ella dice cosas bonitas. Él no le cree ni una. De Cole fallando la letra la primera vez, encontrá…”
- **INFO** · 03_Los_Viejos_Dias.md:581 ↔ 05_La_Casa_No_Quiere_Ruido.md:61 · score `0.1315` (Jaccard 0.1569; shingles 0.0556).
  - A: “La pantalla del teléfono descansaba junto al plato de fruta intacto. Plaza Corona. Tres tiros. Jefe de policía ejecutado en una banca. La versión pública todavía buscaba palabras: atentado, crimen, investigación, comuni…”
  - B: “Ella caminó hacia la ventana. Abajo, la ciudad todavía estaba fingiendo normalidad alrededor de la muerte de Keene. Plaza Corona seguía en todos los noticieros. En el Monarch, en cambio, la gente hablaba de alfombras, l…”
- **INFO** · 02_Demasiado_Listo.md:805 ↔ 03_Los_Viejos_Dias.md:13 · score `0.1220` (Jaccard 0.1455; shingles 0.0517).
  - A: “Se quitó el saco y lo colgó en el respaldo de la silla. Después la camisa, despacio, porque el cuello le había marcado la piel. La dejó doblada sobre una caja de recibos, no por orden, sino porque la ropa buena todavía…”
  - B: “El catre no perdonaba el traje de la noche anterior. Le había dejado una marca en el hombro, otra en la cadera y una tercera en la paciencia. La camisa azul seguía doblada sobre la caja de recibos. El saco colgaba del r…”

## Ritmo comparado

| Cap. | Palabras | Mediana oración | % párrafos 1 oración | Diálogo % | Mediana intervención |
|---:|---:|---:|---:|---:|---:|
| 01 | 7995 | 7.0 | 66.9% | 24.6% | 4.0 |
| 02 | 6972 | 6.0 | 67.1% | 20.3% | 5.0 |
| 03 | 4864 | 5.0 | 74.1% | 21.6% | 4.0 |
| 04 | 2360 | 5.0 | 78.3% | 26.2% | 3.0 |
| 05 | 2795 | 5.0 | 79.0% | 22.8% | 3.0 |
| 06 | 1809 | 4.0 | 90.8% | 19.2% | 2.0 |
| 07 | 4435 | 6.0 | 66.5% | 21.4% | 4.0 |
| 08 | 2780 | 8.0 | 64.9% | 13.3% | 5.0 |
| 09 | 2525 | 8.0 | 45.5% | 10.1% | 3.0 |
| 10 | 5999 | 9.0 | 43.1% | 17.5% | 6.0 |

## Outliers

Se usa IQR (Q1 − 1.5×IQR, Q3 + 1.5×IQR). Un outlier no es un problema.

- 09_La_Carrera_De_Mascaras.md · `RHYTHM_SINGLE_SENTENCE_PARAGRAPH_OUTLIER`: Outlier bajo del corpus en % de párrafos de una oración; no implica un problema. Valor 45.545; rango 47.418–95.182.
- 10_El_Corral.md · `RHYTHM_SINGLE_SENTENCE_PARAGRAPH_OUTLIER`: Outlier bajo del corpus en % de párrafos de una oración; no implica un problema. Valor 43.062; rango 47.418–95.182.
- 09_La_Carrera_De_Mascaras.md · `DIALOGUE_PERCENT_OUTLIER`: Outlier bajo del corpus en % aproximado de diálogo; no implica un problema. Valor 10.139; rango 11.012–29.411.

## Top de alertas para calibración

- **HIGH** · 10_El_Corral.md · `LONG_DIALOGUE_CLUSTER` · `compound` · línea 250: Cluster de 2 intervenciones largas dentro de una ventana de 12 líneas. — “—Yo enterré a mi padre, a mi madre, y enterré cosas que no tienen tumba. Llevo más años de los que quisiera contar aprendiendo a no encariñarme, porque encariñarse, en esta vida,…”
- **MEDIUM** · 01_Un_Hombre_De_Negocios_Intachable.md · `DIALOGUE_EXCHANGE_WITHOUT_ACTION` · `compound` · línea 355: Intercambio prolongado de párrafos de diálogo sin párrafo narrativo intermedio. — “—Usted viene preparado. / —Vengo a no hacerle perder la mañana. / —Eso dicen los hombres que ya decidieron cuánto van a cobrar. / —Por eso se lo estoy diciendo antes de que me lo…”
- **MEDIUM** · 01_Un_Hombre_De_Negocios_Intachable.md · `LONG_DIALOGUE_INTERVENTION` · `descriptive/inventory` · línea 655: Intervención estimada en 62 palabras habladas; la longitud aislada nunca eleva a HIGH. — “—Y no me gusta que esté tranquilo así. Quiero que cambie. Quiero que El Patio vuelva a estar en el juego, que la gente que vive aquí tenga algo parecido a una vida decente. Y sobr…”
- **MEDIUM** · 02_Demasiado_Listo.md · `NEGATIVE_SENTENCE_CHAIN` · `descriptive/inventory` · línea 65: Tres o más oraciones consecutivas empiezan con «No»; posible cadena enfática o residuo de checklist. — “No podía saber que abajo había años. No podía saber que la ciudad que en ese momento le parecía provisional iba a aprender su apellido, su acento, su manera de entrar a una habita…”
- **MEDIUM** · 02_Demasiado_Listo.md · `NEGATIVE_SENTENCE_CHAIN` · `descriptive/inventory` · línea 725: Tres o más oraciones consecutivas empiezan con «No»; posible cadena enfática o residuo de checklist. — “No vendió más. No pidió otra oportunidad. No ofreció bajar el precio.”
- **MEDIUM** · 02_Demasiado_Listo.md · `NEGATIVE_SENTENCE_CHAIN` · `descriptive/inventory` · línea 821: Tres o más oraciones consecutivas empiezan con «No»; posible cadena enfática o residuo de checklist. — “No era inicio de nada. No se dijo eso. No habría sabido qué hacer con una idea tan inútil.”
- **MEDIUM** · 03_Los_Viejos_Dias.md · `LONG_DIALOGUE_INTERVENTION` · `descriptive/inventory` · línea 475: Intervención estimada en 71 palabras habladas; la longitud aislada nunca eleva a HIGH. — “—No limpiar la calle para que venga gente de fuera a comprar barato. No ponerle pintura a dos fachadas y llamarlo progreso. Levantarlo de verdad. Talleres, casas que no se caigan,…”
- **MEDIUM** · 03_Los_Viejos_Dias.md · `LONG_DIALOGUE_INTERVENTION` · `descriptive/inventory` · línea 629: Intervención estimada en 62 palabras habladas; la longitud aislada nunca eleva a HIGH. — “—Un jugador pierde cincuenta mil en una noche y parece idiota. Un jugador paga entrada, recompra fichas, llega a semifinal y pierde contra alguien de Los Ángeles: parece parte de…”
- **MEDIUM** · 04_La_Primera_Llamada.md · `SHORT_NARRATIVE_CLUSTER` · `descriptive/inventory` · línea 469: Secuencia narrative de 13 párrafos de 8 palabras o menos; revisar la cadencia, no uniformarla. — “—El problema llamó. / —Qué bonito, wallah. ¿Traía acento? / Cole levantó la vista. / Nadir sonrió.”
- **MEDIUM** · 06_Una_Amiga.md · `NEGATIVE_SENTENCE_CHAIN` · `descriptive/inventory` · línea 303: Tres o más oraciones consecutivas empiezan con «No»; posible cadena enfática o residuo de checklist. — “No hablaron de Alessio. No hablaron de Keene. No hablaron de Dario, salvo cuando Chiara dijo:”
- **MEDIUM** · 06_Una_Amiga.md · `NEGATIVE_SENTENCE_CHAIN` · `descriptive/inventory` · línea 473: Tres o más oraciones consecutivas empiezan con «No»; posible cadena enfática o residuo de checklist. — “No intentó subir. No preguntó si quería otra copa. No alargó la despedida como hacen los hombres cuando no saben dejar intacto un buen momento.”
- **MEDIUM** · 07_Ambos.md · `LONG_DIALOGUE_INTERVENTION` · `descriptive/inventory` · línea 237: Intervención estimada en 62 palabras habladas; la longitud aislada nunca eleva a HIGH. — “—Cuando tenía seis años me dieron una cámara de video para una fiesta. Una de esas viejas, que pesaban como un ladrillo. Me pasé la noche entera grabando desde un rincón, con un o…”
- **MEDIUM** · 09_La_Carrera_De_Mascaras.md · `NEGATIVE_SENTENCE_CHAIN` · `descriptive/inventory` · línea 177: Tres o más oraciones consecutivas empiezan con «No»; posible cadena enfática o residuo de checklist. — “No un hombre rubio. No una mujer italiana. No una cara. No los dos juntos.”
- **MEDIUM** · 10_El_Corral.md · `PHRASE_UN_SEGUNDO_DE_MAS` · `descriptive/inventory` · línea 66: Frase vigilada: 2 ocurrencia(s) en el capítulo; revisar en contexto. — “Cole se quedó con el teléfono pegado a la oreja un segundo de más, oyendo el silencio plano que sigue a una línea muerta, y después marcó el número de ella directamente.”
- **MEDIUM** · 10_El_Corral.md · `NEGATIVE_SENTENCE_CHAIN` · `descriptive/inventory` · línea 134: Tres o más oraciones consecutivas empiezan con «No»; posible cadena enfática o residuo de checklist. — “No dijo nada más. No hacía falta — el nombre solo, dicho así, ya era más de lo que Cole se permitía decir en voz alta casi nunca. No podía quedarse sentado.”
- **MEDIUM** · 10_El_Corral.md · `PHRASE_UN_MOMENTO_DE_MAS` · `descriptive/inventory` · línea 198: Frase vigilada: 2 ocurrencia(s) en el capítulo; revisar en contexto. — “Dario lo miró un momento de más, como quien archiva algo para después.”
- **MEDIUM** · 10_El_Corral.md · `LONG_DIALOGUE_INTERVENTION` · `descriptive/inventory` · línea 250: Intervención estimada en 92 palabras habladas; la longitud aislada nunca eleva a HIGH. — “—Yo enterré a mi padre, a mi madre, y enterré cosas que no tienen tumba. Llevo más años de los que quisiera contar aprendiendo a no encariñarme, porque encariñarse, en esta vida,…”
- **MEDIUM** · 10_El_Corral.md · `LONG_DIALOGUE_INTERVENTION` · `descriptive/inventory` · línea 254: Intervención estimada en 80 palabras habladas; la longitud aislada nunca eleva a HIGH. — “—Así que aquí estoy, a mis años, con miedo. Miedo de verdad, del que no se dice en el taller ni delante de los muchachos. Porque si algo le pasa a usted, pierdo dos personas de un…”
- **LOW** · 01_Un_Hombre_De_Negocios_Intachable.md · `PHRASE_COMO_SI` · `descriptive/inventory` · línea 17: Frase vigilada: 21 ocurrencia(s) en el capítulo; revisar en contexto. — “El sobre estaba abierto junto a la taza de café. El papel había pasado por demasiadas manos antes de llegar a la suya: funcionario, sello, reclusorio, correo. Aun así, la letra de…”
- **LOW** · 01_Un_Hombre_De_Negocios_Intachable.md · `REPEATED_NGRAM_4` · `descriptive/inventory` · línea 141: N-grama de 4 palabras repetido 4 veces en el capítulo. — “se limpio las manos”
- **LOW** · 01_Un_Hombre_De_Negocios_Intachable.md · `LONG_DIALOGUE_INTERVENTION` · `descriptive/inventory` · línea 143: Intervención estimada en 43 palabras habladas; la longitud aislada nunca eleva a HIGH. — “—Anoche entraron tres llamadas después de medianoche. Omar no puede partirse en dos y Danny se duerme parado si lo dejas sin azúcar. Necesitamos gente para turno nocturno antes de…”
- **LOW** · 01_Un_Hombre_De_Negocios_Intachable.md · `REPEATED_NGRAM_4` · `descriptive/inventory` · línea 205: N-grama de 4 palabras repetido 3 veces en el capítulo. — “solto una risa breve”
- **LOW** · 01_Un_Hombre_De_Negocios_Intachable.md · `NO_ERA_ERA` · `descriptive/inventory` · línea 221: Construcción «No era X. Era Y.»; revisar si la antítesis explica de más. — “No era olor a ley. Era olor a gente intentando que la ley alcanzara para todo.”
- **LOW** · 01_Un_Hombre_De_Negocios_Intachable.md · `GESTURE_CLUSTER_MIRAR` · `descriptive/inventory` · línea 273: El gesto «mirar» aparece agrupado en una ventana de 20 líneas. — “Keene lo miró por encima de la hoja. / La radio del pasillo soltó una clave y volvió a callarse. Keene no miró hacia la puerta. Cole sí, sin mover la cabeza. / Cole miró la taza d…”
- **LOW** · 01_Un_Hombre_De_Negocios_Intachable.md · `LONG_DIALOGUE_INTERVENTION` · `descriptive/inventory` · línea 293: Intervención estimada en 47 palabras habladas; la longitud aislada nunca eleva a HIGH. — “—Compra que mis grúas no sean sorpresa cuando estén cerca de una patrulla. Compra que si una unidad truena en Santa Brígida no espere dos horas por un remolque del condado. Compra…”
- **LOW** · 01_Un_Hombre_De_Negocios_Intachable.md · `SHORT_MIXED_CLUSTER` · `descriptive/inventory` · línea 295: Secuencia mixed de 6 párrafos de 8 palabras o menos; revisar la cadencia, no uniformarla. — “Keene cerró la carpeta. / —Eso suena a favor. / —Suena a servicio. / —En esta ciudad la diferencia importa.”
- **LOW** · 01_Un_Hombre_De_Negocios_Intachable.md · `NO_ERA_ERA` · `descriptive/inventory` · línea 309: Construcción «No era X. Era Y.»; revisar si la antítesis explica de más. — “no era legal. Era política.”
- **LOW** · 01_Un_Hombre_De_Negocios_Intachable.md · `LONG_DIALOGUE_INTERVENTION` · `descriptive/inventory` · línea 311: Intervención estimada en 46 palabras habladas; la longitud aislada nunca eleva a HIGH. — “—Diga que está probando un sistema de mantenimiento —respondió—. Seis unidades. Tres meses. Fechas, kilometraje, piezas y tiempos de respuesta. Si no funciona, lo cancela con núme…”
- **LOW** · 01_Un_Hombre_De_Negocios_Intachable.md · `LONG_DIALOGUE_INTERVENTION` · `descriptive/inventory` · línea 341: Intervención estimada en 54 palabras habladas; la longitud aislada nunca eleva a HIGH. — “—Tiene doce unidades con más de ciento veinte mil millas —dijo Cole—. Cuatro con llantas que no pasan lluvia fuerte. Dos Crown Victoria que siguen rodando porque nadie quiere firm…”
- **LOW** · 01_Un_Hombre_De_Negocios_Intachable.md · `PHRASE_NO_HACIA_FALTA` · `descriptive/inventory` · línea 343: Frase vigilada: 2 ocurrencia(s) en el capítulo; revisar en contexto. — “Keene abrió la carpeta otra vez, aunque no hacía falta.”

## Límite de V1.1

No hay análisis lingüístico profundo ni atribución automática de hablantes. Las oraciones, intervenciones y proporciones son aproximaciones mecánicas; no existe autofix.
