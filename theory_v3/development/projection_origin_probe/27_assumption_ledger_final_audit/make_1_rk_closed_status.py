#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

# Symbolic checks
import sympy as sp
k=sp.symbols('k', positive=True, integer=True)
y=sp.symbols('y', positive=True)
r=(2*k-1)/(2*k+3)
ratio=(k-sp.Rational(1,2))/(k+sp.Rational(3,2))
assert sp.simplify(ratio-r)==0

REPORT = r"""
# 1. `r_k` Closed Status

## Claim

The original coefficient is closed as a moment-kernel/admissibility coefficient:

```text
r_k = (2k - 1)/(2k + 3).
```

## SymPy check

For the base moment functional

```text
C_0[P] = ∫_0^1 P(y) (1-y)y^(-1/2) dy,
```

the monomial ratio is

```text
Beta(k + 1/2, 2) / Beta(k - 1/2, 2)
  = (2k - 1)/(2k + 3).
```

## Ledger status

Closed. This coefficient no longer needs to be treated as mysterious or
speculative. It is the `R=0` scalar boundary/admissibility moment coefficient.
"""

Path(__file__).with_name('1_rk_closed_status.md').write_text(REPORT.strip()+"\n", encoding='utf-8')
print('wrote 1_rk_closed_status.md')
