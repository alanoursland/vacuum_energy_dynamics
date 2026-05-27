#!/usr/bin/env python3
"""
make_73_nonlinear_energy_convexity.py

Validate convexity conditions for polynomial nonlinear strain densities:

    W(g) = 1/2 |g|^2 + alpha/(2p) |g|^(2p).

Output:
    73_nonlinear_energy_convexity.md
"""

from pathlib import Path
import sympy as sp


gx, gy, alpha = sp.symbols("gx gy alpha", real=True)
p = sp.symbols("p", integer=True, positive=True)


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []
rows = []

z = gx**2 + gy**2

for pval in range(1, 6):
    W = sp.Rational(1, 2) * z + alpha * z**pval / (2 * pval)
    H = sp.hessian(W, (gx, gy))

    # Tangential direction at point (g,0): vector (0,1).
    g = sp.symbols("g", positive=True)
    H_axis = sp.simplify(H.subs({gx: g, gy: 0}))
    tangential = sp.simplify(H_axis[1, 1])
    radial = sp.simplify(H_axis[0, 0])

    require_equal(f"tangential Hessian eigenvalue p={pval}", tangential, 1 + alpha * g ** (2 * pval - 2))
    require_equal(f"radial Hessian eigenvalue p={pval}", radial, 1 + alpha * (2 * pval - 1) * g ** (2 * pval - 2))
    rows.append((pval, sp.sstr(tangential), sp.sstr(radial)))

checks.append("radial and tangential Hessian eigenvalues verified for p=1..5")

row_lines = "\n".join(
    f"p={pval}: tangential={tangent}, radial={radial}"
    for pval, tangent, radial in rows
)
validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Boundary Flux Field Bridge 73: Nonlinear Energy Convexity

## Purpose

This report validates convexity conditions for nonlinear scalar strain
densities:

```text
W(g) = 1/2 |g|^2 + alpha/(2p)|g|^(2p).
```

## Validated Checks

{validation_bullets}

## Hessian Eigenvalues

At a point where `|g|=g`, the Hessian has tangential and radial eigenvalues:

```text
{row_lines}
```

Thus for:

```text
alpha >= 0,
```

both eigenvalues are positive.

## Interpretation

Positive polynomial nonlinear coefficients preserve convexity of the scalar
strain density. Negative coefficients can destabilize the energy and match the
invertibility failures found in proof `72`.
"""

out = Path(__file__).with_name("73_nonlinear_energy_convexity.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
