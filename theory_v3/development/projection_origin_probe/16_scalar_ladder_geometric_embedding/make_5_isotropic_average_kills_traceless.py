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

a,b = sp.symbols('a b')
S = sp.diag(a,b,-a-b)
# Isotropic second moment <v_i v_j> = delta_ij/3.
avg = sp.trace(S)/3
require_zero(avg, 'isotropic average of traceless quadratic form')

write_md("# 5. Isotropic Average Kills Traceless Sector\n\nUsing the isotropic second-moment identity\n\n```text\n< v_i v_j > = delta_ij / 3,\n```\n\nthe angular average of a quadratic response is\n\n```text\n< v^T S v > = Tr(S)/3.\n```\n\nFor traceless `S`, this vanishes. The scalar/isotropic average therefore kills\ntraceless tensor structure by construction.")
