# 2026-11-10 — Referencias de la numeración de 56 llevadas a la de 47 (Claude Code)

**Encargo del autor:** «Sí, hazlo», es decir, llevar a la numeración de 47 (nuevo cauce, 2026-11-08) las sustituciones que hizo Codex el 2026-11-01 ([[98_Agent_Handoff/sessions/2026-11-01_codex_para_claude_referencias_viejas]]). Viene después de [[98_Agent_Handoff/sessions/2026-11-10_claude_referencias_dudosas]].

## Método

Codex dejó todas sus sustituciones con el formato `Cap. N (archivo X)`. Como el archivo identifica el capítulo, se puede convertir sin ambigüedad. Se rastreó en todo el vault cada `Cap. N (archivo X)` cuyo N fuera el de 56 y distinto del de 47.

- **Excluidos:** sesiones y archivo del relevo, `97_Supersedido`, `99_Reference`, `Escenas_Eliminadas`, el Book_Map del Libro I (sus secciones históricas conservan su numeración) y la tabla de equivalencias.
- **Por script (418):** líneas que nadie tocó después de Codex (comprobado con `git blame`), con archivo activo y sin marcas de época en el contexto.
- **Por subagentes (196):** archivos fundidos o retirados, líneas editadas después, contextos con fecha o con «antes», y rangos. Resultado:
  - 156 convertidas.
  - 38 históricas conservadas.
  - 2 ambiguas.
  - Fundidos: `Cap. N (archivo Y; antes archivo X)`, con el lugar donde vive hoy el contenido comprobado en la prosa.
  - Retirados sin destino: `*Título* (archivo X, retirado)`.

Registro íntegro: [[98_Agent_Handoff/sessions/2026-11-10_claude_referencias_56_a_47.csv]].

Además:

- [[01_Timeline/09_Equivalencias_Numeracion_Libro_I]] gana la columna **47 (2026-11-08)**, con los fundidos y retirados, y declara vigente la numeración de 47.
- Los diez documentos con nota «Numeración del 2026-11-01» llevan una segunda nota debajo. Dice que las referencias `Cap. N (archivo X)` ya están en 47, y que las históricas y los números sin archivo conservan su época.

**Quedan en 56, a propósito:** unas 40 referencias dentro de pasajes declarados históricos. Por ejemplo, el cuerpo de [[11_Books/Book_01_Mascaras_De_Cristal/Part_03_Ardizzone/00_Plan_Cierre_Parte_III]], que su nota NUEVO CAUCE declara historial, y las anclas «Cap. 32 (archivo 28)» de las cabeceras de las fichas de voz de Kal y Chiara. Los números sueltos, sin archivo, no se tocaron.

## Ambiguas (2)

- [[01_Timeline/02_Libro_01_Mascaras_De_Cristal]], línea ~189: bloque «ESCRITO (2026-09-20)» sobre *Cuatro letras*. No está claro si es histórico o vivo; si es vivo, sería el Cap. 35 (archivo 38) o el 34.
- [[02_Characters/Lucia_Varek]], línea 43: el interrogatorio de Lucía sobre el Peugeot rojo, «Cap. 14 (archivo 13), *Auster*». En el Cap. 13 Kal solo la describe. Candidatos: el Cap. 15 (Lucía ante Chiara) o el 17 (el Peugeot).

## Para el autor: afirmaciones que el nuevo cauce volvió falsas

La referencia ya apunta bien, pero la frase de la ficha describe algo que la prosa ya no hace. No se reescribió ninguna; son candidatas a una pasada de contenido.

- **Vento muere en el corral (Cap. 23):**
  - [[06_Relationships/Hitos]] todavía lo sitúa a mediados de octubre, «más de un mes antes» del cumpleaños, y vivo en el 24c.
  - [[02_Characters/Chiara_Bellandi]] y [[13_Auditorias/Book_01_Mascaras_De_Cristal/Carretera_Libro_I]] sitúan su sacrificio en *La mano* (33b, retirado).
- **La Parte I cierra con *Grazie* (19):** [[06_Relationships/Hitos]] sigue diciendo que cierra *El primer huésped*.
- ***Bajo juramento* (24, retirado):**
  - [[02_Characters/Garrett_Cross]]: el «No» ante el Lancia ya no está en la prosa.
  - [[02_Characters/Rocco]]: tampoco está la siembra de la manta de Russ.
  - [[13_Auditorias/Book_01_Mascaras_De_Cristal/Carretera_Libro_I]]: faltan «Tommaso, no.», «Lo cobro ahora» y la videollamada.
  - La fila de [[01_Timeline/08_Matriz_Renombramiento_Capitulos_Libro_I]] todavía dice «CANON / FUERTE, Conservar».
- ***Lleve equipaje* (27) y *No hace falta* (28), retirados:**
  - [[02_Characters/Warren_Halbrook]]: Halbrook ya no convoca a Kal en escena. El mensaje está en el 26, los golpes en el 27 y el relato en el 28.
  - Las «Muestras» de [[12_Craft_Policies/voice/Chiara_Bellandi]] y [[12_Craft_Policies/voice/Kal_Mercer]] anclan en líneas que ya no existen.
  - [[06_Relationships/Hitos]] describe la lectura de «Me encuentro bien», que no aparece en el 26.
- **Fechas y detalles movidos:**
  - [[02_Characters/Dario_Varek]]: la ventana del 36 es el diecinueve, no el catorce.
  - [[12_Craft_Policies/voice/Hector_Navarro]]: el monólogo del 24 lo «medio oye» Chiara, ya no se lo dice dormida.
  - [[02_Characters/Lucia_Varek]]: el interrogatorio se cuenta en el 13, ya no hay diálogo directo.
- **Carretera:** [[13_Auditorias/Book_01_Mascaras_De_Cristal/Carretera_Libro_I]] queda mixta: las referencias con archivo están en 47, y las notas cruzadas sin archivo, como «Blake cierra en el 47», siguen en 56.
