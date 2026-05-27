#!/usr/bin/env python3
"""
make_46_scalar_ladder_tensor_rank_obstruction.py

Validate that a scalar projection ladder cannot determine full symmetric
boundary tensor data without extra tensor labels.

Output:
    46_scalar_ladder_tensor_rank_obstruction.md
"""

from pathlib import Path
import sympy as sp


n, N = sp.symbols("n N", integer=True, positive=True)


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

sym_components = n * (n + 1) / 2
scalar_ladder_equations = N
tensor_boundary_unknowns = N * sym_components
rank_gap = simplify_expr(tensor_boundary_unknowns - scalar_ladder_equations)

require_zero(
    "scalar ladder tensor rank gap",
    rank_gap - N * (n * (n + 1) / 2 - 1),
)
checks.append("N scalar ladder rows leave N*(n(n+1)/2-1) tensor components unresolved")

rank_gap_3d = simplify_expr(rank_gap.subs(n, 3))
require_zero("3D boundary rank gap", rank_gap_3d - 5 * N)
checks.append("for a 3D boundary, scalar ladder misses 5N tensor directions")

rank_gap_1d = simplify_expr(rank_gap.subs(n, 1))
require_zero("1D boundary rank gap", rank_gap_1d)
checks.append("scalar ladder is rank-complete only for a one-component boundary")

if simplify_expr(rank_gap_3d.subs(N, 1)) == 0:
    raise AssertionError("3D scalar ladder should have a nonzero tensor rank gap")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 46: Scalar Ladder Tensor Rank Obstruction

## Purpose

This proof tests whether a scalar projection/admissibility ladder can supply
the full tensor boundary data needed by a nonlinear metric boundary term.

## Validated Checks

{validation_bullets}

## Rank Count

An induced metric on an `n`-dimensional boundary has:

```text
n(n+1)/2
```

symmetric components.

An `N`-row scalar ladder supplies:

```text
N
```

scalar conditions.

Full tensor boundary data would require:

```text
N * n(n+1)/2
```

component conditions.

The unresolved rank gap is:

```text
N * (n(n+1)/2 - 1).
```

For a three-dimensional boundary this is:

```text
5N.
```

## Interpretation

The scalar projection ladder cannot by itself determine the full tensor
boundary variation. It is complete only in a one-component boundary sector, or
after a separate theorem supplies tensor-indexed copies of the ladder.
"""

out = Path(__file__).with_name("46_scalar_ladder_tensor_rank_obstruction.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Scalar ladder tensor rank obstruction passed.")
print(f"Wrote {out.resolve()}")
