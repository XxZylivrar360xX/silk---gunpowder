# 2026-10-29 — Corte Parte I → Parte II movido al Cap. 25

**Agente:** Claude Code (principal). **Origen:** informe de ChatGPT [[98_Agent_Handoff/ChatGPT/2026-10-29_informe_resena_parte_I_oportunidades_lectura]] (OP-06, longitud de la Parte I). **Decisión:** autor, opción B.

## Cambio

- Parte I — *Dos mundos* = Caps. 1–25 (archivos 01–21, con 12b). Cierra en *El primer huésped*, «—Volvemos adentro».
- Parte II — *Con peores personas he tratado* = Caps. 26–43 (archivos 22a–34, con 24b, 24c, 24d, 33b). Abre con *La cifra*.
- Parte III sin cambios (44–60). La numeración corrida no cambia; no se tocó prosa.
- Proporción de prosa (sin notas): I 96.4k / II 62.8k / III 62.5k palabras (43/28/28 %; antes 57/15/28).

## Razón

El corte de 2026-08-29 ("antes de H5") ya no se cumplía: *Oveja entre lobos* (Cap. 31) abre H5 dentro de la Parte I, y el bloque 26–33 (robo, Hoover, *Lo que cueste*, ataque, rescate, *Libros abiertos*) hace la función de la Parte II. El bloque 30–33 que el informe pide no separar pasa entero.

## Verificación del cierre

- *Lo pequeño* (Cap. 24) no puede cerrar la parte: el 25 ocurre la misma madrugada.
- *El primer huésped* sí aguanta. Responde la pregunta de la Parte I (Kal se duerme con alguien despierto al lado sin vigilar), Chiara entra en la familia de Kal, la manzana sube en el refrigerador y la puerta se cierra con los dos dentro. *La cifra* abre «días después», en medio del robo.
- Riesgo menor: el cierre no deja amenaza explícita; las deudas abiertas (Hoover sembrado en el 23, Walt) bastan como tensión diferida.

## Mecánica

- `git mv` de 22a, 22b, 23, 24, 24b, 24c, 24d, 25 y `00_Plan_Robo_Monarch` a `Part_02_Con_Peores_Personas_He_Tratado`; enlaces reescritos en 89 archivos (incluidos los históricos; sólo cambia la ruta).
- Notas de corte en los comentarios de 21, 22a–25 y 26–31; los ordinales viejos quedan como históricos.
- Actualizados: [[11_Books/Book_01_Mascaras_De_Cristal/00_Book_Map]] (encabezado, Estructura, Umbral A), [[06_Relationships/Hitos]] (marca de corte), [[03_Factions/Villani_Motors]], brief.
- EPUB, PDF y audiolibro toman las partes de las carpetas: el título de la Parte II se anuncia ahora en *La cifra*. El EPUB no se regeneró.

## Pendiente

- Regenerar el EPUB y el PDF cuando el autor lo pida.
- Resto del informe (OP-01 a OP-05 y OP-07 a OP-10): sin decisión del autor.
