#!/usr/bin/env python3
"""
make_25_operational_clock_redshift_universality.py

Validate the operational redshift universality gate.

Output:
    25_operational_clock_redshift_universality.md
"""

from pathlib import Path
import sympy as sp


phi, beta1, beta2, gamma1, gamma2 = sp.symbols("phi beta1 beta2 gamma1 gamma2")


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

rate1 = gamma1 * (1 + beta1 * phi)
rate2 = gamma2 * (1 + beta2 * phi)
calibrated_ratio = simplify_expr((rate1 / rate2) / (gamma1 / gamma2))
require_zero(
    "calibrated ratio",
    calibrated_ratio - (1 + beta1 * phi) / (1 + beta2 * phi),
)
checks.append("species calibration constants divide out of relative redshift")

first_order_ratio = sp.series(calibrated_ratio, phi, 0, 2).removeO()
expected_first_order = 1 + (beta1 - beta2) * phi
require_zero("first-order relative redshift", first_order_ratio - expected_first_order)
checks.append("relative redshift drift is controlled by beta1-beta2")

drift = simplify_expr(sp.diff(first_order_ratio, phi))
solution = sp.solve([sp.Eq(drift, 0)], [beta1], dict=True)
if solution != [{beta1: beta2}]:
    raise AssertionError(f"unexpected universality solution: {solution}")
checks.append("no operational species drift requires beta1=beta2")

require_zero("universal clock response", calibrated_ratio.subs(beta1, beta2) - 1)
checks.append("equal beta values give identical calibrated clock response")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Matter Source Origin Gate 25: Operational Clock Redshift Universality

## Purpose

This proof makes the interval-universality condition operational.

Two clock species may have different calibration constants. Those constants are
not the issue. The issue is whether their clock-rate response to the vacuum
interval changes differently as the potential changes.

## Validated Checks

{validation_bullets}

## Setup

Let the weak clock rates be:

```text
rate_1 = gamma_1 (1 + beta_1 phi)
rate_2 = gamma_2 (1 + beta_2 phi).
```

The constants `gamma_i` are fixed local calibration factors. Divide them out:

```text
R(phi) = (rate_1/rate_2)/(gamma_1/gamma_2)
       = (1 + beta_1 phi)/(1 + beta_2 phi).
```

To first order:

```text
R(phi) = 1 + (beta_1 - beta_2) phi.
```

Therefore no potential-dependent species drift requires:

```text
beta_1 = beta_2.
```

## Gate Interpretation

Operational interval universality means all clock species respond to the same
vacuum-defined interval with the same weak redshift coefficient. Calibration
constants are harmless; species-dependent response coefficients are not.
"""

out = Path(__file__).with_name("25_operational_clock_redshift_universality.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Operational clock redshift universality passed.")
print(f"Wrote {out.resolve()}")
