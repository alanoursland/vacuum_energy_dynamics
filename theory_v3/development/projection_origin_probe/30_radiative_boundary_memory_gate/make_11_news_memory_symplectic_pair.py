
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent

def write_report(filename: str, title: str, body: str):
    path = ROOT / filename
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(f"# {title}\n\n" + body.strip() + "\n")
    tmp.replace(path)

import sympy as sp
C1, C2, N1, N2 = sp.symbols('C1 C2 N1 N2')
omega = C1*N2 - C2*N1
assert sp.simplify(omega + (C2*N1 - C1*N2)) == 0
assert omega.subs({C1:C2,N1:N2}) == 0

write_report('11_news_memory_symplectic_pair.md', 'News/memory symplectic pair witness', '\nA simple boundary symplectic pairing has the antisymmetric form\n\n```text\nomega((C1,N1),(C2,N2)) = C1 N2 - C2 N1.\n```\n\nThe script verifies antisymmetry and self-pairing zero. Radiative boundary data is\nphase-space data, not a single scalar charge.\n')
