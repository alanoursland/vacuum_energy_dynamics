
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "15_anisotropic_stress_blindness.md"

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

p1,p2,p3=sp.symbols('p1 p2 p3')
T=sp.diag(p1,p2,p3)
trace=p1+p2+p3
S=T-trace/3*sp.eye(3)
# choose p1=s,p2=-s,p3=0 => trace zero but nonzero anisotropic stress
s=sp.symbols('s')
Ssub=sp.simplify(S.subs({p1:s,p2:-s,p3:0}))
norm=sum(Ssub[i,j]**2 for i in range(3) for j in range(3))
require_equal(norm, 2*s**2, 'trace-free anisotropic stress nonzero')

write_md(r'''
# 15. Anisotropic stress blindness

Anisotropic stress can be trace-free and still nonzero. For

```text
p1=s, p2=-s, p3=0,
```

the trace vanishes but the anisotropic stress norm is

```text
2 s^2.
```

Scalar trace coupling cannot detect this source sector.
''')
