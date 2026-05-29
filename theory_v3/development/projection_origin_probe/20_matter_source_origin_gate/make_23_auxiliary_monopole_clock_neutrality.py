#!/usr/bin/env python3
"""
make_23_auxiliary_monopole_clock_neutrality.py

Validate the monopole-neutrality condition for auxiliary clock/source channels.

Output:
    23_auxiliary_monopole_clock_neutrality.md
"""

from pathlib import Path
import sympy as sp


r, R, rho0, eps_h, eps_p, G, c = sp.symbols("r R rho0 eps_h eps_p G c", positive=True)
pi = sp.pi
alpha = 8 * pi * G / c**2


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_nonzero(label, expr):
    result = simplify_expr(expr)
    if result == 0:
        raise AssertionError(f"{label} unexpectedly vanished")
    return result


checks = []

H = r**2 - sp.Rational(3, 5) * R**2
P = r**4 - sp.Rational(3, 7) * R**4

monopole_H = simplify_expr(4 * pi * sp.integrate(H * r**2, (r, 0, R)))
monopole_P = simplify_expr(4 * pi * sp.integrate(P * r**2, (r, 0, R)))
require_zero("H zero monopole", monopole_H)
require_zero("P zero monopole", monopole_P)
checks.append("two independent auxiliary shapes have zero radial monopole")

shape_H = require_nonzero("H shape witness", simplify_expr(4 * pi * sp.integrate(H * r**4, (r, 0, R))))
shape_P = require_nonzero("P shape witness", simplify_expr(4 * pi * sp.integrate(P * r**4, (r, 0, R))))
checks.append("auxiliary shapes are not zero functions")

rho_total = rho0 + eps_h * H + eps_p * P
M_total = simplify_expr(4 * pi * sp.integrate(rho_total * r**2, (r, 0, R)))
M_base = simplify_expr(4 * pi * sp.integrate(rho0 * r**2, (r, 0, R)))
require_zero("auxiliary zero-monopole mass neutrality", M_total - M_base)
checks.append("zero-monopole auxiliary channels leave enclosed mass unchanged")

flux_shift = simplify_expr(alpha * (M_total - M_base))
require_zero("zero-monopole auxiliary flux neutrality", flux_shift)
checks.append("zero-monopole auxiliary channels leave exterior A flux unchanged")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Matter Source Origin Gate 23: Auxiliary Monopole Clock Neutrality

## Purpose

This proof gives the allowed route for auxiliary residual/projection channels
if they are represented in a source-like way:

```text
their routed ordinary monopole must vanish.
```

## Validated Checks

{validation_bullets}

## Witness Shapes

Use:

```text
H(r) = r^2 - (3/5)R^2
P(r) = r^4 - (3/7)R^4.
```

Both satisfy:

```text
4*pi integral_0^R H r^2 dr = 0
4*pi integral_0^R P r^2 dr = 0.
```

But they are not zero as shapes. For example:

```text
4*pi integral_0^R H r^4 dr = {shape_H}
4*pi integral_0^R P r^4 dr = {shape_P}
```

## Source Ledger

For:

```text
rho_total = rho0 + eps_h H + eps_p P,
```

the enclosed ordinary mass is unchanged:

```text
M_total = M_base.
```

Therefore the exterior A-sector flux is unchanged:

```text
Delta F_A = 0.
```

## Gate Interpretation

Auxiliary structures may carry internal shape information. They do not become
ordinary matter source unless they carry routed monopole. This is the safe
compatibility condition for projection/admissibility diagnostics.
"""

out = Path(__file__).with_name("23_auxiliary_monopole_clock_neutrality.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Auxiliary monopole clock neutrality passed.")
print(f"Wrote {out.resolve()}")
