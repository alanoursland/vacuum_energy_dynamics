"""Structure analyzer: core analysis engine for candidate vacuum structures.

Implements the five algorithms from the design:
1. Induced source projection
2. Source classification
3. Conditional trace-free solve
4. Creation trace test
5. Full chain validation
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import sympy

from vacuumforge.core.simplify import is_zero
from vacuumforge.core.status import SourceClass
from vacuumforge.modes.sources import classify_source
from vacuumforge.structure_search.constraints import (
    check_traceful_condition,
    solve_trace_free_conditions,
)
from vacuumforge.structure_search.operators import SourceOperator
from vacuumforge.structure_search.results import (
    InducedModeSource,
    StructureAnalysisResult,
    StructureStatus,
)
from vacuumforge.structure_search.structure import VacuumStructure

if TYPE_CHECKING:
    from vacuumforge.core.context import TheoryContext


class StructureAnalyzer:
    """Analyzes candidate vacuum structures for trace-free exchange.

    Given a VacuumStructure, projects source operators through the
    projection map, classifies induced sources, solves for conditions,
    detects assumption leaks, and optionally runs downstream validation.
    """

    def analyze(
        self,
        structure: VacuumStructure,
        ctx: TheoryContext | None = None,
    ) -> StructureAnalysisResult:
        """Run full analysis on a candidate structure.

        Args:
            structure: The candidate vacuum structure.
            ctx: Optional TheoryContext for downstream validation.

        Returns:
            StructureAnalysisResult with full classification.
        """
        exchange_results = []
        creation_results = []

        # Analyze exchange operators
        for op in structure.exchange_operators:
            induced = self._project_operator(structure, op)
            induced = self._classify_induced(induced, op)
            induced = self._check_leak(induced, structure)
            exchange_results.append(induced)

        # Analyze creation operators
        for op in structure.creation_operators:
            induced = self._project_operator(structure, op)
            induced = self._classify_induced(induced, op)
            creation_results.append(induced)

        # Build overall result
        result = self._build_result(structure, exchange_results, creation_results)

        # Downstream validation if context provided
        if ctx is not None and result.derived_trace_free_exchange:
            self._run_downstream(result, ctx)

        return result

    def _project_operator(
        self,
        structure: VacuumStructure,
        operator: SourceOperator,
    ) -> InducedModeSource:
        """Algorithm 1: Induced source projection.

        Project a source operator through the projection map to get
        induced metric sources.
        """
        # Compute induced (J_a, J_b) via Jacobian projection
        J_a, J_b = structure.projection.induced_source(operator.deltas)

        # Decompose to mode sources
        J_kappa = sympy.simplify(J_a + J_b)
        J_sigma = sympy.simplify(J_a - J_b)

        return InducedModeSource(
            structure_id=structure.id,
            operator_id=operator.id,
            operator_kind=operator.kind,
            J_a=J_a,
            J_b=J_b,
            J_kappa=J_kappa,
            J_sigma=J_sigma,
            classification="undetermined",
        )

    def _classify_induced(
        self,
        induced: InducedModeSource,
        operator: SourceOperator,
    ) -> InducedModeSource:
        """Algorithm 2 & 3: Classify the induced source and solve conditions.

        Determines whether the source is trace-free, pure trace, mixed,
        zero, or conditionally trace-free.
        """
        # Use existing source classification
        source_class = classify_source(induced.J_kappa, induced.J_sigma)

        if source_class == SourceClass.TRACE_FREE:
            induced.classification = "trace_free"
            induced.status = StructureStatus.DERIVED
            induced.notes.append(
                "J_kappa = 0 follows structurally from the projection and operator."
            )
        elif source_class == SourceClass.PURE_TRACE:
            induced.classification = "pure_trace"
            if operator.kind == "creation":
                induced.status = StructureStatus.DERIVED
                induced.notes.append("Creation source is pure trace (traceful).")
            else:
                induced.status = StructureStatus.FAILED
                induced.notes.append("Exchange source is pure trace — only kappa is sourced.")
        elif source_class == SourceClass.MIXED:
            induced.classification = "mixed"
            if operator.kind == "exchange":
                induced.status = StructureStatus.FAILED
                induced.notes.append(
                    f"Exchange sources both kappa and sigma: "
                    f"J_kappa = {induced.J_kappa}"
                )
            else:
                induced.status = StructureStatus.DERIVED
                induced.notes.append("Creation source has both trace and shear components.")
        elif source_class == SourceClass.ZERO:
            induced.classification = "zero"
            induced.status = StructureStatus.FAILED
            induced.notes.append("Source operator produces no metric response.")
        else:
            # Undetermined — attempt conditional solve
            induced = self._try_conditional_solve(induced, operator)

        return induced

    def _try_conditional_solve(
        self,
        induced: InducedModeSource,
        operator: SourceOperator,
    ) -> InducedModeSource:
        """Algorithm 3: Conditional trace-free solve.

        When J_kappa is not identically zero, find coefficient conditions
        that would make it zero.
        """
        if operator.kind == "exchange":
            constraint_result = solve_trace_free_conditions(
                induced.J_kappa,
                operator.source_symbols,
            )
            if constraint_result.solvable and constraint_result.conditions:
                induced.classification = "conditional_trace_free"
                induced.status = StructureStatus.CONDITIONAL
                induced.conditions = [
                    c for c in constraint_result.conditions if isinstance(c, sympy.Basic)
                ]
                induced.notes.extend(constraint_result.notes)
            elif constraint_result.solvable and not constraint_result.conditions:
                induced.classification = "trace_free"
                induced.status = StructureStatus.DERIVED
                induced.notes.extend(constraint_result.notes)
            else:
                induced.classification = "undetermined"
                induced.status = StructureStatus.UNDETERMINED
                induced.notes.extend(constraint_result.notes)
        elif operator.kind == "creation":
            # Algorithm 4: Creation trace test
            constraint_result = check_traceful_condition(
                induced.J_kappa,
                operator.source_symbols,
            )
            if constraint_result.solvable:
                induced.classification = "traceful"
                induced.status = StructureStatus.DERIVED
            else:
                induced.classification = "undetermined"
                induced.status = StructureStatus.UNDETERMINED
            induced.notes.extend(constraint_result.notes)
        else:
            induced.classification = "undetermined"
            induced.status = StructureStatus.UNDETERMINED

        return induced

    def _check_leak(
        self,
        induced: InducedModeSource,
        structure: VacuumStructure,
    ) -> InducedModeSource:
        """Check for assumption leaks in exchange operator results.

        Detects when:
        1. The projection map itself enforces a+b = 0.
        2. The Jacobian sum row is all zeros (a+b independent of all variables).
        3. The exchange operator directly zeroes out the variable(s) that
           contribute to J_kappa, making trace-free exchange tautological.
        """
        if induced.classification != "trace_free":
            return induced

        proj = structure.projection

        # Check 1: projection map enforces a + b = constant
        a_plus_b = sympy.simplify(proj.a_expr + proj.b_expr)
        if a_plus_b == 0 or (a_plus_b.is_number and a_plus_b.is_zero):
            induced.notes.append(
                "LEAK WARNING: Projection map enforces a + b = 0 "
                "(reciprocal scaling built into projection)."
            )
            induced.status = StructureStatus.TAUTOLOGICAL

        jac = proj.jacobian()
        # Check 2: sum of Jacobian rows is all zeros
        sum_row = jac.row(0) + jac.row(1)
        all_sum_zero = all(
            is_zero(sum_row[i]) is True for i in range(sum_row.cols)
        )
        if all_sum_zero:
            induced.notes.append(
                "LEAK WARNING: Projection sum (a+b) is independent of all variables. "
                "Trace-free exchange is structurally guaranteed by the projection map."
            )
            induced.status = StructureStatus.TAUTOLOGICAL

        # Check 3: exchange operator directly zeroes out trace-contributing variables
        # For each variable, check if it contributes to J_kappa (nonzero sum-row entry).
        # If exchange explicitly sets delta=0 for ALL variables that contribute to J_kappa,
        # then trace-free exchange is tautologically assumed via the operator definition.
        if induced.status != StructureStatus.TAUTOLOGICAL:
            # Find the operator that produced this induced source
            op = None
            for o in structure.exchange_operators:
                if o.id == induced.operator_id:
                    op = o
                    break

            if op is not None:
                trace_contributors = []
                for i, q in enumerate(proj.variables):
                    if not is_zero(sum_row[i]) is True:
                        trace_contributors.append(q)

                if trace_contributors:
                    all_trace_zeroed = all(
                        is_zero(op.deltas.get(q, sympy.Integer(0))) is True
                        for q in trace_contributors
                    )
                    if all_trace_zeroed:
                        induced.notes.append(
                            "LEAK WARNING: Exchange operator explicitly zeroes all "
                            "trace-contributing variables. Trace-free exchange is "
                            "assumed via the operator definition, not derived from "
                            "deeper structure."
                        )
                        induced.status = StructureStatus.TAUTOLOGICAL

        return induced

    def _build_result(
        self,
        structure: VacuumStructure,
        exchange_results: list[InducedModeSource],
        creation_results: list[InducedModeSource],
    ) -> StructureAnalysisResult:
        """Build the overall analysis result from individual operator results."""
        result = StructureAnalysisResult(
            structure_id=structure.id,
            exchange_results=exchange_results,
            creation_results=creation_results,
        )

        # Check if all exchange operators are trace-free
        exchange_statuses = [r.status for r in exchange_results]
        creation_statuses = [r.status for r in creation_results]

        # Determine derived_trace_free_exchange
        if exchange_results:
            all_trace_free = all(
                r.classification in ("trace_free",)
                for r in exchange_results
            )
            any_tautological = any(
                r.status == StructureStatus.TAUTOLOGICAL
                for r in exchange_results
            )
            any_conditional = any(
                r.status == StructureStatus.CONDITIONAL
                for r in exchange_results
            )
            any_failed = any(
                r.status == StructureStatus.FAILED
                for r in exchange_results
            )

            if all_trace_free and not any_tautological:
                result.derived_trace_free_exchange = True
            elif any_tautological:
                result.derived_trace_free_exchange = False
                result.leak_warnings.extend(
                    note for r in exchange_results for note in r.notes
                    if "LEAK WARNING" in note
                )

        # Determine derived_traceful_creation
        if creation_results:
            all_traceful = all(
                r.classification in ("pure_trace", "traceful", "mixed")
                for r in creation_results
            )
            result.derived_traceful_creation = all_traceful

        # Collect conditions
        for r in exchange_results + creation_results:
            result.conditions.extend(r.conditions)

        # Collect failures
        for r in exchange_results:
            if r.status == StructureStatus.FAILED:
                result.failures.append(
                    f"Exchange operator '{r.operator_id}': {r.classification}"
                )
        for r in creation_results:
            if r.status == StructureStatus.FAILED:
                result.failures.append(
                    f"Creation operator '{r.operator_id}': {r.classification}"
                )

        # Determine summary status
        if result.failures:
            result.summary_status = StructureStatus.FAILED
        elif result.leak_warnings:
            result.summary_status = StructureStatus.TAUTOLOGICAL
        elif result.conditions:
            result.summary_status = StructureStatus.CONDITIONAL
        elif result.derived_trace_free_exchange and result.derived_traceful_creation:
            result.summary_status = StructureStatus.DERIVED
        elif result.derived_trace_free_exchange:
            result.summary_status = StructureStatus.DERIVED
            if not creation_results:
                result.notes.append("No creation operators defined to test.")
        elif not exchange_results:
            result.summary_status = StructureStatus.UNDETERMINED
            result.notes.append("No exchange operators defined.")
        else:
            result.summary_status = StructureStatus.UNDETERMINED

        return result

    def _run_downstream(
        self,
        result: StructureAnalysisResult,
        ctx: TheoryContext,
    ) -> None:
        """Algorithm 5: Full chain validation.

        If trace-free exchange is derived, feed it into the existing
        VacuumForge pipeline.
        """
        ms = ctx._mode_symbols
        if ms is None:
            result.notes.append(
                "Cannot run downstream validation: no standard symbols defined."
            )
            return

        # Get the first exchange result's J_sigma
        exchange = result.exchange_results[0]

        # Register derived source in context
        source_id = f"derived_exchange_from_{result.structure_id}"
        if not ctx.sources.has(source_id):
            ctx.sources.add_modes(
                id=source_id,
                J_kappa=sympy.Integer(0),
                J_sigma=exchange.J_sigma,
                source_type="exchange",
                description=(
                    f"Trace-free exchange derived from structure '{result.structure_id}'"
                ),
            )
            # Mark as derived, not assumed
            src = ctx.sources.get(source_id)
            src.assumed_trace_free = False

        result.notes.append(
            f"Downstream: derived source '{source_id}' registered with J_kappa=0."
        )
