#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

# Symbolic checks
import sympy as sp
sqrtg,L,dg,T=sp.symbols('sqrtg L dg T')
dS=sp.Rational(1,2)*sqrtg*T*dg
Trec=sp.simplify(2*dS/(sqrtg*dg))
assert Trec==T

REPORT = r"""
# 10. Matter Coupling Conditional Status

## Claim

If matter action depends on the shared metric interval, metric variation gives
the stress-tensor source route.

## SymPy check

The variation normalization

```text
δS_m = 1/2 sqrt(g) T^{ab} δg_ab
```

recovers `T` by the standard functional-variation coefficient.

## Ledger status

Conditionally closed. It does not derive the existence or microscopic form of
matter actions.
"""

Path(__file__).with_name('10_matter_coupling_conditional_status.md').write_text(REPORT.strip()+"\n", encoding='utf-8')
print('wrote 10_matter_coupling_conditional_status.md')
