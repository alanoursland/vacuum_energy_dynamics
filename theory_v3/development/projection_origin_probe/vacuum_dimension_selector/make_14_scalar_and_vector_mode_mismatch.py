#!/usr/bin/env python3
"""
make_14_scalar_and_vector_mode_mismatch.py

Validate that scalar, vector, and symmetric tensor lifts are distinct field
types even when some degree counts coincide in D=4.

Output:
    14_scalar_and_vector_mode_mismatch.md
"""

from pathlib import Path
import sympy as sp


D = sp.symbols("D", integer=True, positive=True)
scalar_dof = sp.Integer(1)
vector_dof = D - 2
spin2_dof = sp.simplify(D * (D - 3) / 2)

rank_scalar = sp.Integer(0)
rank_vector = sp.Integer(1)
rank_tensor = sp.Integer(2)


def require_zero(label, expr):
    result = sp.simplify(expr)
    if result != 0:
        raise AssertionError(f"{label} failed: {result}")


require_zero("D=4 vector dof", vector_dof.subs(D, 4) - 2)
require_zero("D=4 spin2 dof", spin2_dof.subs(D, 4) - 2)
require_zero("scalar rank mismatch", rank_tensor - rank_scalar - 2)
require_zero("vector rank mismatch", rank_tensor - rank_vector - 1)

md = f"""# Vacuum Dimension Selector 14: Scalar And Vector Mode Mismatch

## Purpose

This proof prevents a common counting mistake: matching a number of degrees of
freedom is not the same as matching the field type.

## Validated Checks

- in `D=4`, a massless vector and a massless spin-2 field both have two
  propagating degrees of freedom: passed
- scalar, vector, and symmetric tensor ranks are distinct: passed

## Computation

```text
N_scalar = {scalar_dof}
N_vector(D) = D - 2
N_spin2(D) = {spin2_dof}
N_vector(4) = {vector_dof.subs(D, 4)}
N_spin2(4) = {spin2_dof.subs(D, 4)}
```

But the field ranks differ:

```text
scalar rank = {rank_scalar}
vector rank = {rank_vector}
symmetric metric perturbation rank = {rank_tensor}
```

## Interpretation

The weak-field GR lift needs a symmetric rank-2 field, not merely any field with
two modes. Vector and scalar branches remain separate candidate branches unless
an independent argument excludes or embeds them.
"""

out = Path(__file__).with_name("14_scalar_and_vector_mode_mismatch.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Scalar/vector/tensor mismatch check passed.")
print(f"Wrote {out.resolve()}")

