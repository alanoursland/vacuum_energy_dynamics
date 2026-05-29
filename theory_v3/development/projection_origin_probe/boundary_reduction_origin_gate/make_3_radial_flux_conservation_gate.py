#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / '3_radial_flux_conservation_gate.md'

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


r,n,Q,Omega=sp.symbols('r n Q Omega', positive=True)
F=Q/(Omega*r**(n-1))
flux=Omega*r**(n-1)*F
require_equal(flux,Q,'radial flux equals enclosed charge')
report=f"""# 3. Radial flux conservation gate

In `n` spatial dimensions, a radial inverse-area field

```text
F(r) = Q / (Omega_n r^(n-1))
```

has conserved enclosing flux

```text
Omega_n r^(n-1) F(r) = Q.
```

SymPy check:

```text
Omega*r^(n-1)*Q/(Omega*r^(n-1)) = {sp.simplify(flux)}
```

Conclusion: the boundary surface measures the conserved bulk/source ledger.
The charge is surface-invariant, but that does not make the surface the source.
"""


write_report(report)
