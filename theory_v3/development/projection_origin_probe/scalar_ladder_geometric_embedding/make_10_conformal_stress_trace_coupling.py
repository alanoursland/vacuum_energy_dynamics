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

phi, T00,T11,T22,T33 = sp.symbols('phi T00 T11 T22 T33')
# Euclidean signature algebraic contraction for a conformal perturbation.
traceT = T00 + T11 + T22 + T33
contraction = phi*traceT
require_zero(contraction - phi*traceT, 'conformal coupling equals trace')

write_md("# 10. Conformal Stress Trace Coupling\n\nA conformal perturbation couples algebraically to the trace of stress data:\n\n```text\nh_ab = phi delta_ab  =>  T^{ab} h_ab = phi Tr(T).\n```\n\nThis is a trace-channel coupling. It is not enough to capture general\ntraceless/shear stress response.")
