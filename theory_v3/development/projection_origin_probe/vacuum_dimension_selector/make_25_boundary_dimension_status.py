#!/usr/bin/env python3
"""
make_25_boundary_dimension_status.py

Summarize the boundary-dimension selector gate.

Output:
    25_boundary_dimension_status.md
"""

from pathlib import Path


base = Path(__file__).resolve().parent
required = [
    "21_boundary_dimension_relation.md",
    "22_induced_metric_component_count_by_boundary_dimension.md",
    "23_three_boundary_component_match.md",
    "24_scalar_projection_rank_gap_by_dimension.md",
]

missing = [name for name in required if not (base / name).exists()]
if missing:
    raise FileNotFoundError(f"missing required reports: {missing}")

md = """# Vacuum Dimension Selector 25: Boundary Dimension Status

## Status

The boundary-dimension gate is closed conditionally.

## What Was Proved

- in `D=4`, a spacetime boundary hypersurface is three-dimensional
- a three-dimensional induced metric has six independent components
- three directional axes plus three directional pairs also give six components
- scalar boundary data alone has a five-component rank gap relative to a
  three-dimensional induced metric

## What Was Not Proved

The scalar projection hierarchy does not become a full tensor boundary theory
by itself. It needs a geometric lift with induced metric data or an equivalent
tensorial replacement.

## Gate Result

```text
D = 4
=> boundary hypersurface dimension = 3
=> induced metric component count = 6.
```

The scalar projection branch remains useful as an admissibility sector, not as
the whole boundary geometry.
"""

out = base / "25_boundary_dimension_status.md"
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Boundary-dimension status report validated.")
print(f"Wrote {out}")

