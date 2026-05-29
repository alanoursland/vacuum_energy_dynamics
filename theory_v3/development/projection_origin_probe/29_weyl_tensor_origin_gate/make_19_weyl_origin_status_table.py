#!/usr/bin/env python3
from pathlib import Path
import sympy as sp
OUT = Path(__file__).with_name('19_weyl_origin_status_table.md')
def require_zero(expr, name='expr'):
    if sp.simplify(expr) != 0:
        raise AssertionError(f"{name} not zero: {sp.simplify(expr)}")
def require(cond, name='condition'):
    if not bool(cond):
        raise AssertionError(f"failed: {name}")
def write_md(text):
    tmp = OUT.with_suffix('.tmp')
    tmp.write_text(text.strip() + "\n", encoding='utf-8')
    tmp.replace(OUT)

md = """# 19. Weyl origin status table

| Claim | Status |
|---|---|
| Scalar trace data sees only monopole/trace sector | Closed |
| Directional quadratic probes recover local traceless/shear data | Closed |
| Vacuum trace can vanish while tidal trace-free data remains | Closed by witness |
| TT witnesses are trace-free and non-scalar | Closed by witness |
| Local Weyl dynamics follows from directional probes alone | Not closed |
| Hyperbolic propagation / constraint closure | Imported from later geometry |
| Radiative boundary phase space | Requires symplectic/news data |

Conclusion:

```text
directional probes solve the local tensor-data gap;
transport/symplectic closure solves the dynamical Weyl gap.
```
"""

write_md(md)
