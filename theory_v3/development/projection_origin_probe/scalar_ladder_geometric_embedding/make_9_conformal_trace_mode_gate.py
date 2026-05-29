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

n, psi = sp.symbols('n psi', positive=True)
# Spatial h_ij = 2 psi delta_ij has trace 2 n psi.
trace_expr = 2*n*psi
require_zero(trace_expr/n - 2*psi, 'isotropic conformal response per direction')

write_md("# 9. Conformal Trace Mode Gate\n\nAn isotropic spatial perturbation\n\n```text\nh_ij = 2 psi delta_ij\n```\n\nhas trace\n\n```text\nTr(h) = 2 n psi.\n```\n\nThe scalar ladder can naturally encode this conformal/trace sector. It cannot\nencode the traceless deviation from this form.")
