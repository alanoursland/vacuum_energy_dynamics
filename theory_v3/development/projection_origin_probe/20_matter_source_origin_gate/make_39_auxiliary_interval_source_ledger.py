#!/usr/bin/env python3
"""
make_39_auxiliary_interval_source_ledger.py

Validate that an auxiliary field entering the matter interval becomes an
explicit matter-coupled field with its own source variation.

Output:
    39_auxiliary_interval_source_ledger.md
"""

from pathlib import Path
import sympy as sp


A, zeta, alpha, M, F_A, F_z = sp.symbols("A zeta alpha M F_A F_z", positive=True)


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

A_eff = A + alpha * zeta
E = F_A * A + F_z * zeta - M * sp.sqrt(A_eff)

dA = simplify_expr(sp.diff(E, A))
dz = simplify_expr(sp.diff(E, zeta))
require_zero("A source variation with auxiliary interval", dA - (F_A - M / (2 * sp.sqrt(A_eff))))
require_zero("zeta source variation with auxiliary interval", dz - (F_z - alpha * M / (2 * sp.sqrt(A_eff))))
checks.append("auxiliary interval coupling gives zeta an explicit matter source")

decoupled_dz = simplify_expr(dz.subs(alpha, 0))
require_zero("decoupled auxiliary source", decoupled_dz - F_z)
checks.append("alpha=0 removes matter source from the auxiliary field")

stationary_Fz = sp.solve([sp.Eq(dz, 0)], [F_z], dict=True)
if stationary_Fz != [{F_z: alpha * M / (2 * sp.sqrt(A + alpha * zeta))}]:
    raise AssertionError(f"unexpected F_z stationarity: {stationary_Fz}")
checks.append("if alpha is nonzero, zeta requires its own source ledger")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Matter Source Origin Gate 39: Auxiliary Interval Source Ledger

## Purpose

This proof checks what happens if an auxiliary residual/projection variable is
allowed to enter the matter interval.

## Validated Checks

{validation_bullets}

## Setup

Let:

```text
A_eff = A + alpha zeta
E = F_A A + F_z zeta - M sqrt(A_eff).
```

Then:

```text
dE/dA    = F_A - M/(2 sqrt(A_eff))
dE/dzeta = F_z - alpha M/(2 sqrt(A_eff)).
```

## Consequence

If:

```text
alpha != 0,
```

then `zeta` is explicitly matter-coupled. It is no longer hidden projection
bookkeeping or a neutral residual. It needs its own source ledger.

The decoupled route is:

```text
alpha = 0,
```

which removes the matter source term from the auxiliary variation.

## Gate Interpretation

An auxiliary field can be coupled to the interval only by promoting it to an
explicit matter-coupled physical field. Otherwise it must remain outside the
interval seen by matter.
"""

out = Path(__file__).with_name("39_auxiliary_interval_source_ledger.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Auxiliary interval source ledger passed.")
print(f"Wrote {out.resolve()}")
