"""Source decomposition and classification.

Decomposes sources between (J_a, J_b) and (J_kappa, J_sigma),
and classifies as trace-free, pure-trace, mixed, or zero.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import sympy

from vacuumforge.core.simplify import is_zero
from vacuumforge.core.status import SourceClass


@dataclass
class SourceRecord:
    """A source definition with its components and classification."""

    id: str
    J_a: sympy.Basic | None = None
    J_b: sympy.Basic | None = None
    J_kappa: sympy.Basic | None = None
    J_sigma: sympy.Basic | None = None
    source_type: str = "general"  # exchange, creation, general
    description: str | None = None
    classification: SourceClass = SourceClass.UNDETERMINED
    assumed_trace_free: bool = False


def decompose_ab_to_modes(
    J_a: sympy.Basic, J_b: sympy.Basic
) -> tuple[sympy.Basic, sympy.Basic]:
    """Decompose (J_a, J_b) into (J_kappa, J_sigma)."""
    J_kappa = sympy.simplify(J_a + J_b)
    J_sigma = sympy.simplify(J_a - J_b)
    return J_kappa, J_sigma


def decompose_modes_to_ab(
    J_kappa: sympy.Basic, J_sigma: sympy.Basic
) -> tuple[sympy.Basic, sympy.Basic]:
    """Decompose (J_kappa, J_sigma) into (J_a, J_b)."""
    J_a = sympy.simplify((J_kappa + J_sigma) / 2)
    J_b = sympy.simplify((J_kappa - J_sigma) / 2)
    return J_a, J_b


def classify_source(J_kappa: sympy.Basic, J_sigma: sympy.Basic) -> SourceClass:
    """Classify a source by its trace/shear content."""
    kappa_zero = is_zero(J_kappa)
    sigma_zero = is_zero(J_sigma)

    if kappa_zero is True and sigma_zero is True:
        return SourceClass.ZERO
    if kappa_zero is True and sigma_zero is not True:
        return SourceClass.TRACE_FREE
    if sigma_zero is True and kappa_zero is not True:
        return SourceClass.PURE_TRACE
    if kappa_zero is False and sigma_zero is False:
        return SourceClass.MIXED
    return SourceClass.UNDETERMINED


class SourceManager:
    """Manages source definitions for a theory context."""

    def __init__(self) -> None:
        self._records: dict[str, SourceRecord] = {}

    def add_ab(
        self,
        id: str,
        J_a: sympy.Basic,
        J_b: sympy.Basic,
        source_type: str = "general",
        description: str | None = None,
    ) -> SourceRecord:
        """Define a source in (J_a, J_b) components."""
        J_kappa, J_sigma = decompose_ab_to_modes(J_a, J_b)
        classification = classify_source(J_kappa, J_sigma)
        record = SourceRecord(
            id=id, J_a=J_a, J_b=J_b,
            J_kappa=J_kappa, J_sigma=J_sigma,
            source_type=source_type,
            description=description,
            classification=classification,
        )
        self._records[id] = record
        return record

    def add_modes(
        self,
        id: str,
        J_kappa: sympy.Basic,
        J_sigma: sympy.Basic,
        source_type: str = "general",
        description: str | None = None,
    ) -> SourceRecord:
        """Define a source in (J_kappa, J_sigma) mode components."""
        J_a, J_b = decompose_modes_to_ab(J_kappa, J_sigma)
        classification = classify_source(J_kappa, J_sigma)

        # Check if trace-free was directly declared
        assumed_trace_free = False
        if is_zero(J_kappa) is True and isinstance(J_kappa, (int, float, sympy.Integer)):
            assumed_trace_free = True

        record = SourceRecord(
            id=id, J_a=J_a, J_b=J_b,
            J_kappa=J_kappa, J_sigma=J_sigma,
            source_type=source_type,
            description=description,
            classification=classification,
            assumed_trace_free=assumed_trace_free,
        )
        self._records[id] = record
        return record

    def exchange_trace_free(
        self, J_sigma: sympy.Basic, id: str = "exchange", description: str | None = None
    ) -> SourceRecord:
        """Create a trace-free exchange source (J_kappa=0)."""
        record = self.add_modes(
            id=id, J_kappa=sympy.Integer(0), J_sigma=J_sigma,
            source_type="exchange",
            description=description or "Trace-free exchange source",
        )
        record.assumed_trace_free = True
        return record

    def creation_uniform(
        self, J_kappa: sympy.Basic, id: str = "creation", description: str | None = None
    ) -> SourceRecord:
        """Create a pure-trace creation source (J_sigma=0)."""
        return self.add_modes(
            id=id, J_kappa=J_kappa, J_sigma=sympy.Integer(0),
            source_type="creation",
            description=description or "Uniform creation source",
        )

    def get(self, id: str) -> SourceRecord:
        return self._records[id]

    def has(self, id: str) -> bool:
        return id in self._records

    def list(self) -> list[SourceRecord]:
        return list(self._records.values())

    def classify(self, id: str) -> SourceClass:
        return self._records[id].classification

    def summary(self) -> str:
        lines = ["Sources:"]
        for r in self._records.values():
            desc = f" — {r.description}" if r.description else ""
            lines.append(f"  [{r.id}] {r.source_type} ({r.classification.value}){desc}")
            lines.append(f"    J_kappa = {r.J_kappa}, J_sigma = {r.J_sigma}")
        return "\n".join(lines)
