from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name(Path(__file__).name.replace('make_', '').replace('.py', '.md'))

def require_zero(expr, label):
    simplified = sp.simplify(expr)
    if simplified != 0:
        raise AssertionError(f"{label} failed: {simplified}")

def write_md(text):
    tmp = OUT.with_suffix('.tmp')
    tmp.write_text(text.strip() + "\n", encoding='utf-8')
    tmp.replace(OUT)

a,b,c = sp.symbols('a b c')
H = sp.Matrix([[a,b],[b,c]])
trace_projection = sp.trace(H)/2
require_zero(trace_projection - (a+c)/2, '2D trace projection')
S = sp.Matrix([[a,b],[b,-a]])
require_zero(sp.trace(S), 'traceless shear has zero scalar trace')

write_md("# 1. Scalar Trace Projection Gate\n\nA scalar interval channel can encode the isotropic trace of a symmetric\nbilinear response. In two dimensions, for\n\n```text\nH = [[a, b], [b, c]],\n```\n\nthe scalar trace projection is\n\n```text\nTr(H)/2 = (a + c)/2.\n```\n\nThe script also checks that a nonzero traceless shear matrix can have zero\nscalar trace. This is the first placement rule: scalar data can carry the trace\nchannel, not the full tensor.")
