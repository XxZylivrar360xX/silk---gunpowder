"""Frecuencias léxicas, adverbios y gestos configurables."""

from __future__ import annotations

import re
from collections import Counter
from typing import Any

from .common import Alert, ChapterDocument, excerpt, normalize_text, words


def analyze(
    document: ChapterDocument, config: dict[str, Any], stopwords: set[str]
) -> tuple[dict[str, Any], list[Alert]]:
    normalized_words = words(document.prose_text, normalized=True)
    total_words = max(1, len(normalized_words))
    frequencies = Counter(word for word in normalized_words if word not in stopwords and len(word) > 2)
    top_limit = int(config.get("limits", {}).get("lexical_top", 25))
    adverbs = Counter(word for word in normalized_words if word.endswith("mente") and len(word) > 7)
    gesture_metrics: dict[str, Any] = {}
    alerts: list[Alert] = []

    for gesture in config.get("gestures", []):
        pattern = re.compile(gesture["regex"], re.IGNORECASE)
        occurrences: list[tuple[int, str]] = []
        for line in document.prose_lines:
            if pattern.search(line.text):
                occurrences.append((line.number, line.text))
        if not occurrences:
            continue
        count = len(occurrences)
        density = count * 1000 / total_words
        cluster_window = int(config.get("gesture_cluster_line_window", 20))
        cluster_threshold = int(config.get("gesture_cluster_threshold", 3))
        clusters: list[list[tuple[int, str]]] = []
        for index, occurrence in enumerate(occurrences):
            cluster = [item for item in occurrences[index:] if item[0] - occurrence[0] <= cluster_window]
            if len(cluster) >= cluster_threshold:
                clusters.append(cluster)
        gesture_metrics[gesture["id"]] = {
            "label": gesture["label"],
            "count": count,
            "density_per_1000_words": round(density, 3),
            "lines": [line for line, _ in occurrences],
            "clusters": len(clusters),
        }
        if clusters:
            first = clusters[0]
            alerts.append(
                Alert(
                    check_id="GESTURE_CLUSTER_" + gesture["id"],
                    severity=gesture.get("severity", "low"),
                    chapter=document.filename,
                    line=first[0][0],
                    excerpt=excerpt(" / ".join(item[1] for item in first[:3])),
                    message=f"El gesto «{gesture['label']}» aparece agrupado en una ventana de {cluster_window} líneas.",
                    metric=gesture_metrics[gesture["id"]],
                    category="lexical",
                )
            )

    metrics = {
        "top_words": [{"word": word, "count": count} for word, count in frequencies.most_common(top_limit)],
        "adverbs_mente": {
            "count": sum(adverbs.values()),
            "density_per_1000_words": round(sum(adverbs.values()) * 1000 / total_words, 3),
            "forms": [{"word": word, "count": count} for word, count in adverbs.most_common(top_limit)],
        },
        "gestures": gesture_metrics,
    }
    return metrics, alerts

