
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "3_symmetric_metric_component_gap.md"

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

m=sp.symbols('m', integer=True, positive=True)
components = m*(m+1)/2
trace = sp.Integer(1)
gap = components-trace
require_equal(gap.subs(m,3), 5, '3D symmetric spatial metric has five non-trace components')

write_md(r'''
# 3. Symmetric metric component gap

A symmetric spatial metric perturbation in `m` dimensions has

```text
m(m+1)/2
```

components. A scalar trace channel supplies one component.

For `m = 3`, the missing traceless/shear sector has

```text
3(4)/2 - 1 = 5
```

components.
''')
