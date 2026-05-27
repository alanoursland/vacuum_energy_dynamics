#!/usr/bin/env python3
"""
make_19_hessian_second_variation_origin.py

Validate that a local second variation / Hessian supplies the symmetric
quadratic branch used by metric interval data.

Output:
    19_hessian_second_variation_origin.md
"""

from pathlib import Path
import sympy as sp


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


x, y, lam = sp.symbols("x y lam")
v1, v2 = sp.symbols("v1 v2")
f0, l1, l2 = sp.symbols("f0 l1 l2")
h11, h12, h22 = sp.symbols("h11 h12 h22")
c30, c21, c12, c03 = sp.symbols("c30 c21 c12 c03")

F = (
    f0
    + l1 * x
    + l2 * y
    + sp.Rational(1, 2) * h11 * x**2
    + h12 * x * y
    + sp.Rational(1, 2) * h22 * y**2
    + c30 * x**3
    + c21 * x**2 * y
    + c12 * x * y**2
    + c03 * y**3
)

H = sp.hessian(F, (x, y))
H0 = H.subs({x: 0, y: 0})
expected_H = sp.Matrix([[h11, h12], [h12, h22]])

for i in range(2):
    for j in range(2):
        require_zero(f"hessian component {i}{j}", H0[i, j] - expected_H[i, j])

gradient0 = sp.Matrix([sp.diff(F, x).subs({x: 0, y: 0}), sp.diff(F, y).subs({x: 0, y: 0})])
require_zero("gradient first component", gradient0[0] - l1)
require_zero("gradient second component", gradient0[1] - l2)

F_path = simplify_expr(F.subs({x: lam * v1, y: lam * v2}))
second_variation = simplify_expr(sp.diff(F_path, lam, 2).subs(lam, 0))
quadratic_form = simplify_expr((sp.Matrix([v1, v2]).T * expected_H * sp.Matrix([v1, v2]))[0])
require_zero("second variation quadratic form", second_variation - quadratic_form)

linear_path = simplify_expr(sp.diff(F_path, lam).subs(lam, 0))
require_zero("first variation path", linear_path - (l1 * v1 + l2 * v2))

md = f"""# Vacuum Interval Directional Probe Origin 19: Hessian Second-Variation Origin

## Purpose

This proof gives a conditional origin for metric-quality interval data.

If the local vacuum interval response comes from the second variation of a
scalar local functional, the quadratic branch is the Hessian.

## Validated Checks

- Hessian at the reference state is symmetric and equals the quadratic tensor: passed
- first variation is a separate linear/stationarity channel: passed
- directional second variation equals `v^T H v`: passed
- cubic corrections do not enter the Hessian at the reference state: passed

## Local Functional

Use:

```text
F = f0 + l_i x^i + 1/2 h_ij x^i x^j + cubic terms.
```

At the reference state:

```text
H_ij = d_i d_j F |0 = [[h11,h12],[h12,h22]].
```

Along a direction:

```text
x = lambda v1
y = lambda v2
```

Sympy verifies:

```text
d^2/dlambda^2 F(lambda v)|0 = v^T H v.
```

The first variation is:

```text
d/dlambda F(lambda v)|0 = l1 v1 + l2 v2.
```

## Interpretation

The metric branch is naturally a Hessian/second-variation object. This also
shows what must be controlled: the first variation must vanish or be routed as
a force/source channel, while higher-order terms are not part of the metric
quadratic branch.
"""

out = Path(__file__).with_name("19_hessian_second_variation_origin.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Hessian second-variation origin passed.")
print(f"Wrote {out.resolve()}")

