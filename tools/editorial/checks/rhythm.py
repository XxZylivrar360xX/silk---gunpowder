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

    short_runs: list[list[Any]] = []
    current: list[Any] = []
    for item, count in zip(document.prose_lines, paragraph_counts):
        if count <= short_limit:
            current.append(item)
        else:
            if current:
                short_runs.append(current)
            current = []
    if current:
        short_runs.append(current)
    max_run_lines = max(short_runs, key=len, default=[])
    max_run = len(max_run_lines)

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
        "short_paragraph_clusters": [],
        "paragraph_size_distribution": distribution,
    }
    alerts: list[Alert] = []
    dialogue_ratio = float(config.get("short_cluster_dialogue_ratio", 0.67))
    narrative_ratio = float(config.get("short_cluster_narrative_ratio", 0.25))
    mixed_medium = int(config.get("short_mixed_cluster_medium", 20))
    narrative_high = int(config.get("short_narrative_cluster_high", 20))
    for run in short_runs:
        if len(run) < run_warning:
            continue
        ratio = sum(item.text.lstrip().startswith("—") for item in run) / len(run)
        if ratio >= dialogue_ratio:
            check_id = "SHORT_DIALOGUE_CLUSTER"
            severity = "low" if len(run) >= run_high else "info"
            kind = "dialogue"
        elif ratio <= narrative_ratio:
            check_id = "SHORT_NARRATIVE_CLUSTER"
            severity = "high" if len(run) >= narrative_high else "medium"
            kind = "narrative"
        else:
            check_id = "SHORT_MIXED_CLUSTER"
            severity = "medium" if len(run) >= mixed_medium else "low"
            kind = "mixed"
        cluster_metric = {
            "run": len(run),
            "threshold_words": short_limit,
            "dialogue_ratio": round(ratio, 3),
            "kind": kind,
            "start_line": run[0].number,
            "end_line": run[-1].number,
        }
        metrics["short_paragraph_clusters"].append(cluster_metric)
        alerts.append(
            Alert(
                check_id=check_id,
                severity=severity,
                chapter=document.filename,
                line=run[0].number,
                excerpt=excerpt(" / ".join(item.text for item in run[:4])),
                message=(
                    f"Secuencia {kind} de {len(run)} párrafos de {short_limit} palabras o menos; "
                    "revisar la cadencia, no uniformarla."
                ),
                metric=cluster_metric,
                category="rhythm",
                confidence="high-confidence" if severity == "high" else "descriptive/inventory",
            )
        )
    return metrics, alerts
