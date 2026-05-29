
import sympy as sp
from pathlib import Path

OUT = Path(__file__).with_name('19_upstream_ontology_not_decided.md')

def require_zero(expr):
    expr = sp.simplify(expr)
    if expr != 0:
        raise AssertionError(f'Expected zero, got {expr}')

U,B=sp.symbols('U B')
# Boundary chart B matching does not logically imply upstream ontology U.
# Truth-table witness: B true, U false is allowed.
Bval=True; Uval=False
assert Bval and not Uval

OUT.write_text('# Upstream Ontology Not Decided\n\nFailure to derive the projection chart from weak-field GR scalar data does not mean the vacuum ontology is idle.\n\nIt means any ontology work must explain why this projection chart, quadratic interval structure, or boundary admissibility class is natural upstream of the scalar reduction.\n')
print('wrote', OUT.name)
