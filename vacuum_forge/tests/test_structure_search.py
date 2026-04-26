"""Tests for the structure_search module.

Covers:
- Projection map computation (linear and nonlinear)
- Source classification through projection
- Leak detection for tautological structures
- Conditional trace-free solve
- Creation tracefulness test
- Candidate structure families
- Family search
- Sign pattern enumeration
- Downstream integration
- Report generation
"""

import sympy
import pytest

from vacuumforge.structure_search.projection import ProjectionMap
from vacuumforge.structure_search.operators import SourceOperator
from vacuumforge.structure_search.structure import VacuumStructure
from vacuumforge.structure_search.results import StructureStatus
from vacuumforge.structure_search.analyzer import StructureAnalyzer
from vacuumforge.structure_search.search import StructureSearchEngine
from vacuumforge.structure_search.constraints import (
    solve_trace_free_conditions,
    check_traceful_condition,
)
from vacuumforge.structure_search.families import (
    direct_mode_basis,
    symmetric_antisymmetric_pair,
    two_channel_exchange,
    general_linear_projection,
    conserved_volume_family,
    mixed_exchange_family,
)
from vacuumforge.structure_search.reports import generate_structure_report


# ============================================================
# Projection tests
# ============================================================


class TestProjectionMap:
    """Test ProjectionMap computation."""

    def test_linear_projection_jacobian(self):
        q1, q2 = sympy.symbols("q1 q2")
        proj = ProjectionMap(
            id="test",
            variables=[q1, q2],
            a_expr=q1 + q2,
            b_expr=q1 - q2,
        )
        jac = proj.jacobian()
        assert jac == sympy.Matrix([[1, 1], [1, -1]])

    def test_linear_projection_is_linear(self):
        q1, q2 = sympy.symbols("q1 q2")
        proj = ProjectionMap(
            id="test",
            variables=[q1, q2],
            a_expr=q1 + q2,
            b_expr=q1 - q2,
        )
        assert proj.is_linear() is True

    def test_nonlinear_projection(self):
        q1, q2 = sympy.symbols("q1 q2", positive=True)
        proj = ProjectionMap(
            id="test_nonlinear",
            variables=[q1, q2],
            a_expr=sympy.log(q1 * q2),
            b_expr=sympy.log(q1 / q2),
        )
        assert proj.is_linear() is False
        jac = proj.jacobian()
        # da/dq1 = 1/q1, da/dq2 = 1/q2
        assert sympy.simplify(jac[0, 0] - 1 / q1) == 0
        assert sympy.simplify(jac[0, 1] - 1 / q2) == 0

    def test_induced_source_linear(self):
        q1, q2 = sympy.symbols("q1 q2")
        S = sympy.Symbol("S")
        proj = ProjectionMap(
            id="test",
            variables=[q1, q2],
            a_expr=q1,
            b_expr=q2,
        )
        J_a, J_b = proj.induced_source({q1: S, q2: -S})
        assert J_a == S
        assert J_b == -S

    def test_induced_source_with_coefficients(self):
        q1, q2 = sympy.symbols("q1 q2")
        alpha, beta = sympy.symbols("alpha beta")
        S = sympy.Symbol("S")
        proj = ProjectionMap(
            id="test",
            variables=[q1, q2],
            a_expr=alpha * q1 + beta * q2,
            b_expr=beta * q1 + alpha * q2,
        )
        J_a, J_b = proj.induced_source({q1: S, q2: -S})
        assert sympy.simplify(J_a - (alpha - beta) * S) == 0
        assert sympy.simplify(J_b - (beta - alpha) * S) == 0

    def test_missing_delta_defaults_to_zero(self):
        q1, q2 = sympy.symbols("q1 q2")
        S = sympy.Symbol("S")
        proj = ProjectionMap(
            id="test",
            variables=[q1, q2],
            a_expr=q1,
            b_expr=q2,
        )
        # Only delta q1 given, q2 defaults to 0
        J_a, J_b = proj.induced_source({q1: S})
        assert J_a == S
        assert J_b == 0


# ============================================================
# Classification tests
# ============================================================


class TestAnalyzerClassification:
    """Test source classification through the analyzer."""

    def test_antisymmetric_exchange_is_trace_free(self):
        structure = two_channel_exchange()
        analyzer = StructureAnalyzer()
        result = analyzer.analyze(structure)

        assert len(result.exchange_results) == 1
        ex = result.exchange_results[0]
        assert ex.classification == "trace_free"
        assert sympy.simplify(ex.J_kappa) == 0

    def test_symmetric_creation_is_pure_trace(self):
        structure = two_channel_exchange()
        analyzer = StructureAnalyzer()
        result = analyzer.analyze(structure)

        assert len(result.creation_results) == 1
        cr = result.creation_results[0]
        assert cr.classification == "pure_trace"
        assert sympy.simplify(cr.J_sigma) == 0

    def test_mixed_exchange_fails(self):
        structure = mixed_exchange_family()
        analyzer = StructureAnalyzer()
        result = analyzer.analyze(structure)

        assert len(result.exchange_results) == 1
        ex = result.exchange_results[0]
        # One-sided exchange: J_a = S, J_b = 0
        # J_kappa = S, J_sigma = S -> mixed
        assert ex.classification == "mixed"
        assert ex.status == StructureStatus.FAILED

    def test_zero_operator(self):
        q1, q2 = sympy.symbols("q1 q2")
        proj = ProjectionMap(
            id="test",
            variables=[q1, q2],
            a_expr=q1,
            b_expr=q2,
        )
        exchange = SourceOperator(
            id="zero_exchange",
            kind="exchange",
            deltas={q1: sympy.Integer(0), q2: sympy.Integer(0)},
            source_symbols=[],
        )
        structure = VacuumStructure(
            id="zero_test",
            variables=[q1, q2],
            projection=proj,
            exchange_operators=[exchange],
        )
        analyzer = StructureAnalyzer()
        result = analyzer.analyze(structure)
        ex = result.exchange_results[0]
        assert ex.classification == "zero"
        assert ex.status == StructureStatus.FAILED


# ============================================================
# Leak detection tests
# ============================================================


class TestLeakDetection:
    """Test assumption leak detection for structure search."""

    def test_direct_mode_basis_is_tautological(self):
        structure = direct_mode_basis()
        analyzer = StructureAnalyzer()
        result = analyzer.analyze(structure)

        # The direct mode basis defines exchange as delta kappa = 0
        # The projection has a+b = 2*kappa, independent of sigma
        # But since delta kappa = 0, J_kappa = 0 is structurally guaranteed
        # by the Jacobian sum being nonzero — actually the leak check
        # looks at the sum of Jacobian rows
        assert result.summary_status == StructureStatus.TAUTOLOGICAL
        assert any("LEAK" in w for w in result.leak_warnings)

    def test_symmetric_antisymmetric_pair_is_tautological(self):
        structure = symmetric_antisymmetric_pair()
        analyzer = StructureAnalyzer()
        result = analyzer.analyze(structure)

        # Same structure as direct mode basis — also tautological
        assert result.summary_status == StructureStatus.TAUTOLOGICAL

    def test_two_channel_is_not_tautological(self):
        structure = two_channel_exchange()
        analyzer = StructureAnalyzer()
        result = analyzer.analyze(structure)

        # Two-channel with a=q_t, b=q_x: projection sum row = [1, 1]
        # NOT zero, so not tautological via the sum-row check.
        # Trace-free exchange comes from antisymmetric operator.
        assert result.summary_status == StructureStatus.DERIVED
        assert result.derived_trace_free_exchange is True
        assert not result.leak_warnings


# ============================================================
# Constraint solving tests
# ============================================================


class TestConstraintSolving:
    """Test conditional trace-free solve and traceful check."""

    def test_trace_free_identity(self):
        S = sympy.Symbol("S")
        result = solve_trace_free_conditions(sympy.Integer(0), [S])
        assert result.solvable is True

    def test_trace_free_with_condition(self):
        alpha, beta = sympy.symbols("alpha beta")
        S = sympy.Symbol("S")
        J_kappa = (alpha + beta) * S
        result = solve_trace_free_conditions(J_kappa, [S])
        assert result.solvable is True
        assert len(result.conditions) > 0
        # Should require alpha + beta = 0
        found = False
        for cond in result.conditions:
            if isinstance(cond, sympy.Eq):
                diff = sympy.simplify(cond.lhs - cond.rhs)
                # Check if condition is alpha = -beta or beta = -alpha
                if sympy.simplify(diff - (alpha + beta)) == 0:
                    found = True
                elif sympy.simplify(diff + (alpha + beta)) == 0:
                    found = True
                # Also check if one symbol was solved in terms of the other
                if cond.lhs == alpha and sympy.simplify(cond.rhs + beta) == 0:
                    found = True
                if cond.lhs == beta and sympy.simplify(cond.rhs + alpha) == 0:
                    found = True
        assert found, f"Expected alpha + beta = 0 condition, got {result.conditions}"

    def test_traceful_nonzero(self):
        C = sympy.Symbol("C")
        J_kappa = 2 * C
        result = check_traceful_condition(J_kappa, [C])
        assert result.solvable is True

    def test_traceful_zero_fails(self):
        C = sympy.Symbol("C")
        result = check_traceful_condition(sympy.Integer(0), [C])
        assert result.solvable is False

    def test_general_linear_conditions(self):
        """Test the general linear family reveals the trace-free condition."""
        structure = general_linear_projection(n_vars=2)
        analyzer = StructureAnalyzer()
        result = analyzer.analyze(structure)

        # Should be conditional — needs coefficient constraints
        assert result.summary_status in (
            StructureStatus.CONDITIONAL,
            StructureStatus.UNDETERMINED,
        )


# ============================================================
# Family tests
# ============================================================


class TestFamilies:
    """Test built-in candidate structure families."""

    def test_two_channel_derives_trace_free(self):
        structure = two_channel_exchange()
        analyzer = StructureAnalyzer()
        result = analyzer.analyze(structure)

        assert result.derived_trace_free_exchange is True
        assert result.derived_traceful_creation is True

        # Check specific values
        S = sympy.Symbol("S")
        C = sympy.Symbol("C")
        ex = result.exchange_results[0]
        assert sympy.simplify(ex.J_kappa) == 0
        assert sympy.simplify(ex.J_sigma - 2 * S) == 0

        cr = result.creation_results[0]
        assert sympy.simplify(cr.J_kappa - 2 * C) == 0
        assert sympy.simplify(cr.J_sigma) == 0

    def test_conserved_volume_derives_trace_free(self):
        structure = conserved_volume_family()
        analyzer = StructureAnalyzer()
        result = analyzer.analyze(structure)

        # Same operator structure as two-channel antisymmetric
        assert result.derived_trace_free_exchange is True

    def test_mixed_exchange_fails(self):
        structure = mixed_exchange_family()
        analyzer = StructureAnalyzer()
        result = analyzer.analyze(structure)

        assert result.summary_status == StructureStatus.FAILED
        assert result.derived_trace_free_exchange is False
        assert len(result.failures) > 0


# ============================================================
# Search engine tests
# ============================================================


class TestSearchEngine:
    """Test the StructureSearchEngine."""

    def test_analyze_single(self):
        engine = StructureSearchEngine()
        structure = two_channel_exchange()
        result = engine.analyze(structure)
        assert result.summary_status == StructureStatus.DERIVED

    def test_search_family(self):
        engine = StructureSearchEngine()
        family = two_channel_exchange()
        fam_result = engine.search_family(family)
        assert fam_result.candidates_analyzed == 1
        assert len(fam_result.trace_free_derived) == 1

    def test_search_family_failing(self):
        engine = StructureSearchEngine()
        family = mixed_exchange_family()
        fam_result = engine.search_family(family)
        assert len(fam_result.failed) == 1

    def test_enumerate_sign_patterns(self):
        engine = StructureSearchEngine()
        fam_result = engine.enumerate_sign_patterns(n_vars=2)

        # 3^2 - 1 = 8 candidates (excluding (0,0))
        assert fam_result.candidates_analyzed == 8

        # Only antisymmetric patterns should derive trace-free:
        # (1, -1) and (-1, 1) give J_kappa = 0
        assert len(fam_result.trace_free_derived) == 2

        # (0, S) and (S, 0) type patterns should fail
        assert len(fam_result.failed) > 0

    def test_summary(self):
        engine = StructureSearchEngine()
        engine.analyze(two_channel_exchange())
        engine.analyze(mixed_exchange_family())
        summary = engine.summary()
        assert "two_channel_exchange" in summary
        assert "mixed_exchange_family" in summary


# ============================================================
# Downstream integration tests
# ============================================================


class TestDownstreamIntegration:
    """Test feeding derived sources into existing VacuumForge pipeline."""

    def test_derived_source_feeds_into_context(self):
        from vacuumforge import TheoryContext

        ctx = TheoryContext("downstream_test")
        ctx.define_equal_response_algebraic_symbols()

        structure = two_channel_exchange()
        result = ctx.structure_search.analyze(structure, ctx)

        assert result.derived_trace_free_exchange is True

        # Check that a derived source was registered
        source_id = f"derived_exchange_from_{structure.id}"
        assert ctx.sources.has(source_id)

        src = ctx.sources.get(source_id)
        assert src.assumed_trace_free is False
        assert src.source_type == "exchange"
        assert sympy.simplify(src.J_kappa) == 0

    def test_full_chain_reciprocal_scaling(self):
        """End-to-end: structure -> trace-free -> energy -> kappa=0 -> AB=1 -> gamma=1."""
        from vacuumforge import TheoryContext

        ctx = TheoryContext("full_chain_test")
        ms = ctx.define_equal_response_algebraic_symbols()

        # 1. Analyze structure
        structure = two_channel_exchange()
        result = ctx.structure_search.analyze(structure, ctx)
        assert result.derived_trace_free_exchange is True

        # 2. Define energy functional
        ctx.energy.source_coupled(
            C_kappa=ms.C_kappa, C_sigma=ms.C_sigma,
            J_kappa=ms.J_kappa, J_sigma=ms.J_sigma,
            kappa=ms.kappa, sigma=ms.sigma,
        )

        # 3. Solve stationary with J_kappa = 0
        sol = ctx.energy.solve_stationary(
            "source_coupled_energy",
            extra_subs={ms.J_kappa: 0},
        )
        assert len(sol.solutions) > 0
        kappa_val = sol.solutions[0][ms.kappa]
        assert sympy.simplify(kappa_val) == 0

        # 4. Set up assumptions for metric
        ctx.assumptions.add("A_redshift", sympy.Eq(ms.A, sympy.exp(ms.Phi / ms.c**2)))
        ctx.assumptions.add("B_reciprocal", sympy.Eq(ms.B, 1 / ms.A))

        # 5. Check reciprocal scaling
        check = ctx.checks.reciprocal_scaling()
        assert check.status == "pass"

        # 6. Extract gamma_v
        A_val = ctx.assumptions.apply(ms.A)
        B_val = ctx.assumptions.apply(ms.B)
        metric = ctx.metric.from_scale_factors(A_val, B_val)
        gamma = ctx.ppn.extract_gamma(metric)
        assert sympy.simplify(gamma.value - 1) == 0


# ============================================================
# Report tests
# ============================================================


class TestReports:
    """Test report generation for structure search."""

    def test_report_generation(self):
        structure = two_channel_exchange()
        analyzer = StructureAnalyzer()
        result = analyzer.analyze(structure)

        report = generate_structure_report(structure, result)
        assert "Structure Search Analysis" in report
        assert "two_channel_exchange" in report
        assert "trace_free" in report
        assert "DERIVED" in report
        assert "J_\\kappa" in report

    def test_failed_report(self):
        structure = mixed_exchange_family()
        analyzer = StructureAnalyzer()
        result = analyzer.analyze(structure)

        report = generate_structure_report(structure, result)
        assert "FAILED" in report
        assert "Failures" in report

    def test_tautological_report(self):
        structure = direct_mode_basis()
        analyzer = StructureAnalyzer()
        result = analyzer.analyze(structure)

        report = generate_structure_report(structure, result)
        assert "TAUTOLOGICAL" in report
        assert "Leak" in report or "LEAK" in report


# ============================================================
# Counterexample tests
# ============================================================


class TestCounterexamples:
    """Test counterexample-style structures."""

    def test_total_conservation_does_not_force_trace_free(self):
        """Total energy conservation alone does not imply J_kappa = 0.

        A structure where exchange preserves total energy but
        deposits energy into both modes.
        """
        q1, q2 = sympy.symbols("q1 q2")
        S = sympy.Symbol("S")
        C = sympy.Symbol("C")

        # Exchange: delta q1 = S, delta q2 = 0
        # Total delta = S (conservation violated in one sense)
        # But more importantly: J_a = S, J_b = 0, J_kappa = S != 0
        proj = ProjectionMap(
            id="counterex",
            variables=[q1, q2],
            a_expr=q1,
            b_expr=q2,
        )
        exchange = SourceOperator(
            id="one_channel_exchange",
            kind="exchange",
            deltas={q1: S, q2: sympy.Integer(0)},
            source_symbols=[S],
        )
        structure = VacuumStructure(
            id="conservation_counterexample",
            variables=[q1, q2],
            projection=proj,
            exchange_operators=[exchange],
        )

        analyzer = StructureAnalyzer()
        result = analyzer.analyze(structure)

        # Exchange is NOT trace-free
        assert result.derived_trace_free_exchange is False
        assert result.exchange_results[0].classification == "mixed"

    def test_parallel_scaling_failure(self):
        """Parallel scaling: exchange symmetric => J_sigma = 0, J_kappa != 0."""
        q_t, q_x = sympy.symbols("q_t q_x")
        S = sympy.Symbol("S")

        proj = ProjectionMap(
            id="parallel",
            variables=[q_t, q_x],
            a_expr=q_t,
            b_expr=q_x,
        )
        exchange = SourceOperator(
            id="symmetric_exchange",
            kind="exchange",
            deltas={q_t: S, q_x: S},
            source_symbols=[S],
        )
        structure = VacuumStructure(
            id="parallel_scaling",
            variables=[q_t, q_x],
            projection=proj,
            exchange_operators=[exchange],
        )

        analyzer = StructureAnalyzer()
        result = analyzer.analyze(structure)

        ex = result.exchange_results[0]
        assert ex.classification == "pure_trace"
        assert ex.status == StructureStatus.FAILED
        # J_kappa = 2S, J_sigma = 0
        assert sympy.simplify(ex.J_kappa - 2 * S) == 0
        assert sympy.simplify(ex.J_sigma) == 0
