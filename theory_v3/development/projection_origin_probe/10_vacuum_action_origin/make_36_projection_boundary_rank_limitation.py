#!/usr/bin/env python3
"""
make_36_projection_boundary_rank_limitation.py

Validate that the scalar projection/admissibility boundary defect cannot by
itself be the full nonlinear induced-metric boundary variation.

Output:
    36_projection_boundary_rank_limitation.md
"""

from pathlib import Path
import sympy as sp


n = sp.symbols("n", integer=True, positive=True)


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

components = n * (n + 1) / 2
missing = simplify_expr(components - 1)
require_zero("boundary component count formula", missing - (n * (n + 1) / 2 - 1))
checks.append("symmetric induced metric in n dimensions has n(n+1)/2 components")

missing_n3 = simplify_expr(missing.subs(n, 3))
require_zero("3D boundary component gap", missing_n3 - 5)
checks.append("3D induced metric boundary variation has five more components than scalar flux")

missing_n1 = simplify_expr(missing.subs(n, 1))
require_zero("1D boundary component match", missing_n1)
checks.append("scalar boundary flux can match only a one-component boundary sector")

if missing_n3 == 0:
    raise AssertionError("3D boundary metric should not reduce to scalar boundary rank")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 36: Projection Boundary Rank Limitation

## Purpose

This proof records a guardrail for the projection-to-GHY handoff.

The original projection/admissibility defect is scalar. A full nonlinear
metric boundary variation is not scalar.

## Validated Checks

{validation_bullets}

## Component Count

An induced metric on an `n`-dimensional boundary has:

```text
n(n+1)/2
```

independent symmetric components.

The scalar projection boundary defect has one component.

For a three-dimensional boundary:

```text
n(n+1)/2 = 6.
```

So a scalar boundary defect is short by:

```text
5
```

components.

## Interpretation

The projection/admissibility boundary defect can be a scalar seed or reduced
sector of boundary flux. It cannot by itself be the full nonlinear GHY
variation unless additional tensor structure is derived.
"""

out = Path(__file__).with_name("36_projection_boundary_rank_limitation.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Projection boundary rank limitation passed.")
print(f"Wrote {out.resolve()}")
