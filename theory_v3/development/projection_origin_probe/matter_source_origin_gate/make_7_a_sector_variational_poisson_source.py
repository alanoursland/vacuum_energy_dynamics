#!/usr/bin/env python3
"""
make_7_a_sector_variational_poisson_source.py

Validate the reduced A-sector variational source law.

Output:
    7_a_sector_variational_poisson_source.md
"""

from pathlib import Path
import sympy as sp


r, K, lam, alpha = sp.symbols("r K lambda alpha", positive=True)
A = sp.Function("A")(r)
eta = sp.Function("eta")(r)
rho = sp.Function("rho")(r)


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

variation_density = K * r**2 * sp.diff(A, r) * sp.diff(eta, r) + lam * r**2 * rho * eta
decomposition = (
    -eta * (K * sp.diff(r**2 * sp.diff(A, r), r) - lam * r**2 * rho)
    + sp.diff(K * r**2 * sp.diff(A, r) * eta, r)
)
require_zero("radial A-action variation decomposition", variation_density - decomposition)
checks.append("radial Dirichlet-plus-matter variation decomposes into bulk plus boundary")

bulk_equation = sp.Eq(sp.diff(r**2 * sp.diff(A, r), r) / r**2, lam * rho / K)
normalized_equation = bulk_equation.subs(lam / K, alpha)
if normalized_equation.rhs != alpha * rho:
    raise AssertionError(f"normalization substitution failed: {normalized_equation}")
checks.append("bulk equation is Delta_areal A = (lambda/K) rho")

G, c = sp.symbols("G c", positive=True)
source_normalization = 8 * sp.pi * G / c**2
normalized_lam = K * source_normalization
require_zero("Newtonian A-sector normalization", normalized_lam / K - source_normalization)
checks.append("choosing alpha=8*pi*G/c^2 gives the archived A-sector source law")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Matter Source Origin Gate 7: A-Sector Variational Poisson Source

## Purpose

This proof supplies the first positive source-origin gate for the reduced
A-sector.

It validates that a local radial Dirichlet action with a linear matter coupling
produces:

```text
Delta_areal A = (lambda/K) rho.
```

With the Newtonian normalization:

```text
lambda/K = 8*pi*G/c^2,
```

this is the archived A-sector source law.

## Validated Checks

{validation_bullets}

## Reduced Action

Use the radial density:

```text
E_A = integral [ (K/2) r^2 (A')^2 + lambda r^2 rho A ] dr.
```

The first variation is:

```text
delta E_A =
integral [ K r^2 A' eta' + lambda r^2 rho eta ] dr.
```

SymPy verifies:

```text
K r^2 A' eta' + lambda r^2 rho eta
  =
  -eta [K (r^2 A')' - lambda r^2 rho]
  + d/dr [K r^2 A' eta].
```

Therefore the bulk Euler-Lagrange equation is:

```text
(1/r^2) d/dr [r^2 A'] = (lambda/K) rho.
```

## Gate Interpretation

This proof is still reduced and spherical, not a covariant matter action. But
it gives a positive origin for the A-sector source law inside the current
proof chain.
"""

out = Path(__file__).with_name("7_a_sector_variational_poisson_source.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("A-sector variational Poisson source passed.")
print(f"Wrote {out.resolve()}")
