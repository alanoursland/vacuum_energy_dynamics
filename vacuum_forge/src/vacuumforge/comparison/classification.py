"""Model status classification (M27).

Automatically classifies candidate models by scientific status
based on validation results and leak audits.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vacuumforge.core.context import TheoryContext


class ModelClass(str, Enum):
    DERIVES_EQUAL_RESPONSE = "derives_equal_response"
    ASSUMES_EQUAL_RESPONSE = "assumes_equal_response"
    ALGEBRAICALLY_CONSISTENT = "algebraically_consistent"
    FAILS_POSITIVITY = "fails_positivity"
    LEAVES_GAMMA_FREE = "leaves_gamma_free"
    PREDICTS_WRONG_WEAK_FIELD = "predicts_wrong_weak_field"
    REQUIRES_NEW_POSTULATE = "requires_new_postulate"
    CANDIDATE_FOR_DEVELOPMENT = "candidate_for_development"
    EXPLORATORY = "exploratory"


@dataclass
class ClassificationResult:
    """Result of classifying a model."""

    primary: ModelClass
    secondary: list[ModelClass] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    @property
    def label(self) -> str:
        return self.primary.value.replace("_", " ").title()


def classify_model(ctx: TheoryContext) -> ClassificationResult:
    """Classify a model based on its validation results.

    Classification hierarchy (first match wins for primary):
    1. If reciprocal_scaling is assumed → assumes_equal_response
    2. If reciprocal_scaling fails → check gamma, positivity
    3. If reciprocal_scaling passes and derived → derives_equal_response
    4. Otherwise → exploratory
    """
    results = ctx.requirements.validate_all(ctx)
    rs = {r.requirement_id: r for r in results}

    secondary = []
    notes = []

    recip = rs.get("reciprocal_scaling")
    gamma = rs.get("gamma_v_one")
    beta = rs.get("beta_one")
    energy = rs.get("positive_energy")
    trace = rs.get("trace_free_exchange")

    # Check for assumed equal-response
    if recip and recip.status == "assumed":
        notes.append("Reciprocal scaling (AB=1) was assumed, not derived.")
        if trace and trace.status == "assumed":
            secondary.append(ModelClass.REQUIRES_NEW_POSTULATE)
            notes.append("Trace-free exchange also assumed.")
        return ClassificationResult(
            ModelClass.ASSUMES_EQUAL_RESPONSE, secondary, notes
        )

    # Check for derived equal-response
    if recip and recip.status == "pass":
        if gamma and gamma.status == "pass" and beta and beta.status == "pass":
            if energy and energy.status == "pass":
                if trace and trace.status == "assumed":
                    secondary.append(ModelClass.REQUIRES_NEW_POSTULATE)
                    notes.append(
                        "Equal-response derived, but trace-free exchange assumed."
                    )
                return ClassificationResult(
                    ModelClass.DERIVES_EQUAL_RESPONSE, secondary, notes
                )
            elif energy and energy.status == "fail":
                secondary.append(ModelClass.FAILS_POSITIVITY)
                return ClassificationResult(
                    ModelClass.ALGEBRAICALLY_CONSISTENT, secondary, notes
                )
            else:
                return ClassificationResult(
                    ModelClass.CANDIDATE_FOR_DEVELOPMENT, secondary, notes
                )

    # Failure modes for gamma
    if gamma and gamma.status == "fail":
        # Check if gamma_v is symbolic (free) vs a wrong numeric value
        gamma_is_free = False
        if gamma.evidence:
            import sympy
            val = gamma.evidence[0]
            if hasattr(val, 'free_symbols') and val.free_symbols:
                gamma_is_free = True
        if gamma_is_free:
            notes.append("gamma_v remains a free parameter in the model.")
            return ClassificationResult(
                ModelClass.LEAVES_GAMMA_FREE, secondary, notes
            )
        notes.append(f"gamma_v: {gamma.message}")
        return ClassificationResult(
            ModelClass.PREDICTS_WRONG_WEAK_FIELD, secondary, notes
        )

    if gamma and gamma.status == "undetermined":
        notes.append("gamma_v remains free (not constrained by model).")
        return ClassificationResult(
            ModelClass.LEAVES_GAMMA_FREE, secondary, notes
        )

    if energy and energy.status == "fail":
        return ClassificationResult(
            ModelClass.FAILS_POSITIVITY, secondary, notes
        )

    if recip and recip.status == "fail":
        notes.append(f"Reciprocal scaling fails: {recip.message}")
        return ClassificationResult(
            ModelClass.PREDICTS_WRONG_WEAK_FIELD, secondary, notes
        )

    return ClassificationResult(ModelClass.EXPLORATORY, secondary, notes)
