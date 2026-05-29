
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "11_tt_polarization_not_scalar.md"

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

hp,hx=sp.symbols('hp hx')
H=sp.Matrix([[hp,hx,0],[hx,-hp,0],[0,0,0]])
require_zero(sp.trace(H),'TT transverse plane trace zero')
norm=sum(H[i,j]**2 for i in range(3) for j in range(3))
require_equal(norm, 2*hp**2+2*hx**2, 'TT carries two amplitudes')

write_md(r'''
# 11. TT polarization not scalar

A transverse-traceless plane-wave tensor can be represented by

```text
[[h_plus, h_cross, 0],
 [h_cross, -h_plus, 0],
 [0, 0, 0]].
```

It has zero trace but two nonzero polarizations. Scalar trace data cannot see it.
''')
