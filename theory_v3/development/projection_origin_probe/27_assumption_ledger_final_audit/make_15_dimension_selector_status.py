#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

# Symbolic checks
import sympy as sp
D=sp.symbols('D')
sol=sp.solve(sp.Eq(D*(D-3)/2,2),D)
assert set(sol)=={-1,4}
# Lovelock p=2 topological in D=4
p=2
D4=4
assert D4==2*p

REPORT = r"""
# 15. Dimension Selector Status

## Claim

`D=4` is strongly selected as the minimal two-polarization Einstein/Lovelock
branch, not derived from pure logic alone.

## SymPy check

Solving

```text
D(D-3)/2 = 2
```

gives the positive solution `D=4`. Also, the Gauss-Bonnet Lovelock term is
topological in `D=4` because `D=2p` for `p=2`.

## Ledger status

Conditional selector. It depends on massless spin-2, Lorentzian/time-channel,
diffeomorphism, and Lovelock/action-class assumptions.
"""

Path(__file__).with_name('15_dimension_selector_status.md').write_text(REPORT.strip()+"\n", encoding='utf-8')
print('wrote 15_dimension_selector_status.md')
