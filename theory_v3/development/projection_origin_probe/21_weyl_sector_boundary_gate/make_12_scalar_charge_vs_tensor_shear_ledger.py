#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name('12_scalar_charge_vs_tensor_shear_ledger.md')

def require_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label} != 0: {z}")


M,s=sp.symbols('M s')
B=sp.diag(M/3+s, M/3-s, M/3)
trace=sp.trace(B)
require_zero(trace-M,'charge trace')
B0=B.subs(s,0)
diff=B-B0
require_zero(sp.trace(diff),'shear trace zero')
if sp.simplify(diff[0,0]) == 0:
    raise AssertionError('shear witness vanished')


md = f"""# 12. Scalar charge versus tensor shear ledger

## Checked identities

A boundary tensor can change by a shear witness

```text
diag(s, -s, 0)
```

without changing scalar trace/charge `M`.

## Conclusion

Scalar boundary charge is not enough to reconstruct boundary shear data.
"""
TMP = OUT.with_suffix('.tmp')
TMP.write_text(md)
TMP.replace(OUT)
print(f"wrote {OUT.name}")
