#!/usr/bin/env python3
"""
make_6_synthesis_source_weight_diagnostics.py

Validate synthesis claims about source-family signatures, moment ratios,
and the orthogonal-polynomial neighborhood of the weight a^4.

Run from:
    theory_v3/development/projection_origin_probe/

Output:
    6_synthesis_source_weight_diagnostics.md
"""

from pathlib import Path
import sympy as sp


# ---------------------------------------------------------------------
# Symbols and core definitions
# ---------------------------------------------------------------------

x = sp.symbols("x", real=True)
k = sp.symbols("k", integer=True, positive=True)
p, q = sp.symbols("p q", integer=True, nonnegative=True)
lam = sp.symbols("lambda")

a = 1 - x**2
w = a**4

r_k = sp.simplify((2 * k - 1) / (2 * k + 3))
psi_k = x ** (2 * k) - r_k * x ** (2 * k - 2)


# ---------------------------------------------------------------------
# Utility helpers
# ---------------------------------------------------------------------

def simplify_expr(expr):
    """Aggressive cleanup for rational/power expressions."""
    out = sp.simplify(expr)
    out = sp.factor(out)
    out = sp.powsimp(out, force=True)
    out = sp.cancel(out)
    out = sp.factor(out)
    out = sp.powsimp(out, force=True)
    out = sp.simplify(out)
    return out


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


def moment_poly(n, power):
    """
    Exact termwise integral:

        integral_0^1 x^n (1-x^2)^power dx

    for nonnegative integer power.
    """
    return sp.simplify(
        sum(
            sp.binomial(power, ell) * (-1) ** ell / (n + 2 * ell + 1)
            for ell in range(power + 1)
        )
    )


def beta_moment(n_shift, p_power):
    """
    Integral skeleton for source-family terms:

        integral_0^1 x^(2k + 2q + n_shift) a^(p+4) dx

    represented by beta factors after y=x^2.
    """
    alpha = k + q + sp.Rational(n_shift + 1, 2)
    return sp.beta(alpha, p_power + 5) / 2


# ---------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------

checks = []

# 1. Auxiliary ratio under a:
#
#   int x^(2k)a / int x^(2k-2)a = (2k-1)/(2k+3).
aux_ratio = sp.simplify(moment_poly(2 * k, 1) / moment_poly(2 * k - 2, 1))
require_equal("auxiliary a-weight moment ratio", aux_ratio, r_k)
checks.append("auxiliary a-weight moment ratio")

# 2. Actual same-weight ratio under a^4:
#
#   int x^(2k)a^4 / int x^(2k-2)a^4 = (2k-1)/(2k+9).
same_weight_ratio = sp.simplify(moment_poly(2 * k, 4) / moment_poly(2 * k - 2, 4))
expected_same_weight_ratio = sp.simplify((2 * k - 1) / (2 * k + 9))
require_equal("same-weight a^4 moment ratio", same_weight_ratio, expected_same_weight_ratio)

if simplify_expr(same_weight_ratio - r_k) == 0:
    raise AssertionError("same-weight a^4 ratio unexpectedly equals observed r_k")

checks.append("same-weight a^4 ratio distinction")

# 3. Source-family signature:
#
# For S_pq = x^(2q)a^p,
#
#   b_k(S_pq) = int psi_k S_pq a^4 dx
#
# and the sign is controlled by:
#
#   -[2kp + 6k - p - 4q - 3]
#
# up to positive factors.
# The beta recurrence B(A+1,B)/B(A,B)=A/(A+B) controls the ratio of the
# x^(2k+2q) term to the x^(2k+2q-2) term, with
# A = k+q-1/2 and B = p+5.
A_source = k + q - sp.Rational(1, 2)
source_ratio_part = A_source / (A_source + p + 5) - r_k

source_signature_factor = simplify_expr(source_ratio_part)
expected_source_signature_factor = simplify_expr(
    -2 * (2 * k * p + 6 * k - p - 4 * q - 3)
    / ((2 * k + 3) * (2 * k + 2 * p + 2 * q + 9))
)

require_equal(
    "source-family signature factor",
    source_signature_factor,
    expected_source_signature_factor,
)
checks.append("source-family signature factor")

# 4. Concrete source-family polynomial checks for small p,q,k.
#
# The beta-derived sign factor should reproduce the direct polynomial integral
# after removing the positive lower beta moment.
for K in range(1, 5):
    for P in range(0, 5):
        for Q in range(0, 5):
            rK = sp.Rational(2 * K - 1, 2 * K + 3)
            psiK = x ** (2 * K) - rK * x ** (2 * K - 2)
            source = x ** (2 * Q) * a**P
            direct = sp.integrate(sp.expand(psiK * source * w), (x, 0, 1))

            lower = sp.integrate(sp.expand(x ** (2 * K + 2 * Q - 2) * a ** (P + 4)), (x, 0, 1))
            expected = lower * (
                (sp.Rational(K + Q, 1) - sp.Rational(1, 2))
                / (sp.Rational(K + Q + P, 1) + sp.Rational(9, 2))
                - rK
            )
            require_equal(
                f"direct source check K={K} P={P} Q={Q}",
                direct,
                expected,
            )
checks.append("direct source-family polynomial grid K=1..4 P,Q=0..4")

# 5. Endpoint-order bookkeeping for S_pq:
#
# At x=0, S_pq ~ x^(2q).  At x=1, a=1-x^2 has simple zero in x,
# so S_pq has a^p vanishing order p in the a-variable.
for Q in range(0, 5):
    source_at_zero = (x ** (2 * Q) * a**2).subs(x, 0)
    expected_zero = 1 if Q == 0 else 0
    require_equal(f"origin endpoint order Q={Q}", source_at_zero, expected_zero)
checks.append("endpoint bookkeeping at x=0")

# 6. Gegenbauer neighborhood:
#
#   (1-x^2)^4 = (1-x^2)^(lambda - 1/2)
#   gives lambda = 9/2.
lambda_solution = sp.solve(sp.Eq(lam - sp.Rational(1, 2), 4), lam)
if lambda_solution != [sp.Rational(9, 2)]:
    raise AssertionError(f"unexpected Gegenbauer lambda solution: {lambda_solution}")
checks.append("Gegenbauer lambda=9/2 weight identification")


# ---------------------------------------------------------------------
# Markdown generation
# ---------------------------------------------------------------------

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Synthesis Proof 6: Source and Weight Diagnostics

## Purpose

This report validates the source-family and weight-context claims used in
`speculative_synthesis.md`.

It focuses on:

```text
same-weight ratio failure
source-family endpoint diagnostics
source-signature control factor
Gegenbauer/Jacobi weight neighborhood
```

## Validated Identities

{validation_bullets}

## Moment-Ratio Distinction

The observed ratio is:

```text
r_k = (2k - 1)/(2k + 3).
```

SymPy verifies that this is the moment ratio under the auxiliary weight `a`:

```text
int x^(2k)a dx / int x^(2k-2)a dx
  = (2k - 1)/(2k + 3).
```

Under the actual projection weight `a^4`, the same-weight ratio is instead:

```text
int x^(2k)a^4 dx / int x^(2k-2)a^4 dx
  = (2k - 1)/(2k + 9).
```

Therefore the observed row function is not explained by same-weight
orthogonality under `w=a^4`.

## Source-Family Signature

For:

```text
S_(p,q)(x) = x^(2q)(1 - x^2)^p,
```

the parameters separately track endpoint behavior:

```text
p: vanishing order at x = 1 in the a-variable
q: vanishing order at x = 0 through x^(2q)
```

The sign of:

```text
b_k(S_(p,q)) = integral psi_k S_(p,q) a^4 dx
```

is controlled, up to positive beta/moment factors, by:

```text
-(2kp + 6k - p - 4q - 3).
```

The coefficient `6` is the same coefficient that appears in:

```text
L[f] = a f' - 6xf.
```

This proves a shared exponent bookkeeping structure. It does not identify a
physical source law.

## Weight Context

On `[-1,1]`, the weight:

```text
(1 - x^2)^4
```

is a Gegenbauer weight with:

```text
lambda = 9/2.
```

Equivalently, it is a symmetric Jacobi weight. This places the projection
weight in a known orthogonal-polynomial neighborhood, but it does not derive
the row functions or select `m=2`.
"""

out = Path("6_synthesis_source_weight_diagnostics.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
