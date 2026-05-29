#!/usr/bin/env python3
"""
make_5_boundary_induced_metric_projection.py

Validate that tangent interval probes recover induced boundary metric data,
while normal components require separate extrinsic/bulk information.

Output:
    5_boundary_induced_metric_projection.md
"""

from pathlib import Path
import sympy as sp


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


g11, g22, g33, g12, g13, g23 = sp.symbols("g11 g22 g33 g12 g13 g23")

G = sp.Matrix(
    [
        [g11, g12, g13],
        [g12, g22, g23],
        [g13, g23, g33],
    ]
)

# Boundary tangent basis for the plane x3 = constant.
E = sp.Matrix(
    [
        [1, 0],
        [0, 1],
        [0, 0],
    ]
)

H = sp.simplify(E.T * G * E)
expected_H = sp.Matrix([[g11, g12], [g12, g22]])

for i in range(2):
    for j in range(2):
        require_zero(f"induced metric component {i}{j}", H[i, j] - expected_H[i, j])

normal_variables = [g13, g23, g33]
for variable in normal_variables:
    for entry in H:
        require_zero(f"tangent induced metric independent of {variable}", sp.diff(entry, variable))

v1, v2 = sp.symbols("v1 v2")
v_boundary = sp.Matrix([v1, v2])
Q_boundary = simplify_expr((v_boundary.T * H * v_boundary)[0])
Q_expected = simplify_expr(g11 * v1**2 + 2 * g12 * v1 * v2 + g22 * v2**2)
require_zero("boundary interval quadratic form", Q_boundary - Q_expected)

validation_bullets = "\n".join(
    [
        "- tangent probes recover the induced boundary metric h_ab: passed",
        "- tangent probes are blind to normal/bulk components: passed",
        "- boundary interval quadratic form matches h_ab v^a v^b: passed",
    ]
)

md = f"""# Vacuum Interval Directional Probe Origin 5: Boundary Induced Metric Projection

## Purpose

This proof clarifies exactly what boundary interval probes can recover.

Tangent directional interval probes recover the induced boundary metric. They
do not recover normal/bulk components without additional extrinsic information.

## Validated Checks

{validation_bullets}

## Projection

For a 3D symmetric bulk form:

```text
G = [[g11,g12,g13],
     [g12,g22,g23],
     [g13,g23,g33]]
```

and boundary tangent basis:

```text
E = [[1,0],
     [0,1],
     [0,0]]
```

the induced metric is:

```text
h = E^T G E = [[g11,g12],[g12,g22]].
```

The tangent interval is:

```text
Q_boundary(v) = g11 v1^2 + 2 g12 v1 v2 + g22 v2^2.
```

## Interpretation

Directional interval data can close the induced-boundary-metric gate, but not
the full bulk-normal gate. Normal data, extrinsic curvature, or boundary
embedding information must enter separately when the action requires it.
"""

out = Path(__file__).with_name("5_boundary_induced_metric_projection.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Boundary induced metric projection passed.")
print(f"Wrote {out.resolve()}")

