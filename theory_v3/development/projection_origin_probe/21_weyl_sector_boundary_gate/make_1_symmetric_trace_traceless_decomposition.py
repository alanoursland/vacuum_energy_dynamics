#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name('1_symmetric_trace_traceless_decomposition.md')

def require_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label} != 0: {z}")


n=sp.symbols('n', integer=True, positive=True)
t=sp.symbols('t')
A=sp.diag(sp.symbols('a1'), sp.symbols('a2'), sp.symbols('a3'))
tr=sp.trace(A)
I=sp.eye(3)
T=A - tr/3*I
require_zero(sp.trace(T), 'trace of traceless part')
reconstructed=T + tr/3*I
require_zero((reconstructed-A)[0,0], 'reconstruct 00')
require_zero((reconstructed-A)[1,1], 'reconstruct 11')
require_zero((reconstructed-A)[2,2], 'reconstruct 22')


md = f"""# 1. Symmetric trace/traceless decomposition

## Checked identities

For a symmetric tensor `A`, the decomposition

```text
A = (Tr A / 3) I + (A - (Tr A / 3) I)
```

was checked. The second term has zero trace and reconstructs `A` only when it is retained.

## Conclusion

Scalar trace data keeps only `Tr A`; it erases the traceless tensor information.
"""
TMP = OUT.with_suffix('.tmp')
TMP.write_text(md)
TMP.replace(OUT)
print(f"wrote {OUT.name}")
