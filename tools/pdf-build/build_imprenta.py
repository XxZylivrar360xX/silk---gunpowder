#!/usr/bin/env python3
"""Interior de imprenta (tapa blanda 6 x 9 in) del Libro I con Pandoc y Typst.

Distinto del PDF de lectura (`build_pdf.py`, A5): páginas en espejo, capítulos y
partes en página impar, cabeceras corridas, folios, preliminares en orden y
sin cubierta (la cubierta va en archivo aparte). Al final imprime el número de
páginas y el lomo estimado para KDP.

`--edicion autor`: el mismo interior con portada y contraportada, para lectura
privada (no es el archivo de KDP).
"""

from __future__ import annotations

import argparse
import importlib.util
import io
import json
import re
import shutil
import subprocess
import sys
from contextlib import redirect_stdout
from datetime import date
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parents[2]
EPUB_BUILDER = VAULT_ROOT / "tools" / "epub-build" / "build_epub.py"
OUTPUT_DIR = VAULT_ROOT / "output" / "pdf"
TEMP_DIR = VAULT_ROOT / "tmp" / "imprenta"
PART_RE = re.compile(
    r"^# \[(?P<ordinal>.+?)\]\{\.part-number\} \[(?P<title>.+?)\]\{\.part-name\} \{\.part-title\}$",
    re.MULTILINE,
)
# Grosor por página de KDP (pulgadas): papel blanco y crema.
BLEED = 0.125  # sangrado de la tapa completa, en pulgadas
SPINE_PER_PAGE = {"blanco": 0.002252, "crema": 0.0025}

TEMPLATE = r"""
#let book-title = __TITLE__
#let book-author = __AUTHOR__
#let book-series = __SERIES__
#let book-volume = __VOLUME__
#let book-year = __YEAR__

#set document(title: book-title, author: book-author)
#set text(font: "Libertinus Serif", size: 11pt, lang: "es", region: "mx", hyphenate: true)
#set par(justify: true, leading: 0.68em, spacing: 0.68em, first-line-indent: 1.25em)
#set smartquote(enabled: false)

// ── Marcas para saber qué página abre sección y cuál quedó en blanco ──
#let mark-end = [#metadata("fin") <sec-end>]
#let mark-start = [#metadata("inicio") <sec-start>]
#let pages-of(lbl) = query(lbl).map(m => m.location().page())
#let is-opening(p) = pages-of(<sec-start>).contains(p)
#let is-blank(p) = {
  let later = pages-of(<sec-start>).filter(s => s > p)
  if later.len() == 0 { return false }
  let next = calc.min(..later)
  let ends = pages-of(<sec-end>).filter(e => e < next)
  ends.len() > 0 and calc.max(..ends) < p
}
#let in-body(p) = {
  let starts = pages-of(<sec-start>)
  let idx = pages-of(<index-start>)
  starts.len() > 0 and p >= calc.min(..starts) and (idx.len() == 0 or p < idx.first())
}

#set page(
  width: 6in, height: 9in, binding: left,
  margin: (inside: 0.875in, outside: 0.625in, top: 0.85in, bottom: 0.85in),
  header-ascent: 45%, footer-descent: 40%,
  header: context {
    let p = here().page()
    if not in-body(p) or is-opening(p) or is-blank(p) { return }
    set text(size: 8.5pt, tracking: 0.04em)
    set par(first-line-indent: 0pt, justify: false)
    if calc.odd(p) {
      let chs = query(heading.where(level: 1).before(here()))
      let cur = if chs.len() > 0 { chs.last().body } else { [] }
      [#h(1fr)#smallcaps(cur)#h(1.6em)#str(p)]
    } else {
      [#str(p)#h(1.6em)#smallcaps(book-title)#h(1fr)]
    }
  },
  footer: context {
    let p = here().page()
    if not in-body(p) or not is-opening(p) or pages-of(<part>).contains(p) { return }
    set text(size: 8.5pt)
    align(center, str(p))
  },
)

// ── Capítulos: página impar, caída, número y título ──
#let chapter-counter = counter("capitulo")
#show heading.where(level: 1): it => {
  mark-end
  pagebreak(to: "odd", weak: true)
  mark-start
  chapter-counter.step()
  v(1.55in)
  set par(first-line-indent: 0pt, justify: false)
  align(center)[
    #text(size: 9pt, tracking: 0.3em)[#upper[Capítulo]#h(0.45em)#context chapter-counter.display()]
    #v(0.9em)
    #text(size: 17pt, style: "italic", hyphenate: false, it.body)
    #v(0.5em)
    #text(size: 9pt)[#sym.diamond.stroked.small]
  ]
  v(0.55in)
}

// ── Portadillas de parte: página impar, verso en blanco ──
#let part-page(ordinal, title) = {
  mark-end
  pagebreak(to: "odd", weak: true)
  mark-start
  [#metadata((ordinal: ordinal, title: title)) <part>]
  v(2.5in)
  align(center)[
    #text(size: 9.5pt, tracking: 0.35em, upper(ordinal))
    #v(1.1em)
    #text(size: 24pt, title)
  ]
  mark-end
}

// ── Cambio de escena y cartas ──
#let divider() = block(above: 1.15em, below: 1.15em, width: 100%, sticky: true,
  align(center, text(size: 10pt)[\* #h(0.9em) \* #h(0.9em) \*]))
#show quote.where(block: true): it => pad(x: 1.5em, block(above: 1.1em, below: 1.1em, {
  set text(size: 10.3pt)
  set par(first-line-indent: 0pt, spacing: 0.75em)
  it.body
}))

// ── Preliminares ──
#let plain(body) = page(header: none, footer: none, body)
#let cover(file) = page(margin: 0pt, header: none, footer: none,
  image(file, width: 100%, height: 100%, fit: "cover"))
__FRONT_COVER__
#plain[
  #v(2.3in)
  #align(center, text(size: 14pt, tracking: 0.18em, upper(book-title)))
]
#plain[]
#plain[
  #set par(first-line-indent: 0pt)
  #v(1.25in)
  #align(center)[
    #text(size: 12pt, tracking: 0.2em, upper(book-author))
    #v(0.85in)
    #text(size: 30pt, book-title)
    #v(0.35in)
    #text(size: 11pt, style: "italic")[#book-series · #book-volume]
  ]
]
#plain[
  #set text(size: 8.5pt)
  #set par(first-line-indent: 0pt, justify: false, spacing: 1.05em)
  #v(1fr)
  #emph(book-title)

  © #book-year #book-author
__EDITION_NOTE__

  Todos los derechos reservados. Queda prohibida la reproducción total o parcial de esta obra sin autorización escrita del autor.

  Esta es una obra de ficción. Los nombres, personajes, lugares y sucesos son producto de la imaginación del autor o se usan de manera ficticia. Cualquier parecido con personas, vivas o muertas, o con hechos reales es pura coincidencia.
]

__BODY__

// ── Índice al final, como en la edición en español ──
#mark-end
#pagebreak(to: "odd")
#mark-start
#metadata("indice") <index-start>
#page(header: none, footer: none)[
  #set par(first-line-indent: 0pt, justify: false, spacing: 0.5em)
  #v(0.6in)
  #align(center, text(size: 10pt, tracking: 0.3em, upper[Índice]))
  #v(0.35in)
  #context {
    let items = (query(<part>) + query(heading.where(level: 1)))
      .sorted(key: e => (e.location().page(), e.location().position().y.pt()))
    let n = 0
    for e in items {
      if e.func() == metadata {
        v(0.8em)
        align(center, text(size: 8.5pt, tracking: 0.25em,
          upper(e.value.ordinal + " · " + e.value.title)))
        v(0.35em)
      } else {
        n += 1
        set text(size: 9.5pt)
        grid(columns: (1.8em, 1fr, auto), column-gutter: 0.3em,
          align(right, str(n) + "."),
          [#e.body #box(width: 1fr, repeat[#h(0.25em).])],
          str(e.location().page()))
      }
    }
  }
]
__BACK_COVER__
"""


def load_epub_builder():
    spec = importlib.util.spec_from_file_location("build_epub", EPUB_BUILDER)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


def part_to_typst(match: re.Match[str]) -> str:
    args = ", ".join(json.dumps(match.group(k), ensure_ascii=False) for k in ("ordinal", "title"))
    return f"```{{=typst}}\n#part-page({args})\n```"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--book", default="11_Books/Book_01_Mascaras_De_Cristal")
    parser.add_argument("--title", default="Máscaras de Cristal")
    parser.add_argument("--author", default="Víctor Paz")
    parser.add_argument("--series", default="Seda y Pólvora")
    parser.add_argument("--volume", default="Libro I")
    parser.add_argument("--year", default=str(date.today().year))
    parser.add_argument("--edicion", choices=("kdp", "autor"), default="kdp",
                        help="kdp: interior sin cubierta para la imprenta; autor: con portada y contraportada, para lectura privada.")
    parser.add_argument("--tapa", default="99_Reference/book_covers/Mascaras_De_Cristal_Tapa_6x9_v1.png",
                        help="Tapa completa (contraportada + lomo + portada, con sangrado) de la que salen las cubiertas de la edición de autor.")
    parser.add_argument("--output-name")
    parser.add_argument("--muestra", metavar="PAGINAS",
                        help="En vez del PDF, exporta esas páginas a PNG (p. ej. 1-8,15) en --muestra-dir.")
    parser.add_argument("--muestra-dir", default=str(TEMP_DIR / "muestra"))
    args = parser.parse_args()

    pandoc, typst = shutil.which("pandoc"), shutil.which("typst")
    if not pandoc or not typst:
        print("Error: hacen falta Pandoc y Typst en PATH.", file=sys.stderr)
        return 1

    builder = load_epub_builder()
    book_dir = (VAULT_ROOT / args.book).resolve()
    log = io.StringIO()
    with redirect_stdout(log):
        manuscript = builder.collect_manuscript(book_dir, include_front_matter=False)
    chapters = sum(line.startswith("  + ") for line in log.getvalue().splitlines())
    manuscript, parts = PART_RE.subn(part_to_typst, manuscript)
    print(f"Manuscrito reunido: {chapters} capítulos en {parts} partes.")

    TEMP_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    md_path, body_path, main_path = (TEMP_DIR / n for n in ("manuscript.md", "body.typ", "main.typ"))
    autor = args.edicion == "autor"
    output_name = args.output_name or (
        "Mascaras_De_Cristal_Edicion_Autor_6x9" if autor else "Mascaras_De_Cristal_Imprenta_6x9")
    output_path = OUTPUT_DIR / f"{output_name}.pdf"
    cover_files = [TEMP_DIR / "portada.jpg", TEMP_DIR / "contraportada.jpg"]
    covers = {"__FRONT_COVER__": "", "__BACK_COVER__": "", "__EDITION_NOTE__": ""}
    if autor:
        tapa = (VAULT_ROOT / args.tapa).resolve()
        if not tapa.is_file():
            print(f"Error: no encuentro la tapa {args.tapa}.", file=sys.stderr)
            return 2
        try:
            from PIL import Image
        except ImportError:
            print("Error: la edición de autor necesita Pillow (pip install pillow).", file=sys.stderr)
            return 1
        with Image.open(tapa) as im:
            im = im.convert("RGB")
            dpi = im.height / (9 + 2 * BLEED)  # la altura de la tapa incluye el sangrado
            bleed, w, h = round(BLEED * dpi), round(6 * dpi), round(9 * dpi)
            im.crop((im.width - bleed - w, bleed, im.width - bleed, bleed + h)).save(
                cover_files[0], quality=92)
            im.crop((bleed, bleed, bleed + w, bleed + h)).save(cover_files[1], quality=92)
        covers = {
            # Portada, interior de cubierta en blanco y la portadilla vuelve a caer en impar.
            "__FRONT_COVER__": '#cover("portada.jpg")\n#plain[]',
            # Contraportada siempre en página par, como en el libro impreso.
            "__BACK_COVER__": '#pagebreak(weak: true, to: "even")\n#cover("contraportada.jpg")',
            "__EDITION_NOTE__": "\n  Edición de autor, para lectura privada.\n",
        }
    values = {
        "__TITLE__": args.title, "__AUTHOR__": args.author, "__SERIES__": args.series,
        "__VOLUME__": args.volume, "__YEAR__": args.year,
    }
    template = TEMPLATE
    for key, value in values.items():
        template = template.replace(key, json.dumps(value, ensure_ascii=False))
    for key, value in covers.items():
        template = template.replace(key, value)
    try:
        md_path.write_text(manuscript, encoding="utf-8")
        subprocess.run([pandoc, str(md_path), "-f", "markdown", "-t", "typst", "-o", str(body_path)],
                       check=True)
        body = body_path.read_text(encoding="utf-8")
        main_path.write_text(template.replace("__BODY__", body, 1), encoding="utf-8")
        if args.muestra:
            sample_dir = Path(args.muestra_dir)
            sample_dir.mkdir(parents=True, exist_ok=True)
            subprocess.run([typst, "compile", "--root", str(TEMP_DIR), "--pages", args.muestra,
                            "--ppi", "110", str(main_path), str(sample_dir / "p{0p}.png")], check=True)
            print(f"Muestra en {sample_dir}")
            return 0
        print(f"Componiendo {output_path.relative_to(VAULT_ROOT)} ...")
        subprocess.run([typst, "compile", "--root", str(TEMP_DIR), str(main_path), str(output_path)],
                       check=True)
    except subprocess.CalledProcessError as exc:
        print(f"Error: el proceso terminó con código {exc.returncode}.", file=sys.stderr)
        return exc.returncode or 1
    finally:
        for path in (md_path, body_path, main_path, *cover_files):
            path.unlink(missing_ok=True)

    data = output_path.read_bytes()
    pages = len(re.findall(rb"/Type\s*/Page[^s]", data))
    print(f"PDF de imprenta listo: {output_path.relative_to(VAULT_ROOT)}")
    if pages and autor:
        print(f"Páginas: {pages}, con portada, contraportada y sus interiores.")
    elif pages:
        spine = ", ".join(f"papel {k}: {pages * v:.3f} in ({pages * v * 25.4:.1f} mm)"
                          for k, v in SPINE_PER_PAGE.items())
        print(f"Páginas: {pages}. Lomo estimado (KDP) — {spine}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
