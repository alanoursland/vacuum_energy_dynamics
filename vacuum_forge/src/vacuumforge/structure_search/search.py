"""Search engine for systematic exploration of structure families."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

import sympy

from vacuumforge.structure_search.analyzer import StructureAnalyzer
from vacuumforge.structure_search.operators import SourceOperator
from vacuumforge.structure_search.projection import ProjectionMap
from vacuumforge.structure_search.results import (
    StructureAnalysisResult,
    StructureStatus,
)
from vacuumforge.structure_search.structure import VacuumStructure

if TYPE_CHECKING:
    from vacuumforge.core.context import TheoryContext


@dataclass
class FamilySearchResult:
    """Result of searching over a parameterized family of structures."""

    family_id: str
    candidates_analyzed: int
    trace_free_derived: list[StructureAnalysisResult] = field(default_factory=list)
    conditional: list[StructureAnalysisResult] = field(default_factory=list)
    failed: list[StructureAnalysisResult] = field(default_factory=list)
    tautological: list[StructureAnalysisResult] = field(default_factory=list)
    conditions_for_trace_free: list[sympy.Basic] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    def summary(self) -> str:
        lines = [
            f"Family Search: {self.family_id}",
            f"  Candidates analyzed: {self.candidates_analyzed}",
            f"  Trace-free derived: {len(self.trace_free_derived)}",
            f"  Conditional: {len(self.conditional)}",
            f"  Failed: {len(self.failed)}",
            f"  Tautological: {len(self.tautological)}",
        ]
        if self.conditions_for_trace_free:
            lines.append(f"  Conditions for trace-free exchange:")
            for c in self.conditions_for_trace_free:
                lines.append(f"    {c}")
        if self.notes:
            for n in self.notes:
                lines.append(f"  Note: {n}")
        return "\n".join(lines)


class StructureSearchEngine:
    """Systematic search over candidate vacuum structures.

    Supports:
    - Manual single-structure analysis
    - Family parameter search with symbolic coefficient solving
    - Enumeration over discrete candidate sets
    """

    def __init__(self) -> None:
        self._analyzer = StructureAnalyzer()
        self._results: dict[str, StructureAnalysisResult] = {}

    def analyze(
        self,
        structure: VacuumStructure,
        ctx: TheoryContext | None = None,
    ) -> StructureAnalysisResult:
        """Analyze a single candidate structure."""
        result = self._analyzer.analyze(structure, ctx)
        self._results[structure.id] = result
        return result

    def search_family(
        self,
        family: VacuumStructure,
        require_exchange_trace_free: bool = True,
        require_creation_traceful: bool = True,
        ctx: TheoryContext | None = None,
    ) -> FamilySearchResult:
        """Search a parameterized family for trace-free exchange conditions.

        Analyzes the family's symbolic structure and extracts coefficient
        conditions for trace-free exchange and traceful creation.
        """
        result = self._analyzer.analyze(family, ctx)
        self._results[family.id] = result

        family_result = FamilySearchResult(
            family_id=family.id,
            candidates_analyzed=1,
        )

        # Classify the result
        if result.summary_status == StructureStatus.DERIVED:
            family_result.trace_free_derived.append(result)
        elif result.summary_status == StructureStatus.CONDITIONAL:
            family_result.conditional.append(result)
            family_result.conditions_for_trace_free = list(result.conditions)
        elif result.summary_status == StructureStatus.TAUTOLOGICAL:
            family_result.tautological.append(result)
        elif result.summary_status == StructureStatus.FAILED:
            family_result.failed.append(result)

        # Extract conditions summary
        if result.conditions:
            family_result.notes.append(
                f"Exchange trace-free requires: {result.conditions}"
            )

        if require_creation_traceful and not result.derived_traceful_creation:
            if result.creation_results:
                family_result.notes.append(
                    "Creation tracefulness not derived."
                )

        return family_result

    def enumerate_sign_patterns(
        self,
        n_vars: int = 2,
        ctx: TheoryContext | None = None,
    ) -> FamilySearchResult:
        """Enumerate all sign-pattern structures for n variables.

        Tests all combinations of exchange deltas in {-1, 0, +1}
        with a direct projection (a = q_1, b = q_2 for 2D).
        """
        if n_vars != 2:
            return FamilySearchResult(
                family_id="sign_patterns",
                candidates_analyzed=0,
                notes=[f"Sign pattern enumeration only supports 2 variables, got {n_vars}."],
            )

        q1, q2 = sympy.symbols("q_1 q_2", real=True)
        S, C = sympy.symbols("S C")

        projection = ProjectionMap(
            id="direct_2d",
            variables=[q1, q2],
            a_expr=q1,
            b_expr=q2,
        )

        creation = SourceOperator(
            id="symmetric_creation",
            kind="creation",
            deltas={q1: C, q2: C},
            source_symbols=[C],
        )

        family_result = FamilySearchResult(
            family_id="sign_patterns_2d",
            candidates_analyzed=0,
        )

        signs = [sympy.Integer(-1), sympy.Integer(0), sympy.Integer(1)]
        for s1 in signs:
            for s2 in signs:
                if s1 == 0 and s2 == 0:
                    continue  # Skip trivial zero operator

                exchange = SourceOperator(
                    id=f"exchange_({s1},{s2})",
                    kind="exchange",
                    deltas={q1: s1 * S, q2: s2 * S},
                    source_symbols=[S],
                )

                structure = VacuumStructure(
                    id=f"sign_pattern_({s1},{s2})",
                    variables=[q1, q2],
                    projection=projection,
                    exchange_operators=[exchange],
                    creation_operators=[creation],
                )

                result = self._analyzer.analyze(structure, ctx)
                self._results[structure.id] = result
                family_result.candidates_analyzed += 1

                if result.summary_status == StructureStatus.DERIVED:
                    family_result.trace_free_derived.append(result)
                elif result.summary_status == StructureStatus.TAUTOLOGICAL:
                    family_result.tautological.append(result)
                elif result.summary_status == StructureStatus.FAILED:
                    family_result.failed.append(result)

        family_result.notes.append(
            f"Tested {family_result.candidates_analyzed} sign patterns."
        )
        return family_result

    def get_result(self, structure_id: str) -> StructureAnalysisResult | None:
        return self._results.get(structure_id)

    def all_results(self) -> list[StructureAnalysisResult]:
        return list(self._results.values())

    def summary(self) -> str:
        lines = ["Structure Search Results:"]
        for sid, r in self._results.items():
            lines.append(f"  [{sid}] {r.summary_status.value}")
            if r.derived_trace_free_exchange:
                lines.append("    -> trace-free exchange derived")
            if r.derived_traceful_creation:
                lines.append("    -> traceful creation derived")
            if r.conditions:
                lines.append(f"    conditions: {r.conditions}")
            if r.failures:
                for f in r.failures:
                    lines.append(f"    failure: {f}")
        return "\n".join(lines)
