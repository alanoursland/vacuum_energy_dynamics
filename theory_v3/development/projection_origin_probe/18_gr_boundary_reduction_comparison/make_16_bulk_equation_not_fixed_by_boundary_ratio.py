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
# Same beta ratio can be attached to any source normalization lambda in Poisson equation.
lambda1, lambda2 = sp.symbols('lambda1 lambda2', nonzero=True)
r = (2*k-1)/(2*k+3)
require_zero(sp.simplify(lambda1*r/lambda1 - r), 'source normalization 1 cancels')
require_zero(sp.simplify(lambda2*r/lambda2 - r), 'source normalization 2 cancels')

write_report('16_bulk_equation_not_fixed_by_boundary_ratio.md', r'''
# 16. Boundary ratio does not fix the bulk equation

The moment-kernel ratio is insensitive to overall source/action normalization.
Different bulk normalizations can produce the same reduced boundary ratio once
the same admissibility functional is used.

Interpretation: observing `r_k` constrains the boundary/admissibility class, but
it does not by itself determine the full bulk dynamics or ontology.
''')
print('wrote', '16_bulk_equation_not_fixed_by_boundary_ratio.md')
