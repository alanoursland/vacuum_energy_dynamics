#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name('4_scalar_monopole_projection_gate.md')

def require_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label} != 0: {z}")


mu=sp.symbols('mu')
for ell in range(1,7):
    P=sp.legendre(ell, mu)
    avg=sp.integrate(P,(mu,-1,1))
    require_zero(avg, f'Legendre monopole avg ell={ell}')
P0=sp.legendre(0,mu)
val=sp.integrate(P0,(mu,-1,1))
require_zero(val-2,'P0 average')


md = f"""# 4. Scalar monopole projection gate

## Checked identities

The angular monopole projection was checked using Legendre polynomials:

```text
∫_{-1}^1 P_l(mu) dmu = 0 for l>0,
∫_{-1}^1 P_0(mu) dmu = 2.
```

## Conclusion

A scalar monopole boundary ledger keeps only `l=0` data and is blind to higher angular multipoles.
"""
TMP = OUT.with_suffix('.tmp')
TMP.write_text(md)
TMP.replace(OUT)
print(f"wrote {OUT.name}")
