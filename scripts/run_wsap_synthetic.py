from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DERIVED = ROOT / "data" / "derived"
RESULTS_JSON = DERIVED / "results_v10_numeric.json"
SUMMARY_CSV = DERIVED / "wsap_v10_recomputed_summary.csv"


def load_results() -> dict:
    with RESULTS_JSON.open("r", encoding="utf-8") as f:
        return json.load(f)


def compute_summary(results: dict) -> dict:
    singles = results["single"]
    max_single = max(singles.values())
    joint = float(results["joint"])
    joint_gain = joint - max_single
    controls = results["controls"]
    specificity = (
        joint
        - max(0.0, float(controls["kernel_shuffle_tau_parent_corr"]))
        - max(0.0, float(controls["common_noise_tau_corr_with_true_parent"]))
        - 0.5 * abs(float(controls["phase_scrambled_parent_corr_with_joint_tau"]))
    )
    heldout_noisy_mean = sum(v["noisy"] for v in results["heldout"].values()) / len(
        results["heldout"]
    )
    heldout_hidden_mean = sum(v["hidden"] for v in results["heldout"].values()) / len(
        results["heldout"]
    )
    pass_flags = {
        "single_suppression": max_single < 0.75,
        "joint_gain": joint_gain > 0.10,
        "heldout_noisy": heldout_noisy_mean > 0.18,
        "specificity": specificity > 0.30,
    }
    return {
        "version": results["version"],
        "max_single": max_single,
        "joint": joint,
        "joint_gain": joint_gain,
        "heldout_noisy_mean": heldout_noisy_mean,
        "heldout_hidden_mean": heldout_hidden_mean,
        "specificity": specificity,
        "verdict": "PASS" if all(pass_flags.values()) else "FAIL",
        **{f"pass_{k}": v for k, v in pass_flags.items()},
    }


def write_summary(summary: dict) -> None:
    SUMMARY_CSV.parent.mkdir(parents=True, exist_ok=True)
    with SUMMARY_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["metric", "value"])
        for key, value in summary.items():
            writer.writerow([key, value])


def main() -> None:
    results = load_results()
    summary = compute_summary(results)
    write_summary(summary)
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
