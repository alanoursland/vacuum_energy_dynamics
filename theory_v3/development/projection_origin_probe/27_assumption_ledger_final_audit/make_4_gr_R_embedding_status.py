#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

# Symbolic checks
import sympy as sp
R,k=sp.symbols('R k', integer=True, nonnegative=True)
rR=(2*k-1)/(2*k+2*R+3)
r0=(2*k-1)/(2*k+3)
diff=sp.factor(rR-r0)
assert diff.subs(R,0)==0
assert sp.simplify(diff.subs({R:1,k:1}) - (sp.Rational(1,7)-sp.Rational(1,5)))==0

REPORT = r"""
# 4. GR `R` Embedding Status

## Claim

The projection contact class `R` is visible in the ladder coefficient, but weak
field scalar finite-flux data alone does not specify the projection embedding.

If a GR scalar ledger is embedded into the same `C_0` projection chart, then
`R_GR = 0`. A different contact class would produce a different coefficient,
for example:

```text
R = 0, k = 1 -> 1/5
R = 1, k = 1 -> 1/7
```

## Ledger status

Closed as a representation statement. Open as an ontology statement unless the
projection embedding is derived from the physical reduction.
"""

Path(__file__).with_name('4_gr_R_embedding_status.md').write_text(REPORT.strip()+"\n", encoding='utf-8')
print('wrote 4_gr_R_embedding_status.md')
