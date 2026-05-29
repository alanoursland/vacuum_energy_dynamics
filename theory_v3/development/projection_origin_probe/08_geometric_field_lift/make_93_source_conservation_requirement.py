#!/usr/bin/env python3
"""
make_93_source_conservation_requirement.py

Validate that the linearized Einstein equation requires source conservation:

    G_ab = kappa T_ab
    partial^a G_ab = 0

implies:

    partial^a T_ab = 0.

Output:
    93_source_conservation_requirement.md
"""

from pathlib import Path
import sympy as sp


t, x, y, z = sp.symbols("t x y z", real=True)
coords = (t, x, y, z)
eta = [-1, 1, 1, 1]
dim = 4
kappa = sp.symbols("kappa", nonzero=True)


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


def hsym(a, b):
    i, j = sorted((a, b))
    return sp.Function(f"h{i}{j}")(*coords)


def Tsym(a, b):
    i, j = sorted((a, b))
    return sp.Function(f"T{i}{j}")(*coords)


def d_up(a, expr):
    return eta[a] * sp.diff(expr, coords[a])


def box(expr):
    return sum(eta[a] * sp.diff(expr, coords[a], 2) for a in range(dim))


checks = []

h = [[hsym(a, b) for b in range(dim)] for a in range(dim)]
T = [[Tsym(a, b) for b in range(dim)] for a in range(dim)]
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
    div_G = sum(d_up(a, G_linear(a, b)) for a in range(dim))
    div_T = sum(d_up(a, T[a][b]) for a in range(dim))
    div_residual = sum(d_up(a, G_linear(a, b) - kappa * T[a][b]) for a in range(dim))

    require_zero(f"Bianchi identity component {b}", div_G)
    require_equal(f"field-equation divergence component {b}", div_residual, -kappa * div_T)

checks.append("field-equation divergence requires source conservation")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Geometric Field Lift 93: Source Conservation Requirement

## Purpose

This report validates the source-conservation requirement in the linearized
geometric field equation.

## Validated Checks

{validation_bullets}

## Field Equation

Let:

```text
G_ab = kappa T_ab.
```

The linearized Bianchi identity gives:

```text
partial^a G_ab = 0.
```

Taking the divergence of the field equation therefore gives:

```text
0 = kappa partial^a T_ab.
```

For nonzero `kappa`:

```text
partial^a T_ab = 0.
```

## Interpretation

The geometric lift imposes a conservation law on admissible sources. This is a
stronger structural requirement than the scalar bridge alone.
"""

out = Path(__file__).with_name("93_source_conservation_requirement.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
