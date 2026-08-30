"""Métricas aproximadas de ritmo y párrafo."""

from __future__ import annotations

from statistics import mean, median
from typing import Any

from .common import Alert, ChapterDocument, approximate_sentences, excerpt, words


def _safe_mean(values: list[int]) -> float:
    return round(mean(values), 3) if values else 0.0


def _safe_median(values: list[int]) -> float:
    return round(float(median(values)), 3) if values else 0.0


def analyze(document: ChapterDocument, config: dict[str, Any]) -> tuple[dict[str, Any], list[Alert]]:
    paragraph_counts = [len(words(item.text)) for item in document.prose_lines]
    sentence_counts = [len(words(sentence)) for sentence in approximate_sentences(document.prose_text)]
    short_limit = int(config.get("short_paragraph_words", 8))
    run_warning = int(config.get("short_paragraph_run_warning", 6))
    run_high = int(config.get("short_paragraph_run_high", 10))
    single_sentence = sum(1 for item in document.prose_lines if len(approximate_sentences(item.text)) == 1)

    max_run = 0
    current: list[Any] = []
    max_run_lines: list[Any] = []
    for item, count in zip(document.prose_lines, paragraph_counts):
        if count <= short_limit:
            current.append(item)
            if len(current) > max_run:
                max_run = len(current)
                max_run_lines = list(current)
        else:
            current = []

    distribution = {"1_5": 0, "6_10": 0, "11_20": 0, "21_40": 0, "41_plus": 0}
    for count in paragraph_counts:
        if count <= 5:
            distribution["1_5"] += 1
        elif count <= 10:
            distribution["6_10"] += 1
        elif count <= 20:
            distribution["11_20"] += 1
        elif count <= 40:
            distribution["21_40"] += 1
        else:
            distribution["41_plus"] += 1

    metrics = {
        "words": sum(paragraph_counts),
        "paragraphs": len(paragraph_counts),
        "sentences_approx": len(sentence_counts),
        "words_per_sentence_mean": _safe_mean(sentence_counts),
        "words_per_sentence_median": _safe_median(sentence_counts),
        "words_per_paragraph_mean": _safe_mean(paragraph_counts),
        "words_per_paragraph_median": _safe_median(paragraph_counts),
        "single_sentence_paragraph_percent": round(single_sentence * 100 / max(1, len(paragraph_counts)), 3),
        "short_paragraph_words_threshold": short_limit,
        "short_paragraphs": sum(1 for value in paragraph_counts if value <= short_limit),
        "max_consecutive_short_paragraphs": max_run,
        "paragraph_size_distribution": distribution,
    }
    alerts: list[Alert] = []
    if max_run >= run_warning:
        severity = "high" if max_run >= run_high else "medium"
        alerts.append(
            Alert(
                check_id="SHORT_PARAGRAPH_CLUSTER",
                severity=severity,
                chapter=document.filename,
                line=max_run_lines[0].number if max_run_lines else None,
                excerpt=excerpt(" / ".join(item.text for item in max_run_lines[:4])),
                message=f"Secuencia de {max_run} párrafos de {short_limit} palabras o menos; revisar la cadencia, no uniformarla.",
                metric={"run": max_run, "threshold_words": short_limit},
                category="rhythm",
            )
        )
    return metrics, alerts

