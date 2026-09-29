#!/usr/bin/env python3
"""Build a reading PDF from the Book I manuscript using Pandoc and Typst."""

from __future__ import annotations

import argparse
import importlib.util
import io
import json
import shutil
import subprocess
import sys
from contextlib import redirect_stdout
from datetime import date
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parents[2]
EPUB_BUILDER = VAULT_ROOT / "tools" / "epub-build" / "build_epub.py"
OUTPUT_DIR = VAULT_ROOT / "output" / "pdf"
TEMP_DIR = VAULT_ROOT / "tmp" / "pdfs"

def typst_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def build_credits_typst(builder, title: str, author: str, year: str) -> str:
    """Render the EPUB builder's existing credits copy as Typst content."""
    blocks = builder.build_credits_page(title, author, year).strip().split("\n\n")
    paragraphs = [block.strip() for block in blocks[3:]]
    credits_title = "Créditos"
    copyright_line = blocks[2].strip()
    legal = "\n#parbreak()\n".join(
        f"#par(justify: true)[#text({typst_string(paragraph)})]"
        for paragraph in paragraphs
    )
    return (
        "#pagebreak()\n"
        "#align(center)[\n"
        f"  #text({typst_string(credits_title)}, size: 10pt, weight: \"bold\")\n"
        "  #v(1.2em)\n"
        f"  #text({typst_string(title)}, size: 18pt, style: \"italic\")\n"
        "  #v(1.5em)\n"
        f"  #text({typst_string(copyright_line)}, size: 9pt)\n"
        "]\n"
        "#v(2em)\n"
        f"{legal}\n"
        "#pagebreak()\n"
    )


def load_epub_builder():
    """Reuse the established manuscript collection and editorial safeguards."""
    spec = importlib.util.spec_from_file_location("epub_builder", EPUB_BUILDER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load manuscript builder: {EPUB_BUILDER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--book", default="11_Books/Book_01_Mascaras_De_Cristal",
        help="Book folder relative to the vault root.",
    )
    parser.add_argument("--title", default="Máscaras de Cristal")
    parser.add_argument("--author", default="Víctor Paz")
    parser.add_argument("--year", default=str(date.today().year))
    parser.add_argument("--output-name", default="Mascaras_De_Cristal")
    parser.add_argument("--paper", default="a5", help="Pandoc paper size (default: a5).")
    parser.add_argument("--draft-label", default="Borrador de lectura")
    args = parser.parse_args()
    if Path(args.output_name).name != args.output_name or args.output_name in {".", ".."}:
        print("Error: --output-name debe ser un nombre de archivo simple.", file=sys.stderr)
        return 2

    pandoc = shutil.which("pandoc")
    engine = shutil.which("typst")
    if not pandoc:
        print("Error: Pandoc no está instalado o no está en PATH.", file=sys.stderr)
        return 2
    if not engine:
        print(
            "Error: no se encuentra el motor PDF 'typst' en PATH. "
            "Instálalo y vuelve a ejecutar el generador.",
            file=sys.stderr,
        )
        return 2

    builder = load_epub_builder()
    book_dir = (VAULT_ROOT / args.book).resolve()
    if not book_dir.is_relative_to(VAULT_ROOT):
        print("Error: --book debe apuntar a una carpeta dentro del vault.", file=sys.stderr)
        return 2

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    TEMP_DIR.mkdir(parents=True, exist_ok=True)
    manuscript_path = TEMP_DIR / f"{args.output_name}.manuscript.md"
    credits_path = TEMP_DIR / f"{args.output_name}.credits.md"
    layout_path = TEMP_DIR / f"{args.output_name}.layout.typ"
    output_path = OUTPUT_DIR / f"{args.output_name}.pdf"
    manuscript = builder.build_frontmatter(
        args.title, args.draft_label, args.author, "es", args.year,
        "Seda y Pólvora", "1",
    )
    header, body = manuscript.split("\n---\n", maxsplit=1)
    manuscript = (
        header
        + "\nmargin:\n"
        + "  top: 18mm\n  bottom: 18mm\n  left: 19mm\n  right: 19mm"
        + "\n---\n"
        + body
    )
    collector_log = io.StringIO()
    with redirect_stdout(collector_log):
        manuscript += builder.collect_manuscript(book_dir, include_front_matter=False)
    collector_lines = collector_log.getvalue().splitlines()
    chapter_count = sum(line.startswith("  + ") for line in collector_lines)
    excluded_count = sum(line.startswith("  - excluded") for line in collector_lines)
    part_count = sum(line.startswith("[Part_") for line in collector_lines)
    print(
        f"Manuscrito reunido: {chapter_count} archivos en {part_count} partes; "
        f"{excluded_count} notas internas excluidas."
    )
    credits = build_credits_typst(builder, args.title, args.author, args.year)
    layout = (
        "#show heading.where(level: 1): it => {\n"
        "  set text(hyphenate: false)\n"
        "  pagebreak(weak: true)\n"
        "  it\n"
        "}\n"
    )

    try:
        manuscript_path.write_text(manuscript, encoding="utf-8")
        credits_path.write_text(credits, encoding="utf-8")
        layout_path.write_text(layout, encoding="utf-8")
        command = [
            pandoc,
            str(manuscript_path),
            "--standalone",
            f"--include-before-body={credits_path}",
            f"--include-in-header={layout_path}",
            "--toc",
            "--toc-depth=1",
            "--pdf-engine=typst",
            "-V", f"papersize={args.paper}",
            "-V", "fontsize=11pt",
            "-V", "linestretch=1.2",
            "-V", "page-numbering=1",
            "-V", "lang=es",
            "-o", str(output_path),
        ]
        print(f"Generando {output_path.relative_to(VAULT_ROOT)} ...")
        subprocess.run(command, check=True, cwd=VAULT_ROOT)
    except subprocess.CalledProcessError as exc:
        print(f"Error: Pandoc terminó con código {exc.returncode}.", file=sys.stderr)
        return exc.returncode or 1
    finally:
        manuscript_path.unlink(missing_ok=True)
        credits_path.unlink(missing_ok=True)
        layout_path.unlink(missing_ok=True)

    print(f"PDF listo: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
