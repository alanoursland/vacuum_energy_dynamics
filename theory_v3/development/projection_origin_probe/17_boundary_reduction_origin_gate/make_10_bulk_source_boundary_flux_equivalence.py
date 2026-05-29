#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / '10_bulk_source_boundary_flux_equivalence.md'

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


r,R,rho,Omega=sp.symbols('r R rho Omega', positive=True)
# uniform source density in n=3 ball: M=4*pi*rho R^3/3. Use Omega=4pi symbolic.
M=Omega*rho*R**3/3
F=M/(Omega*R**2)
flux=Omega*R**2*F
require_equal(flux,M,'flux equals bulk source integral')
report=f"""# 10. Bulk-source boundary-flux equivalence

For a uniform source in a three-dimensional ball with solid-angle factor
`Omega`, the enclosed source is

```text
M = Omega rho R^3 / 3.
```

The boundary field

```text
F(R) = M/(Omega R^2)
```

has flux

```text
Omega R^2 F(R) = {sp.simplify(flux)}.
```

Conclusion: the boundary flux equals the bulk source ledger. The boundary is a
measurement/reduction surface for interior physics.
"""


write_report(report)
