
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "13_tensor_invariant_independence_witness.md"

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

a,b=sp.symbols('a b')
H=sp.diag(a,b,-a-b) # traceless
tr=sp.trace(H)
I2=sp.trace(H*H)
require_zero(tr,'traceless diagonal tensor')
require_equal(I2, a**2+b**2+(a+b)**2, 'nonzero quadratic tensor invariant independent of trace')

write_md(r'''
# 13. Tensor invariant independence witness

A traceless tensor can have nonzero invariants:

```text
H = diag(a,b,-a-b),
Tr(H)=0,
Tr(H^2)=a^2+b^2+(a+b)^2.
```

Tensor nonlinearities can depend on data that scalar trace powers cannot encode.
''')
