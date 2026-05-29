#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

# Symbolic checks
import sympy as sp
D=sp.symbols('D', integer=True, positive=True)
weyl=sp.simplify((D+2)*(D+1)*D*(D-3)/12)
assert weyl.subs(D,3)==0
assert weyl.subs(D,4)==10
pol=sp.simplify(D*(D-3)/2)
assert pol.subs(D,4)==2

REPORT = r"""
# 8. Weyl/TT Scope Status

## Claim

The Weyl/TT sector is outside the scalar trace ledger.

## SymPy check

The Weyl component count is

```text
(D+2)(D+1)D(D-3)/12,
```

which gives zero in `D=3` and ten in `D=4`. The massless spin-2 propagating
count

```text
D(D-3)/2
```

gives two in `D=4`.

## Ledger status

Closed as a counting result. The scalar ladder does not contain Weyl/TT data.
"""

Path(__file__).with_name('8_weyl_tt_scope_status.md').write_text(REPORT.strip()+"\n", encoding='utf-8')
print('wrote 8_weyl_tt_scope_status.md')
