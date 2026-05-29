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

a,b,c,theta = sp.symbols('a b c theta')
H = sp.Matrix([[a,b],[b,c]])
ct,st = sp.cos(theta), sp.sin(theta)
R = sp.Matrix([[ct,-st],[st,ct]])
Hp = R.T*H*R
require_zero(sp.simplify(sp.trace(Hp)-sp.trace(H)), 'trace rotation invariance')

write_md("# 16. Trace Invariance Under Rotation\n\nThe scalar trace channel is invariant under rotation of the directional probe\nbasis:\n\n```text\nTr(R^T H R) = Tr(H).\n```\n\nThis explains why scalar projection is a stable isotropic shadow. It also\nexplains why it discards orientation-sensitive tensor information.")
