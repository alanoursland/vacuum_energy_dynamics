#!/usr/bin/env python3
"""
make_3_projection_source_independence.py

Validate that the formal projection source vector is independent of simple
mass/monopole functionals and therefore cannot be identified as ordinary mass
without an additional routing theorem.

Output:
    3_projection_source_independence.md
"""

from pathlib import Path
import sympy as sp


x = sp.symbols("x")
a = 1 - x**2
w = a**4
psi1 = x**2 - sp.Rational(1, 5)


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_nonzero(label, expr):
    result = simplify_expr(expr)
    if result == 0:
        raise AssertionError(f"{label} unexpectedly vanished")
    return result


checks = []

S_unweighted_zero = x**2 - sp.Rational(1, 3)
M0 = simplify_expr(sp.integrate(S_unweighted_zero, (x, 0, 1)))
b1_unweighted_zero = simplify_expr(2 * sp.integrate(psi1 * S_unweighted_zero * w, (x, 0, 1)))
require_zero("unweighted monopole variation", M0)
nonzero_b1_unweighted = require_nonzero("projection response to unweighted-zero variation", b1_unweighted_zero)
checks.append("zero unweighted monopole can still have nonzero projection source")

S_weighted_zero = x**2 - sp.Rational(1, 11)
Mw = simplify_expr(sp.integrate(S_weighted_zero * w, (x, 0, 1)))
b1_weighted_zero = simplify_expr(2 * sp.integrate(psi1 * S_weighted_zero * w, (x, 0, 1)))
require_zero("projection-weight monopole variation", Mw)
nonzero_b1_weighted = require_nonzero("projection response to a^4-zero variation", b1_weighted_zero)
checks.append("zero a^4-weighted monopole can still have nonzero projection source")

contact_moment = simplify_expr(sp.integrate(a * psi1, (x, 0, 1)))
self_projection = simplify_expr(2 * sp.integrate(psi1 * psi1 * w, (x, 0, 1)))
require_zero("auxiliary contact moment of psi1", contact_moment)
nonzero_self_projection = require_nonzero("self projection under a^4", self_projection)
checks.append("contact cancellation does not mean zero projection response")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Matter Source Origin Gate 3: Projection Source Independence

## Purpose

This proof checks the formal projection source vector:

```text
b_k(S) = 2 integral_0^1 psi_k S a^4 dx.
```

It shows that `b_k(S)` is not an ordinary mass/monopole functional by itself.
It can detect variations that have zero simple monopole.

## Validated Checks

{validation_bullets}

## Witness 1: Zero Unweighted Monopole

Let:

```text
S = x^2 - 1/3.
```

Then:

```text
integral_0^1 S dx = 0,
```

but:

```text
b_1(S) = {nonzero_b1_unweighted}.
```

## Witness 2: Zero a^4-Weighted Monopole

Let:

```text
S = x^2 - 1/11.
```

Then:

```text
integral_0^1 S a^4 dx = 0,
```

but:

```text
b_1(S) = {nonzero_b1_weighted}.
```

## Witness 3: Contact Cancellation Is Not Projection Silence

For:

```text
psi_1 = x^2 - 1/5,
```

the contact moment cancels:

```text
integral_0^1 a psi_1 dx = 0.
```

But the projection self-pairing is nonzero:

```text
2 integral_0^1 psi_1^2 a^4 dx = {self_projection}.
```

## Gate Interpretation

The formal projection source vector is a real linear diagnostic, but it is not
licensed as ordinary matter mass. A later source-origin theorem must explain
how `b_k(S)` is routed, or else keep it in the formal admissibility layer.
"""

out = Path(__file__).with_name("3_projection_source_independence.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Projection source independence passed.")
print(f"Wrote {out.resolve()}")
