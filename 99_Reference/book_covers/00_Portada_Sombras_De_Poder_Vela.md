# Portada de *Sombras de Poder*: la vela

**Estado:** DISEÑO (2026-11-16); v1 compuesta, espera aprobación. El autor eligió el concepto «la vela y el collar» y, tras el choque con el canon, el prompt A sin collar. Las imágenes generadas son referencia, no canon. Sustituye como dirección a [[99_Reference/book_covers/Sombras_De_Poder_VICTOR_PAZ.png]] (ajedrez con la reina blanca caída), que se conserva hasta que se apruebe la nueva.

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

## Pendiente

- El autor aprueba la v1 o pide ajustes. La copia de lectura del Libro II (`tools/build_sombras.py`) no lleva portada; cuando la lleve, usar la v1 aprobada.
- Escalado por IA de la base antes de la versión impresa.
