#!/usr/bin/env python3
"""
make_49_dimension_dependence_inverse_square.py

Validate the spatial-dimension dependence of the radial Laplace bridge.

For n > 2:

    u(r) = Q / ((n-2) Omega_n) * r^(2-n)

has conserved flux:

    Q = -Omega_n r^(n-1) u'(r).

The field strength scales as r^(1-n), so inverse-square strength is specific to
n=3 spatial dimensions.

Output:
    49_dimension_dependence_inverse_square.md
"""

from pathlib import Path
import sympy as sp


r = sp.symbols("r", positive=True)
n = sp.symbols("n", integer=True, positive=True)
Omega = sp.symbols("Omega", positive=True)
Q = sp.symbols("Q", real=True)
pi = sp.pi


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

u_n = Q * r ** (2 - n) / ((n - 2) * Omega)
radial_laplacian_n = sp.diff(u_n, r, 2) + (n - 1) * sp.diff(u_n, r) / r
flux_n = -Omega * r ** (n - 1) * sp.diff(u_n, r)

require_zero("n-dimensional harmonic power for n>2", radial_laplacian_n)
checks.append("n-dimensional harmonic power for n>2")
require_equal("n-dimensional conserved flux", flux_n, Q)
checks.append("n-dimensional conserved flux")

field_strength_n = -sp.diff(u_n, r)
scaled_field = sp.simplify(field_strength_n * r ** (n - 1))
require_equal("n-dimensional field-strength scaling coefficient", scaled_field, Q / Omega)
checks.append("n-dimensional field-strength scaling coefficient")

u_3 = sp.simplify(u_n.subs({n: 3, Omega: 4 * pi}))
field_3 = sp.simplify(field_strength_n.subs({n: 3, Omega: 4 * pi}))
require_equal("three-dimensional potential", u_3, Q / (4 * pi * r))
checks.append("three-dimensional potential")
require_equal("three-dimensional inverse-square field", field_3, Q / (4 * pi * r**2))
checks.append("three-dimensional inverse-square field")

# n=2 logarithmic special case.
Omega2 = sp.symbols("Omega2", positive=True)
u_2 = -Q * sp.log(r) / Omega2
lap_2 = sp.diff(u_2, r, 2) + sp.diff(u_2, r) / r
flux_2 = -Omega2 * r * sp.diff(u_2, r)
require_zero("two-dimensional logarithmic harmonic field", lap_2)
checks.append("two-dimensional logarithmic harmonic field")
require_equal("two-dimensional conserved flux", flux_2, Q)
checks.append("two-dimensional conserved flux")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Boundary Flux Field Bridge 49: Dimension Dependence of Inverse-Square Scaling

## Purpose

This report proves that inverse-square field strength is the spatial
three-dimensional case of the radial Laplace boundary-flux bridge.

## Validated Checks

{validation_bullets}

## General `n > 2` Result

Let `Omega_n` be the area of the unit `(n-1)`-sphere.

For `n > 2`, the flux-normalized exterior field is:

```text
u(r) = Q / ((n-2)Omega_n) * r^(2-n).
```

It satisfies:

```text
u'' + ((n-1)/r)u' = 0
```

and:

```text
Q = -Omega_n r^(n-1) u'(r).
```

Therefore:

```text
|u'(r)| proportional to r^(1-n).
```

## Three Spatial Dimensions

For `n=3` and `Omega_3=4*pi`:

```text
u(r)=Q/(4*pi*r)
|u'(r)|=Q/(4*pi*r^2).
```

So inverse-square strength is not generic. It is the 3D member of the
dimension-dependent Laplace/flux family.

## Two Spatial Dimensions

The `n=2` special case is logarithmic:

```text
u(r)=-(Q/Omega_2)log(r),
```

with conserved flux but non-inverse-square field behavior.

## Interpretation

The bridge now explains why the inverse-square law appears at this level:

```text
source-free Laplace equation + conserved flux + three spatial dimensions.
```
"""

out = Path(__file__).with_name("49_dimension_dependence_inverse_square.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
