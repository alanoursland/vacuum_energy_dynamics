#!/usr/bin/env python3
"""
make_34_auxiliary_second_interval_exclusion.py

Validate that an auxiliary field coupled as a second interval component creates
an independent operational clock response unless decoupled, locked, or silent.

Output:
    34_auxiliary_second_interval_exclusion.md
"""

from pathlib import Path
import sympy as sp


phi, zeta, alpha, beta, lam = sp.symbols("phi zeta alpha beta lambda")


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

rate = 1 + phi + alpha * zeta
response_phi = sp.diff(rate, phi)
response_zeta = sp.diff(rate, zeta)
require_zero("phi response", response_phi - 1)
require_zero("zeta response", response_zeta - alpha)
checks.append("auxiliary interval channel introduces independent zeta response alpha")

decoupled_rate = simplify_expr(rate.subs(alpha, 0))
require_zero("decoupled auxiliary interval", decoupled_rate - (1 + phi))
checks.append("alpha=0 restores the single-interval clock response")

locked_rate = simplify_expr(rate.subs(zeta, lam * phi))
locked_beta = simplify_expr(sp.diff(locked_rate, phi))
require_zero("locked auxiliary beta", locked_beta - (1 + alpha * lam))
checks.append("if zeta=lambda phi, the auxiliary channel renormalizes beta")

require_zero(
    "locked beta unchanged only by zero product",
    (locked_beta - 1).subs(alpha * lam, 0),
)
checks.append("locked auxiliary channel preserves beta only when alpha*lambda=0")

silent_rate = simplify_expr(rate.subs(zeta, 0))
require_zero("silent auxiliary interval", silent_rate - (1 + phi))
checks.append("zeta=0 on the operational clock sector is also silent")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Matter Source Origin Gate 34: Auxiliary Second-Interval Exclusion

## Purpose

This proof checks what happens if a residual/projection variable enters the
clock interval as an independent second channel.

## Validated Checks

{validation_bullets}

## Setup

Let the clock response be:

```text
rate = 1 + phi + alpha zeta.
```

Then:

```text
d rate/d phi = 1
d rate/d zeta = alpha.
```

So `zeta` is an independent operational clock response unless it is silenced
or locked.

## Safe Routes

The clean decoupling route is:

```text
alpha = 0.
```

The exterior-silent route is:

```text
zeta = 0
```

on the operational clock sector.

If instead:

```text
zeta = lambda phi,
```

then the effective beta becomes:

```text
beta_eff = 1 + alpha lambda.
```

That preserves the standard beta only when:

```text
alpha lambda = 0.
```

## Gate Interpretation

Auxiliary projection/residual structures cannot quietly modify the interval
seen by matter. They must decouple from clocks, be operationally silent, or be
promoted to explicit physical fields with a new beta/source ledger.
"""

out = Path(__file__).with_name("34_auxiliary_second_interval_exclusion.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Auxiliary second-interval exclusion passed.")
print(f"Wrote {out.resolve()}")
