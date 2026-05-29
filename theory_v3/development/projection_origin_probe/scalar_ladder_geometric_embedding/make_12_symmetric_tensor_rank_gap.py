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

m = sp.symbols('m', integer=True, positive=True)
components = m*(m+1)/2
gap = components - 1
require_zero(gap - (m*(m+1)/2 - 1), 'rank gap formula')
# Sample m=3: 6 tensor components, 1 scalar trace, gap 5.
require_zero(gap.subs(m,3) - 5, 'm=3 rank gap')

write_md("# 12. Symmetric Tensor Rank Gap\n\nA symmetric bilinear form on an `m`-dimensional space has\n\n```text\nm(m+1)/2\n```\n\ncomponents. A scalar trace channel has one component. The per-mode rank gap is\ntherefore\n\n```text\nm(m+1)/2 - 1.\n```\n\nFor `m=3`, the gap is `5`.")
