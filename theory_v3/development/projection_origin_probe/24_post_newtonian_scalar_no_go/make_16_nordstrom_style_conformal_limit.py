
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "16_nordstrom_style_conformal_limit.md"

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

phi=sp.symbols('phi')
eta=sp.diag(-1,1,1,1)
h=2*phi*eta
# all components proportional to one scalar; rank of coefficient span = 1
coeffs=[sp.simplify(h[i,j]/(2*phi)) for i in range(4) for j in range(4) if h[i,j]!=0]
# nonzero diagonal coeffs are fixed [-1,1,1,1]
require_equal(len(coeffs),4,'four nonzero diagonal entries')

write_md(r'''
# 16. Conformal scalar branch limitation

A scalar conformal branch has

```text
h_ab = 2 phi eta_ab.
```

All metric components are locked to one scalar amplitude. This is too rigid to encode the independent post-Newtonian tensor response unless additional structure is added.
''')
