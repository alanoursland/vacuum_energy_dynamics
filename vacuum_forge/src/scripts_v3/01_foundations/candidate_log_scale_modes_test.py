# Candidate log-scale exterior modes: VacuumForge test script
#
# Group:
#   01_foundations
#
# Script type:
#   SAMPLE
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

from pathlib import Path

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    ClaimRecord,
    ClaimTier,
    GovernanceStatus,
    ObligationStatus,
    ProofObligationRecord,
    RecordKind,
    RouteRecord,
    ScriptOutput,
    StatusMark,
)
from vacuumforge.core.context import TheoryContext
from vacuumforge.structure_search import (
    VacuumStructure,
    ProjectionMap,
    SourceOperator,
    StructureAnalyzer,
)
from vacuumforge.requirements.leak_detection import detect_leaks


ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"


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


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    return archive, ns, invalidated


# ---------------------------------------------------------------------------
# Section 1: Pure algebra of log-scale modes
# ---------------------------------------------------------------------------

def section_1_algebraic_identity(out: ScriptOutput) -> None:
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

    kappa_zero_ab_one = is_zero(sp.simplify(AB_expr.subs(kappa, 0) - 1))

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

    gamma_v_one = bool(gamma_solution and sp.simplify(gamma_solution[0] - 1) == 0)

    with out.derived_results():
        out.line(
            "kappa = 0 implies AB = 1",
            StatusMark.PASS if kappa_zero_ab_one else StatusMark.FAIL,
            f"AB|kappa=0 = {sp.simplify(AB_expr.subs(kappa, 0))}",
        )
        out.line(
            "AB = 1 implies gamma_v = 1 under weak-field ansatz",
            StatusMark.PASS if gamma_v_one else StatusMark.WARN,
            f"gamma_v solutions: {gamma_solution}",
        )

    return AB_expr, gamma_solution


# ---------------------------------------------------------------------------
# Section 2: Leak control — direct mode basis is tautological
# ---------------------------------------------------------------------------

def section_2_leak_control(out: ScriptOutput) -> None:
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

    is_tautological = result.summary_status.value == "tautological"

    with out.governance_assessments():
        out.line(
            "direct delta_kappa=0 classified as tautological",
            StatusMark.PASS if is_tautological else StatusMark.WARN,
            "direct mode assumption is leak-controlled, not a derivation",
        )


# ---------------------------------------------------------------------------
# Section 3: Structural trace-kernel exchange in physical 3+1 projection
# ---------------------------------------------------------------------------

def section_3_trace_kernel_31(out: ScriptOutput) -> None:
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

    is_derived = result.summary_status.value == "derived"

    with out.derived_results():
        out.line(
            "trace-free exchange derived from 3+1 projection kernel",
            StatusMark.PASS if is_derived else StatusMark.WARN,
            f"summary_status={result.summary_status.value}",
        )

    return is_derived


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


def section_4_energy_forks(out: ScriptOutput) -> None:
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

    kappa_tc_zero = False
    kappa_ks_nonzero = False

    if sol_tc.solutions:
        kappa_tc = sol_tc.solutions[0].get(ms_tc.kappa)
        sigma_tc = sol_tc.solutions[0].get(ms_tc.sigma)
        print(f"kappa_eq = {kappa_tc}")
        print(f"s_eq     = {sigma_tc}")

        if kappa_tc == 0:
            kappa_tc_zero = True
            print("Consequence: kappa = 0 -> AB = 1 -> gamma_v = 1 under ansatz.")

    subheader("Fork KS: kappa-sourced exterior")
    print(f"Stationary equations: {sol_ks.equations}")
    print(f"Solutions: {sol_ks.solutions}")

    if sol_ks.solutions:
        kappa_ks = sol_ks.solutions[0].get(ms_ks.kappa)
        sigma_ks = sol_ks.solutions[0].get(ms_ks.sigma)
        print(f"kappa_eq = {kappa_ks}")
        print(f"s_eq     = {sigma_ks}")

        if kappa_ks != 0:
            kappa_ks_nonzero = True
            AB_ks = sp.simplify(sp.exp(2 * kappa_ks))
            print(f"AB = exp(2*kappa_eq) = {AB_ks}")
            print("Consequence: AB != 1 generically; gamma_v is not fixed to 1.")

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

    with out.sample_results():
        out.line(
            "Fork TC: kappa_eq = 0 under trace-free exchange",
            StatusMark.PASS if kappa_tc_zero else StatusMark.WARN,
            "toy sample only; J_kappa=0 assumed not derived from source law",
        )
        out.line(
            "Fork KS: kappa_eq != 0 when exchange sources kappa",
            StatusMark.PASS if kappa_ks_nonzero else StatusMark.WARN,
            "toy sample showing AB != 1 when kappa is sourced",
        )

    with out.unresolved_obligations():
        out.line(
            "derive source law suppressing kappa in static source-free exterior",
            StatusMark.OBLIGATION,
            "toy energy fork confirms need; physical mechanism not yet derived",
        )


# ---------------------------------------------------------------------------
# Section 5: Candidate verdict
# ---------------------------------------------------------------------------

def section_5_verdict(out: ScriptOutput) -> None:
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

    with out.governance_assessments():
        out.line(
            "log-scale mode basis algebraically clean for kappa/s decomposition",
            StatusMark.PASS,
            "kappa=0 exactly encodes AB=1; basis is structurally sound",
        )
        out.line(
            "trace-kernel exchange route is candidate, not licensed",
            StatusMark.DEFER,
            "J_kappa=0 derivable from trace-kernel structure; physical source law open",
        )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    header("Candidate Log-Scale Exterior Modes — VacuumForge Test")
    archive, ns, invalidated = prepare_archive()
    if invalidated:
        print("[INFO] Archive invalidated due to source change.")

    out = ScriptOutput()

    section_1_algebraic_identity(out)
    section_2_leak_control(out)
    section_3_trace_kernel_31(out)
    section_4_energy_forks(out)
    section_5_verdict(out)

    kappa, s = sp.symbols("kappa s", real=True)
    A_expr = sp.exp(kappa + s)
    B_expr = sp.exp(kappa - s)
    AB_expr = sp.simplify(A_expr * B_expr)
    kappa_zero_residual = sp.simplify(AB_expr.subs(kappa, 0) - 1)

    ns.record_derivation(
        derivation_id="kappa_zero_implies_AB_one_residual",
        inputs=[kappa, s],
        output=sp.Eq(kappa_zero_residual, 0),
        method="simplify(exp(2*kappa)|kappa=0 - 1)",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="identity_residual",
    )

    Phi, c, gamma_v = sp.symbols("Phi c gamma_v", nonzero=True, real=True)
    A_ansatz = sp.exp(Phi / c**2)
    B_ansatz = sp.exp(-gamma_v * Phi / c**2)
    AB_ansatz = sp.simplify(A_ansatz * B_ansatz)
    log_AB = sp.simplify(sp.log(AB_ansatz))

    ns.record_derivation(
        derivation_id="weak_field_gamma_v_from_reciprocal_scaling",
        inputs=[A_ansatz, B_ansatz],
        output=sp.Eq(log_AB, 0),
        method="log(A_ansatz*B_ansatz) = 0 under AB=1",
        status=Status.DERIVED,
        record_kind=RecordKind.SAMPLE_DERIVATION,
        scope="weak-field ansatz only; gamma_v not derived from source law",
    )

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_kappa_suppression_source_law",
        script_id=SCRIPT_ID,
        title="Derive source law suppressing kappa in static source-free exterior",
        status=ObligationStatus.OPEN,
        required_by=["trace_kernel_kappa_suppression_route"],
        description=(
            "Find a covariant source law, boundary/interface rule, or "
            "configuration-energy functional that suppresses kappa in the "
            "static source-free exterior without assuming reciprocal scaling "
            "by hand. Toy energy forks confirm the need but do not supply "
            "the physical mechanism."
        ),
    ))

    ns.record_route(RouteRecord(
        route_id="trace_kernel_kappa_suppression_route",
        script_id=SCRIPT_ID,
        name="Trace-kernel exchange derives J_kappa = 0",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=["derive_kappa_suppression_source_law"],
        description=(
            "A pre-mode exchange direction lying in the trace kernel of the "
            "3+1 projection derives J_kappa = 0 non-tautologically. "
            "With a toy quadratic energy this gives kappa=0 and AB=1. "
            "Physical source law remains open."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="direct_mode_assumption_is_tautological",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Setting delta_kappa = 0 directly in the log-mode basis is "
            "tautological and does not count as a derivation of kappa suppression."
        ),
    ))

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
