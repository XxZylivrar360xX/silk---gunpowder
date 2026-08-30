"""Similaridad experimental y determinista entre pasajes de capítulos distintos."""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations
from typing import Any

from .common import Alert, ChapterDocument, excerpt, normalize_text, words


def _content_tokens(text: str, stopwords: set[str], excluded: set[str]) -> list[str]:
    return [
        token
        for token in words(text, normalized=True)
        if token not in stopwords and token not in excluded and len(token) > 2
    ]


def _jaccard(left: set[Any], right: set[Any]) -> float:
    return len(left & right) / len(left | right) if left or right else 0.0


def analyze(
    documents: list[ChapterDocument], config: dict[str, Any], stopwords: set[str]
) -> tuple[list[dict[str, Any]], dict[str, list[Alert]]]:
    minimum_words = int(config.get("passage_similarity_min_words", 35))
    minimum_content = int(config.get("passage_similarity_min_content_words", 12))
    minimum_shared = int(config.get("passage_similarity_min_shared_words", 7))
    info_threshold = float(config.get("passage_similarity_info_threshold", 0.20))
    medium_threshold = float(config.get("passage_similarity_medium_threshold", 0.32))
    shingle_size = int(config.get("passage_similarity_shingle_size", 2))
    excluded = {normalize_text(value) for value in config.get("passage_similarity_excluded_terms", [])}
    passages: list[dict[str, Any]] = []
    for document in documents:
        for prose_line in document.prose_lines:
            if len(words(prose_line.text)) < minimum_words:
                continue
            tokens = _content_tokens(prose_line.text, stopwords, excluded)
            if len(tokens) < minimum_content:
                continue
            passages.append(
                {
                    "chapter": document.filename,
                    "line": prose_line.number,
                    "text": prose_line.text,
                    "tokens": tokens,
                    "words": set(tokens),
                    "shingles": {
                        tuple(tokens[index:index + shingle_size])
                        for index in range(max(0, len(tokens) - shingle_size + 1))
                    },
                }
            )

    rows: list[dict[str, Any]] = []
    alerts: dict[str, list[Alert]] = defaultdict(list)
    for left, right in combinations(passages, 2):
        if left["chapter"] == right["chapter"]:
            continue
        shared = left["words"] & right["words"]
        if len(shared) < minimum_shared:
            continue
        word_score = _jaccard(left["words"], right["words"])
        shingle_score = _jaccard(left["shingles"], right["shingles"])
        score = 0.75 * word_score + 0.25 * shingle_score
        if score < info_threshold:
            continue
        severity = "medium" if score >= medium_threshold else "info"
        row = {
            "chapter_a": left["chapter"],
            "line_a": left["line"],
            "chapter_b": right["chapter"],
            "line_b": right["line"],
            "score": round(score, 4),
            "word_jaccard": round(word_score, 4),
            "shingle_jaccard": round(shingle_score, 4),
            "shared_content_words": sorted(shared),
            "excerpt_a": excerpt(left["text"], 220),
            "excerpt_b": excerpt(right["text"], 220),
            "severity": severity,
            "experimental": True,
        }
        rows.append(row)
        alerts[right["chapter"]].append(
            Alert(
                check_id="CROSS_CHAPTER_PASSAGE_SIMILARITY",
                severity=severity,
                chapter=right["chapter"],
                line=right["line"],
                excerpt=row["excerpt_b"],
                message=(
                    f"Posible similitud con {left['chapter']}:{left['line']} "
                    f"(score {row['score']:.4f}); señal experimental."
                ),
                metric=row,
                category="similarity",
            )
        )
    rows.sort(key=lambda row: (-row["score"], row["chapter_a"], row["line_a"], row["chapter_b"], row["line_b"]))
    return rows, dict(alerts)
