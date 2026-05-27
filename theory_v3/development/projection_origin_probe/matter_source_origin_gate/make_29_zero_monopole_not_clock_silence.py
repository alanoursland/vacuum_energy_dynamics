#!/usr/bin/env python3
"""
make_29_zero_monopole_not_clock_silence.py

Validate that zero monopole is enough for exterior mass neutrality but not
enough for local clock neutrality.

Output:
    29_zero_monopole_not_clock_silence.md
"""

from pathlib import Path
import sympy as sp


r, R, alpha, c = sp.symbols("r R alpha c", positive=True)
pi = sp.pi


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
monopole = simplify_expr(4 * pi * sp.integrate(H * r**2, (r, 0, R)))
require_zero("zero monopole shape", monopole)
checks.append("H has zero routed ordinary monopole")

clock_shift = alpha * H
local_accel = simplify_expr(-c**2 * sp.diff(clock_shift, r))
nonzero_accel = require_nonzero("local clock acceleration witness", local_accel)
checks.append("the same H gives a nonzero local clock-force witness if coupled to clocks")

require_zero("clock decoupling route", local_accel.subs(alpha, 0))
checks.append("clock decoupling alpha=0 silences the local clock effect")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Matter Source Origin Gate 29: Zero Monopole Is Not Clock Silence

## Purpose

This proof separates two safety concepts:

```text
zero exterior mass monopole
```

and:

```text
zero local clock-rate effect.
```

The first does not imply the second.

## Validated Checks

{validation_bullets}

## Witness Shape

Use:

```text
H(r) = r^2 - (3/5)R^2.
```

It has zero ordinary radial monopole:

```text
4*pi integral_0^R H r^2 dr = 0.
```

So it does not shift exterior A-sector mass if routed only through the
ordinary monopole ledger.

## Clock-Coupled Failure

If the same shape changes clock rate:

```text
d tau/dt -> d tau/dt + alpha H,
```

then the local clock-force witness is:

```text
-c^2 d(alpha H)/dr = {nonzero_accel}.
```

This is not zero.

## Gate Interpretation

Zero monopole is enough for exterior mass neutrality, but not enough for local
clock neutrality. Auxiliary projection/residual structures must either remain
outside the clock coupling or be given a physical interpretation as local
clock-rate effects.
"""

out = Path(__file__).with_name("29_zero_monopole_not_clock_silence.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Zero-monopole not clock-silence gate passed.")
print(f"Wrote {out.resolve()}")
