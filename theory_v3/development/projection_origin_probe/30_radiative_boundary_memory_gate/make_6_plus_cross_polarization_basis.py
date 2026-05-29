
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent

def write_report(filename: str, title: str, body: str):
    path = ROOT / filename
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(f"# {title}\n\n" + body.strip() + "\n")
    tmp.replace(path)

import sympy as sp
ep = sp.Matrix([[1,0],[0,-1]])
ex = sp.Matrix([[0,1],[1,0]])
inner = lambda A,B: sum(A[i,j]*B[i,j] for i in range(2) for j in range(2))
assert sp.trace(ep) == 0
assert sp.trace(ex) == 0
assert inner(ep,ex) == 0
assert inner(ep,ep) == 2
assert inner(ex,ex) == 2

write_report('6_plus_cross_polarization_basis.md', 'Plus/cross polarization basis', '\nThe script verifies the standard transverse traceless polarization basis:\n\n```text\ne_+ = [[1,0],[0,-1]],\ne_x = [[0,1],[1,0]].\n```\n\nBoth are traceless, mutually orthogonal, and nonzero. This is tensorial data that a\nscalar trace ledger cannot reconstruct.\n')
