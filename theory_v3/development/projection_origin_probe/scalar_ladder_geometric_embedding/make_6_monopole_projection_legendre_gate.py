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

x = sp.symbols('x')
for ell in range(1,5):
    P = sp.legendre(ell, x)
    require_zero(sp.integrate(P, (x,-1,1)), f'Legendre l={ell} zero monopole')
require_zero(sp.integrate(sp.legendre(0,x),(x,-1,1)) - 2, 'l=0 monopole normalization')

write_md("# 6. Monopole Projection Legendre Gate\n\nThe scalar boundary ladder naturally matches the monopole projection. The\nscript checks\n\n```text\nint_{-1}^{1} P_l(x) dx = 0  for l >= 1,\nint_{-1}^{1} P_0(x) dx = 2.\n```\n\nSo the angular scalar average retains only the `l=0` mode. Higher multipoles\nare not recovered by a scalar monopole ledger.")
