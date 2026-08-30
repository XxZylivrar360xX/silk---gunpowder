#!/usr/bin/env python3
"""Auditor editorial determinista y de solo lectura para Seda y Pólvora."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from statistics import quantiles
from typing import Any

from checks import dialogue, lexical, metadata, repetitions, rhythm, tics
from checks.common import Alert, SEVERITY_ORDER, parse_chapter, sorted_alerts


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[1]
DEFAULT_CONFIG = SCRIPT_DIR / "editorial_config.json"


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def resolve_from_root(value: str | Path) -> Path:
    path = Path(value)
    return path.resolve() if path.is_absolute() else (REPO_ROOT / path).resolve()


def validate_manifest(manifest: dict[str, Any], manifest_path: Path) -> list[Path]:
    if manifest.get("mode") != "audit_only":
        raise ValueError("El manifiesto debe declarar mode=audit_only.")
    chapters = manifest.get("chapters")
    if not isinstance(chapters, list) or not chapters:
        raise ValueError("El manifiesto debe contener una lista explícita de capítulos.")
    paths: list[Path] = []
    for value in chapters:
        path = resolve_from_root(value)
        if not path.is_file():
            raise FileNotFoundError(f"Capítulo no encontrado en {manifest_path}: {value}")
        if path.suffix.casefold() != ".md":
            raise ValueError(f"El corpus sólo admite Markdown: {value}")
        paths.append(path)
    if len(paths) != len(set(paths)):
        raise ValueError("El manifiesto contiene capítulos duplicados.")
    return paths


def build_stopwords(config: dict[str, Any]) -> set[str]:
    return {value.casefold() for value in config.get("stopwords", []) + config.get("stopwords_additional", [])}


def severity_counts(alerts: list[Alert]) -> dict[str, int]:
    counts = Counter(alert.severity for alert in alerts)
    return {severity: counts.get(severity, 0) for severity in ("high", "medium", "low", "info")}


def write_text_if_changed(path: Path, content: str) -> None:
    """Evita reabrir reportes idénticos, útil en carpetas sincronizadas."""
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return
    path.write_text(content, encoding="utf-8", newline="\n")


def iqr_bounds(values: list[float]) -> tuple[float, float] | None:
    if len(values) < 4 or len(set(values)) < 2:
        return None
    q1, _, q3 = quantiles(values, n=4, method="inclusive")
    spread = q3 - q1
    if spread == 0:
        return None
    return q1 - 1.5 * spread, q3 + 1.5 * spread


def add_corpus_outliers(chapters: list[dict[str, Any]]) -> list[dict[str, Any]]:
    fields = {
        "words": ("RHYTHM_WORD_COUNT_OUTLIER", "conteo de palabras"),
        "words_per_sentence_median": ("RHYTHM_SENTENCE_MEDIAN_OUTLIER", "mediana de palabras por oración"),
        "single_sentence_paragraph_percent": ("RHYTHM_SINGLE_SENTENCE_PARAGRAPH_OUTLIER", "% de párrafos de una oración"),
        "dialogue_percent_approx": ("DIALOGUE_PERCENT_OUTLIER", "% aproximado de diálogo"),
        "words_per_intervention_median": ("DIALOGUE_INTERVENTION_MEDIAN_OUTLIER", "mediana de intervención"),
    }
    outliers: list[dict[str, Any]] = []
    for field, (check_id, label) in fields.items():
        source = "dialogue" if field in {"dialogue_percent_approx", "words_per_intervention_median"} else "rhythm"
        values = [float(chapter["metrics"][source][field]) for chapter in chapters]
        bounds = iqr_bounds(values)
        if bounds is None:
            continue
        lower, upper = bounds
        for chapter, value in zip(chapters, values):
            if value < lower or value > upper:
                direction = "bajo" if value < lower else "alto"
                alert = Alert(
                    check_id=check_id,
                    severity="low",
                    chapter=chapter["filename"],
                    line=None,
                    excerpt="",
                    message=f"Outlier {direction} del corpus en {label}; no implica un problema.",
                    metric={
                        "value": round(value, 3),
                        "iqr_lower": round(lower, 3),
                        "iqr_upper": round(upper, 3),
                    },
                    category=source,
                )
                chapter["alerts"].append(alert)
                outliers.append(alert.to_dict())
    return outliers


def alert_markdown(alert: Alert) -> str:
    location = f"línea {alert.line}" if alert.line is not None else "métrica de capítulo"
    value = f" — “{alert.excerpt}”" if alert.excerpt else ""
    return f"- `{alert.check_id}` · {location}: {alert.message}{value}"


def metric_table(rows: list[tuple[str, Any]]) -> list[str]:
    return [f"- {label}: {value}" for label, value in rows]


def render_chapter_report(chapter: dict[str, Any], config: dict[str, Any]) -> str:
    alerts = sorted_alerts(chapter["alerts"])
    counts = severity_counts(alerts)
    rhythm_metrics = chapter["metrics"]["rhythm"]
    dialogue_metrics = chapter["metrics"]["dialogue"]
    repetition_metrics = chapter["metrics"]["repetitions"]
    lexical_metrics = chapter["metrics"]["lexical"]
    metadata_metrics = chapter["metrics"]["metadata"]
    lines = [
        f"# Auditoría editorial — Capítulo {chapter['number']:02d}",
        "",
        "> Esto es diagnóstico, no una lista de correcciones. Una alerta —incluso HIGH— sólo pide lectura humana prioritaria.",
        "",
        "## Resumen",
        "",
        *metric_table(
            [
                ("Palabras", rhythm_metrics["words"]),
                ("Párrafos narrativos", rhythm_metrics["paragraphs"]),
                ("Diálogo aproximado", f"{dialogue_metrics['dialogue_percent_approx']:.1f}%"),
                ("Alertas HIGH / MEDIUM / LOW / INFO", f"{counts['high']} / {counts['medium']} / {counts['low']} / {counts['info']}"),
            ]
        ),
        "",
        "## Prioridad de lectura",
        "",
    ]
    for severity in ("high", "medium", "low", "info"):
        lines.extend([f"### {severity.upper()}", ""])
        matching = [alert for alert in alerts if alert.severity == severity]
        if matching:
            lines.extend(alert_markdown(alert) for alert in matching)
        else:
            lines.append("- Sin alertas.")
        lines.append("")

    lines.extend(["## Repeticiones", ""])
    phrases = repetition_metrics["phrases"]
    if phrases:
        lines.extend(
            f"- `{phrase}`: {data['count']} · {data['density_per_1000_words']:.3f}/1,000 palabras · líneas {', '.join(map(str, data['lines'][:8]))}"
            for phrase, data in phrases.items()
        )
    else:
        lines.append("- Sin frases vigiladas presentes.")
    ngrams = repetition_metrics["repeated_ngrams"]
    lines.extend(["", "### N-gramas locales", ""])
    if ngrams:
        lines.extend(f"- `{row['ngram']}` ({row['length']} palabras): {row['count']}" for row in ngrams)
    else:
        lines.append("- Sin n-gramas por encima del umbral local.")

    lines.extend(
        [
            "",
            "## Ritmo",
            "",
            *metric_table(
                [
                    ("Oraciones aproximadas", rhythm_metrics["sentences_approx"]),
                    ("Palabras/oración, media", rhythm_metrics["words_per_sentence_mean"]),
                    ("Palabras/oración, mediana", rhythm_metrics["words_per_sentence_median"]),
                    ("Palabras/párrafo, media", rhythm_metrics["words_per_paragraph_mean"]),
                    ("Palabras/párrafo, mediana", rhythm_metrics["words_per_paragraph_median"]),
                    ("Párrafos de una oración", f"{rhythm_metrics['single_sentence_paragraph_percent']:.1f}%"),
                    ("Máxima secuencia de párrafos cortos", rhythm_metrics["max_consecutive_short_paragraphs"]),
                    ("Distribución 1–5 / 6–10 / 11–20 / 21–40 / 41+", " / ".join(str(value) for value in rhythm_metrics["paragraph_size_distribution"].values())),
                ]
            ),
            "",
            "## Diálogo",
            "",
            *metric_table(
                [
                    ("Intervenciones", dialogue_metrics["interventions"]),
                    ("Palabras/intervención, media", dialogue_metrics["words_per_intervention_mean"]),
                    ("Palabras/intervención, mediana", dialogue_metrics["words_per_intervention_median"]),
                    ("Máximo", dialogue_metrics["words_per_intervention_max"]),
                    ("Más de 25 / 40 / 60 palabras", " / ".join(str(dialogue_metrics["over_thresholds"].get(str(value), 0)) for value in (25, 40, 60))),
                    ("Máximo intercambio sin acción", dialogue_metrics["max_exchange_without_action"]),
                ]
            ),
            "",
            "## Léxico / gestos",
            "",
            f"- Adverbios en `-mente`: {lexical_metrics['adverbs_mente']['count']} ({lexical_metrics['adverbs_mente']['density_per_1000_words']:.3f}/1,000 palabras).",
            "- Palabras frecuentes sin stopwords: " + ", ".join(f"{row['word']} ({row['count']})" for row in lexical_metrics["top_words"][:15]) + ".",
        ]
    )
    gestures = lexical_metrics["gestures"]
    if gestures:
        lines.extend(
            f"- {data['label']}: {data['count']} ({data['density_per_1000_words']:.3f}/1,000; clusters: {data['clusters']})."
            for data in gestures.values()
        )
    else:
        lines.append("- Sin gestos vigilados presentes.")

    lines.extend(
        [
            "",
            "## Metadata",
            "",
            *metric_table(
                [
                    ("Metadata inicial", "sí" if metadata_metrics["metadata_present"] else "no"),
                    ("Título Markdown", "sí" if metadata_metrics["title_present"] else "no"),
                    ("Número filename/título", "coincide" if metadata_metrics["filename_title_match"] is True else "no evaluable" if metadata_metrics["filename_title_match"] is None else "NO coincide"),
                    ("Marcadores en metadata", ", ".join(metadata_metrics["metadata_markers"]) or "ninguno"),
                    ("Marcadores en prosa", len(metadata_metrics["prose_markers"])),
                    ("Comentarios HTML internos", metadata_metrics["internal_comments"]),
                    ("Headings internos", metadata_metrics["unexpected_headings"]),
                ]
            ),
            "",
        ]
    )
    return "\n".join(lines)


def render_global_report(global_data: dict[str, Any], chapters: list[dict[str, Any]], config: dict[str, Any]) -> str:
    counts = global_data["alert_counts"]
    lines = [
        f"# Auditoría editorial global — {global_data['pilot']}",
        "",
        "> Esto es diagnóstico, no una lista de correcciones. HIGH significa lectura humana prioritaria, no obligación de modificar.",
        "",
        "## Corpus",
        "",
        f"- Capítulos: {len(chapters)}.",
        f"- Palabras totales: {global_data['total_words']}.",
        f"- Alertas HIGH / MEDIUM / LOW / INFO: {counts['high']} / {counts['medium']} / {counts['low']} / {counts['info']}.",
        "",
        "| Capítulo | Palabras |",
        "|---|---:|",
    ]
    lines.extend(f"| {chapter['number']:02d} · {chapter['filename']} | {chapter['metrics']['rhythm']['words']} |" for chapter in chapters)

    lines.extend(["", "## Patrones globales", "", "### Frases vigiladas", ""])
    if global_data["phrases"]:
        lines.extend(
            f"- `{phrase}`: {data['count']} ({data['density_per_1000_words']:.3f}/1,000 palabras; capítulos: {len(data['chapters'])}; umbral global {data['configured_global_threshold']}: {'alcanzado' if data['above_global_threshold'] else 'no alcanzado'})."
            for phrase, data in global_data["phrases"].items()
        )
    else:
        lines.append("- Sin ocurrencias.")
    lines.extend(["", "### N-gramas destacables", ""])
    if global_data["ngrams"]:
        lines.extend(f"- `{row['ngram']}` ({row['length']} palabras): {row['count']}" for row in global_data["ngrams"])
    else:
        lines.append("- Sin n-gramas por encima del umbral global.")
    lines.extend(["", "### Gestos y adverbios", ""])
    lines.extend(f"- {label}: {data['count']} ({data['density_per_1000_words']:.3f}/1,000)." for label, data in global_data["gestures"].items())
    lines.append(f"- Adverbios terminados en `-mente`: {global_data['adverbs_mente']['count']} ({global_data['adverbs_mente']['density_per_1000_words']:.3f}/1,000).")
    lines.extend(["", "### Construcciones / tics", ""])
    if global_data["tics"]:
        lines.extend(f"- `{check_id}`: {count}" for check_id, count in global_data["tics"].items())
    else:
        lines.append("- Sin construcciones por encima de cero.")

    lines.extend(
        [
            "",
            "## Ritmo comparado",
            "",
            "| Cap. | Palabras | Mediana oración | % párrafos 1 oración | Diálogo % | Mediana intervención |",
            "|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for chapter in chapters:
        r = chapter["metrics"]["rhythm"]
        d = chapter["metrics"]["dialogue"]
        lines.append(
            f"| {chapter['number']:02d} | {r['words']} | {r['words_per_sentence_median']:.1f} | "
            f"{r['single_sentence_paragraph_percent']:.1f}% | {d['dialogue_percent_approx']:.1f}% | "
            f"{d['words_per_intervention_median']:.1f} |"
        )

    lines.extend(["", "## Outliers", "", "Se usa IQR (Q1 − 1.5×IQR, Q3 + 1.5×IQR). Un outlier no es un problema.", ""])
    if global_data["outliers"]:
        lines.extend(
            f"- {item['chapter']} · `{item['check_id']}`: {item['message']} Valor {item['metric']['value']}; rango {item['metric']['iqr_lower']}–{item['metric']['iqr_upper']}."
            for item in global_data["outliers"]
        )
    else:
        lines.append("- Sin outliers por IQR en las métricas comparadas.")

    lines.extend(["", "## Top de alertas para calibración", ""])
    top_limit = int(config.get("limits", {}).get("global_alerts", 30))
    top_alerts = sorted_alerts([alert for chapter in chapters for alert in chapter["alerts"]])[:top_limit]
    if top_alerts:
        lines.extend(f"- **{alert.severity.upper()}** · {alert.chapter} · {alert_markdown(alert)[2:]}" for alert in top_alerts)
    else:
        lines.append("- Sin alertas.")
    lines.extend(
        [
            "",
            "## Límite de V1",
            "",
            "No hay análisis lingüístico profundo ni atribución automática de hablantes. Las oraciones, intervenciones y proporciones son aproximaciones mecánicas; no existe autofix.",
            "",
        ]
    )
    return "\n".join(lines)


def build_global(chapters: list[dict[str, Any]], manifest: dict[str, Any], config: dict[str, Any], ngram_counters: list[Any]) -> dict[str, Any]:
    all_alerts = [alert for chapter in chapters for alert in chapter["alerts"]]
    total_words = sum(chapter["metrics"]["rhythm"]["words"] for chapter in chapters)
    phrase_totals: dict[str, dict[str, Any]] = {}
    for phrase in config.get("phrases", {}):
        rows = [
            (chapter["filename"], chapter["metrics"]["repetitions"]["phrases"].get(phrase))
            for chapter in chapters
        ]
        count = sum(row[1]["count"] for row in rows if row[1])
        if count:
            threshold = int(config["phrases"][phrase].get("global_threshold", 1))
            phrase_totals[phrase] = {
                "count": count,
                "density_per_1000_words": round(count * 1000 / max(1, total_words), 3),
                "chapters": [name for name, data in rows if data],
                "configured_global_threshold": threshold,
                "above_global_threshold": count >= threshold,
            }

    gesture_totals: dict[str, dict[str, Any]] = {}
    for chapter in chapters:
        for data in chapter["metrics"]["lexical"]["gestures"].values():
            target = gesture_totals.setdefault(data["label"], {"count": 0})
            target["count"] += data["count"]
    for data in gesture_totals.values():
        data["density_per_1000_words"] = round(data["count"] * 1000 / max(1, total_words), 3)

    adverb_count = sum(chapter["metrics"]["lexical"]["adverbs_mente"]["count"] for chapter in chapters)
    tic_totals = Counter(
        alert.check_id
        for alert in all_alerts
        if alert.category == "tics" and alert.check_id != "EDITORIAL_INSTRUCTION_LEAK"
    )
    return {
        "pilot": manifest.get("pilot", "PILOT"),
        "mode": "audit_only",
        "chapters": len(chapters),
        "total_words": total_words,
        "alert_counts": severity_counts(all_alerts),
        "phrases": phrase_totals,
        "ngrams": repetitions.merge_ngram_counters(ngram_counters, config),
        "gestures": gesture_totals,
        "adverbs_mente": {
            "count": adverb_count,
            "density_per_1000_words": round(adverb_count * 1000 / max(1, total_words), 3),
        },
        "tics": dict(sorted(tic_totals.items())),
        "outliers": [],
    }


def run(manifest_path: Path, config_path: Path, output_dir: Path, chapter_filter: str | None = None) -> dict[str, Any]:
    manifest = load_json(manifest_path)
    config = load_json(config_path)
    chapter_paths = validate_manifest(manifest, manifest_path)
    if chapter_filter:
        needle = chapter_filter.casefold()
        chapter_paths = [path for path in chapter_paths if needle in path.name.casefold() or needle in path.stem.casefold()]
        if not chapter_paths:
            raise ValueError(f"--chapter no coincide con el manifiesto: {chapter_filter}")

    stopwords = build_stopwords(config)
    chapters: list[dict[str, Any]] = []
    ngram_counters: list[Any] = []
    for path in chapter_paths:
        document = parse_chapter(path, REPO_ROOT)
        phrase_metrics, phrase_alerts = repetitions.analyze_phrases(document, config)
        ngram_metrics, ngram_alerts, counters = repetitions.repeated_ngram_metrics(document, config, stopwords)
        rhythm_metrics, rhythm_alerts = rhythm.analyze(document, config)
        dialogue_metrics, dialogue_alerts = dialogue.analyze(document, config)
        tic_metrics, tic_alerts = tics.analyze(document, config)
        lexical_metrics, lexical_alerts = lexical.analyze(document, config, stopwords)
        metadata_metrics, metadata_alerts = metadata.analyze(document, config)
        alerts = phrase_alerts + ngram_alerts + rhythm_alerts + dialogue_alerts + tic_alerts + lexical_alerts + metadata_alerts
        number_match = __import__("re").match(r"^(\d+)_", document.filename)
        chapters.append(
            {
                "number": int(number_match.group(1)) if number_match else len(chapters) + 1,
                "filename": document.filename,
                "path": document.relative_path,
                "metrics": {
                    "repetitions": {"phrases": phrase_metrics, "repeated_ngrams": ngram_metrics},
                    "tics": tic_metrics,
                    "rhythm": rhythm_metrics,
                    "dialogue": dialogue_metrics,
                    "lexical": lexical_metrics,
                    "metadata": metadata_metrics,
                },
                "alerts": alerts,
            }
        )
        ngram_counters.append(counters)

    outliers = add_corpus_outliers(chapters) if not chapter_filter else []
    global_data = build_global(chapters, manifest, config, ngram_counters)
    global_data["outliers"] = outliers
    global_data["alert_counts"] = severity_counts([alert for chapter in chapters for alert in chapter["alerts"]])

    output_dir.mkdir(parents=True, exist_ok=True)
    pilot_name = str(manifest.get("pilot", "PILOT")).upper()
    for chapter in chapters:
        report_path = output_dir / f"{Path(chapter['filename']).stem}.editorial.md"
        if report_path.resolve() in chapter_paths:
            raise ValueError("El output intentaría sobrescribir un capítulo; operación rechazada.")
        write_text_if_changed(report_path, render_chapter_report(chapter, config))
    global_report = output_dir / f"{pilot_name}_GLOBAL.md"
    structured_report = output_dir / f"{pilot_name}.json"
    write_text_if_changed(global_report, render_global_report(global_data, chapters, config))
    payload = {
        "schema_version": 1,
        "pilot": manifest.get("pilot", "PILOT"),
        "mode": "audit_only",
        "manifest": manifest_path.relative_to(REPO_ROOT).as_posix() if manifest_path.is_relative_to(REPO_ROOT) else str(manifest_path),
        "config": config_path.relative_to(REPO_ROOT).as_posix() if config_path.is_relative_to(REPO_ROOT) else str(config_path),
        "global": global_data,
        "chapters": [
            {**chapter, "alerts": [alert.to_dict() for alert in sorted_alerts(chapter["alerts"])]}
            for chapter in chapters
        ],
    }
    write_text_if_changed(structured_report, json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
    return payload


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Auditor editorial determinista (sólo lectura del corpus).")
    parser.add_argument("--manifest", required=True, help="Manifiesto JSON con lista explícita de capítulos.")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG), help="Configuración JSON; por defecto usa editorial_config.json.")
    parser.add_argument("--output", required=True, help="Directorio donde se escriben exclusivamente los reportes.")
    parser.add_argument("--quiet", action="store_true", help="No imprime resumen al terminar.")
    parser.add_argument("--chapter", help="Filtra por número o fragmento del filename para depuración.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        payload = run(
            resolve_from_root(args.manifest),
            resolve_from_root(args.config),
            resolve_from_root(args.output),
            args.chapter,
        )
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2
    if not args.quiet:
        counts = payload["global"]["alert_counts"]
        print(
            f"{payload['pilot']}: {payload['global']['chapters']} capítulos, "
            f"{payload['global']['total_words']} palabras, "
            f"alertas H/M/L/I={counts['high']}/{counts['medium']}/{counts['low']}/{counts['info']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
