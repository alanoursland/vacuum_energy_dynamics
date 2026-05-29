
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "1_newtonian_scalar_success_gate.md"

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

r, G, M = sp.symbols('r G M', positive=True)
Phi = -G*M/r
lap_radial = (1/r**2)*sp.diff(r**2*sp.diff(Phi,r),r)
require_zero(lap_radial, 'exterior 1/r is harmonic away from source')
flux = 4*sp.pi*r**2*sp.diff(Phi,r)
require_equal(flux, 4*sp.pi*G*M, 'finite conserved radial flux')

write_md(r'''
# 1. Newtonian scalar success gate

A scalar potential can reproduce the Newtonian exterior sector.

For

```text
Phi(r) = -G M / r,
```

the radial Laplacian vanishes away from the source:

```text
(1/r^2) d/dr (r^2 Phi') = 0.
```

The radial flux is conserved:

```text
4 pi r^2 Phi' = 4 pi G M.
```

This group does not deny the scalar success. The no-go starts only when one asks the scalar branch to reproduce the full post-Newtonian tensor structure.
''')
