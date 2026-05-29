#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / '17_source_crossing_flux_difference_gate.md'

def require_zero(expr, label):
    simplified = sp.simplify(expr)
    if simplified != 0:
        raise AssertionError(f"{label} expected 0, got {simplified}")
    return simplified

def require_equal(a, b, label):
    return require_zero(sp.simplify(a-b), label)

def write_report(text):
    tmp = OUT.with_suffix('.tmp')
    tmp.write_text(text)
    tmp.replace(OUT)


rho,Omega,r1,r2=sp.symbols('rho Omega r1 r2', positive=True)
Q1=Omega*rho*r1**3/3
Q2=Omega*rho*r2**3/3
diff=sp.simplify(Q2-Q1)
require_equal(diff,Omega*rho*(r2**3-r1**3)/3,'flux difference enclosed source')
report=f"""# 17. Source-crossing flux difference gate

For uniform source density, the flux difference between two enclosing spheres is
the source contained in the shell:

```text
Q(r2)-Q(r1) = {sp.sstr(diff)}.
```

Conclusion: boundary flux changes only when the boundary sweep crosses source
content. This keeps source ontology in the interior/source ledger, not in the
choice of boundary itself.
"""


write_report(report)
