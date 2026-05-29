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

# Required status identities for the conclusion.
k, R = sp.symbols('k R', positive=True, integer=True)
r0 = (2*k-1)/(2*k+3)
rR = (2*k-1)/(2*k+2*R+3)
require_equal(rR.subs(R,0), r0, 'base class status')
require_equal((rR-r0).subs(R,0), 0, 'difference vanishes at base')

write_report('23_comparison_status.md', r'''
# 23. Comparison status

The status is:

```text
R=0 gives the projection-origin base ratio.
R≠0 gives a distinct contact/admissibility class.
```

The comparison with weak-field GR should therefore be made by reducing GR to
the same compactified scalar variables and reading off the effective `R`.

Interpretation: the boundary-reduction question is finite and concrete, but it
must be normalized carefully before claiming match or mismatch.
''')
print('wrote', '23_comparison_status.md')
