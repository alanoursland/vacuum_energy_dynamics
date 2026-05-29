
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "7_ppn_metric_two_potential_form.md"

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

Phi, gamma = sp.symbols('Phi gamma')
g00_coeff = -2 # g00 = -1 + 2 Phi convention coefficient relative to Phi can vary; use magnitude relation
spatial_coeff = 2*gamma
# gamma is independent unless constrained.
require_zero(sp.diff(g00_coeff, gamma), 'g00 coefficient independent of gamma')
require_equal(sp.diff(spatial_coeff,gamma), 2, 'spatial coefficient depends on gamma')

write_md(r'''
# 7. PPN metric two-potential form

The standard weak static isotropic metric uses independent temporal and spatial response data:

```text
g_00 = -1 + 2 Phi + ...
g_ij = (1 + 2 gamma Phi + ...) delta_ij.
```

The parameter `gamma` measures the spatial curvature response per unit Newtonian potential. A Newtonian scalar potential alone does not fix `gamma` without an additional metric-response rule.
''')
