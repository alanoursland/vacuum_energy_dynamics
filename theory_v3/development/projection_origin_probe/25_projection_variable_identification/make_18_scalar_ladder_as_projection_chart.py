
import sympy as sp
from pathlib import Path

OUT = Path(__file__).with_name('18_scalar_ladder_as_projection_chart.md')

def require_zero(expr):
    expr = sp.simplify(expr)
    if expr != 0:
        raise AssertionError(f'Expected zero, got {expr}')

k=sp.symbols('k', positive=True, integer=True)
chart_ratio=(2*k-1)/(2*k+3)
assert sp.simplify(chart_ratio.subs(k,1)-sp.Rational(1,5))==0

OUT.write_text("# Scalar Ladder as Projection Chart\n\nThe scalar ladder should be read as a compactified projection chart for a scalar boundary/admissibility problem.\n\nIt is compatible with weak-field GR's scalar ledger when the same chart is chosen, but the chart itself is not forced by the scalar ledger alone.\n")
print('wrote', OUT.name)
