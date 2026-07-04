from __future__ import annotations

import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "paper16_submission_source"
OUT = ROOT / "arxiv_submission_source.zip"
EXCLUDED_SUFFIXES = {".aux", ".bbl", ".blg", ".log", ".out", ".toc", ".pdf"}


def main() -> None:
    with zipfile.ZipFile(OUT, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in SRC.rglob("*"):
            if path.is_dir():
                continue
            if path.name == "main.pdf":
                continue
            if path.suffix in EXCLUDED_SUFFIXES and path.parent == SRC:
                continue
            zf.write(path, path.relative_to(SRC))
    print(f"WROTE {OUT}")


if __name__ == "__main__":
    main()
