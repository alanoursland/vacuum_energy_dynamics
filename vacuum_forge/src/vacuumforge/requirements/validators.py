"""Requirement validation system.

Validates candidate structures against declared requirements,
distinguishing pass/fail/assumed/undetermined.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any

import sympy

from vacuumforge.core.simplify import check_equal, is_zero
from vacuumforge.core.status import Exactness

if TYPE_CHECKING:
    from vacuumforge.core.context import TheoryContext


@dataclass
class ValidationResult:
    """Result of validating a single requirement."""

    requirement_id: str
    status: str  # "pass", "fail", "assumed", "undetermined"
    message: str
    evidence: list[sympy.Basic] = field(default_factory=list)
    dependencies: list[str] = field(default_factory=list)
    exactness: Exactness = Exactness.UNDETERMINED


class Requirement:
    """A requirement that a candidate structure must satisfy."""

    def __init__(
        self,
        id: str,
        description: str,
        validator: Any = None,
        exactness: str = "exact",
    ) -> None:
        self.id = id
        self.description = description
        self._validator = validator
        self.exactness = exactness

    def validate(self, ctx: TheoryContext) -> ValidationResult:
        if self._validator:
            return self._validator(ctx, self.id)
        return ValidationResult(
            requirement_id=self.id,
            status="undetermined",
            message=f"No validator defined for {self.id}",
        )


# --- Built-in validators ---

def _validate_reciprocal_scaling(ctx: TheoryContext, req_id: str) -> ValidationResult:
    """Check if the model implies A*B = 1."""
    from vacuumforge.requirements.leak_detection import detect_leaks

    ms = ctx._mode_symbols
    if ms is None:
        return ValidationResult(req_id, "undetermined", "No standard symbols defined.")

    # Check for assumption leak first
    if hasattr(ctx, '_targets') and ctx._targets is not None:
        leak = detect_leaks("reciprocal_scaling", ctx.assumptions, ctx._targets)
        if leak.leaked:
            return ValidationResult(
                req_id, "assumed", leak.message,
                dependencies=leak.leaked_via,
            )

    # Try to check with applied assumptions
    A_val = ctx.assumptions.apply(ms.A)
    B_val = ctx.assumptions.apply(ms.B)
    result = ctx.checks.reciprocal_scaling(A_val, B_val)

    return ValidationResult(
        req_id, result.status, result.message,
        evidence=[result.residual] if result.residual is not None else [],
    )


def _validate_gamma_v_one(ctx: TheoryContext, req_id: str) -> ValidationResult:
    """Check if gamma_v = 1."""
    ms = ctx._mode_symbols
    if ms is None:
        return ValidationResult(req_id, "undetermined", "No standard symbols defined.")

    A_val = ctx.assumptions.apply(ms.A)
    B_val = ctx.assumptions.apply(ms.B)

    if A_val == ms.A or B_val == ms.B:
        return ValidationResult(req_id, "undetermined",
                                "A or B not determined by assumptions.")

    metric = ctx.metric.from_scale_factors(A_val, B_val)
    gamma = ctx.ppn.extract_gamma(metric)

    if check_equal(gamma.value, sympy.Integer(1)):
        return ValidationResult(req_id, "pass", f"gamma_v = {gamma.value} = 1",
                                evidence=[gamma.value])
    else:
        return ValidationResult(req_id, "fail", f"gamma_v = {gamma.value} != 1",
                                evidence=[gamma.value])


def _validate_beta_one(ctx: TheoryContext, req_id: str) -> ValidationResult:
    """Check if beta = 1."""
    ms = ctx._mode_symbols
    if ms is None:
        return ValidationResult(req_id, "undetermined", "No standard symbols defined.")

    A_val = ctx.assumptions.apply(ms.A)
    B_val = ctx.assumptions.apply(ms.B)

    if A_val == ms.A:
        return ValidationResult(req_id, "undetermined", "A not determined by assumptions.")

    metric = ctx.metric.from_scale_factors(A_val, B_val)
    beta = ctx.ppn.extract_beta(metric)

    if check_equal(beta.value, sympy.Integer(1)):
        return ValidationResult(req_id, "pass", f"beta = {beta.value} = 1",
                                evidence=[beta.value])
    else:
        return ValidationResult(req_id, "fail", f"beta = {beta.value} != 1",
                                evidence=[beta.value])


def _validate_positive_energy(ctx: TheoryContext, req_id: str) -> ValidationResult:
    """Check if the first energy functional is positive."""
    from vacuumforge.energy.positivity import check_quadratic_positivity

    functionals = ctx.energy.list()
    if not functionals:
        return ValidationResult(req_id, "undetermined", "No energy functional defined.")

    func = functionals[0]
    result = check_quadratic_positivity(func.expression, func.variables)

    if result.status == "positive":
        return ValidationResult(req_id, "pass", "Energy functional is positive definite.")
    elif result.status == "indefinite":
        return ValidationResult(req_id, "fail",
                                f"Energy functional is indefinite. {'; '.join(result.notes)}")
    else:
        msg = f"Positivity {result.status}."
        if result.conditions:
            msg += f" Requires: {result.conditions}"
        return ValidationResult(req_id, "undetermined", msg)


def _validate_trace_free_exchange(ctx: TheoryContext, req_id: str) -> ValidationResult:
    """Check if exchange source is trace-free."""
    from vacuumforge.core.status import SourceClass

    sources = ctx.sources.list()
    exchange_sources = [s for s in sources if s.source_type == "exchange"]

    if not exchange_sources:
        return ValidationResult(req_id, "undetermined", "No exchange source defined.")

    src = exchange_sources[0]
    if src.classification == SourceClass.TRACE_FREE:
        if src.assumed_trace_free:
            return ValidationResult(req_id, "assumed",
                                    "Exchange is trace-free by direct assumption.")
        return ValidationResult(req_id, "pass", "Exchange source is trace-free.")
    elif src.classification == SourceClass.MIXED:
        return ValidationResult(req_id, "fail", "Exchange source has nonzero J_kappa.")
    else:
        return ValidationResult(req_id, "undetermined",
                                f"Exchange source classification: {src.classification.value}")


def build_standard_requirements() -> list[Requirement]:
    """Build the standard requirement set for the equal-response problem."""
    return [
        Requirement("reciprocal_scaling", "A*B = 1", _validate_reciprocal_scaling),
        Requirement("gamma_v_one", "gamma_v = 1", _validate_gamma_v_one),
        Requirement("beta_one", "beta = 1", _validate_beta_one),
        Requirement("positive_energy", "Configuration energy is positive",
                    _validate_positive_energy),
        Requirement("trace_free_exchange", "Exchange source is trace-free",
                    _validate_trace_free_exchange),
    ]


class RequirementManager:
    """Manages and runs requirements against a theory context."""

    def __init__(self) -> None:
        self._requirements: dict[str, Requirement] = {}

    def add(self, req: Requirement) -> None:
        self._requirements[req.id] = req

    def add_standard(self) -> None:
        for req in build_standard_requirements():
            self.add(req)

    def get(self, id: str) -> Requirement:
        return self._requirements[id]

    def validate(self, id: str, ctx: TheoryContext) -> ValidationResult:
        return self._requirements[id].validate(ctx)

    def validate_all(self, ctx: TheoryContext) -> list[ValidationResult]:
        return [req.validate(ctx) for req in self._requirements.values()]

    def list(self) -> list[Requirement]:
        return list(self._requirements.values())

    def summary(self, results: list[ValidationResult]) -> str:
        lines = ["Validation Results:"]
        for r in results:
            icon = {"pass": "+", "fail": "X", "assumed": "~", "undetermined": "?"}
            lines.append(f"  [{icon.get(r.status, '?')}] {r.requirement_id}: {r.message}")
        return "\n".join(lines)
