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

# Scalar boundary cannot measure Weyl sector

m = sp.symbols('m', integer=True, positive=True)
tensor_components = m*(m+1)/2
scalar_components = 1
gap = sp.simplify(tensor_components - scalar_components)
require_equal(gap.subs(m,3), 5, '3-boundary scalar/tensor gap')


write_report('18_scalar_boundary_cannot_measure_weyl_sector.md', r'''
# 18. Scalar boundary cannot measure the Weyl/traceless sector

On a three-dimensional spatial boundary, a symmetric tensor has

```text
3(3+1)/2 = 6
```

components.  The scalar trace/monopole channel supplies only one.

Validated gap:

```text
6 - 1 = 5.
```

So the scalar GR boundary comparison cannot decide the traceless/Weyl/TT sector.
That sector requires directional/tensor boundary data.

''')
print('wrote 18_scalar_boundary_cannot_measure_weyl_sector.md')
