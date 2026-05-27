#!/usr/bin/env python3
"""
make_90_componentwise_strain_failure_modes.py

Validate why the naive componentwise strain operator cannot be the final
geometric field operator.

For a pure gauge perturbation:

    h_ab = partial_a xi_b + partial_b xi_a,

the componentwise wave operator is generally nonzero, while the linearized
Einstein tensor vanishes.

Output:
    90_componentwise_strain_failure_modes.md
"""

from pathlib import Path
import sympy as sp


t, x, y, z = sp.symbols("t x y z", real=True)
coords = (t, x, y, z)
eta = [-1, 1, 1, 1]
dim = 4


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


def d_up(a, expr):
    return eta[a] * sp.diff(expr, coords[a])


def box(expr):
    return sum(eta[a] * sp.diff(expr, coords[a], 2) for a in range(dim))


checks = []

xi = [sp.Function(f"xi{a}")(*coords) for a in range(dim)]
h = [
    [
        sp.diff(xi[b], coords[a]) + sp.diff(xi[a], coords[b])
        for b in range(dim)
    ]
    for a in range(dim)
]

# Componentwise operator on pure gauge.
for a in range(dim):
    for b in range(dim):
        comp_op = -sp.Rational(1, 2) * box(h[a][b])
        expected = -sp.Rational(1, 2) * (
            sp.diff(box(xi[b]), coords[a]) + sp.diff(box(xi[a]), coords[b])
        )
        require_equal(f"componentwise pure-gauge operator {a}{b}", comp_op, expected)

checks.append("componentwise pure-gauge operator is generally nonzero")

trace_h = sum(eta[a] * h[a][a] for a in range(dim))


def Ricci(a, b):
    term1 = sum(d_up(c, sp.diff(h[b][c], coords[a])) for c in range(dim))
    term2 = sum(d_up(c, sp.diff(h[a][c], coords[b])) for c in range(dim))
    return sp.Rational(1, 2) * (
        term1 + term2 - box(h[a][b]) - sp.diff(trace_h, coords[a], coords[b])
    )


R_scalar = sum(eta[a] * Ricci(a, a) for a in range(dim))


def Einstein(a, b):
    return Ricci(a, b) - sp.Rational(1, 2) * (eta[a] if a == b else 0) * R_scalar


for a in range(dim):
    for b in range(dim):
        require_zero(f"pure-gauge linearized Einstein tensor {a}{b}", Einstein(a, b))

checks.append("linearized Einstein tensor vanishes for pure gauge")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Geometric Field Lift 90: Componentwise Strain Failure Modes

## Purpose

This report validates why the naive componentwise strain operator cannot be the
final geometric field operator.

## Validated Checks

{validation_bullets}

## Pure Gauge Perturbation

For:

```text
h_ab = partial_a xi_b + partial_b xi_a,
```

the naive componentwise operator gives:

```text
-1/2 box h_ab
  =
  -1/2(partial_a box xi_b + partial_b box xi_a).
```

This is generally nonzero.

## Linearized Einstein Operator

For the same pure gauge perturbation, SymPy verifies:

```text
G_ab = 0.
```

## Interpretation

The componentwise scalar strain model is useful only as a baseline and for the
trace/Newtonian sector. A geometric field equation needs the trace/divergence
terms of the Fierz-Pauli / linearized Einstein operator to remove pure gauge
artifacts.
"""

out = Path(__file__).with_name("90_componentwise_strain_failure_modes.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
