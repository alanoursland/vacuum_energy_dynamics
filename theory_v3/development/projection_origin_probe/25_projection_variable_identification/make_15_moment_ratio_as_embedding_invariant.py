
import sympy as sp
from pathlib import Path

OUT = Path(__file__).with_name('15_moment_ratio_as_embedding_invariant.md')

def require_zero(expr):
    expr = sp.simplify(expr)
    if expr != 0:
        raise AssertionError(f'Expected zero, got {expr}')

k,c=sp.symbols('k c', positive=True, integer=True)
R=sp.symbols('R', nonnegative=True, integer=True)
M_k=sp.symbols('M_k', nonzero=True)
M_prev=sp.symbols('M_prev', nonzero=True)
require_zero((c*M_k)/(c*M_prev)-M_k/M_prev)

OUT.write_text('# Moment Ratio as Embedding Invariant\n\nWithin a fixed projection embedding, adjacent moment ratios are invariant under overall normalization and are the right way to identify the ladder.\n\nThus `r_k` is an invariant of the chosen projection chart, not of all equivalent physical coordinate descriptions.\n')
print('wrote', OUT.name)
