from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DERIVED = ROOT / "data" / "derived"
FIGURES = ROOT / "figures"
PAPER_FIGURES = ROOT / "paper16_submission_source" / "figures"


def load_results() -> dict:
    with (DERIVED / "results_v10_numeric.json").open("r", encoding="utf-8") as f:
        return json.load(f)


def style() -> None:
    plt.rcParams.update(
        {
            "font.size": 9,
            "axes.titlesize": 11,
            "axes.labelsize": 9,
            "legend.fontsize": 8,
            "figure.dpi": 160,
            "savefig.bbox": "tight",
        }
    )


def save(fig, name: str) -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    PAPER_FIGURES.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIGURES / name)
    fig.savefig(PAPER_FIGURES / name)
    plt.close(fig)


def fig_protocol() -> None:
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    ax.axis("off")
    boxes = [
        (0.05, 0.58, 0.18, 0.22, "Frozen\nsynthetic parent\n$P_\\tau$"),
        (0.31, 0.74, 0.18, 0.16, "Topology\nvector $W$"),
        (0.31, 0.52, 0.18, 0.16, "Shear-stat\nvector $L$"),
        (0.31, 0.30, 0.18, 0.16, "Sparse galaxy\nvector $R$"),
        (0.31, 0.08, 0.18, 0.16, "Coarse environment\nvector $H$"),
        (0.61, 0.44, 0.18, 0.22, "Joint compressed\nparent recovery\n$\\widehat P_\\tau$"),
        (0.82, 0.58, 0.14, 0.16, "Held-out\nprediction"),
        (0.82, 0.30, 0.14, 0.16, "Negative\ncontrols"),
    ]
    colors = ["#d7ecff", "#eaf4dc", "#eaf4dc", "#eaf4dc", "#eaf4dc", "#fff0c7", "#e6dcff", "#ffd9d9"]
    for (x, y, w, h, label), color in zip(boxes, colors):
        ax.add_patch(plt.Rectangle((x, y), w, h, facecolor=color, edgecolor="#333333", lw=1.2))
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center", wrap=True)
    for y in [0.82, 0.60, 0.38, 0.16]:
        ax.annotate("", xy=(0.31, y), xytext=(0.23, 0.69), arrowprops=dict(arrowstyle="->", lw=1))
    for y in [0.82, 0.60, 0.38, 0.16]:
        ax.annotate("", xy=(0.61, 0.55), xytext=(0.49, y), arrowprops=dict(arrowstyle="->", lw=1))
    ax.annotate("", xy=(0.82, 0.66), xytext=(0.79, 0.56), arrowprops=dict(arrowstyle="->", lw=1))
    ax.annotate("", xy=(0.82, 0.38), xytext=(0.79, 0.52), arrowprops=dict(arrowstyle="->", lw=1))
    ax.set_title("WSAP protocol: weak readouts, joint recovery, controls")
    save(fig, "fig_wsap_protocol.pdf")


def fig_recovery(results: dict) -> None:
    singles = results["single"]
    labels = list(singles.keys()) + ["Joint"]
    values = list(singles.values()) + [results["joint"]]
    colors = ["#7aa6c2"] * len(singles) + ["#d0802f"]
    fig, ax = plt.subplots(figsize=(7.2, 3.8))
    ax.bar(np.arange(len(values)), values, color=colors, edgecolor="#333333")
    ax.axhline(results["max_single"], color="#555555", ls="--", lw=1, label="best single")
    ax.set_xticks(np.arange(len(values)))
    ax.set_xticklabels(["W", "L", "R", "H", "Joint"])
    ax.set_ylabel("correlation with frozen parent")
    ax.set_title("Single-sector suppression and joint recovery")
    ax.legend(loc="upper left")
    for i, v in enumerate(values):
        ax.text(i, v + 0.025, f"{v:.3f}", ha="center", va="bottom")
    ax.set_ylim(-0.10, 0.78)
    save(fig, "fig_single_vs_joint.pdf")


def fig_controls(results: dict) -> None:
    controls = results["controls"]
    keep = [
        "kernel_shuffle_tau_parent_corr",
        "common_noise_tau_corr_with_true_parent",
        "phase_scrambled_parent_corr_with_joint_tau",
        "random_parent_corr_with_joint_tau",
        "rotated_parent_corr_with_joint_tau",
    ]
    labels = ["kernel\nshuffle", "common\nnoise", "phase\nscramble", "random\nparent", "rotated\nparent"]
    values = [controls[k] for k in keep]
    fig, ax = plt.subplots(figsize=(7.2, 3.7))
    ax.bar(np.arange(len(values)), values, color="#c9c9c9", edgecolor="#333333")
    ax.axhline(results["joint"], color="#d0802f", lw=2, label="joint candidate")
    ax.axhline(0, color="#222222", lw=0.8)
    ax.set_xticks(np.arange(len(values)))
    ax.set_xticklabels(labels)
    ax.set_ylabel("correlation score")
    ax.set_title("Negative controls remain separated from the joint candidate")
    ax.legend(loc="upper right")
    for i, v in enumerate(values):
        va = "bottom" if v >= 0 else "top"
        offset = 0.025 if v >= 0 else -0.025
        ax.text(i, v + offset, f"{v:.3f}", ha="center", va=va)
    ax.set_ylim(-0.48, 0.76)
    save(fig, "fig_negative_controls.pdf")


def fig_heldout(results: dict) -> None:
    channels = list(results["heldout"].keys())
    noisy = [results["heldout"][c]["noisy"] for c in channels]
    hidden = [results["heldout"][c]["hidden"] for c in channels]
    x = np.arange(len(channels))
    fig, ax = plt.subplots(figsize=(7.2, 3.7))
    ax.bar(x - 0.18, noisy, width=0.36, color="#8bbbd9", edgecolor="#333333", label="noisy residual")
    ax.bar(x + 0.18, hidden, width=0.36, color="#f2bf70", edgecolor="#333333", label="hidden signal")
    ax.axhline(0.18, color="#555555", ls="--", lw=1, label="held-out threshold")
    ax.set_xticks(x)
    ax.set_xticklabels(channels)
    ax.set_ylabel("held-out correlation")
    ax.set_title("Held-out prediction remains positive across synthetic channels")
    ax.legend(loc="upper right")
    ax.set_ylim(0, 1.0)
    save(fig, "fig_heldout_prediction.pdf")


def fig_history() -> None:
    rows = []
    with (DERIVED / "version_history.csv").open("r", encoding="utf-8") as f:
        next(f)
        for line in f:
            parts = line.rstrip("\n").split(",", 2)
            if len(parts) >= 2:
                rows.append((parts[0], parts[1]))
    verdict_score = {"FAIL_OR_WEAK / hard test": 0.15, "FAIL_OR_WEAK": 0.20, "PARTIAL PASS": 0.55, "PASS": 0.90}
    values = [verdict_score.get(v, 0.4) for _, v in rows]
    fig, ax = plt.subplots(figsize=(7.2, 3.3))
    ax.plot(range(len(rows)), values, marker="o", color="#536fae", lw=2)
    ax.set_xticks(range(len(rows)))
    ax.set_xticklabels([r[0] for r in rows], rotation=45, ha="right")
    ax.set_yticks([0.2, 0.55, 0.9])
    ax.set_yticklabels(["weak/fail", "partial", "pass"])
    ax.set_ylim(0.0, 1.0)
    ax.set_title("Development history: controls tightened before v1.0 PASS")
    ax.grid(axis="y", alpha=0.25)
    save(fig, "fig_development_history.pdf")


def main() -> None:
    style()
    results = load_results()
    fig_protocol()
    fig_recovery(results)
    fig_controls(results)
    fig_heldout(results)
    fig_history()


if __name__ == "__main__":
    main()
