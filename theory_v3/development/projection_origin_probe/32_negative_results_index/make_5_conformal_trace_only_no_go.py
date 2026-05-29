import os
os.chdir(os.path.dirname(__file__))

import sympy as sp
from pathlib import Path
l1,l2,l3=sp.symbols('l1 l2 l3')
T=sp.diag(l1,l2,l3)
trace=sp.trace(T)
S=sp.diag(2,-1,-1)
assert sp.trace(S)==0
md=f"""# 5. Conformal Trace-Only Coupling No-Go

A conformal variation sees only the trace of stress.

For a stress matrix

```text
T = diag(l1, l2, l3), tr(T) = {trace}
```

A traceless witness

```text
S = diag(2, -1, -1)
```

has

```text
tr(S) = {sp.trace(S)}.
```

## Closed result

Trace-only/conformal response misses traceless stress and shear. Full metric
variation is needed for full stress coupling.
"""
Path('5_conformal_trace_only_no_go.md').write_text(md)
