#!/usr/bin/env python3
"""Regenera EPUB y PDF de Sombras de Poder desde la selección de capítulos."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parents[1]
BOOK = "11_Books/Book_02_Sombras_De_Poder"
TITLE = "Sombras de Poder"
OUTPUT_NAME = "Sombras_De_Poder"
AUTHOR = "Víctor Paz"
SERIES = "Seda y Pólvora"
SERIES_POSITION = "2"
# Mantener fijo para conservar los marcadores del lector entre regeneraciones.
IDENTIFIER = "urn:uuid:2bbb6f80-be4e-478a-8ff2-4a7348319358"
COVER = "99_Reference/book_covers/Sombras_De_Poder_VICTOR_PAZ.png"

# Añadir aquí los capítulos que el autor incorpore a la copia de lectura.
# Las rutas son relativas a BOOK; el recolector conserva el orden de carpetas/archivos.
CHAPTERS = (
    "Part_01_Nieve_Y_Ceniza/01_Hogar.md",
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--format", choices=("both", "epub", "pdf"), default="both",
                        help="Formatos por regenerar (predeterminado: both).")
    parser.add_argument("--paper", default="a5", help="Tamaño del PDF (predeterminado: a5).")
    parser.add_argument("--year", default=str(date.today().year), help="Año de los créditos.")
    args = parser.parse_args()

    formats = ("epub", "pdf") if args.format == "both" else (args.format,)
    required = ["pandoc"] + (["typst"] if "pdf" in formats else [])
    for executable in required:
        if not shutil.which(executable):
            print(f"Error: no se encuentra {executable} en PATH.", file=sys.stderr)
            return 2
    for chapter in CHAPTERS:
        if not (VAULT_ROOT / BOOK / chapter).is_file():
            print(f"Error: falta el capítulo {chapter}.", file=sys.stderr)
            return 2
    if "epub" in formats and not (VAULT_ROOT / COVER).is_file():
        print(f"Error: falta la portada {COVER}.", file=sys.stderr)
        return 2

    common = [
        "--book", BOOK, "--title", TITLE, "--author", AUTHOR,
        "--output-name", OUTPUT_NAME, "--year", args.year,
        "--series", SERIES, "--series-position", SERIES_POSITION,
        "--identifier", IDENTIFIER,
    ]
    for chapter in CHAPTERS:
        common.extend(["--chapter", chapter])

    print(f"{TITLE}: {len(CHAPTERS)} capítulo(s) en la selección de lectura.", flush=True)
    try:
        for output_format in formats:
            builder = VAULT_ROOT / "tools" / f"{output_format}-build" / f"build_{output_format}.py"
            options = ["--cover", COVER] if output_format == "epub" else ["--paper", args.paper]
            subprocess.run(
                [sys.executable, "-B", str(builder), *common, *options],
                check=True, cwd=VAULT_ROOT,
            )
    except subprocess.CalledProcessError as exc:
        print(f"Error: la generación se detuvo con código {exc.returncode}.", file=sys.stderr)
        return exc.returncode or 1

    print("Regeneración terminada.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
