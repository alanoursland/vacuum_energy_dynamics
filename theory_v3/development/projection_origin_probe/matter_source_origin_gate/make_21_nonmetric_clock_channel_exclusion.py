#!/usr/bin/env python3
"""
make_21_nonmetric_clock_channel_exclusion.py

Validate the exclusion gate for independent nonmetric clock-rate channels.

Output:
    21_nonmetric_clock_channel_exclusion.md
"""

from pathlib import Path
import sympy as sp


r, alpha, c, C0, C1 = sp.symbols("r alpha c C0 C1", positive=True)


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

zeta = C0 + C1 / r
clock_extra = alpha * zeta
accel_extra = simplify_expr(-c**2 * sp.diff(clock_extra, r))
expected_accel = alpha * c**2 * C1 / r**2
require_zero("nonmetric clock channel exterior acceleration", accel_extra - expected_accel)
checks.append("independent clock channel with 1/r tail produces inverse-square acceleration")

require_zero("decoupled nonmetric clock route", accel_extra.subs(alpha, 0))
if simplify_expr(accel_extra.subs({alpha: 1, C1: 1})) == 0:
    raise AssertionError("nonzero coupling and nonzero tail should not be silent")
checks.append("for arbitrary nonzero tail, silence requires alpha=0")

require_zero("zero-tail nonmetric clock silence", accel_extra.subs(C1, 0))
checks.append("zero exterior tail also silences the nonmetric clock channel")

constant_shift = simplify_expr(clock_extra.subs(C1, 0))
if constant_shift == 0:
    raise AssertionError("constant channel shift should remain as a background-clock witness")
checks.append("constant exterior shift is not a force but remains a background-clock datum")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Matter Source Origin Gate 21: Nonmetric Clock Channel Exclusion

## Purpose

This proof checks what happens if an independent nonmetric channel changes
clock rate.

## Validated Checks

{validation_bullets}

## Setup

Let the clock rate contain an extra channel:

```text
d tau/dt = 1 + Phi/c^2 + alpha zeta.
```

For a source-free exterior scalar:

```text
zeta = C0 + C1/r.
```

The additional acceleration is:

```text
a_extra = -c^2 d(alpha zeta)/dr
        = alpha c^2 C1/r^2.
```

## Silence Routes

For an arbitrary nonzero exterior tail, silence requires:

```text
alpha = 0.
```

Alternatively, if the channel is allowed but must be exterior-silent:

```text
C1 = 0.
```

The remaining constant mode does not produce a force, but it is still a
background-clock datum that must be fixed or interpreted.

## Gate Interpretation

Nonmetric residual/projection channels cannot be allowed to alter clock rate
with a `1/r` tail. They either remain outside the clock coupling, have zero
exterior tail, or require an explicit new routing theorem.
"""

out = Path(__file__).with_name("21_nonmetric_clock_channel_exclusion.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Nonmetric clock channel exclusion passed.")
print(f"Wrote {out.resolve()}")
