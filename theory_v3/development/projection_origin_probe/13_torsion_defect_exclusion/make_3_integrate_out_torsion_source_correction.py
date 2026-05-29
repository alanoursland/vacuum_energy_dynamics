#!/usr/bin/env python3
"""
make_3_integrate_out_torsion_source_correction.py

Validate that a nonzero torsion source produces a reduced correction after
integrating out torsion.

Output:
    3_integrate_out_torsion_source_correction.md
"""

from pathlib import Path
import sympy as sp


tau, mu, J_total = sp.symbols("tau mu J_total")


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


energy = 12 * mu * tau**2 - J_total * tau
stationary_tau = J_total / (24 * mu)
reduced_energy = simplify_expr(energy.subs(tau, stationary_tau))
no_source_energy = simplify_expr(energy.subs({tau: 0, J_total: 0}))

require_zero("reduced energy", reduced_energy + J_total**2 / (48 * mu))
require_zero("no-source energy", no_source_energy)

source_derivative = simplify_expr(sp.diff(reduced_energy, J_total))
require_zero("source derivative", source_derivative + J_total / (24 * mu))

md = f"""# Torsion Defect Exclusion 3: Integrating Out Torsion Source Correction

## Purpose

This proof shows what happens if a torsion source survives.

The result is not pure Einstein-Hilbert. The torsion sector leaves a reduced
source correction.

## Validated Checks

- stationary torsion is substituted into the torsion energy: passed
- reduced energy is `-J_total^2/(48 mu)`: passed
- no-source branch has zero reduced torsion correction: passed
- nonzero source changes the reduced action: passed

## Computation

Use:

```text
E_T = 12 mu tau^2 - J_total tau.
```

At:

```text
tau = J_total/(24 mu),
```

Sympy gives:

```text
E_reduced = {reduced_energy}.
```

When:

```text
J_total = 0,
tau = 0,
```

the torsion correction is:

```text
{no_source_energy}.
```

## Interpretation

If a torsion source remains, torsion is not a harmless eliminated variable. It
produces a real source-dependent correction. The pure EH branch is recovered
only on the no-source branch or under a structural cancellation.
"""

out = Path(__file__).with_name("3_integrate_out_torsion_source_correction.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Integrate-out torsion source correction passed.")
print(f"Wrote {out.resolve()}")

