# 2026-10-11 — Codex -> Claude Code — Barrido de carpetas poco usadas

## Objetivo

Continuar la ronda de mantenimiento señalada en [[98_Agent_Handoff/PENDING]]: contrastar carpetas con pocos archivos contra su propósito, referencias y estado antes de sugerir cambios.

## Hallazgos

- **No conviene retirar scaffolding de `11_Books/`.** `Book_03`–`Book_07` contienen sólo su `00_Book_Map.md`, como prevé `11_Books/README.md` mientras no se aprueben los desgloses. `Book_02/Part_03_Torna_A_Casa/` contiene `.gitkeep` y también está prevista para el montaje futuro. La baja cantidad de archivos es intencional.
- **`13_Auditorias/Book_02_Sombras_De_Poder/` está en uso.** Su único archivo es una auditoría del Cap. 1; no hay base para tratar la carpeta como residuo.
- **Las carpetas pequeñas de `12_Craft_Policies/` tienen función y dependencias documentadas.** `milestones/INDEX.md`, `revelations/`, `tonal_calibration/` y las reglas se enlazan desde el README de políticas, mapas y fichas. No consolidar ni quitar por recuento.
- **`08_Scenes/Book_03/` sigue alojando dos materiales de escenas referenciados:** el borrador exploratorio de *Cuentas de Sangre* y el epílogo aprobado. `08_Scenes/README.md` explica que el nombre de la carpeta conserva una organización previa y que los mapas determinan el destino operativo; retenerla evita romper referencias vigentes.
- **Candidato que requiere reconciliación de Claude/autor:** `08_Scenes/Book_01/Stavanger_Ya_Llego_Material_Narrativo.md` es una versión de escena marcada no canónica, sin referencias entrantes encontradas en el barrido de Markdown operativo. Su metadata dice Libro I y su ventana temporal está marcada desactualizada; el encabezado registra la antigua ubicación previa a F2. La versión de trabajo actual está en `11_Books/Book_02_Sombras_De_Poder/Part_04_Torna_A_Casa/Ya_Llego.md`, cuyo estado y ubicación corresponden al Libro II. Recomiendo decidir si el archivo auxiliar debe marcarse como histórico/supersedido o conservarse con una nota clara de su relación con el manuscrito. No lo modifiqué: contiene prosa y referencias a decisiones autorales.
- `07_Ideas/Libro_01_Incubadora/` sigue enlazada desde el propio material y conserva registros de diseño; su nombre histórico no basta para retirarla.

## Verificación y alcance

- Revisé los README de `08_Scenes/`, `11_Books/`, `12_Craft_Policies/` y `99_Reference/`, el inventario recursivo de carpetas con cuatro archivos o menos y referencias Markdown a las rutas candidatas. No hice cambios de contenido ni moví archivos.
- `99_Reference/` se revisó sólo a nivel de catálogo; se respetó la regla de no usar su material externo para inferir canon.
- No recomiendo ajustes estructurales adicionales en esta ronda. El único seguimiento concreto es resolver el estatus de la escena antigua de Stavanger antes de que alguien la use como fuente.
