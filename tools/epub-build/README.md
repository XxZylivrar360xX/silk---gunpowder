# EPUB build

Generador local para el EPUB de *Seda y Polvora*.

```powershell
python .\tools\epub-build\build_epub.py
```

Salida esperada:

- `tools/epub-build/output/Seda_y_Polvora.epub`

Requiere `pandoc` disponible en PATH.

Notas:

- Cuando ya hay capitulos en `Part_*`, la nota editorial de `00_Front_Matter` se omite por defecto para que el EPUB lea como novela.
- Usa `--include-front-matter` si necesitas incluir esa nota de montaje.
