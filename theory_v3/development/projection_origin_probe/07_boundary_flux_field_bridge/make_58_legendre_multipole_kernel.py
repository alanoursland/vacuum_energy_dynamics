#!/usr/bin/env python3
"""
make_58_legendre_multipole_kernel.py

Validate the Legendre multipole kernel expansion to finite order and show that
uniform spherical flux keeps only the l=0 mode.

Output:
    58_legendre_multipole_kernel.md
"""

from pathlib import Path
import sympy as sp


t, eps = sp.symbols("t eps", real=True)


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

N = 8
kernel = 1 / sp.sqrt(1 - 2 * eps * t + eps**2)
series_kernel = sp.series(kernel, eps, 0, N + 1).removeO()
legendre_sum = sum(sp.legendre(l, t) * eps**l for l in range(N + 1))

require_zero("Legendre generating expansion through order 8", sp.expand(series_kernel - legendre_sum))
checks.append("Legendre generating expansion through order 8")

for l in range(1, N + 1):
    avg = sp.integrate(sp.legendre(l, t), (t, -1, 1))
    require_zero(f"uniform sphere removes l={l}", avg)

require_equal("uniform sphere keeps l=0 average", sp.integrate(sp.legendre(0, t), (t, -1, 1)) / 2, 1)
checks.append("uniform sphere keeps l=0 average")
checks.append("uniform spherical average removes l=1..8")

# Orthogonality check for low modes.
for l in range(0, 6):
    for m in range(0, 6):
        val = sp.integrate(sp.legendre(l, t) * sp.legendre(m, t), (t, -1, 1))
        expected = sp.Rational(2, 2 * l + 1) if l == m else 0
        require_equal(f"Legendre orthogonality l={l} m={m}", val, expected)

checks.append("Legendre orthogonality verified for l,m=0..5")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Boundary Flux Field Bridge 58: Legendre Multipole Kernel

## Purpose

This report validates the multipole expansion machinery behind the finite
boundary proofs.

## Validated Checks

{validation_bullets}

## Generating Expansion

For `|eps| < 1`:

```text
1/sqrt(1 - 2 eps t + eps^2)
  =
  sum_l eps^l P_l(t).
```

SymPy verifies this expansion through order `8`.

## Uniform Spherical Flux

Uniform spherical averaging integrates over `t=cos(theta)`.

For `l > 0`:

```text
integral_-1^1 P_l(t) dt = 0.
```

For `l=0`:

```text
(1/2) integral_-1^1 P_0(t) dt = 1.
```

Therefore uniform spherical flux keeps only the monopole mode.

## Interpretation

This explains why proof `40` had no finite-radius correction in the uniform
monopole sector. Finite-radius corrections enter through nonuniform boundary
data, induced multipoles, fixed-potential response, or higher external field
gradients.
"""

out = Path(__file__).with_name("58_legendre_multipole_kernel.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
