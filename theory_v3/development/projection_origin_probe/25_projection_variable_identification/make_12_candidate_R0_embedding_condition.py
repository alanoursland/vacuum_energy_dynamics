
import sympy as sp
from pathlib import Path

OUT = Path(__file__).with_name('12_candidate_R0_embedding_condition.md')

def require_zero(expr):
    expr = sp.simplify(expr)
    if expr != 0:
        raise AssertionError(f'Expected zero, got {expr}')

k=sp.symbols('k', positive=True, integer=True)
r0=(2*k-1)/(2*k+3)
assert sp.simplify(r0.subs(k,1)-sp.Rational(1,5))==0

OUT.write_text('# Candidate R0 Embedding Condition\n\nIf the GR scalar boundary ledger is embedded using the same projection chart\n\n```text\ny=x^2,   C_0[P]=∫P(y)(1-y)y^(-1/2)dy,\n```\n\nthen by construction the GR ledger lands in the observed `R=0` projection class.\n\nThis is a valid compatibility embedding, not an invariant derivation of `R=0` from GR alone.\n')
print('wrote', OUT.name)
