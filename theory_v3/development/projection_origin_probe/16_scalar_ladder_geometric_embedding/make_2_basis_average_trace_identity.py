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

n = sp.symbols('n', positive=True, integer=True)
a,b,c = sp.symbols('a b c')
H = sp.diag(a,b,c)
# Average of Q(e_i) over an orthonormal basis equals trace/n in n=3.
avg = sum(H[i,i] for i in range(3))/3
require_zero(avg - sp.trace(H)/3, 'basis average trace identity')

write_md("# 2. Basis Average Trace Identity\n\nFor an orthonormal directional probe basis, the average of the quadratic\nresponses\n\n```text\nQ(e_i) = e_i^T H e_i\n```\n\nrecovers the trace channel:\n\n```text\n(1/3) sum_i Q(e_i) = Tr(H)/3.\n```\n\nThe scalar projection is therefore naturally interpreted as an isotropic\naverage of directional interval probes.")
