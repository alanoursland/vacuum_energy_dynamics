# dataexp: Data Experiments

Observational data and the experiments that confront theory candidates with
it. Data is treated like ML datasets: versioned dataset modules, a local
gitignored cache, manifests with checksums, deterministic loaders.

## Layout

```text
dataexp/
  .data/                  local artifact cache -- NEVER committed (gitignored)
    <dataset>/<version>/  downloaded/digitized files + manifest.json
  datasets/
    base.py               Dataset base class: ensure()/load()/verify()
    short_range_gravity.py
  experiments/
    exp01_short_range_anchors.py
```

## Running

Everything runs from `vacuum_forge/src` with the same convention as the
forge scripts:

```text
cd vacuum_forge/src
PYTHONPATH=. python dataexp/experiments/exp01_short_range_anchors.py
```

`Dataset.ensure()` downloads what can be downloaded into `.data/` on first
use. Artifacts that cannot be auto-downloaded (e.g. exclusion curves that
must be digitized from published figures) are declared in the dataset module
with explicit instructions and a file schema; `load()` reports their status
instead of failing.

## Rules (see theory_v3/development/field_equation_trials/01_data_gate_protocol.md)

- Every value carries provenance (citation, verification status, date).
- Experiments consume datasets only through loaders; no number is typed twice.
- Data bounds parameters; data never selects them.
- Exclusions are stated at the experiment's confidence level and validity
  range, never extrapolated.
- Superseded bounds stay, marked superseded. Negative space (what is NOT
  excluded) is recorded as a result.
