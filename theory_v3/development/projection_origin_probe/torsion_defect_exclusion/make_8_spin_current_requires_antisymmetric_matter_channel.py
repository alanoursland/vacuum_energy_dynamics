#!/usr/bin/env python3
"""
make_8_spin_current_requires_antisymmetric_matter_channel.py

Validate that a spin-like torsion source requires antisymmetric/internal
angular data, not only symmetric metric stress data.

Output:
    8_spin_current_requires_antisymmetric_matter_channel.md
"""

from pathlib import Path
import sympy as sp


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


t11, t22, t33, t12, t13, t23 = sp.symbols("t11 t22 t33 t12 t13 t23")
sx, sy, sz, bx, by, bz = sp.symbols("sx sy sz bx by bz")

T_sym = sp.Matrix(
    [
        [t11, t12, t13],
        [t12, t22, t23],
        [t13, t23, t33],
    ]
)

Spin = sp.Matrix(
    [
        [0, sz, -sy],
        [-sz, 0, sx],
        [sy, -sx, 0],
    ]
)

Carrier = sp.Matrix(
    [
        [0, bz, -by],
        [-bz, 0, bx],
        [by, -bx, 0],
    ]
)

sym_spin_contraction = simplify_expr(
    sum(T_sym[i, j] * Spin[i, j] for i in range(3) for j in range(3))
)
spin_carrier_contraction = simplify_expr(
    sum(Spin[i, j] * Carrier[i, j] for i in range(3) for j in range(3))
)
expected_spin_carrier = simplify_expr(2 * (sx * bx + sy * by + sz * bz))

require_zero("symmetric stress spin contraction", sym_spin_contraction)
require_zero("spin carrier contraction", spin_carrier_contraction - expected_spin_carrier)

md = f"""# Torsion Defect Exclusion 8: Spin Current Requires Antisymmetric Matter Channel

## Purpose

This proof checks the index structure of a spin-like torsion source.

Symmetric metric stress data does not by itself provide a spin/torsion source.
An antisymmetric or internal-angular carrier is required.

## Validated Checks

- symmetric tensor contraction with spin-like antisymmetric tensor vanishes: passed
- antisymmetric carrier pairs nontrivially with spin-like source: passed

## Algebra

Let `T_sym` be symmetric and let `Spin` be antisymmetric. Sympy verifies:

```text
sum_ij T_sym_ij Spin_ij = {sym_spin_contraction}.
```

With an antisymmetric carrier `B`, the pairing is:

```text
sum_ij Spin_ij B_ij = {spin_carrier_contraction}.
```

## Interpretation

A spin-like torsion source requires data with antisymmetric/internal-angular
index structure. It cannot be hidden inside the symmetric metric stress or
directional interval Hessian channel.
"""

out = Path(__file__).with_name("8_spin_current_requires_antisymmetric_matter_channel.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Spin current antisymmetric-channel gate passed.")
print(f"Wrote {out.resolve()}")

