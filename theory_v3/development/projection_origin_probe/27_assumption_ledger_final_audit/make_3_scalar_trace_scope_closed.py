#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

# Symbolic checks
import sympy as sp
m=sp.symbols('m', integer=True, positive=True)
full=m*(m+1)/2
gap=sp.simplify(full-1)
assert gap.subs(m,3)==5
assert full.subs(m,3)==6

REPORT = r"""
# 3. Scalar Trace Scope Closed

## Claim

Scalar trace data is one channel; a symmetric boundary tensor has

```text
m(m+1)/2
```

components on an `m`-dimensional boundary.

For `m=3`, the full tensor has six components and the scalar trace leaves a
five-component traceless/shear gap.

## Ledger status

Closed. The scalar projection ladder cannot by itself reconstruct full tensor
boundary data.
"""

Path(__file__).with_name('3_scalar_trace_scope_closed.md').write_text(REPORT.strip()+"\n", encoding='utf-8')
print('wrote 3_scalar_trace_scope_closed.md')
