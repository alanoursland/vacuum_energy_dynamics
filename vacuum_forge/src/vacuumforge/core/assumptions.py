"""Assumption management for VacuumForge."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import sympy


@dataclass
class AssumptionRecord:
    """An explicitly declared assumption."""

    id: str
    expression: sympy.Basic
    description: str | None = None
    status: str = "assumption"
    dependencies: list[str] = field(default_factory=list)
    assumption_type: str = "equation"  # equation, inequality, substitution, boundary

    def as_substitution(self) -> dict[sympy.Basic, sympy.Basic] | None:
        """If this is an Eq assumption, return a substitution dict {lhs: rhs}."""
        if isinstance(self.expression, sympy.Eq):
            return {self.expression.lhs: self.expression.rhs}
        return None


class AssumptionManager:
    """Manages explicit assumptions for a theory context."""

    def __init__(self) -> None:
        self._records: dict[str, AssumptionRecord] = {}

    def add(
        self,
        id: str,
        expression: sympy.Basic,
        description: str | None = None,
        status: str = "assumption",
        dependencies: list[str] | None = None,
        assumption_type: str | None = None,
    ) -> AssumptionRecord:
        if assumption_type is None:
            if isinstance(expression, sympy.Eq):
                assumption_type = "equation"
            elif isinstance(expression, sympy.Rel):
                assumption_type = "inequality"
            else:
                assumption_type = "equation"

        record = AssumptionRecord(
            id=id,
            expression=expression,
            description=description,
            status=status,
            dependencies=dependencies or [],
            assumption_type=assumption_type,
        )
        self._records[id] = record
        return record

    def remove(self, id: str) -> None:
        self._records.pop(id, None)

    def get(self, id: str) -> AssumptionRecord:
        return self._records[id]

    def has(self, id: str) -> bool:
        return id in self._records

    def active(self) -> list[AssumptionRecord]:
        return list(self._records.values())

    def ids(self) -> list[str]:
        return list(self._records.keys())

    def substitution_map(self) -> dict[sympy.Basic, sympy.Basic]:
        """Build a combined substitution map from all equation assumptions."""
        subs = {}
        for record in self._records.values():
            s = record.as_substitution()
            if s:
                subs.update(s)
        return subs

    def apply(self, expr: sympy.Basic, max_iterations: int = 10) -> sympy.Basic:
        """Apply all active substitution assumptions to an expression.

        Iterates until the expression stabilizes, handling chained
        substitutions like B = 1/A, A = exp(Phi/c^2).
        """
        subs = self.substitution_map()
        for _ in range(max_iterations):
            new_expr = expr.subs(subs)
            if new_expr == expr:
                break
            expr = new_expr
        return expr

    def apply_specific(self, expr: sympy.Basic, ids: list[str]) -> sympy.Basic:
        """Apply only named assumptions to an expression."""
        subs = {}
        for aid in ids:
            record = self._records[aid]
            s = record.as_substitution()
            if s:
                subs.update(s)
        return expr.subs(subs)

    def contains_expression(self, target: sympy.Basic) -> list[str]:
        """Find assumptions whose expression matches or is equivalent to target."""
        matches = []
        for record in self._records.values():
            expr = record.expression
            if isinstance(expr, sympy.Eq):
                # Check if the equation is equivalent to the target
                diff = sympy.simplify(expr.lhs - expr.rhs)
                target_diff = _normalize_target(target)
                if target_diff is not None and sympy.simplify(diff - target_diff) == 0:
                    matches.append(record.id)
            elif sympy.simplify(expr - target) == 0:
                matches.append(record.id)
        return matches

    def summary(self) -> str:
        lines = ["Assumptions:"]
        for record in self._records.values():
            desc = f" — {record.description}" if record.description else ""
            lines.append(f"  [{record.id}] {sympy.pretty(record.expression)}{desc}")
        return "\n".join(lines)


def _normalize_target(target: sympy.Basic) -> sympy.Basic | None:
    """Normalize a target expression to lhs - rhs form."""
    if isinstance(target, sympy.Eq):
        return sympy.simplify(target.lhs - target.rhs)
    return None
