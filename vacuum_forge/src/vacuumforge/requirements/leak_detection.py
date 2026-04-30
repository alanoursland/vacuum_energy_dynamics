"""Assumption leak detection.

Detects when a target result has been inserted into assumptions
or definitions under another name.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import sympy

from vacuumforge.core.assumptions import AssumptionManager
from vacuumforge.core.simplify import check_equal
from vacuumforge.requirements.targets import TargetLibrary


@dataclass
class LeakReport:
    """Report of detected assumption leaks."""

    target_id: str
    leaked: bool
    leaked_via: list[str] = field(default_factory=list)
    message: str = ""


def detect_leaks(
    target_id: str,
    assumptions: AssumptionManager,
    targets: TargetLibrary,
) -> LeakReport:
    """Check if a target result is already present in the assumptions."""
    if not targets.has(target_id):
        return LeakReport(target_id=target_id, leaked=False, message="Target not found in library")

    target = targets.get(target_id)
    all_forms = [target.expression] + target.equivalent_forms
    leaked_via = []

    for record in assumptions.active():
        # Records marked as derived were produced by upstream logic,
        # not smuggled in as premises.  Skip them.
        if record.status == "derived":
            continue
        expr = record.expression
        for form in all_forms:
            if _assumption_contains_target(expr, form):
                leaked_via.append(record.id)
                break

    if leaked_via:
        return LeakReport(
            target_id=target_id,
            leaked=True,
            leaked_via=leaked_via,
            message=(
                f"Target '{target_id}' is present as assumption(s): "
                f"{', '.join(leaked_via)}. "
                f"Derivation cannot classify this result as derived unless "
                f"these assumptions are removed."
            ),
        )

    return LeakReport(
        target_id=target_id,
        leaked=False,
        message=f"No assumption leak detected for '{target_id}'.",
    )


def _assumption_contains_target(assumption: sympy.Basic, target: sympy.Basic) -> bool:
    """Check if an assumption is equivalent to a target form."""
    if isinstance(assumption, sympy.Eq) and isinstance(target, sympy.Eq):
        diff_a = assumption.lhs - assumption.rhs
        diff_t = target.lhs - target.rhs
        return check_equal(diff_a, diff_t) or check_equal(diff_a, -diff_t)

    if isinstance(assumption, sympy.Eq):
        diff = assumption.lhs - assumption.rhs
        if isinstance(target, sympy.Eq):
            target_diff = target.lhs - target.rhs
            return check_equal(diff, target_diff) or check_equal(diff, -target_diff)
        return check_equal(diff, target)

    return False
