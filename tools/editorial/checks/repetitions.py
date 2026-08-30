"""Frases vigiladas y n-gramas repetidos."""

from __future__ import annotations

import re
from collections import Counter, defaultdict
from typing import Any

from .common import Alert, ChapterDocument, excerpt, normalize_text, words


def _phrase_occurrences(document: ChapterDocument, phrase: str) -> list[tuple[int, str]]:
    pattern = re.compile(rf"(?<!\w){re.escape(normalize_text(phrase))}(?!\w)")
    matches: list[tuple[int, str]] = []
    for prose_line in document.prose_lines:
        for _ in pattern.finditer(normalize_text(prose_line.text)):
            matches.append((prose_line.number, prose_line.text))
    return matches


def analyze_phrases(document: ChapterDocument, config: dict[str, Any]) -> tuple[dict[str, Any], list[Alert]]:
    total_words = max(1, len(words(document.prose_text)))
    metrics: dict[str, Any] = {}
    alerts: list[Alert] = []
    for phrase, rule in config.get("phrases", {}).items():
        found = _phrase_occurrences(document, phrase)
        if not found:
            continue
        count = len(found)
        threshold = int(rule.get("chapter_threshold", 2))
        base_severity = rule.get("severity", "low")
        severity = base_severity if count >= threshold else rule.get("isolated_severity", "info")
        density = count * 1000 / total_words
        line_numbers = [line for line, _ in found]
        metrics[phrase] = {
            "count": count,
            "lines": line_numbers,
            "density_per_1000_words": round(density, 3),
        }
        alerts.append(
            Alert(
                check_id="PHRASE_" + re.sub(r"[^A-Z0-9]+", "_", normalize_text(phrase).upper()).strip("_"),
                severity=severity,
                chapter=document.filename,
                line=found[0][0],
                excerpt=excerpt(found[0][1]),
                message=f"Frase vigilada: {count} ocurrencia(s) en el capítulo; revisar en contexto.",
                metric=metrics[phrase],
                category="repetitions",
            )
        )
    return metrics, alerts


def _is_noisy_ngram(ngram: tuple[str, ...], stopwords: set[str], exclusions: list[str]) -> bool:
    if all(token in stopwords for token in ngram):
        return True
    content = [token for token in ngram if token not in stopwords]
    if len(content) < 2:
        return True
    joined = " ".join(ngram)
    if any(re.search(pattern, joined) for pattern in exclusions):
        return True
    if len(set(ngram)) == 1:
        return True
    return False


def collect_ngrams(
    document: ChapterDocument, config: dict[str, Any], stopwords: set[str]
) -> dict[int, Counter[tuple[str, ...]]]:
    tokens = words(document.prose_text, normalized=True)
    exclusions = config.get("ngram_exclusions", [])
    result: dict[int, Counter[tuple[str, ...]]] = {}
    for length in config.get("ngram_lengths", [3, 4, 5, 6, 7, 8]):
        counter: Counter[tuple[str, ...]] = Counter()
        for index in range(len(tokens) - length + 1):
            ngram = tuple(tokens[index : index + length])
            if not _is_noisy_ngram(ngram, stopwords, exclusions):
                counter[ngram] += 1
        result[int(length)] = counter
    return result


def repeated_ngram_metrics(
    document: ChapterDocument,
    config: dict[str, Any],
    stopwords: set[str],
) -> tuple[list[dict[str, Any]], list[Alert], dict[int, Counter[tuple[str, ...]]]]:
    counters = collect_ngrams(document, config, stopwords)
    minimum = int(config.get("ngram_min_count_chapter", 3))
    report_limit = int(config.get("limits", {}).get("ngrams_per_chapter", 12))
    rows: list[dict[str, Any]] = []
    alerts: list[Alert] = []
    candidates: list[tuple[int, int, tuple[str, ...]]] = []
    for length, counter in counters.items():
        for ngram, count in counter.items():
            if count >= minimum:
                candidates.append((count, length, ngram))
    candidates.sort(key=lambda item: (-item[0], -item[1], item[2]))
    for count, length, ngram in candidates[:report_limit]:
        phrase = " ".join(ngram)
        row = {"ngram": phrase, "length": length, "count": count}
        rows.append(row)
        severity = "medium" if length >= 6 and count >= 3 else "low"
        line = next(
            (item.number for item in document.prose_lines if normalize_text(phrase) in normalize_text(item.text)),
            None,
        )
        alerts.append(
            Alert(
                check_id=f"REPEATED_NGRAM_{length}",
                severity=severity,
                chapter=document.filename,
                line=line,
                excerpt=phrase,
                message=f"N-grama de {length} palabras repetido {count} veces en el capítulo.",
                metric=row,
                category="repetitions",
            )
        )
    return rows, alerts, counters


def merge_ngram_counters(
    chapter_counters: list[dict[int, Counter[tuple[str, ...]]]], config: dict[str, Any]
) -> list[dict[str, Any]]:
    totals: dict[int, Counter[tuple[str, ...]]] = defaultdict(Counter)
    for counters in chapter_counters:
        for length, counter in counters.items():
            totals[length].update(counter)
    minimum = int(config.get("ngram_min_count_global", 4))
    limit = int(config.get("limits", {}).get("global_ngrams", 30))
    rows = [
        {"ngram": " ".join(ngram), "length": length, "count": count}
        for length, counter in totals.items()
        for ngram, count in counter.items()
        if count >= minimum
    ]
    rows.sort(key=lambda row: (-row["count"], -row["length"], row["ngram"]))
    return rows[:limit]

