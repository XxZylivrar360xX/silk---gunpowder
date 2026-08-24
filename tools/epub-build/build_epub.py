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
    parts = folder_name.split("_")
    if parts[0].lower() == "part" and len(parts) >= 3:
        return f"Part {parts[1]} - {' '.join(parts[2:])}"
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


def read_markdown(path: Path) -> str:
    text = path.read_text(encoding="utf-8-sig")
    text = strip_yaml_frontmatter(text)
    text = clean_wikilinks(text)
    return text.strip() + "\n"


def collect_folder(folder: Path, include_divider: bool) -> list[str]:
    files = sorted(p for p in folder.glob("*.md") if p.is_file())
    if not files:
        return []

    sections: list[str] = []
    if include_divider:
        sections.append(f"# {divider_title(folder.name)}\n")
    for file_path in files:
        print(f"  + {file_path.relative_to(VAULT_ROOT)}")
        sections.append(read_markdown(file_path))
    return sections


def collect_manuscript(book_dir: Path) -> str:
    if not book_dir.exists():
        raise SystemExit(f"Book folder not found: {book_dir}")

    sections: list[str] = []
    front_matter = book_dir / "00_Front_Matter"
    if front_matter.exists():
        print("[00_Front_Matter]")
        sections.extend(collect_folder(front_matter, include_divider=False))

    part_dirs = sorted(
        d for d in book_dir.iterdir()
        if d.is_dir() and d.name.lower().startswith("part_")
    )
    for part_dir in part_dirs:
        collected = collect_folder(part_dir, include_divider=True)
        if collected:
            print(f"[{part_dir.name}]")
            sections.extend(collected)

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
        "--toc-depth=2",
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
    parser.add_argument("--author", default="Vic")
    parser.add_argument("--lang", default="es")
    parser.add_argument("--cover", default="99_Reference/book_covers/seda_y_polvora_cover.png")
    parser.add_argument("--css", default="tools/epub-build/epub_style.css")
    parser.add_argument("--output-name", default="Seda_y_Polvora")
    parser.add_argument("--keep-manuscript", action="store_true")
    args = parser.parse_args()

    book_dir = (VAULT_ROOT / args.book).resolve()
    cover = (VAULT_ROOT / args.cover).resolve() if args.cover else None
    css = (VAULT_ROOT / args.css).resolve() if args.css else None
    out_dir = SCRIPT_DIR / "output"
    out_dir.mkdir(exist_ok=True)

    print(f"Building manuscript from {book_dir} ...")
    manuscript = build_frontmatter(args.title, args.subtitle, args.author, args.lang)
    manuscript += collect_manuscript(book_dir)

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

