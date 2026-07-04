from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run(cmd: list[str], cwd: Path = ROOT) -> None:
    print("$", " ".join(cmd))
    subprocess.run(cmd, cwd=cwd, check=True)


def main() -> None:
    run(["python", "scripts/run_wsap_synthetic.py"])
    run(["python", "scripts/build_figures.py"])
    run(["tectonic", "main.tex"], cwd=ROOT / "paper16_submission_source")
    run(["python", "scripts/build_arxiv_source.py"])
    run(["python", "-m", "pytest", "-q"])
    print("PAPER16_WSAP_REPRODUCTION_COMPLETE")


if __name__ == "__main__":
    main()
