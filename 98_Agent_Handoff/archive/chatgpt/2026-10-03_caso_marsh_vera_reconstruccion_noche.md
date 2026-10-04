# Caso Marsh–Vera — reconstrucción de la noche

Identificador: PROYECTO RECLUTA

## Objetivo

Preservar la reconstrucción actualmente explorada para la noche que origina el caso Vera y conecta a los dos antagonistas de la trilogía de Elenna. Esta nota es material de handoff para Claude Code: no implica integración al repo ni sustituye el canon vigente en `develop`.

## Contexto mínimo

En la nueva arquitectura de los Libros V–VII, el caso Vera deja de ser únicamente el origen de Ethan/Dylan y se convierte en la noche fundacional de dos conflictos distintos:

- **Ethan Cole / Dylan Marsh**: antagonista personal de Elenna y futuro asesino serial.
- **Antagonista velado de Nicholas**: responsable original de la muerte de los padres Marsh y de la mentira histórica alrededor del caso.

El diseño explorado identifica a **Blake Stanton** como candidato principal para ese antagonista velado. Esto colisiona con material vigente en `develop`, donde Blake todavía está definido como un personaje transitorio/limitado del Libro I; Claude deberá tratar cualquier cambio futuro como reemplazo deliberado, no como simple añadido.

## CANON DEL AUTOR

### Función macro del caso Vera

- El caso Vera es el núcleo histórico de ambos antagonistas.
- **Dylan Marsh es el niño que toma el arma y dispara a Vera.**
- La muerte de Vera ocurre después del asesinato de los padres Marsh.
- El asesino serial moderno no tiene un “predecesor serial” en aquella noche: el asesinato de los padres crea el trauma que, décadas después, desemboca en Dylan/Ethan como asesino serial.
- La verdad completa de aquella noche queda reservada para **Libro VII — Camino a Casa**, después de que Dylan Marsh ya haya sido detenido y enjuiciado.
- Dylan es el único testigo capaz de aportar la versión humana/ocular de lo ocurrido dentro de la casa.

### Dylan durante la noche

- Dylan es un niño pequeño.
- Presencia fragmentos del asesinato de sus padres.
- **No ve claramente el rostro del agresor.**
- Lo que queda grabado en su memoria es principalmente:
  - una placa policial;
  - un arma;
  - la presencia/autoridad de un adulto armado.
- Cuando Vera llega armada y con placa, Dylan reacciona desde el trauma inmediato.
- Vera intenta desescalar y su gesto de levantar las manos / presentarse como amiga sigue siendo central.
- Dylan dispara a Vera con la misma arma utilizada antes contra sus padres.

### El arma y la escena

- El agresor lleva un **arma no policial y no registrada**.
- Tras matar a los padres Marsh, la deja en la escena por nervios, shock y falta de experiencia criminal.
- Dylan toma esa arma.
- Dylan dispara a Vera con ella.
- **Nereo Volpi recoge el arma** cuando llega a limpiar la escena y extrae al niño.
- Para cuando Nicholas llega, la casa presenta:
  - tres muertos;
  - ningún arma;
  - ningún niño;
  - una ventana abierta al fondo del pasillo.
- La escena induce de forma natural la lectura de un único agresor adulto que asesinó a los Marsh y a Vera y huyó.
- La verdad física es distinta: la misma arma fue utilizada por dos tiradores.

### Volpi

- Volpi llega después de Vera, pero antes de la llegada de Nicholas y del procesamiento normal de la escena.
- Es enviado por **Dario Varek** cuando alguien le avisa de que los Marsh fueron ejecutados.
- Su misión es limpiar/contener el desastre, no descubrir la verdad moral.
- Volpi:
  - encuentra al niño;
  - lo extrae;
  - recoge el arma;
  - deja una escena suficientemente ambigua para que la interpretación equivocada se sostenga;
  - entrega al niño a un tercero, iniciando el camino que terminará vinculándolo con los Varek.
- El método de Volpi consiste en retirar las piezas que permiten demostrar la secuencia real, no en fabricar una escena falsa perfecta.

### Consecuencia para Blake / el agresor

- El agresor no sabe que Dylan presenció fragmentos de la noche.
- Después, al enterarse de que:
  - Vera murió;
  - el arma no apareció en la escena;
  - había un niño asociado a la casa;
  entiende que **alguien más intervino**.
- Su paranoia histórica nace de tres preguntas:
  - ¿quién recogió el arma?
  - ¿qué sabe esa persona?
  - ¿dónde está el niño?
- Esta incertidumbre debe influir en la evolución del antagonista durante las dos décadas siguientes.

## DISEÑO / PENDIENTE — Blake Stanton como agresor original

El candidato actual para el hombre que mata a los padres Marsh es **Blake Stanton**.

Diseño explorado:

- Blake conoce u oculta evidencia relacionada con un soborno cometido por otro policía conocido.
- Ese encubrimiento contribuye a que el padre de Dylan sea golpeado/perjudicado.
- Alguien informa al padre Marsh de que Blake ocultó la evidencia.
- El padre confronta a Blake en la comisaría.
- Blake descarta la acusación públicamente como difamación o escándalo sin fundamento.
- Esa misma noche va a la casa Marsh convencido de que su autoridad como policía basta para imponer obediencia.
- La visita no comienza necesariamente como una misión de asesinato.
- La situación escala:
  - Blake dispara primero a la madre;
  - el padre queda como testigo;
  - Blake decide ejecutarlo para eliminarlo.
- Ese segundo homicidio es el verdadero cruce moral del personaje: el primer disparo puede surgir de escalada/pánico; el segundo es una decisión consciente.
- Dylan observa sólo fragmentos y la placa, no la cara.
- Blake se marcha sin saber que el niño vio algo.
- La muerte posterior de Vera y la limpieza de Volpi desvían la investigación hacia una narrativa equivocada.

### Razón dramática de Blake

La propuesta busca que Blake no haya sido un “supervillano secreto” ya formado en Libro I.

Su evolución sería:

1. policía arrogante y vanidoso;
2. primer encubrimiento serio;
3. abuso de autoridad;
4. homicidio que se sale de control;
5. ejecución del testigo;
6. descubrimiento de que una estructura desconocida limpió su crimen;
7. décadas de aprendizaje institucional y paranoia;
8. eventual posición de poder dentro de Asuntos Internos.

La regla de diseño es que Blake no se convierta en antagonista final por resentimiento hacia Chiara o Kal. Su vínculo con ellos debe ser una ironía histórica, no el motor del conflicto de Elenna.

## Hipótesis forense útil

El diseño permite que la evidencia balística histórica haya sido correcta y que la interpretación sea la equivocada:

- los proyectiles de los tres muertos pueden vincularse a una misma arma;
- durante años Nicholas puede asumir:
  - misma arma = mismo tirador;
- la verdad es:
  - Blake dispara a los padres;
  - Dylan dispara a Vera.

Esto conserva un policial más sólido porque el error está en la lectura de los hechos, no necesariamente en datos forenses falsificados.

## Preguntas pendientes

1. ¿Qué tipo exacto de soborno policial ocultó Blake y qué relación causal tuvo con la agresión al padre Marsh?
2. ¿Quién informa al padre Marsh de que Blake ocultó la evidencia?
3. ¿Cómo ocurre exactamente la confrontación en la comisaría sin dejar un registro tan obvio que señale a Blake de inmediato?
4. ¿Cómo llega Dario Varek a enterarse tan rápido de la ejecución de los Marsh?
5. ¿Quién llama a Dario?
6. ¿Cuánto tiempo transcurre entre:
   - muerte de los padres;
   - llegada de Vera;
   - disparo de Dylan;
   - llegada de Volpi;
   - llegada de Nicholas?
7. ¿La ventana abierta es intervención de Volpi o ya estaba abierta?
8. ¿Volpi sabe con certeza que Dylan disparó a Vera o sólo lo deduce?
9. ¿Qué hace Volpi con el arma después de recogerla?
10. ¿Quién es exactamente el “tercero” al que Volpi entrega a Dylan antes de que el niño termine bajo influencia Varek?
11. ¿Cuándo y cómo se establece en canon que Blake es el agresor original?
12. ¿Qué material vigente en `develop` debe reemplazarse si Blake deja de ser personaje transitorio y pasa a ser némesis histórica de Nicholas?

## Regla de revelación

No revelar la secuencia completa antes de **Camino a Casa**.

Antes de VII pueden existir:
- inconsistencias;
- archivos incompletos;
- pistas sobre Dylan;
- vínculos con Varek;
- Volpi;
- dudas sobre la lectura histórica del caso.

Pero la reconstrucción real de aquella noche debe depender del testimonio de Dylan una vez detenido y juzgado.

El efecto buscado es:

> detener a Dylan Marsh resuelve al asesino serial, pero abre por primera vez el caso Vera real.
