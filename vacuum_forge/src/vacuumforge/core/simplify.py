"""Controlled simplification utilities for VacuumForge.

SymPy's simplify() can be unpredictable with logs and exponentials.
These wrappers provide reproducible simplification behavior.
"""

from __future__ import annotations

import sympy


def vf_simplify(
    expr: sympy.Basic,
    *,
    log: bool = True,
    powers: bool = True,
    factor: bool = False,
) -> sympy.Basic:
    """Controlled simplification pipeline."""
    result = sympy.expand(expr)
    if log:
        result = sympy.expand_log(result, force=True)
        result = sympy.logcombine(result, force=True)
    if powers:
        result = sympy.powsimp(result, force=True)
    if factor:
        result = sympy.factor(result)
    return result


def is_zero(expr: sympy.Basic) -> bool | None:
    """Check if expression is zero. Returns None if undetermined."""
    simplified = sympy.simplify(expr)
    if simplified == 0:
        return True
    if simplified.is_zero is True:
        return True
    if simplified.is_zero is False:
        return False
    # Try harder
    expanded = sympy.expand(expr)
    if expanded == 0:
        return True
    # If the simplified expression contains free symbols and is structurally
    # nontrivial (not just 0 in disguise), it's generically nonzero.
    # Check by evaluating at a random point.
    free = simplified.free_symbols
    if free:
        try:
            test_val = simplified.subs({s: sympy.Rational(17, 10) for s in free})
            test_val = sympy.nsimplify(test_val)
            if test_val != 0:
                return False
        except (TypeError, ValueError, ZeroDivisionError):
            pass
    return None


def is_equivalent(a: sympy.Basic, b: sympy.Basic) -> bool | None:
    """Check if two expressions are equivalent. Returns None if undetermined."""
    return is_zero(a - b)


def check_equal(a: sympy.Basic, b: sympy.Basic) -> bool:
    """Best-effort check if a == b. Returns False if undetermined."""
    result = is_zero(a - b)
    return result is True
