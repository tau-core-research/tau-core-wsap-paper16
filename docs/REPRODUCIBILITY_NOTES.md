# Reproducibility Notes

This paper package summarizes iterative synthetic runs v0.1 through v1.0.

Important:

- The final v1.0 numeric result is synthetic.
- It is not a real-data result.
- The exact generated ZIP packages from previous turns are separate artifacts.
- This package consolidates theory, protocol, final metrics, and roadmap.

Recommended future repository layout:

```text
tau_core_wsap/
  paper/
    PAPER.md
    EXECUTIVE_SUMMARY.md
  data/
    v10_results_table.csv
    version_history.csv
  protocol/
    REAL_DATA_ROADMAP.md
    REPRODUCIBILITY_NOTES.md
```

Future code package should include:

- deterministic seed,
- explicit synthetic parent generator,
- frozen readout definitions,
- frozen negative controls,
- unit tests for PASS conditions,
- automatic report generation.
