"""Energy functional definition and analysis.

Supports algebraic energy functionals over mode variables,
stationary condition derivation, and equilibrium solving.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import sympy


@dataclass
class EnergyFunctional:
    """A symbolic energy functional over vacuum modes."""

    id: str
    expression: sympy.Basic
    variables: list[sympy.Basic]
    description: str | None = None
    sources: list[str] = field(default_factory=list)
    dependencies: list[str] = field(default_factory=list)


@dataclass
class StationaryResult:
    """Result of solving stationary conditions dE/dvar = 0."""

    equations: list[sympy.Basic]
    solutions: list[dict[sympy.Basic, sympy.Basic]]
    dependencies: list[str] = field(default_factory=list)


class EnergyManager:
    """Manages energy functionals for a theory context."""

    def __init__(self) -> None:
        self._functionals: dict[str, EnergyFunctional] = {}

    def add(
        self,
        id: str,
        expression: sympy.Basic,
        variables: list[sympy.Basic],
        description: str | None = None,
        sources: list[str] | None = None,
        dependencies: list[str] | None = None,
    ) -> EnergyFunctional:
        func = EnergyFunctional(
            id=id,
            expression=expression,
            variables=variables,
            description=description,
            sources=sources or [],
            dependencies=dependencies or [],
        )
        self._functionals[id] = func
        return func

    def get(self, id: str) -> EnergyFunctional:
        return self._functionals[id]

    def has(self, id: str) -> bool:
        return id in self._functionals

    def stationary_conditions(self, id: str) -> list[sympy.Eq]:
        """Derive dE/dvar = 0 for each variable."""
        func = self._functionals[id]
        return [
            sympy.Eq(sympy.diff(func.expression, var), 0)
            for var in func.variables
        ]

    def solve_stationary(
        self,
        id: str,
        extra_subs: dict[sympy.Basic, sympy.Basic] | None = None,
    ) -> StationaryResult:
        """Solve stationary conditions for equilibrium values."""
        func = self._functionals[id]
        equations = [sympy.diff(func.expression, var) for var in func.variables]
        solutions = sympy.solve(equations, func.variables, dict=True)

        if extra_subs and solutions:
            solutions = [
                {k: sympy.simplify(v.subs(extra_subs)) for k, v in sol.items()}
                for sol in solutions
            ]

        return StationaryResult(
            equations=[sympy.Eq(eq, 0) for eq in equations],
            solutions=solutions,
            dependencies=func.dependencies,
        )

    def quadratic_modes(
        self,
        C_kappa: sympy.Basic,
        C_sigma: sympy.Basic,
        kappa: sympy.Basic,
        sigma: sympy.Basic,
        cross: sympy.Basic = sympy.Integer(0),
        id: str = "quadratic_mode_energy",
    ) -> EnergyFunctional:
        """Create a quadratic energy in mode variables."""
        E = C_kappa * kappa**2 + C_sigma * sigma**2 + cross * kappa * sigma
        return self.add(id, E, [kappa, sigma], description="Quadratic mode energy")

    def source_coupled(
        self,
        C_kappa: sympy.Basic,
        C_sigma: sympy.Basic,
        J_kappa: sympy.Basic,
        J_sigma: sympy.Basic,
        kappa: sympy.Basic,
        sigma: sympy.Basic,
        id: str = "source_coupled_energy",
    ) -> EnergyFunctional:
        """Create source-coupled quadratic energy: C*var^2 - J*var."""
        E = (C_kappa * kappa**2 + C_sigma * sigma**2
             - J_kappa * kappa - J_sigma * sigma)
        return self.add(
            id, E, [kappa, sigma],
            description="Source-coupled quadratic mode energy",
        )

    def list(self) -> list[EnergyFunctional]:
        return list(self._functionals.values())

    def summary(self) -> str:
        lines = ["Energy Functionals:"]
        for f in self._functionals.values():
            desc = f" — {f.description}" if f.description else ""
            lines.append(f"  [{f.id}]{desc}")
            lines.append(f"    E = {f.expression}")
        return "\n".join(lines)
