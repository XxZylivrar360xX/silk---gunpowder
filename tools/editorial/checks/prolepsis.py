"""Candidatos a prolepsis de narrador y presagio garantizado (EDITORIAL_POLICY §L).

Separa cada línea en segmentos por contexto (narración, inciso de diálogo,
parlamento, cita entrecomillada, cursiva) y aplica patrones sólo a los
contextos donde habla el narrador. La prolepsis de personaje (lo que el POV
cree, teme o amenaza) es lícita y se excluye por defecto.
"""

from __future__ import annotations

import re
from typing import Any

from .common import Alert, ChapterDocument, excerpt, normalize_text

FUERZA_A_SEVERIDAD = {"fuerte": "medium", "media": "low", "debil": "info"}
BAJAR = {"medium": "low", "low": "info", "info": "info"}

QUOTE_RE = re.compile(r"«[^»]*»|“[^”]*”|\"[^\"]*\"")
ITALIC_RE = re.compile(r"(?<![*\w])\*(?!\*)([^*]+)\*(?!\*)|(?<![_\w])_([^_]+)_(?![_\w])")
SENTENCE_END = ".!?…"


def _normalize_with_map(text: str) -> tuple[str, list[int]]:
    """Normaliza conservando, para cada carácter normalizado, su índice original."""
    out: list[str] = []
    index_map: list[int] = []
    for position, char in enumerate(text):
        norm = normalize_text(char)
        for piece in norm:
            out.append(piece)
            index_map.append(position)
    return "".join(out), index_map


def _clean_markup(text: str) -> str:
    text = re.sub(r"!?\[\[[^\]|]*\|([^\]]+)\]\]", r"\1", text)
    text = re.sub(r"!?\[\[([^\]]+)\]\]", r"\1", text)
    text = re.sub(r"^\s*>\s?", "", text)
    return text


def segments(raw_line: str) -> list[tuple[str, str]]:
    """Devuelve [(contexto, texto)] para una línea de manuscrito."""
    line = _clean_markup(raw_line).strip()
    result: list[tuple[str, str]] = []
    if line.startswith("—"):
        parts = line.split("—")
        for index, part in enumerate(parts):
            if not part.strip():
                continue
            context = "dialogo" if index % 2 == 1 else "inciso"
            result.extend(_split_inner(part, context))
        return result
    return _split_inner(line, "narracion")


def _split_inner(text: str, base: str) -> list[tuple[str, str]]:
    """Separa citas y cursivas dentro de un segmento de narración o inciso."""
    if base == "dialogo":
        return [("dialogo", text.replace("*", "").replace("_", " "))]
    spans: list[tuple[int, int, str]] = []
    for match in QUOTE_RE.finditer(text):
        spans.append((match.start(), match.end(), "cita"))
    for match in ITALIC_RE.finditer(text):
        if not any(s <= match.start() < e for s, e, _ in spans):
            spans.append((match.start(), match.end(), "cursiva"))
    spans.sort()
    out: list[tuple[str, str]] = []
    cursor = 0
    for start, end, context in spans:
        if start > cursor:
            out.append((base, text[cursor:start]))
        out.append((context, text[start:end].strip("*_")))
        cursor = end
    if cursor < len(text):
        out.append((base, text[cursor:]))
    return [(c, t.replace("*", "")) for c, t in out if t.strip()]


def _sentence_around(text: str, start: int, end: int) -> str:
    left = max((text.rfind(ch, 0, start) for ch in SENTENCE_END), default=-1)
    right_candidates = [pos for pos in (text.find(ch, end) for ch in SENTENCE_END) if pos != -1]
    right = min(right_candidates) + 1 if right_candidates else len(text)
    return text[left + 1 : right].strip()


def compile_patterns(config: dict[str, Any]) -> list[dict[str, Any]]:
    compiled = []
    for rule in config.get("patrones", []):
        compiled.append({**rule, "compiled": re.compile(rule["regex"], re.IGNORECASE)})
    return compiled


def analyze(
    document: ChapterDocument,
    config: dict[str, Any],
    *,
    incluir_dialogo: bool = False,
    patterns: list[dict[str, Any]] | None = None,
) -> tuple[dict[str, Any], list[Alert]]:
    patterns = patterns if patterns is not None else compile_patterns(config)
    reported = set(config.get("contextos_reportados", ["narracion", "inciso", "cursiva"]))
    lowered = set(config.get("contextos_rebajados", ["cursiva"]))
    if incluir_dialogo:
        reported |= {"dialogo", "cita"}
        lowered |= {"dialogo", "cita"}

    raw_lines = document.raw_text.splitlines()
    alerts: list[Alert] = []
    counts: dict[str, int] = {}
    for prose_line in document.prose_lines:
        raw_line = raw_lines[prose_line.number - 1]
        seen: set[tuple[str, str]] = set()
        for context, text in segments(raw_line):
            if context not in reported:
                continue
            normalized, index_map = _normalize_with_map(text)
            for rule in patterns:
                for match in rule["compiled"].finditer(normalized):
                    if not index_map:
                        continue
                    start = index_map[match.start()]
                    end = index_map[max(match.end() - 1, match.start())] + 1
                    sentence = _sentence_around(text, start, end)
                    key = (rule["id"], sentence)
                    if key in seen:
                        continue
                    seen.add(key)
                    severity = FUERZA_A_SEVERIDAD[rule["fuerza"]]
                    if context in lowered:
                        severity = BAJAR[severity]
                    counts[rule["id"]] = counts.get(rule["id"], 0) + 1
                    alerts.append(
                        Alert(
                            check_id=rule["id"],
                            severity=severity,
                            chapter=document.filename,
                            line=prose_line.number,
                            excerpt=excerpt(sentence, 260),
                            message=rule["mensaje"],
                            metric={
                                "familia": rule["familia"],
                                "fuerza": rule["fuerza"],
                                "contexto": context,
                                "coincidencia": text[start:end],
                            },
                            category="prolepsis",
                        )
                    )
    return {"prolepsis_candidates": len(alerts), "by_pattern": counts}, alerts
