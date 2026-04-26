"""Model comparison tools for VacuumForge (M26).

Compare candidate structures side by side, producing structured
summaries and comparison reports.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any

import sympy

if TYPE_CHECKING:
    from vacuumforge.core.context import TheoryContext
    from vacuumforge.requirements.validators import ValidationResult


@dataclass
class ModelSummary:
    """Summary of a single candidate model."""

    name: str
    assumptions: list[str] = field(default_factory=list)
    source_classification: str = "undetermined"
    reciprocal_status: str = "undetermined"
    gamma_v: str = "undetermined"
    beta: str = "undetermined"
    positivity_status: str = "undetermined"
    exchange_creation_status: str = "undetermined"
    failed_requirements: list[str] = field(default_factory=list)
    undetermined_requirements: list[str] = field(default_factory=list)
    passed_requirements: list[str] = field(default_factory=list)
    assumed_requirements: list[str] = field(default_factory=list)


@dataclass
class ModelComparison:
    """Side-by-side comparison of multiple models."""

    models: list[ModelSummary]
    fields: list[str] = field(default_factory=lambda: [
        "reciprocal_status", "gamma_v", "beta",
        "positivity_status", "source_classification",
        "exchange_creation_status",
    ])

    def to_markdown(self) -> str:
        """Generate a markdown comparison table."""
        lines = ["# Model Comparison", ""]
        if not self.models:
            return "No models to compare."

        # Header
        header = "| Field | " + " | ".join(m.name for m in self.models) + " |"
        sep = "|---|" + "|".join("---" for _ in self.models) + "|"
        lines.extend([header, sep])

        # Rows
        field_labels = {
            "reciprocal_status": "Reciprocal Scaling",
            "gamma_v": "gamma_v",
            "beta": "beta",
            "positivity_status": "Energy Positivity",
            "source_classification": "Source Classification",
            "exchange_creation_status": "Exchange/Creation",
        }
        for f in self.fields:
            label = field_labels.get(f, f)
            vals = [getattr(m, f, "—") for m in self.models]
            lines.append(f"| {label} | " + " | ".join(str(v) for v in vals) + " |")

        # Requirements summary
        lines.extend(["", "## Requirement Summary", ""])
        header2 = "| Requirement Status | " + " | ".join(m.name for m in self.models) + " |"
        lines.extend([header2, sep])

        for status_attr, label in [
            ("passed_requirements", "Passed"),
            ("failed_requirements", "Failed"),
            ("assumed_requirements", "Assumed"),
            ("undetermined_requirements", "Undetermined"),
        ]:
            counts = [str(len(getattr(m, status_attr))) for m in self.models]
            lines.append(f"| {label} | " + " | ".join(counts) + " |")

        return "\n".join(lines)


def summarize_model(ctx: TheoryContext) -> ModelSummary:
    """Build a ModelSummary from a TheoryContext."""
    summary = ModelSummary(name=ctx.name)

    # Assumptions
    summary.assumptions = [a.id for a in ctx.assumptions.active()]

    # Source classification
    sources = ctx.sources.list()
    if sources:
        classifications = [s.classification.value for s in sources]
        summary.source_classification = ", ".join(classifications)

    # Run validation
    results = ctx.requirements.validate_all(ctx)
    rs = {r.requirement_id: r for r in results}

    for r in results:
        if r.status == "pass":
            summary.passed_requirements.append(r.requirement_id)
        elif r.status == "fail":
            summary.failed_requirements.append(r.requirement_id)
        elif r.status == "assumed":
            summary.assumed_requirements.append(r.requirement_id)
        else:
            summary.undetermined_requirements.append(r.requirement_id)

    # Specific fields
    if "reciprocal_scaling" in rs:
        summary.reciprocal_status = rs["reciprocal_scaling"].status

    if "gamma_v_one" in rs:
        r = rs["gamma_v_one"]
        if r.evidence:
            summary.gamma_v = str(r.evidence[0])
        else:
            summary.gamma_v = r.status

    if "beta_one" in rs:
        r = rs["beta_one"]
        if r.evidence:
            summary.beta = str(r.evidence[0])
        else:
            summary.beta = r.status

    if "positive_energy" in rs:
        summary.positivity_status = rs["positive_energy"].status

    if "trace_free_exchange" in rs:
        summary.exchange_creation_status = rs["trace_free_exchange"].status

    return summary


def compare_models(contexts: list[TheoryContext]) -> ModelComparison:
    """Compare multiple TheoryContexts side by side."""
    summaries = [summarize_model(ctx) for ctx in contexts]
    return ModelComparison(models=summaries)
