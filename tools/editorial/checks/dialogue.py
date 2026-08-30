"""Métricas conservadoras de diálogo sin atribución de hablante."""

from __future__ import annotations

from statistics import mean, median
from typing import Any

from .common import Alert, ChapterDocument, excerpt, words


def analyze(document: ChapterDocument, config: dict[str, Any]) -> tuple[dict[str, Any], list[Alert]]:
    interventions = [item for item in document.prose_lines if item.text.lstrip().startswith("—")]
    lengths = [len(words(item.text.lstrip()[1:])) for item in interventions]
    total_words = max(1, len(words(document.prose_text)))
    dialogue_words = sum(lengths)
    thresholds = sorted(int(value) for value in config.get("dialogue_word_thresholds", [25, 40, 60]))

    longest_run = 0
    longest_lines: list[Any] = []
    current: list[Any] = []
    for item in document.prose_lines:
        if item.text.lstrip().startswith("—"):
            current.append(item)
            if len(current) > longest_run:
                longest_run = len(current)
                longest_lines = list(current)
        else:
            current = []

    metrics = {
        "interventions": len(interventions),
        "words_per_intervention_mean": round(mean(lengths), 3) if lengths else 0.0,
        "words_per_intervention_median": round(float(median(lengths)), 3) if lengths else 0.0,
        "words_per_intervention_max": max(lengths, default=0),
        "over_thresholds": {str(value): sum(1 for length in lengths if length > value) for value in thresholds},
        "dialogue_words_approx": dialogue_words,
        "dialogue_percent_approx": round(dialogue_words * 100 / total_words, 3),
        "max_exchange_without_action": longest_run,
    }
    alerts: list[Alert] = []
    medium_threshold = int(config.get("long_exchange_warning", 8))
    high_threshold = int(config.get("long_exchange_high", 14))
    if longest_run >= medium_threshold:
        alerts.append(
            Alert(
                check_id="DIALOGUE_EXCHANGE_WITHOUT_ACTION",
                severity="high" if longest_run >= high_threshold else "medium",
                chapter=document.filename,
                line=longest_lines[0].number if longest_lines else None,
                excerpt=excerpt(" / ".join(item.text for item in longest_lines[:4])),
                message="Intercambio prolongado de párrafos de diálogo sin párrafo narrativo intermedio.",
                metric={"interventions": longest_run},
                category="dialogue",
            )
        )
    long_threshold = thresholds[1] if len(thresholds) > 1 else thresholds[0]
    for item, length in zip(interventions, lengths):
        if length > long_threshold:
            alerts.append(
                Alert(
                    check_id="LONG_DIALOGUE_INTERVENTION",
                    severity="medium" if length <= thresholds[-1] else "high",
                    chapter=document.filename,
                    line=item.number,
                    excerpt=excerpt(item.text),
                    message=f"Intervención de diálogo de {length} palabras; posible outlier para lectura humana.",
                    metric={"words": length},
                    category="dialogue",
                )
            )
    return metrics, alerts

