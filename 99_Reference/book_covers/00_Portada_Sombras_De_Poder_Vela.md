# Portada de *Sombras de Poder*: la vela

**Estado:** DECISIÓN DEL AUTOR (2026-11-16): v1 aprobada como portada. El autor eligió el concepto «la vela y el collar» y, tras el choque con el canon, el prompt A sin collar. Las imágenes generadas son referencia, no canon. Sustituye como dirección a [[99_Reference/book_covers/Sombras_De_Poder_VICTOR_PAZ_v0_retirada.png]] (ajedrez con la reina blanca caída), retirada el 2026-11-16 y conservada con ese nombre.

## Por qué este concepto

- **El título:** las sombras las proyecta una luz, y la luz del libro es la vela que Chiara enciende cada vez que Kal sale a «trabajar» ([[04_Concepts/Fe_y_Velas]]). El poder se paga: Kal acumula poder reuniendo gente; Chiara, mientras pierde gente ([[11_Books/Book_02_Sombras_De_Poder/00_Plan_Cuatro_Partes]], Brújula).
- **El final sin contarlo:** la noche de la tormenta empieza con la vela de Kal en la iglesia y la de Chiara antes de salir; afuera, las bandas contra Crowe y la escalada policial.
- **La serie:** objeto con luz lateral, como *Máscaras de Cristal*. Allá la máscara tras la ventanilla; aquí la ciudad tras la ventana. El vidrio rojo de la veladora da el acento rojo.

## Choque con el canon (y cómo se resuelve)

[[04_Concepts/Fe_y_Velas]] reparte la promesa: «La vela es lo que Chiara hace cuando él se va. El collar es lo que Kal lleva cuando ya se fue.» En el incendio, el collar sobrevive porque Kal lo lleva puesto. Un collar junto a la vela diría que Kal salió sin él: un mal presagio que el libro no cumple.

- **Prompt A (principal):** la vela con el fósforo recién apagado, sin collar. El fósforo es canon: «Antes de una salida mala, tarda más en soltar el fósforo».
- **Prompt B (variante con collar):** sólo si el autor acepta esa lectura o la quiere como ambigüedad deliberada.

## Lo que fija el canon (no contradecir)

| Elemento | Canon | Fuente |
|---|---|---|
| Vela | Ritual de Chiara cada vez que Kal sale; reza en italiano | [[04_Concepts/Fe_y_Velas]] |
| Fósforo | Antes de una salida mala tarda en soltarlo | ídem, «Usos narrativos» |
| Collar | Placa grabada TORNA A CASA; lo lleva Kal | [[06_Relationships/Hitos]], [[01_Timeline/03_Libro_02_Sombras_De_Poder]] |
| Noche final | Diciembre A4, tormenta; escalada policial (alerta, SWAT) | Plan Cuatro Partes, «El final» |

**DISEÑO (no fijado en el canon):** el vidrio rojo de la veladora, el alféizar y la habitación. No usar la imagen para fijar dónde enciende Chiara la vela esa noche.

Fuera: ajedrez, pistolas, sangre, crucifijos o santos, caras, manos, texto legible (el grabado del collar, si aparece, de canto).

## Prompts (en inglés, para el generador de imágenes)

Pide siempre la imagen **sin texto**; la tipografía se compone después con [[tools/portada/componer_portada.py|el script de portada]].

### A. La vela y el fósforo (principal)

> Cinematic book cover photograph, vertical 1:1.6. Night, heavy winter storm. On a dark wooden windowsill inside a quiet room, a single votive candle burns in a deep red glass holder. Beside it lies a spent wooden match with a blackened tip, a thin thread of smoke still rising from it. The small flame throws long, soft shadows across the sill toward the viewer. Beyond the rain-streaked window glass, a dark city at night: blurred high-rises, wet streets, and far away the faint red and blue glow of police lights. Warm candle glow against a cold blue city. Low-key lighting, deep blacks, large empty dark area in the upper third. Intimate, devout, foreboding. No people, no hands, no text, no religious statues, no crucifix, no weapons.

### B. Con el collar (variante; ver «Choque con el canon»)

> Same scene as above. Next to the candle, a thin chain necklace with a small rectangular metal plaque lies loosely coiled on the sill, the plaque turned on its edge so no engraving is visible, catching a sliver of the candle light.

**Negativos para cualquier generador:** `chess, chess pieces, gun, pistol, blood, crucifix, saint statue, rosary, face, person, hands, text, letters, engraving, watermark, logo`.

### Cómo pedir correcciones

ChatGPT regenera la imagen completa en cada edición y puede romper la perspectiva (pasó con *Máscaras*). Pide **una corrección por vez**, empezando con «Keep this exact image, composition and lighting. Only change…», y guarda cada versión buena antes de pedir otra.

## Composición

- La vela entre el 55 % y el 80 % de la altura, ligeramente descentrada; la ciudad en el tercio medio.
- Tercio superior oscuro para el título; franja inferior oscura para el autor.
- Tipografía igual a *Máscaras de Cristal* y *Voto de Ceniza*, con «SEDA Y PÓLVORA · LIBRO II» arriba.

## Especificaciones de entrega (KDP)

Las mismas de [[99_Reference/book_covers/00_Portada_Mascaras_De_Cristal_Colombina]]: 2560 × 4096 para el ebook; tapa blanda cuando haya número de páginas; prueba de miniatura a 160 px.

## v1 compuesta (2026-11-16)

- **El autor eligió el prompt A (sin collar)** y pidió un fósforo de madera (largo; en la imagen salió de tamaño normal y se aceptó así).
- **Base:** primera generación de ChatGPT, sin ediciones: [[99_Reference/book_covers/Sombras_De_Poder_Vela_base.webp]] (992 × 1586).
- **Portada:** [[99_Reference/book_covers/Sombras_De_Poder_Vela_v1.png]] (2560 × 4096), con `python -B tools/portada/componer_portada.py --libro sombras --base 99_Reference/book_covers/Sombras_De_Poder_Vela_base.webp --salida 99_Reference/book_covers/Sombras_De_Poder_Vela_v1.png`. Misma tipografía que *Máscaras de Cristal*; «Poder» con inicial alta.
- **Para la prosa (DISEÑO, no canon todavía):** si se escribe con qué enciende Chiara la vela, que sean fósforos de madera, como en la portada.

## Portada completa para tapa blanda (DISEÑO, 2026-11-22)

Mismo método que [[99_Reference/book_covers/00_Portada_Mascaras_De_Cristal_Colombina#Portada completa para tapa blanda (DISEÑO, 2026-11-16)|*Máscaras de Cristal*]]: extensión hacia la izquierda en ChatGPT, base original pegada encima en el panel derecho, lomo y contraportada con `tools/portada/componer_tapa.py`. Sinopsis: [[11_Books/Book_02_Sombras_De_Poder/00_Sinopsis_Contraportada]] (borrador). El lomo se calcula cuando el libro tenga páginas.

### Prompt de extensión

Adjuntar [[99_Reference/book_covers/Sombras_De_Poder_Vela_base.webp]]:

> Extend this image to the left into a horizontal 3:2 landscape for a book wraparound cover. The original image must stay exactly as it is, at full height, on the right edge. Continue the scene leftward: past the dark wooden window frame, the same wooden windowsill keeps running along the bottom of the image, catching the last faint red and amber glow of the candle and fading into shadow. Above it, the interior wall of a quiet, dark room: old dark wood paneling or plain dark plaster, almost black, with the candle's warm light dying out within a short distance. No second window, no second candle. The left half must be dark and calm, with large areas of soft shadow and almost no detail, to hold text. Same lighting, same color palette, same night storm mood. No people, no hands, no furniture in focus, no text, no logos, no religious objects, no weapons.

### Tapa completa v1 (2026-11-22, provisional)

- **Extensión:** [[99_Reference/book_covers/Sombras_De_Poder_Vela_extension.webp]] (1536 × 1024), primera generación de ChatGPT con el prompt de arriba; la costura con la base no se nota.
- **Tapa:** [[99_Reference/book_covers/Sombras_De_Poder_Tapa_6x9_v1.png]] (4200 × 2775 px), con `python -B tools/portada/componer_tapa.py --libro sombras --paginas 700 --extension 99_Reference/book_covers/Sombras_De_Poder_Vela_extension.webp --base 99_Reference/book_covers/Sombras_De_Poder_Vela_base.webp --sinopsis 11_Books/Book_02_Sombras_De_Poder/00_Sinopsis_Contraportada.md --salida 99_Reference/book_covers/Sombras_De_Poder_Tapa_6x9_v1.png`.
- **Provisional:** el lomo usa 700 páginas de relleno (1.75 in en crema), porque el libro está en redacción; la sinopsis es borrador. Se vuelve a correr con el número real y la sinopsis aprobada.

## Pendiente

- **Aprobada por el autor (2026-11-16):** la v1 es la portada del EPUB de lectura (`COVER` de `tools/build_sombras.py`).
- Escalado por IA de la base antes de la versión impresa.
