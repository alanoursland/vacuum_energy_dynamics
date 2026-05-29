#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name('2_trace_projection_kernel_dimension.md')

def require_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label} != 0: {z}")


n=sp.symbols('n', integer=True, positive=True)
sym_dim=n*(n+1)/2
trace_dim=1
kernel_dim=sp.simplify(sym_dim-trace_dim)
expected=(n*(n+1)-2)/2
require_zero(kernel_dim-expected, 'trace kernel dimension')
val3=kernel_dim.subs(n,3)
require_zero(val3-5, '3D traceless symmetric dimension')


md = f"""# 2. Trace projection kernel dimension

## Checked identities

The symmetric rank-2 dimension in `n` dimensions is

```text
n(n+1)/2.
```

The scalar trace channel has dimension `1`, so the trace-blind kernel has dimension

```text
n(n+1)/2 - 1.
```

For `n=3`, this is `5`.

## Conclusion

A scalar boundary ledger misses five independent traceless/shear components on a three-dimensional spatial slice.
"""
TMP = OUT.with_suffix('.tmp')
TMP.write_text(md)
TMP.replace(OUT)
print(f"wrote {OUT.name}")
