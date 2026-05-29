from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent

def require_zero(expr, label):
    z = sp.simplify(sp.factor(expr))
    if z != 0:
        raise AssertionError(f"{label} failed: {z}")

def require_equal(a, b, label):
    require_zero(sp.simplify(a-b), label)

def write_report(name, text):
    path = ROOT / name
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(text, encoding='utf-8')
    tmp.replace(path)

# Gauss flux fixed by GR scalar ledger

r, G, M = sp.symbols('r G M', positive=True)
Phi = -G*M/r
flux = sp.simplify(4*sp.pi*r**2*sp.diff(Phi,r))
require_equal(flux, 4*sp.pi*G*M, 'finite Gauss flux')
require_zero(sp.diff(flux,r), 'Gauss flux radius independence')


write_report('2_gauss_flux_fixed_by_gr.md', r'''
# 2. Gauss flux fixed by the GR scalar ledger

For the exterior scalar potential,

```text
4πr² Φ'(r) = 4πGM.
```

Validated checks:

```text
4πr² d(-GM/r)/dr = 4πGM,
d/dr [4πr² Φ'(r)] = 0.
```

The conserved scalar flux is fixed by weak-field GR/Newtonian gravity.  This is
the physical boundary ledger that any compatible projection representation must
reproduce.

''')
print('wrote 2_gauss_flux_fixed_by_gr.md')
