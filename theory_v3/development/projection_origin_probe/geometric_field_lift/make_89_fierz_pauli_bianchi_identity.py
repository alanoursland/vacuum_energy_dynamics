#!/usr/bin/env python3
"""
make_89_fierz_pauli_bianchi_identity.py

Validate the linearized Bianchi identity for the Fierz-Pauli / linearized
Einstein operator:

    partial^a G_ab = 0.

Output:
    89_fierz_pauli_bianchi_identity.md
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


def C(b):
    return sum(d_up(a, bar[a][b]) for a in range(dim))


div_C = sum(d_up(c, C(c)) for c in range(dim))


def G_linear(a, b):
    return (
        -sp.Rational(1, 2) * box(bar[a][b])
        + sp.Rational(1, 2) * sp.diff(C(b), coords[a])
        + sp.Rational(1, 2) * sp.diff(C(a), coords[b])
        - sp.Rational(1, 2) * (eta[a] if a == b else 0) * div_C
    )


for b in range(dim):
    divergence = sum(d_up(a, G_linear(a, b)) for a in range(dim))
    require_zero(f"linearized Bianchi identity component {b}", divergence)

checks.append("linearized Bianchi identity verified for all components")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Geometric Field Lift 89: Fierz-Pauli Bianchi Identity

## Purpose

This report validates the conservation identity of the Fierz-Pauli /
linearized Einstein operator.

## Validated Checks

{validation_bullets}

## Operator

Using trace-reversed variables:

```text
C_b = partial^a bar h_ab.
```

The linearized Einstein operator is:

```text
G_ab
  =
  -1/2 box bar h_ab
  + 1/2 partial_a C_b
  + 1/2 partial_b C_a
  - 1/2 eta_ab partial^c C_c.
```

SymPy verifies:

```text
partial^a G_ab = 0.
```

## Interpretation

This identity is essential: it forces source conservation in the linearized
geometric theory. A naive componentwise Laplacian does not carry this structure
by itself.
"""

out = Path(__file__).with_name("89_fierz_pauli_bianchi_identity.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
