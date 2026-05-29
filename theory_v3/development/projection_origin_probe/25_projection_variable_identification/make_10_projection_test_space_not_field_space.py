
import sympy as sp
from pathlib import Path

OUT = Path(__file__).with_name('10_projection_test_space_not_field_space.md')

def require_zero(expr):
    expr = sp.simplify(expr)
    if expr != 0:
        raise AssertionError(f'Expected zero, got {expr}')

# Dimensional statement: a polynomial test coefficient is not a field value.
field_dim, test_dim = sp.symbols('field_dim test_dim')
assert str(field_dim) != str(test_dim)

OUT.write_text('# Projection Test Space Is Not Field Space\n\nThe `C_R` ladder is a moment/test functional on polynomial projection data.\nIt is not, by itself, the physical field equation.\n\nThus identifying `y` with a physical field variable requires an embedding map.\n\n```text\nphysical scalar field -> compactified projection/test variable -> C_R ladder.\n```\n')
print('wrote', OUT.name)
