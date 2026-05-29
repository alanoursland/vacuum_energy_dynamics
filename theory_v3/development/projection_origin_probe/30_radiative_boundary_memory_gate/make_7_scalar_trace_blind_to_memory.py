
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent

def write_report(filename: str, title: str, body: str):
    path = ROOT / filename
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(f"# {title}\n\n" + body.strip() + "\n")
    tmp.replace(path)

import sympy as sp
Cp, Cx = sp.symbols('Cp Cx')
C = sp.Matrix([[Cp,Cx],[Cx,-Cp]])
trace = sp.trace(C)
assert sp.simplify(trace) == 0
norm = sp.simplify(sum(C[i,j]**2 for i in range(2) for j in range(2)))
assert sp.simplify(norm - 2*(Cp**2+Cx**2)) == 0

write_report('7_scalar_trace_blind_to_memory.md', 'Scalar trace is blind to memory shear', '\nA permanent memory displacement can be traceless:\n\n```text\nC_AB = [[C_+, C_x], [C_x, -C_+]].\n```\n\nThe scalar trace is zero while the tensor norm is nonzero. Therefore scalar boundary\ncharge is blind to traceless memory.\n')
