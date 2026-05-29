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

k = sp.symbols('k')
H = sp.Matrix([[0,k],[k,0]])
require_zero(sp.trace(H), 'off diagonal trace invisible')
e1 = sp.Matrix([1,0]); e2 = sp.Matrix([0,1]); ep = sp.Matrix([1,1])
Q = lambda v: (v.T*H*v)[0]
# polarization recovers H12
recovered = (Q(ep) - Q(e1) - Q(e2))/2
require_zero(recovered - k, 'polarization sees off diagonal')

write_md("# 4. Off-Diagonal Scalar Invisibility\n\nAn off-diagonal symmetric response\n\n```text\nH = [[0, k], [k, 0]]\n```\n\nhas zero trace. The scalar channel cannot detect it. But polarization from\ndirectional probes gives\n\n```text\nH_12 = (Q(e_1 + e_2) - Q(e_1) - Q(e_2))/2 = k.\n```\n\nThus off-diagonal metric data belongs to the directional branch, not the scalar\nladder.")
