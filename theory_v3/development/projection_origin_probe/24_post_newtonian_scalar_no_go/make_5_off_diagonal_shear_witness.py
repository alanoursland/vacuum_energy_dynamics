
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "5_off_diagonal_shear_witness.md"

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

s=sp.symbols('s')
H=sp.Matrix([[0,s,0],[s,0,0],[0,0,0]])
require_zero(sp.trace(H), 'off diagonal shear is trace-free')
norm=sum(H[i,j]**2 for i in range(3) for j in range(3))
require_equal(norm, 2*s**2, 'off diagonal shear nonzero norm')

write_md(r'''
# 5. Off-diagonal shear witness

The symmetric perturbation

```text
H = [[0,s,0],[s,0,0],[0,0,0]]
```

has zero trace but nonzero tensor content:

```text
Tr(H)=0,
||H||^2 = 2 s^2.
```

A scalar trace boundary ledger cannot reconstruct this component.
''')
