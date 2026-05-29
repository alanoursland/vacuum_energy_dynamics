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

# Boundary action term gate

r, G, M, dPhi = sp.symbols('r G M dPhi', positive=True)
Phi = -G*M/r
boundary_variation = sp.simplify(r**2*sp.diff(Phi,r)*dPhi)
require_equal(boundary_variation, G*M*dPhi, 'finite boundary variation coefficient')


write_report('4_boundary_action_term_gate.md', r'''
# 4. Boundary action term gate

The radial scalar Dirichlet energy variation carries a boundary term of the
form

```text
r² Φ'(r) δΦ.
```

For the exterior weak-field monopole,

```text
r² Φ'(r) δΦ = GM δΦ.
```

This confirms that the boundary variation ledger is finite in the physical
scalar GR reduction.  It still does not determine the projection moment weight
or endpoint-contact ladder index.

''')
print('wrote 4_boundary_action_term_gate.md')
