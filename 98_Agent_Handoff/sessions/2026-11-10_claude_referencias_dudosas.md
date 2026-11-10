# 2026-11-10 — Las 402 referencias dudosas de numeración (Claude Code)

**Encargo del autor:** resolver las 402 citas que Codex dejó sin tocar el 2026-11-01 ([[98_Agent_Handoff/sessions/2026-11-01_codex_para_claude_referencias_viejas]]), con subagentes por carpeta, consultando solo lo ambiguo. Destino: la **numeración de 47** (2026-11-08), no la de 56 en que se generó la lista.

## Criterio

Cinco lotes por carpeta, sin archivos compartidos. Cada cita se clasificó en una de cuatro categorías:

- **A, no aplica:** código de lote, otro libro, cita archivo:línea, cita que ya coincide con la numeración vigente, o cita que ya no existe.
- **B, histórica:** nota fechada, SUPERSEDIDO o tachada. Conserva la numeración de su época, por convención.
- **C, corregida:** texto vivo cuya escena se verificó en la prosa. Se escribió `Cap. N (*Título*)` en la numeración de 47; el título hace la referencia estable si la numeración vuelve a cambiar.
- **D, ambigua:** no se editó.

Solo se cambió la referencia, nunca la afirmación. Registro íntegro, con antes, después y motivo: [[98_Agent_Handoff/sessions/2026-11-10_claude_referencias_dudosas_resolucion.csv]].

## Resultado

**A 106 · B 231 · C 42 · D 23.** Las A incluyen 3 citas de la ficha de Anya, que ya no está en el vault. Hubo 27 archivos editados, entre fichas, facciones, lugares, staging_rules y `00_Trilogy_Structure`. En la celda de la bisagra de `00_Trilogy_Structure`, «Cap. 56 (archivo 50b)» pasó además a «Cap. 47», para que la celda no quedara mezclada.

## Para el autor: afirmaciones que el nuevo cauce pudo volver falsas

En estos casos la duda es de contenido, no de número. La escena citada ya no ocurre como dice la ficha.

- [[02_Characters/Iris_Harlow]] (2 citas, una en un bloque CANON): Trix opera a Chiara «en el Cap. 9», es decir, *El corral*, hoy Cap. 23. En la prosa vigente dice «Por ahora no vamos a operar».
- [[02_Characters/Jim_Keegan]]:
  - El balcón de Dale y Ruth (antes en el archivo 10) está en Escenas_Eliminadas y espera un capítulo POV Kal.
  - «Sí. Afganistán.» ya no está en *El mirador* (Cap. 18); se le dice a Chiara en el Cap. 6.
- [[05_Locations/El_Taller_del_Norte]] y [[05_Locations/San_Aurelio]] (H5, «Cap. 27»): Varek amenaza a Chiara en el taller, pero en el archivo 26 (Cap. 26) ya no la amenaza, y *Lleve equipaje* se retiró.
- [[02_Characters/Walter_Keegan]] (2 citas, «Cap. 9»): Walt ayuda a Corrado a desaparecer. No aparece ni en el archivo 08 ni en el 24c; puede ser trasfondo no escrito.
- [[03_Factions/Fiscalia_de_San_Aurelio]] («Cap. 23»): «un favor de prensa» no está en la prosa.
- [[05_Locations/Mapa_Operativo_de_San_Aurelio]] («Cap. 9»): «Kal llega en siete» no está en la prosa. En *La balanza* tarda catorce minutos.
- Revisar también, aunque la referencia se corrigió (C):
  - [[03_Factions/Fiscalia_de_San_Aurelio]]: la ficha dice «sale del Monarch», pero en el Cap. 6 sale del restaurante.
  - [[05_Locations/El_Lago]]: *Lake Meriwether* ya no aparece en la prosa.
  - [[02_Characters/Rocco]]: la «mancha blanca» y el collar «Es tu perro, Danny» no están en el archivo 05c.
  - [[02_Characters/Giancarlo_Krane]]: «traje caro» no aparece literal en el Cap. 22.

## Para el autor: numeración ambigua (candidatas)

| Ficha | Cita | Candidatas |
|---|---|---|
| [[02_Characters/Blake_Stanton]] | Cap. 29 (Kal entra a la mesa de Varek) | 27 *Una silla* o 28 *Media Baraja* |
| [[02_Characters/Michael_Grayson]] | Capítulo 12 (regla del teléfono, tienda, cazo) | 14 *La regla del teléfono*; la «primera presencia» quizá ya es el 1 |
| [[02_Characters/Russell_Whitaker]] | Cap. 5 (Russ llama «Mercer» a Kal) | Russ no aparece en la prosa del 5 ni del 6 |
| [[02_Characters/Silas_Crowe]] | Caps. 1, 3, 9, 11 y 17 | Hoy aparece en los caps. 1, 3, 11, 13, 16 y 17 |
| [[06_Relationships/Hitos]] | Capítulo 9 (el sospechoso que Kal secuestró) | 23 *Oveja entre lobos* o 24 *Vienes conmigo* |
| [[05_Locations/San_Aurelio]] | Caps. 26–31; 7–11 y 38–50b | La línea mezcla épocas; hay que reescribirla entera |
| [[07_Ideas/Origen_de_i_Sussurri]] | torneo del Capítulo 11 | ¿13 *Roma Atrii*? |
| [[12_Craft_Policies/dialogue_rules/05-esticomitia-de-una-sola-voz]] | Capítulo 6 (pasillo Chiara–Tommaso) | Coda del 5 (antes 05b) o el 6 |
| [[12_Craft_Policies/staging_rules/05-gesto-de-manos-en-serie]] | Cap. 10 (dedos a la sien) | 12 *Dos sillas vacías* u 11 *La balanza* |
| [[12_Craft_Policies/voice/Hector_Navarro]] | Caps. 1, 3, 5, 16, 23 y 24c | El 16 es hoy el 14; la lista mezcla épocas |
| [[12_Craft_Policies/voice/Kal_Mercer]] | Caps. 35-50 | Hoy 33–47, pero toda la línea está en numeración de Prefijo |
| [[98_Agent_Handoff/BACKLOG]] | capítulos 2 y 10 (Corrado vivo) | 8, 13 o 19 |

## Fuera de alcance, para después

Las **917 referencias que Codex sustituyó el 2026-11-01** quedaron en la numeración de 56, que tampoco es la vigente desde el 2026-11-08. Los agentes detectaron varias en texto vivo, por ejemplo en `Giancarlo_Krane` («Cap. 25», «Cap. 49 (archivo 44)») y `11_Books/README` («Cap. 56», «Cap. 55»). Llevarlas a 47 es otra pasada mecánica, del tamaño de esta.
