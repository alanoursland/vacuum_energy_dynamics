#!/usr/bin/env python3
"""
make_20_universal_coupling_species_gate.py

Validate the species-universality gate for interval/clock-rate coupling.

Output:
    20_universal_coupling_species_gate.md
"""

from pathlib import Path
import sympy as sp


x = sp.symbols("x")
m1, m2, beta1, beta2 = sp.symbols("m1 m2 beta1 beta2", positive=True)
Phi = sp.Function("Phi")(x)


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

force1 = -beta1 * m1 * sp.diff(Phi, x)
force2 = -beta2 * m2 * sp.diff(Phi, x)
accel1 = simplify_expr(force1 / m1)
accel2 = simplify_expr(force2 / m2)
require_zero("mass cancellation in species 1 acceleration", accel1 + beta1 * sp.diff(Phi, x))
require_zero("mass cancellation in species 2 acceleration", accel2 + beta2 * sp.diff(Phi, x))
checks.append("inertial mass cancels from acceleration for clock-rate coupling")

universality_error = simplify_expr(accel1 - accel2)
poly = sp.Poly(universality_error, sp.diff(Phi, x))
coeff = poly.coeff_monomial(sp.diff(Phi, x))
solution = sp.solve([sp.Eq(coeff, 0)], [beta1], dict=True)
if solution != [{beta1: beta2}]:
    raise AssertionError(f"unexpected universality solution: {solution}")
checks.append("species-independent acceleration requires equal clock coupling")

require_zero("standard universal coupling", universality_error.subs({beta1: 1, beta2: 1}))
checks.append("beta1=beta2=1 gives universal Newtonian acceleration")

nonuniversal_witness = simplify_expr(universality_error.subs({beta1: 1, beta2: 2}))
if nonuniversal_witness == 0:
    raise AssertionError("different beta values should leave a nonzero universality witness")
checks.append("different beta values produce a nonzero universality violation")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Matter Source Origin Gate 20: Universal Coupling Species Gate

## Purpose

This proof records the species-universality condition for interval/clock-rate
coupling.

## Validated Checks

{validation_bullets}

## Setup

Allow a species-dependent clock coupling:

```text
U_i = beta_i m_i Phi.
```

Then:

```text
F_i = -beta_i m_i grad Phi
a_i = F_i/m_i = -beta_i grad Phi.
```

The inertial mass cancels, but species universality still requires:

```text
beta_1 = beta_2.
```

The standard metric/interval coupling has:

```text
beta_i = 1
```

for every matter species.

## Gate Interpretation

If the vacuum interval is the universal clock-rate structure, the coupling is
universal. If any species has an independent coefficient, the weak-limit
source law is no longer universal and the A-sector mass ledger is not closed.
"""

out = Path(__file__).with_name("20_universal_coupling_species_gate.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Universal coupling species gate passed.")
print(f"Wrote {out.resolve()}")
