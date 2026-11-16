# Portada de *Cuentas de Sangre*: el hilo rojo

**Estado:** DISEÑO (2026-11-16). Concepto elegido por el autor: el foco deja de ser la silla (quién gobierna el vacío) y pasa a ser **la salida de Kal y Chiara y las cadenas del pasado que los detienen de volver a Elenna**, conservando el expediente de Meridian. Las imágenes generadas son referencia, no canon. Sustituye como dirección a [[99_Reference/book_covers/Cuentas_De_Sangre_VICTOR_PAZ.png]] (sillón, mano con anillo, expediente con fotos de frente), que se conserva hasta aprobar la nueva.

## Por qué este concepto

- **El libro:** *Cuentas de Sangre* trata de hacer posible la salida ([[00_Biblia/00_Trilogy_Structure]], Libro IV). Kal: `ser indispensable → construir reemplazo → soltar`. Chiara: `… → terminar la ausencia`. Tras el IV no pueden volver a pertenecer a San Aurelio: Meridian contra Kal, La Mesa contra Chiara (CANON DEL AUTOR, 2026-11-15).
- **Las cadenas:** Meridian «convierte vidas en expedientes» y reconstruye la estructura causal del poder de Kal ([[03_Factions/Fuerza_de_Tarea_Meridian]]); a Chiara la atan Il Consorzio y una herida federal (la redada contra su padre). Corrado no se revela para no atraparla «en el pasado y en las cadenas de Il Consorzio» ([[11_Books/Book_04_Cuentas_De_Sangre/00_Diseno_Complot_De_La_Mesa]], §1.6).
- **La imagen:** el tablero de Meridian, con hilos rojos que convergen en una foto de vigilancia de Kal y Chiara **de espaldas, caminando juntos hacia la salida**. Se van, pero la red sigue atada a ellos. El hilo es cadena y es la sangre del título; el tablero es el libro mayor de lo que deben ([[11_Books/00_Libro_Mayor_Deudas_Saga]]). Elenna queda fuera de cuadro: es hacia donde caminan.

## Lo que fija el canon (no contradecir)

| Elemento | Canon | Fuente |
|---|---|---|
| Kal | 1.92 m, rubio de pelo desordenado, barba corta | [[02_Characters/Kal_Mercer]] |
| Chiara | Pelo negro largo, hasta media espalda | [[02_Characters/Chiara_Bellandi]] |
| Meridian | Fuerza de tarea **federal**; cabeza: Callahan | [[03_Factions/Fuerza_de_Tarea_Meridian]] |

**DISEÑO (no fijado):** el tablero de corcho, los hilos, la ropa, el lugar hacia el que caminan. La ficha de Meridian no dice FBI: **sin sellos ni insignias de agencias reales** (además, son marcas oficiales).

Fuera: caras de frente o reconocibles, armas, sangre literal, la silla, sellos del FBI o de cualquier agencia, texto legible salvo, opcionalmente, «MERIDIAN».

## Prompts (en inglés, para el generador de imágenes)

Pide siempre la imagen sin título ni autor; la tipografía se compone con [[tools/portada/componer_portada.py|el script de portada]].

### Primer intento (2026-11-16): lo que no funcionó

El prompt A original (corcho con hilo rojo radial) dio una base aceptable, pero el autor señaló dos fallas: **Kal y Chiara no se parecen a ellos** (él casi no le saca altura a ella) y **parece el tablero de un universitario, no una investigación federal**. Además, el tablero puede **contar la saga del I al III**. El prompt v2 sustituye al A.

### Guion del tablero (DISEÑO; lo que Meridian tendría)

El tablero es la versión federal del expediente de fotos que Halbrook abre al bajar del helicóptero en el epílogo del Libro I ([[11_Books/Book_01_Mascaras_De_Cristal/00_Plan_Arco_Final_Sin_Kal]]). Sólo lo que Meridian puede saber: **nada de Elenna viva**.

| Libro | Hecho (canon) | En el tablero |
|---|---|---|
| I | El apagón de Camp Alder, pasada la medianoche; Halbrook saca a Kal y aterriza al alba en Kingsley Field | Foto aérea de una base con el perímetro a oscuras; helicóptero en una pista al amanecer |
| I | La persecución de Collins: el Peugeot rojo y el giro de 360 en la fuente de Plaza Corona, grabado por la cámara del poste | Fotograma granulado de cámara de tráfico, con sello de hora, de un hatchback rojo derrapando alrededor de una fuente |
| I | Keene, muerto en Plaza Corona por Volpi: «una muerte expuesta» | Escena del crimen nocturna en una plaza, cuerpo bajo una sábana, cinta policial |
| I–II | El Tasador (Crowe): asesina a Boone, incendia el loft | Foto de vigilancia de un hombre corpulento con X roja; interior de un loft quemado |
| II | Fabrizio, muerto en su apartamento al abrir el libro | Departamento con marcadores amarillos de evidencia |
| II | Meiko: el Camaro; su entierro | Camaro negro; foto con teleobjetivo de un entierro (los federales fotografían a los asistentes) |
| II | La tormenta: cae Crowe, escalada policial | Calle inundada de noche con luces de patrulla y SWAT |
| III | Muerte pública de Halbrook (la ciudad cree que fue Kal o Nadir) | Recorte de prensa sobre la muerte de un general, titular ilegible |
| Todo | La estructura de Kal y Chiara | Gráfico de vínculos impreso (organigrama con fotos tipo credencial y líneas rectas), transferencias, registros telefónicos con marcatexto, bolsas de evidencia con etiqueta de custodia |

Los muertos llevan una **X roja de plumón**; el rojo del concepto ya no es hilo sino **plumón y X**, como en una pizarra real. En el centro, la foto nueva: Kal y Chiara de espaldas, saliendo, con un círculo rojo y flechas que llegan desde el gráfico.

### Prompt v2 (principal)

**Adjunta a ChatGPT** las referencias realistas [[99_Reference/character_art/Kal_Mercer.png]] y [[99_Reference/character_art/Chiara_Bellandi.png]] y dile: «Use the attached images only for body type, hair and clothing style of the two people seen from behind».

> Cinematic book cover photograph, vertical 1:1.6. A federal organized-crime task force war room at night, almost dark, lit by the cold glow of a computer monitor and a single desk lamp. Filling the frame is a large white magnetic case board, worn and dense, the way real federal investigations look — not a cork board, no string. It holds: a printed link-analysis chart (boxes with small ID-style photos joined by straight black lines); a horizontal timeline of printed cards across the board; black-and-white evidence photos held by magnets; wire-transfer flowcharts and phone records marked with yellow highlighter; small evidence bags with chain-of-custody labels. Several photos are crossed out with a red marker X. Among the evidence photos: an aerial night shot of a military base with its perimeter lights dark; a helicopter on a small airfield at dawn; a grainy traffic-camera still with a timestamp of a small red hatchback drifting around a plaza fountain at night; a covered body in a plaza behind police tape; the burned-out interior of a loft; an apartment crime scene with yellow evidence markers; a black muscle car; a long-lens photo of a burial in a cemetery; a flooded street at night with police lights; a newspaper clipping with an illegible headline. In the center, larger than the rest and pinned on top as the newest item, a long-lens surveillance photo: a very tall, broad-shouldered man with messy blond hair, a dark jacket and boots, and a noticeably shorter, slender woman with long wavy black hair down to the middle of her back and an elegant dark coat, seen from behind, walking side by side away from the camera toward a bright doorway at dawn. A red marker circle surrounds this photo, and red marker arrows from the chart converge on it. All text on the board is small and illegible, except a printed header strip that reads "MERIDIAN". No faces visible, no agency seals, badges or logos, no weapons, no blood. The upper third of the image is dark (the wall above the board in shadow). Low-key, deep blacks; red marker and the dawn light in the central photo are the only warm accents.

### Variante (si queda estática)

> Same scene. One magnet holding the central photo has slipped, so the photo hangs askew, half free from the board.

**Negativos:** `cork board, red string, pushpins, faces, frontal portrait, FBI seal, badge, government logo, gun, blood, chair, legible text other than MERIDIAN, watermark`.

### Cómo pedir correcciones

Esta vez conviene **generar de nuevo, no editar** la primera imagen: el cambio es de fondo. Después, una corrección por vez, empezando con «Keep this exact image, composition and lighting. Only change…», y guarda cada versión buena antes de pedir otra. Si el generador se satura con tantos elementos, quita primero los del Libro III y conserva el apagón, la cámara de Plaza Corona, el entierro y la foto central.

## Composición

- La foto central entre el 50 % y el 72 % de la altura; la evidencia abriéndose hacia los bordes.
- Tercio superior oscuro para el título; franja inferior oscura para el autor.
- Tipografía de la saga, con «SEDA Y PÓLVORA · LIBRO IV»; «Sangre» con inicial alta.

## Pendiente

- El autor genera con el prompt v2 (adjuntando las referencias) y elige.
- Componer con `componer_portada.py` (falta añadir el Libro IV al script).
