
import sympy as sp
from pathlib import Path

OUT = Path(__file__).with_name('17_projection_variable_status_table.md')

def require_zero(expr):
    expr = sp.simplify(expr)
    if expr != 0:
        raise AssertionError(f'Expected zero, got {expr}')

fixed=sp.Integer(3)  # Poisson, flux, exterior
chosen=sp.Integer(4) # y, basis, contact, pairing
assert fixed < fixed+chosen

OUT.write_text('# Projection Variable Status Table\n\nThis folder separates what is fixed from what is chosen.\n\nFixed by weak-field scalar physics:\n\n```text\n1/r exterior, finite Gauss flux, Poisson source ledger.\n```\n\nChosen by projection embedding:\n\n```text\ny=x^2 chart, endpoint contact factor, polynomial test basis, moment pairing.\n```\n')
print('wrote', OUT.name)
