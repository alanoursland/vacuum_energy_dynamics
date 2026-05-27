#!/usr/bin/env python3
"""
make_38_admissibility_defect_boundary_charge.py

Validate the bridge between the 1D admissibility obstruction and a 3D boundary
charge/flux interpretation.

1D transformed problem:

    -u'' = F

has flux derivative:

    d(-u')/dx = F.

The first admissibility condition integral F dx = 0 is the zero-net-flux case.
If it is not zero, the obstruction can be recorded as an endpoint flux.

3D radial source-free exterior:

    d/dr[4*pi*r^2 u'] = 0

has conserved boundary flux:

    Q = -4*pi*r^2 u'.

Output:
    38_admissibility_defect_boundary_charge.md
"""

from pathlib import Path
import sympy as sp


x = sp.symbols("x", real=True)
r = sp.symbols("r", positive=True)
Q = sp.symbols("Q", real=True)
pi = sp.pi

u1 = sp.Function("u1")
F = sp.Function("F")


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

# 1D flux identity for -u''=F:
flux_1d = -sp.diff(u1(x), x)
require_equal(
    "1D flux derivative equals source under -u''=F",
    sp.diff(flux_1d, x).subs(sp.diff(u1(x), x, 2), -F(x)),
    F(x),
)
checks.append("1D flux derivative equals source under -u''=F")

# Polynomial audit: F=x^2-c on [0,1], c=1/3, has zero net flux.
c_balanced = sp.Rational(1, 3)
F_balanced = x**2 - c_balanced
require_zero("balanced polynomial has zero total source", sp.integrate(F_balanced, (x, 0, 1)))
checks.append("balanced polynomial has zero total source")

# Unbalanced source produces endpoint flux equal to its total integral.
F_unbalanced = x**2
total_unbalanced = sp.integrate(F_unbalanced, (x, 0, 1))
require_equal("unbalanced source total", total_unbalanced, sp.Rational(1, 3))
checks.append("unbalanced source total")

# 3D radial conserved flux for u=Q/(4*pi*r).
u_Q = Q / (4 * pi * r)
flux_3d = -4 * pi * r**2 * sp.diff(u_Q, r)
require_equal("3D radial conserved flux", flux_3d, Q)
checks.append("3D radial conserved flux")

require_zero("3D flux derivative vanishes in source-free exterior", sp.diff(flux_3d, r))
checks.append("3D flux derivative vanishes in source-free exterior")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Radial Boundary Field Bridge 38: Admissibility Defect as Boundary Charge

## Purpose

This report validates the conceptual bridge from the one-dimensional
regularity/admissibility result to the radial boundary-field interpretation.

The core idea is:

```text
zero endpoint obstruction -> admissible regular solution
nonzero endpoint obstruction -> controlled boundary flux / charge
```

## Validated Checks

{validation_bullets}

## 1D Transformed Problem

The regularity-admissibility ladder used:

```text
-u'' = F
```

with `F=aS`.

Define the 1D flux:

```text
J = -u'.
```

Then:

```text
J' = F.
```

Integrating over the domain gives:

```text
J(1)-J(0) = integral_0^1 F dx.
```

The first admissibility condition:

```text
integral_0^1 F dx = 0
```

is therefore the zero-net-flux case.

## Boundary-Charge Reading

If the first admissibility integral is not zero, the obstruction can be
recorded as an endpoint flux instead of treated only as a failure:

```text
Q_endpoint = integral F dx.
```

That is the mathematical move needed for the field-equation bridge.

## 3D Radial Exterior

In the 3D exterior source-free region, the radial flux is:

```text
Q = -4*pi*r^2*u'(r).
```

For:

```text
u(r) = Q/(4*pi*r),
```

SymPy verifies:

```text
Q = -4*pi*r^2*u'(r)
dQ/dr = 0.
```

So the same structural object that appeared as an endpoint obstruction in the
1D regularity problem becomes a conserved boundary charge in the 3D radial
field problem.

## Interpretation

The 1D proof said:

```text
regularity requires canceling the net source obstruction.
```

The radial bridge says:

```text
a mass-like boundary constraint is precisely a controlled nonzero obstruction,
carried as conserved exterior flux.
```

This is the first step toward field equations:

```text
admissibility defect
  -> boundary charge
  -> source-free exterior equation
  -> harmonic potential
  -> inverse-square field strength.
```
"""

out = Path(__file__).with_name("38_admissibility_defect_boundary_charge.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
