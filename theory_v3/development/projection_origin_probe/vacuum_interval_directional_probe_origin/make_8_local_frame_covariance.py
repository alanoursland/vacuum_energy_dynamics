#!/usr/bin/env python3
"""
make_8_local_frame_covariance.py

Validate that the recovered bilinear form transforms as a metric-like tensor
under a local frame change.

Output:
    8_local_frame_covariance.md
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
p11, p12, p21, p22 = sp.symbols("p11 p12 p21 p22")
y1, y2 = sp.symbols("y1 y2")

H = sp.Matrix([[h11, h12], [h12, h22]])
P = sp.Matrix([[p11, p12], [p21, p22]])
y = sp.Matrix([y1, y2])

x = P * y
H_prime = simplify_expr(P.T * H * P)

old_interval = simplify_expr((x.T * H * x)[0])
new_interval = simplify_expr((y.T * H_prime * y)[0])
require_zero("frame covariance of interval", new_interval - old_interval)

det_relation = simplify_expr(H_prime.det() - (P.det() ** 2) * H.det())
require_zero("determinant density relation", det_relation)

md = f"""# Vacuum Interval Directional Probe Origin 8: Local Frame Covariance

## Purpose

This proof checks that the reconstructed interval object has the correct
change-of-frame behavior.

## Validated Checks

- interval value is invariant under component/frame relabeling: passed
- determinant transforms by the square of the frame determinant: passed

## Frame Change

Let:

```text
x = P y
Q(x) = x^T H x.
```

The same interval written in the `y` frame is:

```text
Q(y) = y^T H' y
H' = P^T H P.
```

Sympy verifies:

```text
y^T(P^T H P)y = (Py)^T H(Py).
```

It also verifies:

```text
det(H') = det(P)^2 det(H).
```

## Interpretation

Once directional interval probes reconstruct `H`, the recovered object behaves
as a symmetric covariant tensor under local frame changes. This is the correct
transformation behavior for induced metric data.
"""

out = Path(__file__).with_name("8_local_frame_covariance.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Local frame covariance passed.")
print(f"Wrote {out.resolve()}")

