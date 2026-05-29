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

k = sp.symbols('k', positive=True, integer=True)
M = lambda j: sp.Rational(4,1)/((2*j+1)*(2*j+3))
rk = sp.simplify(M(k)/M(k-1))
expected = (2*k-1)/(2*k+3)
require_equal(rk, expected, 'r_k beta moment ratio')
# Kernel row y^k - r_k y^(k-1) has zero moment.
y = sp.symbols('y', positive=True)
# symbolic moment using closed form
kernel_moment = sp.simplify(M(k) - expected*M(k-1))
require_zero(kernel_moment, 'kernel row moment cancellation')

write_report('7_rk_moment_kernel_ratio.md', r'''
# 7. Base `r_k` moment-kernel ratio

Using the compactified beta moments,

```text
M_j = ∫₀¹ y^j (1-y)y^{-1/2} dy,
```

the moment-kernel coefficient is

```text
r_k = M_k/M_{k-1} = (2k-1)/(2k+3).
```

Therefore

```text
y^k - r_k y^{k-1}
```

has zero moment under the same functional.

Interpretation: the observed ratio is exactly the base compactified
moment-kernel coefficient.
''')
print('wrote', '7_rk_moment_kernel_ratio.md')
