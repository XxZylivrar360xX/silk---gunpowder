# 2026-11-08 - Codex para Claude - Renumeracion de la Parte II

## Resultado

Encargo ejecutado en su alcance mecanico: 13 encabezados y notas de renumeracion, Caps. 20-32 sin huecos ni repetidos; nombres de archivo y prosa intactos (comparacion contra el estado inicial, excluyendo comentario y numero del encabezado). Book_Map actualizado; CHAPTER_STATUS contiene los 13 BORRADOR con fecha 2026-11-08, POV y conteos aproximados de las notas, y cuatro RETIRADOS. README de eliminadas: 17 filas nuevas (13 versiones, incluidas las tres del 2026-11-07, y cuatro retiros).

## Archivos tocados

- [[01_Timeline/08_Matriz_Renombramiento_Capitulos_Libro_I]]
- [[02_Characters/Edward_Connors]]
- [[02_Characters/Garrett_Cross]]
- [[02_Characters/Rocco]]
- [[02_Characters/Warren_Halbrook]]
- [[03_Factions/Villani_Motors]]
- [[06_Relationships/Hitos]]
- [[11_Books/Book_01_Mascaras_De_Cristal/00_Book_Map]]
- [[11_Books/Book_01_Mascaras_De_Cristal/Escenas_Eliminadas/README]]
- [[11_Books/Book_01_Mascaras_De_Cristal/Part_02_Con_Peores_Personas_He_Tratado/22a_La_Cifra]]
- [[11_Books/Book_01_Mascaras_De_Cristal/Part_02_Con_Peores_Personas_He_Tratado/22b_Con_Su_Proveedor]]
- [[11_Books/Book_01_Mascaras_De_Cristal/Part_02_Con_Peores_Personas_He_Tratado/24b_Lo_Que_Cueste]]
- [[11_Books/Book_01_Mascaras_De_Cristal/Part_02_Con_Peores_Personas_He_Tratado/24c_El_Corral]]
- [[11_Books/Book_01_Mascaras_De_Cristal/Part_02_Con_Peores_Personas_He_Tratado/24d_Vienes_Conmigo]]
- [[11_Books/Book_01_Mascaras_De_Cristal/Part_02_Con_Peores_Personas_He_Tratado/25_Libros_Abiertos]]
- [[11_Books/Book_01_Mascaras_De_Cristal/Part_02_Con_Peores_Personas_He_Tratado/26_Me_Encuentro_Bien]]
- [[11_Books/Book_01_Mascaras_De_Cristal/Part_02_Con_Peores_Personas_He_Tratado/29_El_Patio_Ajeno]]
- [[11_Books/Book_01_Mascaras_De_Cristal/Part_02_Con_Peores_Personas_He_Tratado/30_Media_Baraja]]
- [[11_Books/Book_01_Mascaras_De_Cristal/Part_02_Con_Peores_Personas_He_Tratado/31_Vamos_A_Casa]]
- [[11_Books/Book_01_Mascaras_De_Cristal/Part_02_Con_Peores_Personas_He_Tratado/32_Linea_Directa]]
- [[11_Books/Book_01_Mascaras_De_Cristal/Part_02_Con_Peores_Personas_He_Tratado/33_Mas_De_La_Cuenta]]
- [[11_Books/Book_01_Mascaras_De_Cristal/Part_02_Con_Peores_Personas_He_Tratado/34_Mi_Pareja]]
- [[12_Craft_Policies/CHAPTER_STATUS]]
- `tools/audiolibro/bitacora/Mascaras_De_Cristal.md` y `.json` (generados por --estado).

## Enlaces corregidos

- `01_Timeline/08_Matriz_Renombramiento_Capitulos_Libro_I.md`: `28_La_Correa` -> copia `_Version_2026-11-08` (1 enlaces).
- `02_Characters/Warren_Halbrook.md`: `27_Riesgo_Pendiente` -> copia `_Version_2026-11-08` (1 enlaces).
- `02_Characters/Garrett_Cross.md`: `24_Bajo_Juramento` -> copia `_Version_2026-11-08` (1 enlaces).
- `02_Characters/Edward_Connors.md`: `24_Bajo_Juramento` -> copia `_Version_2026-11-08` (1 enlaces).
- `02_Characters/Rocco.md`: `24_Bajo_Juramento` -> copia `_Version_2026-11-08` (1 enlaces).
- `03_Factions/Villani_Motors.md`: `24_Bajo_Juramento` -> copia `_Version_2026-11-08` (1 enlaces).
- `06_Relationships/Hitos.md`: `27_Riesgo_Pendiente` -> copia `_Version_2026-11-08` (2 enlaces).
- `06_Relationships/Hitos.md`: `28_La_Correa` -> copia `_Version_2026-11-08` (4 enlaces).
- `11_Books/Book_01_Mascaras_De_Cristal/00_Book_Map.md`: `24_Bajo_Juramento` -> copia `_Version_2026-11-08` (1 enlaces).
- `11_Books/Book_01_Mascaras_De_Cristal/00_Book_Map.md`: `27_Riesgo_Pendiente` -> copia `_Version_2026-11-08` (1 enlaces).
- `11_Books/Book_01_Mascaras_De_Cristal/00_Book_Map.md`: `28_La_Correa` -> copia `_Version_2026-11-08` (1 enlaces).
- `11_Books/Book_01_Mascaras_De_Cristal/00_Book_Map.md`: `33b_La_Mano` -> copia `_Version_2026-11-08` (1 enlaces).

Tambien las cuatro filas retiradas de CHAPTER_STATUS apuntan a sus copias. En Hitos se verifico que solo cambiaron seis rutas; texto y alias intactos.

## Audio y verificacion

`python -B ./tools/audiolibro/build_audiobook.py --estado`: salida correcta, 29 sin audio al dia; bitacora: 17 de 46 al dia. Parte II: 20-32, todos SIN AUDIO tras el cambio de numeracion. No aparecen los cuatro archivos retirados entre los capitulos activos. No hay numeros repetidos con Parte III; desaparecieron las colisiones 35 y 39. Sin red ni generacion de audio. `rg` confirma encabezados 20-32. CHAPTER_STATUS: 13 filas activas y cuatro retiros verificados.

## Pendientes y limites

- Parte III NO esta completamente renumerada: archivo 35 = Cap. 40; 36 = 34; 37 es marcador; 38 = 35; 39 es marcador; 40-43 = 36-39; 44-50b = 49-56. No se toco. Faltan 33 y 40-47 del cauce en su lugar definitivo; el mapa conserva las filas antiguas de esa Parte.
- El barrido no puede certificar cero enlaces antiguos fuera de carpetas exentas: el propio encargo prohibe tocar voice/ y revelations/, y preservar notas fechadas de planes y sesiones. Se conservaron estas referencias y se entregan para Claude:
  - `99_Reference/Conversacion_Kyle_Giulia_Regreso.md`: `28_La_Correa`.
  - `13_Auditorias/Book_01_Mascaras_De_Cristal/Audit_Dialogo_Kal_Chiara_Parte_I.md`: `28_La_Correa`.
  - `11_Books/Book_01_Mascaras_De_Cristal/00_Plan_Vento.md`: `33b_La_Mano`.
  - `98_Agent_Handoff/ChatGPT/2026-10-28_lectura_cap22_lo_que_nadie_estaba_mirando.md`: `24_Bajo_Juramento`.
  - `98_Agent_Handoff/ChatGPT/2026-10-28_lectura_cap27_nada_caro_cierre_editorial.md`: `24_Bajo_Juramento`.
  - `98_Agent_Handoff/ChatGPT/2026-10-28_lectura_cap28_bajo_juramento_mecanica_judicial.md`: `24_Bajo_Juramento`.
  - `98_Agent_Handoff/ChatGPT/2026-10-28_lectura_cap29_lo_que_cueste_microcirugia.md`: `24_Bajo_Juramento`.
  - `98_Agent_Handoff/ChatGPT/2026-10-29_informe_resena_parte_I_oportunidades_lectura.md`: `24_Bajo_Juramento`.
  - `98_Agent_Handoff/encargos/ENCARGO_Codex_Bajo_Juramento_Mecanica.md`: `24_Bajo_Juramento`.
  - `12_Craft_Policies/voice/Kal_Mercer.md`: `28_La_Correa`.
  - `12_Craft_Policies/voice/Chiara_Bellandi.md`: `28_La_Correa`.
  - `12_Craft_Policies/revelations/Book_01_Mascaras_De_Cristal.md`: `24_Bajo_Juramento`.
- `git diff --check` detecta dos espacios finales preexistentes (salto Markdown) en Edward_Connors, linea 10 ahora modificada por la ruta; se conservaron para respetar el cambio exclusivo de enlace.
- Habia cambios de otras sesiones al iniciar; no se revirtieron. No se tocaron CURRENT_BRIEF, PENDING, DECISIONS, log ni INDEX. Sin EPUB, PDF, commit ni push.
