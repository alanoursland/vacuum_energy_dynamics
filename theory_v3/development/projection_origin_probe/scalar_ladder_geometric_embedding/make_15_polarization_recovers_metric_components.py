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
e1 = sp.Matrix([1,0]); e2 = sp.Matrix([0,1])
Q = lambda v: (v.T*H*v)[0]
H11 = Q(e1)
H22 = Q(e2)
H12 = (Q(e1+e2)-Q(e1)-Q(e2))/2
require_zero(H11-a, 'H11')
require_zero(H22-c, 'H22')
require_zero(H12-b, 'H12')

write_md("# 15. Polarization Recovers Metric Components\n\nDirectional probes reconstruct the full symmetric bilinear form. In two\ndimensions,\n\n```text\nH_11 = Q(e_1),\nH_22 = Q(e_2),\nH_12 = (Q(e_1 + e_2) - Q(e_1) - Q(e_2))/2.\n```\n\nThe script checks these identities exactly. This is the directional completion\nthat the scalar ladder lacks.")
