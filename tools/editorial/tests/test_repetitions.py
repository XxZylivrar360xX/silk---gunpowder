from __future__ import annotations

import json
import unittest
from pathlib import Path

from tools.editorial.checks import repetitions
from tools.editorial.checks.common import parse_chapter_text


ROOT = Path(__file__).resolve().parents[3]
CONFIG = json.loads((ROOT / "tools/editorial/editorial_config.json").read_text(encoding="utf-8"))
CASES = json.loads((Path(__file__).with_name("known_cases.json")).read_text(encoding="utf-8"))


def document_for(text: str):
    raw = "<!-- metadata -->\n# Capítulo 1 — Caso\n\n" + text + "\n"
    return parse_chapter_text(raw, Path("virtual/01_Caso.md"), Path("virtual"))


class RepetitionChecksTest(unittest.TestCase):
    def test_repeated_known_tic_is_counted_and_alerted(self) -> None:
        case = next(item for item in CASES["should_alert"] if item["id"] == "repeated_tic")
        metrics, alerts = repetitions.analyze_phrases(document_for(case["text"]), CONFIG)
        self.assertEqual(metrics["un segundo de más"]["count"], 3)
        self.assertIn(case["expected_check"], {alert.check_id for alert in alerts})

    def test_isolated_como_si_stays_info(self) -> None:
        document = document_for("La sostuvo como si pesara poco.")
        metrics, alerts = repetitions.analyze_phrases(document, CONFIG)
        self.assertEqual(metrics["como si"]["count"], 1)
        alert = next(item for item in alerts if item.check_id == "PHRASE_COMO_SI")
        self.assertEqual(alert.severity, "info")

    def test_function_word_ngram_is_filtered(self) -> None:
        local_config = dict(CONFIG)
        local_config["ngram_lengths"] = [3]
        document = document_for("de la que de la que de la que")
        counters = repetitions.collect_ngrams(document, local_config, {"de", "la", "que"})
        self.assertFalse(counters[3])


if __name__ == "__main__":
    unittest.main()
