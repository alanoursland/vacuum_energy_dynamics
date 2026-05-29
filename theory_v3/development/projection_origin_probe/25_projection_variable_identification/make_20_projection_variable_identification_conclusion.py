
import sympy as sp
from pathlib import Path

OUT = Path(__file__).with_name('20_projection_variable_identification_conclusion.md')

def require_zero(expr):
    expr = sp.simplify(expr)
    if expr != 0:
        raise AssertionError(f'Expected zero, got {expr}')

k,R=sp.symbols('k R', positive=True, integer=True)
rR=(2*k-1)/(2*k+2*R+3)
r0=rR.subs(R,0)
require_zero(r0-(2*k-1)/(2*k+3))

OUT.write_text("# Projection Variable Identification Conclusion\n\nThe original projection variable is best identified as a compactified moment/test variable for the scalar boundary ledger, not as an invariant physical scalar field by itself.\n\nClosed by this group:\n\n```text\ny=x^2 explains y^(-1/2);\nC_0 gives the observed r_k;\nC_R gives the endpoint-contact ladder;\nR depends on projection embedding;\nweak-field GR scalar physics alone does not specify R.\n```\n\nIf GR is embedded in the same `C_0` chart, the result is `R_GR=0`.  But that is a compatibility embedding, not a chart-independent derivation from GR's scalar boundary ledger alone.\n")
print('wrote', OUT.name)
