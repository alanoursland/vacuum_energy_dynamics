#!/usr/bin/env python3
"""
make_11_cancellation_structural_vs_tuned.py

Validate the distinction between structural cancellation and parameter-tuned
cancellation in the torsion source ledger.

Output:
    11_cancellation_structural_vs_tuned.md
"""

from pathlib import Path
import sympy as sp


X, Y, a, b = sp.symbols("X Y a b")


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


structural_total = simplify_expr(X - X)
require_zero("structural cancellation", structural_total)

tuned_total = a * X + b * Y
tuned_solution = sp.solve([sp.Eq(tuned_total, 0)], [b], dict=True)
if tuned_solution != [{b: -X * a / Y}]:
    raise AssertionError(f"unexpected tuned cancellation solution: {tuned_solution}")

residual_after_structural_relation = simplify_expr(tuned_total.subs({Y: X, b: -a}))
require_zero("structural relation residual", residual_after_structural_relation)

sensitivity_to_Y = simplify_expr(sp.diff(tuned_total, Y))
require_zero("sensitivity to independent channel", sensitivity_to_Y - b)

md = f"""# Torsion Defect Exclusion 11: Cancellation Structural Vs Tuned

## Purpose

This proof separates two ways of obtaining `J_total = 0`.

Structural cancellation is an identity. Parameter-tuned cancellation is a
condition that must be justified by an additional mechanism.

## Validated Checks

- identity cancellation vanishes for all source values: passed
- independent-channel cancellation imposes a tuning condition: passed
- a structural relation converts tuned-looking cancellation into an identity: passed

## Structural Cancellation

For paired terms:

```text
J_total = X - X,
```

Sympy verifies:

```text
J_total = {structural_total}.
```

## Tuned Cancellation

For independent channels:

```text
J_total = a X + b Y,
```

the cancellation condition is:

```text
b = -a X/Y.
```

This is not an identity unless a separate structural relation is supplied.

With:

```text
Y = X
b = -a,
```

the residual becomes:

```text
{residual_after_structural_relation}.
```

## Interpretation

The torsion-free branch can be selected by structural cancellation, but not by
unexplained coefficient tuning. A cancellation theorem must identify the
relation that makes `J_total = 0` an identity.
"""

out = Path(__file__).with_name("11_cancellation_structural_vs_tuned.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Cancellation structural-vs-tuned gate passed.")
print(f"Wrote {out.resolve()}")

