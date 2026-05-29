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

k, c = sp.symbols('k c', positive=True)
M = lambda j: c*sp.Rational(4,1)/((2*j+1)*(2*j+3))
ratio = sp.simplify(M(k)/M(k-1))
expected = (2*k-1)/(2*k+3)
require_equal(ratio, expected, 'constant normalization cancels in r_k')

write_report('12_allowed_rescaling_preserves_kernel_ratio.md', r'''
# 12. Allowed normalization rescaling preserves `r_k`

If the moment functional is multiplied by an overall nonzero constant,

```text
M_j -> c M_j,
```

the ratio

```text
M_k/M_{k-1}
```

is unchanged.

Validated check:

```text
(cM_k)/(cM_{k-1}) = (2k-1)/(2k+3).
```

Interpretation: comparison with GR should not depend on irrelevant global
normalizations of the reduced action or moment functional.
''')
print('wrote', '12_allowed_rescaling_preserves_kernel_ratio.md')
