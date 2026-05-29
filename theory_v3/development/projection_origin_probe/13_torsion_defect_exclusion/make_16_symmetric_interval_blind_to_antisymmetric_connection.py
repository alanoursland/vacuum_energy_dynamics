#!/usr/bin/env python3
"""
make_16_symmetric_interval_blind_to_antisymmetric_connection.py

Validate that symmetric interval probes are blind to antisymmetric connection
slots.

Output:
    16_symmetric_interval_blind_to_antisymmetric_connection.md
"""

from pathlib import Path
import sympy as sp


a12, a13, a23 = sp.symbols("a12 a13 a23")
v1, v2, v3 = sp.symbols("v1 v2 v3")


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


A = sp.Matrix(
    [
        [0, a12, a13],
        [-a12, 0, a23],
        [-a13, -a23, 0],
    ]
)
v = sp.Matrix([v1, v2, v3])

interval_contribution = simplify_expr((v.T * A * v)[0])
require_zero("antisymmetric interval contribution", interval_contribution)

for symbol in [a12, a13, a23]:
    require_zero(f"interval derivative wrt {symbol}", sp.diff(interval_contribution, symbol))

md = """# Torsion Defect Exclusion 16: Symmetric Interval Blind To Antisymmetric Connection

## Purpose

This proof records a limitation of interval probes.

Quadratic interval data sees symmetric bilinear information. It is blind to an
antisymmetric two-form slot.

## Validated Checks

- antisymmetric contribution to `v^T A v` vanishes: passed
- interval is insensitive to all antisymmetric components: passed

## Algebra

Let:

```text
A_ij = -A_ji.
```

For any vector `v`, Sympy verifies:

```text
v^T A v = 0.
```

Therefore:

```text
d(v^T A v)/dA_ij = 0.
```

## Interpretation

The directional interval folder recovered symmetric metric data. That recovery
does not inspect the antisymmetric connection/torsion slot. Torsion requires
oriented, spin, holonomy, or connection-comparison data beyond symmetric
intervals.
"""

out = Path(__file__).with_name("16_symmetric_interval_blind_to_antisymmetric_connection.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Symmetric interval blindness gate passed.")
print(f"Wrote {out.resolve()}")

