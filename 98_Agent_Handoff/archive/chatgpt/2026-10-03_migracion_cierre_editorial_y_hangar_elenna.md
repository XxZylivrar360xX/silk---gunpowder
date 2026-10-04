# Migracion — Cierre editorial y hangar Elenna

## Alcance

Material incubado en esta conversacion sobre la despedida final de Kal y Chiara con Elenna en el hangar de *Camino a Casa*, con dependencia previa en las cartas manuscritas de Chiara.

Se contrasto con `develop` antes de preparar esta nota.

Las antiguas conclusiones de esta conversacion sobre un Libro I cerrado en el Cap. 44 NO se migran: `develop` registra una arquitectura posterior con arco final 44–50 + 50b. Las auditorias de Partes I–III tampoco se duplican porque ya existen encargos y mapas editoriales en `98_Agent_Handoff/`.

## Decisiones

### M-01 — La despedida cobra las raices de San Aurelio
- Estado: CANON DEL AUTOR
- Enunciado: el intercambio del aeropuerto debe cobrar que Chiara llego a San Aurelio pensando que seria una escala y que la ciudad termino exigiendole raices. Elenna, en contraste, elige conscientemente quedarse en San Aurelio.
- Choca con el repo: No choca. `07_Ideas/Libro_04_Incubadora/06_Escenas_Faro.md` ya establece que Chiara recuerda su llegada como escala y que San Aurelio le exigio raices; falta desarrollar plenamente el payoff de Elenna.
- Archivos afectados: `07_Ideas/Libro_04_Incubadora/06_Escenas_Faro.md`, `07_Ideas/Libro_04_Incubadora/03_Relaciones_Elenna.md`, `11_Books/Book_06_Camino_A_Casa/00_Book_Map.md`

### M-02 — Las cartas son el puente hacia el payoff
- Estado: CANON DEL AUTOR
- Enunciado: Elenna llega a la despedida despues de haber buscado durante libros, a traves de las cartas de Chiara, una aprobacion explicita que nunca recibe por escrito. Las cartas contienen amor, consejo, preocupacion y reconocimiento, pero reservan el payoff verbal para el final.
- Choca con el repo: Parcialmente desarrollado. `07_Ideas/Libro_04_Incubadora/03_Relaciones_Elenna.md` establece que Chiara comunica las cosas importantes mediante cartas manuscritas; `11_Books/Book_05_Juramento_De_Hierro/00_Book_Map.md` fija la presencia de Chiara mediante cartas durante su ausencia fisica. La duracion exacta de “tres libros” requiere reconciliacion con la arquitectura vigente.
- Archivos afectados: `07_Ideas/Libro_04_Incubadora/03_Relaciones_Elenna.md`, `11_Books/Book_05_Juramento_De_Hierro/00_Book_Map.md`, `11_Books/Book_06_Camino_A_Casa/00_Book_Map.md`

### M-03 — Elenna espera esas palabras durante tres libros
- Estado: CANON DEL AUTOR
- Enunciado: el autor fija que Elenna ha esperado escuchar de Chiara “Estoy orgullosa de ti” durante tres libros, buscandolo o esperandolo a traves de las cartas, y lo escucha finalmente al cierre de la historia.
- Choca con el repo: Requiere reconciliacion estructural. `develop` fija explicitamente las cartas de Chiara durante *Juramento de Hierro*, pero no esta propagada todavia una arquitectura epistolar explicita de tres libros.
- Archivos afectados: arco de Elenna, `11_Books/Book_05_Juramento_De_Hierro/00_Book_Map.md`, `11_Books/Book_06_Camino_A_Casa/00_Book_Map.md`, material de relaciones Chiara–Elenna.
- Depende de: M-02

### M-04 — Sustituir `Cuidate` como payoff principal
- Estado: CANON DEL AUTOR
- Enunciado: `Cuidate` deja de ser la culminacion emocional de la despedida de Chiara. El payoff principal pasa al reconocimiento explicito de Elenna.
- Choca con el repo: No choca con canon fuente. La version exploratoria del hangar usaba `Cuidate`, pero no aparece fijado como linea obligatoria en `07_Ideas/Libro_04_Incubadora/06_Escenas_Faro.md`.
- Archivos afectados: futuro capitulo de *Camino a Casa*; material de apoyo del hangar.

### M-05 — Linea exacta sobre la policia
- Estado: CANON DEL AUTOR
- Enunciado: Chiara dice exactamente: `—Jamas pense que le diria esto a una policia.`
- Choca con el repo: No choca; no esta registrado actualmente en `develop`.
- Archivos afectados: `07_Ideas/Libro_04_Incubadora/06_Escenas_Faro.md`, `07_Ideas/Libro_04_Incubadora/03_Relaciones_Elenna.md`, futuro capitulo de *Camino a Casa*.

### M-06 — Linea exacta de orgullo
- Estado: CANON DEL AUTOR
- Enunciado: Chiara dice exactamente: `—Estoy orgullosa de ti, Elenna.`
- Choca con el repo: No choca; no esta registrado actualmente en `develop`.
- Archivos afectados: `07_Ideas/Libro_04_Incubadora/06_Escenas_Faro.md`, `07_Ideas/Libro_04_Incubadora/03_Relaciones_Elenna.md`, futuro capitulo de *Camino a Casa*.
- Depende de: M-02, M-05

### M-07 — Que significa “policia”
- Estado: CANON DEL AUTOR
- Enunciado: la linea es profunda porque Chiara reconoce deliberadamente a su hija como integrante de las fuerzas de la ley pese a su propia historia con policias, federales, expedientes, persecuciones y redadas. No implica que Chiara haya reconciliado globalmente su relacion con la ley: reconoce y acepta la eleccion de Elenna.
- Choca con el repo: No choca.
- Archivos afectados: `02_Characters/Chiara_Bellandi.md`, `02_Characters/Elenna_Mercer.md`, `07_Ideas/Libro_04_Incubadora/03_Relaciones_Elenna.md`

### M-08 — El orgullo no depende de la profesion
- Estado: CANON DEL AUTOR
- Enunciado: `Estoy orgullosa de ti, Elenna` significa que Chiara esta orgullosa de la mujer que Elenna decidio ser, aunque su camino no sea el que Chiara habria elegido para ella. “Policia” es el marco de la aceptacion, no la razon del orgullo.
- Choca con el repo: No choca.
- Archivos afectados: `02_Characters/Chiara_Bellandi.md`, `02_Characters/Elenna_Mercer.md`, material futuro de *Camino a Casa*.

### M-09 — Elenna llevaba tiempo esperando esas palabras
- Estado: CANON DEL AUTOR
- Enunciado: Elenna sabe que su madre la ama, pero ha esperado escuchar explicitamente que Chiara esta orgullosa de ella. El hueco debe existir a traves de las cartas sin convertir a Chiara en una madre cruel o retentiva.
- Choca con el repo: No choca; falta propagacion.
- Archivos afectados: `07_Ideas/Libro_04_Incubadora/03_Relaciones_Elenna.md`, `11_Books/Book_05_Juramento_De_Hierro/00_Book_Map.md`
- Depende de: M-02, M-03

### M-10 — No convertir el hueco en rechazo explicito
- Estado: DISENO
- Enunciado: Elenna no deberia haber preguntado antes `¿Estas orgullosa de mi?` para recibir una negativa o evasion directa. El vacio funciona mejor como algo que busca entre lineas en cartas afectuosas.
- Choca con el repo: No choca.
- Archivos afectados: cartas futuras de Chiara, arco Elenna–Chiara.

### M-11 — Reaccion de Elenna
- Estado: CANON DEL AUTOR
- Enunciado: al escuchar `Estoy orgullosa de ti, Elenna`, a Elenna se le escapa un sollozo real mezclado con una risa de felicidad y lagrimas. No debe reducirse a “algo que no llego a ser sollozo”.
- Choca con el repo: No choca; no esta registrado en `develop`.
- Archivos afectados: futuro capitulo de *Camino a Casa*.

### M-12 — Chiara santigua a Elenna
- Estado: CANON DEL AUTOR
- Enunciado: Chiara santigua/persigna a Elenna antes de irse. No le dibuja ni le traza una cruz pequena en la frente.
- Choca con el repo: No choca; confirma el repo. `07_Ideas/Libro_04_Incubadora/06_Escenas_Faro.md` ya dice que Chiara santigua a Elenna antes de irse.
- Archivos afectados: material futuro de *Camino a Casa*.

### M-13 — Orden emocional de la culminacion
- Estado: DISENO
- Enunciado: la secuencia propuesta es: pago de aeropuerto/raices → memoria de cartas → abrazo → `Ti amo con tutto il… / Mio cuore` → `Jamas pense...` → `Estoy orgullosa...` → sollozo/risa de Elenna → Chiara la santigua → Chiara la suelta.
- Choca con el repo: No choca.
- Archivos afectados: futuro capitulo de *Camino a Casa*.
- Depende de: M-01, M-02, M-05, M-06, M-11, M-12

### M-14 — La raiz no debe explicarse literalmente
- Estado: CANON DEL AUTOR
- Enunciado: evitar una formulacion explicita equivalente a `Una de esas raices era ella`. El texto debe dejar que el lector conecte la historia de Chiara con la decision consciente de Elenna de quedarse.
- Choca con el repo: No choca.
- Archivos afectados: futuro capitulo de *Camino a Casa*.

### M-15 — Soltarla como cierre del gesto materno
- Estado: DISENO
- Enunciado: despues de reconocerla, emocionarse y santiguarla, Chiara finalmente la suelta. El gesto puede cobrar proteccion vs. control sin explicarlo en narracion.
- Choca con el repo: No choca.
- Archivos afectados: futuro capitulo de *Camino a Casa*.

## Descartado

- `Cuidate` como payoff emocional principal de la despedida de Chiara.
- Que Chiara “dibuje” o “trace” una cruz pequena sobre la frente de Elenna; el gesto correcto es santiguarla/persignarla.
- Explicar literalmente que Elenna es “una de las raices” de Chiara.
- Contener la reaccion de Elenna como “algo que no llego a ser sollozo”; el autor quiere un sollozo real mezclado con risa de felicidad.
- Migrar como vigentes las conclusiones de esta conversacion que fijaban el final de *Mascaras de Cristal* en el Cap. 44. `develop` las supersedio.
- Duplicar los dictamenes editoriales completos de Partes I–III: ya estan representados en la `98` y en las auditorias vigentes.

## Preguntas para el autor

1. M-03: ¿quieres que Claude formalice ahora la distribucion de ese arco epistolar de tres libros, o que conserve la decision como canon de resultado y deje pendiente la distribucion exacta por libro?
2. M-13/M-15: ¿quieres fijar como canon el orden `Mio cuore → orgullo → reaccion → santiguarla → soltarla`, o dejar el orden exacto como DISENO hasta el montaje del capitulo definitivo?
