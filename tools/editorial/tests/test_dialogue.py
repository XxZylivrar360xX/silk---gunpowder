from __future__ import annotations

import json
import unittest
from pathlib import Path

from tools.editorial.checks import dialogue
from tools.editorial.checks.common import parse_chapter_text


ROOT = Path(__file__).resolve().parents[3]
CONFIG = json.loads((ROOT / "tools/editorial/editorial_config.json").read_text(encoding="utf-8"))


def document_for(text: str):
    raw = "<!-- metadata -->\n# Capítulo 1 — Caso\n\n" + text + "\n"
    return parse_chapter_text(raw, Path("virtual/01_Caso.md"), Path("virtual"))


class DialogueChecksTest(unittest.TestCase):
    def test_minimal_intervention_is_not_an_alert(self) -> None:
        metrics, alerts = dialogue.analyze(document_for("—Sí."), CONFIG)
        self.assertEqual(metrics["interventions"], 1)
        self.assertFalse(alerts)

    def test_long_exchange_without_action_is_detected(self) -> None:
        text = "\n\n".join(f"—Intervención número {number}." for number in range(9))
        metrics, alerts = dialogue.analyze(document_for(text), CONFIG)
        self.assertEqual(metrics["max_exchange_without_action"], 9)
        self.assertIn("DIALOGUE_EXCHANGE_WITHOUT_ACTION", {alert.check_id for alert in alerts})

    def test_long_intervention_uses_configured_threshold(self) -> None:
        text = "—" + " ".join(["palabra"] * 45) + "."
        _, alerts = dialogue.analyze(document_for(text), CONFIG)
        self.assertIn("LONG_DIALOGUE_INTERVENTION", {alert.check_id for alert in alerts})


if __name__ == "__main__":
    unittest.main()
