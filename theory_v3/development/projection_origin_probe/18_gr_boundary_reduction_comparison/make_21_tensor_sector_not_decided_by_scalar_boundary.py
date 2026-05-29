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

m = sp.symbols('m', integer=True, positive=True)
tensor_components = m*(m+1)/2
scalar_components = 1
gap = sp.simplify(tensor_components - scalar_components)
require_equal(gap.subs(m,3), 5, '3-boundary scalar/tensor rank gap')

write_report('21_tensor_sector_not_decided_by_scalar_boundary.md', r'''
# 21. Tensor sector not decided by scalar boundary

On an `m`-dimensional boundary, a symmetric tensor has

```text
m(m+1)/2
```

components, while the scalar trace ledger supplies one component. For `m=3`,
the rank gap is

```text
6 - 1 = 5.
```

Interpretation: matching scalar boundary conditions does not decide the full
traceless/Weyl/tensor sector. Any novelty or ontology work may live there.
''')
print('wrote', '21_tensor_sector_not_decided_by_scalar_boundary.md')
