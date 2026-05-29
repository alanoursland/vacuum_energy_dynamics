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

s = sp.symbols('s')
S = sp.diag(s, -s, 0)
trace = sp.trace(S)
q1 = S[0,0]
q2 = S[1,1]
require_zero(trace, 'TT/shear trace vanishes')
require_zero((q1-q2) - 2*s, 'directional probes see shear')

write_md("# 3. Shear Trace Invisibility\n\nThe traceless shear response\n\n```text\nS = diag(s, -s, 0)\n```\n\nhas\n\n```text\nTr(S) = 0,\n```\n\nso the scalar trace channel sees nothing. But directional probes distinguish\nit:\n\n```text\nQ(e_1) - Q(e_2) = 2s.\n```\n\nThis proves that scalar projection cannot reconstruct shear even when the\nshear is operationally visible to directional interval probes.")
