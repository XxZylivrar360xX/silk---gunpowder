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

### A. El tablero (principal)

> Cinematic book cover photograph, vertical 1:1.6. A federal investigators' cork evidence board in a dark office at night, lit only by a low desk lamp from below and to the side. The board is covered with grainy black-and-white surveillance photos, property documents, tagged keys and a city map, all connected by taut red strings pinned with brass pushpins. Every red string converges on one central photograph: a long-lens surveillance shot of a tall man with messy blond hair and a woman with long black hair down to the middle of her back, seen from behind, walking side by side away from the camera toward a bright doorway at dawn. Their faces are not visible. Shallow depth of field: the central photo and the strings around it in sharp focus, the edges of the board falling into darkness. The upper third of the image is dark and empty. Low-key, deep blacks, the red strings the only saturated color. No legible text, no agency seals or logos, no weapons, no blood.

### B. El alfiler que cede (variante)

> Same scene. The pushpin holding the central photograph has been pulled half out, and the photo hangs slightly askew, the red strings pulled tight toward it as if it were about to come loose from the board.

Añade la tensión de «¿pueden irse?». Úsala si A queda demasiado estática.

**Opcional, en A o B:** `a manila folder tab at the edge of the board labeled "MERIDIAN"`. Revisa la ortografía; si sale mal, pide quitarlo.

**Negativos para cualquier generador:** `faces, frontal portrait, FBI seal, badge, government logo, gun, blood, chair, legible text, watermark, logo`.

### Cómo pedir correcciones

Una corrección por vez, empezando con «Keep this exact image, composition and lighting. Only change…», y guarda cada versión buena antes de pedir otra.

## Composición

- La foto central entre el 50 % y el 72 % de la altura; los hilos abriéndose hacia los bordes.
- Tercio superior oscuro para el título; franja inferior oscura para el autor.
- Tipografía de la saga, con «SEDA Y PÓLVORA · LIBRO IV»; «Sangre» con inicial alta.

## Pendiente

- El autor genera con A (o B) y elige.
- Componer con `componer_portada.py` (falta añadir el Libro IV al script).
