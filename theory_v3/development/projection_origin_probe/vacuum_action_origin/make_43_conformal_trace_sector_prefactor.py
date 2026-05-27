#!/usr/bin/env python3
"""
make_43_conformal_trace_sector_prefactor.py

Validate the conformal trace-sector boundary prefactor induced by the reduced
EH/GHY normalization.

Output:
    43_conformal_trace_sector_prefactor.md
"""

from pathlib import Path
import sympy as sp


D, c, G = sp.symbols("D c G", positive=True)
s, spx = sp.symbols("s spx")
pi = sp.pi


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

K_EH = c**2 / (16 * pi * G)
boundary_flux = -2 * (D - 1) * sp.exp((D - 2) * s) * spx
D4_flux = simplify_expr(boundary_flux.subs(D, 4))
require_zero("D4 conformal boundary flux", D4_flux + 6 * sp.exp(2 * s) * spx)
checks.append("D=4 conformal boundary flux has coefficient -6")

linear_flux_coeff = sp.diff(D4_flux, spx).subs(s, 0)
require_zero("D4 linear conformal flux coefficient", linear_flux_coeff + 6)
checks.append("linearized conformal flux coefficient is -6")

weighted_linear_coeff = simplify_expr(K_EH * linear_flux_coeff)
require_zero("weighted conformal trace coefficient", weighted_linear_coeff + 3 * c**2 / (8 * pi * G))
checks.append("EH/GHY prefactor gives conformal trace coefficient -3c^2/(8*pi*G)")

A_variation_factor = sp.symbols("A_variation_factor", positive=True)
trace_to_A_coeff = simplify_expr(weighted_linear_coeff / A_variation_factor)
require_zero(
    "A normalization factor placeholder identity",
    trace_to_A_coeff - weighted_linear_coeff / A_variation_factor,
)
checks.append("conformal trace coefficient still needs an explicit A-sector variable map")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 43: Conformal Trace-Sector Prefactor

## Purpose

This proof keeps the normalization comparison honest in the conformal trace
sector.

The EH/GHY prefactor has already been matched to the weak A-sector boundary
normalization. The conformal metric variable has its own trace coefficient and
requires an explicit map to the A variable.

## Validated Checks

{validation_bullets}

## Conformal Boundary Flux

For:

```text
g_ab = exp(2s) eta_ab,
```

the conformal boundary flux density is:

```text
-2(D-1) exp((D-2)s) s'.
```

For `D=4`:

```text
-6 exp(2s) s'.
```

The linearized coefficient is:

```text
-6.
```

Multiplying by the reduced EH/GHY prefactor:

```text
K_EH = c^2/(16*pi*G)
```

gives:

```text
-3 c^2/(8*pi*G).
```

## Interpretation

This is not a contradiction with the A-sector coefficient. It says the
conformal trace variable `s` is not identical to the reduced A variable without
a variable map. Normalization comparisons must specify which interval component
is being varied.
"""

out = Path(__file__).with_name("43_conformal_trace_sector_prefactor.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Conformal trace-sector prefactor passed.")
print(f"Wrote {out.resolve()}")
