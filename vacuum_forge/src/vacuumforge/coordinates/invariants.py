"""Coordinate invariance validation helpers."""

from __future__ import annotations

import sympy

from vacuumforge.core.simplify import is_zero
from vacuumforge.requirements.validators import ValidationResult


def validate_coordinate_invariance(ctx, req_id: str, quantity: sympy.Basic, change) -> ValidationResult:
    """Check whether a scalar expression is invariant under a coordinate change."""
    transformed = sympy.simplify(quantity.subs(change.old_coord, change.transform))
    residual = sympy.simplify(quantity - transformed)
    zero = is_zero(residual)
    if zero is True:
        return ValidationResult(
            requirement_id=req_id,
            status="pass",
            message=f"{quantity} is invariant under {change.old_coord} = {change.transform}.",
            evidence=[residual],
            dependencies=[change.derivation_id] if change.derivation_id else [],
        )
    if zero is False:
        return ValidationResult(
            requirement_id=req_id,
            status="fail",
            message=f"{quantity} shifts by {residual} under coordinate change.",
            evidence=[residual, transformed],
            dependencies=[change.derivation_id] if change.derivation_id else [],
        )
    return ValidationResult(
        requirement_id=req_id,
        status="undetermined",
        message="Could not determine coordinate invariance.",
        evidence=[residual, transformed],
        dependencies=[change.derivation_id] if change.derivation_id else [],
    )


_validate_coordinate_invariance = validate_coordinate_invariance
