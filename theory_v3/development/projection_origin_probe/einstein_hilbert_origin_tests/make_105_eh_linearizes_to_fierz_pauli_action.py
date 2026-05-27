#!/usr/bin/env python3
"""
make_105_eh_linearizes_to_fierz_pauli_action.py

Validate that the quadratic Gamma-Gamma density built from the linearized
connection matches the Fierz-Pauli / linearized Einstein quadratic action:

    L_GG^(2) = 1/2 h^ab G_ab[h]

in momentum-space algebra.

Output:
    105_eh_linearizes_to_fierz_pauli_action.md
"""

from pathlib import Path
import sympy as sp


dim = 4
eta = [-1, 1, 1, 1]
k = sp.symbols("k0:4", real=True)


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


def symvar(a, b):
    i, j = sorted((a, b))
    return sp.symbols(f"H{i}{j}", real=True)


H = [[symvar(a, b) for b in range(dim)] for a in range(dim)]
dh = [[[k[c] * H[a][b] for b in range(dim)] for a in range(dim)] for c in range(dim)]


def Gamma_linear(up, low1, low2):
    return sp.Rational(1, 2) * eta[up] * (
        dh[low1][up][low2]
        + dh[low2][up][low1]
        - dh[up][low1][low2]
    )


gamma_gamma_quadratic = 0
for a in range(dim):
    for b in range(dim):
        eta_ab = eta[a] if a == b else 0
        if eta_ab == 0:
            continue
        for c in range(dim):
            for d in range(dim):
                gamma_gamma_quadratic += eta_ab * (
                    Gamma_linear(c, a, d) * Gamma_linear(d, b, c)
                    - Gamma_linear(c, a, b) * Gamma_linear(d, c, d)
                )
gamma_gamma_quadratic = sp.expand(gamma_gamma_quadratic)

trace_H = sum(eta[a] * H[a][a] for a in range(dim))
k2 = sum(eta[a] * k[a] ** 2 for a in range(dim))


def divH(b):
    return sum(eta[c] * k[c] * H[b][c] for c in range(dim))


def Ricci_linear(a, b):
    return sp.Rational(1, 2) * (
        k[a] * divH(b)
        + k[b] * divH(a)
        - k2 * H[a][b]
        - k[a] * k[b] * trace_H
    )


R_scalar = sum(eta[a] * Ricci_linear(a, a) for a in range(dim))


def Einstein_linear(a, b):
    return simplify_expr(
        Ricci_linear(a, b) - sp.Rational(1, 2) * (eta[a] if a == b else 0) * R_scalar
    )


fierz_pauli_quadratic = sp.Rational(1, 2) * sum(
    eta[a] * eta[b] * H[a][b] * Einstein_linear(a, b)
    for a in range(dim)
    for b in range(dim)
)

checks = []

require_equal(
    "Gamma-Gamma quadratic equals Fierz-Pauli action",
    gamma_gamma_quadratic,
    fierz_pauli_quadratic,
)
checks.append("Gamma-Gamma quadratic equals Fierz-Pauli action")

for a in range(dim):
    for b in range(a, dim):
        derivative = sp.diff(gamma_gamma_quadratic, H[a][b])
        multiplicity = 2 if a != b else 1
        target = multiplicity * eta[a] * eta[b] * Einstein_linear(a, b)
        require_equal(f"Gamma-Gamma action derivative {a}{b}", derivative, target)

checks.append("Gamma-Gamma quadratic varies to linearized Einstein operator")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Einstein-Hilbert Origin Test 105: EH Linearizes to Fierz-Pauli Action

## Purpose

This report validates that the Gamma-Gamma part of the Einstein-Hilbert action
linearizes to the Fierz-Pauli / linearized Einstein quadratic action.

## Validated Checks

{validation_bullets}

## Identity

Using a plane-wave/momentum-space substitution:

```text
partial_c h_ab -> k_c H_ab,
```

SymPy verifies:

```text
L_GG^(2) = 1/2 h^ab G_ab[h].
```

It also verifies that varying the quadratic Gamma-Gamma density with respect to
the independent symmetric components gives the linearized Einstein operator.

## Interpretation

This proves the direct action bridge:

```text
Einstein-Hilbert
  -> Gamma-Gamma connection strain
  -> Fierz-Pauli quadratic action
  -> linearized Einstein equations.
```
"""

out = Path(__file__).with_name("105_eh_linearizes_to_fierz_pauli_action.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
