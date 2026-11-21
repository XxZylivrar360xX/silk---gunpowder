"""Detector de dialogo ping-pong (regla de dialogo 05, prohibicion del 2026-11-21).

Marca tramos de N o mas replicas seguidas cuyo texto hablado (sin acotaciones
entre rayas) tiene MAXW palabras o menos. Beats narrativos de una linea corta
no rompen el tramo. Solo lectura; sin dependencias.

Uso:
  python tools/editorial/pingpong_audit.py                 # Libro I
  python tools/editorial/pingpong_audit.py --book 2
  python tools/editorial/pingpong_audit.py --min 5 --maxw 14 RUTA.md ...
  python tools/editorial/pingpong_audit.py --cortas      # regla 06: % de replicas de <=3 palabras
"""
import argparse
import glob
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BOOKS = {
    "1": "11_Books/Book_01_Mascaras_De_Cristal",
    "2": "11_Books/Book_02_Sombras_De_Poder",
}
BEAT_MAX = 12  # palabras de un beat narrativo que no corta el tramo


def book_files(book):
    base = os.path.join(ROOT, BOOKS[book])
    out = []
    for part in sorted(glob.glob(os.path.join(base, "Part_*"))):
        out += sorted(f for f in glob.glob(os.path.join(part, "*.md"))
                      if not os.path.basename(f).startswith("00_"))
    return out


def spoken(par):
    body = par[1:]
    pieces = body.split("—")
    return len(" ".join(pieces[0::2]).split()), len(body.split())


def scan(path, minrun, maxw):
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    found, run = [], []

    def flush():
        if len(run) >= minrun:
            found.append((run[0], run[-1], len(run)))

    for i, raw in enumerate(lines, 1):
        t = raw.strip()
        if not t:
            continue
        if t.startswith("—"):
            sw, tw = spoken(t)
            if sw <= maxw and tw <= maxw + 10:
                run.append(i)
                continue
        elif run and len(t.split()) <= BEAT_MAX and not t.startswith("#") and t != "***":
            continue
        flush()
        run = []
    flush()
    return found


def short_share(path, maxw=3):
    total = short = 0
    with open(path, encoding="utf-8") as fh:
        for raw in fh:
            t = raw.strip()
            if t.startswith("—"):
                total += 1
                if spoken(t)[0] <= maxw:
                    short += 1
    return total, short


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*")
    ap.add_argument("--book", default="1", choices=sorted(BOOKS))
    ap.add_argument("--min", type=int, default=5)
    ap.add_argument("--maxw", type=int, default=14)
    ap.add_argument("--cortas", action="store_true",
                    help="regla 06: porcentaje de replicas de <=3 palabras por archivo")
    ap.add_argument("--vara", type=int, default=25)
    a = ap.parse_args()
    files = a.files or book_files(a.book)
    if a.cortas:
        over = 0
        for f in files:
            total, short = short_share(f)
            if not total:
                continue
            pct = 100 * short / total
            mark = "  <-- sobre la vara" if pct > a.vara else ""
            over += bool(mark)
            print(f"{os.path.relpath(f, ROOT)}: {short}/{total} = {pct:.0f}%{mark}")
        print(f"TOTAL: {over} archivos sobre la vara de {a.vara}%")
        return 1 if over else 0
    total = nfiles = 0
    for f in files:
        hits = scan(f, a.min, a.maxw)
        if hits:
            nfiles += 1
        for start, end, n in hits:
            total += 1
            print(f"{os.path.relpath(f, ROOT)}:{start}-{end}  ({n} replicas)")
    print(f"TOTAL: {total} tramos en {nfiles} archivos (min={a.min}, maxw={a.maxw})")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
