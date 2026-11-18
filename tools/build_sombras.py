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
COVER = "99_Reference/book_covers/Sombras_De_Poder_Vela_v1.png"

# Los 58 capítulos en orden (los sin redactar son placeholders; ver 00_Book_Map).
# El orden de esta lista manda en la copia de lectura.
# Las rutas son relativas a BOOK; el recolector conserva el orden de carpetas/archivos.
CHAPTERS = (
    "Part_01_Territorio_Ajeno/01_Hogar.md",
    "Part_01_Territorio_Ajeno/02_Con_Su_Letra.md",
    "Part_01_Territorio_Ajeno/03_Bellandi.md",
    "Part_01_Territorio_Ajeno/04_El_Barrio_Ajeno.md",
    "Part_01_Territorio_Ajeno/05_La_Almendra.md",
    "Part_01_Territorio_Ajeno/06_La_Primera_Cuota.md",
    "Part_01_Territorio_Ajeno/07_El_Farol.md",
    "Part_01_Territorio_Ajeno/08_La_Lluvia.md",
    "Part_01_Territorio_Ajeno/09_El_Error_De_Tyler.md",
    "Part_01_Territorio_Ajeno/10_Fuga_De_Gas.md",
    "Part_01_Territorio_Ajeno/11_Capacidad.md",
    "Part_01_Territorio_Ajeno/12_Queremos_Esta.md",
    "Part_01_Territorio_Ajeno/13_Encubierto.md",
    "Part_01_Territorio_Ajeno/14_Senor_Militar.md",
    "Part_01_Territorio_Ajeno/15_Lentejuelas.md",
    "Part_01_Territorio_Ajeno/16_El_Otro_Dario.md",
    "Part_01_Territorio_Ajeno/17_El_Benefactor.md",
    "Part_02_Nieve_Y_Ceniza/18_Veintitres_De_Noviembre.md",
    "Part_02_Nieve_Y_Ceniza/19_No_Cargues_Sola.md",
    "Part_02_Nieve_Y_Ceniza/20a_Una_Noche_De_Mudanza.md",
    "Part_02_Nieve_Y_Ceniza/20b_El_Collar.md",
    "Part_02_Nieve_Y_Ceniza/21_Ano_Nuevo.md",
    "Part_02_Nieve_Y_Ceniza/22_La_Carretera.md",
    "Part_02_Nieve_Y_Ceniza/23_La_Vela_Tardia.md",
    "Part_02_Nieve_Y_Ceniza/24_La_Jaula.md",
    "Part_02_Nieve_Y_Ceniza/25_Deseame_Suerte.md",
    "Part_02_Nieve_Y_Ceniza/26_Lussia.md",
    "Part_02_Nieve_Y_Ceniza/27_Sin_Publico.md",
    "Part_02_Nieve_Y_Ceniza/28_El_Millon.md",
    "Part_02_Nieve_Y_Ceniza/29_Nadie_Tiene_Prisa.md",
    "Part_02_Nieve_Y_Ceniza/30_Calle_Corona.md",
    "Part_02_Nieve_Y_Ceniza/31_El_Armario.md",
    "Part_03_Exilio/32_Vacio.md",
    "Part_03_Exilio/33_Escenarios.md",
    "Part_03_Exilio/34_El_Agua_Corriendo.md",
    "Part_03_Exilio/35_El_Baston.md",
    "Part_03_Exilio/36_Las_Latas.md",
    "Part_03_Exilio/37_Lo_Del_Hermano.md",
    "Part_03_Exilio/38_Perdoname_Jefe.md",
    "Part_03_Exilio/39_Lo_Que_Queda.md",
    "Part_03_Exilio/40_Una_Sola_Frase.md",
    "Part_04_Torna_A_Casa/41_Diez_Segundos.md",
    "Part_04_Torna_A_Casa/42_Yo_Respondo.md",
    "Part_04_Torna_A_Casa/43_Las_Bandas.md",
    "Part_04_Torna_A_Casa/44_Mover_La_Mirada.md",
    "Part_04_Torna_A_Casa/45_Lo_Poco_Que_Llegue_A_Saber.md",
    "Part_04_Torna_A_Casa/Stavanger.md",
    "Part_04_Torna_A_Casa/Henrik.md",
    "Part_04_Torna_A_Casa/Ya_Llego.md",
    "Part_04_Torna_A_Casa/49_Llegar_Tarde.md",
    "Part_04_Torna_A_Casa/50_Veintitres_De_Noviembre.md",
    "Part_04_Torna_A_Casa/51_La_Fecha.md",
    "Part_04_Torna_A_Casa/52_Santa_Lucia.md",
    "Part_04_Torna_A_Casa/53_Torna_A_Casa.md",
    "Part_04_Torna_A_Casa/54_Dime_Amore.md",
    "Part_04_Torna_A_Casa/55_De_Rodillas.md",
    "Part_04_Torna_A_Casa/56_No_Otra_Vez.md",
    "Part_04_Torna_A_Casa/57_La_Chimenea.md",
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
            options = ["--cover", COVER] + ([] if output_format == "epub" else ["--paper", args.paper])
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
