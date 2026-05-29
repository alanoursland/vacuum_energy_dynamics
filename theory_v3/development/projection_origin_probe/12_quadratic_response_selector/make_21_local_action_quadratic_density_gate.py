#!/usr/bin/env python3
"""
Validate that local quadratic strain density assumes a fixed quadratic metric branch.

Output:
    21_local_action_quadratic_density_gate.md
"""
from pathlib import Path
import sympy as sp

s11,s12,s22,lam,mu,eps = sp.symbols('s11 s12 s22 lam mu eps')
tr = s11 + s22
norm = s11**2 + 2*s12**2 + s22**2
E2 = sp.Rational(1,2)*lam*tr**2 + mu*norm
vars = (s11,s12,s22)
H2 = sp.hessian(E2, vars)
# Add a quartic correction and show Hessian now depends on strain.
E4 = E2 + eps*tr**4
H4 = sp.hessian(E4, vars)
drift = sp.simplify(H4 - H4.subs({s11:0,s12:0,s22:0}))
if drift == sp.zeros(3):
    raise AssertionError('quartic action Hessian drift unexpectedly vanished')
if any(entry.has(s11,s12,s22) for entry in H2):
    raise AssertionError('quadratic strain Hessian should be constant in strain variables')

md = f"""# Quadratic Response Selector 21: Local Action Quadratic Density Gate

## Purpose

This proof records that the standard local quadratic strain-density branch
assumes a fixed quadratic response structure.

## Computation

For the quadratic density

```text
E2 = 1/2 lambda tr(s)^2 + mu ||s||^2,
```

SymPy computes a strain-independent Hessian:

```text
Hessian(E2) = {sp.sstr(H2)}
```

After adding a quartic correction `eps tr(s)^4`, the Hessian drift is:

```text
{sp.sstr(drift)}
```

## Interpretation

A local quadratic action density belongs to the metric/Hessian branch. Higher
strain response must be separately justified, suppressed, or routed.
"""

out = Path(__file__).with_name('21_local_action_quadratic_density_gate.md')
tmp = out.with_suffix(out.suffix + '.tmp')
tmp.write_text(md, encoding='utf-8')
tmp.replace(out)
print('Local action quadratic density gate passed.')
print(f'Wrote {out.resolve()}')
