#!/usr/bin/env python3
"""
make_44_weak_field_nonlinear_extension.py

Validate a controlled nonlinear weak-field extension:

    E[u] = integral 4*pi*r^2 Phi((u')^2) dr

with example:

    Phi(z) = 1/2 z + alpha/4 z^2.

The conserved flux reduces to the Dirichlet flux in the weak-field limit, and
the first perturbative correction to the 1/r solution is computed.

Output:
    44_weak_field_nonlinear_extension.md
"""

from pathlib import Path
import sympy as sp


r = sp.symbols("r", positive=True)
Q, alpha = sp.symbols("Q alpha", real=True)
pi = sp.pi

s = sp.symbols("s", real=True)
z = sp.symbols("z", real=True)


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

# Nonlinear density Phi(z)=1/2 z + alpha/4 z^2 with z=s^2, where s=u'.
Phi = sp.Rational(1, 2) * z + alpha * z**2 / 4
radial_density = 4 * pi * r**2 * Phi.subs(z, s**2)
canonical_momentum = sp.diff(radial_density, s)

require_equal(
    "nonlinear canonical radial momentum",
    canonical_momentum,
    4 * pi * r**2 * (s + alpha * s**3),
)
checks.append("nonlinear canonical radial momentum")

# The conserved outward positive flux is minus the radial canonical momentum.
flux = -canonical_momentum
require_equal("weak-field flux limit", flux.subs(alpha, 0), -4 * pi * r**2 * s)
checks.append("weak-field flux limit")

# Let y=-u' be positive for a positive outward flux Q:
#   Q = 4*pi*r^2 (y + alpha*y^3).
# Perturbative solution:
#   y = y0 - alpha*y0^3 + O(alpha^2)
y0 = Q / (4 * pi * r**2)
y_approx = y0 - alpha * y0**3
flux_residual = sp.expand(4 * pi * r**2 * (y_approx + alpha * y_approx**3) - Q)
require_zero("perturbative flux residual through first order", sp.series(flux_residual, alpha, 0, 2).removeO())
checks.append("perturbative flux residual through first order")

# Potential with u(infinity)=0 is integral_r^infty y(sigma)d sigma.
u_approx = Q / (4 * pi * r) - alpha * Q**3 / (320 * pi**3 * r**5)
y_from_u = -sp.diff(u_approx, r)
require_zero("potential derivative matches perturbative y", sp.series(y_from_u - y_approx, alpha, 0, 2).removeO())
checks.append("potential derivative matches perturbative y")

require_equal("weak-field potential limit", u_approx.subs(alpha, 0), Q / (4 * pi * r))
checks.append("weak-field potential limit")

# The first nonlinear correction scales as r^-5.
correction = sp.expand(u_approx - u_approx.subs(alpha, 0))
scaled_correction = sp.simplify(correction * r**5 / alpha)
require_equal("first nonlinear correction coefficient", scaled_correction, -Q**3 / (320 * pi**3))
checks.append("first nonlinear correction coefficient")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Boundary Flux Field Bridge 44: Weak-Field Nonlinear Extension

## Purpose

This report tests a controlled nonlinear extension of the radial Dirichlet
energy.

The general radial energy form is:

```text
E[u] = integral 4*pi*r^2 Phi((u')^2) dr.
```

The concrete test density is:

```text
Phi(z) = 1/2 z + alpha/4 z^2.
```

## Validated Checks

{validation_bullets}

## Conserved Flux

For `s=u'`, the radial canonical momentum is:

```text
d/ds [4*pi*r^2 Phi(s^2)]
  =
  4*pi*r^2(s + alpha s^3).
```

The outward positive flux is:

```text
Q = -4*pi*r^2(u' + alpha (u')^3).
```

When `alpha=0`, this reduces to the Dirichlet flux:

```text
Q = -4*pi*r^2 u'.
```

## Perturbative Exterior Field

Let:

```text
y = -u' > 0.
```

Then:

```text
Q = 4*pi*r^2(y + alpha y^3).
```

With:

```text
y0 = Q/(4*pi*r^2),
```

the first-order perturbative solution is:

```text
y = y0 - alpha y0^3 + O(alpha^2).
```

Integrating from infinity gives:

```text
u(r)
  =
  Q/(4*pi*r)
  - alpha Q^3/(320*pi^3*r^5)
  + O(alpha^2).
```

## Interpretation

This proves that a nonlinear vacuum strain density can have the Dirichlet model
as its weak-field limit while producing controlled higher-order corrections.

The first correction in this example is not another `1/r` term. It scales as:

```text
r^-5.
```

That makes this kind of script useful for testing candidate nonlinear energy
densities: each candidate predicts a definite correction hierarchy.
"""

out = Path(__file__).with_name("44_weak_field_nonlinear_extension.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
