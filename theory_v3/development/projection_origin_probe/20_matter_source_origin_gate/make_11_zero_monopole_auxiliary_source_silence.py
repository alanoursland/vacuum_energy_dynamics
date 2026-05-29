#!/usr/bin/env python3
"""
make_11_zero_monopole_auxiliary_source_silence.py

Validate that an auxiliary source with zero radial monopole does not change
the exterior A-sector mass flux.

Output:
    11_zero_monopole_auxiliary_source_silence.md
"""

from pathlib import Path
import sympy as sp


r, R, eps, G, c = sp.symbols("r R epsilon G c", positive=True)
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
monopole_H = simplify_expr(4 * pi * sp.integrate(H * r**2, (r, 0, R)))
require_zero("zero monopole auxiliary source", monopole_H)
checks.append("chosen auxiliary source has zero radial monopole")

shape_moment_H = simplify_expr(4 * pi * sp.integrate(H * r**4, (r, 0, R)))
nonzero_shape = require_nonzero("nonzero shape moment", shape_moment_H)
checks.append("auxiliary source is not pointwise zero and has nonzero shape moment")

delta_flux = simplify_expr(alpha * eps * monopole_H)
require_zero("zero exterior flux shift", delta_flux)
checks.append("zero-monopole auxiliary source gives no exterior A flux shift")

rho0 = sp.symbols("rho0", positive=True)
M_total = simplify_expr(4 * pi * sp.integrate((rho0 + eps * H) * r**2, (r, 0, R)))
M_base = simplify_expr(4 * pi * sp.integrate(rho0 * r**2, (r, 0, R)))
require_zero("total mass unchanged by zero-monopole auxiliary source", M_total - M_base)
checks.append("adding the auxiliary source leaves enclosed ordinary mass unchanged")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Matter Source Origin Gate 11: Zero-Monopole Auxiliary Source Silence

## Purpose

This proof records the allowed way an auxiliary source-like object can remain
safe in the A-sector:

```text
it may have internal shape,
but its ordinary mass monopole must vanish.
```

## Validated Checks

{validation_bullets}

## Witness

Use the compact interior shape:

```text
H(r) = r^2 - (3/5)R^2.
```

It is not zero as a function. Its higher shape moment is:

```text
4*pi integral_0^R H r^4 dr = {nonzero_shape}.
```

But its radial monopole vanishes:

```text
4*pi integral_0^R H r^2 dr = 0.
```

Therefore adding `epsilon H` to an A-sector source produces no exterior mass
flux shift:

```text
Delta F_A = (8*pi*G/c^2) epsilon integral H dV = 0.
```

## Gate Interpretation

This gives a precise safety condition for any residual or projection-derived
source candidate: it may only enter the A-sector without changing ordinary
mass if its routed monopole is zero. Otherwise it duplicates or shifts the
ordinary source ledger.
"""

out = Path(__file__).with_name("11_zero_monopole_auxiliary_source_silence.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Zero-monopole auxiliary source silence passed.")
print(f"Wrote {out.resolve()}")
