from __future__ import annotations

import json
import unittest
from pathlib import Path

from tools.editorial.checks import prolepsis
from tools.editorial.checks.common import parse_chapter_text


ROOT = Path(__file__).resolve().parents[3]
CONFIG = json.loads((ROOT / "tools/editorial/prolepsis_config.json").read_text(encoding="utf-8"))


def ids_for(text: str, **kwargs) -> set[str]:
    raw = "<!--\nEstado: prueba.\n-->\n\n# Capítulo 1 — Caso\n\n" + text + "\n"
    document = parse_chapter_text(raw, Path("virtual/01_Caso.md"), Path("virtual"))
    _, alerts = prolepsis.analyze(document, CONFIG, **kwargs)
    return {alert.check_id for alert in alerts}


class ProlepsisTest(unittest.TestCase):
    # Casos ya dictados como PROLEPSIS DE NARRADOR en 13_Auditorias (Libro I).
    def test_casos_dictados_alertan(self) -> None:
        casos = {
            "No se lo contó a nadie, ni esa noche ni después.": "NI_DESPUES",
            "Tres personas que jamás se habían visto y que nunca sabrían que habían escrito la misma página.": "NUNCA_COND_SABER",
            "Se lo guardó, como guardaba todo lo que no sabía todavía cómo iba a costarle.": "COSTARIA_CAMBIARIA",
            "Lo dejó con la delicadeza de las cosas que todavía no saben que ya lo cambiaron todo.": "COSTARIA_CAMBIARIA",
            "No volvieron a hablar del balcón.": "NO_VOLVIO_A",
            "Años después recordaría esa mesa.": "TIEMPO_LARGO_DESPUES",
            "Todavía no sabía que iba a necesitarlo.": "TODAVIA_NO_SABIA",
        }
        for text, expected in casos.items():
            with self.subTest(text=text):
                self.assertIn(expected, ids_for(text))

    def test_prolepsis_de_personaje_en_dialogo_se_excluye(self) -> None:
        self.assertEqual(ids_for("—Una es mucho, Chiara. Nunca lo olvidaría, ya lo vas a ver."), set())

    def test_inciso_de_dialogo_si_se_revisa(self) -> None:
        found = ids_for("—Vámonos —dijo Kal, y no volvieron a hablar del tema—. Ya.")
        self.assertIn("NO_VOLVIO_A", found)

    def test_dialogo_opcional(self) -> None:
        self.assertIn("NUNCA_COND_SABER", ids_for("—Nunca sabría que fuiste tú.", incluir_dialogo=True))

    def test_creencia_presente_no_alerta(self) -> None:
        self.assertEqual(ids_for("Pensó que San Aurelio sería eso: una escala."), set())


if __name__ == "__main__":
    unittest.main()
