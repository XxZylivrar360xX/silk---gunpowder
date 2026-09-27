#!/usr/bin/env python3
"""
Build the Seda y Polvora EPUB from the active book folder.

The script is intentionally tolerant during early drafting:
- front matter in 00_Front_Matter is included first;
- prose chapters are collected from Part_* folders in filename order;
- Obsidian wikilinks are flattened for reader-facing output;
- if no chapters exist yet, the front matter still builds a valid starter EPUB.
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parents[2]
SCRIPT_DIR = Path(__file__).resolve().parent

WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)?(?:#[^\]|]+)?(?:\|([^\]]+))?\]\]")
HTML_COMMENT_RE = re.compile(r"<!--.*?-->\s*", re.DOTALL)
EPUB_EXCLUDE_MARKER = "EPUB: EXCLUDE"


def is_epub_excluded(raw_text: str) -> bool:
    """Files carrying this marker (e.g. redirect stubs) are kept in the vault
    but never incorporated into the exported EPUB."""
    return EPUB_EXCLUDE_MARKER in raw_text


def clean_wikilinks(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        target = match.group(1) or ""
        alias = match.group(2)
        if alias:
            return alias
        if not target:
            return ""
        return Path(target).name.replace("_", " ")

    return WIKILINK_RE.sub(repl, text)


def divider_title(folder_name: str) -> str:
    # Reader-facing capitalization for the current manuscript folders.
    aliases = {
        "Part_01_Dos_Mundos": "Part_01_Dos_Mundos",
        "Part_02_Con_Peores_Personas_He_Tratado": "Part_02_Con_peores_personas_he_tratado",
    }
    folder_name = aliases.get(folder_name, folder_name)
    parts = folder_name.split("_")
    if parts[0].lower() == "part" and len(parts) >= 3:
        roman = {"01": "I", "02": "II", "03": "III", "04": "IV", "05": "V", "06": "VI"}
        number = roman.get(parts[1], parts[1])
        title = " ".join(parts[2:]).replace(" Y ", " y ")
        return f"Parte {number} — {title} {{.part-title}}"
    if parts and parts[0].isdigit():
        parts = parts[1:]
    return " ".join(parts)


def strip_yaml_frontmatter(text: str) -> str:
    lines = text.splitlines()
    if lines and lines[0].strip() == "---":
        end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
        if end is not None:
            return "\n".join(lines[end + 1 :]).lstrip()
    return text


def format_markdown(text: str) -> str:
    text = strip_yaml_frontmatter(text)
    text = HTML_COMMENT_RE.sub("", text)
    text = clean_wikilinks(text)
    return text.strip() + "\n"


def read_markdown(path: Path) -> str:
    return format_markdown(path.read_text(encoding="utf-8-sig"))


def collect_folder(folder: Path, include_divider: bool) -> list[str]:
    files = sorted(p for p in folder.glob("*.md") if p.is_file())
    if not files:
        return []

    sections: list[str] = []
    for file_path in files:
        raw_text = file_path.read_text(encoding="utf-8-sig")
        if is_epub_excluded(raw_text):
            print(f"  - excluded from EPUB: {file_path.relative_to(VAULT_ROOT)}")
            continue
        print(f"  + {file_path.relative_to(VAULT_ROOT)}")
        sections.append(format_markdown(raw_text))

    if not sections:
        return []

    if include_divider:
        sections.insert(0, f"# {divider_title(folder.name)}\n")
    return sections


def collect_part_sections(book_dir: Path) -> list[str]:
    part_sections: list[str] = []
    part_dirs = sorted(
        d for d in book_dir.iterdir()
        if d.is_dir() and d.name.lower().startswith("part_")
    )
    for part_dir in part_dirs:
        collected = collect_folder(part_dir, include_divider=True)
        if collected:
            print(f"[{part_dir.name}]")
            part_sections.extend(collected)
    return part_sections


def collect_manuscript(book_dir: Path, include_front_matter: bool) -> str:
    if not book_dir.exists():
        raise SystemExit(f"Book folder not found: {book_dir}")

    sections: list[str] = []
    part_sections = collect_part_sections(book_dir)
    front_matter = book_dir / "00_Front_Matter"
    if front_matter.exists() and (include_front_matter or not part_sections):
        print("[00_Front_Matter]")
        sections.extend(collect_folder(front_matter, include_divider=False))

    sections.extend(part_sections)

    if not sections:
        raise SystemExit(
            f"No markdown content found under {book_dir}. Add front matter or chapters."
        )

    return "\n\n".join(sections) + "\n"


def build_frontmatter(title: str, subtitle: str, author: str, lang: str) -> str:
    return (
        "---\n"
        f'title: "{title}"\n'
        f'subtitle: "{subtitle}"\n'
        f'author: "{author}"\n'
        f"lang: {lang}\n"
        "---\n\n"
    )


def run_pandoc(manuscript_path: Path, output_path: Path, cover: Path | None,
               css: Path | None) -> None:
    cmd = [
        "pandoc",
        str(manuscript_path),
        "-o",
        str(output_path),
        "--toc",
        "--toc-depth=1",
        "--split-level=1",
        "--standalone",
    ]
    if cover:
        if cover.exists():
            cmd += ["--epub-cover-image", str(cover)]
        else:
            print(f"  ! warning: cover image not found at {cover}", file=sys.stderr)
    if css and css.exists():
        cmd += ["--css", str(css)]

    print("  $", " ".join(f'"{c}"' if " " in c else c for c in cmd))
    subprocess.run(cmd, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--book", default="11_Books/Book_01_Seda_y_Polvora")
    parser.add_argument("--title", default="Seda y Polvora")
    parser.add_argument("--subtitle", default="Silk & Gunpowder")
    parser.add_argument("--author", default="VICTOR PAZ")
    parser.add_argument("--lang", default="es")
    parser.add_argument("--cover", default="99_Reference/book_covers/Seda_y_Polvora_VICTOR_PAZ.png")
    parser.add_argument("--css", default="tools/epub-build/epub_style.css")
    parser.add_argument("--output-name", default="Seda_y_Polvora")
    parser.add_argument("--keep-manuscript", action="store_true")
    parser.add_argument(
        "--include-front-matter",
        action="store_true",
        help="Include 00_Front_Matter even when prose chapters exist.",
    )
    args = parser.parse_args()

    book_dir = (VAULT_ROOT / args.book).resolve()
    cover = (VAULT_ROOT / args.cover).resolve() if args.cover else None
    css = (VAULT_ROOT / args.css).resolve() if args.css else None
    out_dir = SCRIPT_DIR / "output"
    out_dir.mkdir(exist_ok=True)

    print(f"Building manuscript from {book_dir} ...")
    manuscript = build_frontmatter(args.title, args.subtitle, args.author, args.lang)
    manuscript += collect_manuscript(book_dir, args.include_front_matter)

    manuscript_path = out_dir / f"{args.output_name}.manuscript.md"
    manuscript_path.write_text(manuscript, encoding="utf-8")
    print(f"Manuscript written: {manuscript_path} ({len(manuscript):,} chars)")

    epub_path = out_dir / f"{args.output_name}.epub"
    print("Running Pandoc (EPUB) ...")
    run_pandoc(manuscript_path, epub_path, cover, css)
    print(f"EPUB ready: {epub_path}")

    if not args.keep_manuscript:
        manuscript_path.unlink()


if __name__ == "__main__":
    main()
