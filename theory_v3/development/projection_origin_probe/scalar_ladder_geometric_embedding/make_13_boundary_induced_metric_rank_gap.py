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

D = sp.symbols('D', integer=True, positive=True)
m = D - 1
components = m*(m+1)/2
scalar_gap = components - 1
require_zero(scalar_gap.subs(D,4) - 5, 'D=4 boundary rank gap')
require_zero(components.subs(D,4) - 6, 'D=4 boundary metric components')

write_md("# 13. Boundary Induced Metric Rank Gap\n\nFor spacetime dimension `D`, a hypersurface boundary has dimension\n\n```text\nm = D - 1.\n```\n\nThe induced boundary metric has\n\n```text\nm(m+1)/2\n```\n\ncomponents. In `D=4`, this is `6`, while the scalar trace channel supplies one.\nThe boundary tensor gap is therefore `5`.")
