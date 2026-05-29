import os
os.chdir(os.path.dirname(__file__))

import sympy as sp
from pathlib import Path
mu,J,tau=sp.symbols('mu J tau', nonzero=True)
E=sp.Rational(1,2)*mu*tau**2-J*tau
stationary=sp.solve(sp.diff(E,tau),tau)[0]
assert stationary==J/mu
md=f"""# 10. Unrouted Torsion Source No-Go

A torsion source cannot be hidden while setting torsion to zero.

For the reduced quadratic model

```text
E(tau) = 1/2 mu tau^2 - J tau
```

stationarity gives

```text
tau = {stationary}.
```

## Closed result

Torsion-free closure requires the torsion source ledger to vanish or be routed.
Nonzero torsion source implies an explicit torsion branch.
"""
Path('10_torsion_unrouted_no_go.md').write_text(md)
