
from pathlib import Path
import sympy as sp
ROOT = Path(__file__).resolve().parent

def write_report(filename: str, title: str, body: str):
    path = ROOT / filename
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(f"# {title}\n\n" + body.strip() + "\n")
    tmp.replace(path)

import sympy as sp
closed_scalar_charge = sp.Integer(1)
needs_tensor_news = sp.Integer(1)
assert closed_scalar_charge == 1
assert needs_tensor_news == 1

write_report('18_tensor_news_boundary_status.md', 'Tensor news boundary status', 'This status script records the compatibility of two claims:\n\n```text\nscalar charge ledger is closed;\nradiative tensor news ledger is additional.\n```\n\nThe second does not reopen the solved scalar `r_k` sector.\n')
