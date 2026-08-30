from __future__ import annotations

import json
import unittest
from collections import Counter
from pathlib import Path

from tools.editorial.checks import dialogue, lexical, repetitions, rhythm, similarity, tics
from tools.editorial.checks.common import parse_chapter_text


ROOT = Path(__file__).resolve().parents[3]
CONFIG = json.loads((ROOT / "tools/editorial/editorial_config.json").read_text(encoding="utf-8"))
CASES = json.loads(Path(__file__).with_name("regression_v1_1.json").read_text(encoding="utf-8"))


def document_for(text: str, filename: str = "01_Caso.md"):
    raw = "<!-- metadata -->\n# Capítulo 1 — Caso\n\n" + text + "\n"
    return parse_chapter_text(raw, Path("virtual") / filename, Path("virtual"))


class V11RegressionTest(unittest.TestCase):
    def test_real_short_cluster_regressions_never_raise_high(self) -> None:
        local = dict(CONFIG)
        local["short_paragraph_run_warning"] = 3
        for case in CASES["short_clusters"]:
            with self.subTest(case=case["id"]):
                _, alerts = rhythm.analyze(document_for(case["text"]), local)
                self.assertTrue(alerts)
                self.assertNotIn("high", {alert.severity for alert in alerts})
                self.assertNotIn("SHORT_PARAGRAPH_CLUSTER", {alert.check_id for alert in alerts})

    def test_dialogue_incise_is_excluded_from_spoken_estimate(self) -> None:
        text = (
            "—Uno dos tres cuatro cinco seis siete ocho nueve diez —Lo dijo despacio, midiendo cuánto contar.— "
            "Once doce trece catorce quince dieciséis diecisiete dieciocho diecinueve veinte."
        )
        estimate = dialogue.estimate_spoken_segments(text, CONFIG)
        self.assertEqual(estimate.spoken_words_estimate, 20)
        self.assertGreater(estimate.dialogue_paragraph_words_raw, estimate.spoken_words_estimate)
        self.assertEqual(len(estimate.narrative_segments), 1)

    def test_single_long_intervention_is_never_high(self) -> None:
        text = "—" + " ".join(["palabra"] * 70) + " —Cole dijo esto muy despacio.— Fin."
        _, alerts = dialogue.analyze(document_for(text), CONFIG)
        intervention = next(alert for alert in alerts if alert.check_id == "LONG_DIALOGUE_INTERVENTION")
        self.assertEqual(intervention.severity, "medium")
        self.assertNotIn("high", {alert.severity for alert in alerts})

    def test_two_long_interventions_raise_compound_high(self) -> None:
        speech = "—" + " ".join(["palabra"] * 65) + "."
        text = f"{speech}\n\nCole dejó el vaso.\n\n{speech}"
        _, alerts = dialogue.analyze(document_for(text), CONFIG)
        cluster = next(alert for alert in alerts if alert.check_id == "LONG_DIALOGUE_CLUSTER")
        self.assertEqual(cluster.severity, "high")
        self.assertEqual(cluster.confidence, "compound")
        self.assertEqual(len(cluster.metric["lines"]), 2)

    def test_trigram_is_inventory_but_not_local_alert(self) -> None:
        local = dict(CONFIG)
        local["ngram_lengths"] = [3]
        local["ngram_min_count_global"] = 3
        document = document_for("Metal bajo lluvia. Metal bajo lluvia. Metal bajo lluvia.")
        rows, alerts, counters = repetitions.repeated_ngram_metrics(document, local, set(CONFIG["stopwords"]))
        self.assertTrue(any(row["length"] == 3 for row in rows))
        self.assertFalse(alerts)
        global_rows = repetitions.merge_ngram_counters([counters], local)
        self.assertTrue(any(row["length"] == 3 for row in global_rows))

    def test_contained_ngram_prefers_longer_expression(self) -> None:
        document = document_for("Se limpió las manos. Se limpió las manos. Se limpió las manos.")
        rows, _, _ = repetitions.repeated_ngram_metrics(document, CONFIG, set(CONFIG["stopwords"]))
        phrases = {row["ngram"] for row in rows}
        self.assertNotIn("limpio las manos", phrases)
        self.assertTrue(any("se limpio las manos" in phrase for phrase in phrases))

    def test_negative_chain_stays_inside_dialogue_intervention(self) -> None:
        narrative = document_for('No hubo beso. No hubo un "sube". No hubo nada que se pareciera a una invitación.')
        _, narrative_alerts = tics.analyze(narrative, CONFIG)
        self.assertIn("NEGATIVE_SENTENCE_CHAIN", {alert.check_id for alert in narrative_alerts})
        dialogue_turns = document_for("—No.\n\n—No es eso.\n\n—No dije eso.")
        _, dialogue_alerts = tics.analyze(dialogue_turns, CONFIG)
        self.assertNotIn("NEGATIVE_SENTENCE_CHAIN", {alert.check_id for alert in dialogue_alerts})

    def test_overlapping_gesture_windows_form_one_real_cluster(self) -> None:
        occurrences = [(10, "miró"), (14, "miró"), (18, "miró"), (22, "miró")]
        clusters = lexical.build_distinct_clusters(occurrences, line_window=10, threshold=3)
        self.assertEqual(len(clusters), 1)
        self.assertEqual(len(clusters[0]), 3)

    def test_editorial_leak_has_two_confidence_levels(self) -> None:
        high_doc = document_for("No narró lo que hizo con el coche.")
        _, high_alerts = tics.analyze(high_doc, CONFIG)
        high = next(alert for alert in high_alerts if alert.check_id == "EDITORIAL_INSTRUCTION_LEAK")
        self.assertEqual((high.severity, high.confidence), ("high", "high-confidence"))
        possible_doc = document_for("No contó lo que había sucedido aquella noche.")
        _, possible_alerts = tics.analyze(possible_doc, CONFIG)
        possible = next(alert for alert in possible_alerts if alert.check_id == "POSSIBLE_EDITORIAL_INSTRUCTION_LEAK")
        self.assertEqual(possible.severity, "low")

    def test_cross_chapter_similarity_is_experimental_and_never_high(self) -> None:
        passage = " ".join(
            ["talleres", "casas", "barrio", "seguridad", "trabajo", "familias", "negocios", "futuro"] * 6
        )
        docs = [document_for(passage, "01_Uno.md"), document_for(passage + " futuro", "02_Dos.md")]
        rows, alerts = similarity.analyze(docs, CONFIG, set(CONFIG["stopwords"]))
        self.assertTrue(rows)
        self.assertEqual(rows[0]["experimental"], True)
        self.assertNotIn("high", {alert.severity for values in alerts.values() for alert in values})


if __name__ == "__main__":
    unittest.main()
