import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_pair_readout_scope():
    p = json.loads((ROOT / "data/derived/pair_readout_update_20260927.json").read_text())
    assert not p["empirical_scores_changed"] and not p["tau_specific_evidence"]
    assert p["canonical_result"]["id"] == "CPR1"
    assert p["canonical_result"]["version"] == "1.0"
    for name in p["manuscripts"]:
        text = (ROOT / name).read_text()
        assert "% BEGIN PAIR READOUT UPDATE" not in text
        assert "``Conditional source preparation and time-resolved access''" in text
        assert "Theorem\nCPR1(" in text or "Theorem CPR1(" in text
        assert "v1.0 (2026-09-28)" in text
        assert "full_derivation.pdf#nameddest=cpr1" in text
