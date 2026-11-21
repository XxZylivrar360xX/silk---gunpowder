"""Revisor de citas protegidas (canon) tras editar prosa. Solo lectura; sin dependencias.

Compara cada archivo con una version de git (HEAD por defecto) y avisa si una cita
protegida aparece menos veces que antes. Citas protegidas:
  - las entrecomilladas («...» o "...") en lineas con canon de 06_Relationships/Hitos.md,
    98_Agent_Handoff/DECISIONS.md, 06_Relationships/Kal_y_Chiara.md y el 00_Book_Map del libro;
  - las entrecomilladas en las lineas del propio archivo (encabezado incluido) que dicen
    canon, literal, intocable, no tocar, no reintervenir o transcripcion.

LIMITE CONOCIDO: una nota que protege una escena entera sin citar sus lineas
(p. ej. «La moto de Nadir, literal salvo la primera frase») NO se detecta. Esas notas
hay que leerlas en el encabezado antes de editar.

Uso (desde la raiz del vault):
  python -I -X utf8 tools/editorial/canon_check.py ARCHIVO.md [...]
  python -I -X utf8 tools/editorial/canon_check.py --contra 8268b60 ARCHIVO.md
Sale con 1 si hay citas perdidas. Un aviso sobre una palabra suelta (p. ej. un nombre)
puede ser falso positivo: revisar el diff.
"""
import argparse
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SOURCES = [
    "06_Relationships/Hitos.md",
    "98_Agent_Handoff/DECISIONS.md",
    "06_Relationships/Kal_y_Chiara.md",
    "11_Books/Book_01_Mascaras_De_Cristal/00_Book_Map.md",
    "11_Books/Book_02_Sombras_De_Poder/00_Book_Map.md",
]
QUOTE = re.compile(r"[«\"“]([^»\"”]{6,200})[»\"”]")
MARK = re.compile(r"canon|literal|intocable|no tocar|no reintervenir|transcripci", re.I)


def norm(text):
    return re.sub(r"\s+", " ", text)


def clean(q):
    return norm(q).strip(" .…—")


def global_quotes():
    found = set()
    for rel in SOURCES:
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                if re.search("canon", line, re.I):
                    found.update(clean(q) for q in QUOTE.findall(line))
    return found


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--contra", default="HEAD", help="commit de referencia (HEAD por defecto)")
    a = ap.parse_args()
    base = global_quotes()
    lost = 0
    for f in a.files:
        rel = os.path.relpath(os.path.abspath(f), ROOT).replace("\\", "/")
        old = subprocess.run(["git", "show", f"{a.contra}:{rel}"], cwd=ROOT,
                             capture_output=True, text=True, encoding="utf-8").stdout
        if not old:
            print(f"{rel}: sin version en {a.contra}; se omite")
            continue
        with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
            new = fh.read()
        quotes = set(base)
        for line in old.split("\n"):
            if MARK.search(line):
                quotes.update(clean(q) for q in QUOTE.findall(line))
        on, nn = norm(old), norm(new)
        for q in sorted(quotes):
            if len(q) >= 6 and on.count(q) > nn.count(q):
                lost += 1
                print(f"{rel} :: PERDIDA: {q[:110]}")
    print("OK" if not lost else f"{lost} citas protegidas perdidas")
    return 1 if lost else 0


if __name__ == "__main__":
    sys.exit(main())
