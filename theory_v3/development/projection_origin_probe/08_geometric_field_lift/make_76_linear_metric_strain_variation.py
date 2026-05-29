#!/usr/bin/env python3
"""
make_76_linear_metric_strain_variation.py

Validate the first cautious geometric lift:

    E[h] = 1/2 integral sum_ij |grad h_ij|^2 dV
           - integral sum_ij S_ij h_ij dV

has componentwise Euler-Lagrange equations:

    -Delta h_ij = S_ij.

This is not GR. It is only the componentwise weak-field strain model.

Output:
    76_linear_metric_strain_variation.md
"""

from pathlib import Path
import sympy as sp


x, y, z = sp.symbols("x y z", real=True)
coords = (x, y, z)


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []


def lap(expr):
    return sum(sp.diff(expr, c, 2) for c in coords)


def grad_dot(a, b):
    return sum(sp.diff(a, c) * sp.diff(b, c) for c in coords)


def div_v_grad_h(v, h):
    return sum(sp.diff(v * sp.diff(h, c), c) for c in coords)


components = ["00", "01", "02", "11", "12", "22"]

for name in components:
    h = sp.Function(f"h{name}")(x, y, z)
    v = sp.Function(f"v{name}")(x, y, z)
    S = sp.Function(f"S{name}")(x, y, z)

    variation_density = grad_dot(h, v) - S * v
    ibp_density = div_v_grad_h(v, h) + (-lap(h) - S) * v
    require_zero(f"component {name} first-variation identity", variation_density - ibp_density)

checks.append("componentwise first-variation identities verified")

# Explicit representative Euler-Lagrange equation from the density.
h = sp.Function("h")(x, y, z)
S = sp.Function("S")(x, y, z)
v = sp.Function("v")(x, y, z)
identity = grad_dot(h, v) - S * v - div_v_grad_h(v, h) - (-lap(h) - S) * v
require_zero("representative Euler-Lagrange density identity", identity)
checks.append("representative Euler-Lagrange density identity")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Geometric Field Lift 76: Linear Metric Strain Variation

## Purpose

This report validates the safest first geometric lift from the scalar bridge:
a componentwise weak-field strain energy for a symmetric perturbation `h_ij`.

It does not derive general relativity. It only proves the Euler-Lagrange
equations of the naive componentwise model.

## Validated Checks

{validation_bullets}

## Energy

The tested energy is:

```text
E[h] =
  1/2 integral sum_ij |grad h_ij|^2 dV
  - integral sum_ij S_ij h_ij dV.
```

For each component:

```text
grad h_ij . grad v_ij - S_ij v_ij
  =
  div(v_ij grad h_ij)
  + (-Delta h_ij - S_ij)v_ij.
```

Therefore the interior Euler-Lagrange equation is:

```text
-Delta h_ij = S_ij.
```

## Interpretation

This is the direct multi-component analogue of the scalar boundary-flux bridge.
It is useful as a baseline, but it is not yet a gauge-invariant spin-2 theory.
"""

out = Path(__file__).with_name("76_linear_metric_strain_variation.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
