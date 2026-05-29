
import sympy as sp
from pathlib import Path

OUT = Path(__file__).with_name('11_poisson_equation_not_projection_embedding.md')

def require_zero(expr):
    expr = sp.simplify(expr)
    if expr != 0:
        raise AssertionError(f'Expected zero, got {expr}')

r,A=sp.symbols('r A', positive=True)
Phi=A/r
lap=sp.simplify((1/r**2)*sp.diff(r**2*sp.diff(Phi,r),r))
require_zero(lap)

OUT.write_text('# Poisson Equation Does Not Fix Projection Embedding\n\nThe radial Poisson equation fixes the physical exterior solution and flux ledger.\nIt does not uniquely specify which polynomial test space or compactified moment pairing should be used to represent that ledger.\n\nThis is why the projection variable identification is a separate bridge.\n')
print('wrote', OUT.name)
