#!/usr/bin/env python3
"""
make_18_metric_origin_gate_status.py

Summarize directional interval selector proofs 13-17.

Output:
    18_metric_origin_gate_status.md
"""

from pathlib import Path


base = Path(__file__).parent
required = [
    "13_parallelogram_metricity_gate.md",
    "14_common_conformal_scale_gate.md",
    "15_nonquadratic_response_obstruction.md",
    "16_isotropic_average_trace_only.md",
    "17_directional_set_recovers_shear.md",
]

missing = [name for name in required if not (base / name).exists()]
if missing:
    raise FileNotFoundError(f"missing required reports: {missing}")

md = """# Vacuum Interval Directional Probe Origin 18: Metric-Origin Gate Status

## Purpose

This report summarizes the third directional selector batch.

## Proofs Completed

Proof `13` validates the parallelogram metricity gate:

```text
Q(u+v)+Q(u-v)-2Q(u)-2Q(v)=0
```

for quadratic interval data, and shows constant, linear, and cubic
contamination violate it.

Proof `14` validates the common conformal scale gate:

```text
m1/q1 = m2/q2
```

for multiple non-null calibrations.

Proof `15` validates that nonquadratic directional response obstructs metric
reconstruction.

Proof `16` validates that isotropic direction averaging recovers only trace.

Proof `17` validates that directional probes recover mean, diagonal shear, and
off-diagonal shear separately.

## Current Result

The metric-origin gate is now sharper:

```text
metric interval data requires:
  quadratic/parallelogram behavior;
  one shared local scale;
  non-isotropic directional comparisons;
  no un-routed nonquadratic directional contamination.
```

## Remaining Gap

The open physical question is no longer whether directional interval data can
represent tensor data. It can.

The remaining question is whether the vacuum model supplies these metricity
conditions from its own dynamics:

```text
Why parallelogram/quadratic?
Why one shared scale?
Why enough preserved directions rather than only isotropic averages?
Why no active nonquadratic interval channel?
```

Those are ontology or action-principle selectors, not projection-algebra
selectors.
"""

out = base / "18_metric_origin_gate_status.md"
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Metric origin gate status validated.")
print(f"Wrote {out.resolve()}")

