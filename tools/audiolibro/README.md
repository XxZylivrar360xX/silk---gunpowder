# Audiolibro

Genera un MP3 por capitulo con voz neuronal de Microsoft (por defecto `es-MX-DaliaNeural`, elegida por el autor el 2026-10-23). Toma los capitulos igual que el EPUB: mismo orden, mismos `EPUB: EXCLUDE` y misma barrera contra marcas internas.

```powershell
python -m pip install --user edge-tts truststore   # una sola vez
python -B .\tools\audiolibro\build_audiobook.py                 # libro completo
python -B .\tools\audiolibro\build_audiobook.py --capitulo 11   # repetible
```

Salida: `output/audiolibro/Mascaras_De_Cristal/NN - Titulo.mp3` (ignorada por git; Google Drive la sincroniza, asi que se puede oir desde la app de Drive). Cada archivo abre con «Capitulo N. Titulo.»; el primero de cada parte anuncia la parte.

- **Regeneracion incremental:** `manifest.json` guarda un hash del texto hablado, la voz y la velocidad. Sin `--forzar`, solo se regeneran los capitulos cuyo texto cambio (incluye cambios de numeracion o del diccionario que les afecten). Un capitulo renumerado borra su MP3 anterior.
- **Pronunciacion:** `pronunciaciones.txt` reescribe nombres y frases en italiano o ingles con ortografia espanola (`Chiara = Kiara`). Solo cambia lo que se manda a la voz; el manuscrito no se toca. `--probar-diccionario` genera `00 - Prueba de diccionario.mp3`, que lee cada entrada.
- **Etiquetas y portada:** cada MP3 nuevo lleva titulo (`Capitulo N — Titulo`), album (titulo del libro), subtitulo (`Seda y Pólvora · Libro I`), autor, pista `N/total`, genero Audiolibro y la portada de `99_Reference/book_covers/` reducida a 800 px. `--etiquetar` las reescribe en los MP3 existentes sin red ni audio (p. ej. tras cambiar una portada o el diccionario `BOOKS` del script). Requiere `python -m pip install --user mutagen pillow`.
- **Otras opciones:** `--voz` (p. ej. `es-MX-JorgeNeural`), `--velocidad -10%`, `--solo-texto` (escribe el `.txt` que se leeria, sin audio), `--book Book_02_Sombras_De_Poder`.
- **Red:** el texto se envia al servicio de Microsoft. En esta laptop, Python no valida el certificado con el bundle de `certifi`; `truststore` usa el almacen de Windows. Cada capitulo reintenta dos veces si falla la red.
- Escala: el Libro I son unas 194 mil palabras, ~21 h de audio, ~3 h de generacion y ~480 MB.
- **Bitacora (trazabilidad):** cada corrida reescribe `bitacora/Mascaras_De_Cristal.md` (y su `.json` de estado), ambos en git: capitulos AL DIA, PENDIENTE (con motivo: prosa, o numeracion/diccionario/voz) o SIN AUDIO, y un historial de cada cambio de estado. Tras editar prosa, `--estado` refresca la bitacora sin red ni audio; la bandera se cierra sola al regenerar ese capitulo. No editarla a mano.
