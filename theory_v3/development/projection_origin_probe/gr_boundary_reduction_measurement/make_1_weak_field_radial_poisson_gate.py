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

# Weak-field radial Poisson gate

r, G, M = sp.symbols('r G M', positive=True)
Phi = -G*M/r
lap = (1/r**2)*sp.diff(r**2*sp.diff(Phi,r),r)
require_zero(lap, 'exterior weak-field monopole is harmonic')


write_report('1_weak_field_radial_poisson_gate.md', r'''
# 1. Weak-field radial Poisson gate

The weak-field scalar sector of GR reduces, in the static slow-motion limit, to
the Newtonian Poisson ledger

```text
∇²Φ = 4πGρ.
```

Outside the source, the monopole solution

```text
Φ(r) = -GM/r
```

is radial harmonic.

Validated check:

```text
(1/r²) d/dr [r² d(-GM/r)/dr] = 0.
```

This fixes the physical exterior scalar equation.  It does not yet specify a
compactified projection moment weight.

''')
print('wrote 1_weak_field_radial_poisson_gate.md')
