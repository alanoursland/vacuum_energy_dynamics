#!/usr/bin/env python3
"""
make_50_screened_field_long_range_failure.py

Validate that a screened scalar exterior equation gives Yukawa behavior, not a
long-range inverse-square law:

    (Delta - mu^2)u = 0
    u(r) = A exp(-mu r)/r.

Output:
    50_screened_field_long_range_failure.md
"""

from pathlib import Path
import sympy as sp


r, d, mu = sp.symbols("r d mu", positive=True)
A, K = sp.symbols("A K", positive=True)


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

u = A * sp.exp(-mu * r) / r
radial_laplacian = sp.diff(u, r, 2) + 2 * sp.diff(u, r) / r
screened_operator = radial_laplacian - mu**2 * u

require_zero("Yukawa field solves screened exterior equation", screened_operator)
checks.append("Yukawa field solves screened exterior equation")

field_strength = -sp.diff(u, r)
require_equal("Yukawa field strength", field_strength, A * sp.exp(-mu * r) * (mu / r + 1 / r**2))
checks.append("Yukawa field strength")

massless_limit = sp.limit(u, mu, 0, dir="+")
require_equal("massless limit recovers Coulomb profile", massless_limit, A / r)
checks.append("massless limit recovers Coulomb profile")

E_yukawa = -K * sp.exp(-mu * d) / d
F_yukawa = -sp.diff(E_yukawa, d)
require_equal("attractive Yukawa separation derivative", F_yukawa, -K * sp.exp(-mu * d) * (mu / d + 1 / d**2))
checks.append("attractive Yukawa separation derivative")

F_massless = sp.limit(F_yukawa, mu, 0, dir="+")
require_equal("massless force limit", F_massless, -K / d**2)
checks.append("massless force limit")

screened_ratio = sp.simplify(field_strength / (A / r**2))
require_equal("screened-to-inverse-square ratio", screened_ratio, sp.exp(-mu * r) * (1 + mu * r))
checks.append("screened-to-inverse-square ratio")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Boundary Flux Field Bridge 50: Screened Field Long-Range Failure

## Purpose

This report tests the screened exterior equation:

```text
(Delta - mu^2)u = 0.
```

The goal is to show that screening destroys the exact long-range inverse-square
behavior unless `mu=0`.

## Validated Checks

{validation_bullets}

## Screened Exterior Solution

SymPy verifies:

```text
u(r)=A exp(-mu r)/r
```

solves:

```text
(Delta - mu^2)u = 0.
```

The field strength is:

```text
-u'(r)=A exp(-mu r)(mu/r + 1/r^2).
```

Relative to an inverse-square field `A/r^2`, the ratio is:

```text
exp(-mu r)(1+mu r).
```

This ratio is not constant for `mu>0`.

## Interaction Scaling

For attractive Yukawa interaction:

```text
E(d)=-K exp(-mu d)/d,
```

the separation derivative is:

```text
F_d=-K exp(-mu d)(mu/d + 1/d^2).
```

Only the massless limit gives:

```text
F_d=-K/d^2.
```

## Interpretation

The weak-field exterior equation must be massless/Laplace-like if the theory is
to preserve exact long-range inverse-square behavior.
"""

out = Path(__file__).with_name("50_screened_field_long_range_failure.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
