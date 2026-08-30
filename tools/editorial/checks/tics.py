"""Construcciones configurables y residuos de instrucción."""

from __future__ import annotations

import re
from typing import Any

from .common import Alert, ChapterDocument, approximate_sentences, excerpt


def analyze(document: ChapterDocument, config: dict[str, Any]) -> tuple[dict[str, Any], list[Alert]]:
    metrics: dict[str, Any] = {"patterns": {}}
    alerts: list[Alert] = []
    text = document.prose_text

    for rule in config.get("tic_patterns", []):
        pattern = re.compile(rule["regex"], re.IGNORECASE | re.MULTILINE | re.DOTALL)
        found = list(pattern.finditer(text))
        if not found:
            continue
        metrics["patterns"][rule["id"]] = len(found)
        for match in found[: int(config.get("limits", {}).get("occurrences_per_check", 8))]:
            fragment = match.group(0)
            line = next(
                (item.number for item in document.prose_lines if fragment[:40].strip() in item.text),
                None,
            )
            alerts.append(
                Alert(
                    check_id=rule["id"],
                    severity=rule.get("severity", "low"),
                    chapter=document.filename,
                    line=line,
                    excerpt=excerpt(fragment),
                    message=rule["message"],
                    metric={"chapter_occurrences": len(found)},
                    category="tics",
                )
            )

    negative_runs: list[dict[str, Any]] = []
    run: list[tuple[int, str]] = []
    for prose_line in document.prose_lines:
        for sentence in approximate_sentences(prose_line.text):
            if re.match(r"^[—\"“«(]*No\b", sentence, re.IGNORECASE):
                run.append((prose_line.number, sentence))
            else:
                if len(run) >= 3:
                    negative_runs.append({"line": run[0][0], "sentences": [item[1] for item in run]})
                run = []
    if len(run) >= 3:
        negative_runs.append({"line": run[0][0], "sentences": [item[1] for item in run]})
    metrics["negative_chains"] = len(negative_runs)
    for item in negative_runs:
        alerts.append(
            Alert(
                check_id="NEGATIVE_SENTENCE_CHAIN",
                severity="medium",
                chapter=document.filename,
                line=item["line"],
                excerpt=excerpt(" ".join(item["sentences"])),
                message="Tres o más oraciones consecutivas empiezan con «No»; posible cadena enfática o residuo de checklist.",
                metric={"sentences": len(item["sentences"])},
                category="tics",
            )
        )

    instruction_patterns = [re.compile(value, re.IGNORECASE) for value in config.get("editorial_instruction_patterns", [])]
    leaks = 0
    for prose_line in document.prose_lines:
        if prose_line.text.lstrip().startswith("—"):
            continue
        for pattern in instruction_patterns:
            if pattern.search(prose_line.text):
                leaks += 1
                alerts.append(
                    Alert(
                        check_id="EDITORIAL_INSTRUCTION_LEAK",
                        severity="high",
                        chapter=document.filename,
                        line=prose_line.number,
                        excerpt=excerpt(prose_line.text),
                        message="La narración parece describir una instrucción de redacción en vez de un hecho de escena.",
                        category="tics",
                    )
                )
                break
    metrics["editorial_instruction_leaks"] = leaks
    return metrics, alerts

