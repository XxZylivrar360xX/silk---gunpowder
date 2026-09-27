from __future__ import annotations

import json
import unittest
from pathlib import Path

from tools.editorial.checks import metadata, rhythm, tics
from tools.editorial.checks.common import parse_chapter_text


ROOT = Path(__file__).resolve().parents[3]
CONFIG = json.loads((ROOT / "tools/editorial/editorial_config.json").read_text(encoding="utf-8"))
CASES = json.loads((Path(__file__).with_name("known_cases.json")).read_text(encoding="utf-8"))


def document_for(text: str):
    raw = "<!--\nEstado: prueba.\n-->\n\n# Capítulo 1 — Caso\n\n" + text + "\n"
    return parse_chapter_text(raw, Path("virtual/01_Caso.md"), Path("virtual"))


class TicChecksTest(unittest.TestCase):
    def test_known_tic_cases_raise_expected_alert(self) -> None:
        for case in CASES["should_alert"]:
            if case["expected_check"].startswith("PHRASE_"):
                continue
            with self.subTest(case=case["id"]):
                _, alerts = tics.analyze(document_for(case["text"]), CONFIG)
                self.assertIn(case["expected_check"], {alert.check_id for alert in alerts})

    def test_short_prose_is_not_high_by_itself(self) -> None:
        for case in CASES["should_not_alert_high"]:
            if case["id"] == "minimal_dialogue":
                continue
            with self.subTest(case=case["id"]):
                document = document_for(case["text"])
                _, tic_alerts = tics.analyze(document, CONFIG)
                _, rhythm_alerts = rhythm.analyze(document, CONFIG)
                self.assertFalse(any(alert.severity == "high" for alert in tic_alerts + rhythm_alerts))

    def test_todo_marker_does_not_match_ordinary_word_todo(self) -> None:
        _, alerts = metadata.analyze(document_for("Todo parecía limpio."), CONFIG)
        self.assertNotIn("INTERNAL_MARKER_IN_PROSE", {alert.check_id for alert in alerts})

        _, alerts = metadata.analyze(document_for("TODO: revisar transición."), CONFIG)
        self.assertIn("INTERNAL_MARKER_IN_PROSE", {alert.check_id for alert in alerts})


if __name__ == "__main__":
    unittest.main()
