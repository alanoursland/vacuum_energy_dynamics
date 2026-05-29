#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

# Symbolic checks
import sympy as sp
r,Lambda,M=sp.symbols('r Lambda M', positive=True)
Phi=-M/r-Lambda*r**2/6
F=-sp.diff(Phi,r)
flux=sp.expand(r**2*F)
assert sp.expand(flux - (-M + Lambda*r**3/3))==0

REPORT = r"""
# 16. Lambda Branch Status

## Claim

`Lambda=0` is selected by asymptotically flat finite-flux normalization; nonzero
`Lambda` is an allowed vacuum-baseline branch that changes the asymptotic
class.

## SymPy check

For

```text
Phi = -M/r - Lambda r^2/6,
```

the radial flux ledger contains a growing `Lambda r^3` contribution.

## Ledger status

Conditional branch. Zero Lambda follows from asymptotically flat finite-flux
choice, not from the scalar ladder alone.
"""

Path(__file__).with_name('16_lambda_branch_status.md').write_text(REPORT.strip()+"\n", encoding='utf-8')
print('wrote 16_lambda_branch_status.md')
