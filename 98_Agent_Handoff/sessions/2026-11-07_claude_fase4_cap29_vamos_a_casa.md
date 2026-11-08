# Sesión 2026-11-07: Fase 4, nuevo Cap. 29 *Vamos a casa* (terminal B)

**Agente:** Claude Code (Opus 5.5), terminal B, según [[98_Agent_Handoff/encargos/ENCARGO_Fase4_Paralelo_Reusa]]. El autor lee al terminar los cuatro capítulos del reparto.

**Qué se hizo:** el archivo 31, *Vamos a casa*, queda como nuevo Cap. 29 (T16, H7, POV Chiara, «Reusa y unifica el POV»). Fue una cirugía (skill `editorial-surgery`, modo SURGERY), no una reescritura. El capítulo ya estaba casi entero en POV Chiara. El «mixto» del Mapa de POV venía de seis deslices al interior de Kal. Prosa: ~4,667 → ~4,674 palabras (sin metadata). Estado: BORRADOR; los cambios son DISEÑO. Versión anterior íntegra: [[11_Books/Book_01_Mascaras_De_Cristal/Escenas_Eliminadas/31_Vamos_A_Casa_Version_2026-11-07]] (git `3d26627`).

**Decisiones del autor (CANON, 2026-11-07):**
- Reusa mínimo: sin poda y sin meta de palabras. La regla 06 no se dispara: todas las paradas pasan dentro de una sola espera, y el cementerio cambia lo que Chiara sabe de Kal.
- El «Bellandi.» de Harper se queda. El canon de Tommaso dice cómo la llama él, no lo prohíbe a otros.
- La línea de Varek pasa a «el día anterior» y no cobra la deuda (el H7 no habla de Varek).

**DISEÑO del agente (before → after):**
1. «Para cuando Kal se cansó de esperar en el estacionamiento y subió…» → «Para cuando Kal subió al penthouse sin que nadie tuviera que abrirle, cansado de esperar en el estacionamiento…». Lo que antes era interior de Kal ahora es lo que Chiara infiere.
2. «Kal frunció el ceño un segundo antes de que el nombre completo le cayera encima.» → «…un segundo, y después se le vio en la cara que el nombre completo le había caído encima.»
3. «…sin ninguna intención de darle esa satisfacción completa.» → «La miró de reojo y no le dio la satisfacción completa.» La intención de Kal pasa a ser conducta.
4. «Algo le tiró del costado al hacerlo — las costillas…—. Chiara lo sintió en el brazo…» → «Chiara sintió en el brazo que la sostenía que algo le tiraba del costado —las costillas…—, y en la cara de él no se vio nada.» De paso se corrige la raya con espacio.
5. «Kal también se dio cuenta.» → «Vio que Kal también se había dado cuenta.»
6. «Había negociado con Dario Varek esa misma mañana.» → «Un día antes le había sostenido la mirada a Dario Varek.»

**Lo que protegí:** «Kal se rió. No de ella. Con ella…» (la lectura es de Chiara); el «francés torcido que sólo le salía cuando estaba orgulloso» (lo sabe ella); «Kal tuvo la prudencia de no sonreír» (se ve desde fuera); «Sabía sentarse a negociar con Dario Varek» (es general y sigue siendo verdad en el cauce); el «Walt, probablemente» de la luz del porche (es una conjetura de ella). Todas las líneas de diálogo y las de CANON quedan literales. El ganador de la pesca sigue PENDIENTE.

**Autocrítica:**
- **El cambio que más dudas da** es el 2: «se le vio en la cara» es un poco más pesado que el original.
- **El más agresivo** es el 6, porque cambia el sentido: «negociar» pasa a «sostenerle la mirada». La elección es tuya, pero la formulación es mía.
- **No hay riesgo de esterilizar la voz:** no toqué ninguna rareza de voz ni ningún diálogo.

**Para propagar (lo hace la terminal principal):**
- `12_Craft_Policies/CHAPTER_STATUS.md`: archivo 31 = nuevo Cap. 29, BORRADOR, ajustado el 2026-11-07 (nuevo cauce), POV Chiara único.
- `11_Books/Book_01_Mascaras_De_Cristal/00_Book_Map.md`: el 31 pasa a ser el nuevo 29. Al renumerar, el encabezado «Capítulo 35» pasa a «Capítulo 29».
- `13_Auditorias/Book_01_Mascaras_De_Cristal/Mapa_POV_Libro_I.md`: la fila 35 (archivo 31) pasa de mixto a 100 % Chiara.
- `11_Books/Book_01_Mascaras_De_Cristal/Escenas_Eliminadas/README.md`: añadir la fila de la copia `31_Vamos_A_Casa_Version_2026-11-07`, si se registran ahí las copias de la Fase 4. No lo toqué.
- Para quien escriba el **nuevo 25** (archivo 25, POV Chiara): el cementerio del 29 cobra «Y decirle que Marisol está bien. Que ya lo lloré.». Hay que conservarla. Hoy la tercera hilera y el ciprés (archivo 25, línea 356) son interior de Kal; en POV Chiara se pierde que él evitaba esa hilera, y el 29 sigue funcionando sin eso.
- Para quien escriba el **nuevo 26/27** (archivo 28): «No era una orden. / Sonó como una.» tiene su eco en la coda del sillón. Hay que conservarla en el capítulo que se quede con esa escena.
- Para quien escriba el **nuevo 28** (archivo 30, sin coda de Kal): la reunión de El Patio sale de página. El 29 la da por ocurrida («¿Cómo se lo tomó Nadir?», Camp Alder, «Idea de Nadir»), y Chiara tiene que haber oído «Camp Alder» en Las Gemelas (hoy lo oye, línea 122).
- `98_Agent_Handoff/CURRENT_BRIEF.md` y `PENDING.md`: añadir el nuevo 29 a «Lecturas del autor».
- `log.md`: enlace a esta nota.

**Costuras provisionales:**
- Apertura («esa mañana había estado sentada sobre una piedra escuchando el nombre de un general»): depende del nuevo 28.
- Cementerio: depende del nuevo 25.
- Sillón: depende del nuevo 26 o 27.
- El cierre no engancha con el nuevo 30 (T17, POV Kal).

**Fuera de mi reparto (sólo anoto):**
- *Tierra buena* está en `Escenas_Eliminadas/`, así que «la parcela» y la cita plantada de Harper ya no tienen presentación. Para el lector, Harper es la barista del Cap. 4 y ahora tiene una relación de trabajo con Kal que nadie explica. Funciona como misterio leve, pero conviene decidirlo.
- La metadata del 31 dice que Walt «cobra su línea del Cap. 27 (quería verlo con sus propios ojos)». `rg` ya no la encuentra en ningún capítulo, así que el cobro (una mirada) se queda sin siembra. Es inofensivo.
- La foto de Héctor se cobra en «la apertura del Cap. 33 (el cuadro con moño)» y en el Cap. 50, en numeraciones viejas. Hay que verificar el destino en el cauce de 47.
- La Beretta .25 aparece por primera vez aquí (vestidor). Si el nuevo cauce la muestra antes, hay que ajustar.

**Audio PENDIENTE:** archivo 31. No corrí `--estado` porque escribe la bitácora compartida.
