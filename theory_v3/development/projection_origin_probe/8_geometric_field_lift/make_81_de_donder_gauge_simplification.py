#!/usr/bin/env python3
"""
make_81_de_donder_gauge_simplification.py

Validate the Minkowski-sign linearized gauge bookkeeping for the trace-reversed
perturbation:

    bar_h_ab = h_ab - 1/2 eta_ab h.

Under h'_ab = h_ab + partial_a xi_b + partial_b xi_a, the de Donder vector:

    C_b = partial^a bar_h_ab

transforms as:

    C'_b - C_b = box xi_b.

Output:
    81_de_donder_gauge_simplification.md
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
xi = [sp.Function(f"xi{a}")(*coords) for a in range(dim)]

trace_h = sum(eta[a] * h[a][a] for a in range(dim))
div_xi_up = sum(d_up(a, xi[a]) for a in range(dim))

hprime = [
    [
        h[a][b] + sp.diff(xi[b], coords[a]) + sp.diff(xi[a], coords[b])
        for b in range(dim)
    ]
    for a in range(dim)
]
trace_hprime = sum(eta[a] * hprime[a][a] for a in range(dim))

require_equal("Minkowski trace gauge transform", trace_hprime - trace_h, 2 * div_xi_up)
checks.append("Minkowski trace gauge transform")

bar = [
    [
        h[a][b] - sp.Rational(1, 2) * (eta[a] if a == b else 0) * trace_h
        for b in range(dim)
    ]
    for a in range(dim)
]
barprime = [
    [
        hprime[a][b] - sp.Rational(1, 2) * (eta[a] if a == b else 0) * trace_hprime
        for b in range(dim)
    ]
    for a in range(dim)
]

for a in range(dim):
    for b in range(dim):
        delta_bar = sp.simplify(barprime[a][b] - bar[a][b])
        expected = (
            sp.diff(xi[b], coords[a])
            + sp.diff(xi[a], coords[b])
            - (eta[a] if a == b else 0) * div_xi_up
        )
        require_equal(f"trace-reversed gauge transform {a}{b}", delta_bar, expected)

checks.append("trace-reversed perturbation gauge transform")

for b in range(dim):
    C = sum(d_up(a, bar[a][b]) for a in range(dim))
    Cprime = sum(d_up(a, barprime[a][b]) for a in range(dim))
    require_equal(f"de Donder vector transform component {b}", Cprime - C, box(xi[b]))

checks.append("de Donder vector transforms by box xi_b")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Geometric Field Lift 81: de Donder Gauge Simplification

## Purpose

This report repeats the trace/divergence gauge bookkeeping with Minkowski signs.

## Validated Checks

{validation_bullets}

## Trace-Reversed Perturbation

Define:

```text
bar h_ab = h_ab - 1/2 eta_ab h
h = eta^ab h_ab.
```

Under:

```text
h'_ab = h_ab + partial_a xi_b + partial_b xi_a,
```

SymPy verifies:

```text
bar h'_ab - bar h_ab
  =
  partial_a xi_b + partial_b xi_a - eta_ab partial^c xi_c.
```

## de Donder Vector

Define:

```text
C_b = partial^a bar h_ab.
```

Then:

```text
C'_b - C_b = box xi_b.
```

## Interpretation

The de Donder condition:

```text
partial^a bar h_ab = 0
```

is reachable, at the linearized level, by solving:

```text
box xi_b = -C_b.
```

This is the gauge step needed before the linearized Einstein operator reduces
to a simple wave/Laplace operator on `bar h_ab`.
"""

out = Path(__file__).with_name("81_de_donder_gauge_simplification.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
