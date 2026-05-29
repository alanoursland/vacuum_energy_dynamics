
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "4_conformal_scalar_trace_only.md"

def require_zero(expr, label):
    val = sp.simplify(expr)
    if val != 0:
        raise AssertionError(f"{label} failed: {val}")

def require_equal(a,b,label):
    require_zero(sp.simplify(a-b), label)

def write_md(text):
    tmp = OUT.with_suffix(OUT.suffix + ".tmp")
    tmp.write_text(text.strip()+"\n")
    tmp.replace(OUT)

phi = sp.symbols('phi')
I=sp.eye(3)
h = 2*phi*I
tr = sp.trace(h)
traceless = h - tr/3*I
require_zero(sum(traceless[i,j]**2 for i in range(3) for j in range(3)), 'conformal scalar has zero traceless shear')

write_md(r'''
# 4. Conformal scalar trace-only gate

A conformal scalar spatial perturbation

```text
h_ij = 2 phi delta_ij
```

has nonzero trace but zero traceless shear:

```text
h_ij - (Tr h / 3) delta_ij = 0.
```

Thus a pure conformal scalar can encode isotropic expansion, but not shear.
''')
