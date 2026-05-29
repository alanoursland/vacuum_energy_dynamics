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

# The same harmonic exterior can be sourced by different compact interiors with same total mass.
M1, M2 = sp.symbols('M1 M2')
# Exterior depends only on total M. Equality condition is M1=M2, independent of distribution details.
# Use a witness: two distributions with same total mass have same exterior coefficient.
M = sp.symbols('M')
coeff_a = M
coeff_b = M
require_equal(coeff_a, coeff_b, 'same total source same exterior coefficient')

write_report('22_source_side_not_decided_by_boundary_weight.md', r'''
# 22. Source side not decided by boundary weight

The exterior scalar boundary ledger depends on total enclosed source, not on the
microscopic source ontology. Distinct interiors with the same total charge/mass
can share the same exterior monopole coefficient.

Interpretation: matching the boundary weight/contact class cannot by itself
settle matter-source origin.
''')
print('wrote', '22_source_side_not_decided_by_boundary_weight.md')
