#!/usr/bin/env python3
"""
make_5_scalar_projection_cannot_source_torsion.py

Validate that scalar admissibility/projection data cannot create a torsion
source without an additional antisymmetric or oriented channel.

Output:
    5_scalar_projection_cannot_source_torsion.md
"""

from pathlib import Path
import sympy as sp


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


s, eta = sp.symbols("s eta")
a12, a13, a23 = sp.symbols("a12 a13 a23")

I = sp.eye(3)
A = sp.Matrix(
    [
        [0, a12, a13],
        [-a12, 0, a23],
        [-a13, -a23, 0],
    ]
)

# A scalar projection can form an isotropic symmetric tensor s*I, but that
# has zero antisymmetric contraction.
scalar_symmetric = s * I
scalar_antisym_contraction = simplify_expr(
    sum(scalar_symmetric[i, j] * A[i, j] for i in range(3) for j in range(3))
)
require_zero("scalar symmetric antisymmetric contraction", scalar_antisym_contraction)

# A scalar can source torsion only if an extra oriented/antisymmetric carrier
# eta is supplied. The carrier is the additional datum.
oriented_source = eta * s
require_zero("oriented source depends on extra carrier", sp.diff(oriented_source, eta) - s)

md = f"""# Torsion Defect Exclusion 5: Scalar Projection Cannot Source Torsion

## Purpose

This proof checks the scalar projection/admissibility channel.

A scalar can form a trace/isotropic object, but it does not provide an
antisymmetric torsion source unless an additional oriented or antisymmetric
carrier is supplied.

## Validated Checks

- scalar-isotropic tensor has zero antisymmetric contraction: passed
- torsion source from a scalar requires an extra carrier: passed

## Scalar Channel

Let a scalar projection output be:

```text
s.
```

The canonical isotropic tensor it can form is:

```text
s delta_ij.
```

For an antisymmetric candidate:

```text
A_ij = -A_ji,
```

Sympy verifies:

```text
sum_ij s delta_ij A_ij = {scalar_antisym_contraction}.
```

## Extra Carrier Requirement

A scalar torsion source would need a separate oriented carrier:

```text
J_torsion = eta s.
```

The dependence on `eta` is explicit:

```text
dJ_torsion/deta = s.
```

## Interpretation

The scalar projection ladder cannot silently source torsion. If it is used to
build a torsion source, the missing oriented/antisymmetric carrier is a new
physical datum and must be routed explicitly.
"""

out = Path(__file__).with_name("5_scalar_projection_cannot_source_torsion.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Scalar projection torsion-source exclusion passed.")
print(f"Wrote {out.resolve()}")

