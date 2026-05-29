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

hp,hx = sp.symbols('h_plus h_cross')
H = sp.Matrix([[hp,hx,0],[hx,-hp,0],[0,0,0]])
require_zero(sp.trace(H), 'TT trace zero')
# Plus and cross are still recoverable directionally.
e1=sp.Matrix([1,0,0]); e2=sp.Matrix([0,1,0]); ep=sp.Matrix([1,1,0])
Q=lambda v:(v.T*H*v)[0]
require_zero(Q(e1)-hp, 'plus directional')
require_zero((Q(ep)-Q(e1)-Q(e2))/2 - hx, 'cross directional')

write_md("# 17. TT Mode Scalar Projection Zero\n\nA standard transverse-traceless block\n\n```text\n[[h_plus, h_cross, 0],\n [h_cross, -h_plus, 0],\n [0, 0, 0]]\n```\n\nhas zero trace, so scalar projection kills it. Directional polarization still\nrecovers `h_plus` and `h_cross`. Therefore TT radiation cannot be supplied by\nthe scalar ladder alone.")
