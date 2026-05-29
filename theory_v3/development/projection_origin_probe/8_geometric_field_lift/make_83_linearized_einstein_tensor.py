#!/usr/bin/env python3
"""
make_83_linearized_einstein_tensor.py

Validate the linearized Einstein tensor in trace-reversed variables:

    G_ab = -1/2 box bar_h_ab
           +1/2 partial_a C_b
           +1/2 partial_b C_a
           -1/2 eta_ab partial^c C_c

where C_b = partial^a bar_h_ab.

Output:
    83_linearized_einstein_tensor.md
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


def hsym(a, b):
    i, j = sorted((a, b))
    return sp.Function(f"h{i}{j}")(*coords)


def d_up(a, expr):
    return eta[a] * sp.diff(expr, coords[a])


def box(expr):
    return sum(eta[a] * sp.diff(expr, coords[a], 2) for a in range(dim))


checks = []

h = [[hsym(a, b) for b in range(dim)] for a in range(dim)]
trace_h = sum(eta[a] * h[a][a] for a in range(dim))
bar = [
    [
        h[a][b] - sp.Rational(1, 2) * (eta[a] if a == b else 0) * trace_h
        for b in range(dim)
    ]
    for a in range(dim)
]


def Ricci(a, b):
    term1 = sum(d_up(c, sp.diff(h[b][c], coords[a])) for c in range(dim))
    term2 = sum(d_up(c, sp.diff(h[a][c], coords[b])) for c in range(dim))
    return sp.Rational(1, 2) * (
        term1 + term2 - box(h[a][b]) - sp.diff(trace_h, coords[a], coords[b])
    )


R_scalar = sum(eta[a] * Ricci(a, a) for a in range(dim))


def Einstein(a, b):
    return Ricci(a, b) - sp.Rational(1, 2) * (eta[a] if a == b else 0) * R_scalar


def C(b):
    return sum(d_up(a, bar[a][b]) for a in range(dim))


div_C = sum(d_up(c, C(c)) for c in range(dim))


def Einstein_bar_formula(a, b):
    return (
        -sp.Rational(1, 2) * box(bar[a][b])
        + sp.Rational(1, 2) * sp.diff(C(b), coords[a])
        + sp.Rational(1, 2) * sp.diff(C(a), coords[b])
        - sp.Rational(1, 2) * (eta[a] if a == b else 0) * div_C
    )


for a in range(dim):
    for b in range(dim):
        require_equal(
            f"linearized Einstein trace-reversed formula {a}{b}",
            Einstein(a, b),
            Einstein_bar_formula(a, b),
        )

checks.append("linearized Einstein trace-reversed formula verified for all components")

for a in range(dim):
    for b in range(dim):
        de_donder_remainder = sp.simplify(
            Einstein_bar_formula(a, b)
            + sp.Rational(1, 2) * box(bar[a][b])
        )
        gauge_terms = (
            sp.Rational(1, 2) * sp.diff(C(b), coords[a])
            + sp.Rational(1, 2) * sp.diff(C(a), coords[b])
            - sp.Rational(1, 2) * (eta[a] if a == b else 0) * div_C
        )
        require_equal(f"de Donder remainder is gauge terms {a}{b}", de_donder_remainder, gauge_terms)

checks.append("de Donder simplification remainder isolated")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Geometric Field Lift 83: Linearized Einstein Tensor

## Purpose

This report validates the linearized Einstein tensor in trace-reversed
variables.

## Validated Checks

{validation_bullets}

## Trace-Reversed Form

Define:

```text
bar h_ab = h_ab - 1/2 eta_ab h
C_b = partial^a bar h_ab.
```

SymPy verifies:

```text
G_ab
  =
  -1/2 box bar h_ab
  + 1/2 partial_a C_b
  + 1/2 partial_b C_a
  - 1/2 eta_ab partial^c C_c.
```

## de Donder Gauge

In de Donder gauge:

```text
C_b = 0,
```

the operator reduces to:

```text
G_ab = -1/2 box bar h_ab.
```

## Interpretation

This is the controlled replacement for the naive componentwise Laplacian. The
componentwise scalar bridge is recovered only after gauge and trace-reversal
bookkeeping are handled.

This imports the standard massless spin-2 weak-field operator. The report does
not by itself prove that the vacuum ontology uniquely forces this operator.
"""

out = Path(__file__).with_name("83_linearized_einstein_tensor.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
