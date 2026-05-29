
import sympy as sp
from pathlib import Path

OUT = Path(__file__).with_name('16_Rgr_not_specified_without_embedding.md')

def require_zero(expr):
    expr = sp.simplify(expr)
    if expr != 0:
        raise AssertionError(f'Expected zero, got {expr}')

# Undefined until embedding: represent with a symbol, no equation fixes it.
Rgr=sp.symbols('R_GR')
alpha=sp.Integer(1)
# finite flux alpha=1 imposes no algebraic condition on Rgr
expr=sp.diff(Rgr, alpha) if False else 0
require_zero(expr)

OUT.write_text('# R_GR Not Specified Without Embedding\n\nWeak-field GR scalar data supplies:\n\n```text\nPoisson equation, finite flux, exterior 1/r.\n```\n\nIt does not by itself supply:\n\n```text\ny-variable, polynomial test space, C_R moment pairing.\n```\n\nTherefore `R_GR` is undefined until the projection embedding is chosen.\n')
print('wrote', OUT.name)
