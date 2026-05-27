#!/usr/bin/env python3
"""
make_23_nonquadratic_remainder_routing.py

Validate that nonquadratic finite-probe response can fake tensor components on
a small probe set but fails on a consistency direction.

Output:
    23_nonquadratic_remainder_routing.md
"""

from pathlib import Path
import sympy as sp


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


eps = sp.symbols("eps")
v1, v2 = sp.symbols("v1 v2")


def F(x, y):
    return simplify_expr(x**2 + y**2 + eps * x**2 * y**2)


Qe1 = F(1, 0)
Qe2 = F(0, 1)
Qp = F(1, 1)

h11 = Qe1
h22 = Qe2
h12 = simplify_expr((Qp - Qe1 - Qe2) / 2)

Q_fake = simplify_expr(h11 * v1**2 + 2 * h12 * v1 * v2 + h22 * v2**2)
actual_minus = F(1, -1)
fake_minus = Q_fake.subs({v1: 1, v2: -1})
defect_minus = simplify_expr(actual_minus - fake_minus)

require_zero("probe fit e1", Q_fake.subs({v1: 1, v2: 0}) - Qe1)
require_zero("probe fit e2", Q_fake.subs({v1: 0, v2: 1}) - Qe2)
require_zero("probe fit ep", Q_fake.subs({v1: 1, v2: 1}) - Qp)
require_zero("consistency defect", defect_minus - 2 * eps)

md = f"""# Vacuum Interval Directional Probe Origin 23: Nonquadratic Remainder Routing

## Purpose

This proof shows why finite directional reconstruction is not by itself enough
to prove metricity.

A nonquadratic response can fit the axis-plus-pair probe set and appear as a
fake tensor component, but it fails on another direction.

## Validated Checks

- nonquadratic response fits the initial three 2D probes: passed
- reconstructed fake tensor predicts those probes exactly: passed
- a consistency direction exposes the nonquadratic remainder: passed

## Model

Use:

```text
F(x,y) = x^2 + y^2 + eps x^2 y^2.
```

From:

```text
F(e1), F(e2), F(e1+e2)
```

the reconstructed tensor would be:

```text
h11 = {h11}
h22 = {h22}
h12 = {h12}
```

This fake tensor matches the three probes, but at:

```text
e1-e2
```

the defect is:

```text
F(e1-e2) - Q_fake(e1-e2) = {defect_minus}.
```

## Interpretation

Nonquadratic response can masquerade as shear on a finite probe set. The
metric branch therefore needs a metricity check such as the parallelogram law
or small-displacement scaling. Otherwise higher-order response must be routed
as an auxiliary channel, not hidden inside `h_ab`.
"""

out = Path(__file__).with_name("23_nonquadratic_remainder_routing.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Nonquadratic remainder routing passed.")
print(f"Wrote {out.resolve()}")

