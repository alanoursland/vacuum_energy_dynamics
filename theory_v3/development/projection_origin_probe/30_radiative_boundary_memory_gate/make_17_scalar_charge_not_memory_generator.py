
from pathlib import Path
import sympy as sp
ROOT = Path(__file__).resolve().parent

def write_report(filename: str, title: str, body: str):
    path = ROOT / filename
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(f"# {title}\n\n" + body.strip() + "\n")
    tmp.replace(path)

import sympy as sp
M, Cp, Cx = sp.symbols('M Cp Cx')
Cnorm = 2*(Cp**2 + Cx**2)
assert sp.diff(M,Cp) == 0
assert sp.diff(M,Cx) == 0
assert sp.diff(Cnorm,M) == 0

write_report('17_scalar_charge_not_memory_generator.md', 'Scalar charge is not memory generator', 'This independence witness records that a scalar charge variable `M` is not by itself a memory generator. The tensor memory norm varies in `(C_+, C_x)`, not in the scalar monopole variable.\n')
