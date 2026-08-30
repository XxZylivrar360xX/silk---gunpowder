"""Métricas conservadoras de diálogo sin atribución de hablante."""

from __future__ import annotations

import re
from dataclasses import dataclass
from statistics import mean, median
from typing import Any

from .common import Alert, ChapterDocument, excerpt, words


DEFAULT_INCISE_RE = re.compile(
    r"^(?:[A-ZÁÉÍÓÚÜÑ][\wÁÉÍÓÚÜÑáéíóúüñ'’.-]*\s+)?"
    r"(?:dijo|preguntó|respondió|contestó|añadió|replicó|murmuró|susurró|"
    r"gritó|advirtió|explicó|insistió|continuó|prosiguió|aclaró|señaló|"
    r"hizo|miró|sonrió|rió|asintió|negó|encogió|levantó|bajó|tomó|soltó)\b",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class DialogueEstimate:
    """Estimación conservadora: ante ambigüedad, no suma el segmento como hablado."""

    dialogue_paragraph_words_raw: int
    spoken_words_estimate: int
    spoken_segments: tuple[str, ...]
    narrative_segments: tuple[str, ...]
    ambiguous_segments: tuple[str, ...]


def estimate_spoken_segments(text: str, config: dict[str, Any] | None = None) -> DialogueEstimate:
    """Separa habla e incisos con rayas sin pretender resolver atribución o NLP."""
    config = config or {}
    stripped = text.strip()
    raw = len(words(stripped[1:] if stripped.startswith("—") else stripped))
    if not stripped.startswith("—"):
        return DialogueEstimate(raw, 0, (), (), (stripped,) if stripped else ())

    body = stripped[1:]
    parts = [part.strip() for part in body.split("—")]
    spoken: list[str] = [parts[0]] if parts and parts[0] else []
    narrative: list[str] = []
    ambiguous: list[str] = []
    incise_patterns = [DEFAULT_INCISE_RE]
    for pattern in config.get("dialogue_incise_patterns", []):
        incise_patterns.append(re.compile(str(pattern), re.IGNORECASE))

    last_was_incise = False
    for index, part in enumerate(parts[1:], start=1):
        if not part:
            continue
        if index % 2 == 1:
            is_incise = any(pattern.search(part) for pattern in incise_patterns)
            if is_incise:
                narrative.append(part)
                last_was_incise = True
            else:
                ambiguous.append(part)
                last_was_incise = False
        elif last_was_incise:
            spoken.append(part)
        else:
            ambiguous.append(part)

    return DialogueEstimate(
        dialogue_paragraph_words_raw=raw,
        spoken_words_estimate=sum(len(words(segment)) for segment in spoken),
        spoken_segments=tuple(spoken),
        narrative_segments=tuple(narrative),
        ambiguous_segments=tuple(ambiguous),
    )


def analyze(document: ChapterDocument, config: dict[str, Any]) -> tuple[dict[str, Any], list[Alert]]:
    interventions = [item for item in document.prose_lines if item.text.lstrip().startswith("—")]
    estimates = [estimate_spoken_segments(item.text, config) for item in interventions]
    raw_lengths = [item.dialogue_paragraph_words_raw for item in estimates]
    spoken_lengths = [item.spoken_words_estimate for item in estimates]
    total_words = max(1, len(words(document.prose_text)))
    dialogue_words_raw = sum(raw_lengths)
    spoken_words = sum(spoken_lengths)
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
        "dialogue_paragraph_words_raw": dialogue_words_raw,
        "spoken_words_estimate": spoken_words,
        "words_per_intervention_mean": round(mean(spoken_lengths), 3) if spoken_lengths else 0.0,
        "words_per_intervention_median": round(float(median(spoken_lengths)), 3) if spoken_lengths else 0.0,
        "words_per_intervention_max": max(spoken_lengths, default=0),
        "raw_words_per_intervention_max": max(raw_lengths, default=0),
        "over_thresholds": {
            str(value): sum(1 for length in spoken_lengths if length > value) for value in thresholds
        },
        "dialogue_words_approx": spoken_words,
        "dialogue_percent_approx": round(spoken_words * 100 / total_words, 3),
        "max_exchange_without_action": longest_run,
        "intervention_estimates": [
            {
                "line": item.number,
                "dialogue_paragraph_words_raw": estimate.dialogue_paragraph_words_raw,
                "spoken_words_estimate": estimate.spoken_words_estimate,
                "narrative_segments": list(estimate.narrative_segments),
                "ambiguous_segments": list(estimate.ambiguous_segments),
            }
            for item, estimate in zip(interventions, estimates)
        ],
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
                confidence="compound",
            )
        )
    long_threshold = thresholds[1] if len(thresholds) > 1 else thresholds[0]
    for item, estimate, length in zip(interventions, estimates, spoken_lengths):
        if length > long_threshold:
            alerts.append(
                Alert(
                    check_id="LONG_DIALOGUE_INTERVENTION",
                    severity="low" if length <= thresholds[-1] else "medium",
                    chapter=document.filename,
                    line=item.number,
                    excerpt=excerpt(item.text),
                    message=(
                        f"Intervención estimada en {length} palabras habladas; "
                        "la longitud aislada nunca eleva a HIGH."
                    ),
                    metric={
                        "spoken_words_estimate": length,
                        "dialogue_paragraph_words_raw": estimate.dialogue_paragraph_words_raw,
                    },
                    category="dialogue",
                )
            )

    strong_words = int(config.get("long_dialogue_cluster_min_words", 60))
    strong_count = int(config.get("long_dialogue_cluster_count", 2))
    line_window = int(config.get("long_dialogue_cluster_line_window", 12))
    weak_words = int(config.get("long_dialogue_cluster_weak_words", 45))
    candidates = [
        (item, length)
        for item, length in zip(interventions, spoken_lengths)
        if length > weak_words
    ]
    clusters: list[list[tuple[Any, int]]] = []
    index = 0
    while index < len(candidates):
        cluster = [candidates[index]]
        cursor = index + 1
        while cursor < len(candidates) and candidates[cursor][0].number - candidates[index][0].number <= line_window:
            cluster.append(candidates[cursor])
            cursor += 1
        if len(cluster) >= 2:
            clusters.append(cluster)
        index = cursor if cursor > index + 1 else index + 1

    metrics["long_dialogue_clusters"] = [
        {
            "lines": [item.number for item, _ in cluster],
            "spoken_words_estimate": [length for _, length in cluster],
        }
        for cluster in clusters
    ]
    for cluster in clusters:
        strong = [(item, length) for item, length in cluster if length > strong_words]
        severity = "high" if len(strong) >= strong_count else "medium"
        selected = strong if severity == "high" else cluster
        alerts.append(
            Alert(
                check_id="LONG_DIALOGUE_CLUSTER",
                severity=severity,
                chapter=document.filename,
                line=selected[0][0].number,
                excerpt=excerpt(" / ".join(item.text for item, _ in selected[:3])),
                message=(
                    f"Cluster de {len(selected)} intervenciones largas dentro de una ventana "
                    f"de {line_window} líneas."
                ),
                metric={
                    "lines": [item.number for item, _ in selected],
                    "spoken_words_estimate": [length for _, length in selected],
                    "line_window": line_window,
                },
                category="dialogue",
                confidence="compound",
            )
        )
    return metrics, alerts
