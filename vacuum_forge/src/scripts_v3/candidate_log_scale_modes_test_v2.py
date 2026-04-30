# Candidate log-scale exterior modes v2: derive-record-validate forge test
#
# Purpose
# -------
# This is the v2 VacuumForge test for candidate_log_scale_exterior_modes.md.
#
# v1 confirmed:
#   - kappa is the reduced reciprocal-scaling mode because AB = exp(2*kappa).
#   - kappa = 0 implies AB = 1.
#   - AB = 1 implies gamma_v = 1 under the weak-field gamma ansatz.
#   - directly setting delta_kappa = 0 is tautological.
#   - structural pre-mode exchange can derive J_kappa = 0.
#   - a kappa-sourced toy energy gives kappa != 0 and AB != 1.
#
# v2 improves the pipeline by:
#   1. Recording derived consequences back into the context.
#   2. Rerunning validation after derived AB=1 and gamma_v=1 are registered.
#   3. Separating four cases:
#
#      Case A: Direct mode assumption
#        delta kappa = 0 is inserted directly.
#        Expected: tautological / leak warning.
#
#      Case B: Structural trace-kernel exterior
#        pre-mode exchange lies in trace kernel.
#        Expected: derived J_kappa = 0 -> kappa_eq = 0 -> AB = 1 -> gamma_v = 1.
#
#      Case C: Generic kappa-sourced exchange
#        J_kappa = J_k.
#        Expected: kappa_eq = J_k/(2*C_kappa) -> AB != 1 generically.
#
#      Case D: Interface/source-to-exterior separation toy
#        source/interface may seed shear, but source-free exterior has J_kappa = 0.
#        Expected: exterior kappa_eq = 0 while s != 0, matching P7-style exterior compensation.
#
# This script is a reduced-sector development tool. It is not a theorem,
# not a field equation, and not evidence for the full framework by itself.
#
# Suggested location:
#   scripts_v3/candidate_log_scale_modes_test_v2.py

import sympy as sp

from vacuumforge.core.context import TheoryContext
from vacuumforge.structure_search import (
    VacuumStructure,
    ProjectionMap,
    SourceOperator,
    StructureAnalyzer,
)
from vacuumforge.requirements.leak_detection import detect_leaks


# =============================================================================
# Utility helpers
# =============================================================================

def header(title: str) -> None:
    print()
    print("=" * 88)
    print(title)
    print("=" * 88)


def subheader(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


def status_line(label: str, ok: bool, detail: str = "") -> None:
    mark = "PASS" if ok else "WARN"
    if detail:
        print(f"[{mark}] {label}: {detail}")
    else:
        print(f"[{mark}] {label}")


def simplify_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


def validate_and_print(ctx: TheoryContext, name: str) -> None:
    """Run requirement validation and leak audit."""
    subheader(f"{name}: requirement validation")
    results = ctx.requirements.validate_all(ctx)
    print(ctx.requirements.summary(results))

    subheader(f"{name}: leak detection audit")
    if hasattr(ctx, "_targets") and ctx._targets is not None:
        for target_id in [
            "reciprocal_scaling",
            "kappa_zero",
            "gamma_v_one",
            "trace_free_exchange",
        ]:
            if ctx._targets.has(target_id):
                leak = detect_leaks(target_id, ctx.assumptions, ctx._targets)
                status = "LEAKED" if leak.leaked else "clean"
                print(f"  {target_id}: {status}")
                if leak.leaked:
                    print(f"    via: {leak.leaked_via}")
    else:
        print("  No target library available.")


def add_standard_metric_ansatz(ctx: TheoryContext) -> None:
    """Add weak-field ansatz A=exp(Phi/c^2), B=exp(-gamma_v Phi/c^2)."""
    ms = ctx._mode_symbols
    ctx.assumptions.add(
        "A_exp",
        sp.Eq(ms.A, sp.exp(ms.Phi / ms.c**2)),
        description="A = exp(Phi/c^2), weak-field temporal ansatz.",
    )
    ctx.assumptions.add(
        "B_free_gamma",
        sp.Eq(ms.B, sp.exp(-ms.gamma_v * ms.Phi / ms.c**2)),
        description="B = exp(-gamma_v Phi/c^2), gamma_v initially free.",
    )


def record_reciprocal_chain(ctx: TheoryContext, chain_label: str = "derived") -> bool:
    """Record kappa=0 -> AB=1 -> gamma_v=1 into context.

    This is the v2 improvement over v1: the script does not merely print the
    consequence. It registers the derived results so validation can see them.
    """
    ms = ctx._mode_symbols

    # Add kappa = 0 as a derived result/assumption.
    # Note: this is intentionally added after an energy or structural derivation.
    ctx.assumptions.add(
        f"kappa_zero_{chain_label}",
        sp.Eq(ms.kappa, 0),
        description=f"Derived in {chain_label}: exterior equilibrium has kappa = 0.",
        status="derived",
    )

    ctx.assumptions.add(
        f"reciprocal_scaling_{chain_label}",
        sp.Eq(ms.A * ms.B, 1),
        description=f"Derived in {chain_label}: kappa = 0 implies AB = 1.",
        status="derived",
    )

    # Solve gamma_v from A*B=1 under the ansatz.
    A_sub = ctx.assumptions.apply(ms.A)
    B_sub = ctx.assumptions.apply(ms.B)
    AB_expr = sp.simplify(A_sub * B_sub)

    # Use log when AB is exponential.
    try:
        gamma_solutions = sp.solve(sp.Eq(sp.log(AB_expr), 0), ms.gamma_v)
    except Exception:
        gamma_solutions = []

    if not gamma_solutions:
        try:
            gamma_solutions = sp.solve(sp.Eq(AB_expr, 1), ms.gamma_v)
        except Exception:
            gamma_solutions = []

    if gamma_solutions:
        gamma_value = sp.simplify(gamma_solutions[0])
        ctx.assumptions.add(
            f"gamma_v_one_{chain_label}",
            sp.Eq(ms.gamma_v, gamma_value),
            description=f"Derived in {chain_label}: AB = 1 implies gamma_v = {gamma_value}.",
            status="derived",
        )
        return simplify_zero(gamma_value - 1)

    return False


# =============================================================================
# Section 1: Algebraic spine
# =============================================================================

def section_1_algebraic_spine() -> None:
    header("Section 1: Algebraic spine")

    kappa, s = sp.symbols("kappa s", real=True)
    Phi, c, gamma_v = sp.symbols("Phi c gamma_v", nonzero=True, real=True)

    A = sp.exp(kappa + s)
    B = sp.exp(kappa - s)
    AB = sp.simplify(A * B)

    print(f"A(kappa,s)  = {A}")
    print(f"B(kappa,s)  = {B}")
    print(f"AB          = {AB}")
    print(f"AB|kappa=0  = {sp.simplify(AB.subs(kappa, 0))}")

    status_line("kappa = 0 -> AB = 1", simplify_zero(AB.subs(kappa, 0) - 1))

    A_gamma = sp.exp(Phi / c**2)
    B_gamma = sp.exp(-gamma_v * Phi / c**2)
    AB_gamma = sp.simplify(A_gamma * B_gamma)
    log_AB_gamma = sp.simplify(sp.log(AB_gamma))
    gamma_solution = sp.solve(sp.Eq(log_AB_gamma, 0), gamma_v)

    print()
    print(f"A_gamma     = {A_gamma}")
    print(f"B_gamma     = {B_gamma}")
    print(f"AB_gamma    = {AB_gamma}")
    print(f"log(AB)     = {log_AB_gamma}")
    print(f"gamma_v sol = {gamma_solution}")

    ok = bool(gamma_solution) and simplify_zero(gamma_solution[0] - 1)
    status_line("AB = 1 -> gamma_v = 1 under weak-field ansatz", ok)


# =============================================================================
# Case A: direct mode-basis assumption is tautological
# =============================================================================

def case_a_tautology_control() -> None:
    header("Case A: Direct mode assumption / tautology control")

    analyzer = StructureAnalyzer()
    S, C = sp.symbols("S C", real=True)
    kappa, s = sp.symbols("kappa s", real=True)

    projection = ProjectionMap(
        id="direct_log_mode_basis",
        variables=[kappa, s],
        a_expr=kappa + s,
        b_expr=kappa - s,
        description="a = kappa + s, b = kappa - s",
    )

    exchange = SourceOperator(
        id="direct_delta_kappa_zero",
        kind="exchange",
        deltas={kappa: sp.Integer(0), s: S},
        source_symbols=[S],
        description="Directly assumes delta kappa = 0.",
    )

    creation = SourceOperator(
        id="direct_creation_kappa",
        kind="creation",
        deltas={kappa: C, s: sp.Integer(0)},
        source_symbols=[C],
        description="Creation sources kappa.",
    )

    structure = VacuumStructure(
        id="case_a_direct_mode_assumption",
        variables=[kappa, s],
        projection=projection,
        exchange_operators=[exchange],
        creation_operators=[creation],
        description="Tautology control: delta kappa = 0 inserted directly.",
    )

    result = analyzer.analyze(structure)
    print(result.summary())

    ex = result.exchange_results[0]
    print()
    print(f"J_kappa = {ex.J_kappa}")
    print(f"J_s     = {ex.J_sigma}")
    print(f"Status  = {result.summary_status.value}")

    status_line(
        "direct delta_kappa=0 classified as tautological",
        result.summary_status.value == "tautological",
    )


# =============================================================================
# Case B: structural trace-kernel exterior
# =============================================================================

def build_case_b_context() -> TheoryContext:
    """Build a context where J_kappa = 0 comes from trace-kernel structure."""
    ctx = TheoryContext("case_b_structural_trace_kernel_exterior")
    ctx.define_equal_response_algebraic_symbols()
    add_standard_metric_ansatz(ctx)
    ms = ctx._mode_symbols

    # Use the result of a structural pre-mode test as the source input:
    # J_kappa = 0, J_sigma = J_s.
    Js = sp.Symbol("J_s", real=True)

    ctx.sources.exchange_trace_free(
        Js,
        description="J_kappa = 0 supplied by structural trace-kernel exchange.",
    )
    ctx.ledger.add_derived(
        "structural_trace_kernel_exchange",
        "Pre-mode exchange lies in the trace kernel, so J_kappa = 0.",
        expression=sp.Eq(ms.J_kappa, 0),
        dependencies=["physical_3plus1_projection", "trace_kernel_exchange_direction"],
    )

    ctx.energy.source_coupled(
        C_kappa=ms.C_kappa,
        C_sigma=ms.C_sigma,
        J_kappa=sp.Integer(0),
        J_sigma=Js,
        kappa=ms.kappa,
        sigma=ms.sigma,
    )

    return ctx


def case_b_structural_trace_kernel() -> None:
    header("Case B: Structural trace-kernel exterior")

    # First show the structural pre-mode derivation directly.
    subheader("B1: pre-mode trace-kernel analyzer check")
    analyzer = StructureAnalyzer()
    S, C = sp.symbols("S C", real=True)
    q_t, q_x, q_y, q_z = sp.symbols("q_t q_x q_y q_z", real=True)

    projection = ProjectionMap(
        id="physical_3plus1_log_projection",
        variables=[q_t, q_x, q_y, q_z],
        a_expr=q_t,
        b_expr=(q_x + q_y + q_z) / 3,
        description="a = q_t, b = average spatial log scale.",
    )

    exchange = SourceOperator(
        id="isotropic_time_vs_space_exchange",
        kind="exchange",
        deltas={q_t: -S, q_x: S, q_y: S, q_z: S},
        source_symbols=[S],
        description="Trace-kernel exchange: -1 + (1+1+1)/3 = 0.",
    )

    creation = SourceOperator(
        id="symmetric_creation_31",
        kind="creation",
        deltas={q_t: C, q_x: C, q_y: C, q_z: C},
        source_symbols=[C],
        description="Symmetric creation sources trace.",
    )

    structure = VacuumStructure(
        id="case_b_physical_31_trace_kernel",
        variables=[q_t, q_x, q_y, q_z],
        projection=projection,
        exchange_operators=[exchange],
        creation_operators=[creation],
    )

    result = analyzer.analyze(structure)
    print(result.summary())

    ex = result.exchange_results[0]
    print(f"Exchange J_kappa = {ex.J_kappa}")
    print(f"Exchange J_s     = {ex.J_sigma}")
    status_line("pre-mode exchange derives J_kappa = 0", result.summary_status.value == "derived")

    # Now do the derive-record-validate chain.
    subheader("B2: energy equilibrium and recorded reciprocal chain")
    ctx = build_case_b_context()
    ms = ctx._mode_symbols
    sol = ctx.energy.solve_stationary("source_coupled_energy")

    print(f"Stationary equations: {sol.equations}")
    print(f"Solutions: {sol.solutions}")

    kappa_eq = sol.solutions[0].get(ms.kappa) if sol.solutions else None
    s_eq = sol.solutions[0].get(ms.sigma) if sol.solutions else None

    print(f"kappa_eq = {kappa_eq}")
    print(f"s_eq     = {s_eq}")

    if kappa_eq == 0:
        ok = record_reciprocal_chain(ctx, chain_label="case_b")
        status_line("recorded kappa=0 -> AB=1 -> gamma_v=1", ok)
    else:
        status_line("kappa_eq = 0", False, f"got {kappa_eq}")

    validate_and_print(ctx, "Case B")


# =============================================================================
# Case C: generic kappa-sourced exchange
# =============================================================================

def build_case_c_context() -> TheoryContext:
    ctx = TheoryContext("case_c_kappa_sourced_exchange")
    ctx.define_equal_response_algebraic_symbols()
    add_standard_metric_ansatz(ctx)
    ms = ctx._mode_symbols

    Jk, Js = sp.symbols("J_k J_s", real=True)

    ctx.sources.add_modes(
        "exchange",
        J_kappa=Jk,
        J_sigma=Js,
        source_type="exchange",
        description="Generic exchange sources kappa and shear.",
    )
    ctx.ledger.add_candidate_postulate(
        "generic_kappa_sourcing",
        "Exchange sources kappa: J_kappa = J_k.",
        expression=sp.Eq(ms.J_kappa, Jk),
    )

    ctx.energy.source_coupled(
        C_kappa=ms.C_kappa,
        C_sigma=ms.C_sigma,
        J_kappa=Jk,
        J_sigma=Js,
        kappa=ms.kappa,
        sigma=ms.sigma,
    )

    return ctx


def case_c_kappa_sourced() -> None:
    header("Case C: Generic kappa-sourced exchange")

    ctx = build_case_c_context()
    ms = ctx._mode_symbols
    sol = ctx.energy.solve_stationary("source_coupled_energy")

    print(f"Stationary equations: {sol.equations}")
    print(f"Solutions: {sol.solutions}")

    kappa_eq = sol.solutions[0].get(ms.kappa) if sol.solutions else None
    s_eq = sol.solutions[0].get(ms.sigma) if sol.solutions else None

    print(f"kappa_eq = {kappa_eq}")
    print(f"s_eq     = {s_eq}")

    if kappa_eq is not None:
        AB = sp.simplify(sp.exp(2 * kappa_eq))
        print(f"AB = exp(2*kappa_eq) = {AB}")
        status_line("generic kappa sourcing prevents AB=1", not simplify_zero(AB - 1))
    else:
        status_line("kappa equilibrium solved", False)

    validate_and_print(ctx, "Case C")


# =============================================================================
# Case D: source/interface-to-exterior separation toy
# =============================================================================

def build_case_d_context() -> TheoryContext:
    """Build source/interface-to-exterior separation context.

    This toy models the new framework's distinction:

      - Source/interface/substance-region physics may create or transform
        vacuum and may seed boundary conditions.
      - The static source-free exterior is a configuration-regime region.
      - In the exterior, J_kappa_ext = 0, while shear mode s may remain active.

    This does NOT derive the source law. It only checks that a boundary-sourced
    shear with exterior kappa suppression yields reciprocal scaling.
    """
    ctx = TheoryContext("case_d_interface_seeded_source_free_exterior")
    ctx.define_equal_response_algebraic_symbols()
    add_standard_metric_ansatz(ctx)
    ms = ctx._mode_symbols

    S_boundary = sp.Symbol("S_boundary", real=True)

    # Exterior equation: no kappa source in the source-free region.
    # Boundary/interface seeds shear through S_boundary.
    ctx.sources.add_modes(
        "exterior_response",
        J_kappa=sp.Integer(0),
        J_sigma=S_boundary,
        source_type="exchange",
        description=(
            "Source-free exterior response: J_kappa_ext=0; "
            "interface/boundary seeds compensated shear."
        ),
    )

    ctx.ledger.add_candidate_postulate(
        "source_interface_exterior_separation",
        (
            "Source/interface may seed exterior shear, but the source-free "
            "exterior has no kappa source."
        ),
        expression=sp.Eq(ms.J_kappa, 0),
    )

    ctx.energy.source_coupled(
        C_kappa=ms.C_kappa,
        C_sigma=ms.C_sigma,
        J_kappa=sp.Integer(0),
        J_sigma=S_boundary,
        kappa=ms.kappa,
        sigma=ms.sigma,
    )

    return ctx


def case_d_interface_exterior_separation() -> None:
    header("Case D: Interface/source-to-exterior separation toy")

    ctx = build_case_d_context()
    ms = ctx._mode_symbols
    sol = ctx.energy.solve_stationary("source_coupled_energy")

    print("Interpretation:")
    print("  Source/interface may set a boundary shear amplitude.")
    print("  The exterior region itself is source-free with J_kappa_ext = 0.")
    print("  This tests whether exterior kappa suppression can coexist with s != 0.")
    print()

    print(f"Stationary equations: {sol.equations}")
    print(f"Solutions: {sol.solutions}")

    kappa_eq = sol.solutions[0].get(ms.kappa) if sol.solutions else None
    s_eq = sol.solutions[0].get(ms.sigma) if sol.solutions else None

    print(f"kappa_eq = {kappa_eq}")
    print(f"s_eq     = {s_eq}")

    if kappa_eq == 0:
        ok = record_reciprocal_chain(ctx, chain_label="case_d")
        status_line("exterior kappa suppression records AB=1 and gamma_v=1", ok)
    else:
        status_line("exterior kappa_eq = 0", False, f"got {kappa_eq}")

    if s_eq != 0:
        status_line("compensated/shear exterior mode remains active", True, f"s_eq = {s_eq}")
    else:
        status_line("compensated/shear exterior mode remains active", False, "s_eq simplified to 0")

    validate_and_print(ctx, "Case D")


# =============================================================================
# Summary
# =============================================================================

def final_summary() -> None:
    header("Final v2 interpretation")

    print("The v2 experiment distinguishes four concepts:")
    print()
    print("A. Direct mode assumption:")
    print("   Setting delta_kappa = 0 directly is tautological and should not be")
    print("   counted as a derivation.")
    print()
    print("B. Structural trace-kernel exterior:")
    print("   A pre-mode exchange direction can derive J_kappa = 0 non-tautologically.")
    print("   With the toy energy equilibrium, this gives kappa = 0, AB = 1,")
    print("   and gamma_v = 1 after derived consequences are recorded.")
    print()
    print("C. Generic kappa-sourced exchange:")
    print("   If J_kappa is nonzero, kappa_eq = J_k/(2*C_kappa), so")
    print("   AB = exp(J_k/C_kappa) and reciprocal scaling is not generic.")
    print()
    print("D. Interface/source-to-exterior separation:")
    print("   The current framework can allow source/interface physics to seed")
    print("   exterior shear while the source-free exterior suppresses kappa.")
    print("   This is the reduced-sector analogue of P7-style exterior compensation.")
    print()
    print("Main research target sharpened by the forge:")
    print()
    print("   Find a covariant source law, boundary/interface rule, or")
    print("   configuration-energy functional that suppresses kappa in the")
    print("   static source-free exterior while allowing compensated shear s.")
    print()
    print("This script still does not derive that deeper rule. It only verifies")
    print("the reduced algebraic and energy-equilibrium consequences once such")
    print("a rule is supplied.")


def main() -> None:
    header("Candidate Log-Scale Exterior Modes v2 — Derive, Record, Validate")
    section_1_algebraic_spine()
    case_a_tautology_control()
    case_b_structural_trace_kernel()
    case_c_kappa_sourced()
    case_d_interface_exterior_separation()
    final_summary()


if __name__ == "__main__":
    main()
