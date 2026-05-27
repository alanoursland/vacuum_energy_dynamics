#!/usr/bin/env python3
"""
make_43_radial_reduction_to_admissibility_defect.py

Show that the 3D radial source equation reduces to the same flux-obstruction
structure as the 1D transformed admissibility problem.

Output:
    43_radial_reduction_to_admissibility_defect.md
"""

from pathlib import Path
import sympy as sp


r, R = sp.symbols("r R", positive=True)
rho0 = sp.symbols("rho0", real=True)
Q = sp.symbols("Q", real=True)
pi = sp.pi

u = sp.Function("u")
rho = sp.Function("rho")


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

# 3D radial Poisson form:
#   -Delta u = rho
#   Q(r) = -4*pi*r^2*u'(r)
#   Q'(r) = 4*pi*r^2*rho(r).
radial_flux = -4 * pi * r**2 * sp.diff(u(r), r)
radial_laplacian = sp.diff(u(r), r, 2) + 2 * sp.diff(u(r), r) / r
flux_derivative_under_poisson = sp.diff(radial_flux, r).subs(radial_laplacian, -rho(r))

# Direct substitution of the compound laplacian does not replace inside the
# expanded derivative reliably, so verify by expansion.
expanded_flux_relation = sp.expand(
    sp.diff(radial_flux, r) - 4 * pi * r**2 * (-radial_laplacian)
)
require_zero("radial flux derivative identity", expanded_flux_relation)
checks.append("radial flux derivative identity")

# Uniform ball source: total charge inside radius R.
total_uniform_charge = sp.integrate(4 * pi * r**2 * rho0, (r, 0, R))
require_equal("uniform ball total charge", total_uniform_charge, 4 * pi * rho0 * R**3 / 3)
checks.append("uniform ball total charge")

# Exterior solution from total charge.
u_ext = total_uniform_charge / (4 * pi * r)
flux_ext = -4 * pi * r**2 * sp.diff(u_ext, r)
require_equal("exterior flux equals enclosed source", flux_ext, total_uniform_charge)
checks.append("exterior flux equals enclosed source")

require_zero("exterior source-free flux conservation", sp.diff(flux_ext, r))
checks.append("exterior source-free flux conservation")

# 1D transformed analog:
#   -u'' = F, J=-u', J'=F.
x = sp.symbols("x", real=True)
u1 = sp.Function("u1")
F = sp.Function("F")
J = -sp.diff(u1(x), x)
require_equal(
    "1D flux obstruction identity",
    sp.diff(J, x).subs(sp.diff(u1(x), x, 2), -F(x)),
    F(x),
)
checks.append("1D flux obstruction identity")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Boundary Flux Field Bridge 43: Radial Reduction to Admissibility Defect

## Purpose

This report strengthens the bridge between the earlier one-dimensional
regularity result and the 3D radial boundary-flux model.

It shows that both systems have the same conserved-flux obstruction structure.

## Validated Checks

{validation_bullets}

## 3D Radial Source Equation

Use the sign convention:

```text
-Delta u = rho.
```

For a radial field:

```text
Delta u = u'' + (2/r)u'.
```

Define enclosed flux/charge:

```text
Q(r) = -4*pi*r^2*u'(r).
```

Then:

```text
Q'(r) = 4*pi*r^2*rho(r).
```

So total enclosed source is exactly the change in radial flux.

## Uniform Ball Audit

For constant density `rho0` inside radius `R`:

```text
Q_total = integral_0^R 4*pi*r^2*rho0 dr
        = 4*pi*rho0*R^3/3.
```

The exterior solution is:

```text
u(r) = Q_total/(4*pi*r).
```

and its exterior flux is:

```text
-4*pi*r^2*u'(r) = Q_total.
```

## 1D Admissibility Analog

The transformed one-dimensional problem had:

```text
-u'' = F.
```

With:

```text
J = -u',
```

one gets:

```text
J' = F.
```

Thus:

```text
integral F dx
```

is the one-dimensional version of total enclosed source/flux.

## Interpretation

The earlier first admissibility condition:

```text
integral F dx = 0
```

is the zero-net-flux sector.

The boundary-field bridge keeps the same obstruction but interprets a controlled
nonzero value as boundary/source charge:

```text
integral F dx != 0
  -> nonzero conserved exterior flux.
```
"""

out = Path(__file__).with_name("43_radial_reduction_to_admissibility_defect.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
