#!/usr/bin/env python3
"""
make_21_boundary_dimension_relation.py

Validate the relation between spacetime dimension, one-clock spatial dimension,
spacetime boundary hypersurface dimension, and spatial boundary dimension.

Output:
    21_boundary_dimension_relation.md
"""

from pathlib import Path
import sympy as sp


D = sp.symbols("D", integer=True, positive=True)
spatial_dimension = D - 1
spacetime_boundary_hypersurface = D - 1
spatial_boundary_surface = D - 2


def require_zero(label, expr):
    result = sp.simplify(expr)
    if result != 0:
        raise AssertionError(f"{label} failed: {result}")


require_zero("D=4 spatial dimension", spatial_dimension.subs(D, 4) - 3)
require_zero("D=4 spacetime boundary hypersurface", spacetime_boundary_hypersurface.subs(D, 4) - 3)
require_zero("D=4 spatial boundary surface", spatial_boundary_surface.subs(D, 4) - 2)

md = f"""# Vacuum Dimension Selector 21: Boundary Dimension Relation

## Purpose

This proof separates two boundary counts that are easy to confuse.

## Validated Checks

- in `D=4`, one-clock spatial slices have dimension `3`: passed
- in `D=4`, spacetime boundary hypersurfaces have dimension `3`: passed
- in `D=4`, spatial boundary surfaces have dimension `2`: passed

## Computation

```text
spatial slice dimension = D - 1
spacetime boundary hypersurface dimension = D - 1
spatial boundary surface dimension = D - 2
```

At `D=4`:

```text
spatial slice dimension = {spatial_dimension.subs(D, 4)}
spacetime boundary hypersurface dimension = {spacetime_boundary_hypersurface.subs(D, 4)}
spatial boundary surface dimension = {spatial_boundary_surface.subs(D, 4)}
```

## Interpretation

The induced-metric boundary bookkeeping used by the action bridge concerns a
spacetime boundary hypersurface, not merely a two-dimensional spatial sphere.
"""

out = Path(__file__).with_name("21_boundary_dimension_relation.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Boundary dimension relation passed.")
print(f"Wrote {out.resolve()}")

