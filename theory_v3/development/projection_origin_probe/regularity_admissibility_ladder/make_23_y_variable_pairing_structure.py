#!/usr/bin/env python3
"""
make_23_y_variable_pairing_structure.py

Rewrite the balanced projection pairing under y=x^2.

Output:
    23_y_variable_pairing_structure.md
"""

from pathlib import Path
import sympy as sp


x, y = sp.symbols("x y", positive=True)
k, q, R = sp.symbols("k q R", integer=True, positive=True)


def simplify_expr(expr):
    out = sp.simplify(expr)
    out = sp.factor(out)
    out = sp.powsimp(out, force=True)
    out = sp.cancel(out)
    out = sp.factor(out)
    return out


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

# y=x^2 gives dx = 1/(2 sqrt(y)) dy.
dxdy = sp.Rational(1, 2) * y ** sp.Rational(-1, 2)
a_y = 1 - y

r_k = (2 * k - 1) / (2 * k + 3)
psi_x = x ** (2 * k) - r_k * x ** (2 * k - 2)
psi_y = y ** k - r_k * y ** (k - 1)
require_zero("psi y transform", psi_x.subs(x, sp.sqrt(y)) - psi_y)
checks.append("psi_k becomes y^(k-1)(y-r_k)")

B_x = (1 - x**2) ** R * (x ** (2 * q) - sp.symbols("c"))
B_y = (1 - y) ** R * (y**q - sp.symbols("c"))
require_zero("balanced source y transform", B_x.subs(x, sp.sqrt(y)) - B_y)
checks.append("balanced sources become (1-y)^R(y^q-c)")

# Full pairing:
# int_0^1 psi_k(x) B_Rq(x) a^4 dx
# = 1/2 int_0^1 psi_k(y) (y^q-c)(1-y)^(R+4)y^(-1/2) dy.
c = sp.symbols("c")
x_integrand_y = (
    psi_x.subs(x, sp.sqrt(y))
    * ((1 - x**2) ** R * (x ** (2 * q) - c)).subs(x, sp.sqrt(y))
    * ((1 - x**2) ** 4).subs(x, sp.sqrt(y))
    * dxdy
)
y_integrand = sp.Rational(1, 2) * psi_y * (y**q - c) * (1 - y) ** (R + 4) * y ** sp.Rational(-1, 2)
require_zero("full y-pairing integrand", x_integrand_y - y_integrand)
checks.append("full y-pairing integrand verified")

# Balancing coefficient:
# c_Rq = int y^q y^-1/2(1-y)^(R+1) / int y^-1/2(1-y)^(R+1)
# since int_x a^(R+1)x^(2q) dx has the same 1/2 factor.
c_Rq_beta = sp.beta(q + sp.Rational(1, 2), R + 2) / sp.beta(sp.Rational(1, 2), R + 2)
c_Rq_product = sp.simplify(
    sp.rf(sp.Rational(1, 2), q) / sp.rf(R + sp.Rational(5, 2), q)
)
require_zero("balancing beta/product form", c_Rq_beta - c_Rq_product)
checks.append("balancing coefficient beta/product form")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Synthesis Proof 23: `y=x^2` Pairing Structure

## Purpose

This report rewrites the balanced projection pairing using:

```text
y = x^2.
```

## Validated Checks

{validation_bullets}

## Transformed Objects

The row tests become:

```text
psi_k(y) = y^k - ((2k-1)/(2k+3)) y^(k-1)
         = y^(k-1)(y-r_k).
```

Balanced sources become:

```text
B_(R,q)(y) = (1-y)^R (y^q - c_(R,q)).
```

The pairing becomes:

```text
integral_0^1 psi_k(x) B_(R,q)(x) a^4 dx

= 1/2 integral_0^1
    psi_k(y) (y^q-c_(R,q)) (1-y)^(R+4) y^(-1/2) dy.
```

So the problem is a Jacobi-type weighted polynomial pairing on `[0,1]`.

## Balancing Coefficient

The balancing coefficient is:

```text
c_(R,q)
  =
  B(q+1/2, R+2) / B(1/2, R+2)
```

or equivalently:

```text
c_(R,q)
  =
  (1/2)_q / (R+5/2)_q.
```

This is the `y`-variable form of the admissibility condition:

```text
integral_0^1 a B_(R,q) dx = 0.
```
"""

out = Path("23_y_variable_pairing_structure.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
