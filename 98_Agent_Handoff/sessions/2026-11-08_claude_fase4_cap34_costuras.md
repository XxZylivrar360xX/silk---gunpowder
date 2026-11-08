# 2026-11-08 · Claude Code · Fase 4: nuevo Cap. 34, costuras y retiro de *Cuatro letras*

Encargo: orden del autor (2026-11-08), con el método de [[98_Agent_Handoff/encargos/ENCARGO_Fase4_Paralelo_Reusa]]. El nuevo 34 (T21, H16, POV Chiara) **ya lo había redactado hoy la terminal B** en [[11_Books/Book_01_Mascaras_De_Cristal/Part_03_Ardizzone/36_Tambien_Las_Mananas]] ([[98_Agent_Handoff/sessions/2026-11-08_claude_fase4_cap34_tambien_las_mananas]]). Esta sesión no reescribe: hace microedición (skill `editorial-surgery`, modo SURGERY, ámbito de cinco ajustes aprobado por el autor) y retira el archivo 37.

## Qué se hizo

- **Revisión contra el canon del encargo:** cumple. El cumpleaños es el 23 nov; la llave (H16) llega antes de la carta; «¿Faltó más, verdad? Lo sabía.» está literal; la invitación de Kal se escribe sin que se vea el texto. En la prosa no aparecen el beso, «—Chiara», Bonnie, Mei-Lin, «Roma», la cocaína, Mabel ni Acción de Gracias, y tampoco Halbrook, un jefe de policía, la bala ni el pañuelo.
- **Microedición en el archivo 36** (la prosa sigue en unas 2,870 palabras, BORRADOR):
  1. «Las invitaciones llegaron en sobres…» → «Las invitaciones llegaron **el miércoles**, en sobres…». Fija la mañana de la cafetera el jueves 25.
  2. «a bordo, **este viernes**, en la costa» → «a bordo, **el viernes diez**, en la costa». El yate es el vie 10 dic (calendario A); «este viernes» habría sido el 26 nov.
  3. «Apoyó el sobre contra la cafetera, ~~todavía tibia,~~ con el nombre…». La imagen se repetía con la primera línea del 35, que la conserva.
  4. Encabezado: «Capítulo 41» → «Capítulo 34 — También las mañanas».
  5. Metadata: la costura con el 33 queda resuelta, la de cierre también, y sigue PROVISIONAL la dependencia de Las Gemelas (27/28).
- **Archivo 37, *Cuatro letras*:** copia íntegra en [[11_Books/Book_01_Mascaras_De_Cristal/Escenas_Eliminadas/37_Cuatro_Letras_Version_2026-11-08]] (byte a byte, verificada con `cmp`). El archivo queda como marcador `EPUB: EXCLUDE`, igual que el 39.

## Decisiones del autor (CANON, 2026-11-08)

1. Para el 34 se hace microedición sobre el borrador de B, no una reescritura.
2. El marcador EXCLUDE queda en el **archivo 37**. El capítulo sigue en el 36, con el título *También las mañanas*.
3. **Matteo se fue por Elio, no por el robo** (confirma el CANON 2026-11-07 de la nota del 37). **Contradice** lo que la nota del 33 marca como CANON («la salida ya la causa el robo»: Il Consorzio se entera, Volpi va por Elio). La prosa del 34 aguanta las dos versiones; la del 33 no la revisé.
## DISEÑO del agente

- El plato de Mabel no se rescata: sin Acción de Gracias queda suelto en POV Chiara. Es recomendación del agente y el autor no la confirmó.
- Sólo el miércoles 24 como día de las invitaciones y «el viernes diez» en el texto impreso. No toqué nada más de la prosa de B.

## Para propagar (lo hace la terminal principal)

- `CHAPTER_STATUS` y `00_Book_Map.md`: archivo 36 = nuevo Cap. 34, BORRADOR (Fase 4), unas 2,870 palabras. Archivo 37 = marcador EXCLUDE (fusionado en los nuevos 34 y 35).
- `Escenas_Eliminadas/README.md`: fila para `37_Cuatro_Letras_Version_2026-11-08` (y la de `36_…_2026-11-07` que pidió B).
- `00_Mapa_Cauce_Cap11_Camp_Alder.md`, «Avance de la Fase 4»: el nuevo 34 queda redactado y el 37 retirado.
- `DECISIONS.md` y `log.md`: la decisión 3. **Hay que corregir lo que la nota del 33 pide propagar** a `02_Characters/Matteo_Bellacorte.md`, `Nereo_Volpi.md`, `Elio_Bellacorte.md`, `00_Plan_Robo_Monarch.md` línea 47 y `revelations/`: la salida **no** la causa el robo.
- **Nuevo 33** (`35_Sin_Fecha_De_Regreso.md`): revisar que la intuición de Chiara («el cobro por las rutas») no diga en prosa que el robo es la causa. No lo leí y no lo edité.
- `06_Relationships/Hitos.md` §H16: las invitaciones salen el miércoles 24 y la carta queda contra la cafetera el jueves 25.
- **Nuevo 30** (`32_Linea_Directa`): la ferretería («el Tasador me subió la cuota», libreta de los fiados) sólo vive ahora en la versión archivada del 37. Hay que trasladarla al reconstruir el 30.
- `CURRENT_BRIEF.md` / `PENDING.md`: el nuevo 34 entra en «Lecturas del autor», con la nota de B como principal.
- `tools/audiolibro/bitacora/`: hay que correr `--estado`. El 37 sale del audiolibro.

## Costuras

- **Apertura:** con el nuevo 33, resuelta. Sigue PROVISIONAL con los nuevos 27/28 (Las Gemelas), porque todavía no se reconstruyen.
- **Cierre:** resuelta. El sobre queda contra la cafetera el jueves 25 y el 35 abre ahí con «todavía tibia».

## Verificación

- Se buscaron con grep las tres ediciones de prosa y el encabezado. «todavía tibia» ya no está en la prosa del 34. Los enlaces a `37_Cuatro_Letras` del vault resuelven al marcador.
- No se tocaron archivos compartidos, el 35 ni el 33, ni la bitácora de audio.

audio PENDIENTE: archivo 36 (el archivo 37 sale del audiolibro como marcador EXCLUDE)
