# Portada de *Hijos del Silencio*: la presa

**Estado:** DISEÑO (2026-11-16); v1 compuesta, espera aprobación. Concepto del autor: **pensar en grande**, la Presa del Sur con Elenna y Erin. Es la primera portada del libro (no había ninguna). Las imágenes generadas son referencia, no canon.

## Por qué este concepto

- **El escenario:** la Presa del Sur es el único lugar del ciclo con escala para una portada vertical, y el libro la usa en **dos registros** (CANON DEL AUTOR, 2026-10-03): arriba, en el mirador, Erin confiesa y Elenna la pierde; abajo, en la instalación subterránea de desfogue, se enfrentan Ethan, Nicholas y Elenna en la captura ([[11_Books/Book_06_Hijos_Del_Silencio/00_Book_Map]]; [[05_Locations/Presa_Del_Sur]]).
- **La escena:** la discusión sobre Ethan en el mirador, con el agua cayendo tan fuerte que hay que gritar. Erin: «¡Porque te amo, Elenna, te amo y tú ni siquiera puedes verme de la misma manera!» La discusión las aparta ([[07_Ideas/Libro_04_Incubadora/06_Escenas_Faro]], §6, CANON DEL AUTOR).
- **El título:** dos mujeres que no se dicen lo que importa hasta que es tarde, sobre el lugar donde trabaja el hijo del silencio más literal (Ethan es Dylan, el niño que sobrevivió a la noche Vera y nunca habló). Arriba se grita; abajo, en el desfogue, espera lo que calla.
- **La serie:** cambia la escala, no el sistema. Cielo oscuro arriba para el título, una luz, un acento rojo (la luz de advertencia del desfogue).

## Lo que fija el canon (no contradecir)

| Elemento | Canon | Fuente |
|---|---|---|
| Presa | Represa masiva al sureste de San Aurelio; mirador público sobre el muro, con el agua en cascada; desfogue subterráneo debajo; el lago detrás | [[05_Locations/Presa_Del_Sur]] |
| Ruido | El agua obliga a gritar para hacerse oír | ídem |
| Elenna | Rubio oscuro ceniza, corto y desfilado; estatura media-alta, esbelta | [[02_Characters/Elenna_Mercer]] |
| Erin | Pelo negro, largo y lacio (referencia visual) | [[99_Reference/character_art/Erin_Reyes.png]] |
| Momento | Antes de confirmarse la identidad de Ethan; Elenna todavía lo defiende | Escenas faro, §6 |

**DISEÑO (no fijado):** la hora (el mirador es para ver el atardecer; la escena no fija hora), la ropa (la chamarra de mezclilla con cuello de borrego de Kal para Elenna; chaqueta clara para Erin, como en su referencia) y la luz roja del desfogue.

**Nunca** nombrar en el prompt a la actriz que sirve de referencia para Elenna: no se generan parecidos de personas reales.

Fuera: caras reconocibles (las figuras son pequeñas, a contraluz), Ethan, armas, sangre, texto.

## Prompt (en inglés, para el generador de imágenes)

**Adjunta** [[99_Reference/character_art/Elenna_Mercer.png]] y [[99_Reference/character_art/Erin_Reyes.png]] con la frase: «Use the attached images only for the hair and general silhouette of the two women. They must be small in the frame, with no visible faces».

> Cinematic book cover photograph, vertical 1:1.6, epic scale. An enormous concrete gravity dam, more than 100 meters tall, spanning a deep forested canyon in the hills of Oregon at dusk, seen from far downstream and low, looking up at its sheer face. Most of the dam face is a vast, dry, weathered concrete wall with drainage stains, small inspection-gallery windows and service catwalks. On one side, three massive radial spillway gates are open, and water roars down a steep concrete spillway chute into a churning plunge pool, throwing up a tall column of mist. Along the crest run a road, gate-hoist towers and a row of lampposts, and a small public viewpoint balcony juts out over the face. On that balcony, tiny against the scale of the dam, two young women stand a few steps apart, facing each other in a heated argument: one with short, tousled dark ash-blonde hair and a denim jacket with a sheepskin collar, the other with long straight black hair and a light-colored jacket; backlit, no faces visible. At the foot of the dam stands a concrete powerhouse with transformers, and the steel door of the underground spillway control facility, a small red warning light above it and the faint beam of a flashlight inside. The crest sits just below the middle of the image; the upper 40% is open dark sky, deep blue fading to a thin band of dusk on the horizon. Cold blue tones, mist and spray; the only warm accents are the last light on the horizon, the crest lamps and the red warning light. No text, no logos, no weapons, no blood.

**Por qué cambió (2026-11-16):** el primer intento salió como una cortina baja desbordada de lado a lado, «solo un puente» (autor). Una presa creíble es un muro de más de cien metros, seco casi entero; el agua sale por compuertas radiales a un vertedor; hay casetas de compuertas en la corona y casa de máquinas al pie. Se genera de nuevo, no se edita.

**Negativos:** `close-up, faces, portrait, text, logo, weapon, blood, daylight, summer colors`.

### Qué revisar

- **Escala:** la presa tiene que verse enorme y las dos figuras diminutas. Si salen grandes, se pierde la idea.
- **Las dos:** separadas, frente a frente, distinguibles por el pelo (corto rubio ceniza y largo negro). Sin caras.
- **El desfogue:** la boca del túnel abajo, con la luz roja. Es el «abajo» del libro.
- **El cielo:** oscuro en el 40 % de arriba para el título.

Una corrección por vez, empezando con «Keep this exact image, composition and lighting. Only change…».

## Composición

- Corona de la presa (y las dos figuras) en torno al 50 % de la altura; la cascada hasta el 85 %; la boca del desfogue entre el 70 % y el 80 %, a un lado.
- Tipografía de la saga, con «SEDA Y PÓLVORA · LIBRO VI»; «Silencio» con inicial alta.

## v1 compuesta (2026-11-16)

- **Base:** segunda generación (prompt de la presa masiva), sin ediciones: [[99_Reference/book_covers/Hijos_Del_Silencio_Presa_base.webp]] (992 × 1586). Compuertas radiales, vertedor, casa de máquinas con transformadores, puerta del desfogue con la luz roja y la linterna; Elenna y Erin en un balcón mirador sobre el muro.
- **Portada:** [[99_Reference/book_covers/Hijos_Del_Silencio_Presa_v1.png]] (2560 × 4096), con `python -B tools/portada/componer_portada.py --libro hijos --base 99_Reference/book_covers/Hijos_Del_Silencio_Presa_base.webp --salida 99_Reference/book_covers/Hijos_Del_Silencio_Presa_v1.png`. El enlace es «DEL»; «Silencio» con inicial alta; pie oscurecido hasta el borde (el río claro asomaba), como en el III y el V. A pedido del autor, «Silencio» sube 70 px y «DEL» 35 px, para que quede centrado entre las dos palabras (ajuste por libro del script, sólo para el VI).

## Pendiente

- El autor aprueba la v1. No hay portada anterior que retirar. El Libro VI todavía no tiene build de EPUB.
- Escalado por IA de la base antes de la versión impresa.
