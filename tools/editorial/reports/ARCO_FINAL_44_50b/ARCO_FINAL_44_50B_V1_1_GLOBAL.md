# Auditoría editorial global — ARCO_FINAL_44_50B_V1_1

- `editor_version`: `1.1`

> Esto es diagnóstico, no una lista de correcciones. HIGH significa lectura humana prioritaria, no obligación de modificar.

## Corpus

- Capítulos: 8.
- Palabras totales: 24847.
- Alertas HIGH / MEDIUM / LOW / INFO: 1 / 15 / 50 / 29.

| Capítulo | Palabras |
|---|---:|
| 44 · 44_Jurisdiccion.md | 2045 |
| 45 · 45_Ropa_Limpia.md | 4218 |
| 46 · 46_Llaves.md | 3206 |
| 47 · 47_Intereses.md | 3966 |
| 48 · 48_Su_Nombre.md | 3442 |
| 49 · 49_Enfrente.md | 2594 |
| 50 · 50_A_Oscuras.md | 3963 |
| 08 · 50b_La_Tierra_Bajo_Sus_Botas.md | 1413 |

## Señales por confianza

- `high-confidence`: 0 alertas.
- `compound`: 6 alertas.
- `descriptive/inventory`: 89 alertas.

## Patrones globales

### Frases vigiladas

- `como si`: 22 (0.885/1,000 palabras; capítulos: 8; umbral global 12: alcanzado).
- `no contestó`: 10 (0.402/1,000 palabras; capítulos: 5; umbral global 4: alcanzado).
- `no dijo nada`: 12 (0.483/1,000 palabras; capítulos: 7; umbral global 4: alcanzado).
- `un segundo de más`: 2 (0.080/1,000 palabras; capítulos: 2; umbral global 3: no alcanzado).

### N-gramas destacables

- `no dijo nada` (3 palabras): 12
- `de pie junto` (3 palabras): 10
- `las manos en los bolsillos` (5 palabras): 9
- `libro de cuentas` (3 palabras): 8
- `de pie junto a` (4 palabras): 7
- `el senor mercer` (3 palabras): 7
- `la torre norte` (3 palabras): 7
- `por primera vez` (3 palabras): 7
- `con las manos en los bolsillos` (6 palabras): 6
- `de pie junto a la` (5 palabras): 6
- `extremo de la barra` (4 palabras): 6
- `junto a la puerta` (4 palabras): 6
- `manos en el volante` (4 palabras): 6
- `abrio la puerta` (3 palabras): 6
- `asiento del copiloto` (3 palabras): 6
- `chiara miro la` (3 palabras): 6
- `chiara no contesto` (3 palabras): 6
- `el letrero verde` (3 palabras): 6
- `volvio a cerrar` (3 palabras): 6
- `bolsillo interior del saco` (4 palabras): 5
- `el libro de cuentas` (4 palabras): 5
- `la esquina de mabel` (4 palabras): 5
- `chiara se detuvo` (3 palabras): 5
- `chiara se quedo` (3 palabras): 5
- `detras del mostrador` (3 palabras): 5
- `habia vuelto a` (3 palabras): 5
- `hoja de turnos` (3 palabras): 5
- `junto al lancia` (3 palabras): 5
- `levanto la vista` (3 palabras): 5
- `piso de juego` (3 palabras): 5

### Gestos y adverbios

- mirar: 101 (4.065/1,000).
- asentir: 12 (0.483/1,000).
- tardar antes de responder: 2 (0.080/1,000).
- encogerse de hombros: 4 (0.161/1,000).
- levantar la vista: 5 (0.201/1,000).
- sonreír: 9 (0.362/1,000).
- pasarse una mano por la cara: 2 (0.080/1,000).
- quedarse quieto/a: 1 (0.040/1,000).
- Adverbios terminados en `-mente`: 2 (0.080/1,000).

### Construcciones / tics

- `NEGATIVE_SENTENCE_CHAIN`: 2
- `NO_ERA_ERA`: 2
- `NO_FUE_FUE`: 1
- `POSSIBLE_EDITORIAL_INSTRUCTION_LEAK`: 1

### Similaridad entre pasajes (experimental)

- **MEDIUM** · 45_Ropa_Limpia.md:99 ↔ 48_Su_Nombre.md:325 · score `0.5054` (Jaccard 0.5556; shingles 0.3548).
  - A: “Mabel estaba detrás del mostrador, cortando jamón. Vio a Chiara entrar y no le dijo buenos días. Le sirvió café en una taza gruesa, sin preguntarle cómo lo quería, y la puso en el extremo de la barra, lejos de los del o…”
  - B: “Los dos del overol desayunaban en la barra. El taxista tomaba café de pie junto a la puerta. Mabel estaba detrás del mostrador cortando jamón, y vio entrar a Chiara, y le sirvió el café en la taza gruesa, y la puso en e…”
- **INFO** · 45_Ropa_Limpia.md:137 ↔ 48_Su_Nombre.md:337 · score `0.2632` (Jaccard 0.2903; shingles 0.1818).
  - A: “Lo dijo sin enojo, igual que decía el precio del pan. Uno de los del overol pidió más café y Mabel fue a servírselo, le cobró, le dio el cambio, le preguntó por la hija. Cuando volvió, traía una bolsa de papel de estraz…”
  - B: “Uno de los del overol pidió más café. Mabel fue, le sirvió, le cobró, le preguntó por la hija. Volvió. Chiara se terminó el café, dejó un billete debajo de la taza y se levantó.”
- **INFO** · 50_A_Oscuras.md:284 ↔ 50b_La_Tierra_Bajo_Sus_Botas.md:30 · score `0.2072` (Jaccard 0.2500; shingles 0.0789).
  - A: “Avenida Almendra estaba negra de punta a punta. La Esquina de Mabel, con la cortina abajo. La tlapalería. El poste del circo. En la esquina del semáforo muerto, Chiara puso la direccional y dio vuelta a la izquierda.”
  - B: “En la Avenida Almendra los postes alumbraban banquetas vacías. La cortina de La Esquina de Mabel seguía abajo. En el poste del circo, el cartel de hacía dos temporadas se había despegado de una esquina y se movía un poc…”
- **INFO** · 50_A_Oscuras.md:284 ↔ 50b_La_Tierra_Bajo_Sus_Botas.md:72 · score `0.2038` (Jaccard 0.2414; shingles 0.0909).
  - A: “Avenida Almendra estaba negra de punta a punta. La Esquina de Mabel, con la cortina abajo. La tlapalería. El poste del circo. En la esquina del semáforo muerto, Chiara puso la direccional y dio vuelta a la izquierda.”
  - B: “La primera era la Avenida Almendra, de día. La cortina de La Esquina de Mabel arriba, gente en la banqueta, una señora con bolsas del mercado, el poste del circo con el cartel todavía pegado.”
- **INFO** · 45_Ropa_Limpia.md:97 ↔ 48_Su_Nombre.md:325 · score `0.1767` (Jaccard 0.1957; shingles 0.1200).
  - A: “Olía a café recalentado, a pan, al cloro barato con que alguien acababa de trapear el piso. En la vitrina había conchas de la víspera. Dos hombres con overol de taller desayunaban en la barra con los codos sobre la fórm…”
  - B: “Los dos del overol desayunaban en la barra. El taxista tomaba café de pie junto a la puerta. Mabel estaba detrás del mostrador cortando jamón, y vio entrar a Chiara, y le sirvió el café en la taza gruesa, y la puso en e…”
- **INFO** · 45_Ropa_Limpia.md:211 ↔ 50b_La_Tierra_Bajo_Sus_Botas.md:86 · score `0.1696` (Jaccard 0.2000; shingles 0.0784).
  - A: “La cámara estaba al fondo del pasillo, alta, mirando hacia la puerta del penthouse desde atrás de la salida de emergencia. La imagen era en blanco y negro y un poco ancha en las orillas, como si el pasillo se curvara. E…”
  - B: “La siguiente no era una fotografía como las otras. Era un fotograma impreso, en blanco y negro, un poco ancho en las orillas, como si el pasillo se curvara. Un pasillo de hotel. Una puerta al fondo. Frente a la puerta,…”
- **INFO** · 46_Llaves.md:316 ↔ 47_Intereses.md:59 · score `0.1657` (Jaccard 0.2121; shingles 0.0263).
  - A: “Chiara miró la pantalla. Marisol, sin apellido, con una foto pequeña en el círculo: pelo cobrizo con las puntas rubias, la lengua de fuera, una gorra que no era suya. Miró a Héctor. Héctor no bajó el brazo.”
  - B: “Chiara sí sabía. Lo había visto en el círculo de la pantalla, la tarde anterior, sobre el pelo cobrizo: una gorra que no era de Marisol. No dijo nada. Sacó un cigarro, lo miró, y lo volvió a guardar sin encenderlo, porq…”
- **INFO** · 45_Ropa_Limpia.md:317 ↔ 48_Su_Nombre.md:123 · score `0.1468` (Jaccard 0.1757; shingles 0.0602).
  - A: “Kingsley Field apareció a la derecha como aparecen los aeropuertos de carga de noche: una extensión de luces bajas y anaranjadas, sin gente, con la silueta de un avión de fuselaje ancho detenido junto a un hangar y un c…”
  - B: “Dejaron atrás Kingsley Field por la izquierda, de día más feo que de noche: hangares de lámina sin pintar, una cerca larga con alambre en la punta, un avión de carga con las compuertas abiertas como una boca. Pasaron la…”
- **INFO** · 47_Intereses.md:71 ↔ 49_Enfrente.md:84 · score `0.1462` (Jaccard 0.1795; shingles 0.0465).
  - A: “El hombre del Audi era más joven de lo que esperaba, de traje gris sin corbata, con el pelo cortado tan corto que se le veía la forma del cráneo. Tenía las dos manos en el volante. No le dio la mano ni se quitó los lent…”
  - B: “Valenti estaba de pie junto a la ventana, con una taza en la mano, mirando hacia afuera. Llevaba un traje gris oscuro sin corbata y el pelo, más gris que en Palermo, cortado igual. Se volvió cuando ella tocó con los nud…”
- **INFO** · 46_Llaves.md:242 ↔ 47_Intereses.md:67 · score `0.1419` (Jaccard 0.1892; shingles 0.0000).
  - A: “Danny asintió y volvió al sedán. Garrett se quedó un momento más en la puerta, con los brazos cruzados, y después entró a la oficina y cerró. A través del vidrio, Chiara lo vio sentarse, abrir una carpeta de pasta gris…”
  - B: “Danny sacó la cabeza del cofre de la pick-up. Héctor no se movió del capó. En la oficina, Garrett se levantó del escritorio y se quedó de pie junto al vidrio, sin abrir la puerta, al lado de Nadir dormido.”
- **INFO** · 46_Llaves.md:34 ↔ 47_Intereses.md:89 · score `0.1413` (Jaccard 0.1818; shingles 0.0196).
  - A: “Detrás del mostrador del taller, Nadir tenía abierto un libro de cuentas de pasta dura, de los que Kal se burlaba porque existían computadoras, y una pluma en la mano. La pluma no se movía. Detrás del vidrio de la ofici…”
  - B: “Nadir se despertó con el ruido de la puerta de la oficina. Garrett la había abierto. Nadir se enderezó en el sillón, se pasó la mano por la cara, vio el libro de cuentas en el regazo y lo cerró como si alguien lo hubier…”
- **INFO** · 44_Jurisdiccion.md:194 ↔ 46_Llaves.md:62 · score `0.1375` (Jaccard 0.1600; shingles 0.0702).
  - A: “—No estaba desde antes de que yo llegara. Lo tuvieron unas horas. A las cinco y diez de la mañana llegó la reclamación de jurisdicción y se lo llevaron. Lo que el sargento me tuvo esperando toda la mañana era el papel d…”
  - B: “—No está en la comisaría. No estaba desde la primera mañana. A las cinco y diez la base reclamó jurisdicción y se lo llevaron. —Lo dijo en orden, como lo había dicho Krane—. Lo tiene Camp Alder. La municipal ya no tiene…”
- **INFO** · 44_Jurisdiccion.md:236 ↔ 45_Ropa_Limpia.md:237 · score `0.1349` (Jaccard 0.1591; shingles 0.0625).
  - A: “—En Camp Alder. —Lucía sostuvo la mirada antes de seguir—. Lo detuvo una patrulla municipal en un camino rural a menos de un kilómetro del perímetro. Antes de que nadie lo procesara del todo, la base reclamó jurisdicció…”
  - B: “Kal Mercer en la puerta de su casa a las siete de la tarde. Kal Mercer, horas después, en un camino rural a menos de un kilómetro de una base federal. Dos registros, el mismo día, el mismo hombre. Una grabación que exis…”
- **INFO** · 49_Enfrente.md:224 ↔ 50_A_Oscuras.md:156 · score `0.1348` (Jaccard 0.1515; shingles 0.0845).
  - A: “Atravesó el lobby. El ruido de las máquinas le llegó desde la sala de juego como le llegaba siempre, una lluvia de monedas que no eran monedas, campanitas, la voz grabada de una mujer felicitando a alguien. Una de las g…”
  - B: “Eso fue lo primero. No la oscuridad, que con las luces de emergencia era una penumbra amarilla en la que se adivinaban las mesas y las columnas, sino el silencio de las máquinas: cuatrocientas pantallas negras, sin camp…”
- **INFO** · 45_Ropa_Limpia.md:215 ↔ 50b_La_Tierra_Bajo_Sus_Botas.md:86 · score `0.1291` (Jaccard 0.1522; shingles 0.0600).
  - A: “Chiara lo reconoció antes de que la imagen le diera nada con qué reconocerlo: por cómo se movía, por cómo no miraba hacia ningún lado porque ya sabía dónde estaba todo. Llevaba la chaqueta oscura. Caminó por el pasillo…”
  - B: “La siguiente no era una fotografía como las otras. Era un fotograma impreso, en blanco y negro, un poco ancho en las orillas, como si el pasillo se curvara. Un pasillo de hotel. Una puerta al fondo. Frente a la puerta,…”
- **INFO** · 49_Enfrente.md:84 ↔ 50b_La_Tierra_Bajo_Sus_Botas.md:46 · score `0.1241` (Jaccard 0.1591; shingles 0.0192).
  - A: “Valenti estaba de pie junto a la ventana, con una taza en la mano, mirando hacia afuera. Llevaba un traje gris oscuro sin corbata y el pelo, más gris que en Palermo, cortado igual. Se volvió cuando ella tocó con los nud…”
  - B: “Había un sedán oscuro estacionado junto a la reja. Sin nada que lo distinguiera de ningún otro sedán oscuro. Junto a él esperaba un hombre delgado, de traje gris, con la corbata bien puesta a las cinco de la mañana. Cua…”
- **INFO** · 48_Su_Nombre.md:63 ↔ 50_A_Oscuras.md:32 · score `0.1233` (Jaccard 0.1552; shingles 0.0278).
  - A: “Mabel se le quedó viendo un momento más. Luego tomó una charola de la pila y se fue a recoger la mesa que había dejado la familia, y no volvió al extremo de la barra en todo el tiempo que Chiara tardó en terminarse el c…”
  - B: “Chiara estaba ahí desde las siete. Había llegado con el último turno de la cena, cuando la vitrina ya tenía más charolas vacías que pan, y se había sentado en el extremo de la barra con el saco puesto. Mabel le había se…”

## Ritmo comparado

| Cap. | Palabras | Mediana oración | % párrafos 1 oración | Diálogo % | Mediana intervención |
|---:|---:|---:|---:|---:|---:|
| 44 | 2045 | 6.0 | 47.0% | 27.7% | 5.0 |
| 45 | 4218 | 7.0 | 45.3% | 21.7% | 5.0 |
| 46 | 3206 | 6.0 | 42.8% | 22.1% | 4.0 |
| 47 | 3966 | 6.0 | 43.5% | 23.4% | 4.0 |
| 48 | 3442 | 6.0 | 40.6% | 23.0% | 5.0 |
| 49 | 2594 | 7.0 | 47.7% | 21.7% | 5.0 |
| 50 | 3963 | 8.0 | 38.5% | 11.8% | 7.0 |
| 08 | 1413 | 10.0 | 40.8% | 0.1% | 1.0 |

## Outliers

Se usa IQR (Q1 − 1.5×IQR, Q3 + 1.5×IQR). Un outlier no es un problema.

- 50b_La_Tierra_Bajo_Sus_Botas.md · `RHYTHM_SENTENCE_MEDIAN_OUTLIER`: Outlier alto del corpus en mediana de palabras por oración; no implica un problema. Valor 10.0; rango 4.125–9.125.
- 50_A_Oscuras.md · `DIALOGUE_PERCENT_OUTLIER`: Outlier bajo del corpus en % aproximado de diálogo; no implica un problema. Valor 11.759; rango 13.32–28.97.
- 50b_La_Tierra_Bajo_Sus_Botas.md · `DIALOGUE_PERCENT_OUTLIER`: Outlier bajo del corpus en % aproximado de diálogo; no implica un problema. Valor 0.071; rango 13.32–28.97.
- 50_A_Oscuras.md · `DIALOGUE_INTERVENTION_MEDIAN_OUTLIER`: Outlier alto del corpus en mediana de intervención; no implica un problema. Valor 7.0; rango 2.5–6.5.
- 50b_La_Tierra_Bajo_Sus_Botas.md · `DIALOGUE_INTERVENTION_MEDIAN_OUTLIER`: Outlier bajo del corpus en mediana de intervención; no implica un problema. Valor 1.0; rango 2.5–6.5.

## Top de alertas para calibración

- **HIGH** · 48_Su_Nombre.md · `LONG_DIALOGUE_CLUSTER` · `compound` · línea 259: Cluster de 2 intervenciones largas dentro de una ventana de 12 líneas. — “—Hace unos meses —dijo— alguien en Calle Corona decidió que yo manejaba un Peugeot rojo. Un coche que yo no he visto en mi vida. Y durante semanas tuve policías tomando café en mi…”
- **MEDIUM** · 44_Jurisdiccion.md · `DIALOGUE_EXCHANGE_WITHOUT_ACTION` · `compound` · línea 40: Intercambio prolongado de párrafos de diálogo sin párrafo narrativo intermedio. — “—¿Quién lo tiene? / —La municipal. Se quedó atrás para que pudiéramos irnos. Un agente se le echó encima por un lado que él no estaba mirando. Lo vimos desde arriba. / —¿Está heri…”
- **MEDIUM** · 44_Jurisdiccion.md · `NEGATIVE_SENTENCE_CHAIN` · `descriptive/inventory` · línea 248: Tres o más oraciones consecutivas empiezan con «No»; posible cadena enfática o residuo de checklist. — “—No puedo entrar a esa base —siguió Lucía—. No puedo exigir custodia. No puedo llamar a nadie que tenga autoridad sobre lo que pasa ahí adentro, porque esa autoridad no es mía y n…”
- **MEDIUM** · 45_Ropa_Limpia.md · `LONG_DIALOGUE_INTERVENTION` · `descriptive/inventory` · línea 191: Intervención estimada en 62 palabras habladas; la longitud aislada nunca eleva a HIGH. — “—La otra tarde, antes de que yo entrara. Mi compañero del turno de día me lo comentó, porque se le hizo raro. El señor Mercer subió, como siempre, sin anunciarse, porque a él ya n…”
- **MEDIUM** · 45_Ropa_Limpia.md · `LONG_DIALOGUE_INTERVENTION` · `descriptive/inventory` · línea 279: Intervención estimada en 93 palabras habladas; la longitud aislada nunca eleva a HIGH. — “—El turno de noche sale a las cinco y media, pero los camiones de la base salen antes —dijo Mei-Lin, sin voltear—. Como a las cinco, llenos. Regresan a las siete con lo sucio. La…”
- **MEDIUM** · 47_Intereses.md · `DIALOGUE_EXCHANGE_WITHOUT_ACTION` · `compound` · línea 99: Intercambio prolongado de párrafos de diálogo sin párrafo narrativo intermedio. — “—¿Y? / —Esta noche —dijo Chiara—. A las nueve, en el puerto. Varek quiere las cajas y quiere hablar. / —Quiere hablar. —Nadir se acomodó la camisa dentro del pantalón, de un lado,…”
- **MEDIUM** · 47_Intereses.md · `LONG_DIALOGUE_CLUSTER` · `compound` · línea 215: Cluster de 3 intervenciones largas dentro de una ventana de 12 líneas. — “—Hace cinco días esas cajas eran mercancía —dijo—. Hoy la base las está contando. Cada noche que pasaron en tu barrio, alguien en Camp Alder estuvo haciendo una lista, y esa lista…”
- **MEDIUM** · 47_Intereses.md · `LONG_DIALOGUE_INTERVENTION` · `descriptive/inventory` · línea 227: Intervención estimada en 73 palabras habladas; la longitud aislada nunca eleva a HIGH. — “—No es dinero. Dinero tengo. —Lo dijo sin mirarla, mirándose las manos—. El taller de Mercer tiene grúas. Tiene un patio con portón y un hombre que sabe de papeles. Tiene muchacho…”
- **MEDIUM** · 47_Intereses.md · `NEGATIVE_SENTENCE_CHAIN` · `descriptive/inventory` · línea 393: Tres o más oraciones consecutivas empiezan con «No»; posible cadena enfática o residuo de checklist. — “No tengo hora. No tengo destino. No tengo quién lo firma.”
- **MEDIUM** · 48_Su_Nombre.md · `DIALOGUE_EXCHANGE_WITHOUT_ACTION` · `compound` · línea 219: Intercambio prolongado de párrafos de diálogo sin párrafo narrativo intermedio. — “—¿Y tú de quién eres? / —De nadie. / —Eso dicen todos los que son de alguien. —Rafe se rió, una risa corta, de garganta, y se volvió otra vez hacia Chiara—. El puente de la cement…”
- **MEDIUM** · 48_Su_Nombre.md · `LONG_DIALOGUE_INTERVENTION` · `descriptive/inventory` · línea 259: Intervención estimada en 86 palabras habladas; la longitud aislada nunca eleva a HIGH. — “—Hace unos meses —dijo— alguien en Calle Corona decidió que yo manejaba un Peugeot rojo. Un coche que yo no he visto en mi vida. Y durante semanas tuve policías tomando café en mi…”
- **MEDIUM** · 48_Su_Nombre.md · `LONG_DIALOGUE_INTERVENTION` · `descriptive/inventory` · línea 263: Intervención estimada en 63 palabras habladas; la longitud aislada nunca eleva a HIGH. — “—Si esto sale bien —dijo Rafe—, nadie va a preguntar nada, y su nombre se queda aquí, en esa libreta, y ahí se muere. Si sale mal, y vienen a tocarme la puerta los que vienen a to…”
- **MEDIUM** · 48_Su_Nombre.md · `CROSS_CHAPTER_PASSAGE_SIMILARITY` · `descriptive/inventory` · línea 325: Posible similitud con 45_Ropa_Limpia.md:99 (score 0.5054); señal experimental. — “Los dos del overol desayunaban en la barra. El taxista tomaba café de pie junto a la puerta. Mabel estaba detrás del mostrador cortando jamón, y vio entrar a Chiara, y le sirvió el café en la taza gruesa, y la puso en e…”
- **MEDIUM** · 49_Enfrente.md · `LONG_DIALOGUE_CLUSTER` · `compound` · línea 144: Cluster de 2 intervenciones largas dentro de una ventana de 12 líneas. — “—El señor Mercer está en Camp Alder —dijo Valenti—. Lo que lo tiene ahí no es la ciudad, ni la policía de la ciudad, ni un juez que se pueda invitar a cenar. Usted ya lo sabe, por…”
- **MEDIUM** · 49_Enfrente.md · `LONG_DIALOGUE_INTERVENTION` · `descriptive/inventory` · línea 144: Intervención estimada en 65 palabras habladas; la longitud aislada nunca eleva a HIGH. — “—El señor Mercer está en Camp Alder —dijo Valenti—. Lo que lo tiene ahí no es la ciudad, ni la policía de la ciudad, ni un juez que se pueda invitar a cenar. Usted ya lo sabe, por…”
- **MEDIUM** · 50_A_Oscuras.md · `LONG_DIALOGUE_INTERVENTION` · `descriptive/inventory` · línea 198: Intervención estimada en 76 palabras habladas; la longitud aislada nunca eleva a HIGH. — “—Pagué todo. Le di mi nombre a un hombre que cobraba en la banqueta desde niño. Le quedé a deber a Dario lo que él quiera, cuando él quiera, y no sé qué es. Me senté a tomar café…”
- **LOW** · 44_Jurisdiccion.md · `PHRASE_COMO_SI` · `descriptive/inventory` · línea 90: Frase vigilada: 4 ocurrencia(s) en el capítulo; revisar en contexto. — “Krane contestó al primer timbre, como si ya tuviera el teléfono en la mano.”
- **LOW** · 44_Jurisdiccion.md · `LONG_DIALOGUE_INTERVENTION` · `descriptive/inventory` · línea 194: Intervención estimada en 49 palabras habladas; la longitud aislada nunca eleva a HIGH. — “—No estaba desde antes de que yo llegara. Lo tuvieron unas horas. A las cinco y diez de la mañana llegó la reclamación de jurisdicción y se lo llevaron. Lo que el sargento me tuvo…”
- **LOW** · 45_Ropa_Limpia.md · `PHRASE_NO_DIJO_NADA` · `descriptive/inventory` · línea 157: Frase vigilada: 3 ocurrencia(s) en el capítulo; revisar en contexto. — “Chiara dejó un billete debajo de la taza. Mabel lo vio y no dijo nada. Chiara salió con la bolsa de estraza en la mano. No se la comió, pero tampoco la tiró.”
- **LOW** · 45_Ropa_Limpia.md · `LONG_DIALOGUE_INTERVENTION` · `descriptive/inventory` · línea 163: Intervención estimada en 47 palabras habladas; la longitud aislada nunca eleva a HIGH. — “—Dice que mañana. Que hoy ya tiene apartadas las del bloque y que las va a mirar ella. Que la esperes a la salida del turno, del lado de la barda que da al Cutoff, no en la entrad…”
- **LOW** · 45_Ropa_Limpia.md · `GESTURE_CLUSTER_MIRAR` · `descriptive/inventory` · línea 201: El gesto «mirar» aparece agrupado en una ventana de 20 líneas. — “Chiara no se movió del mostrador. La luz amarilla seguía donde estaba; el mármol seguía pareciendo recién lavado. El muchacho la miraba esperando que ella dijera algo que le permi…”
- **LOW** · 45_Ropa_Limpia.md · `LONG_DIALOGUE_INTERVENTION` · `descriptive/inventory` · línea 357: Intervención estimada en 50 palabras habladas; la longitud aislada nunca eleva a HIGH. — “—Las del calabozo llegan aparte. Una bolsa por cabeza, con una etiqueta de plástico amarrada, con el apellido y un número. Son pocas. Ocho, diez, a veces menos. Las lavamos aparte…”
- **LOW** · 46_Llaves.md · `NO_ERA_ERA` · `descriptive/inventory` · línea 40: Construcción «No era X. Era Y.»; revisar si la antítesis explica de más. — “No era un saludo. Era el apellido.”
- **LOW** · 46_Llaves.md · `PHRASE_NO_CONTESTO` · `descriptive/inventory` · línea 48: Frase vigilada: 2 ocurrencia(s) en el capítulo; revisar en contexto. — “Chiara no contestó. Se detuvo a mitad del Patio, entre la grúa y el capó, donde la podían ver todos, y esperó.”
- **LOW** · 46_Llaves.md · `LONG_DIALOGUE_INTERVENTION` · `descriptive/inventory` · línea 62: Intervención estimada en 60 palabras habladas; la longitud aislada nunca eleva a HIGH. — “—No está en la comisaría. No estaba desde la primera mañana. A las cinco y diez la base reclamó jurisdicción y se lo llevaron. —Lo dijo en orden, como lo había dicho Krane—. Lo ti…”
- **LOW** · 46_Llaves.md · `REPEATED_NGRAM_5` · `descriptive/inventory` · línea 64: N-grama de 5 palabras repetido 3 veces en el capítulo. — “la puerta de la oficina”
- **LOW** · 46_Llaves.md · `GESTURE_CLUSTER_MIRAR` · `descriptive/inventory` · línea 138: El gesto «mirar» aparece agrupado en una ventana de 20 líneas. — “Nadir había vuelto al libro de cuentas. Lo abrió en cualquier página, miró los números sin leerlos y lo volvió a cerrar. Después rodeó el mostrador, cruzó el Patio sin mirar a nad…”
- **LOW** · 47_Intereses.md · `REPEATED_NGRAM_4` · `descriptive/inventory` · línea 37: N-grama de 4 palabras repetido 4 veces en el capítulo. — “el libro de cuentas”
- **LOW** · 47_Intereses.md · `PHRASE_NO_DIJO_NADA` · `descriptive/inventory` · línea 59: Frase vigilada: 4 ocurrencia(s) en el capítulo; revisar en contexto. — “Chiara sí sabía. Lo había visto en el círculo de la pantalla, la tarde anterior, sobre el pelo cobrizo: una gorra que no era de Marisol. No dijo nada. Sacó un cigarro, lo miró, y…”
- **LOW** · 47_Intereses.md · `REPEATED_NGRAM_4` · `descriptive/inventory` · línea 71: N-grama de 4 palabras repetido 4 veces en el capítulo. — “el hombre del audi”

## Límite de V1.1

No hay análisis lingüístico profundo ni atribución automática de hablantes. Las oraciones, intervenciones y proporciones son aproximaciones mecánicas; no existe autofix.
