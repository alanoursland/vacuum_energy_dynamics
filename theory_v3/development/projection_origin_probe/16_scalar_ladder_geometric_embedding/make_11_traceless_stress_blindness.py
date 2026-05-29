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

s,t = sp.symbols('s t')
T = sp.diag(s, -s, t, -t)
phi = sp.symbols('phi')
require_zero(sp.trace(T), 'stress trace zero')
require_zero(phi*sp.trace(T), 'conformal channel blind to traceless stress')

write_md("# 11. Traceless Stress Blindness\n\nFor traceless stress data, the conformal/trace scalar channel gives zero\ncoupling. The script checks an explicit nonzero traceless diagonal tensor with\n\n```text\nTr(T) = 0,\nphi Tr(T) = 0.\n```\n\nThus scalar interval response cannot be the full matter-coupling geometry.")
