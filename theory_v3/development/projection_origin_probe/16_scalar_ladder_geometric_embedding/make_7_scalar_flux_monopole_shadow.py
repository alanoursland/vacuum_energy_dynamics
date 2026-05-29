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

r,Q = sp.symbols('r Q', positive=True)
Fr = Q/r**2
flux = 4*sp.pi*r**2*Fr
require_zero(flux - 4*sp.pi*Q, 'monopole flux conserved')

write_md("# 7. Scalar Flux Monopole Shadow\n\nFor the monopole radial field\n\n```text\nF_r = Q/r^2,\n```\n\nthe conserved scalar flux is\n\n```text\n4 pi r^2 F_r = 4 pi Q.\n```\n\nThis is the scalar boundary-flux channel: conserved monopole charge, not full\nboundary tensor data.")
