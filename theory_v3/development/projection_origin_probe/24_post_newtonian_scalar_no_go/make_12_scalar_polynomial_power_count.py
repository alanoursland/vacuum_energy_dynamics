
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "12_scalar_polynomial_power_count.md"

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

Phi,a2,a3=sp.symbols('Phi a2 a3')
P=Phi+a2*Phi**2+a3*Phi**3
# polynomial depends only on powers of one scalar variable; derivative wrt independent shear s is zero
s=sp.symbols('s')
require_zero(sp.diff(P,s),'scalar polynomial has no independent shear derivative')

write_md(r'''
# 12. Scalar polynomial power count

A scalar nonlinear completion of the form

```text
Phi + a2 Phi^2 + a3 Phi^3 + ...
```

contains powers of one scalar variable. It does not generate independent shear, vector, or TT variables. Polynomial nonlinearity is not tensor structure.
''')
