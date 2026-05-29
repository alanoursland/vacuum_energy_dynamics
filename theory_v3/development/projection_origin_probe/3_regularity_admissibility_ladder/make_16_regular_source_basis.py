#!/usr/bin/env python3
"""
make_16_regular_source_basis.py

Construct signed source profiles satisfying the first boundedness/admissibility
condition:

    integral_0^1 a S dx = 0

and compare their psi_k projection signatures with positive source probes.

Output:
    16_regular_source_basis.md
"""

from pathlib import Path
import sympy as sp


x = sp.symbols("x", real=True)
a = 1 - x**2
w = a**4


def simplify_expr(expr):
    out = sp.simplify(expr)
    out = sp.factor(out)
    out = sp.powsimp(out, force=True)
    out = sp.cancel(out)
    out = sp.factor(out)
    return out


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


def integrate_poly(expr):
    return sp.integrate(sp.expand(expr), (x, 0, 1))


def psi(k):
    r = sp.Rational(2 * k - 1, 2 * k + 3)
    return x ** (2 * k) - r * x ** (2 * k - 2)


def projection_signature(S, Kmax=6):
    return [sp.factor(integrate_poly(psi(k) * S * w)) for k in range(1, Kmax + 1)]


def first_admissibility(S):
    return sp.factor(integrate_poly(a * S))


checks = []

# Positive monomial source probes fail the first admissibility condition.
positive_rows = []
for q in range(0, 7):
    S_pos = x ** (2 * q)
    moment = first_admissibility(S_pos)
    if not (moment > 0):
        raise AssertionError(f"expected positive admissibility moment q={q}: {moment}")
    sig = projection_signature(S_pos, Kmax=5)
    positive_rows.append((q, moment, sig))
checks.append("positive even monomial probes fail first admissibility")

# Build balanced sources:
#
#   B_q = x^(2q) - c_q
#
# choose c_q so int a B_q dx = 0.
balanced_rows = []
balanced_sources = []
for q in range(1, 8):
    c_q = sp.factor(integrate_poly(a * x ** (2 * q)) / integrate_poly(a))
    B_q = sp.expand(x ** (2 * q) - c_q)
    require_zero(f"balanced source first admissibility q={q}", first_admissibility(B_q))
    sig = projection_signature(B_q, Kmax=6)
    balanced_sources.append(B_q)
    balanced_rows.append((q, c_q, sp.factor(B_q), sig))
checks.append("balanced monomial-minus-constant basis satisfies first admissibility")

# Closed form for c_q:
#
# int_0^1 a x^(2q) dx = 2/((2q+1)(2q+3))
# int_0^1 a dx = 2/3
# c_q = 3/((2q+1)(2q+3)).
q_sym = sp.symbols("q", integer=True, positive=True)
for q in range(1, 10):
    c_q = sp.factor(integrate_poly(a * x ** (2 * q)) / integrate_poly(a))
    expected = sp.Rational(3, (2 * q + 1) * (2 * q + 3))
    require_equal(f"balanced c_q closed form q={q}", c_q, expected)
checks.append("balanced coefficient c_q=3/((2q+1)(2q+3))")

# Check independence of the balanced basis over tested truncation.
N = 7
coeff_matrix = []
for B in balanced_sources[:N]:
    poly = sp.Poly(B, x)
    coeff_matrix.append([poly.coeff_monomial(x ** (2 * j)) for j in range(0, N + 1)])
M_coeff = sp.Matrix(coeff_matrix)
if M_coeff.rank() != N:
    raise AssertionError(f"expected rank {N} balanced source coefficient matrix, got {M_coeff.rank()}")
checks.append("balanced source basis independent over tested truncation")

# Compare projection signature matrix of balanced sources.
Kmax = 7
Sig_balanced = sp.Matrix(
    [
        projection_signature(B, Kmax=Kmax)
        for B in balanced_sources[:N]
    ]
)
if Sig_balanced.rank() < min(Sig_balanced.shape):
    raise AssertionError(
        f"balanced projection signature matrix lost rank: {Sig_balanced.rank()} shape={Sig_balanced.shape}"
    )
checks.append("balanced source projection signatures retain full tested rank")

# Signed source from previous admissibility theorem should be one of the
# q=1 balanced sources multiplied by a:
#
# F = a(x^2 - 1/5) corresponds to S = x^2 - 1/5.
require_equal("signed admissible example matches B_1", balanced_sources[0], x**2 - sp.Rational(1, 5))
checks.append("signed admissible example recovered as B_1")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)
positive_lines = "\n".join(
    f"S=x^{2*q}: int aS={moment}, psi signature={sig}"
    for q, moment, sig in positive_rows
)
balanced_lines = "\n".join(
    f"B_{q}=x^{2*q}-{c_q}: {B_q}, psi signature={sig}"
    for q, c_q, B_q, sig in balanced_rows
)

md = f"""# Synthesis Proof 16: Balanced Source Basis

## Purpose

This report constructs signed source profiles satisfying the first
boundedness/admissibility condition:

```text
integral_0^1 aS dx = 0.
```

It then compares their `psi_k` projection signatures with positive source
probes.

## Validated Checks

{validation_bullets}

## Positive Source Probes

Positive even monomials:

```text
S_q = x^(2q)
```

fail the first admissibility condition:

```text
integral_0^1 aS_q dx > 0.
```

Exact checked values and projection signatures:

```text
{positive_lines}
```

## Balanced Signed Basis

Define:

```text
B_q(x) = x^(2q) - c_q
```

with:

```text
c_q = integral a x^(2q) dx / integral a dx.
```

SymPy verifies the closed form:

```text
c_q = 3 / ((2q+1)(2q+3)).
```

Therefore:

```text
integral_0^1 a B_q dx = 0.
```

Exact balanced sources and their projection signatures:

```text
{balanced_lines}
```

The first member is:

```text
B_1 = x^2 - 1/5,
```

which matches the signed admissible example from the boundedness theorem:

```text
F = a(x^2 - 1/5).
```

## Matrix Observation

The tested balanced source basis is linearly independent, and its `psi_k`
projection signature matrix retains full tested rank.

So imposing the first admissibility condition does not collapse the projection
signatures. It removes the purely positive monomial probes and leaves a signed
balanced source space that the projection hierarchy still resolves.
"""

out = Path(__file__).with_name("16_regular_source_basis.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")


