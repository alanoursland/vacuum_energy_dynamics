import os
os.chdir(os.path.dirname(__file__))

import sympy as sp
from pathlib import Path
k,R=sp.symbols('k R', positive=True, integer=True)
rR=(2*k-1)/(2*k+2*R+3)
r0=sp.simplify(rR.subs(R,0))
r1=sp.simplify(rR.subs(R,1))
diff=sp.simplify(r1-r0)
assert diff!=0
md=f"""# 7. Finite Flux Does Not Determine R

The endpoint-contact index `R` belongs to the compactified moment/test pairing,
not to finite scalar flux alone.

The ladder is

```text
r_(R,k) = (2k - 1)/(2k + 2R + 3).
```

The first two classes are

```text
R=0: {r0}
R=1: {r1}
```

with difference

```text
r_(1,k) - r_(0,k) = {diff}.
```

## Closed result

Finite Gauss flux fixes the physical scalar exterior class, but not the
projection embedding index `R` without specifying the moment pairing.
"""
Path('7_finite_flux_not_R_no_go.md').write_text(md)
