# 2026-11-01 — Claude: fusión del 05b como coda del 05a (Cap. 6 → Cap. 5)

**Agente:** Claude Code (`chapter-drafting` + `editorial-surgery` VERIFY). **Origen:** DECISIÓN DEL AUTOR 2026-11-01 en [[98_Agent_Handoff/sessions/2026-10-31_claude_carretera_libro_i#Fusión del 05b en el 05a (Cap. 6 → coda del 5): estudio y decisiones]] y fila V-1 de [[11_Books/Book_01_Mascaras_De_Cristal/Part_01_Dos_Mundos/00_Plan_Rediseno_Parte_I]].

## Resultado

- [[11_Books/Book_01_Mascaras_De_Cristal/Part_01_Dos_Mundos/05a_Cliente_Y_Proveedor]]: la prosa del 05b entra tras «No la acomodó.», separada con ***. Título intacto; 05c intacto («Unos días después de que la caseta dejara de pedirle nombre…» sigue funcionando: la caseta y V-1 van antes del beso del sábado, que cierra la coda). Línea nueva en el encabezado con primera línea, cortes y V-1. Estado heredado sin cambio.
- **Conteo (prosa, `wc -w`):** coda 2,502 (05b 2,863 con el mismo método); capítulo fusionado **5,854**. Quedó ~300 sobre la meta de ~2,200: lo que resta es casi todo lo que pediste conservar. Si quieres llegar a la meta, los candidatos son: «No hay contrato» de Tommaso en la rutina (~55), la grúa vacía del ventanal tras la cena (~34), la anécdota de la persecución de Blake (~45) y la entrada del valet (~40). No los toqué.
- **Primera línea nueva (DISEÑO):** «Los treinta días empezaron a correr, y después las semanas, mientras Plaza Corona iba saliendo de los noticieros…». Toma el «Treinta días» con que cierra la reunión.
- **Cortes:** detallados en el encabezado del 05a; texto literal en [[11_Books/Book_01_Mascaras_De_Cristal/Escenas_Eliminadas/README]] (fila 05b y sección «Texto podado del Cap. 6»). Revierte una protección: el párrafo del trapo vacío de la bisagra («y ése era el problema»), que `Audit_Cap_05_Una_Amiga` había conservado como DUDOSA; sale por reiteración, con tu autorización. Se mantuvieron N5-7 («las excepciones se acumulan…») y las líneas de la regla 05 (piquete del hombro, «Lo tengo anotado con día y hora», «Bellandi», «Chiara pasó junto a él», «Kal no preguntó desde cuándo»).
- **V-1 (DISEÑO):** «Dos días después, el correo interno le dejó en la bandeja un formato de alta de proveedores con un solo renglón marcado en amarillo: *nombre completo del responsable*. No traía firma. En la casilla del solicitante decía *Dirección*. / Chiara lo llenó con lo que venía en la licencia municipal y lo devolvió antes de la comida.» Decisión mía: Chiara contesta, y sin pausa. Contrasta con el segundo de cursor sobre su firma: no ve el ojo. No cita el nombre (no hay nombre completo de Kal en canon). Cobra en `29:47`.

## Verificación (`editorial-surgery`, VERIFY)

- No hay callbacks rotos: `rg` en `11_Books/` no encuentra cobros de ningún texto cortado. Se conservan «Usted es alta», «uno de botones» (`10:56`), «Bellandi», la caseta (`05c:13`, `22a:151`, `29:47`, `47:169`), «No es suyo», «Esta vez sí se rió» y «esta vez sí se bajó».
- Costuras corregidas: «—Y tiene que dejar…» → «—Usted tiene que dejar…» (al caer «Tengo que volver arriba»); «ella dijo» → «Chiara dijo» (al caer Matteo); «Ya sé. —Kal miró el carrito…—. Entonces pídamelo…» sustituye al segundo «¿Entonces?».
- Se perdió valor no informativo, evaluado: «Era verdad. / No toda.» y la conclusión de Chiara con la bisagra. Restaurables si los extrañas.
- Audio: corrí `build_audiobook.py --estado`. No se regeneraron EPUB ni PDF y no hubo commit.

## Fase B (Codex, sin tocar aquí)

`git rm` del 05b, enlaces, Book_Map, CHAPTER_STATUS, matriz, carretera §2, traslado del historial del encabezado del 05b y renumeración. Todo eso queda pendiente.

## Preguntas para el autor

1. ¿Apruebas la primera línea nueva y V-1 (que Chiara conteste sin pausa)?
2. ¿Te quedas con ~2,500 o podamos hasta ~2,200 con los candidatos de arriba?
3. ¿Restauro «Era verdad. / No toda.» o el trapo vacío de la bisagra?
