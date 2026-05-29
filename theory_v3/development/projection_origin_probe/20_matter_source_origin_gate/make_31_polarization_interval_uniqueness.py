#!/usr/bin/env python3
"""
make_31_polarization_interval_uniqueness.py

Validate uniqueness of a local quadratic interval from operational interval
measurements via polarization.

Output:
    31_polarization_interval_uniqueness.md
"""

from pathlib import Path
import sympy as sp


a, b, c = sp.symbols("a b c")
x1, x2, y1, y2 = sp.symbols("x1 x2 y1 y2")


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

M = sp.Matrix([[a, b], [b, c]])
x = sp.Matrix([x1, x2])
y = sp.Matrix([y1, y2])

Q = lambda v: simplify_expr((v.T * M * v)[0])
B = lambda u, v: simplify_expr((u.T * M * v)[0])

polarized = simplify_expr((Q(x + y) - Q(x - y)) / 4)
require_zero("polarization identity", polarized - B(x, y))
checks.append("quadratic interval determines the symmetric bilinear form")

e1 = sp.Matrix([1, 0])
e2 = sp.Matrix([0, 1])
recover_a = Q(e1)
recover_c = Q(e2)
recover_b = simplify_expr((Q(e1 + e2) - Q(e1) - Q(e2)) / 2)
require_zero("recover a", recover_a - a)
require_zero("recover b", recover_b - b)
require_zero("recover c", recover_c - c)
checks.append("basis and sum interval measurements recover all 2D metric components")

da, db, dc = sp.symbols("da db dc")
D = sp.Matrix([[da, db], [db, dc]])
QD = lambda v: simplify_expr((v.T * D * v)[0])
eqs = [
    sp.Eq(QD(e1), 0),
    sp.Eq(QD(e2), 0),
    sp.Eq(QD(e1 + e2), 0),
]
solution = sp.solve(eqs, [da, db, dc], dict=True)
if solution != [{da: 0, db: 0, dc: 0}]:
    raise AssertionError(f"unexpected interval uniqueness solution: {solution}")
checks.append("two symmetric forms with same interval data are identical")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Matter Source Origin Gate 31: Polarization Interval Uniqueness

## Purpose

This proof records the mathematical uniqueness gate behind operational interval
measurements.

If the vacuum state supplies a local quadratic interval:

```text
Q(v) = g(v,v),
```

then the full symmetric bilinear form is determined by the interval data.

## Validated Checks

{validation_bullets}

## Polarization

For a symmetric bilinear form `B` with quadratic interval `Q(v)=B(v,v)`:

```text
B(x,y) = (Q(x+y)-Q(x-y))/4.
```

SymPy verifies this identity for a general 2D symmetric matrix:

```text
M = [[a,b],[b,c]].
```

## Component Recovery

From interval measurements:

```text
Q(e1)
Q(e2)
Q(e1+e2)
```

one recovers:

```text
a = Q(e1)
c = Q(e2)
b = (Q(e1+e2)-Q(e1)-Q(e2))/2.
```

## Gate Interpretation

If operational rods/clocks determine one local quadratic interval for all
directions, then the corresponding metric candidate is unique. The remaining
physical question is whether the vacuum ontology forces matter probes to read
that one interval.
"""

out = Path(__file__).with_name("31_polarization_interval_uniqueness.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Polarization interval uniqueness passed.")
print(f"Wrote {out.resolve()}")
