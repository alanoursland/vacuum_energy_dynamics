#!/usr/bin/env python3
"""
make_9_lorentzian_signature_selector_gate.py

Validate the one-time Lorentzian signature bookkeeping for the selected
three-space plus one-clock branch.

Output:
    9_lorentzian_signature_selector_gate.md
"""

from pathlib import Path
import sympy as sp


eta = sp.diag(-1, 1, 1, 1)
euclidean = sp.eye(4)

eta_det = sp.det(eta)
euclidean_det = sp.det(euclidean)

negative_count = sum(1 for value in eta.diagonal() if value < 0)
positive_count = sum(1 for value in eta.diagonal() if value > 0)


def require_zero(label, expr):
    result = sp.simplify(expr)
    if result != 0:
        raise AssertionError(f"{label} failed: {result}")


require_zero("Lorentzian determinant", eta_det + 1)
require_zero("Euclidean determinant", euclidean_det - 1)

if negative_count != 1 or positive_count != 3:
    raise AssertionError("Lorentzian signature count failed")

md = f"""# Vacuum Dimension Selector 9: Lorentzian Signature Selector Gate

## Purpose

This proof records the signature bookkeeping for the one-clock branch.

## Validated Checks

- `diag(-1,1,1,1)` has one negative and three positive directions: passed
- Lorentzian determinant is `-1`: passed
- Euclidean determinant is `+1`: passed

## Computation

```text
eta = diag(-1, 1, 1, 1)
det(eta) = {eta_det}
negative directions = {negative_count}
positive directions = {positive_count}
```

For comparison:

```text
det(I_4) = {euclidean_det}
```

## Interpretation

The selected branch is conditional: if the parent theory supplies one clock
channel and three flux-selected spatial dimensions, the natural metric
signature is Lorentzian. The proof does not derive the clock channel from the
projection hierarchy.
"""

out = Path(__file__).with_name("9_lorentzian_signature_selector_gate.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Lorentzian signature gate passed.")
print(f"Wrote {out.resolve()}")

