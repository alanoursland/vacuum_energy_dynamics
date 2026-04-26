"""Result data models for structure search analysis."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

import sympy


class StructureStatus(str, Enum):
    """Classification of a structure search result."""

    DERIVED = "derived"
    ASSUMED = "assumed"
    CONDITIONAL = "conditional"
    FAILED = "failed"
    UNDETERMINED = "undetermined"
    TAUTOLOGICAL = "tautological"


@dataclass
class InducedModeSource:
    """Result of projecting a source operator through a projection map.

    Contains the induced metric sources J_a, J_b, J_kappa, J_sigma
    and the classification of the result.
    """

    structure_id: str
    operator_id: str
    operator_kind: str
    J_a: sympy.Expr
    J_b: sympy.Expr
    J_kappa: sympy.Expr
    J_sigma: sympy.Expr
    classification: str  # trace_free, pure_trace, mixed, zero, undetermined
    conditions: list[sympy.Basic] = field(default_factory=list)
    dependencies: list[str] = field(default_factory=list)
    status: StructureStatus = StructureStatus.UNDETERMINED
    notes: list[str] = field(default_factory=list)

    def summary(self) -> str:
        lines = [
            f"Operator: {self.operator_id} ({self.operator_kind})",
            f"  J_a = {self.J_a}",
            f"  J_b = {self.J_b}",
            f"  J_kappa = {self.J_kappa}",
            f"  J_sigma = {self.J_sigma}",
            f"  Classification: {self.classification}",
            f"  Status: {self.status.value}",
        ]
        if self.conditions:
            lines.append(f"  Conditions: {self.conditions}")
        if self.notes:
            for note in self.notes:
                lines.append(f"  Note: {note}")
        return "\n".join(lines)


@dataclass
class StructureAnalysisResult:
    """Full analysis result for a candidate vacuum structure."""

    structure_id: str
    exchange_results: list[InducedModeSource] = field(default_factory=list)
    creation_results: list[InducedModeSource] = field(default_factory=list)
    summary_status: StructureStatus = StructureStatus.UNDETERMINED
    derived_trace_free_exchange: bool = False
    derived_traceful_creation: bool = False
    conditions: list[sympy.Basic] = field(default_factory=list)
    failures: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)
    leak_warnings: list[str] = field(default_factory=list)

    def summary(self) -> str:
        lines = [
            f"Structure: {self.structure_id}",
            f"  Status: {self.summary_status.value}",
            f"  Trace-free exchange derived: {self.derived_trace_free_exchange}",
            f"  Traceful creation derived: {self.derived_traceful_creation}",
        ]
        if self.conditions:
            lines.append(f"  Conditions: {self.conditions}")
        if self.failures:
            for f in self.failures:
                lines.append(f"  Failure: {f}")
        if self.leak_warnings:
            for w in self.leak_warnings:
                lines.append(f"  Leak warning: {w}")
        if self.notes:
            for n in self.notes:
                lines.append(f"  Note: {n}")

        lines.append("")
        lines.append("Exchange operators:")
        for r in self.exchange_results:
            lines.append(r.summary())

        lines.append("")
        lines.append("Creation operators:")
        for r in self.creation_results:
            lines.append(r.summary())

        return "\n".join(lines)
