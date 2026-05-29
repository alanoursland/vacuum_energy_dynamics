#!/usr/bin/env python3
"""
make_24_scalar_projection_rank_gap_by_dimension.py

Validate the rank gap between scalar boundary data and induced metric boundary
data.

Output:
    24_scalar_projection_rank_gap_by_dimension.md
"""

from pathlib import Path
import sympy as sp


m = sp.symbols("m", integer=True, positive=True)
induced_components = sp.simplify(m * (m + 1) / 2)
scalar_components = sp.Integer(1)
rank_gap = sp.simplify(induced_components - scalar_components)


def require_zero(label, expr):
    result = sp.simplify(expr)
    if result != 0:
        raise AssertionError(f"{label} failed: {result}")


require_zero("m=1 scalar gap", rank_gap.subs(m, 1))
require_zero("m=2 scalar gap", rank_gap.subs(m, 2) - 2)
require_zero("m=3 scalar gap", rank_gap.subs(m, 3) - 5)

md = f"""# Vacuum Dimension Selector 24: Scalar Projection Rank Gap By Dimension

## Purpose

This proof checks how far a scalar boundary profile is from carrying full
induced metric boundary data.

## Validated Checks

- for `m=1`, scalar data matches the one induced component: passed
- for `m=2`, scalar data misses two induced components: passed
- for `m=3`, scalar data misses five induced components: passed

## Computation

```text
N_induced(m) = {induced_components}
N_scalar = {scalar_components}
gap(m) = N_induced(m) - N_scalar = {rank_gap}
```

Values:

```text
gap(1) = {rank_gap.subs(m, 1)}
gap(2) = {rank_gap.subs(m, 2)}
gap(3) = {rank_gap.subs(m, 3)}
```

## Interpretation

The scalar projection hierarchy cannot by itself carry all induced metric
boundary data in a three-dimensional hypersurface. It can serve as a scalar
sector or admissibility gate, but the full geometric lift needs additional
tensorial data.
"""

out = Path(__file__).with_name("24_scalar_projection_rank_gap_by_dimension.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Scalar projection rank gap check passed.")
print(f"Wrote {out.resolve()}")

