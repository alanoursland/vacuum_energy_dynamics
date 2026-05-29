
from pathlib import Path
import sympy as sp
ROOT = Path(__file__).resolve().parent

def write_report(filename: str, title: str, body: str):
    path = ROOT / filename
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(f"# {title}\n\n" + body.strip() + "\n")
    tmp.replace(path)

import sympy as sp
C_i, Delta, u = sp.symbols('C_i Delta u')
C_f = C_i + Delta
N_final = sp.diff(C_f, u)
assert N_final == 0
assert sp.simplify(C_f - C_i - Delta) == 0

write_report('16_soft_shift_zero_news_afterward.md', 'Soft shift with zero final news', 'A soft/memory shift can leave a new final shear value with zero final news:\n\n```text\nC_final = C_initial + Delta C,\nN_final = 0.\n```\n\nMemory is a boundary configuration change, not necessarily ongoing radiation.\n')
