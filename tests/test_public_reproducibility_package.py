from __future__ import annotations

import csv
import json
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_publication_files_exist() -> None:
    required = [
        ROOT / "README.md",
        ROOT / "DATA_NOTICE.md",
        ROOT / "paper16_submission_source" / "main.tex",
        ROOT / "paper16_submission_source" / "refs.bib",
        ROOT / "paper16_submission_source" / "main.pdf",
        ROOT / "arxiv_submission_source.zip",
        ROOT / "data" / "derived" / "results_v10_numeric.json",
        ROOT / "data" / "derived" / "wsap_v10_recomputed_summary.csv",
    ]
    missing = [str(p) for p in required if not p.exists()]
    assert not missing, missing


def test_claim_boundary_markers() -> None:
    text = (ROOT / "paper16_submission_source" / "main.tex").read_text(encoding="utf-8")
    forbidden_positive_overclaims = [
        "we prove Tau Core",
        "proves Tau Core",
        "dark matter is solved",
        "dark energy is solved",
        "validation-grade evidence for Tau Core",
    ]
    assert "Synthetic methodological demonstration only" in text
    assert "does not claim" in text
    for phrase in forbidden_positive_overclaims:
        assert phrase not in text


def test_frozen_result_values() -> None:
    data = json.loads((ROOT / "data" / "derived" / "results_v10_numeric.json").read_text())
    assert data["verdict"] == "PASS"
    assert abs(data["joint"] - 0.6729463093741658) < 1e-12
    assert abs(data["joint_gain"] - 0.3123161513272113) < 1e-12
    assert abs(data["specificity"] - 0.646416132588535) < 1e-12


def test_recomputed_summary_matches_pass_conditions() -> None:
    rows = {}
    with (ROOT / "data" / "derived" / "wsap_v10_recomputed_summary.csv").open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rows[row["metric"]] = row["value"]
    assert rows["verdict"] == "PASS"
    assert rows["pass_single_suppression"] == "True"
    assert rows["pass_joint_gain"] == "True"
    assert rows["pass_heldout_noisy"] == "True"
    assert rows["pass_specificity"] == "True"


def test_arxiv_zip_is_source_package() -> None:
    zip_path = ROOT / "arxiv_submission_source.zip"
    with zipfile.ZipFile(zip_path) as zf:
        names = set(zf.namelist())
    assert "main.tex" in names
    assert "refs.bib" in names
    assert "main.pdf" not in names
    assert any(name.startswith("figures/") and name.endswith(".pdf") for name in names)
