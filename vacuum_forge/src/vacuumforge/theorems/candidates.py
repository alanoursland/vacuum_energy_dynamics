"""Theorem candidate system (M35).

Supports promotion of repeated symbolic results into theorem candidates
with supporting evidence and known counterexamples.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import sympy


@dataclass
class TheoremCandidate:
    """A candidate theorem with supporting evidence and counterexamples."""

    id: str
    statement: str
    scope: str = "algebraic_prototype"
    assumptions: list[str] = field(default_factory=list)
    supporting_models: list[str] = field(default_factory=list)
    counterexamples: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)
    status: str = "candidate"  # candidate, supported, refuted, established

    @property
    def is_refuted(self) -> bool:
        return len(self.counterexamples) > 0 or self.status == "refuted"

    @property
    def confidence_level(self) -> str:
        if self.is_refuted:
            return "refuted"
        n_support = len(self.supporting_models)
        if n_support == 0:
            return "unverified"
        if n_support < 3:
            return "weak"
        return "moderate"

    def add_support(self, model_name: str, note: str = "") -> None:
        self.supporting_models.append(model_name)
        if note:
            self.notes.append(f"Support from {model_name}: {note}")

    def add_counterexample(self, name: str, note: str = "") -> None:
        self.counterexamples.append(name)
        self.status = "refuted"
        if note:
            self.notes.append(f"Counterexample {name}: {note}")

    def summary(self) -> str:
        lines = [
            f"Theorem Candidate: {self.id}",
            f"  Statement: {self.statement}",
            f"  Scope: {self.scope}",
            f"  Status: {self.status} ({self.confidence_level})",
            f"  Assumptions: {', '.join(self.assumptions) or 'none'}",
            f"  Supporting models: {len(self.supporting_models)}",
            f"  Counterexamples: {len(self.counterexamples)}",
        ]
        return "\n".join(lines)

    def to_markdown(self) -> str:
        lines = [
            f"### {self.id}: {self.statement}",
            "",
            f"**Status**: {self.status} ({self.confidence_level})",
            f"**Scope**: {self.scope}",
            "",
        ]
        if self.assumptions:
            lines.append("**Assumptions**:")
            for a in self.assumptions:
                lines.append(f"- {a}")
            lines.append("")

        if self.supporting_models:
            lines.append("**Supporting Models**:")
            for m in self.supporting_models:
                lines.append(f"- {m}")
            lines.append("")

        if self.counterexamples:
            lines.append("**Counterexamples**:")
            for c in self.counterexamples:
                lines.append(f"- {c}")
            lines.append("")

        if self.notes:
            lines.append("**Notes**:")
            for n in self.notes:
                lines.append(f"- {n}")

        return "\n".join(lines)


class TheoremRegistry:
    """Manages theorem candidates."""

    def __init__(self) -> None:
        self._candidates: dict[str, TheoremCandidate] = {}

    def add(self, candidate: TheoremCandidate) -> None:
        self._candidates[candidate.id] = candidate

    def create(
        self,
        id: str,
        statement: str,
        scope: str = "algebraic_prototype",
        assumptions: list[str] | None = None,
    ) -> TheoremCandidate:
        tc = TheoremCandidate(
            id=id, statement=statement,
            scope=scope, assumptions=assumptions or [],
        )
        self.add(tc)
        return tc

    def get(self, id: str) -> TheoremCandidate:
        return self._candidates[id]

    def has(self, id: str) -> bool:
        return id in self._candidates

    def list(self) -> list[TheoremCandidate]:
        return list(self._candidates.values())

    def active(self) -> list[TheoremCandidate]:
        return [c for c in self._candidates.values() if c.status != "refuted"]

    def refuted(self) -> list[TheoremCandidate]:
        return [c for c in self._candidates.values() if c.status == "refuted"]

    def summary(self) -> str:
        lines = ["Theorem Candidates:"]
        for tc in self._candidates.values():
            lines.append(f"  [{tc.status}] {tc.id}: {tc.statement}")
        return "\n".join(lines)

    def to_markdown(self) -> str:
        lines = ["# Theorem Candidates", ""]
        for tc in self._candidates.values():
            lines.append(tc.to_markdown())
            lines.append("")
        return "\n".join(lines)
