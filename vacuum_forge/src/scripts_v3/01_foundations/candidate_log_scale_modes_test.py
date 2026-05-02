# Candidate log-scale exterior modes: VacuumForge test script
#
# Purpose
# -------
# This script tests the algebraic core of candidate_log_scale_exterior_modes.md.
#
# It is NOT a proof of the framework.
# It is a reduced-sector sanity test for the candidate mode language:
#
#   a = ln A
#   b = ln B
#   kappa = (a + b)/2     conformal / uncompensated / measure mode
#   s     = (a - b)/2     shear / compensated / reciprocal mode
#
# Target:
#   Static source-free exterior compensation should suppress kappa while
#   allowing the shear/compensated mode s.
#
# In this reduced sector:
#
#   kappa = 0  ->  a + b = 0  ->  A B = 1
#
# With weak-field metric ansatz:
#
#   A = exp(Phi/c^2)
#   B = exp(-gamma_v Phi/c^2)
#
# reciprocal scaling AB = 1 implies:
#
#   gamma_v = 1
#
# This script checks:
#
#   1. Algebraic identity: kappa = 0 implies AB = 1.
#   2. Leak control: directly assuming delta_kappa = 0 is tautological.
#   3. Structural source rule: exchange in the trace kernel derives J_kappa = 0.
#   4. Toy energy forks:
#        TC: J_kappa = 0    -> kappa_eq = 0 -> AB = 1 -> gamma_v = 1
#        KS: J_kappa != 0  -> kappa_eq != 0 -> AB != 1 -> gamma_v free
#
# Expected pedagogical result:
#   The log-scale candidate is algebraically clean, but the crucial physics
#   remains the source/energy reason why the static source-free exterior has
#   J_kappa = 0 or otherwise suppresses kappa.
#
# Suggested location:
#   scripts/dev/candidate_log_scale_modes_test.py

import sympy as sp

from vacuumforge.core.context import TheoryContext
from vacuumforge.structure_search import (
    VacuumStructure,
    ProjectionMap,
    SourceOperator,
    StructureAnalyzer,
)
from vacuumforge.requirements.leak_detection import detect_leaks


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def header(title: str) -> None:
    print()
    print("=" * 78)
    print(title)
    print("=" * 78)


def subheader(title: str) -> None:
    print()
    print("-" * 78)
    print(title)
    print("-" * 78)


def is_zero(expr) -> bool:
    """Conservative symbolic zero check with a simplification fallback."""
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


# ---------------------------------------------------------------------------
# Section 1: Pure algebra of log-scale modes
# ---------------------------------------------------------------------------

def section_1_algebraic_identity() -> None:
    header("Section 1: Algebraic identity")

    A, B, a, b, kappa, s = sp.symbols("A B a b kappa s", positive=True, real=True)

    # Definitions:
    #   a = ln A, b = ln B
    #   kappa = (a+b)/2, s = (a-b)/2
    #
    # Invert:
    #   a = kappa + s
    #   b = kappa - s
    #   A = exp(kappa+s)
    #   B = exp(kappa-s)
    A_expr = sp.exp(kappa + s)
    B_expr = sp.exp(kappa - s)
    AB_expr = sp.simplify(A_expr * B_expr)

    print(f"A = {A_expr}")
    print(f"B = {B_expr}")
    print(f"AB = {AB_expr}")
    print(f"AB | kappa=0 = {sp.simplify(AB_expr.subs(kappa, 0))}")

    if is_zero(sp.simplify(AB_expr.subs(kappa, 0) - 1)):
        print("PASS: kappa = 0 implies AB = 1.")
    else:
        print("FAIL: kappa = 0 did not simplify to AB = 1.")

    # Weak-field gamma_v extraction.
    Phi, c, gamma_v = sp.symbols("Phi c gamma_v", nonzero=True, real=True)

    A_ansatz = sp.exp(Phi / c**2)
    B_ansatz = sp.exp(-gamma_v * Phi / c**2)
    AB_ansatz = sp.simplify(A_ansatz * B_ansatz)

    print()
    print("Weak-field ansatz:")
    print(f"  A = {A_ansatz}")
    print(f"  B = {B_ansatz}")
    print(f"  AB = {AB_ansatz}")

    # AB = 1 -> log(AB)=0 -> (1-gamma_v)*Phi/c^2 = 0.
    log_AB = sp.simplify(sp.log(AB_ansatz))
    gamma_solution = sp.solve(sp.Eq(log_AB, 0), gamma_v)

    print(f"  log(AB) = {log_AB}")
    print(f"  gamma_v solutions from AB=1: {gamma_solution}")

    if gamma_solution and sp.simplify(gamma_solution[0] - 1) == 0:
        print("PASS: AB = 1 implies gamma_v = 1 under the ansatz.")
    else:
        print("WARN: gamma_v was not solved cleanly. Check assumptions / SymPy simplification.")


# ---------------------------------------------------------------------------
# Section 2: Leak control — direct mode basis is tautological
# ---------------------------------------------------------------------------

def section_2_leak_control() -> None:
    header("Section 2: Leak control — direct mode basis")

    analyzer = StructureAnalyzer()
    S, C = sp.symbols("S C", real=True)
    kappa, s = sp.symbols("kappa s", real=True)

    # Projection in direct mode basis:
    #   a = kappa + s
    #   b = kappa - s
    #
    # If we define exchange by setting delta kappa = 0 directly, then
    # trace-freedom is inserted by hand. The analyzer should classify this
    # as tautological or leak-like, not as a structural derivation.
    projection = ProjectionMap(
        id="direct_log_mode_basis",
        variables=[kappa, s],
        a_expr=kappa + s,
        b_expr=kappa - s,
        description="a = kappa + s, b = kappa - s",
    )

    exchange = SourceOperator(
        id="assumed_shear_exchange",
        kind="exchange",
        deltas={kappa: sp.Integer(0), s: S},
        source_symbols=[S],
        description="Assumes delta kappa = 0 directly; should be tautological.",
    )

    creation = SourceOperator(
        id="conformal_creation",
        kind="creation",
        deltas={kappa: C, s: sp.Integer(0)},
        source_symbols=[C],
        description="Creation sources kappa.",
    )

    structure = VacuumStructure(
        id="direct_log_mode_basis_control",
        variables=[kappa, s],
        projection=projection,
        exchange_operators=[exchange],
        creation_operators=[creation],
        description="Tautological control for log-scale exterior mode language.",
    )

    result = analyzer.analyze(structure)
    print(result.summary())

    ex = result.exchange_results[0]
    print()
    print(f"J_kappa = {ex.J_kappa}")
    print(f"J_sigma/shear = {ex.J_sigma}")
    print(f"Status: {result.summary_status.value}")
    print(f"Classification: {ex.classification}")

    if result.leak_warnings:
        print()
        print("Leak warnings:")
        for warning in result.leak_warnings:
            print(f"  - {warning}")

    if result.summary_status.value == "tautological":
        print("PASS: direct delta_kappa=0 was identified as tautological.")
    else:
        print("WARN: expected tautological classification. Inspect analyzer behavior.")


# ---------------------------------------------------------------------------
# Section 3: Structural trace-kernel exchange in physical 3+1 projection
# ---------------------------------------------------------------------------

def section_3_trace_kernel_31() -> None:
    header("Section 3: Structural trace-kernel exchange in physical 3+1")

    analyzer = StructureAnalyzer()
    S, C = sp.symbols("S C", real=True)
    q_t, q_x, q_y, q_z = sp.symbols("q_t q_x q_y q_z", real=True)

    # Physical 3+1 reduced projection:
    #   a = q_t
    #   b = average spatial log scale = (q_x + q_y + q_z)/3
    #
    # Trace vector:
    #   [1, 1/3, 1/3, 1/3]
    #
    # Trace-free exchange condition:
    #   e_t + (e_x + e_y + e_z)/3 = 0
    #
    # Isotropic time-vs-space exchange:
    #   (-S, +S, +S, +S)
    #
    # Check:
    #   -1 + (1+1+1)/3 = 0
    projection = ProjectionMap(
        id="physical_3plus1_log_projection",
        variables=[q_t, q_x, q_y, q_z],
        a_expr=q_t,
        b_expr=(q_x + q_y + q_z) / 3,
        description="a = q_t, b = average spatial log scale",
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
        description="Symmetric creation sources the trace.",
    )

    structure = VacuumStructure(
        id="physical_31_trace_kernel",
        variables=[q_t, q_x, q_y, q_z],
        projection=projection,
        exchange_operators=[exchange],
        creation_operators=[creation],
        description="Physical 3+1 projection with exchange in trace kernel.",
    )

    result = analyzer.analyze(structure)
    print(result.summary())

    jac = projection.jacobian()
    trace_vec = jac.row(0) + jac.row(1)

    print()
    print(f"Jacobian: {jac.tolist()}")
    print(f"Trace vector: {trace_vec.tolist()}")

    ex = result.exchange_results[0]
    cr = result.creation_results[0]

    print()
    print("Exchange:")
    print(f"  J_a     = {ex.J_a}")
    print(f"  J_b     = {ex.J_b}")
    print(f"  J_kappa = {ex.J_kappa}")
    print(f"  J_s     = {ex.J_sigma}")
    print(f"  status  = {ex.status}")
    print(f"  classification = {ex.classification}")

    print()
    print("Creation:")
    print(f"  J_a     = {cr.J_a}")
    print(f"  J_b     = {cr.J_b}")
    print(f"  J_kappa = {cr.J_kappa}")
    print(f"  J_s     = {cr.J_sigma}")
    print(f"  status  = {cr.status}")
    print(f"  classification = {cr.classification}")

    if result.summary_status.value == "derived":
        print()
        print("PASS: trace-free exchange is structurally derived from the projection kernel.")
    else:
        print()
        print("WARN: expected derived status. Inspect classification and leak warnings.")


# ---------------------------------------------------------------------------
# Section 4: Toy energy forks for kappa suppression vs kappa sourcing
# ---------------------------------------------------------------------------

def build_energy_context_tc() -> TheoryContext:
    """Trace-conservation toy: J_kappa = 0."""
    ctx = TheoryContext("candidate_log_modes_tc")
    ms = ctx.define_equal_response_algebraic_symbols()

    Phi, Js = ms.Phi, sp.Symbol("J_s", real=True)

    # Metric ansatz with free gamma_v.
    ctx.assumptions.add(
        "A_exp",
        sp.Eq(ms.A, sp.exp(Phi / ms.c**2)),
        description="A = exp(Phi/c^2) from Newtonian temporal response.",
    )
    ctx.assumptions.add(
        "B_free_gamma",
        sp.Eq(ms.B, sp.exp(-ms.gamma_v * Phi / ms.c**2)),
        description="B = exp(-gamma_v Phi/c^2), gamma_v to be determined.",
    )

    # Candidate source rule: local exterior exchange has no kappa source.
    ctx.sources.exchange_trace_free(Js, description="Candidate exterior exchange: J_kappa = 0")
    ctx.ledger.add_candidate_postulate(
        "candidate_kappa_suppression",
        "Static source-free exterior exchange does not source kappa.",
        expression=sp.Eq(ms.J_kappa, 0),
    )

    # Toy energy:
    #   E = C_kappa*kappa^2 + C_sigma*sigma^2 - J_kappa*kappa - J_sigma*sigma
    # With J_kappa = 0, equilibrium should give kappa = 0.
    ctx.energy.source_coupled(
        C_kappa=ms.C_kappa,
        C_sigma=ms.C_sigma,
        J_kappa=sp.Integer(0),
        J_sigma=Js,
        kappa=ms.kappa,
        sigma=ms.sigma,
    )

    return ctx


def build_energy_context_ks() -> TheoryContext:
    """Kappa-sourced toy: J_kappa != 0."""
    ctx = TheoryContext("candidate_log_modes_kappa_sourced")
    ms = ctx.define_equal_response_algebraic_symbols()

    Phi = ms.Phi
    Jk, Js = sp.symbols("J_k J_s", real=True)

    # Same metric ansatz.
    ctx.assumptions.add(
        "A_exp",
        sp.Eq(ms.A, sp.exp(Phi / ms.c**2)),
        description="A = exp(Phi/c^2) from Newtonian temporal response.",
    )
    ctx.assumptions.add(
        "B_free_gamma",
        sp.Eq(ms.B, sp.exp(-ms.gamma_v * Phi / ms.c**2)),
        description="B = exp(-gamma_v Phi/c^2), gamma_v to be determined.",
    )

    # Alternative source rule: exchange sources kappa.
    ctx.sources.add_modes(
        "exchange",
        J_kappa=Jk,
        J_sigma=Js,
        source_type="exchange",
        description="Alternative exchange: J_kappa = J_k != 0.",
    )
    ctx.ledger.add_candidate_postulate(
        "candidate_kappa_sourcing",
        "Static exterior exchange sources kappa.",
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


def section_4_energy_forks() -> None:
    header("Section 4: Toy energy forks")

    ctx_tc = build_energy_context_tc()
    ctx_ks = build_energy_context_ks()

    ms_tc = ctx_tc._mode_symbols
    ms_ks = ctx_ks._mode_symbols

    sol_tc = ctx_tc.energy.solve_stationary("source_coupled_energy")
    sol_ks = ctx_ks.energy.solve_stationary("source_coupled_energy")

    subheader("Fork TC: kappa-suppressed / trace-conserving exterior")
    print(f"Stationary equations: {sol_tc.equations}")
    print(f"Solutions: {sol_tc.solutions}")

    if sol_tc.solutions:
        kappa_tc = sol_tc.solutions[0].get(ms_tc.kappa)
        sigma_tc = sol_tc.solutions[0].get(ms_tc.sigma)
        print(f"kappa_eq = {kappa_tc}")
        print(f"s_eq     = {sigma_tc}")

        if kappa_tc == 0:
            print("PASS: kappa_eq = 0.")
            print("Consequence: kappa = 0 -> AB = 1 -> gamma_v = 1 under ansatz.")
        else:
            print("FAIL/WARN: expected kappa_eq = 0.")

    subheader("Fork KS: kappa-sourced exterior")
    print(f"Stationary equations: {sol_ks.equations}")
    print(f"Solutions: {sol_ks.solutions}")

    if sol_ks.solutions:
        kappa_ks = sol_ks.solutions[0].get(ms_ks.kappa)
        sigma_ks = sol_ks.solutions[0].get(ms_ks.sigma)
        print(f"kappa_eq = {kappa_ks}")
        print(f"s_eq     = {sigma_ks}")

        if kappa_ks != 0:
            AB_ks = sp.simplify(sp.exp(2 * kappa_ks))
            print(f"AB = exp(2*kappa_eq) = {AB_ks}")
            print("Consequence: AB != 1 generically; gamma_v is not fixed to 1.")
        else:
            print("WARN: kappa_eq simplified to 0; check source setup.")

    subheader("Requirement validation comparison")

    results_tc = ctx_tc.requirements.validate_all(ctx_tc)
    results_ks = ctx_ks.requirements.validate_all(ctx_ks)

    print("Fork TC:")
    print(ctx_tc.requirements.summary(results_tc))
    print()
    print("Fork KS:")
    print(ctx_ks.requirements.summary(results_ks))

    subheader("Leak detection audit")

    for ctx, name in [(ctx_tc, "Fork TC"), (ctx_ks, "Fork KS")]:
        print(f"{name}:")
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


# ---------------------------------------------------------------------------
# Section 5: Candidate verdict
# ---------------------------------------------------------------------------

def section_5_verdict() -> None:
    header("Section 5: Candidate verdict")

    print("Expected interpretation:")
    print()
    print("1. The log-scale variables are algebraically well suited to P7/P8.")
    print("   kappa = 0 is exactly the reciprocal-scaling condition AB = 1.")
    print()
    print("2. Directly imposing delta_kappa = 0 in the mode basis is tautological.")
    print("   That is useful as a leak-control check, not as a derivation.")
    print()
    print("3. A pre-mode source rule can derive J_kappa = 0 if the exchange")
    print("   direction lies in the trace kernel of the projection.")
    print()
    print("4. A toy quadratic energy functional suppresses kappa only when")
    print("   J_kappa = 0 or when some additional exterior constraint/penalty")
    print("   forces kappa = 0.")
    print()
    print("5. Therefore the candidate is useful, but the real physics target remains:")
    print()
    print("      Find a source law or configuration-energy functional that")
    print("      suppresses kappa in static source-free exterior configurations")
    print("      without assuming reciprocal scaling by hand.")
    print()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    header("Candidate Log-Scale Exterior Modes — VacuumForge Test")
    section_1_algebraic_identity()
    section_2_leak_control()
    section_3_trace_kernel_31()
    section_4_energy_forks()
    section_5_verdict()


if __name__ == "__main__":
    main()
