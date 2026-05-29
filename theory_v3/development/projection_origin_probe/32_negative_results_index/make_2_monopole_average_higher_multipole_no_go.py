import os
os.chdir(os.path.dirname(__file__))

import sympy as sp
from pathlib import Path
mu=sp.symbols('mu')
P2=sp.legendre(2,mu)
P3=sp.legendre(3,mu)
I2=sp.integrate(P2,(mu,-1,1))
I3=sp.integrate(P3,(mu,-1,1))
assert sp.simplify(I2)==0 and sp.simplify(I3)==0
md=f"""# 2. Monopole Average / Higher Multipole No-Go

Scalar monopole averaging cannot recover higher angular multipoles.

SymPy verifies

```text
∫_-1^1 P_2(mu) dmu = {I2}
∫_-1^1 P_3(mu) dmu = {I3}
```

A scalar monopole ledger can record total charge/flux but not angular structure.

## Closed result

Higher multipoles can be nonzero locally while contributing zero monopole
average. Scalar monopole data is not angular boundary data.
"""
Path('2_monopole_average_higher_multipole_no_go.md').write_text(md)
