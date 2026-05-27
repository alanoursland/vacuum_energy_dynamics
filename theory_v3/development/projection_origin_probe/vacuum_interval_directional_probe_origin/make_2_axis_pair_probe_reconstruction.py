#!/usr/bin/env python3
"""
make_2_axis_pair_probe_reconstruction.py

Validate that a finite axis-plus-pair probe set reconstructs all components of
a symmetric 3D bilinear form.

Output:
    2_axis_pair_probe_reconstruction.md
"""

from pathlib import Path
import sympy as sp


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


h11, h22, h33, h12, h13, h23 = sp.symbols("h11 h22 h33 h12 h13 h23")

H = sp.Matrix(
    [
        [h11, h12, h13],
        [h12, h22, h23],
        [h13, h23, h33],
    ]
)

e1 = sp.Matrix([1, 0, 0])
e2 = sp.Matrix([0, 1, 0])
e3 = sp.Matrix([0, 0, 1])


def Q(v):
    return simplify_expr((v.T * H * v)[0])


probes = [
    Q(e1),
    Q(e2),
    Q(e3),
    Q(e1 + e2),
    Q(e1 + e3),
    Q(e2 + e3),
]

components = [h11, h22, h33, h12, h13, h23]
probe_matrix = sp.Matrix(
    [[sp.diff(probe, component) for component in components] for probe in probes]
)
det_probe = simplify_expr(probe_matrix.det())

if det_probe == 0:
    raise AssertionError("axis-plus-pair probe matrix is singular")

recover = {
    h11: probes[0],
    h22: probes[1],
    h33: probes[2],
    h12: simplify_expr((probes[3] - probes[0] - probes[1]) / 2),
    h13: simplify_expr((probes[4] - probes[0] - probes[2]) / 2),
    h23: simplify_expr((probes[5] - probes[1] - probes[2]) / 2),
}

for component, expression in recover.items():
    require_zero(f"recover {component}", expression - component)

validation_bullets = "\n".join(
    [
        "- six directional probes match the six symmetric 3D components: passed",
        f"- probe matrix determinant is nonzero: det = {det_probe}",
        "- off-diagonal components are recovered by pair probes: passed",
    ]
)

md = f"""# Vacuum Interval Directional Probe Origin 2: Axis-Pair Probe Reconstruction

## Purpose

This proof validates that full symmetric tensor data can be recovered from a
finite set of local interval comparisons.

## Validated Checks

{validation_bullets}

## Probe Set

For a symmetric 3D form:

```text
H = [[h11,h12,h13],
     [h12,h22,h23],
     [h13,h23,h33]]
```

use:

```text
Q(e1)
Q(e2)
Q(e3)
Q(e1+e2)
Q(e1+e3)
Q(e2+e3)
```

The probe matrix determinant is:

```text
det = {det_probe}
```

so the probe map is invertible.

## Recovered Components

```text
h11 = Q(e1)
h22 = Q(e2)
h33 = Q(e3)
h12 = (Q(e1+e2)-Q(e1)-Q(e2))/2
h13 = (Q(e1+e3)-Q(e1)-Q(e3))/2
h23 = (Q(e2+e3)-Q(e2)-Q(e3))/2
```

## Interpretation

The selector does not need a continuum of directions. In 3D, six local
interval comparisons are already enough to reconstruct the six components of a
symmetric metric-like tensor at a point.
"""

out = Path(__file__).with_name("2_axis_pair_probe_reconstruction.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Axis-pair probe reconstruction passed.")
print(f"Wrote {out.resolve()}")

