#!/usr/bin/env python3
"""
make_10_boundary_domain_classifier.py

Classify endpoint boundary-term behavior for model power profiles.

Output:
    10_boundary_domain_classifier.md
"""

from pathlib import Path
import sympy as sp


x = sp.symbols("x", real=True)
s, t, r = sp.symbols("s t r")
a = 1 - x**2


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


def L(expr):
    return sp.expand(a * sp.diff(expr, x) - 6 * x * expr)


checks = []

# Boundary term for adjoint:
#
#   B_fg = a^5 f g.
#
# For f=a^s and g=x^r, B_fg = a^(5+s)x^r.
f_s = a**s
g_r = x**r
B_fg = a**5 * f_s * g_r
require_equal("adjoint boundary model exponent", B_fg, a ** (5 + s) * x**r)
checks.append("adjoint boundary model exponent")

# Variational boundary term:
#
#   B_eta = a^5 eta L[f].
#
# For eta=a^t and f=a^s:
#   L[a^s] = -2(s+3)x a^s.
eta_t = a**t
Lf_s = L(f_s)
require_equal("L on endpoint power", Lf_s, -2 * (s + 3) * x * a**s)
B_eta = a**5 * eta_t * Lf_s
require_equal("variational boundary model exponent", B_eta, -2 * (s + 3) * x * a ** (5 + s + t))
checks.append("variational boundary model exponent")


def vanish_at_x1_a_power(exponent, coefficient_zero=False):
    if coefficient_zero:
        return "zero coefficient"
    if exponent > 0:
        return "vanishes"
    if exponent == 0:
        return "finite nonzero"
    return "singular/nonvanishing"


def vanish_at_x0_x_power(exponent, coefficient_zero=False):
    if coefficient_zero:
        return "zero coefficient"
    if exponent > 0:
        return "vanishes"
    if exponent == 0:
        return "finite nonzero"
    return "singular/nonvanishing"


adjoint_rows = []
for S in range(-7, 4):
    for R in range(0, 5):
        adjoint_rows.append(
            (S, R, 5 + S, R, vanish_at_x1_a_power(5 + S), vanish_at_x0_x_power(R))
        )

variation_rows = []
for S in range(-7, 4):
    for T in range(-3, 4):
        coeff_zero = S == -3
        variation_rows.append(
            (
                S,
                T,
                5 + S + T,
                vanish_at_x1_a_power(5 + S + T, coeff_zero),
                vanish_at_x0_x_power(1, coeff_zero),
            )
        )

checks.append("integer boundary tables generated")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

adjoint_table = "\n".join(
    f"s={S:2d}, r={R}: x=1 exponent a^{E1:2d} -> {v1}; x=0 exponent x^{E0} -> {v0}"
    for S, R, E1, E0, v1, v0 in adjoint_rows
)
variation_table = "\n".join(
    f"s={S:2d}, t={T:2d}: x=1 exponent a^{E:2d} -> {v1}; x=0 -> {v0}"
    for S, T, E, v1, v0 in variation_rows
)

md = f"""# Synthesis Proof 10: Boundary Domain Classifier

## Purpose

This report classifies boundary behavior for model endpoint profiles.

It checks the two boundary terms used in the synthesis:

```text
[a^5 f g]_0^1
[a^5 eta L[f]]_0^1
```

## Validated Identities

{validation_bullets}

## Adjoint Boundary Term

For model profiles:

```text
f = a^s
g = x^r
```

the adjoint boundary term is:

```text
a^5 f g = a^(5+s)x^r.
```

Thus:

```text
x = 1 is controlled by 5+s
x = 0 is controlled by r
```

## Variational Boundary Term

For:

```text
eta = a^t
f = a^s
```

the operator gives:

```text
L[a^s] = -2(s+3)x a^s.
```

So:

```text
a^5 eta L[f] = -2(s+3)x a^(5+s+t).
```

The exceptional model power `s=-3` makes `L[a^s]=0` formally.

## Adjoint Boundary Table

```text
{adjoint_table}
```

## Variational Boundary Table

```text
{variation_table}
```
"""

out = Path("10_boundary_domain_classifier.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
