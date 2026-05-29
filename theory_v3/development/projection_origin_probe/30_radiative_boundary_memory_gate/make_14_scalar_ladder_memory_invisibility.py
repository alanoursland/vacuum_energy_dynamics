
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent

def write_report(filename: str, title: str, body: str):
    path = ROOT / filename
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(f"# {title}\n\n" + body.strip() + "\n")
    tmp.replace(path)

import sympy as sp
# scalar channel dimension versus transverse traceless memory dimension
scalar_dim = sp.Integer(1)
tt_dim = sp.Integer(2)
gap = tt_dim - scalar_dim
assert gap == 1
# But trace map of TT memory is zero, so scalar trace channel sees zero, not one combination.
Cp, Cx = sp.symbols('Cp Cx')
trace = Cp + (-Cp)
assert sp.simplify(trace) == 0

write_report('14_scalar_ladder_memory_invisibility.md', 'Scalar ladder cannot encode memory tensor', '\nEven though a scalar channel has one number, the trace map of a TT memory tensor gives\nzero rather than one useful combination. The scalar ladder does not encode a hidden\nprojection of plus/cross memory; it is simply the wrong channel.\n')
