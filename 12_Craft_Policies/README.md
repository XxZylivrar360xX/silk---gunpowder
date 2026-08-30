# 12_Craft_Policies

Políticas de oficio narrativo para escribir y editar prosa en `10_Chapters/` y `11_Books/`.

`00_Biblia/` fija qué es la novela. Esta carpeta fija cómo no romperla al escribir: qué sabe cada personaje, qué hitos ya existen, cómo habla cada voz, y qué patrones de diálogo o puesta en escena hay que evitar.

## Estructura

- `revelations/` — ledger de misterios, semillas y revelaciones. Registra qué sabe cada personaje, desde cuándo, y qué no debe insinuarse todavía.
- `milestones/` — índice cronológico de hitos ya fijados. No duplica `06_Relationships/Hitos`; apunta a él.
- `voice/` — fichas de voz. Antes de escribir diálogo, leer la ficha de cada personaje que habla. Si no existe, crearla primero.
- `dialogue_rules/` — anti-patrones de diálogo. No son prohibiciones absolutas; son alarmas contra formas que vuelven intercambiables a los personajes.
- `staging_rules/` — anti-patrones de puesta en escena: espacio físico, cuerpos, silencios, transiciones y escenas resueltas por resumen.
- `editorial/` — política de edición posterior al triaje, zonas protegidas y registro del piloto determinista 01–10.
- [[12_Craft_Policies/Redaccion_De_Capitulos]] — política base para pasar de estructura a capítulo provisional.

No se rescata `powers/` de *Memories Of A Ghost*: era específica de combate fantástico. Para *Seda y Pólvora*, la equivalencia será logística, violencia, favor, relato y ciudad, no poderes.

## Precedencia

En caso de conflicto:

1. **`revelations/` manda.** Ninguna escena puede revelar, insinuar o pagar algo antes de lo permitido por el ledger.
2. **`milestones/` manda sobre el instinto de giro.** Si algo ya es hito, no se contradice ni se repite como si fuera la primera vez.
3. **`voice/` manda sobre la línea bonita.** Una frase brillante que no pertenece a esa boca se corta.
4. **`dialogue_rules/` y `staging_rules/` son la última capa.** Sirven para auditar cuando la escena ya respeta canon, hitos y voz.
5. **`Redaccion_De_Capitulos` gobierna la unidad de capítulo.** Si una escena no mueve poder o consecuencia, puede ser buena prosa y aun así no ser capítulo.

## Flujo antes de escribir

1. Revisar el `00_Book_Map.md` del libro activo.
2. Leer [[12_Craft_Policies/Redaccion_De_Capitulos]].
3. Revisar `milestones/INDEX.md` si la escena depende de un hito ya fijado.
4. Revisar `revelations/Book_01_Seda_y_Polvora.md` si la escena toca secretos, mentiras, rituales, pasado familiar, identidad o información retenida.
5. Leer las fichas de voz de cada personaje que habla.
6. Si la escena es diálogo emocional largo, repasar `dialogue_rules/`.
7. Antes de cerrar, repasar `staging_rules/`: lugar, cuerpos, silencio, transición y costo físico/social.

## Flujo al cerrar escena o capítulo

1. Si se sembró, reveló o pagó algo, actualizar `revelations/`.
2. Si ocurrió un hito irreversible, agregar una fila o nota a `milestones/INDEX.md`.
3. Si una voz reveló un patrón nuevo real, actualizar su ficha.
4. Si apareció un defecto repetido dos veces, promoverlo a regla en `dialogue_rules/` o `staging_rules/`.
5. Si cambió canon o continuidad, actualizar `INDEX.md`, `98_Agent_Handoff/` y `log.md`.

## Índice de reglas de diálogo

| Regla | Descripción |
|---|---|
| [01-interrogatorio-terapeutico-escalonado](dialogue_rules/01-interrogatorio-terapeutico-escalonado.md) | Un personaje acorrala al otro con preguntas cada vez más precisas hasta producir una confesión limpia. |
| [02-confesion-de-identidad-como-funcion](dialogue_rules/02-confesion-de-identidad-como-funcion.md) | El personaje reduce su herida a "soy sólo mi función". |
| [03-antitesis-limpia-como-cierre-de-verdad](dialogue_rules/03-antitesis-limpia-como-cierre-de-verdad.md) | Cierre pulido tipo "no es X, es Y". |
| [04-resumen-perfecto-del-otro](dialogue_rules/04-resumen-perfecto-del-otro.md) | El interlocutor formula la herida del otro mejor que él mismo. |

## Índice de reglas de puesta en escena

| Regla | Descripción |
|---|---|
| [01-vineta-de-tesis-sin-encarnacion-espacial](staging_rules/01-vineta-de-tesis-sin-encarnacion-espacial.md) | La tesis llega antes que el lugar. |
| [02-encuentro-grande-resuelto-por-resumen-funcional](staging_rules/02-encuentro-grande-resuelto-por-resumen-funcional.md) | Una reunión, golpe, amenaza u operación se resume por función sin beats físicos/sociales intermedios. |
| [03-presentacion-por-catalogo-en-vez-de-gesto](staging_rules/03-presentacion-por-catalogo-en-vez-de-gesto.md) | Un personaje o su pasado entran por inventario físico en vez de por un gesto que se le escapa al cuerpo. |

## Fichas de voz existentes

| Personaje | Archivo |
|---|---|
| Cole Mercer | [voice/Cole_Mercer.md](voice/Cole_Mercer.md) |
| Chiara Bellandi | [voice/Chiara_Bellandi.md](voice/Chiara_Bellandi.md) |
| Dario Varek | [voice/Dario_Varek.md](voice/Dario_Varek.md) |
| Matteo Bellacorte | [voice/Matteo_Bellacorte.md](voice/Matteo_Bellacorte.md) |
| Mabel Ortiz | [voice/Mabel_Ortiz.md](voice/Mabel_Ortiz.md) |
| Fabrizio Rinaldi | [voice/Fabrizio_Rinaldi.md](voice/Fabrizio_Rinaldi.md) |
| Tommaso Lusardi | [voice/Tommaso_Lusardi.md](voice/Tommaso_Lusardi.md) |
