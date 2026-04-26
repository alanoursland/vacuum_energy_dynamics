"""VacuumStructure: candidate mathematical structure for vacuum configuration."""

from __future__ import annotations

from dataclasses import dataclass, field

import sympy

from vacuumforge.structure_search.operators import SourceOperator
from vacuumforge.structure_search.projection import ProjectionMap


@dataclass
class VacuumStructure:
    """A candidate mathematical structure for the vacuum.

    Contains pre-mode degrees of freedom, a projection map into
    metric scale variables, source operators for exchange and creation,
    and optional constraints and symmetry rules.
    """

    id: str
    variables: list[sympy.Symbol]
    projection: ProjectionMap
    exchange_operators: list[SourceOperator] = field(default_factory=list)
    creation_operators: list[SourceOperator] = field(default_factory=list)
    constraints: list[sympy.Basic] = field(default_factory=list)
    symmetries: list[str] = field(default_factory=list)
    description: str | None = None
    status: str = "candidate"

    def all_operators(self) -> list[SourceOperator]:
        """Return all exchange and creation operators."""
        return self.exchange_operators + self.creation_operators
