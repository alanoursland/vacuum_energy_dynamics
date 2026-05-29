#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name('11_poisson_trace_tidal_split.md')

def require_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label} != 0: {z}")


phixx,phiyy,phizz=sp.symbols('phixx phiyy phizz')
H=sp.diag(phixx,phiyy,phizz)
lap=sp.trace(H)
T=H-lap/3*sp.eye(3)
require_zero(sp.trace(T),'Hessian traceless split')
rec=T+lap/3*sp.eye(3)
for i in range(3): require_zero(rec[i,i]-H[i,i],f'reconstruct {i}')


md = f"""# 11. Poisson trace versus tidal traceless split

## Checked identities

The Newtonian Hessian decomposes as

```text
∂i∂j Phi = (Delta Phi / 3) delta_ij + traceless tidal part.
```

The scalar Poisson equation fixes `Delta Phi`, not the traceless Hessian.

## Conclusion

The source/trace equation and the tidal/shear field are different pieces of the gravitational data.
"""
TMP = OUT.with_suffix('.tmp')
TMP.write_text(md)
TMP.replace(OUT)
print(f"wrote {OUT.name}")
