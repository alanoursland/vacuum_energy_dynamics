#!/usr/bin/env python3
"""
make_79_linearized_gauge_transform.py

Validate basic linearized gauge bookkeeping for a flat-index perturbation:

    h'_ab = h_ab + partial_a xi_b + partial_b xi_a.

This script uses Euclidean flat-index contractions for symbolic bookkeeping.
Signature signs are not the point here.

Output:
    79_linearized_gauge_transform.md
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

xi = [sp.Function(f"xi{a}")(*coords) for a in range(dim)]
h = [[sp.Function(f"h{a}{b}")(*coords) for b in range(dim)] for a in range(dim)]

hprime = [
    [
        h[a][b] + sp.diff(xi[b], coords[a]) + sp.diff(xi[a], coords[b])
        for b in range(dim)
    ]
    for a in range(dim)
]

trace_h = sum(h[a][a] for a in range(dim))
trace_hprime = sum(hprime[a][a] for a in range(dim))
div_xi = sum(sp.diff(xi[a], coords[a]) for a in range(dim))

require_equal("linearized trace gauge transform", trace_hprime - trace_h, 2 * div_xi)
checks.append("linearized trace gauge transform")

for a in range(dim):
    for b in range(dim):
        require_equal(
            f"gauge transform symmetry {a}{b}",
            hprime[a][b] - hprime[b][a],
            h[a][b] - h[b][a],
        )

checks.append("symmetric perturbations remain symmetric")

# Divergence of transformed perturbation:
#   partial^a h'_ab = partial^a h_ab + Delta xi_b + partial_b div xi.
def flat_lap(expr):
    return sum(sp.diff(expr, c, 2) for c in coords)


for b in range(dim):
    div_h = sum(sp.diff(h[a][b], coords[a]) for a in range(dim))
    div_hprime = sum(sp.diff(hprime[a][b], coords[a]) for a in range(dim))
    expected = div_h + flat_lap(xi[b]) + sp.diff(div_xi, coords[b])
    require_equal(f"divergence gauge transform component {b}", div_hprime, expected)

checks.append("linearized divergence gauge transform")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Geometric Field Lift 79: Linearized Gauge Transform

## Purpose

This report validates basic linearized gauge bookkeeping for a flat-index
perturbation.

The script uses Euclidean flat-index contractions for symbolic bookkeeping.
Metric-signature issues are deferred to later linearized-GR checks.

## Validated Checks

{validation_bullets}

## Gauge Transform

The linearized coordinate/gauge transform is:

```text
h'_ab = h_ab + partial_a xi_b + partial_b xi_a.
```

The trace transforms as:

```text
h' = h + 2 partial_a xi_a.
```

The divergence transforms as:

```text
partial_a h'_ab
  =
  partial_a h_ab
  + Delta xi_b
  + partial_b(partial_a xi_a).
```

## Interpretation

The componentwise strain model has coordinate redundancy once `h_ab` is read as
a metric perturbation. Any geometric lift must account for this gauge freedom.
"""

out = Path(__file__).with_name("79_linearized_gauge_transform.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
