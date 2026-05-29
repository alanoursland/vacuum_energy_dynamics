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

N,m = sp.symbols('N m', integer=True, positive=True)
tensor_modes = N*m*(m+1)/2
scalar_modes = N
gap = tensor_modes - scalar_modes
require_zero(gap - N*(m*(m+1)/2 - 1), 'per mode scalar tensor gap')

write_md("# 14. Per-Mode Scalar Tensor Gap\n\nFor `N` boundary modes, the scalar ladder supplies `N` scalar coefficients. A\nfull symmetric tensor boundary response supplies\n\n```text\nN m(m+1)/2\n```\n\ncoefficients. The missing tensor data is therefore\n\n```text\nN (m(m+1)/2 - 1).\n```\n\nThis proves that increasing scalar mode count alone does not close the tensor\nrank gap.")
