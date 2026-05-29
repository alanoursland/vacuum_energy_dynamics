#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / '14_dirichlet_neumann_boundary_ledger.md'

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


U,q,L=sp.symbols('U q L', positive=True)
# 1D interval harmonic u(x)=U*x/L has derivative U/L, flux q=U/L. Energy=1/2 int (U/L)^2 dx = U^2/(2L)= q^2 L/2
E_D=U**2/(2*L)
q_expr=U/L
E_N=q**2*L/2
E_sub=sp.simplify(E_N.subs(q,q_expr))
require_equal(E_sub,E_D,'Dirichlet-Neumann energy match')
report=f"""# 14. Dirichlet-Neumann boundary ledger

For the one-dimensional harmonic bridge with `u(0)=0`, `u(L)=U`,

```text
u(x)=Ux/L,   q = u' = U/L.
```

The Dirichlet energy is

```text
E_D = U^2/(2L).
```

The equivalent flux ledger energy is

```text
E_N = q^2 L/2.
```

Substituting `q=U/L` gives

```text
E_N = {E_sub} = E_D.
```

Conclusion: boundary value and boundary flux are dual ledgers for the same
bulk harmonic response.
"""


write_report(report)
