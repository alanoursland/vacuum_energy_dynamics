#!/usr/bin/env python3
"""
make_33_single_interval_universal_beta_gate.py

Validate that a single interval source gives one universal beta, while
species-specific interval scaling violates universality.

Output:
    33_single_interval_universal_beta_gate.md
"""

from pathlib import Path
import sympy as sp


phi, beta1, beta2, s1, s2 = sp.symbols("phi beta1 beta2 s1 s2")


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

single_interval_rate = 1 + phi
species1_rate = single_interval_rate
species2_rate = single_interval_rate
require_zero("single interval species equality", species1_rate - species2_rate)
checks.append("one interval gives identical first-order clock response")

scaled1 = 1 + s1 * phi
scaled2 = 1 + s2 * phi
relative = sp.series(scaled1 / scaled2, phi, 0, 2).removeO()
drift = simplify_expr(sp.diff(relative, phi))
solution = sp.solve([sp.Eq(drift, 0)], [s1], dict=True)
if solution != [{s1: s2}]:
    raise AssertionError(f"unexpected species scaling solution: {solution}")
checks.append("species-specific interval scaling is universal only if s1=s2")

beta_map1 = simplify_expr(sp.diff(scaled1, phi))
beta_map2 = simplify_expr(sp.diff(scaled2, phi))
require_zero("beta mapping for species 1", beta_map1 - s1)
require_zero("beta mapping for species 2", beta_map2 - s2)
checks.append("species scaling maps directly to beta coefficients")

require_zero("standard single interval beta", beta_map1.subs(s1, 1) - 1)
checks.append("standard single interval has beta=1")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Matter Source Origin Gate 33: Single-Interval Universal Beta Gate

## Purpose

This proof connects interval uniqueness to the earlier species beta gate.

## Validated Checks

{validation_bullets}

## Single Interval

If every matter probe uses the same weak interval response:

```text
rate = 1 + phi,
```

then every species has the same first-order clock response.

## Species-Scaled Intervals

If species instead respond as:

```text
rate_i = 1 + s_i phi,
```

then `s_i` is exactly the beta coefficient:

```text
beta_i = s_i.
```

No relative redshift drift requires:

```text
s_1 = s_2.
```

## Gate Interpretation

The universal beta condition is equivalent, in the weak clock sector, to all
species coupling to the same interval scale. A single vacuum-defined interval
would provide this automatically; species-specific interval scaling would break
it.
"""

out = Path(__file__).with_name("33_single_interval_universal_beta_gate.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Single-interval universal beta gate passed.")
print(f"Wrote {out.resolve()}")
