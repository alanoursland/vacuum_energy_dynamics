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

r, G, M, rho = sp.symbols('r G M rho', positive=True)
Phi = sp.Function('Phi')
laplacian_radial = (1/r**2) * sp.diff(r**2 * sp.diff(Phi(r), r), r)
# Normalized Newtonian/weak-field scalar sector.
poisson_rhs = 4*sp.pi*G*rho
# Check that the exterior monopole Phi=-GM/r is harmonic away from source.
Phi_ext = -G*M/r
lap_ext = sp.simplify((1/r**2) * sp.diff(r**2 * sp.diff(Phi_ext, r), r))
require_zero(lap_ext, 'exterior monopole is radial harmonic')

write_report('1_weak_field_poisson_normalization.md', r'''
# 1. Weak-field scalar Poisson normalization

This script records the normalized weak-field scalar ledger used for the
comparison:

```text
∇²Φ = 4πGρ.
```

It also checks that the exterior monopole potential

```text
Φ(r) = -GM/r
```

is harmonic away from the source.

Validated check:

```text
(1/r²) d/dr [r² d(-GM/r)/dr] = 0.
```

Interpretation: the comparison begins with the ordinary scalar/Newtonian sector
of weak-field GR, not with a novel boundary equation.
''')
print('wrote', '1_weak_field_poisson_normalization.md')
