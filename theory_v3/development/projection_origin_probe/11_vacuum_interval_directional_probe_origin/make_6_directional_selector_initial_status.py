#!/usr/bin/env python3
"""
make_6_directional_selector_initial_status.py

Summarize the first directional interval selector proof batch.

Output:
    6_directional_selector_initial_status.md
"""

from pathlib import Path


base = Path(__file__).parent
required = [
    "1_quadratic_polarization_identity.md",
    "2_axis_pair_probe_reconstruction.md",
    "3_trace_probe_blind_traceless_sector.md",
    "4_null_probe_conformal_ambiguity.md",
    "5_boundary_induced_metric_projection.md",
]

missing = [name for name in required if not (base / name).exists()]
if missing:
    raise FileNotFoundError(f"missing required reports: {missing}")

md = """# Vacuum Interval Directional Probe Origin 6: Initial Status

## Purpose

This report summarizes the first selector-level proof batch for directional
interval data.

## Proofs Completed

Proof `1` validates polarization:

```text
(Q(u+v)-Q(u)-Q(v))/2 = u^T H v.
```

Proof `2` validates finite reconstruction in 3D:

```text
Q(e_i), Q(e_i+e_j) recover all h_ij.
```

Proof `3` validates the trace limitation:

```text
dim(trace-blind symmetric sector in 3D) = 5.
```

Proof `4` validates null-cone scale ambiguity:

```text
Q = 0 and cQ = 0 have the same null set.
```

Proof `5` validates boundary induced metric projection:

```text
h = E^T G E.
```

## Current Result

The directional interval selector is mathematically viable:

```text
local interval comparisons
  -> quadratic form Q(v)
  -> symmetric bilinear tensor by polarization
  -> induced boundary metric from tangent probes.
```

This supplies exactly the type of data the scalar projection ladder lacks.

## Remaining Gap

This batch proves the algebraic selector, not its physical origin.

The next proofs should ask whether the vacuum ontology supplies:

```text
1. enough independent local direction probes;
2. an interval scale, not just null-cone order;
3. tangent-vs-normal boundary splitting;
4. transformation behavior under local frame changes;
5. a source/action coupling that uses h_ab rather than only tr(h).
```

If those close, this folder can hand back to the action-origin chain with a
candidate origin for tensor boundary data.
"""

out = base / "6_directional_selector_initial_status.md"
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Directional selector initial status validated.")
print(f"Wrote {out.resolve()}")

