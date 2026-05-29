#!/usr/bin/env python3
"""
make_2_rk_discovery_trail_reconstruction.py

Reconstruct the corrected r_k provenance:

1. Group 88 discovered the ratio through a moment-ratio / row-kernel identity.
2. The later primitive identity gives the compact integration-by-parts origin.
3. The endpoint-contact/admissibility ladder identifies the observed case as R=0.

Output:
    2_rk_discovery_trail_reconstruction.md
"""

from pathlib import Path
import sympy as sp


x, t, k, R = sp.symbols("x t k R", positive=True, integer=True)


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

a = 1 - x**2
r_k = (2 * k - 1) / (2 * k + 3)

# Historical archive route: Group 88 writes the row condition as
# I_k = r_k I_(k-1), with
# I_k(P) = integral t^(k-1/2)(1-t)^4 P(t) dt.
# Equivalently, the row test is q_k=t^k-r_k*t^(k-1) under
# mu=t^(-1/2)(1-t)^4.
mu = t ** (-sp.Rational(1, 2)) * (1 - t) ** 4
q_k = t**k - r_k * t ** (k - 1)
monomial_probe = t**R
row_integrand = sp.expand(q_k * monomial_probe * mu)
expected_row_integrand = sp.expand(
    t ** (k + R - sp.Rational(1, 2)) * (1 - t) ** 4
    - r_k * t ** (k + R - sp.Rational(3, 2)) * (1 - t) ** 4
)
require_equal("Group 88 row moment-ratio integrand", row_integrand, expected_row_integrand)
checks.append("Group 88 row moment-ratio integrand")

psi_k = x ** (2 * k) - r_k * x ** (2 * k - 2)
primitive = x ** (2 * k - 1) * a**2

primitive_identity_rhs = -(2 * k + 3) * a * psi_k
require_equal("later primitive identity explaining r_k", sp.diff(primitive, x), primitive_identity_rhs)
checks.append("later primitive identity explaining r_k")

# Auxiliary same-row moment cancellation under weight (1-x^2), not the
# projection weight (1-x^2)^4.
I_high = 1 / (2 * k + 1) - 1 / (2 * k + 3)
I_low = 1 / (2 * k - 1) - 1 / (2 * k + 1)
ratio_from_auxiliary_moment = simplify_expr(I_high / I_low)
require_equal("auxiliary moment ratio", ratio_from_auxiliary_moment, r_k)
checks.append("auxiliary moment ratio")

r_Rk = (2 * k - 1) / (2 * k + 2 * R + 3)
beta_ratio = simplify_expr((k - sp.Rational(1, 2)) / (k + R + sp.Rational(3, 2)))
require_equal("endpoint-contact ladder beta ratio", beta_ratio, r_Rk)
checks.append("endpoint-contact ladder beta ratio")

require_equal("original ratio is R=0 ladder row", r_Rk.subs(R, 0), r_k)
checks.append("original ratio is R=0 ladder row")

# SymPy does not always reduce symbolic beta ratios with integer assumptions.
# Use the beta recurrence B(z+1,n)/B(z,n) = z/(z+n), then validate the
# resulting rational identity symbolically.
z_projection = k - sp.Rational(1, 2)
same_weight_zero_mean_ratio = simplify_expr(z_projection / (z_projection + 5))
require_equal("projection-weight zero-mean ratio differs", same_weight_zero_mean_ratio, (2 * k - 1) / (2 * k + 9))
checks.append("projection-weight zero-mean ratio differs")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Field Search Survivor Audit 2: Corrected r_k Provenance

## Purpose

This report reconstructs the corrected provenance of:

```text
r_k = (2k - 1)/(2k + 3).
```

The historical archive route is Group 88's moment-ratio identity. The later
primitive identity is a compact explanation of the same ratio, not the original
discovery route.

## Validated Checks

{validation_bullets}

## Historical Route: Group 88 Moment Ratio

Group 88 introduced:

```text
I_k(P) = integral_0^1 t^(k-1/2)(1-t)^4 P(t) dt.
```

The finite hierarchy condition was:

```text
I_k(P) = ((2k - 1)/(2k + 3)) I_(k-1)(P).
```

Equivalently, under:

```text
mu(t) = t^(-1/2)(1-t)^4,
q_k(t) = t^k - r_k t^(k-1),
```

the row test is:

```text
integral_0^1 q_k(t) P(t) mu(t) dt = 0.
```

SymPy verifies this row-integrand form directly for a monomial probe.

## Later Compact Proof: Primitive Identity

With:

```text
a = 1 - x^2
psi_k = x^(2k) - r_k x^(2k-2),
```

The later first-series proof verifies:

```text
d/dx [x^(2k-1)a^2]
  =
  -(2k+3)a psi_k.
```

Expanding the derivative explains the same ratio:

```text
r_k = (2k - 1)/(2k + 3).
```

## Auxiliary Moment Cancellation

The same ratio is also recovered from the auxiliary same-row moment condition:

```text
integral_0^1 psi_k(x)(1-x^2) dx = 0.
```

The ratio is:

```text
[integral x^(2k)(1-x^2) dx]
/
[integral x^(2k-2)(1-x^2) dx]
=
(2k-1)/(2k+3).
```

## Endpoint-Contact Ladder

The endpoint-contact/admissibility ladder ratio is:

```text
r_(R,k) = (2k - 1)/(2k + 2R + 3).
```

The later ladder verifies that the observed ratio is:

```text
R = 0.
```

This is a base boundary-contact/admissibility level. It is not an independent
physical derivation of `R=0`.

## Not Same-Weight Projection Orthogonality

Under the projection weight `(1-x^2)^4`, the zero-mean ratio would be:

```text
(2k - 1)/(2k + 9).
```

That is not the observed ratio. The observed ratio belongs to the archived
moment-ratio row object and later primitive / admissibility structure, not to
ordinary zero-mean Gram orthogonality under the projection weight.

The beta-ratio step uses the exact recurrence:

```text
B(z+1,5)/B(z,5) = z/(z+5),
```

with `z = k - 1/2`.

## Provenance Status

```text
Group 88: original archived moment-ratio route.
1_psi_k_ibp_origin: later compact primitive proof.
regularity_admissibility_ladder: later R=0 base-contact interpretation.
```
"""

out = Path(__file__).with_name("2_rk_discovery_trail_reconstruction.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
