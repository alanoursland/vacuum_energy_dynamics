#!/usr/bin/env python3
"""
make_92_fierz_pauli_action_variation.py

Validate the quadratic Fierz-Pauli / linearized Einstein action variation in
momentum-space algebra.

Using symmetric h_ab and Minkowski eta, define:

    L2 = 1/2 h^ab G_ab[h],

where G_ab is the linearized Einstein tensor.  The derivative of L2 with
respect to each independent symmetric component h_ab gives the corresponding
linearized Einstein equation, with the expected factor of 2 for off-diagonal
components.

Output:
    92_fierz_pauli_action_variation.md
"""

from pathlib import Path
import sympy as sp


dim = 4
eta = [-1, 1, 1, 1]
k = sp.symbols("k0:4", real=True)


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


def symvar(a, b):
    i, j = sorted((a, b))
    return sp.symbols(f"H{i}{j}", real=True)


H = [[symvar(a, b) for b in range(dim)] for a in range(dim)]
trace_H = sum(eta[a] * H[a][a] for a in range(dim))
k2 = sum(eta[a] * k[a] ** 2 for a in range(dim))


def divH(b):
    return sum(eta[c] * k[c] * H[b][c] for c in range(dim))


def Ricci(a, b):
    return sp.Rational(1, 2) * (
        k[a] * divH(b)
        + k[b] * divH(a)
        - k2 * H[a][b]
        - k[a] * k[b] * trace_H
    )


R_scalar = sum(eta[a] * Ricci(a, a) for a in range(dim))


def Einstein(a, b):
    return sp.simplify(Ricci(a, b) - sp.Rational(1, 2) * (eta[a] if a == b else 0) * R_scalar)


checks = []

L2 = sp.Rational(1, 2) * sum(
    eta[a] * eta[b] * H[a][b] * Einstein(a, b)
    for a in range(dim)
    for b in range(dim)
)

for a in range(dim):
    for b in range(a, dim):
        var = H[a][b]
        derivative = sp.diff(L2, var)
        multiplicity = 2 if a != b else 1
        target = multiplicity * eta[a] * eta[b] * Einstein(a, b)
        require_equal(f"action derivative component {a}{b}", derivative, target)

checks.append("Fierz-Pauli quadratic action derivatives verified for all symmetric components")

# Bianchi identity in momentum algebra: k^a G_ab = 0.
for b in range(dim):
    divergence = sum(eta[a] * k[a] * Einstein(a, b) for a in range(dim))
    require_zero(f"momentum-space Bianchi identity component {b}", divergence)

checks.append("momentum-space Bianchi identity verified")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Geometric Field Lift 92: Fierz-Pauli Action Variation

## Purpose

This report validates the quadratic Fierz-Pauli / linearized Einstein action
variation in momentum-space algebra.

## Validated Checks

{validation_bullets}

## Quadratic Action

For a symmetric perturbation `h_ab`, define:

```text
L2 = 1/2 h^ab G_ab[h],
```

where `G_ab[h]` is the linearized Einstein tensor.

SymPy verifies that differentiating `L2` with respect to each independent
symmetric component gives:

```text
dL2/dh_ab = G^ab
```

for diagonal components, and the expected doubled equation for off-diagonal
symmetric components.

## Bianchi Identity

The same algebra verifies:

```text
k^a G_ab = 0.
```

## Interpretation

The correct weak-field geometric action varies to the linearized Einstein
operator, not the naive componentwise Laplacian.
"""

out = Path(__file__).with_name("92_fierz_pauli_action_variation.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
