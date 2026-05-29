#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name('13_directional_probe_detects_shear.md')

def require_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label} != 0: {z}")


s=sp.symbols('s')
H=sp.diag(s,-s,0)
e1=sp.Matrix([1,0,0]); e2=sp.Matrix([0,1,0]); e3=sp.Matrix([0,0,1])
Q1=(e1.T*H*e1)[0]
Q2=(e2.T*H*e2)[0]
Q3=(e3.T*H*e3)[0]
require_zero(sp.trace(H),'shear trace')
require_zero(Q1-Q2-2*s,'directional shear contrast')
require_zero(Q1+Q2+Q3,'trace average zero')


md = f"""# 13. Directional probes detect shear

## Checked identities

For `H=diag(s,-s,0)`, the scalar trace is zero but directional probes satisfy

```text
Q(e1)-Q(e2)=2s.
```

## Conclusion

Directional interval probes see shear that scalar trace ledgers erase.
"""
TMP = OUT.with_suffix('.tmp')
TMP.write_text(md)
TMP.replace(OUT)
print(f"wrote {OUT.name}")
