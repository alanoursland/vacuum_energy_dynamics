#!/usr/bin/env python3
"""
make_23_three_boundary_component_match.py

Validate that three boundary directions produce six axis-plus-pair components,
matching a symmetric induced metric on a three-dimensional hypersurface.

Output:
    23_three_boundary_component_match.md
"""

from pathlib import Path
import sympy as sp


m = sp.symbols("m", integer=True, positive=True)
axis_terms = m
pair_terms = sp.simplify(m * (m - 1) / 2)
axis_plus_pair = sp.simplify(axis_terms + pair_terms)
symmetric_count = sp.simplify(m * (m + 1) / 2)


def require_zero(label, expr):
    result = sp.simplify(expr)
    if result != 0:
        raise AssertionError(f"{label} failed: {result}")


require_zero("axis plus pair equals symmetric count", axis_plus_pair - symmetric_count)
require_zero("three-direction component match", axis_plus_pair.subs(m, 3) - 6)

md = f"""# Vacuum Dimension Selector 23: Three Boundary Component Match

## Purpose

This proof connects directional boundary bookkeeping to induced metric
component counting.

## Validated Checks

- `m` axis terms plus `m(m-1)/2` pair terms equals `m(m+1)/2`: passed
- for `m=3`, the count is six: passed

## Computation

```text
axis terms = m
pair terms = m(m-1)/2
axis + pair = {axis_plus_pair}
symmetric metric count = {symmetric_count}
```

For `m=3`:

```text
axis + pair = {axis_plus_pair.subs(m, 3)}
```

## Interpretation

Three boundary directions are the first case where axis and pair bookkeeping
matches the six components of a symmetric induced metric on a boundary
hypersurface.
"""

out = Path(__file__).with_name("23_three_boundary_component_match.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Three-boundary component match passed.")
print(f"Wrote {out.resolve()}")

