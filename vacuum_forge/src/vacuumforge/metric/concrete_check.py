"""Leak-aware checks for concrete metric substitutions.

Implements Milestone 48 from the validation-hardening technical design.

Distinguishes four classification states:
  - satisfied_independently: requirement passes, no leak detected.
  - satisfied_by_construction: requirement passes, target is present in
    the assumption ledger (or implied by the metric definition).
  - failed: requirement does not hold for the concrete metric.
  - undetermined: validator could not evaluate.
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy

from vacuumforge.core.simplify import check_equal
from vacuumforge.requirements.leak_detection import LeakReport, detect_leaks
from vacuumforge.requirements.validators import ValidationResult


@dataclass
class ConcreteMetricCheckResult:
    """Result of checking a concrete metric against one requirement."""

    requirement_id: str
    status: str  # "satisfied_independently", "satisfied_by_construction", "failed", "undetermined"
    message: str
    leak_report: LeakReport | None = None
    underlying_validation: ValidationResult | None = None


def check_concrete_metric(
    ctx,
    A_value: sympy.Basic,
    B_value: sympy.Basic,
    requirement_ids: list[str] | None = None,
) -> list[ConcreteMetricCheckResult]:
    """Check concrete A/B values against requirements with leak-aware vocabulary.

    Clones the context, injects A_value and B_value as assumptions, runs
    each requested validator, then classifies the result using leak detection.
    """
    if ctx._mode_symbols is None:
        return [
            ConcreteMetricCheckResult(
                requirement_id="concrete_metric",
                status="undetermined",
                message="No standard mode symbols are defined.",
            )
        ]

    # Clone the context to avoid polluting the caller's state.
    working = ctx.clone()
    ms = working._mode_symbols
    working.assumptions.add("concrete_metric_A", sympy.Eq(ms.A, A_value))
    working.assumptions.add("concrete_metric_B", sympy.Eq(ms.B, B_value))

    ids = requirement_ids or [req.id for req in working.requirements.list()]
    results: list[ConcreteMetricCheckResult] = []

    for req_id in ids:
        validation = working.requirements.validate(req_id, working)

        # Run generic leak detection if the target library has this requirement.
        leak = None
        if (
            hasattr(working, "_targets")
            and working._targets is not None
            and working._targets.has(req_id)
        ):
            leak = detect_leaks(req_id, working.assumptions, working._targets)

        # Special-case: reciprocal_scaling.  If A·B == 1 holds algebraically,
        # the target is encoded in the concrete metric definition regardless
        # of whether the generic leak detector catches the form.
        if req_id == "reciprocal_scaling" and check_equal(A_value * B_value, sympy.Integer(1)):
            leaked_via = []
            if working.assumptions.has("concrete_metric_A"):
                leaked_via.append("concrete_metric_A")
            if working.assumptions.has("concrete_metric_B"):
                leaked_via.append("concrete_metric_B")
            leak = LeakReport(
                target_id=req_id,
                leaked=True,
                leaked_via=leaked_via,
                message="Reciprocal scaling is encoded by the concrete A/B metric definition.",
            )

        # Four-way classification.
        if validation.status in {"pass", "assumed"}:
            if leak is not None and leak.leaked:
                status = "satisfied_by_construction"
                message = (
                    f"{req_id} is satisfied, but the target form is present "
                    f"in the metric definition. {leak.message}"
                )
            else:
                status = "satisfied_independently"
                message = f"{req_id} is satisfied without the target form being assumed."
        elif validation.status == "fail":
            status = "failed"
            message = validation.message
        else:
            status = "undetermined"
            message = validation.message

        results.append(
            ConcreteMetricCheckResult(
                requirement_id=req_id,
                status=status,
                message=message,
                leak_report=leak,
                underlying_validation=validation,
            )
        )

    return results
