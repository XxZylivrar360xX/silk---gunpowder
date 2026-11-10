"""Barrido de candidatos a prolepsis de narrador (EDITORIAL_POLICY §L).

Modo audit_only: no escribe sobre capítulos. Uso, desde la raíz del vault:

    python tools/editorial/prolepsis_audit.py \
        --manifest tools/editorial/libro_01_completo.json \
        --output tools/editorial/reports/PROLEPSIS_LIBRO_01
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

from checks import prolepsis
from checks.common import SEVERITY_ORDER, parse_chapter

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONFIG = Path(__file__).with_name("prolepsis_config.json")


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def manifest_entries(manifest: dict[str, Any]) -> list[tuple[str, Path]]:
    if manifest.get("mode") != "audit_only":
        raise SystemExit("El manifiesto debe declarar mode: audit_only.")
    entries = []
    for index, item in enumerate(manifest["chapters"], start=1):
        if isinstance(item, str):
            label, rel = str(index), item
        else:
            label, rel = str(item["cap"]), item["path"]
        path = ROOT / rel
        if not path.exists():
            raise SystemExit(f"No existe: {rel}")
        entries.append((label, path))
    return entries


def md_cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def render(rows: list[dict[str, Any]], manifest_name: str, config: dict[str, Any], incluir_dialogo: bool) -> str:
    by_sev = Counter(r["severity"] for r in rows)
    by_rule = Counter(r["check_id"] for r in rows)
    by_cap = Counter(r["cap"] for r in rows)
    out = [
        f"# Barrido de prolepsis — {manifest_name}",
        "",
        f"Versión: `{config.get('editor_version')}`. Modo `audit_only`. Contextos: narración, inciso y cursiva"
        + (" + diálogo y citas" if incluir_dialogo else " (diálogo y citas excluidos: prolepsis de personaje lícita)")
        + ".",
        "",
        "Cada fila es un **candidato**, no un fallo. `medium` = patrón fuerte en voz del narrador; `low` = patrón medio; `info` = débil o en cursiva.",
        "",
        f"**Total:** {len(rows)} — medium {by_sev['medium']}, low {by_sev['low']}, info {by_sev['info']}.",
        "",
        "## Por patrón",
        "",
        "| Patrón | Familia | Fuerza | N |",
        "|---|---|---|---|",
    ]
    rules = {r["id"]: r for r in config["patrones"]}
    for rule_id, n in by_rule.most_common():
        rule = rules[rule_id]
        out.append(f"| {rule_id} | {rule['familia']} | {rule['fuerza']} | {n} |")
    out += ["", "## Candidatos por capítulo", ""]
    current = None
    for row in rows:
        if row["cap"] != current:
            current = row["cap"]
            out += ["", f"### Cap. {row['cap']} — `{row['file']}` ({by_cap[row['cap']]})", "",
                    "| Línea | Sev. | Patrón | Contexto | Fragmento |", "|---|---|---|---|---|"]
        out.append(
            f"| {row['line']} | {row['severity']} | {row['check_id']} | {row['contexto']} | {md_cell(row['excerpt'])} |"
        )
    out.append("")
    return "\n".join(out)


def run(manifest_path: Path, config_path: Path, output: Path, incluir_dialogo: bool) -> list[dict[str, Any]]:
    manifest = load_json(manifest_path)
    config = load_json(config_path)
    patterns = prolepsis.compile_patterns(config)
    rows: list[dict[str, Any]] = []
    for label, path in manifest_entries(manifest):
        document = parse_chapter(path, ROOT)
        _, alerts = prolepsis.analyze(document, config, incluir_dialogo=incluir_dialogo, patterns=patterns)
        for alert in alerts:
            rows.append({
                "cap": label,
                "file": document.filename,
                "line": alert.line,
                "severity": alert.severity,
                "check_id": alert.check_id,
                "contexto": alert.metric["contexto"],
                "familia": alert.metric["familia"],
                "coincidencia": alert.metric["coincidencia"],
                "excerpt": alert.excerpt,
            })
    output.mkdir(parents=True, exist_ok=True)
    name = manifest.get("pilot", manifest_path.stem)
    (output / f"{name}.md").write_text(render(rows, name, config, incluir_dialogo), encoding="utf-8")
    (output / f"{name}.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    return rows


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--incluir-dialogo", action="store_true", help="Reporta también parlamentos y citas (como info).")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args(argv)
    rows = run(args.manifest, args.config, args.output, args.incluir_dialogo)
    if not args.quiet:
        sev = Counter(r["severity"] for r in rows)
        print(f"{len(rows)} candidatos (medium {sev['medium']}, low {sev['low']}, info {sev['info']}) -> {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
