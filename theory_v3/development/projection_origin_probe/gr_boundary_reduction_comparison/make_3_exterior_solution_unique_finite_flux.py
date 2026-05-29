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

r, A, B = sp.symbols('r A B', positive=True)
Phi = A + B/r
lap = sp.simplify((1/r**2) * sp.diff(r**2 * sp.diff(Phi, r), r))
require_zero(lap, 'A+B/r is radial harmonic')
flux = sp.simplify(4*sp.pi*r**2*sp.diff(Phi, r))
require_zero(sp.diff(flux, r), 'A+B/r finite flux constant')

write_report('3_exterior_solution_unique_finite_flux.md', r'''
# 3. Exterior solution finite-flux class

The general exterior radial harmonic solution in three spatial dimensions is

```text
Φ(r) = A + B/r.
```

Validated checks:

```text
∇²(A+B/r) = 0,
d/dr [4πr² Φ'(r)] = 0.
```

Interpretation: once the weak-field scalar reduction is chosen, the boundary
condition class is the standard finite-flux radial harmonic class.
''')
print('wrote', '3_exterior_solution_unique_finite_flux.md')
