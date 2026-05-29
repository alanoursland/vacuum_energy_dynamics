
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "6_directional_probe_needed_for_shear.md"

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
e1=sp.Matrix([1,0,0]); e2=sp.Matrix([0,1,0]); ep=e1+e2
Q=lambda v: (v.T*H*v)[0]
h12=(Q(ep)-Q(e1)-Q(e2))/2
require_equal(h12, s, 'polarization recovers off diagonal shear')

write_md(r'''
# 6. Directional probe needed for shear

The shear component invisible to trace is recovered by directional probing:

```text
h_12 = (Q(e1+e2)-Q(e1)-Q(e2))/2.
```

For the off-diagonal shear witness, this gives

```text
h_12 = s.
```

This is why scalar boundary data must be supplemented by directional/tensor probes.
''')
