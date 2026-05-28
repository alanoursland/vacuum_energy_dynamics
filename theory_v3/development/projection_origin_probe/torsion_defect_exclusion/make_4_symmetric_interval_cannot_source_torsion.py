#!/usr/bin/env python3
"""
make_4_symmetric_interval_cannot_source_torsion.py

Validate that symmetric quadratic interval data has no antisymmetric torsion
source slot.

Output:
    4_symmetric_interval_cannot_source_torsion.md
"""

from pathlib import Path
import sympy as sp


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


h11, h22, h33, h12, h13, h23 = sp.symbols("h11 h22 h33 h12 h13 h23")
a12, a13, a23 = sp.symbols("a12 a13 a23")
v1, v2, v3 = sp.symbols("v1 v2 v3")

H = sp.Matrix(
    [
        [h11, h12, h13],
        [h12, h22, h23],
        [h13, h23, h33],
    ]
)

A = sp.Matrix(
    [
        [0, a12, a13],
        [-a12, 0, a23],
        [-a13, -a23, 0],
    ]
)

v = sp.Matrix([v1, v2, v3])

sym_antisym_contraction = simplify_expr(
    sum(H[i, j] * A[i, j] for i in range(3) for j in range(3))
)
interval_antisym = simplify_expr((v.T * A * v)[0])

require_zero("symmetric-antisymmetric contraction", sym_antisym_contraction)
require_zero("antisymmetric interval contribution", interval_antisym)

md = """# Torsion Defect Exclusion 4: Symmetric Interval Cannot Source Torsion

## Purpose

This proof checks the index-structure limitation of metric interval data.

Symmetric quadratic interval data has no antisymmetric source slot.

## Validated Checks

- contraction of a symmetric tensor with an antisymmetric tensor vanishes: passed
- antisymmetric tensor contributes zero to `v^T A v`: passed

## Algebra

Let:

```text
H_ij = H_ji
A_ij = -A_ji.
```

Sympy verifies:

```text
sum_ij H_ij A_ij = 0.
```

For any vector `v`:

```text
v^T A v = 0.
```

## Interpretation

Directional interval data can recover symmetric metric data, but it does not
by itself provide an antisymmetric torsion source. A torsion source requires
additional spin, rotational, orientation, holonomy, or auxiliary structure.
"""

out = Path(__file__).with_name("4_symmetric_interval_cannot_source_torsion.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Symmetric interval torsion-source exclusion passed.")
print(f"Wrote {out.resolve()}")

