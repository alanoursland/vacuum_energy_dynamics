#!/usr/bin/env python3
"""
make_14_metric_stress_source_reduction.py

Validate that metric variation of a nonrelativistic matter source reduces to a
density source for the A-sector component.

Output:
    14_metric_stress_source_reduction.md
"""

from pathlib import Path
import sympy as sp


rho, c, eta, kappa = sp.symbols("rho c eta kappa", positive=True)


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

# In the weak static sector, g_00 = -A, so delta g_00 = -delta A.
T00 = rho * c**2
delta_g00 = -eta
delta_S_m = sp.Rational(1, 2) * T00 * delta_g00
source_coefficient = simplify_expr(delta_S_m / eta)
require_zero("stress coupling A-variation source", source_coefficient + sp.Rational(1, 2) * rho * c**2)
checks.append("metric matter variation is proportional to rho c^2 in the A component")

# A gravitational coupling normalization kappa converts this stress source into
# the field-equation source coefficient.  This is a normalization gate, not a
# derivation of kappa.
normalized_source = simplify_expr(kappa * T00)
target_source = sp.symbols("target_source")
require_zero(
    "Einstein normalization proxy",
    normalized_source.subs(kappa, 8 * sp.pi / c**4) - 8 * sp.pi * rho / c**2,
)
checks.append("standard 8*pi/c^4 coupling maps T00=rho c^2 to 8*pi*rho/c^2")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Matter Source Origin Gate 14: Metric Stress Source Reduction

## Purpose

This proof checks the local metric-coupling source reduction behind the
A-sector matter law.

It does not derive the gravitational coupling constant. It verifies the source
type: nonrelativistic matter enters the weak metric through mass-energy density.

## Validated Checks

{validation_bullets}

## A-Sector Variation

In the static weak sector:

```text
g_00 = -A
delta g_00 = -delta A.
```

For nonrelativistic matter:

```text
T^00 approximately rho c^2.
```

The standard metric variation has the local form:

```text
delta S_m = (1/2) T^00 delta g_00.
```

Therefore:

```text
delta S_m = -(1/2) rho c^2 delta A.
```

So the A-component source is proportional to ordinary mass density.

## Normalization Proxy

With the standard geometric coupling scale:

```text
kappa = 8*pi/c^4
```

the stress source maps as:

```text
kappa T^00 = 8*pi rho/c^2.
```

Restoring `G` gives the coefficient used earlier:

```text
8*pi*G*rho/c^2.
```

## Gate Interpretation

This is the covariant source-type bridge. The A-sector source is not an
arbitrary scalar; it is the weak static reduction of metric coupling to
stress-energy.
"""

out = Path(__file__).with_name("14_metric_stress_source_reduction.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Metric stress source reduction passed.")
print(f"Wrote {out.resolve()}")
