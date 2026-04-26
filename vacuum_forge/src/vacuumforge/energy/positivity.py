"""Positivity checks for energy functionals.

Uses Hessian-based analysis for quadratic forms.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import sympy


@dataclass
class PositivityResult:
    """Result of a positivity check."""

    status: str  # "positive", "semidefinite", "indefinite", "negative", "undetermined"
    conditions: list[sympy.Basic] = field(default_factory=list)
    hessian: sympy.Matrix | None = None
    notes: list[str] = field(default_factory=list)


def check_quadratic_positivity(
    expr: sympy.Basic,
    variables: list[sympy.Basic],
) -> PositivityResult:
    """Check positive-definiteness of a quadratic form via its Hessian.

    For a two-variable quadratic form, positive definiteness requires:
      H_11 > 0  and  det(H) > 0
    """
    H = sympy.hessian(expr, variables)
    n = len(variables)
    notes = []

    if n == 0:
        return PositivityResult(status="undetermined", notes=["No variables"])

    # Check principal minors (Sylvester's criterion)
    positive_checks = []
    for i in range(1, n + 1):
        minor = H[:i, :i].det()
        minor_simplified = sympy.simplify(minor)

        if minor_simplified.is_positive is True:
            positive_checks.append(True)
        elif minor_simplified.is_negative is True:
            return PositivityResult(
                status="indefinite" if i < n else "negative",
                hessian=H,
                conditions=[minor_simplified > 0],
                notes=[f"Principal minor {i} is negative: {minor_simplified}"],
            )
        elif minor_simplified.is_zero is True:
            notes.append(f"Principal minor {i} is zero — semidefinite direction.")
            positive_checks.append(None)
        else:
            # Can't determine sign
            positive_checks.append(None)
            notes.append(f"Principal minor {i} sign undetermined: {minor_simplified}")

    if all(c is True for c in positive_checks):
        return PositivityResult(status="positive", hessian=H, notes=notes)

    if any(c is None for c in positive_checks):
        # Report conditions needed
        conditions = []
        for i in range(1, n + 1):
            minor = H[:i, :i].det()
            conditions.append(sympy.simplify(minor) > 0)
        return PositivityResult(
            status="undetermined",
            hessian=H,
            conditions=conditions,
            notes=notes,
        )

    return PositivityResult(status="undetermined", hessian=H, notes=notes)
