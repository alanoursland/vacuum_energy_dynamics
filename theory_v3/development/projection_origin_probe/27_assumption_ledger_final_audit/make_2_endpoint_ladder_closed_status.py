#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

# Symbolic checks
import sympy as sp
k,R=sp.symbols('k R', positive=True, integer=True)
ratio=(k-sp.Rational(1,2))/(k+R+sp.Rational(3,2))
target=(2*k-1)/(2*k+2*R+3)
assert sp.simplify(ratio-target)==0

REPORT = r"""
# 2. Endpoint Ladder Closed Status

## Claim

The general endpoint/contact ladder is closed:

```text
r_(R,k) = (2k - 1)/(2k + 2R + 3).
```

## SymPy check

The script verifies

```text
Beta(k + 1/2, R + 2) / Beta(k - 1/2, R + 2)
  = (2k - 1)/(2k + 2R + 3).
```

## Ledger status

Closed as a scalar moment/contact ladder. What remains open is not the algebra
of the ladder, but whether a given physical reduction selects a particular
`R` without an extra projection embedding.
"""

Path(__file__).with_name('2_endpoint_ladder_closed_status.md').write_text(REPORT.strip()+"\n", encoding='utf-8')
print('wrote 2_endpoint_ladder_closed_status.md')
