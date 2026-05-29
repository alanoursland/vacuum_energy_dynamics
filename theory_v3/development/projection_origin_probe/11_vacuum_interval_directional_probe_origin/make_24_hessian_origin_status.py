#!/usr/bin/env python3
"""
make_24_hessian_origin_status.py

Summarize directional interval selector proofs 19-23.

Output:
    24_hessian_origin_status.md
"""

from pathlib import Path


base = Path(__file__).parent
required = [
    "19_hessian_second_variation_origin.md",
    "20_small_displacement_scaling_gate.md",
    "21_single_scale_field_origin.md",
    "22_direction_dependent_scale_obstruction.md",
    "23_nonquadratic_remainder_routing.md",
]

missing = [name for name in required if not (base / name).exists()]
if missing:
    raise FileNotFoundError(f"missing required reports: {missing}")

md = """# Vacuum Interval Directional Probe Origin 24: Hessian-Origin Status

## Purpose

This report summarizes the fourth directional selector batch.

## Proofs Completed

Proof `19` validates the Hessian/second-variation origin:

```text
d^2/dlambda^2 F(lambda v)|0 = v^T H v.
```

Proof `20` validates small-displacement scaling:

```text
F(lambda) = lambda^2 Q + alpha lambda^3 C + beta lambda^4 R
```

separates quadratic, cubic, and quartic channels.

Proof `21` validates the single-scale origin:

```text
m_i = beta q_i -> m_i/q_i = beta.
```

Proof `22` validates that direction-dependent scale is not a scalar conformal
scale. If retained, it is tensor/shear data.

Proof `23` validates that nonquadratic finite-probe response can fake tensor
components unless a metricity check routes the remainder.

## Current Result

The conditional origin is now clear:

```text
local stationary second variation
  -> Hessian
  -> quadratic directional interval branch
  -> symmetric metric-like tensor.
```

The required guardrails are also clear:

```text
first variation must vanish or be routed as source/force;
higher-order response must be separated by scaling/parallelogram tests;
one local scale field must calibrate all directions;
direction-dependent scale must be treated as tensor data, not scalar scale.
```

## Remaining Gap

This folder has not derived the vacuum functional whose second variation is
the interval metric. It has proved what that origin would need to look like.

The next proof target is therefore either:

```text
derive the local vacuum interval functional;
```

or close this folder as a conditional tensor-boundary-data bridge and move to
another selector:

```text
torsion_defect_exclusion
vacuum_dimension_selector
lambda_relaxation_mechanism
```
"""

out = base / "24_hessian_origin_status.md"
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Hessian origin status validated.")
print(f"Wrote {out.resolve()}")

