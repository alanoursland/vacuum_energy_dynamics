#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

# Symbolic checks
import sympy as sp
K,J,mu=sp.symbols('K J mu', nonzero=True)
tau=J/(24*mu)
assert sp.simplify(tau.subs(J,0))==0
assert sp.diff(tau,J)==1/(24*mu)

REPORT = r"""
# 14. Torsion/Affine Status

## Claim

The torsion-free branch is selected only when torsion/spin/defect sources are
absent or routed away.

## SymPy check

In the reduced gate

```text
tau = J_total/(24 mu),
```

torsion vanishes when `J_total=0` and responds linearly when the source is
nonzero.

## Ledger status

Conditional. Levi-Civita is the minimal affine branch under source absence and
calibration coherence, not a proof that torsion is mathematically impossible.
"""

Path(__file__).with_name('14_torsion_affine_status.md').write_text(REPORT.strip()+"\n", encoding='utf-8')
print('wrote 14_torsion_affine_status.md')
