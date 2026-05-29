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
# A radial field with angular factor P_l has net flux proportional to integral P_l.
for ell in range(1,6):
    require_zero(sp.integrate(sp.legendre(ell,x), (x,-1,1)), f'l={ell} net scalar flux')

write_md("# 8. Higher Multipoles Have Zero Net Scalar Flux\n\nThe scalar Gauss ledger integrates over the boundary. Any angular field\nproportional to `P_l(cos theta)` with `l >= 1` has zero net scalar flux because\nits angular integral vanishes.\n\nThis separates scalar charge accounting from higher multipole boundary shape\ninformation.")
