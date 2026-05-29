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

q,a = sp.symbols('q a')
# toy boundary density rho(theta)= q + a P2(cos theta). Net charge depends only on q.
x=sp.symbols('x')
rho = q + a*sp.legendre(2,x)
net = sp.integrate(rho,(x,-1,1))/2
require_zero(net-q, 'net monopole ignores quadrupole shape')

write_md("# 21. Monopole Charge Is Not Shape Data\n\nFor a toy angular density\n\n```text\nrho = q + a P_2(cos theta),\n```\n\nthe normalized angular average is exactly `q`. The quadrupole coefficient `a`\ndoes not affect the net scalar charge.\n\nThus scalar boundary charge accounting does not contain boundary shape/tensor\ninformation.")
