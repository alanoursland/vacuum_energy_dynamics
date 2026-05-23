#!/usr/bin/env python3
"""
make_psi_k_ibp_origin.py

Generate psi_k_ibp_origin.md and validate the symbolic derivation.

Run from:
    theory_v3/development/projection_origin_probe/

Output:
    psi_k_ibp_origin.md

The script checks the algebra before writing the markdown note.
"""

from pathlib import Path
import sympy as sp


# ---------------------------------------------------------------------
# Symbols and core definitions
# ---------------------------------------------------------------------

x = sp.symbols("x", real=True)
k = sp.symbols("k", integer=True, positive=True)
p, q = sp.symbols("p q", integer=True, nonnegative=True)

f = sp.Function("f")

r_k = sp.simplify((2 * k - 1) / (2 * k + 3))
psi_k = x ** (2 * k) - r_k * x ** (2 * k - 2)
w = (1 - x**2) ** 4

G_k = x ** (2 * k - 1) * (1 - x**2) ** 2

L_f = (1 - x**2) * sp.diff(f(x), x) - 6 * x * f(x)
H_f = f(x) * (1 - x**2) ** 3


# ---------------------------------------------------------------------
# Utility helpers
# ---------------------------------------------------------------------

def simplify_expr(expr):
    """
    Aggressive symbolic cleanup.

    SymPy can leave expressions like x**2*x**(2*k-2) unevaluated
    when k is symbolic. The powsimp(force=True) pass is intentional
    for these monomial identities.
    """
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


def validate_polynomial_sample(K, degree=5):
    """
    Check the IBP identity for a generic finite even polynomial:

        f_N(x) = sum_j c_j x^(2j)

    for a concrete positive integer K.
    """
    coeffs = sp.symbols(f"c0:{degree + 1}")
    fN = sum(coeffs[j] * x ** (2 * j) for j in range(degree + 1))

    rK = sp.Rational(2 * K - 1, 2 * K + 3)
    psiK = x ** (2 * K) - rK * x ** (2 * K - 2)
    wK = (1 - x**2) ** 4

    LF = (1 - x**2) * sp.diff(fN, x) - 6 * x * fN

    left = sp.integrate(sp.expand(psiK * fN * wK), (x, 0, 1))
    right = sp.Rational(1, 2 * K + 3) * sp.integrate(
        sp.expand(x ** (2 * K - 1) * wK * LF),
        (x, 0, 1),
    )

    return simplify_expr(left - right)


# ---------------------------------------------------------------------
# Symbolic validation
# ---------------------------------------------------------------------

checks = []

# 1. Derivative identity:
#
#   G_k' + (2k+3)(1-x^2) psi_k = 0
derivative_identity = sp.diff(G_k, x) + (2 * k + 3) * (1 - x**2) * psi_k
require_zero("derivative identity", derivative_identity)
checks.append("derivative identity")

# 2. Auxiliary moment ratio under (1-x^2):
#
#   integral x^(2k)(1-x^2) / integral x^(2k-2)(1-x^2)
#   = (2k-1)/(2k+3)
aux_ratio = sp.simplify(moment_poly(2 * k, 1) / moment_poly(2 * k - 2, 1))
require_equal("auxiliary moment ratio", aux_ratio, r_k)
checks.append("auxiliary moment ratio")

# 3. Same-weight ratio under w=(1-x^2)^4:
#
#   integral x^(2k)w / integral x^(2k-2)w
#   = (2k-1)/(2k+9), not r_k
same_weight_ratio = sp.simplify(moment_poly(2 * k, 4) / moment_poly(2 * k - 2, 4))
expected_same_weight_ratio = sp.simplify((2 * k - 1) / (2 * k + 9))
require_equal("same-weight ratio", same_weight_ratio, expected_same_weight_ratio)

same_weight_difference = simplify_expr(same_weight_ratio - r_k)
if same_weight_difference == 0:
    raise AssertionError("same-weight ratio unexpectedly equals r_k")
checks.append("same-weight ratio distinction")

# 4. Operator pullback algebra.
#
#   H_f' = (1-x^2)^2 L[f]
operator_factor_identity = sp.diff(H_f, x) - (1 - x**2) ** 2 * L_f
require_zero("operator factor identity", operator_factor_identity)
checks.append("operator factor identity")

#   G_k H_f' = x^(2k-1) w L[f]
operator_weight_identity = G_k * sp.diff(H_f, x) - x ** (2 * k - 1) * w * L_f
require_zero("operator weight identity", operator_weight_identity)
checks.append("operator weight identity")

# 5. Boundary term shape:
#
#   H_f G_k = f x^(2k-1)(1-x^2)^5
boundary_term = H_f * G_k
expected_boundary_term = f(x) * x ** (2 * k - 1) * (1 - x**2) ** 5
require_equal("boundary term shape", boundary_term, expected_boundary_term)
checks.append("boundary term shape")

# 6. Concrete polynomial checks.
sample_rows = []
for K in range(1, 8):
    residual = validate_polynomial_sample(K, degree=5)
    require_zero(f"finite polynomial sample K={K}", residual)
    sample_rows.append((K, residual))
checks.append("finite polynomial samples k=1..7")

# 7. Formal source-family signature check.
#
# For S_pq(x)=x^(2q)(1-x^2)^p:
#
#   b_k(S_pq)
#   = B(k+q+1/2, p+5) - r_k B(k+q-1/2, p+5)
#
# Since B(a+1,b)=a/(a+b)B(a,b), with a=k+q-1/2 and b=p+5,
# the sign is controlled by:
#
#   -[2kp + 6k - p - 4q - 3]
#
# up to positive factors.
a = k + q - sp.Rational(1, 2)
beta_ratio_part = a / (a + p + 5) - r_k
source_signature_factor = simplify_expr(beta_ratio_part)
expected_source_signature_factor = simplify_expr(
    -2 * (2 * k * p + 6 * k - p - 4 * q - 3)
    / ((2 * k + 3) * (2 * k + 2 * p + 2 * q + 9))
)
require_equal(
    "formal source-family signature factor",
    source_signature_factor,
    expected_source_signature_factor,
)
checks.append("formal source-family signature factor")


# ---------------------------------------------------------------------
# Markdown generation
# ---------------------------------------------------------------------

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)
sample_k_list = ", ".join(str(K) for K, _ in sample_rows)

md = f"""# `psi_k` Integration-By-Parts Origin

## Status

This note records a symbolic derivation for the row-test functions

```text
psi_k(x) = x^(2k) - ((2k - 1)/(2k + 3)) x^(2k - 2)
```

inside the projection form

```text
A[k,j] = 2 integral_0^1 psi_k(x) phi_j(x) (1 - x^2)^4 dx
```

with

```text
phi_j(x) = x^(2j)
w(x) = (1 - x^2)^4
```

Current status:

```text
psi_k origin: derived as an integration-by-parts pullback
ratio origin: derived from a boundary-vanishing primitive
same-weight Gram interpretation: failed
physical interpretation: not assigned
```

This note does not claim a physical source law, curvature energy, burden functional, or field equation.

## Definitions

Let

```text
r_k = (2k - 1)/(2k + 3)
```

and

```text
psi_k(x) = x^(2k) - r_k x^(2k - 2)
         = x^(2k - 2)(x^2 - r_k).
```

Define the auxiliary primitive

```text
G_k(x) = x^(2k - 1)(1 - x^2)^2.
```

## Core Derivative Identity

Direct differentiation gives

```text
d/dx [x^(2k - 1)(1 - x^2)^2]
=
-(2k + 3)(1 - x^2) psi_k(x).
```

Equivalently,

```text
psi_k(x)
=
- G_k'(x) / ((2k + 3)(1 - x^2)).
```

This is the first concrete origin of the coefficient

```text
(2k - 1)/(2k + 3).
```

The ratio is not inserted by hand after the fact. It is forced by differentiating the boundary-vanishing object

```text
x^(2k - 1)(1 - x^2)^2.
```

## Auxiliary Moment Origin

The same ratio is obtained from zero mean under the auxiliary weight

```text
1 - x^2.
```

Indeed,

```text
integral_0^1 x^(2k)(1 - x^2) dx
/
integral_0^1 x^(2k - 2)(1 - x^2) dx
=
(2k - 1)/(2k + 3).
```

Therefore,

```text
integral_0^1 psi_k(x)(1 - x^2) dx = 0.
```

This is an auxiliary-weight orthogonality result, not an orthogonality result under the full projection weight.

## Same-Weight Orthogonality Fails

Under the actual projection weight

```text
w(x) = (1 - x^2)^4,
```

the corresponding zero-mean ratio would be

```text
integral_0^1 x^(2k)(1 - x^2)^4 dx
/
integral_0^1 x^(2k - 2)(1 - x^2)^4 dx
=
(2k - 1)/(2k + 9).
```

This is not

```text
(2k - 1)/(2k + 3).
```

So `psi_k` should not be interpreted as a naive same-weight Gram/Hessian row under `w`.

## Integration-By-Parts Pullback

Start with

```text
I_k[f] = integral_0^1 psi_k(x) f(x) w(x) dx.
```

Using

```text
psi_k(x)
=
- G_k'(x) / ((2k + 3)(1 - x^2))
```

and

```text
w(x) = (1 - x^2)^4,
```

we get

```text
I_k[f]
=
-1/(2k + 3) integral_0^1 f(x)(1 - x^2)^3 G_k'(x) dx.
```

Let

```text
H(x) = f(x)(1 - x^2)^3.
```

Then

```text
I_k[f]
=
-1/(2k + 3) [H(x)G_k(x)]_0^1
+
1/(2k + 3) integral_0^1 G_k(x) H'(x) dx.
```

The boundary term is

```text
H(x)G_k(x)
=
f(x)x^(2k - 1)(1 - x^2)^5.
```

For `k >= 1` and regular `f`, this vanishes at both endpoints.

Now

```text
H'(x)
=
(1 - x^2)^2 [(1 - x^2)f'(x) - 6x f(x)].
```

Define the first-order operator

```text
L[f](x) = (1 - x^2)f'(x) - 6x f(x).
```

Then

```text
G_k(x)H'(x)
=
x^(2k - 1)(1 - x^2)^4 L[f](x)
=
x^(2k - 1)w(x)L[f](x).
```

Therefore, when the endpoint term vanishes,

```text
integral_0^1 psi_k(x) f(x) w(x) dx
=
1/(2k + 3) integral_0^1 x^(2k - 1) w(x) L[f](x) dx.
```

Equivalently,

```text
<psi_k, f>_w
=
1/(2k + 3) <x^(2k - 1), L[f]>_w
```

with the right-hand side understood as an odd-moment pairing.

## Formal Source-Family Note

For formal sources

```text
S_pq(x) = x^(2q)(1 - x^2)^p,
```

the source-vector component is

```text
b_k(S_pq)
=
2 integral_0^1 psi_k(x) S_pq(x) (1 - x^2)^4 dx.
```

Equivalently,

```text
b_k(S_pq)
=
B(k + q + 1/2, p + 5)
-
r_k B(k + q - 1/2, p + 5).
```

The sign is controlled by

```text
-[2kp + 6k - p - 4q - 3],
```

up to positive factors.

This is only a formal source-signature diagnostic. It is not a physical source law.

## Validation Summary

The generating script validated:

```text
{validation_bullets}
```

Finite polynomial checks for

```text
f_N(x) = sum_j c_j x^(2j),   j = 0,...,5
```

also passed for:

```text
k = {sample_k_list}
```

## Conclusion

The row-test function `psi_k` is not arbitrary.

It has a compact integration-by-parts origin:

```text
psi_k(x)
=
-1 / ((2k + 3)(1 - x^2))
d/dx [x^(2k - 1)(1 - x^2)^2].
```

The coefficient

```text
(2k - 1)/(2k + 3)
```

is forced by this primitive.

However, this does not yet provide a physical interpretation of `x`, `f`, `S`, or the projection hierarchy. The next question is whether the induced operator

```text
L[f] = (1 - x^2)f' - 6xf
```

has an independent operator, boundary, source, or geometric origin.
"""


out = Path("1_psi_k_ibp_origin.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
