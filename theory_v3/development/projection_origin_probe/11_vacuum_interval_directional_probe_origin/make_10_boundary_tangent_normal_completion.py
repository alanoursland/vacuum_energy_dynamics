#!/usr/bin/env python3
"""
make_10_boundary_tangent_normal_completion.py

Validate the split between tangent induced metric probes and the additional
normal/mixed probes needed for the full bulk metric at a boundary.

Output:
    10_boundary_tangent_normal_completion.md
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

e1 = sp.Matrix([1, 0, 0])
e2 = sp.Matrix([0, 1, 0])
n = sp.Matrix([0, 0, 1])


def Q(v):
    return simplify_expr((v.T * G * v)[0])


tangent_recoveries = {
    g11: Q(e1),
    g22: Q(e2),
    g12: simplify_expr((Q(e1 + e2) - Q(e1) - Q(e2)) / 2),
}

normal_recoveries = {
    g33: Q(n),
    g13: simplify_expr((Q(e1 + n) - Q(e1) - Q(n)) / 2),
    g23: simplify_expr((Q(e2 + n) - Q(e2) - Q(n)) / 2),
}

for component, expression in tangent_recoveries.items():
    require_zero(f"tangent recover {component}", expression - component)

for component, expression in normal_recoveries.items():
    require_zero(f"normal recover {component}", expression - component)

tangent_probe_set = [Q(e1), Q(e2), Q(e1 + e2)]
for variable in [g13, g23, g33]:
    for probe in tangent_probe_set:
        require_zero(f"tangent set blind to {variable}", sp.diff(probe, variable))

md = """# Vacuum Interval Directional Probe Origin 10: Boundary Tangent-Normal Completion

## Purpose

This proof separates induced boundary metric data from full bulk boundary data.

Tangent interval probes recover `h_ab`. Normal and mixed probes are additional
data.

## Validated Checks

- tangent probes recover `g11`, `g22`, and `g12`: passed
- tangent probes are blind to `g13`, `g23`, and `g33`: passed
- normal and mixed probes recover `g33`, `g13`, and `g23`: passed

## Tangent Data

For boundary tangent vectors `e1`, `e2`:

```text
g11 = Q(e1)
g22 = Q(e2)
g12 = (Q(e1+e2)-Q(e1)-Q(e2))/2.
```

These are the induced boundary metric components.

## Normal/Mixed Data

With normal vector `n`:

```text
g33 = Q(n)
g13 = (Q(e1+n)-Q(e1)-Q(n))/2
g23 = (Q(e2+n)-Q(e2)-Q(n))/2.
```

## Interpretation

The boundary selector has two levels:

```text
tangent interval probes -> induced boundary metric
tangent + normal/mixed probes -> full bulk metric split at the boundary
```

This matters because GHY-type boundary data starts with the induced metric, but
extrinsic curvature and normal evolution require the second level.
"""

out = Path(__file__).with_name("10_boundary_tangent_normal_completion.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Boundary tangent-normal completion passed.")
print(f"Wrote {out.resolve()}")

