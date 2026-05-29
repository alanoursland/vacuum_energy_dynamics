#!/usr/bin/env python3
"""
make_17_geodesic_autoparallel_split_gate.py

Validate that velocity-squared autoparallel contraction sees the lower-pair
symmetric connection slot and misses a purely lower-pair antisymmetric torsion
slot.

Output:
    17_geodesic_autoparallel_split_gate.md
"""

from pathlib import Path
import sympy as sp


v1, v2 = sp.symbols("v1 v2")
s111, s112, s122, s211, s212, s222 = sp.symbols("s111 s112 s122 s211 s212 s222")
a1, a2 = sp.symbols("a1 a2")


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


v = [v1, v2]


def S(a, b, c):
    table = {
        (0, 0, 0): s111,
        (0, 0, 1): s112,
        (0, 1, 0): s112,
        (0, 1, 1): s122,
        (1, 0, 0): s211,
        (1, 0, 1): s212,
        (1, 1, 0): s212,
        (1, 1, 1): s222,
    }
    return table[(a, b, c)]


def A(a, b, c):
    table = {
        (0, 0, 0): 0,
        (0, 0, 1): a1,
        (0, 1, 0): -a1,
        (0, 1, 1): 0,
        (1, 0, 0): 0,
        (1, 0, 1): a2,
        (1, 1, 0): -a2,
        (1, 1, 1): 0,
    }
    return table[(a, b, c)]


def contraction(component, connection):
    return simplify_expr(
        sum(connection(component, b, c) * v[b] * v[c] for b in range(2) for c in range(2))
    )


for component in range(2):
    require_zero(
        f"antisymmetric contraction component {component}",
        contraction(component, A),
    )

total0 = simplify_expr(contraction(0, S) + contraction(0, A))
total1 = simplify_expr(contraction(1, S) + contraction(1, A))
require_zero("component 0 total equals symmetric", total0 - contraction(0, S))
require_zero("component 1 total equals symmetric", total1 - contraction(1, S))

torsion_witness0 = simplify_expr(A(0, 0, 1) - A(0, 1, 0))
torsion_witness1 = simplify_expr(A(1, 0, 1) - A(1, 1, 0))
require_zero("torsion witness 0", torsion_witness0 - 2 * a1)
require_zero("torsion witness 1", torsion_witness1 - 2 * a2)

md = f"""# Torsion Defect Exclusion 17: Geodesic-Autoparallel Split Gate

## Purpose

This proof records what velocity-squared connection probes can and cannot see.

The contraction:

```text
Gamma^a_bc v^b v^c
```

sees the lower-pair symmetric part of the connection. A purely lower-pair
antisymmetric torsion slot drops out of this contraction.

## Validated Checks

- antisymmetric lower-pair connection part contracts to zero with `v^b v^c`: passed
- total velocity-squared contraction equals symmetric-part contraction: passed
- torsion witnesses remain nonzero even when velocity-squared contraction misses them: passed

## Witness

For the antisymmetric slot:

```text
A^0_01 = a1
A^0_10 = -a1
A^1_01 = a2
A^1_10 = -a2
```

the torsion witnesses are:

```text
T^0_01 = {torsion_witness0}
T^1_01 = {torsion_witness1}
```

but:

```text
A^a_bc v^b v^c = 0.
```

## Interpretation

Metric geodesic-style data and symmetric interval data do not exhaust torsion
data. Torsion needs oriented or connection-comparison probes, or it must be
excluded by a no-source condition.
"""

out = Path(__file__).with_name("17_geodesic_autoparallel_split_gate.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Geodesic-autoparallel split gate passed.")
print(f"Wrote {out.resolve()}")

