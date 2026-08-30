"""Tipos y utilidades compartidas por los checks editoriales."""

from __future__ import annotations

import re
import unicodedata
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Iterable


WORD_RE = re.compile(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+(?:['’][A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+)?", re.UNICODE)
SENTENCE_RE = re.compile(r"(?<=[.!?…])(?:[\"”’»)]*)\s+(?=[—\"“«¿¡A-ZÁÉÍÓÚÜÑ])")
SEPARATOR_RE = re.compile(r"^\s*(?:\*{3,}|-{3,}|_{3,})\s*$")
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+")
OBSIDIAN_LINK_RE = re.compile(r"!?(?:\[\[[^\]]+\]\])")
SEVERITY_ORDER = {"info": 0, "low": 1, "medium": 2, "high": 3}


@dataclass(frozen=True)
class ProseLine:
    number: int
    text: str


@dataclass
class Alert:
    check_id: str
    severity: str
    chapter: str
    line: int | None
    excerpt: str
    message: str
    metric: dict[str, Any] = field(default_factory=dict)
    category: str = "general"

    def __post_init__(self) -> None:
        if self.severity not in SEVERITY_ORDER:
            raise ValueError(f"Severidad no permitida: {self.severity}")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class ChapterDocument:
    path: Path
    relative_path: str
    filename: str
    raw_text: str
    metadata: str
    metadata_start_line: int | None
    metadata_end_line: int | None
    title: str | None
    title_line: int | None
    prose_lines: list[ProseLine]
    internal_comments: list[tuple[int, str]]
    unexpected_headings: list[tuple[int, str]]

    @property
    def prose_text(self) -> str:
        return "\n".join(line.text for line in self.prose_lines)


def normalize_text(text: str) -> str:
    """Normaliza mayúsculas y diacríticos para comparaciones, no para reportes."""
    decomposed = unicodedata.normalize("NFD", text.casefold())
    return "".join(char for char in decomposed if unicodedata.category(char) != "Mn")


def words(text: str, *, normalized: bool = False) -> list[str]:
    found = WORD_RE.findall(text)
    if normalized:
        return [normalize_text(word) for word in found]
    return found


def excerpt(text: str, limit: int = 180) -> str:
    compact = re.sub(r"\s+", " ", text).strip()
    if len(compact) <= limit:
        return compact
    return compact[: limit - 1].rstrip() + "…"


def strip_markdown_for_metrics(text: str) -> str:
    text = OBSIDIAN_LINK_RE.sub(" ", text)
    text = re.sub(r"^\s*>\s?", "", text)
    text = re.sub(r"[*_`]", "", text)
    return text.strip()


def parse_chapter(path: Path, repo_root: Path) -> ChapterDocument:
    raw = path.read_text(encoding="utf-8-sig")
    return parse_chapter_text(raw, path, repo_root)


def parse_chapter_text(raw: str, path: Path, repo_root: Path) -> ChapterDocument:
    """Parsea texto ya cargado; útil para pruebas sin escribir fixtures al disco."""
    lines = raw.splitlines()
    metadata = ""
    metadata_start: int | None = None
    metadata_end: int | None = None
    consumed_metadata: set[int] = set()

    first_nonblank = next((i for i, value in enumerate(lines) if value.strip()), None)
    if first_nonblank is not None and lines[first_nonblank].lstrip().startswith("<!--"):
        metadata_start = first_nonblank + 1
        block: list[str] = []
        for index in range(first_nonblank, len(lines)):
            block.append(lines[index])
            consumed_metadata.add(index)
            if "-->" in lines[index]:
                metadata_end = index + 1
                break
        metadata = "\n".join(block)

    title: str | None = None
    title_line: int | None = None
    prose_lines: list[ProseLine] = []
    internal_comments: list[tuple[int, str]] = []
    unexpected_headings: list[tuple[int, str]] = []
    in_internal_comment = False
    comment_start = 0
    comment_parts: list[str] = []

    for index, raw_line in enumerate(lines):
        if index in consumed_metadata:
            continue
        stripped = raw_line.strip()
        if in_internal_comment:
            comment_parts.append(raw_line)
            if "-->" in raw_line:
                internal_comments.append((comment_start, "\n".join(comment_parts)))
                in_internal_comment = False
                comment_parts = []
            continue
        if "<!--" in raw_line:
            comment_start = index + 1
            comment_parts = [raw_line]
            if "-->" in raw_line[raw_line.index("<!--") + 4 :]:
                internal_comments.append((comment_start, raw_line))
                comment_parts = []
            else:
                in_internal_comment = True
            continue
        if not stripped or SEPARATOR_RE.match(stripped):
            continue
        if HEADING_RE.match(raw_line):
            if title is None and re.match(r"^\s*#\s+", raw_line):
                title = HEADING_RE.sub("", raw_line).strip()
                title_line = index + 1
            else:
                unexpected_headings.append((index + 1, stripped))
            continue
        cleaned = strip_markdown_for_metrics(raw_line)
        if cleaned:
            prose_lines.append(ProseLine(index + 1, cleaned))

    if in_internal_comment:
        internal_comments.append((comment_start, "\n".join(comment_parts)))

    return ChapterDocument(
        path=path,
        relative_path=path.relative_to(repo_root).as_posix(),
        filename=path.name,
        raw_text=raw,
        metadata=metadata,
        metadata_start_line=metadata_start,
        metadata_end_line=metadata_end,
        title=title,
        title_line=title_line,
        prose_lines=prose_lines,
        internal_comments=internal_comments,
        unexpected_headings=unexpected_headings,
    )


def narrative_paragraphs(document: ChapterDocument) -> list[ProseLine]:
    """Cada línea no vacía del manuscrito funciona como párrafo Markdown."""
    return document.prose_lines


def approximate_sentences(text: str) -> list[str]:
    compact = re.sub(r"\s+", " ", text).strip()
    if not compact:
        return []
    return [item.strip() for item in SENTENCE_RE.split(compact) if item.strip()]


def line_for_fragment(document: ChapterDocument, fragment: str) -> int | None:
    needle = normalize_text(fragment)
    for prose_line in document.prose_lines:
        if needle in normalize_text(prose_line.text):
            return prose_line.number
    return None


def severity_at_least(severity: str, minimum: str) -> bool:
    return SEVERITY_ORDER[severity] >= SEVERITY_ORDER[minimum]


def sorted_alerts(alerts: Iterable[Alert]) -> list[Alert]:
    return sorted(
        alerts,
        key=lambda alert: (
            -SEVERITY_ORDER[alert.severity],
            alert.chapter,
            alert.line if alert.line is not None else 10**9,
            alert.check_id,
        ),
    )
