#!/usr/bin/env python3
"""
make_1_quadratic_polarization_identity.py

Validate the basic selector identity:

    Q(v) = v^T H v

determines the symmetric bilinear form by polarization:

    B(u,v) = (Q(u+v)-Q(u)-Q(v))/2 = u^T H v.

Output:
    1_quadratic_polarization_identity.md
"""

from pathlib import Path
import sympy as sp


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


h11, h12, h22 = sp.symbols("h11 h12 h22")
u1, u2, v1, v2 = sp.symbols("u1 u2 v1 v2")

H = sp.Matrix([[h11, h12], [h12, h22]])
u = sp.Matrix([u1, u2])
v = sp.Matrix([v1, v2])


def Q(z):
    return simplify_expr((z.T * H * z)[0])


polarized = simplify_expr((Q(u + v) - Q(u) - Q(v)) / 2)
bilinear = simplify_expr((u.T * H * v)[0])

require_zero("polarization identity", polarized - bilinear)

checks = [
    "quadratic interval probe expands correctly",
    "polarization recovers the symmetric bilinear pairing",
]

validation_bullets = "\n".join(f"- {item}: passed" for item in checks)

md = f"""# Vacuum Interval Directional Probe Origin 1: Quadratic Polarization Identity

## Purpose

This proof establishes the minimal algebra needed for directional interval
probes to carry tensor data.

If the local interval response is:

```text
Q(v) = v^T H v
```

then the symmetric bilinear tensor `H` is recovered by polarization.

## Validated Checks

{validation_bullets}

## Identity

For:

```text
H = [[h11,h12],[h12,h22]]
u = (u1,u2)
v = (v1,v2)
```

Sympy verifies:

```text
(Q(u+v)-Q(u)-Q(v))/2 = u^T H v.
```

## Interpretation

Directional interval comparisons are not scalar trace data. They are
quadratic-form data. Once the ontology supplies `Q(v)` for enough directions,
the symmetric bilinear object is algebraically determined.
"""

out = Path(__file__).with_name("1_quadratic_polarization_identity.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Quadratic polarization identity passed.")
print(f"Wrote {out.resolve()}")

