#!/usr/bin/env python3
"""
Build a chapter-by-chapter MP3 audiobook of a Seda y Polvora book.

- Chapters are collected exactly like the EPUB (tools/epub-build/build_epub.py):
  same order, same EPUB: EXCLUDE stubs, same internal-marker guard.
- pronunciaciones.txt respells Italian/English names for the Spanish voice;
  only the spoken text changes, never the manuscript.
- Speech comes from Microsoft's neural voices through edge-tts (online).
- Unchanged chapters are skipped: a manifest stores a hash of each spoken text.
"""

import argparse
import asyncio
import datetime
import hashlib
import json
import re
import ssl
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
VAULT_ROOT = SCRIPT_DIR.parents[1]
sys.path.insert(0, str(VAULT_ROOT / "tools" / "epub-build"))
import build_epub as be  # noqa: E402

DEFAULT_BOOK = "Book_01_Mascaras_De_Cristal"
DEFAULT_VOICE = "es-MX-DaliaNeural"
DICTIONARY_PATH = SCRIPT_DIR / "pronunciaciones.txt"
OUTPUT_ROOT = VAULT_ROOT / "output" / "audiolibro"
MANIFEST_NAME = "manifest.json"
# Tracked in git: which chapters have audio that no longer matches the prose.
LOG_DIR = SCRIPT_DIR / "bitacora"
RETRIES = 3
# Metadata the players show: album title and saga position per book.
BOOKS = {
    "Book_01_Mascaras_De_Cristal": ("Máscaras de Cristal", "I"),
    "Book_02_Sombras_De_Poder": ("Sombras de Poder", "II"),
    "Book_03_Voto_De_Ceniza": ("Voto de Ceniza", "III"),
    "Book_04_Cuentas_De_Sangre": ("Cuentas de Sangre", "IV"),
    "Book_05_Juramento_De_Hierro": ("Juramento de Hierro", "V"),
    "Book_06_Hijos_Del_Silencio": ("Hijos del Silencio", "VI"),
    "Book_07_Camino_A_Casa": ("Camino a Casa", "VII"),
}
SAGA = "Seda y Pólvora"
AUTHOR = "Víctor Paz"
YEAR = "2026"
COVERS_DIR = VAULT_ROOT / "99_Reference" / "book_covers"
COVER_SIZE = 800  # px; the source PNGs weigh ~2 MB and go into every MP3

HEADING_RE = re.compile(r"^#\s+(?:Capítulo|Capitulo)\s+(\d+)\s*[—–:.-]\s*(.+)$", re.MULTILINE)
SCENE_BREAK_RE = re.compile(r"^\s*(?:\*\s*\*\s*\*|-{3,}|⁂)\s*$", re.MULTILINE)
EMPHASIS_RE = re.compile(r"(\*{1,3}|_{1,3})(?=\S)(.+?)(?<=\S)\1", re.DOTALL)
BLOCKQUOTE_RE = re.compile(r"^\s*>\s?", re.MULTILINE)
ALL_CAPS_RE = re.compile(r"\b[A-ZÁÉÍÓÚÑ]{2,}\b")
# Acronyms the voice should spell out; every other all-caps word is read as a word.
KEEP_CAPS = {"SPV", "PDF", "SUV", "FBI", "DEA", "ATF", "CEO", "GPS", "VIP"}
FILENAME_UNSAFE_RE = re.compile(r'[<>:"/\\|?*]')


def load_dictionary(path: Path) -> list[tuple[re.Pattern[str], str]]:
    entries: list[tuple[str, str]] = []
    for number, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            raise SystemExit(f"{path.name}:{number}: falta '=' en {line!r}")
        original, spoken = (part.strip() for part in line.split("=", 1))
        if not original or not spoken:
            raise SystemExit(f"{path.name}:{number}: entrada incompleta {line!r}")
        entries.append((original, spoken))

    rules: list[tuple[re.Pattern[str], str]] = []
    for original, spoken in sorted(entries, key=lambda e: len(e[0]), reverse=True):
        body = re.escape(original)
        if original[0].islower():
            # lowercase entries also catch the sentence-initial capitalized form
            body = f"[{original[0]}{original[0].upper()}]{re.escape(original[1:])}"
        rules.append((re.compile(rf"(?<![\w']){body}(?![\w'])"), spoken))
    return rules


def apply_dictionary(text: str, rules: list[tuple[re.Pattern[str], str]]) -> str:
    def replacer(spoken: str):
        def repl(match: re.Match[str]) -> str:
            if match.group(0)[0].isupper() and spoken[0].islower():
                return spoken[0].upper() + spoken[1:]
            return spoken
        return repl

    for pattern, spoken in rules:
        text = pattern.sub(replacer(spoken), text)
    return text


def speech_text(raw: str, rules: list[tuple[re.Pattern[str], str]],
                part_title: str | None) -> tuple[str, str, str]:
    """Return (number, title, text to speak) for one chapter."""
    # build_epub drops "Capítulo N" from the heading, so read it from the source
    heading = HEADING_RE.search(be.HTML_COMMENT_RE.sub("", raw))
    if not heading:
        raise ValueError("No encontré el encabezado '# Capítulo N — Título'.")
    number, title = heading.group(1), heading.group(2).strip()

    prose = be.format_markdown(raw)
    body = prose.split("\n", 1)[1] if prose.startswith("# ") else prose
    body = SCENE_BREAK_RE.sub("\n\n", body)
    body = BLOCKQUOTE_RE.sub("", body)
    body = EMPHASIS_RE.sub(r"\2", body)
    body = re.sub(r"^#+\s*", "", body, flags=re.MULTILINE)
    body = ALL_CAPS_RE.sub(
        lambda m: m.group(0) if m.group(0) in KEEP_CAPS else m.group(0).capitalize(), body)

    opening = f"Capítulo {number}. {title}."
    if part_title:
        opening = f"{part_title}.\n\n{opening}"
    text = f"{opening}\n\n{body.strip()}\n"
    text = re.sub(r"\n{3,}", "\n\n", text)
    return number, title, apply_dictionary(text, rules)


def collect_chapters(book_dir: Path) -> list[tuple[Path, str | None]]:
    """Chapter files in EPUB order; the first of each part carries its title."""
    chapters: list[tuple[Path, str | None]] = []
    for part_dir in sorted(d for d in book_dir.iterdir()
                           if d.is_dir() and d.name.lower().startswith("part_")):
        pieces = part_dir.name.split("_")
        ordinal = be.PART_ORDINALS.get(pieces[1], f"Parte {pieces[1]}")
        title = be.PART_TITLES.get(part_dir.name, " ".join(pieces[2:]).capitalize())
        announced = False
        for path in sorted(part_dir.glob("*.md")):
            if be.is_epub_excluded(path.read_text(encoding="utf-8-sig")):
                continue
            chapters.append((path, None if announced else f"{ordinal}. {title}"))
            announced = True
    return chapters


def make_ssl_context() -> ssl.SSLContext:
    # edge-tts trusts only certifi's bundle; on this machine that fails, so use
    # the Windows certificate store when truststore is available.
    try:
        import truststore
        return truststore.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    except ImportError:
        return ssl.create_default_context()


async def synthesize(text: str, voice: str, rate: str, target: Path) -> None:
    import edge_tts
    import edge_tts.communicate
    edge_tts.communicate._SSL_CTX = make_ssl_context()

    partial = target.with_suffix(".part")
    for attempt in range(1, RETRIES + 1):
        try:
            await edge_tts.Communicate(text, voice, rate=rate).save(str(partial))
            partial.replace(target)
            return
        except Exception as error:  # network hiccups are common on long books
            partial.unlink(missing_ok=True)
            if attempt == RETRIES:
                raise
            print(f"    reintento {attempt}/{RETRIES - 1}: {error}")
            await asyncio.sleep(5 * attempt)


def load_cover(book: str) -> bytes | None:
    """The book's cover as a small JPEG, or None if there is no cover yet."""
    stem = book.split("_", 2)[-1].lower()
    found = [p for p in COVERS_DIR.glob("*.png") if p.stem.lower().startswith(stem + "_")]
    if not found:
        print(f"  sin portada para {book} en {COVERS_DIR.relative_to(VAULT_ROOT)}")
        return None
    from io import BytesIO
    from PIL import Image
    with Image.open(found[0]) as image:
        image.thumbnail((COVER_SIZE, COVER_SIZE))
        buffer = BytesIO()
        image.convert("RGB").save(buffer, "JPEG", quality=88)
    return buffer.getvalue()


def tag_audio(target: Path, chapter: dict, total: int, book: str, cover: bytes | None) -> None:
    """Write title, album, author, track and cover; replaces any previous tags."""
    from mutagen.id3 import APIC, ID3, TALB, TCON, TDRC, TIT1, TIT2, TIT3, TPE1, TPE2, TRCK
    title, position = BOOKS.get(book, (book.split("_", 2)[-1].replace("_", " "), ""))
    subtitle = f"{SAGA} · Libro {position}" if position else SAGA
    tags = ID3()
    tags.add(TIT2(encoding=3, text=f"Capítulo {chapter['number']} — {chapter['title']}"))
    tags.add(TIT3(encoding=3, text=subtitle))
    tags.add(TIT1(encoding=3, text=SAGA))
    tags.add(TALB(encoding=3, text=title))
    tags.add(TPE1(encoding=3, text=AUTHOR))
    tags.add(TPE2(encoding=3, text=AUTHOR))
    tags.add(TRCK(encoding=3, text=f"{chapter['number']}/{total}"))
    tags.add(TCON(encoding=3, text="Audiolibro"))
    tags.add(TDRC(encoding=3, text=YEAR))
    if cover:
        tags.add(APIC(encoding=3, mime="image/jpeg", type=3, desc="Portada", data=cover))
    tags.save(target, v2_version=3)  # ID3v2.3: what Windows and most players read


def safe_filename(number: str, title: str) -> str:
    return f"{int(number):02d} - {FILENAME_UNSAFE_RE.sub('', title)}.mp3"


def dictionary_sample(rules) -> str:
    lines = []
    for line in DICTIONARY_PATH.read_text(encoding="utf-8-sig").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            original = line.split("=", 1)[0].strip()
            lines.append(f"{apply_dictionary(original, rules)}.")
    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Genera el audiolibro por capítulos.")
    parser.add_argument("--book", default=DEFAULT_BOOK,
                        help=f"Carpeta del libro en 11_Books (default: {DEFAULT_BOOK})")
    parser.add_argument("--capitulo", type=int, action="append", dest="chapters",
                        help="Número de capítulo a generar; repetible. Sin esto, todo el libro.")
    parser.add_argument("--voz", default=DEFAULT_VOICE, dest="voice")
    parser.add_argument("--velocidad", default="+0%", dest="rate",
                        help="Ajuste de velocidad, p. ej. -10%% o +5%%")
    parser.add_argument("--forzar", action="store_true", dest="force",
                        help="Regenera aunque el texto no haya cambiado.")
    parser.add_argument("--solo-texto", action="store_true", dest="text_only",
                        help="Escribe el texto que se leería (.txt) sin generar audio.")
    parser.add_argument("--estado", action="store_true", dest="status_only",
                        help="Solo actualiza la bitácora (sin red, sin audio).")
    parser.add_argument("--probar-diccionario", action="store_true", dest="test_dictionary",
                        help="Genera un MP3 que lee cada entrada del diccionario.")
    parser.add_argument("--etiquetar", action="store_true", dest="tag_only",
                        help="Reescribe título, álbum, autor y portada de los MP3 existentes "
                             "(sin red, sin audio).")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rules = load_dictionary(DICTIONARY_PATH)
    book_dir = VAULT_ROOT / "11_Books" / args.book
    if not book_dir.is_dir():
        raise SystemExit(f"No existe el libro: {book_dir}")
    out_dir = OUTPUT_ROOT / args.book.split("_", 2)[-1]
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.test_dictionary:
        target = out_dir / "00 - Prueba de diccionario.mp3"
        asyncio.run(synthesize(dictionary_sample(rules), args.voice, args.rate, target))
        print(f"Listo: {target.relative_to(VAULT_ROOT)}")
        return

    manifest_path = out_dir / MANIFEST_NAME
    manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}

    chapters = []
    for path, part_title in collect_chapters(book_dir):
        raw = path.read_text(encoding="utf-8-sig")
        try:
            number, title, text = speech_text(raw, rules, part_title)
        except ValueError as error:
            raise SystemExit(f"{path.relative_to(VAULT_ROOT)}: {error}")
        chapters.append({
            "source": path.name, "number": int(number), "title": title, "text": text,
            "target": out_dir / safe_filename(number, title),
            "hash": hashlib.sha256(f"{args.voice}|{args.rate}|{text}".encode()).hexdigest(),
            "prose": hashlib.sha256(be.format_markdown(raw).encode()).hexdigest(),
        })

    wanted = set(args.chapters or [])
    missing = wanted - {chapter["number"] for chapter in chapters}
    if missing:
        raise SystemExit(f"No encontré los capítulos: {sorted(missing)}")

    if args.tag_only:
        cover = load_cover(args.book)
        for chapter in chapters:
            if chapter["target"].exists() and (not wanted or chapter["number"] in wanted):
                tag_audio(chapter["target"], chapter, len(chapters), args.book, cover)
                print(f"  etiqueta  {chapter['target'].name}")
        return

    cover = None if args.status_only or args.text_only else load_cover(args.book)
    for chapter in chapters:
        if args.status_only or (wanted and chapter["number"] not in wanted):
            continue
        target = chapter["target"]
        if args.text_only:
            target.with_suffix(".txt").write_text(chapter["text"], encoding="utf-8")
            print(f"  texto  {target.with_suffix('.txt').name}")
            continue

        record = manifest.get(chapter["source"], {})
        if not args.force and record.get("hash") == chapter["hash"] and target.exists():
            print(f"  igual  {target.name}")
            continue

        print(f"  audio  {target.name} ({len(chapter['text'].split())} palabras)")
        old = out_dir / record.get("file", "")
        if record.get("file") and old != target and old.exists():
            old.unlink()  # chapter renamed or renumbered
        asyncio.run(synthesize(chapter["text"], args.voice, args.rate, target))
        tag_audio(target, chapter, len(chapters), args.book, cover)
        manifest[chapter["source"]] = {
            "file": target.name, "hash": chapter["hash"], "prose": chapter["prose"],
            "date": datetime.date.today().isoformat(),
        }
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2),
                                 encoding="utf-8")

    if args.text_only:
        return
    # Audio made before the log existed matches today's prose; record it so a later
    # change can be told apart as prose vs. dictionary.
    backfilled = False
    for chapter in chapters:
        record = manifest.get(chapter["source"])
        if record and "prose" not in record and record.get("hash") == chapter["hash"]:
            record["prose"] = chapter["prose"]
            backfilled = True
    if backfilled:
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2),
                                 encoding="utf-8")
    update_log(args.book, chapters, manifest)


def chapter_status(chapter: dict, record: dict) -> tuple[str, str]:
    if not record or not chapter["target"].exists():
        return "SIN AUDIO", ""
    if record.get("hash") == chapter["hash"]:
        return "AL DIA", ""
    if "prose" not in record:  # audio made before the log existed
        return "PENDIENTE", "cambió el texto hablado (prosa, numeración o diccionario)"
    if record["prose"] != chapter["prose"]:
        return "PENDIENTE", "cambió la prosa"
    return "PENDIENTE", "cambió la numeración, el diccionario o la voz"


def update_log(book: str, chapters: list[dict], manifest: dict) -> None:
    """Refresh bitacora/<Libro>.md; every change of state goes to its history."""
    LOG_DIR.mkdir(exist_ok=True)
    name = book.split("_", 2)[-1]
    state_path = LOG_DIR / f"{name}.json"
    md_path = LOG_DIR / f"{name}.md"
    state = json.loads(state_path.read_text(encoding="utf-8")) if state_path.exists() else {}
    previous = state.get("capitulos", {})
    history = state.get("historial", [])
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    if not state:
        history.append([now, "-", "bitácora iniciada"])

    current = {}
    for chapter in chapters:
        record = manifest.get(chapter["source"], {})
        status, reason = chapter_status(chapter, record)
        before = previous.get(chapter["source"], {})
        label = f"Cap. {chapter['number']} ({chapter['source']})"
        if before.get("estado", status) != status or (not before and status == "PENDIENTE"):
            event = {"PENDIENTE": f"audio pendiente: {reason}",
                     "AL DIA": "audio regenerado" if before.get("estado") == "PENDIENTE"
                     else "audio generado",
                     "SIN AUDIO": "audio borrado"}[status]
            history.append([now, label, event])
        audio_date = record.get("date", "")
        if not audio_date and chapter["target"].exists():
            audio_date = datetime.date.fromtimestamp(chapter["target"].stat().st_mtime).isoformat()
        current[chapter["source"]] = {
            "capitulo": chapter["number"], "titulo": chapter["title"],
            "estado": status, "motivo": reason, "audio": audio_date,
            "desde": before["desde"] if before.get("estado") == status else now,
        }

    state_path.write_text(json.dumps({"capitulos": current, "historial": history},
                                     ensure_ascii=False, indent=2), encoding="utf-8")

    rows = sorted(current.values(), key=lambda row: row["capitulo"])
    pending = [row for row in rows if row["estado"] != "AL DIA"]
    lines = [
        f"# Bitácora del audiolibro — {name.replace('_', ' ')}",
        "",
        "Generada por `tools/audiolibro/build_audiobook.py`; no editar a mano. Tras cambiar "
        "la prosa de un capítulo, correr `--estado` para marcarlo PENDIENTE; la bandera se "
        "cierra sola cuando el script regenera ese audio.",
        "",
        f"Actualizada: {now}. Al día: {len(rows) - len(pending)} de {len(rows)}.",
        "",
        "## Pendientes",
        "",
    ]
    if pending:
        lines += ["| Cap. | Título | Estado | Motivo | Desde |", "|---|---|---|---|---|"]
        lines += [f"| {r['capitulo']} | {r['titulo']} | {r['estado']} | {r['motivo']} | {r['desde']} |"
                  for r in pending]
    else:
        lines.append("Ninguno: todos los audios corresponden a la prosa actual.")
    lines += ["", "## Capítulos", "",
              "| Cap. | Título | Estado | Audio generado |", "|---|---|---|---|"]
    lines += [f"| {r['capitulo']} | {r['titulo']} | {r['estado']} | {r['audio']} |" for r in rows]
    lines += ["", "## Historial", ""]
    lines += [f"- {when} · {label} · {event}" for when, label, event in reversed(history)]
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Bitácora: {len(pending)} sin audio al día — {md_path.relative_to(VAULT_ROOT)}")


if __name__ == "__main__":
    main()
