# Auditoría editorial global — PILOT_01_10

> Esto es diagnóstico, no una lista de correcciones. HIGH significa lectura humana prioritaria, no obligación de modificar.

## Corpus

- Capítulos: 10.
- Palabras totales: 42534.
- Alertas HIGH / MEDIUM / LOW / INFO: 15 / 40 / 112 / 9.

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
- `NEGATIVE_SENTENCE_CHAIN`: 8
- `NO_ERA_ERA`: 15
- `NO_FUE_FUE`: 3
- `NO_PORQUE_SINO`: 6

## Ritmo comparado

| Cap. | Palabras | Mediana oración | % párrafos 1 oración | Diálogo % | Mediana intervención |
|---:|---:|---:|---:|---:|---:|
| 01 | 7995 | 7.0 | 66.9% | 26.2% | 4.5 |
| 02 | 6972 | 6.0 | 67.1% | 20.9% | 5.0 |
| 03 | 4864 | 5.0 | 74.1% | 22.5% | 4.0 |
| 04 | 2360 | 5.0 | 78.3% | 26.9% | 3.0 |
| 05 | 2795 | 5.0 | 79.0% | 23.9% | 4.0 |
| 06 | 1809 | 4.0 | 90.8% | 21.6% | 3.0 |
| 07 | 4435 | 6.0 | 66.5% | 25.7% | 4.0 |
| 08 | 2780 | 8.0 | 64.9% | 25.1% | 6.5 |
| 09 | 2525 | 8.0 | 45.5% | 17.9% | 6.0 |
| 10 | 5999 | 9.0 | 43.1% | 24.8% | 11.5 |

## Outliers

Se usa IQR (Q1 − 1.5×IQR, Q3 + 1.5×IQR). Un outlier no es un problema.

- 09_La_Carrera_De_Mascaras.md · `RHYTHM_SINGLE_SENTENCE_PARAGRAPH_OUTLIER`: Outlier bajo del corpus en % de párrafos de una oración; no implica un problema. Valor 45.545; rango 47.418–95.182.
- 10_El_Corral.md · `RHYTHM_SINGLE_SENTENCE_PARAGRAPH_OUTLIER`: Outlier bajo del corpus en % de párrafos de una oración; no implica un problema. Valor 43.062; rango 47.418–95.182.
- 10_El_Corral.md · `DIALOGUE_INTERVENTION_MEDIAN_OUTLIER`: Outlier alto del corpus en mediana de intervención; no implica un problema. Valor 11.5; rango 1.375–8.375.

## Top de alertas para calibración

- **HIGH** · 01_Un_Hombre_De_Negocios_Intachable.md · `LONG_DIALOGUE_INTERVENTION` · línea 655: Intervención de diálogo de 62 palabras; posible outlier para lectura humana. — “—Y no me gusta que esté tranquilo así. Quiero que cambie. Quiero que El Patio vuelva a estar en el juego, que la gente que vive aquí tenga algo parecido a una vida decente. Y sobr…”
- **HIGH** · 02_Demasiado_Listo.md · `SHORT_PARAGRAPH_CLUSTER` · línea 163: Secuencia de 11 párrafos de 8 palabras o menos; revisar la cadencia, no uniformarla. — “—¿Quién manda la ciudad? / Matteo tardó medio segundo más de lo necesario. / —Depende de qué parte. / —No pregunté quién firma.”
- **HIGH** · 03_Los_Viejos_Dias.md · `LONG_DIALOGUE_INTERVENTION` · línea 475: Intervención de diálogo de 71 palabras; posible outlier para lectura humana. — “—No limpiar la calle para que venga gente de fuera a comprar barato. No ponerle pintura a dos fachadas y llamarlo progreso. Levantarlo de verdad. Talleres, casas que no se caigan,…”
- **HIGH** · 03_Los_Viejos_Dias.md · `SHORT_PARAGRAPH_CLUSTER` · línea 511: Secuencia de 16 párrafos de 8 palabras o menos; revisar la cadencia, no uniformarla. — “Walt levantó la suya. / —Renovados. / Cole chocó la botella con ellos. / —Y con sangre nueva.”
- **HIGH** · 03_Los_Viejos_Dias.md · `LONG_DIALOGUE_INTERVENTION` · línea 629: Intervención de diálogo de 62 palabras; posible outlier para lectura humana. — “—Un jugador pierde cincuenta mil en una noche y parece idiota. Un jugador paga entrada, recompra fichas, llega a semifinal y pierde contra alguien de Los Ángeles: parece parte de…”
- **HIGH** · 04_La_Primera_Llamada.md · `SHORT_PARAGRAPH_CLUSTER` · línea 469: Secuencia de 13 párrafos de 8 palabras o menos; revisar la cadencia, no uniformarla. — “—El problema llamó. / —Qué bonito, wallah. ¿Traía acento? / Cole levantó la vista. / Nadir sonrió.”
- **HIGH** · 05_La_Casa_No_Quiere_Ruido.md · `SHORT_PARAGRAPH_CLUSTER` · línea 199: Secuencia de 12 párrafos de 8 palabras o menos; revisar la cadencia, no uniformarla. — “Chiara cerró los ojos. / —Por favor, no me dé otro problema. / —Ya lo tenía. Yo solo lo señalé. / Quiso reírse. No lo hizo.”
- **HIGH** · 06_Una_Amiga.md · `SHORT_PARAGRAPH_CLUSTER` · línea 43: Secuencia de 14 párrafos de 8 palabras o menos; revisar la cadencia, no uniformarla. — “Héctor miró la pata en su bota. / —No me metas en tus cosas raras. / Nadir se rió. / Cole tomó aire.”
- **HIGH** · 07_Ambos.md · `LONG_DIALOGUE_INTERVENTION` · línea 237: Intervención de diálogo de 62 palabras; posible outlier para lectura humana. — “—Cuando tenía seis años me dieron una cámara de video para una fiesta. Una de esas viejas, que pesaban como un ladrillo. Me pasé la noche entera grabando desde un rincón, con un o…”
- **HIGH** · 09_La_Carrera_De_Mascaras.md · `LONG_DIALOGUE_INTERVENTION` · línea 35: Intervención de diálogo de 64 palabras; posible outlier para lectura humana. — “—Dos veces en la questura, de adolescente, en Palermo. —Lo dijo despacio, midiendo cuánto contar—. Una por una Vespa que no era mía. Otra por estar en una plaza que los carabinier…”
- **HIGH** · 09_La_Carrera_De_Mascaras.md · `SHORT_PARAGRAPH_CLUSTER` · línea 187: Secuencia de 10 párrafos de 8 palabras o menos; revisar la cadencia, no uniformarla. — “—Esto fue una pésima idea —dijo Chiara. / —Sí. / El motor siguió tictaqueando. / —¿Ganamos?”
- **HIGH** · 10_El_Corral.md · `LONG_DIALOGUE_INTERVENTION` · línea 250: Intervención de diálogo de 92 palabras; posible outlier para lectura humana. — “—Yo enterré a mi padre, a mi madre, y enterré cosas que no tienen tumba. Llevo más años de los que quisiera contar aprendiendo a no encariñarme, porque encariñarse, en esta vida,…”
- **HIGH** · 10_El_Corral.md · `LONG_DIALOGUE_INTERVENTION` · línea 254: Intervención de diálogo de 80 palabras; posible outlier para lectura humana. — “—Así que aquí estoy, a mis años, con miedo. Miedo de verdad, del que no se dice en el taller ni delante de los muchachos. Porque si algo le pasa a usted, pierdo dos personas de un…”
- **HIGH** · 10_El_Corral.md · `LONG_DIALOGUE_INTERVENTION` · línea 346: Intervención de diálogo de 62 palabras; posible outlier para lectura humana. — “—Alguien te dejó inconsciente en propiedad del Monarch y nadie vio nada. —No levantó la voz; nunca le hacía falta—. Vuelves ahí y sigues siendo la mujer más fácil de encontrar de…”
- **HIGH** · 10_El_Corral.md · `LONG_DIALOGUE_INTERVENTION` · línea 394: Intervención de diálogo de 69 palabras; posible outlier para lectura humana. — “—Hay gente de antes —dijo al fin—. De la vida de mi padre. De la de los socios. Gente que lleva años decidiendo quién administra qué, y a quién se le permite hacer dinero en paz.…”
- **MEDIUM** · 01_Un_Hombre_De_Negocios_Intachable.md · `LONG_DIALOGUE_INTERVENTION` · línea 75: Intervención de diálogo de 41 palabras; posible outlier para lectura humana. — “—El Ford de Santa Brígida volvió a tronar, khoya —dijo Nadir desde la puerta de la oficina, con un vaso de café en una mano y una carpeta en la otra—. El dueño dice que ahora sí n…”
- **MEDIUM** · 01_Un_Hombre_De_Negocios_Intachable.md · `LONG_DIALOGUE_INTERVENTION` · línea 143: Intervención de diálogo de 43 palabras; posible outlier para lectura humana. — “—Anoche entraron tres llamadas después de medianoche. Omar no puede partirse en dos y Danny se duerme parado si lo dejas sin azúcar. Necesitamos gente para turno nocturno antes de…”
- **MEDIUM** · 01_Un_Hombre_De_Negocios_Intachable.md · `SHORT_PARAGRAPH_CLUSTER` · línea 227: Secuencia de 7 párrafos de 8 palabras o menos; revisar la cadencia, no uniformarla. — “—Mercer. / —Buen día. / —El chief lo espera. / —Qué raro.”
- **MEDIUM** · 01_Un_Hombre_De_Negocios_Intachable.md · `LONG_DIALOGUE_INTERVENTION` · línea 293: Intervención de diálogo de 47 palabras; posible outlier para lectura humana. — “—Compra que mis grúas no sean sorpresa cuando estén cerca de una patrulla. Compra que si una unidad truena en Santa Brígida no espere dos horas por un remolque del condado. Compra…”
- **MEDIUM** · 01_Un_Hombre_De_Negocios_Intachable.md · `LONG_DIALOGUE_INTERVENTION` · línea 311: Intervención de diálogo de 47 palabras; posible outlier para lectura humana. — “—Diga que está probando un sistema de mantenimiento —respondió—. Seis unidades. Tres meses. Fechas, kilometraje, piezas y tiempos de respuesta. Si no funciona, lo cancela con núme…”
- **MEDIUM** · 01_Un_Hombre_De_Negocios_Intachable.md · `LONG_DIALOGUE_INTERVENTION` · línea 341: Intervención de diálogo de 56 palabras; posible outlier para lectura humana. — “—Tiene doce unidades con más de ciento veinte mil millas —dijo Cole—. Cuatro con llantas que no pasan lluvia fuerte. Dos Crown Victoria que siguen rodando porque nadie quiere firm…”
- **MEDIUM** · 01_Un_Hombre_De_Negocios_Intachable.md · `DIALOGUE_EXCHANGE_WITHOUT_ACTION` · línea 355: Intercambio prolongado de párrafos de diálogo sin párrafo narrativo intermedio. — “—Usted viene preparado. / —Vengo a no hacerle perder la mañana. / —Eso dicen los hombres que ya decidieron cuánto van a cobrar. / —Por eso se lo estoy diciendo antes de que me lo…”
- **MEDIUM** · 01_Un_Hombre_De_Negocios_Intachable.md · `LONG_DIALOGUE_INTERVENTION` · línea 743: Intervención de diálogo de 50 palabras; posible outlier para lectura humana. — “—La cicatriz. Le pedí a quien me habló de usted algo más útil que rubio, ojos azules. Resopló y me dijo que eso, en este país, es como pedirme que encuentre la diferencia entre do…”
- **MEDIUM** · 01_Un_Hombre_De_Negocios_Intachable.md · `LONG_DIALOGUE_INTERVENTION` · línea 787: Intervención de diálogo de 43 palabras; posible outlier para lectura humana. — “—Por ahora, reputación. Después, quizás coches. Flotillas, mantenimiento, servicio de emergencia, proveedores que no nos dejen tirados un sábado a las dos de la mañana. El casino…”
- **MEDIUM** · 01_Un_Hombre_De_Negocios_Intachable.md · `NEGATIVE_SENTENCE_CHAIN` · línea 797: Tres o más oraciones consecutivas empiezan con «No»; posible cadena enfática o residuo de checklist. — “—No le gusta el juego. —No dije eso. —No hizo falta.”
- **MEDIUM** · 02_Demasiado_Listo.md · `NEGATIVE_SENTENCE_CHAIN` · línea 65: Tres o más oraciones consecutivas empiezan con «No»; posible cadena enfática o residuo de checklist. — “No podía saber que abajo había años. No podía saber que la ciudad que en ese momento le parecía provisional iba a aprender su apellido, su acento, su manera de entrar a una habita…”
- **MEDIUM** · 02_Demasiado_Listo.md · `LONG_DIALOGUE_INTERVENTION` · línea 337: Intervención de diálogo de 53 palabras; posible outlier para lectura humana. — “—Todos en la habitación lo estaban escuchando sin parecer que lo escuchaban. La dueña lo corrigió delante de mí y él la dejó. Un muchacho con casco nuevo se quedó a mirar si él ac…”
- **MEDIUM** · 02_Demasiado_Listo.md · `LONG_DIALOGUE_INTERVENTION` · línea 609: Intervención de diálogo de 54 palabras; posible outlier para lectura humana. — “—Flotilla ejecutiva. Mantenimiento preventivo, no sólo reparaciones cuando ya quedaron mal con un huésped. Servicio de emergencia para valet y proveedores. Un corralón privado par…”
- **MEDIUM** · 02_Demasiado_Listo.md · `LONG_DIALOGUE_INTERVENTION` · línea 625: Intervención de diálogo de 42 palabras; posible outlier para lectura humana. — “—La que está detrás del arreglo floral grande, junto al pasillo del lobby. La cámara la toma de frente, pero no cubre el ángulo de la mano. Si alguien trae gafete falso y sabe cam…”
- **MEDIUM** · 02_Demasiado_Listo.md · `LONG_DIALOGUE_INTERVENTION` · línea 659: Intervención de diálogo de 50 palabras; posible outlier para lectura humana. — “—Para la apertura van a necesitar un premio de sorteo que se vea bien en la nota de prensa. Yo lo pongo. Lo financio, ustedes lo entregan, y nadie tiene que explicar por qué el pr…”

## Límite de V1

No hay análisis lingüístico profundo ni atribución automática de hablantes. Las oraciones, intervenciones y proporciones son aproximaciones mecánicas; no existe autofix.
