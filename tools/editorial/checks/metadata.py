"""Metadata y residuos internos del manuscrito."""

from __future__ import annotations

import re
from typing import Any

from .common import Alert, ChapterDocument, excerpt


def _contains_marker(text: str, marker: str) -> bool:
    if marker in {"TODO", "FIXME"}:
        return re.search(rf"\b{marker}\b", text) is not None
    return marker.casefold() in text.casefold()


def analyze(document: ChapterDocument, config: dict[str, Any]) -> tuple[dict[str, Any], list[Alert]]:
    metrics: dict[str, Any] = {
        "metadata_present": bool(document.metadata),
        "title_present": bool(document.title),
        "metadata_markers": [],
        "prose_markers": [],
        "internal_comments": len(document.internal_comments),
        "unexpected_headings": len(document.unexpected_headings),
        "filename_title_match": None,
    }
    alerts: list[Alert] = []
    markers = config.get(
        "metadata_markers",
        ["TODO", "FIXME", "[PENDIENTE", "> **PENDIENTE", "nota de autor", "nota editorial"],
    )
    for marker in markers:
        if _contains_marker(document.metadata, marker):
            metrics["metadata_markers"].append(marker)
        for line in document.prose_lines:
            if _contains_marker(line.text, marker):
                metrics["prose_markers"].append({"marker": marker, "line": line.number})
                alerts.append(
                    Alert(
                        check_id="INTERNAL_MARKER_IN_PROSE",
                        severity="high",
                        chapter=document.filename,
                        line=line.number,
                        excerpt=excerpt(line.text),
                        message=f"Marcador interno «{marker}» fuera de la metadata inicial.",
                        category="metadata",
                    )
                )
    if not document.metadata:
        alerts.append(
            Alert(
                check_id="MISSING_INITIAL_METADATA",
                severity="medium",
                chapter=document.filename,
                line=1,
                excerpt="",
                message="No se encontró comentario HTML de metadata al inicio.",
                category="metadata",
            )
        )
    if not document.title:
        alerts.append(
            Alert(
                check_id="MISSING_MARKDOWN_TITLE",
                severity="high",
                chapter=document.filename,
                line=None,
                excerpt="",
                message="No se encontró título Markdown de nivel 1.",
                category="metadata",
            )
        )

    filename_match = re.match(r"^(\d+)_", document.filename)
    title_match = re.match(r"^Cap[ií]tulo\s+(\d+)\b", document.title or "", re.IGNORECASE)
    if filename_match and title_match:
        filename_number = int(filename_match.group(1))
        title_number = int(title_match.group(1))
        metrics["filename_title_match"] = filename_number == title_number
        if filename_number != title_number:
            alerts.append(
                Alert(
                    check_id="CHAPTER_NUMBER_MISMATCH",
                    severity="high",
                    chapter=document.filename,
                    line=document.title_line,
                    excerpt=document.title or "",
                    message=f"Filename indica capítulo {filename_number}; el título indica {title_number}.",
                    category="metadata",
                )
            )

    for line, value in document.internal_comments:
        alerts.append(
            Alert(
                check_id="INTERNAL_HTML_COMMENT",
                severity="medium",
                chapter=document.filename,
                line=line,
                excerpt=excerpt(value),
                message="Comentario HTML interno fuera del bloque de metadata inicial.",
                category="metadata",
            )
        )
    for line, value in document.unexpected_headings:
        alerts.append(
            Alert(
                check_id="UNEXPECTED_HEADING_IN_PROSE",
                severity="medium",
                chapter=document.filename,
                line=line,
                excerpt=excerpt(value),
                message="Heading inesperado dentro del cuerpo narrativo.",
                category="metadata",
            )
        )
    return metrics, alerts
