#!/usr/bin/env python3
"""
make_27_hidden_source_failure_witness.py

Validate that any hidden nonzero torsion source makes tau = 0 nonstationary.

Output:
    27_hidden_source_failure_witness.md
"""

from pathlib import Path
import sympy as sp


tau, mu, J_hidden = sp.symbols("tau mu J_hidden")


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


energy = 12 * mu * tau**2 - J_hidden * tau
variation = simplify_expr(sp.diff(energy, tau))
residual_at_zero = simplify_expr(variation.subs(tau, 0))
stationary_tau = sp.solve([sp.Eq(variation, 0)], [tau], dict=True)
hidden_source_condition = sp.solve([sp.Eq(residual_at_zero, 0)], [J_hidden], dict=True)

require_zero("variation", variation - (24 * mu * tau - J_hidden))
require_zero("residual at zero", residual_at_zero + J_hidden)
if stationary_tau != [{tau: J_hidden / (24 * mu)}]:
    raise AssertionError(f"unexpected stationary torsion: {stationary_tau}")
if hidden_source_condition != [{J_hidden: 0}]:
    raise AssertionError(f"unexpected hidden source condition: {hidden_source_condition}")

md = f"""# Torsion Defect Exclusion 27: Hidden Source Failure Witness

## Purpose

This proof records the failure mode the folder is designed to block.

Any hidden nonzero torsion source makes the torsion-free branch nonstationary.

## Validated Checks

- hidden-source variation is `24 mu tau - J_hidden`: passed
- residual at `tau = 0` is `-J_hidden`: passed
- stationarity at `tau = 0` requires `J_hidden = 0`: passed
- actual stationary torsion is shifted by the hidden source: passed

## Computation

Use:

```text
E_T = 12 mu tau^2 - J_hidden tau.
```

Then:

```text
dE_T/dtau = {variation}.
```

At:

```text
tau = 0,
```

the residual is:

```text
{residual_at_zero}.
```

The stationary torsion is:

```text
tau = J_hidden/(24 mu).
```

## Interpretation

A hidden torsion source is incompatible with claiming the pure EH branch. It
must be shown absent, structurally canceled, or routed into a torsion-extended
field branch.
"""

out = Path(__file__).with_name("27_hidden_source_failure_witness.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Hidden source failure witness passed.")
print(f"Wrote {out.resolve()}")

