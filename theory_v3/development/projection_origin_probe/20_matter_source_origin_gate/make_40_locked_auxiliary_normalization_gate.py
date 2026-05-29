#!/usr/bin/env python3
"""
make_40_locked_auxiliary_normalization_gate.py

Validate that locking an auxiliary interval channel to the metric interval
renormalizes the matter source coefficient unless the product alpha*lambda
vanishes or the normalization is explicitly changed.

Output:
    40_locked_auxiliary_normalization_gate.md
"""

from pathlib import Path
import sympy as sp


A, alpha, lam, M = sp.symbols("A alpha lambda M", positive=True)


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

A_eff = (1 + alpha * lam) * A
S_m = -M * sp.sqrt(A_eff)
dS_dA = simplify_expr(sp.diff(S_m, A))
standard_dS = -M / (2 * sp.sqrt(A))
ratio = simplify_expr(dS_dA / standard_dS)
expected_ratio = sp.sqrt(1 + alpha * lam)
require_zero("locked auxiliary source coefficient ratio", ratio - expected_ratio)
checks.append("locked auxiliary interval rescales the matter source coefficient")

weak_ratio = sp.series(expected_ratio, alpha * lam, 0, 2).removeO()
require_zero("weak locked renormalization", weak_ratio - (1 + alpha * lam / 2))
checks.append("weak renormalization is 1 + alpha*lambda/2")

require_zero("zero locked product preserves normalization", ratio.subs(alpha * lam, 0) - 1)
checks.append("standard normalization is preserved when alpha*lambda=0")

if simplify_expr(ratio.subs({alpha: 1, lam: 1}) - 1) == 0:
    raise AssertionError("nonzero locked product should change normalization")
checks.append("nonzero locked product changes the source normalization")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Matter Source Origin Gate 40: Locked Auxiliary Normalization Gate

## Purpose

This proof checks the case where an auxiliary interval channel is not
independent but is locked to the metric interval.

## Validated Checks

{validation_bullets}

## Setup

Suppose:

```text
zeta = lambda A
A_eff = A + alpha zeta
      = (1 + alpha lambda) A.
```

The matter action is:

```text
S_m = -M sqrt(A_eff).
```

Compared to the standard interval source coefficient, the variation is scaled
by:

```text
sqrt(1 + alpha lambda).
```

For weak `alpha lambda`:

```text
sqrt(1 + alpha lambda) = 1 + alpha lambda/2 + ...
```

## Gate Interpretation

Locking an auxiliary channel to the interval does not make it invisible. It
renormalizes the matter source coefficient unless:

```text
alpha lambda = 0.
```

Any nonzero locked auxiliary coupling must therefore be explicit in the source
normalization.
"""

out = Path(__file__).with_name("40_locked_auxiliary_normalization_gate.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Locked auxiliary normalization gate passed.")
print(f"Wrote {out.resolve()}")
