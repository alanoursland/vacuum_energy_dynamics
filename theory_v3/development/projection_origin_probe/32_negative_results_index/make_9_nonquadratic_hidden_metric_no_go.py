import os
os.chdir(os.path.dirname(__file__))

import sympy as sp
from pathlib import Path
x,y,eps=sp.symbols('x y eps')
Q=lambda a,b: a**2+b**2+eps*(a**2+b**2)**2
P=sp.expand(Q(x+y,0)+Q(x-y,0)-2*Q(x,0)-2*Q(y,0))
assert sp.factor(P)==12*eps*x**2*y**2
md=f"""# 9. Nonquadratic Hidden-Metric No-Go

A quartic residual violates the parallelogram identity.

For

```text
Q(v) = |v|^2 + eps |v|^4
```

SymPy verifies the parallelogram defect

```text
Q(x+y)+Q(x-y)-2Q(x)-2Q(y) = {sp.factor(P)}.
```

## Closed result

The nonquadratic residual must vanish (`eps=0`) to live inside an exact metric
branch. Otherwise it must be routed as Finsler/medium/constitutive structure.
"""
Path('9_nonquadratic_hidden_metric_no_go.md').write_text(md)
