from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent

def require_zero(expr, label):
    z = sp.simplify(sp.combsimp(expr))
    if z != 0:
        raise AssertionError(f"{label} failed: {z}")

def require_equal(a, b, label):
    require_zero(sp.simplify(a-b), label)

def write_report(name, text):
    path = ROOT / name
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(text, encoding='utf-8')
    tmp.replace(path)

r, G, M = sp.symbols('r G M', positive=True)
Phi = -G*M/r
flux = 4*sp.pi*r**2 * sp.diff(Phi, r)
require_equal(flux, 4*sp.pi*G*M, 'radial Gauss flux constant')
require_zero(sp.diff(flux, r), 'flux independent of radius')

write_report('2_radial_gauss_flux_ledger.md', r'''
# 2. Radial Gauss flux ledger

For the exterior weak-field potential

```text
Φ(r) = -GM/r,
```

the radial flux is

```text
4πr² Φ'(r) = 4πGM.
```

Validated checks:

```text
4πr² d(-GM/r)/dr = 4πGM,
d/dr [4πr² Φ'(r)] = 0.
```

Interpretation: the boundary ledger is the standard enclosing-surface charge
ledger. It is not distinctive to the projection ontology.
''')
print('wrote', '2_radial_gauss_flux_ledger.md')
