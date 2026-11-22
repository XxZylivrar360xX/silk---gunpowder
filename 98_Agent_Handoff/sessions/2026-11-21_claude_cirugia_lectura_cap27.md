# 2026-11-21 — Claude Code — Cirugía de la lectura, cap. 27

Plan: [[13_Auditorias/Book_01_Mascaras_De_Cristal/Cirugia_Lectura_Libro_I]]. Archivo: `29_El_Patio_Ajeno` (*Una silla*, POV Kal). La prosa queda en BORRADOR y espera la lectura del autor. Se leyó el encabezado completo: las líneas canon de H6 en el loft y la arquitectura del patio del 2026-09-18, que protege la puerta de Camp Alder, la silla, Vivian y la pelirroja, «Bellandi no» y «Estás loco.». También se leyeron la versión de `Escenas_Eliminadas/` y la sesión de origen.

Se comparó contra `b834809`: los barridos `81d252e` (ping-pong) y `346b7ec` (regla 06) tocaron siete réplicas.

## Aplicado (seguro)

- **Restitución (lección 2):**
  - Vuelve literal la puerta de Camp Alder («—Necesito una puerta —dijo.» / «—¿Cuál?» / «—Camp Alder.»). El barrido la había fundido en «La de Camp Alder», y eso chocaba con «la misma rapidez con que había dicho Camp Alder».
  - Salen tres añadidos que explicaban o duplicaban: «Varek no enseña nada que no quiera que veas» (vuelve «—Una multa.»), «La placa se lee, y los horarios los revisé dos veces» (repetía la narración) y «Hasta ayer creía que sí».
  - Sale el dato inventado de Vivian («y con diecisiete el jueves se iban a buscar a otro»). El ping-pong que volvió se corta con un beat: Vivian teclea sin levantar la vista.
  - **Se quedan:** «A Walt las cosas se le dicen de frente, y hoy no traigo cara para eso», porque trae dato (la cara golpeada); «Precisamente por eso», fundido; y la chaqueta a medio colgar.
- **Lectura corrida:**
  - «Me dijo que no levantara piedras». Antes decía «que no me preocupara por nada», cosa que Walt no dijo en el 26.
  - «el Lancia oscuro» (antes «el gris del Lancia»).
  - «la neurocirujana» (antes «del neurólogo»).
- **Segundo lector (mecánico):**
  - Chiara lleva «veintitantos» y «veintitrés minutos» frente a la casa (antes cuarenta y tres): salió del loft después de Kal.
  - El Lancia está «al otro lado de la calle» al abrir. Antes no aparecía en el loft y ella sale en él.
  - «Había más de un Lancia en la ciudad, se dijo», en lugar de «no sabía de qué Lancia hablaban». Así se conserva el «terminó de encajar» de después.
  - Kal descuelga la chaqueta antes de salir, porque después guarda la pistola bajo ella.
  - El Lancia arranca «del otro lado de la reja» (antes, grava hacia la reja).
  - «sobre ropa suya» (antes «la ropa con la que había salido», que Kal no vio).
  - «le había dicho Varek a Chiara».
  - Fuera «en el cajón», que era la imagen de Chiara en el 26.
  - «hace tres noches» (antes «anteayer», dicho un día después) y «de madrugada».
  - «el resto» (antes «tres horas y media», que no daba la cuenta).
  - «Ella conducía como siempre», para separar el sujeto.

## Decisión del autor (mismo día)

- **Excepción de la regla 06:** 28 %, frente a 29 % antes de los barridos. Registrada en `06-replica-minima.md` y en la lección 11.
- «—Ésa ya es su doberman.»
- **Taller de Vivian:** «—¿Hoy no tienes el taller?» / «—A las nueve… La última vez la pelirroja volvió a discutirle…».
- «—Usted primero. Diga qué quiere.» (antes «Entonces diga qué quiere»).
- **Lenguaje neutro («todo hay que neutralizarlo»):**
  - «¿vale?» pasa a «¿sí?» (dos veces en el 27; también «Te vas a mejorar, ¿sí?» en el 23, archivo `24c`).
  - «arcén» pasa a «acotamiento».
  - «grifo» pasa a «llave».
  - Quedan «grifo» en los archivos `02` y `07`, como arrastre en el plan.

## Segundo lector en frío: reportado, sin tocar

- **Costura con el 28:** las fotos se quedan en la barra del loft, y el encabezado las pone en el Lancia (anotado como arrastre).
- **Lo que hay que notar en la escena:**
  - Kal entra armado a casa de Varek y nadie lo revisa.
  - Encuentra la bolsa y el sobre junto a la puerta por donde acaba de entrar.
- **Opacas o forzadas:**
  - «Hasta ahí no le había mentido. Ésa era la primera.» (opaco).
  - «Kal no supo de dónde sabía su nombre», cuando el guardia ya lo llamó Mercer.
  - «porque no sabía que tuviera nada que ocultar» (le lee la mente a Vivian).
  - «una letra… que él conocía de las actas».
  - «Ella acababa de soltarle el brazo».
- **Glosa y aforismos:**
  - «como se cuida un puesto».
  - «nombra una cicatriz».
  - La explicación de la puerta que ella le abre.
  - «Un hombre que entra por la puerta que le abren…».
  - La nube.
  - «para que una mentira se echara a perder sola».
  - «No tenía por qué añadirlo…».
  - La glosa de «Bellandi».
- **Tics:**
  - «el tiempo suficiente» (4).
  - «que era peor».
  - «plano/plana».
  - «un momento largo».
  - «sin prisa».
  - «Una pausa exacta».
- **Léxico:** «un cuerpo de distancia».

## Verificación

- `pingpong_audit`: 0 tramos en el 27 y en el 23.
- `--cortas`: 27 = 45/161 = 28 % (excepción aprobada); 23 = 29 % (excepción ya aprobada).
- `canon_check`, contra HEAD y contra `b834809`: OK en los dos.
- El 27 es CRLF y el 23 es LF; los dos se conservaron.
