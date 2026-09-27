# Cap. 40 — corrección quirúrgica

Fecha: 2026-09-21. Agente: Codex. Rama: develop. Modo: SURGERY por encargo explícito del autor. Estado: BORRADOR, pendiente de revisión del autor.

## Resultado y autoridad

Se conserva título definitivo **Mecánico**, POV Kal y secuencia casa → viñedo → La Mesa → Ettore → Halbrook → partida comercial. Encargo del autor manda para correcciones de canon y orden; skill local editorial-surgery aplicada a la poda.

Fuentes: [[11_Books/Book_01_Seda_y_Polvora/Part_03_Ardizzone/00_Plan_Cierre_Parte_III]], fichas de Chiara, Alessio, Tommaso, Leone, Ettore y Halbrook; [[03_Factions/Il_Consorzio]], H17 en [[06_Relationships/Hitos]], Redaccion_De_Capitulos, voces de Kal/Chiara y políticas editoriales. Voces sin ficha propia: fichas de personaje y función institucional.

## Intervenciones: categoría, razón y función conservada

| Zona | Categoría / razón | Lo que ya hacía la escena; lo que conserva |
|---|---|---|
| Metadata y fotografía | Continuidad autorizada | Boda y nombre identifican al marido muerto; Alessio sustituye sólo la atribución errónea del retrato. Se elimina reconocimiento del yate, sin añadir datos de su muerte. |
| Apertura, cena, vestuario y hojas | Continuidad estacional | Palermo templado al sol, con humedad y frescor de sombra; chaqueta, suéter y botines sostienen el viñedo en otoño tardío. Conversación sobre calor que llegó tarde sigue retrospectiva. |
| Cata | POV / interioridad ajena | Pausa, traducción, risas y toque ya muestran recepción. Kal infiere comprensión del domingo y registra una mirada distinta sin saber qué oyó Chiara. Se retiran Walt/Héctor como pensamientos de ella. |
| Oficio | Orden autorizado | Pregunta/respuesta pasa al intercambio formal, antes de la versión de Chiara y del rumor de Livia. Miradas que vuelven a Chiara muestran reducción; sin otra profesión. |
| Entrada de Kal al rumor | GLOSA | La intervención muestra el reflejo; conserva espontaneidad sin explicar veinte años de conducta. Solución textual intacta. |
| Libreta | GLOSA / COMPETENCIA EXPLICADA | Silencio y escritura muestran efecto; se suprime explicación de reclasificación y charla intermedia para empalmar con Chiara. |
| Ettore | Reserva de revelación | Conserva peligro de ser visto, nombre registrado y palanca hacia Chiara. Sólo señala costo de la sala para ella, no por qué lo declaró ajeno. Se corta respuesta interna dependiente de esa revelación. |
| Halbrook | Continuidad / GLOSA | «Entonces vuelva» exige regreso sin atribuir vigilancia internacional. Buscar vuelos muestra respuesta práctica sin explicar alivio psicológico ni anticipar entrega del 39. |
| Desayuno | GLOSA | Pide boleto, no pregunta por avión ni pide compañía; no nombra a Halbrook ante Chiara. Se retira tesis y afirmación retrospectiva de que nunca lo nombró. |
| Despedida | POV / GLOSA | Ambos callan; no se atribuye preferencia interna a Chiara ni se interpreta como propósito que ella lo sacara de la sala. |
| Cierre | GLOSA | Despegue, Palermo y ojos cerrados ya muestran partida irresuelta. Se elimina «Se fue sin arreglarlo.». |

## Protecciones y verificación

Líneas canon de domingo, hacer reír, oficio, declaración de Chiara y advertencia sobre **la familia Ardizzone** conservadas. Ambigüedad de Kal (por él / contra él; protegido / apartado) protegida como interioridad necesaria. Llegada de Ettore, casa, habitación compartida, viñedo, solución del rumor y sala institucional sin reescritura sustancial.

Reconciliados plan (sólo foto y nota contradictoria), Hitos H17 e INDEX; relevo en CURRENT_BRIEF, PENDING, DECISIONS y log. No se tocaron fichas ni arco de Tommaso. Coincidencias ajenas a esa fotografía, como boda de los Ferretti en el 38, intactas; archivos históricos preservados.

No se añade canon nuevo: costuras de conducta y vestuario ejecutan el encargo sin fijar biografía, vigilancia ni revelaciones. No se escribe 41, no se ejecuta F1, no se regenera EPUB, no hay commit ni push.

## Autocrítica y VERIFY

- Mayor cautela: costura entre libreta y declaración; conserva silencio y evita explicar lo que cambió.
- Cambio más agresivo: traslado del bloque de oficio, requerido expresamente; estructura macro intacta.
- Protección frente a posible corte: incertidumbre final de Kal, necesaria para sostener la otra mitad del 41.
- Riesgo de esterilización bajo: sin limpieza general ni alteración de líneas y gestos de identidad.
- No se racionaliza interioridad: se retiran motivaciones ajenas y queda la duda de Kal.
- Clima y ropa reformulados sólo para continuidad; el viñedo conserva su voz y desarrollo.
- Sin pérdida de información autorizada, voz, callbacks o semillas: se retiran errores, glosas señaladas y revelación prematura. Costuras revisadas; no requiere restauración.
- Pendiente: revisión del autor. H17 sigue parcial hasta la mitad de Chiara; EPUB pendiente de autorización expresa.
- Comprobación final: diff revisado y `git diff --check` sin errores; rama develop. En prosa, oficio en líneas 162/164, rumor en 172, solución en 180, silencio en 182 y escritura en 184. Sin Tommaso, Walt/Héctor ni glosas retiradas en el capítulo. Brief, pendientes y decisiones por debajo de 800 palabras.

## Antes / después exactos

Cada intervención de prosa se registra una sola vez; razones y funciones en la tabla anterior.

```diff
--- 40_Mecanico.md antes
+++ 40_Mecanico.md despues
@@ -3,7 +3,7 @@
 Protagonista: Kal Mercer (POV único, tercera persona cercana). Analepsis completa: todo el capítulo ocurre en Palermo, antes de la primera línea del [[11_Books/Book_01_Seda_y_Polvora/Part_03_Ardizzone/39_Un_Par_De_Dias_Mas|Cap. 39]].
 Personajes con diálogo: Kal Mercer, Chiara Bellandi, Ettore, Leone Valenti, Livia Rinaldi.
 Presencia sin nombre desarrollado: personal de la casa, el encargado del viñedo.
-Mencionado sin aparecer en persona: Warren Halbrook (llamada telefónica, sin pisar Italia); Tommaso Lusardi (fotografía).
+Mencionado sin aparecer en persona: Warren Halbrook (llamada telefónica, sin pisar Italia); Alessio Lusardi (fotografía).
 Ventana temporal: varios días en Palermo — llegada y casa (día 1), viñedo (día 2), la Mesa (día 3), advertencia de Ettore y llamada de Halbrook (noche del día 3), partida (día 4). Cierra con Kal en tránsito de regreso, antes de Kingsley Field, que ya abrió el Cap. 39.
 Lugares: la casa donde Chiara creció, en las colinas sobre Palermo; uno de los viñedos que Chiara posee cerca de la ciudad (sin nombre); una sala donde se reúne La Mesa, en la ciudad baja; el aeropuerto de Palermo (cierre, breve).
 Función: la mitad de Kal sobre Palermo — lo que ve, oye, entiende e interpreta, sin resolver lo que Chiara calla. Instala H17 sin agotarlo: dispara el reflejo camaleónico de Kal ante La Mesa, la respuesta de Chiara que él lee como exclusión, la fotografía de la boda, la advertencia de Ettore y el detonante real del regreso (Halbrook). Cierra con los dos decidiendo solos, sin ruptura visible. La otra mitad de Palermo (por qué Chiara hace lo que hace) se reserva para el Cap. 41, POV Chiara.
@@ -15,7 +15,7 @@
 
 # Capítulo 40 — Mecánico
 
-El calor de Palermo no se parecía al de San Aurelio. No quemaba: se quedaba. Entraba por la ventanilla abierta del coche que los recogió en el aeropuerto y se instalaba en la ropa, en el pelo, en la nuca, y ya no se iba aunque subieran los vidrios y encendieran el aire. Kal llevaba un rato notando que Chiara, con la cabeza apoyada contra la ventanilla, había dejado de hablar en algún punto entre el último semáforo de la ciudad y la primera curva de la colina — no de cansancio: de otra cosa. La ciudad se quedó abajo, blanca y apretada contra el mar, y el camino empezó a subir entre paredes de piedra seca y olivos que llevaban ahí más tiempo del que cualquier cosa llevaba en pie en La Almendra.
+El aire de Palermo entraba húmedo por la ventanilla abierta del coche que los recogió en el aeropuerto. Al sol todavía era templado; en las curvas de sombra de la colina, Kal se cerraba la chaqueta. Llevaba un rato notando que Chiara, con la cabeza apoyada contra la ventanilla, había dejado de hablar en algún punto entre el último semáforo de la ciudad y la primera curva de la colina — no de cansancio: de otra cosa. La ciudad se quedó abajo, blanca y apretada contra el mar, y el camino empezó a subir entre paredes de piedra seca y olivos que llevaban ahí más tiempo del que cualquier cosa llevaba en pie en La Almendra.
 
 Chiara se incorporó antes de que él viera nada que anunciara que habían llegado.
 
@@ -69,13 +69,13 @@
 
 Kal no dijo nada. Pero registró, con la misma parte de él que registraba quién llegaba tarde a una entrega o quién dejaba de mirarlo a los ojos cuando mentía, que la pregunta de Ettore no había sido sobre habitaciones.
 
-Comieron esa noche en una mesa larga que sobraba de comensales, con Ettore a la cabecera sin que nadie se la hubiera cedido y sin que nadie lo discutiera, hablando de la cosecha, del calor que llegó tarde ese año, de un primo de alguien que Kal no conocía y a quien de todos modos siguió la conversación como seguía cualquier conversación de gente que no conocía: por el tono, por quién bajaba la voz, por quién dejaba una frase sin terminar a propósito. Ettore le habló dos o tres veces directamente — le preguntó por el vuelo, por el calor, si el pescado le gustaba — con una corrección impecable que no dejaba ver nada debajo. No hubo ninguna pregunta sobre quién era, qué hacía, de dónde venía. Todavía no.
+Comieron esa noche en una mesa larga que sobraba de comensales, con Ettore a la cabecera sin que nadie se la hubiera cedido y sin que nadie lo discutiera, hablando de la cosecha, del calor que llegó tarde ese año, de un primo de alguien que Kal no conocía y a quien de todos modos siguió la conversación como seguía cualquier conversación de gente que no conocía: por el tono, por quién bajaba la voz, por quién dejaba una frase sin terminar a propósito. Ettore le habló dos o tres veces directamente — le preguntó por el vuelo, por el tiempo, si el pescado le gustaba — con una corrección impecable que no dejaba ver nada debajo. No hubo ninguna pregunta sobre quién era, qué hacía, de dónde venía. Todavía no.
 
 Contenido. Correcto. Difícil de leer. Kal, que llevaba media vida leyendo habitaciones para sobrevivir en ellas, no pudo leer del todo a ese hombre, y eso en sí mismo ya le decía algo.
 
 ---
 
-Al día siguiente Chiara lo despertó temprano con una taza de café en la mano y ropa que no era la de San Aurelio: lino claro, sandalias, el pelo suelto en vez de recogido. No se vestía para una sala. Se vestía para algo que a Kal le tomó un momento identificar como territorio propio, la misma sensación que él tenía cuando se ponía las botas de siempre en vez del traje.
+Al día siguiente Chiara lo despertó temprano con una taza de café en la mano y ropa que no era la de San Aurelio: un suéter fino, pantalones claros, botines, el pelo suelto en vez de recogido y una chaqueta ligera sobre el brazo. No se vestía para una sala. Se vestía para algo que a Kal le tomó un momento identificar como territorio propio, la misma sensación que él tenía cuando se ponía las botas de siempre en vez del traje.
 
 —Hoy te toca a ti aprender algo —dijo, sentándose al borde de la cama—. Llevas meses enseñándome tu ciudad.
 
@@ -101,15 +101,15 @@
 
 Chiara no dijo nada durante un segundo. Después se rio de verdad, la risa completa que Kal conocía de las cuatro paredes del loft y que casi nunca sacaba a la calle, y le tocó el brazo con el dorso de la mano, un gesto rápido, casi sin pensar.
 
-Toda la mesa entendió, sin que nadie tuviera que explicarlo, que Kal venía de gente que no compraba botellas así. Nadie lo dijo. Nadie tenía que decirlo. Y a nadie en esa mesa pareció importarle demasiado, lo cual sorprendió a Kal más que la pregunta que no le hicieron.
-
-Chiara entendió algo más, y eso Kal no lo supo entonces ni lo sabría nunca del todo: entendió a Walt, con su vino barato y su generosidad exacta; entendió a Héctor sirviendo lo poco que tenía como si fuera lo mucho; entendió, sin nombrarlo ni para sí misma, una cocina pequeña en un barrio que no tenía nada que ver con esa colina y que sin embargo acababa de aparecer sentada en esa mesa, servida en una copa que costaba más que la botella entera que Walt hubiera podido comprar.
+Por las risas y las miradas que siguieron a la traducción, a Kal le pareció que habían entendido de qué clase de domingo hablaba. Nadie le preguntó más.
+
+Por la forma en que Chiara lo miró, Kal supo que ella había oído algo distinto al resto. No supo qué.
 
 —Siempre tienes algo gracioso para aligerar el ambiente —le dijo ella, más tarde, cuando ya caminaban solos entre las filas de vides, con el resto del grupo quedándose atrás alrededor de la mesa.
 
 —No —dijo Kal—. Es que me gusta hacerte reír.
 
-Chiara no contestó enseguida. Siguió caminando, con una mano rozando las hojas más altas a su paso, y algo en su cara cambió de una manera que Kal no supo si ella quería que él viera. Después señaló algo al fondo —un árbol solo en medio de la ladera, torcido por el viento de tantos años— y le contó una historia corta sobre por qué nadie lo había cortado nunca, y siguieron caminando.
+Chiara no contestó enseguida. Siguió caminando, con una mano rozando las últimas hojas a su paso, y algo en su cara cambió de una manera que Kal no supo si ella quería que él viera. Después señaló algo al fondo —un árbol solo en medio de la ladera, torcido por el viento de tantos años— y le contó una historia corta sobre por qué nadie lo había cortado nunca, y siguieron caminando.
 
 ---
 
@@ -157,6 +157,14 @@
 
 —Il Consorzio pregunta lo que le corresponde preguntar. —Valenti sonrió apenas, sin que la sonrisa le llegara a los ojos—. El señor Bellacorte se fue sin aviso formal. Eso, para nosotros, es un hueco. Un hueco es una pregunta, no una acusación.
 
+Valenti miró a Kal.
+
+—¿Y usted qué es, señor Mercer?
+
+—Mecánico.
+
+Valenti lo sostuvo con la mirada un segundo, como esperando el resto, y cuando no llegó ningún resto, asintió una vez, con algo que en otro hombre habría sido una sonrisa completa y en él fue apenas el principio de una. Livia volvió la cara hacia Chiara. Valenti también.
+
 Chiara respondió con la versión que Kal ya la había visto construir antes, tantas veces, en tantas salas distintas: una redistribución ordenada, una ausencia temporal cubierta, nada que no pudiera explicarse en una frase. No mintió en nada verificable — Kal, que llevaba meses aprendiendo a distinguir cuándo Chiara administraba la verdad y cuándo la inventaba, no oyó una sola cosa que no pudiera sostenerse si alguien fuera a comprobarla. Sólo eligió qué decir primero, qué dejar para el final, y qué no decir en absoluto.
 
 Livia escuchaba con la cabeza ligeramente inclinada, sin interrumpir, sin que su cara revelara si le creía o no. Fue ella quien, cuando Chiara terminó, dejó pasar un silencio de dos segundos y dijo, como quien piensa en voz alta y no espera respuesta de nadie en particular:
@@ -167,21 +175,13 @@
 
 Kal la recogió.
 
-No lo decidió. Ni siquiera se dio cuenta de que había abierto la boca hasta que ya estaba hablando, con la misma facilidad automática con la que llevaba veinte años resolviendo lo que alguien dejaba tirado frente a él.
+Ni siquiera se dio cuenta de que había abierto la boca hasta que ya estaba hablando.
 
 —No lo desmientan. Denle un nombre aburrido —dijo—. Que alguien que ya conocen empiece a firmar lo de siempre con la letra de la casa, sin anuncio, como si llevara meses haciéndolo. Para cuando alguien pregunte cuándo empezó, ya nadie se va a acordar de que hubo un día en que no era así.
 
 Silencio.
 
-Valenti no dijo nada durante un momento que se estiró más de lo cómodo. Después metió la mano en el bolsillo interior del saco, sacó una libreta pequeña, de cuero gastado, y escribió algo. No dijo qué. No leyó en voz alta lo que había escrito. Cerró la libreta, la guardó, y siguió con la conversación como si no hubiera pasado nada, preguntándole a Livia por su nieto, por una boda en el otoño.
-
-Pero algo había pasado, y Kal, contra la pared con las manos todavía sobre las rodillas, lo sintió tan claro como si alguien hubiera cerrado una puerta en la sala: ya no era el acompañante silencioso al que nadie se dirigía. Había hablado el idioma exacto de esa mesa, sin acento, sin pedir permiso, y esa mesa acababa de decidir que valía la pena escribirlo en alguna parte.
-
-—¿Y usted qué es, señor Mercer? —preguntó Valenti, apenas un momento después, con la misma cortesía exacta con la que había preguntado por el nieto de Livia, como si la pregunta no tuviera más peso que cualquier otra.
-
-—Mecánico —dijo Kal.
-
-Fue lo único que dijo, y lo dijo sin agregar nada, sin apellido de organización, sin explicar de qué taller ni de qué ciudad. Valenti lo sostuvo con la mirada un segundo, como esperando el resto, y cuando no llegó ningún resto, asintió una vez, con algo que en otro hombre habría sido una sonrisa completa y en él fue apenas el principio de una.
+Valenti metió la mano en el bolsillo interior del saco, sacó una libreta pequeña, de cuero gastado, y escribió algo. No lo leyó en voz alta. Cerró la libreta y la guardó.
 
 ---
 
@@ -201,9 +201,11 @@
 
 Fue Livia quien trajo la fotografía. No la sacó de un sobre, no la anunció: la tenía ya sobre la mesa, boca abajo, debajo de su propia taza, como si llevara ahí toda la reunión esperando el momento, y la giró con dos dedos hacia Chiara sin decir nada primero.
 
-Una fotografía en blanco y negro, o quizás sólo vieja de un modo que ya no distinguía colores. Chiara mucho más joven, con un vestido que Kal nunca le había visto, y a su lado un hombre con traje oscuro que reconoció antes de que nadie dijera el nombre — lo había visto hacía apenas unas semanas, en la cubierta de un yate, inclinando la cabeza para despedirse de ella con una sola palabra.
-
-—Tommaso Lusardi —dijo Livia, sin que hiciera falta preguntar—. Qué día tan hermoso fue aquél.
+Una fotografía en blanco y negro, o quizás sólo vieja de un modo que ya no distinguía colores. Chiara mucho más joven, con un vestido de novia, y a su lado un hombre con traje oscuro al que Kal no reconoció.
+
+—Alessio Lusardi —dijo Livia, sin que hiciera falta preguntar—. Qué día tan hermoso fue aquél.
+
+Su marido muerto. Kal volvió a mirar a Chiara en la fotografía.
 
 Chiara no tocó la fotografía. La miró desde donde estaba, sin acercar la mano, con la misma cara exacta que había tenido un momento antes hablando del cuarteto de Roma.
 
@@ -253,9 +255,9 @@
 
 —Ella puede cuidarse sola.
 
-—Puede. —Ettore asintió, sin discutirlo—. Y aun así hoy la vi decidir por usted delante de esa mesa, para que no lo pudieran usar. ¿Cree que eso le costó poco?
-
-Kal no tenía respuesta para eso. O la tenía, y no le gustaba lo que decía de él tenerla.
+—Puede. —Ettore asintió, sin discutirlo—. También vi lo que esa sala le costó a ella.
+
+Kal no contestó.
 
 Ettore se levantó, despacio, con las rodillas de alguien que llevaba demasiados años sentándose en esa misma silla.
 
@@ -279,13 +281,13 @@
 
 —Estoy en Italia.
 
-—Ya lo sé. —No sonó a amenaza. Sonó, otra vez, a alguien constatando un hecho—. Por eso llamo ahora y no después.
+—Entonces vuelva.
 
 Colgó sin despedirse, de la misma forma en que colgaba Dario, de la misma forma en que colgaba cualquier hombre que hablaba con Kal sólo cuando necesitaba algo de él.
 
 Kal se quedó con el teléfono en la mano, en la oscuridad de la habitación, con la respiración pareja de Chiara al otro lado de la cama — dormida, o fingiendo, no lo sabía con certeza, y no iba a preguntarlo.
 
-No tenía fecha todavía. Eso llegaría después, en San Aurelio, envuelto en el lenguaje de una entrega. Pero ya tenía algo peor que una fecha: tenía la certeza de que iba a tener que irse antes de arreglar lo que fuera que se había torcido esa mañana en aquella sala, y una parte de él —la que llevaba veinte años prefiriendo un problema resoluble a uno que no lo era— sintió, debajo de la culpa, algo parecido a un alivio que no se permitió nombrar.
+No tenía fecha todavía. Bajó el brillo del teléfono y buscó los vuelos de regreso.
 
 ---
 
@@ -303,7 +305,9 @@
 
 No fue un reproche. Fue información.
 
-Kal no le preguntó por qué lo necesitaba. No le dijo *ven conmigo*. No esperó a que ella se ofreciera a acompañarlo ni le explicó del todo por qué él sí tenía que irse ya — el nombre de Halbrook no salió de su boca, como no había salido nunca en meses, y en ese momento, mirándola sobre la mesa de la cocina de la casa donde ella había crecido, Kal hizo exactamente lo que llevaba haciendo toda su vida cuando algo se ponía demasiado difícil de resolver de frente: tomó el problema que sí sabía arreglar y dejó el otro donde estaba.
+Kal no le preguntó por qué lo necesitaba. No le dijo *ven conmigo*.
+
+—Sácame un boleto.
 
 —Me quedo unos días más —dijo Chiara, después de un silencio que a Kal le pareció más largo de lo que probablemente fue—. Hay cosas aquí que todavía no terminé.
 
@@ -329,7 +333,7 @@
 
 Ella se rio, corta, contra su camisa, y por un segundo —sólo un segundo— Kal sintió que la sala de esa mañana, la fotografía, la frase de Valenti, la frase de ella misma delante de la Mesa, todo eso se apartaba lo suficiente para dejarlos ser, otra vez, solamente dos personas despidiéndose en un patio.
 
-No se dijeron nada sobre lo que había pasado. No hablaron de La Mesa, ni de la fotografía, ni de la frase que ella había usado para sacarlo de esa sala. Había demasiado, y no había tiempo, y los dos —cada uno a su manera— preferían un problema con fecha a uno sin ella.
+No se dijeron nada sobre lo que había pasado. No hablaron de La Mesa, ni de la fotografía, ni de la frase que ella había dicho delante de todos.
 
 En el coche, camino a la ciudad, Ettore no dijo nada más de lo que ya había dicho la noche anterior. Manejaba mirando el camino, con las manos firmes sobre el volante, y sólo cuando llegaron a la terminal, mientras Kal bajaba la maleta, agregó una última cosa.
 
@@ -346,5 +350,3 @@
 No tenía manera de saber si lo había protegido o si lo había apartado. Las dos cosas seguían pesando lo mismo, una al lado de la otra, sin que ninguna ganara.
 
 Cuando el avión despegó, Palermo se quedó abajo, blanca contra el mar oscuro, y Kal no la vio desaparecer del todo porque cerró los ojos antes de que la ventanilla dejara de mostrar nada reconocible.
-
-Se fue sin arreglarlo.

```
