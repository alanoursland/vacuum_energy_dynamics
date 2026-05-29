#!/usr/bin/env python3
"""
make_80_trace_divergence_decomposition.py

Validate trace-reversal and de Donder-style divergence bookkeeping in four flat
dimensions, using Euclidean contractions for symbolic clarity.

Output:
    80_trace_divergence_decomposition.md
"""

from pathlib import Path
import sympy as sp


t, x, y, z = sp.symbols("t x y z", real=True)
coords = (t, x, y, z)
dim = 4


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

h = [[sp.Function(f"h{a}{b}")(*coords) for b in range(dim)] for a in range(dim)]
trace_h = sum(h[a][a] for a in range(dim))

bar = [
    [
        h[a][b] - sp.Rational(1, 2) * (1 if a == b else 0) * trace_h
        for b in range(dim)
    ]
    for a in range(dim)
]

trace_bar = sum(bar[a][a] for a in range(dim))
require_equal("trace reversal flips trace in four dimensions", trace_bar, -trace_h)
checks.append("trace reversal flips trace in four dimensions")

barbar_trace = trace_bar
barbar = [
    [
        bar[a][b] - sp.Rational(1, 2) * (1 if a == b else 0) * barbar_trace
        for b in range(dim)
    ]
    for a in range(dim)
]

for a in range(dim):
    for b in range(dim):
        require_equal(f"trace reversal is involutive {a}{b}", barbar[a][b], h[a][b])

checks.append("trace reversal is involutive in four dimensions")

for b in range(dim):
    div_bar = sum(sp.diff(bar[a][b], coords[a]) for a in range(dim))
    div_h = sum(sp.diff(h[a][b], coords[a]) for a in range(dim))
    expected = div_h - sp.Rational(1, 2) * sp.diff(trace_h, coords[b])
    require_equal(f"de Donder vector component {b}", div_bar, expected)

checks.append("trace-reversed divergence identity")

# Gauge transform of de Donder vector C_b = partial_a bar h_ab.
xi = [sp.Function(f"xi{a}")(*coords) for a in range(dim)]
div_xi = sum(sp.diff(xi[a], coords[a]) for a in range(dim))

hprime = [
    [
        h[a][b] + sp.diff(xi[b], coords[a]) + sp.diff(xi[a], coords[b])
        for b in range(dim)
    ]
    for a in range(dim)
]
trace_hprime = sum(hprime[a][a] for a in range(dim))
barprime = [
    [
        hprime[a][b] - sp.Rational(1, 2) * (1 if a == b else 0) * trace_hprime
        for b in range(dim)
    ]
    for a in range(dim)
]

def flat_lap(expr):
    return sum(sp.diff(expr, c, 2) for c in coords)


for b in range(dim):
    C = sum(sp.diff(bar[a][b], coords[a]) for a in range(dim))
    Cprime = sum(sp.diff(barprime[a][b], coords[a]) for a in range(dim))
    require_equal(f"de Donder vector gauge transform {b}", Cprime - C, flat_lap(xi[b]))

checks.append("de Donder vector gauge transform")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Geometric Field Lift 80: Trace-Divergence Decomposition

## Purpose

This report validates trace-reversal and de Donder-style divergence bookkeeping
for a four-dimensional flat-index perturbation.

The script uses Euclidean contractions for symbolic clarity. Later scripts can
repeat the calculation with explicit Minkowski signs if needed.

## Validated Checks

{validation_bullets}

## Trace Reversal

Define:

```text
bar h_ab = h_ab - 1/2 delta_ab h.
```

In four dimensions:

```text
bar h = -h.
```

Applying trace reversal twice returns the original perturbation:

```text
bar(bar h)_ab = h_ab.
```

## De Donder Vector

The trace-reversed divergence is:

```text
C_b = partial_a bar h_ab
    = partial_a h_ab - 1/2 partial_b h.
```

Under:

```text
h'_ab = h_ab + partial_a xi_b + partial_b xi_a,
```

SymPy verifies:

```text
C'_b - C_b = Delta xi_b.
```

## Interpretation

The trace/divergence decomposition identifies the gauge-controlled part of a
metric perturbation. This is the first warning that the componentwise scalar
strain lift is incomplete as a geometric theory.
"""

out = Path(__file__).with_name("80_trace_divergence_decomposition.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
