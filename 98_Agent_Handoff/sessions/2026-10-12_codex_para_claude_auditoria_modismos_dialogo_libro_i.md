# 2026-10-12 - Codex -> Claude Code - Auditoría de modismos en diálogos del Libro I

## Objetivo

Localizar expresiones que puedan hacer que los diálogos de *Máscaras de Cristal* suenen demasiado mexicanos frente al objetivo de un español neutro o casi neutro. No se modificó prosa.

## Cobertura y criterio

- Barrido de los 53 capítulos con prosa: 1–25, 24b, 24c, 26–50 y 50b, en las tres partes de `11_Books/Book_01_Mascaras_De_Cristal/`.
- Búsqueda de mexicanismos marcados y construcciones coloquiales regionales; revisión en contexto de cada coincidencia. Se excluyeron coincidencias en notas de trabajo y narración cuando no eran diálogo.
- Se separan los marcadores inequívocos de los usos discutibles. Una alerta no implica que la línea deba cambiar: hace falta ponderar personaje, situación y canon.
- Criterio de voz: preservar italiano de Chiara y darija/francés ocasional de Nadir. Su ficha dice expresamente que Nadir no usa jerga mexicana o centroamericana.

## Hallazgos prioritarios

### A. Mexicanismos claros o de sabor mexicano fuerte

| Ubicación | Voz | Texto localizado | Dictamen |
|---|---|---|---|
| Cap. 3, línea 419 | Kal | «Ahorita los alcanzo.» | **Revisar.** “Ahorita” es un marcador mexicano muy visible; no corresponde a un rasgo de voz establecido para Kal. |
| Cap. 31, línea 109 | Kal | «Ahorita vengo.» | **Revisar.** Mismo marcador; el contexto no le da una motivación regional. |
| Cap. 34, línea 182 | Kal | «Ahorita le regreso la llamada.» | **Revisar.** Mismo marcador en una llamada formal a Varek; destaca más por el contraste de registro. |
| Cap. 46, línea 203 | Danny | «…donde está su coche ahorita…» | **Revisar.** Uso de “ahorita” para situar el coche; no hay ficha que lo establezca como idiolecto de Danny. |
| Cap. 5, línea 1181 | Kal | «Eso es lo que se me hace raro.» | **Revisar.** “Se me hace” con sentido de “me parece” tiene sabor mexicano. |
| Cap. 5, línea 1184 | Chiara | «A mí también se me hizo extraño.» | **Revisar.** Misma construcción en Chiara, cuya voz sí tiene una marca italiana definida, no mexicana. |
| Cap. 48, línea 192 | Rafe | «…se vende todo, nomás que caro.» | **Revisar con contexto.** “Nomás” es marca regional fuerte. Puede funcionar como voz local de Rafe, pero no está documentada como rasgo suyo ni como excepción nacional explícita. |
| Cap. 48, línea 260 | Rafe | «Se fueron, nomás…» | **Revisar con contexto.** Repite el mismo marcador dentro de su parlamento. La repetición ayuda a construir voz, pero también consolida el color mexicano. |
| Cap. 50, línea 69 | Mabel | «Que nomás cajas.» | **Revisar.** “Nomás” aparece en el habla de Mabel, al repetir un recado. Si se busca neutralidad general, es candidato; si se conserva, conviene decidirlo como rasgo consistente de su voz. |
| Cap. 50, línea 199 | Chiara | «Ni siquiera me cobras. Nomás quitas.» | **Prioridad alta.** “Nomás” aparece en el monólogo privado de Chiara y no parece una imitación de otra voz; es el caso más discordante con su perfil italiano. |

### B. Regionalismo menos marcado o discutible

| Ubicación | Voz | Texto localizado | Dictamen |
|---|---|---|---|
| Cap. 18, línea 430 | Chiara | «…que se cuentan de a poco.» | **Revisar por neutralidad, no clasificar como mexicanismo.** “De a poco” es comprensible y se usa en distintas regiones, pero suena más regional que “poco a poco”. Aquí aparece en voz de Chiara. |
| Cap. 48, línea 260 | Rafe | «…si Rafe ya se había vuelto pendejo a su edad.» | **Observación, no alerta automática.** Insulto extendido en varias zonas de América; puede sonar mexicano por el conjunto de “nomás”, pero no basta por sí solo para pedir neutralización. Revisar la voz local de Rafe en contexto. |

## Voces protegidas y falsos positivos

- **Nadir:** el barrido no encontró “ahorita”, “nomás” ni los otros marcadores buscados en sus diálogos. Sus apariciones conservan las marcas aprobadas de darija, vocabulario comercial y cadencia. No encontré motivo para tocar su español por esta auditoría.
- **Chiara:** conservar sus inserciones de italiano; no son mexicanismos. Las alertas de los caps. 5, 18 y 50 son construcciones españolas, no sus rasgos italianos.
- **“Mande” en caps. 1 y 10:** aparece en «Mande la dirección» / «Mande los papeles» con sentido verbal de “envíe”; no es el uso mexicano de «¿mande?» como respuesta y no se cuenta como alerta.
- **“De a poco” en narración (caps. 6, 31 y 39):** no se incluyó en los hallazgos de diálogo. Se registra solo como patrón léxico posible si luego se desea una pasada separada de narrador.
- Expresiones como «no pasa nada», «de veras», «sale», «qué tal» o «un buen rato» aparecieron en la búsqueda de control, pero no se marcaron por ser ampliamente compartidas o por tener otro sentido en contexto.

## Resultado

Hay 10 ocurrencias prioritarias de mexicanismos claros: cuatro de «ahorita», dos de «se me hace» y cuatro de «nomás». Se agregan dos observaciones regionales: «de a poco» y «pendejo». No se editaron líneas ni se propusieron sustituciones cerradas para conservar la decisión del autor sobre el grado de neutralidad y las voces locales.

## Fuentes consultadas

- `CLAUDE.md`, `98_Agent_Handoff/START_HERE.md`, `98_Agent_Handoff/CURRENT_BRIEF.md`, `INDEX.md`, `98_Agent_Handoff/AGENT_ROLES.md`.
- `12_Craft_Policies/editorial/EDITORIAL_POLICY.md`, `12_Craft_Policies/editorial/DO_NOT_TOUCH.md`.
- `12_Craft_Policies/voice/Nadir_Amrani.md`, `Kal_Mercer.md`, `Chiara_Bellandi.md`, `Dario_Varek.md`.
- Capítulos con hallazgos: 3, 5, 18, 31, 34, 46, 48 y 50.

## Pendiente

El autor decide cuáles marcadores forman parte deliberada de la voz local de Rafe, Mabel y Danny. Si aprueba neutralizar los candidatos prioritarios, Claude Code puede proponer microajustes preservando la intención y las líneas canon.
